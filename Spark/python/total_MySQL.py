import torch
from torch import nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import gluonnlp as nlp
import numpy as np
from tqdm import tqdm, tqdm_notebook

from kobert.utils import get_tokenizer
from kobert.pytorch_kobert import get_pytorch_kobert_model

from transformers import AdamW
from transformers.optimization import get_cosine_schedule_with_warmup

from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import *
from pyspark.sql.types import *

# pytorch 에서 cpu 사용 선택 
device = torch.device("cpu")

# 사전 훈련된 kobert model 불러옴
bertmodel, vocab = get_pytorch_kobert_model()

# 데이터 셋 클래스 선언
class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, max_len,
                 pad, pair):
        transform = nlp.data.BERTSentenceTransform(
            bert_tokenizer, max_seq_length=max_len, pad=pad, pair=pair)

        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i], ))

    def __len__(self):
        return (len(self.labels))
    
# 모델 파라미터 설정
max_len = 64
batch_size = 64
warmup_ratio = 0.1
num_epochs = 10
max_grad_norm = 1
log_interval = 200
learning_rate =  5e-5

# 분류에 사용할 모델 클래스 선언
class BERTClassifier(nn.Module):
    def __init__(self,
                 bert,
                 hidden_size = 768,
                 num_classes=3,
                 dr_rate=None,
                 params=None):
        super(BERTClassifier, self).__init__()
        self.bert = bert
        self.dr_rate = dr_rate
                 
        self.classifier = nn.Linear(hidden_size , num_classes)
        if dr_rate:
            self.dropout = nn.Dropout(p=dr_rate)
    
    def gen_attention_mask(self, token_ids, valid_length):
        attention_mask = torch.zeros_like(token_ids)
        for i, v in enumerate(valid_length):
            attention_mask[i][:v] = 1
        return attention_mask.float()

    def forward(self, token_ids, valid_length, segment_ids):
        attention_mask = self.gen_attention_mask(token_ids, valid_length)
        
        _, pooler = self.bert(input_ids = token_ids, token_type_ids = segment_ids.long(), attention_mask = attention_mask.float().to(token_ids.device))
        if self.dr_rate:
            out = self.dropout(pooler)
        return self.classifier(out)
    
# bert모델 불러오기
model = BERTClassifier(bertmodel,  dr_rate=0.5).to(device)

# optimizer와 schedule 설정
no_decay = ['bias', 'LayerNorm.weight']
optimizer_grouped_parameters = [
    {'params': [p for n, p in model.named_parameters() if not any(nd in n for nd in no_decay)], 'weight_decay': 0.01},
    {'params': [p for n, p in model.named_parameters() if any(nd in n for nd in no_decay)], 'weight_decay': 0.0}
]

optimizer = AdamW(optimizer_grouped_parameters, lr=learning_rate)
loss_fn = nn.CrossEntropyLoss()

sentimentModel = torch.load('./sentiment_model.pt',map_location='cpu')

# kobert에서 vocab을 통해서 토큰화 진행
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

# 테스트 함수 
def predict(predict_sentence):

    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tok, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=5)
    
    # 평가 모드
    sentimentModel.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length= valid_length
        label = label.long().to(device)

        out = sentimentModel(token_ids, valid_length, segment_ids)

        test_eval=[]

        # 학습위해 변환한 분류값 초기 분류값으로 변환
        for i in out:
            logits=i
            logits = logits.detach().cpu().numpy()

            if np.argmax(logits) == 0:
                test_eval.append("긍정")
            elif np.argmax(logits) == 1:
                test_eval.append("부정")
            elif np.argmax(logits) == 2:
                test_eval.append("중립")

        return test_eval[0]

# SQL 설정
database = "TTA"
user = "root"
password  = "1234"
conf = SparkConf() \
    .setAppName("spark-sql") \
    .set("spark.driver.extraClassPath","./jars/mysql-connector-java-5.1.38.bin.jar")
sc = SparkContext.getOrCreate(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

predict_udf = udf(predict)

# 트위터 크롤링(원본, 전처리 후 문장) 데이터 불러오기
twittertbl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", "twittertbl") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

# 원본 크롤링 데이터와 감성 연결
oricrawlDF = twittertbl.withColumn("sentiment", predict_udf("word"))

# 후보자 별 감성 개수 및 candidate DB 최신화
LJMcnt = oricrawlDF.where(col("content").like("%이재명%"))
LJMcnt = LJMcnt.groupBy("sentiment").agg(count("sentiment").alias("LJMcnt"))

ACScnt = oricrawlDF.where(col("content").like("%안철수%"))
ACScnt = ACScnt.groupBy("sentiment").agg(count("sentiment").alias("ACScnt"))

YSYcnt = oricrawlDF.where(col("content").like("%윤석열%"))
YSYcnt = YSYcnt.groupBy("sentiment").agg(count("sentiment").alias("YSYcnt"))

SSJcnt = oricrawlDF.where(col("content").like("%심상정%"))
SSJcnt = SSJcnt.groupBy("sentiment").agg(count("sentiment").alias("SSJcnt"))

HGYcnt = oricrawlDF.where(col("content").like("%허경영%"))
HGYcnt = HGYcnt.groupBy("sentiment").agg(count("sentiment").alias("HGYcnt"))

candiDF = LJMcnt.join(ACScnt, ['sentiment'], 'inner')
candiDF = candiDF.join(YSYcnt, ['sentiment'], 'inner')
candiDF = candiDF.join(SSJcnt, ['sentiment'], 'inner')
candiDF = candiDF.join(HGYcnt, ['sentiment'], 'inner')

canditbl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", "canditbl") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

canditbl = canditbl.union(candiDF)

canditbl = canditbl.groupBy("sentiment")\
    .agg(sum("LJMcnt").alias("LJMcnt"),\
         sum("ACScnt").alias("ACScnt"),\
         sum("YSYcnt").alias("YSYcnt"),\
         sum("SSJcnt").alias("SSJcnt"),\
         sum("HGYcnt").alias("HGYcnt"))

canditbl.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", "canditbl") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()

# 총 감정의 개수 및 sentiment DB 최신화
sentimenttbl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", "sentimenttbl") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

sentementDF = oricrawlDF.groupBy("sentiment").count()

sentimenttbl = sentimenttbl.union(sentementDF)

sentimenttbl = sentimenttbl.groupBy("sentiment")\
    .agg(sum("count").alias("count"))

sentimenttbl.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", "sentimenttbl") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()
    
# 최신 트위터 DB 최신화
oricrawltbl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", "oricrawltbl") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

oricrawltbl = oricrawltbl.union(oricrawlDF)

if(oricrawltbl.count() > 100):
    oricrawltbl = spark.createDataFrame(oricrawltbl.tail(100), oricrawltbl.schema)
    
oricrawltbl.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", "oricrawltbl") \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()