import tweepy
from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
import socket
import json
import requests
import base64

import re
import pandas as pd
import numpy as np
from konlpy.tag import Mecab

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import math
from collections import Counter

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
from pyspark.sql.functions import col
from pyspark.sql.types import *



def preprocessing(readData):
    text = re.sub(r'http\S+', '', readData)
    text = re.sub("RT @[\w_]+: ", '', text)
    text = re.sub("@[\w_]+", '', text)
    text = re.sub("[&]+[a-z]+", '', text)
    text = re.sub("[ㄱ-ㅎㅏ-ㅣ.]+", '', text)
    text = re.sub(r"[^가-힣0-9\s?!]", '', text)
    text = text.replace('\n', ' ')
    return text

def preprocessing_mecab(readData):
    
    
    #### Tokenize
    morphs = mecab.pos(readData)

    JOSA = ["JKS", "JKC", "JKG", "JKO", "JKB", "JKV", "JKQ", "JX", "JC"]  # 조사
    SIGN = ["SF", "SE", "SSO", "SSC", "SC", "SY"]  # 문장 부호

    TERMINATION = ["EP", "EF", "EC", "ETN", "ETM"]  # 어미
    SUPPORT_VERB = ["VX"]  # 보조 용언
    NUMBER = ["SN"]

    # Remove JOSA, EOMI, etc
    morphs[:] = (morph for morph in morphs if morph[1] not in JOSA + SIGN + TERMINATION + SUPPORT_VERB)
    # Remove length-1 words
    morphs[:] = (morph for morph in morphs if not (len(morph[0]) == 1))
    # Remove Numbers
    morphs[:] = (morph for morph in morphs if morph[1] not in NUMBER)
    # Result pop-up
    result = []
    
    for morph in morphs:
        result.append(morph[0])
    result_sentence = ' '.join(result)
    
    result_sentence = re.sub("대선", '', result_sentence)

    return result_sentence	

# TF-IDF를 통해 vectorizing
def vectorization(doc):
    vector = TfidfVectorizer(max_df=30)
    X = vector.fit_transform(doc)
    X_array = X.toarray()
    print(X_array)
    return X

# K값 구하기 위한 공식 (첫 항목과 마지목 항목을 이은 선에서 각 클러스터들과의 거리를 계산)
def calc_distance(x1, y1, a, b ,c):
    d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
    print(d)
    return d

# K값 자동계산
def elbow_auto(readVector, Clusters):
    score = []
    K = range(1, Clusters)
    for i in K:
        kmeans = KMeans(n_clusters=i, init='k-means++', random_state=0)
        kmeans.fit(readVector)
        score.append(kmeans.inertia_)
    print(type(score[1]))
    # 자동 계산식
    K_end = len(score)-1
    a = score[0] - score[K_end]
    b = K[K_end] - K[0]
    c1 = K[0] * score[K_end]
    c2 = K[K_end] * score[0]
    c = c1 - c2
    distance_from_line = []

    for i in range(K_end+1):
        distance_from_line.append(
            calc_distance(K[i],score[i], a, b, c))
    
    print("통과")

    distance_max = max(distance_from_line)
    selected_K = distance_from_line.index(distance_max) + 1
    print(" ")
    print("자동으로 계산된 클러스터 개수 : "+ str(selected_K)+"\n")

    return selected_K
	
# K-means clustering 진행
def K_means_clustering(vectorDoc, c_num, doc):

    #kmeans = KMeans().setK(c_num).setSeed(1)

    km_cluster = KMeans(n_clusters=c_num, init='k-means++', random_state=0)
    km_cluster.fit(vectorDoc)
    c_label = km_cluster.labels_
    c_centers = km_cluster.cluster_centers_
    print("통과2")
    df_dict = {'word': doc,
               'cluster_label': c_label}
    doc_df = pd.DataFrame(df_dict)

    for i in range(c_num):
        print('-Clustering Label {0}-'.format(i) + '\n')
        print(doc_df.loc[doc_df['cluster_label'] == i])
        print(' ')
    result_doc = doc_df.sort_values(by=['cluster_label'])
    global kmeans_list
    kmeans_list=[]
    return result_doc

# Wordcloud 시각화
def visualization(c_doc, c_num, stopWord):
    word_doc ={}
    for k in range(0,c_num):
        s = c_doc[c_doc.cluster_label == k]
        text = s['word'].str.cat(sep=' ')
        text = text.lower()
        result = Counter(text.split())
        most_word = result.most_common(2)
        word_doc.update(dict(most_word))
        print(word_doc)
        # for i in most_word_3:
        #     word_doc=i[0]


        text =' '.join([word for word in text.split()])

        wordcloud = WordCloud(font_path='/home/hadoop/python/font/HYKANB.TTF',
                              stopwords= stopWord,
                              max_font_size=100,
                              max_words=100,
                              background_color="white").generate_from_frequencies(word_doc)
        print('Cluster: {}'.format(k+1))
        plt.figure()
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        plt.savefig('/home/hadoop/python/savefig_default.png')
	    ## image send spring boot ##
        api = 'http://219.241.120.18:8080/img'
        image_file = '/home/hadoop/python/savefig_default.png'

        with open(image_file, "rb") as f:
            im_bytes = f.read()
        im_b64 = base64.b64encode(im_bytes).decode("utf-8")

        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        payload = json.dumps({"img": im_b64})
        response = requests.post(api, data=payload, headers=headers)
	    ############################


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

def candiTblRenew():
    
    canditbl = spark.createDataFrame(
        [('긍정', LJMPoscnt, ACSPoscnt, YSYPoscnt, SSJPoscnt),
         ('부정', LJMNegcnt, ACSNegcnt, YSYNegcnt, SSJNegcnt),
         ('중립', LJMNeucnt, ACSNeucnt, YSYNeucnt, SSJNeucnt)],
        ['sentiment','LJMcnt','ACScnt','YSYcnt','SSJcnt']
    )
    
    canditbl.write.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
        .option("dbtable", "canditbl") \
        .option("user", user) \
        .option("password", password) \
        .option("driver", "com.mysql.jdbc.Driver") \
        .mode("overwrite").save()

def sentiTblRenew():
    sentimenttbl = spark.createDataFrame(
        [('긍정',senPoscnt),('부정',senNegcnt),('중립', senNeucnt)],
        ['sentiment','count']
    )

    sentimenttbl.write.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
        .option("dbtable", "sentimenttbl") \
        .option("user", user) \
        .option("password", password) \
        .option("driver", "com.mysql.jdbc.Driver") \
        .mode("overwrite").save()

def oriTblRenew():
    readDFori = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
        .option("dbtable", "readDF") \
        .option("user", user) \
        .option("password", password) \
        .option("driver", "com.mysql.jdbc.Driver") \
        .load()

    if(readDFori.count() > 1):
        oricrawltbl2 = spark.createDataFrame(readDFori.tail(1), readDFori.schema)
        oricrawltbl2.write.format("jdbc") \
            .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
            .option("dbtable", "oricrawltbl") \
            .option("user", user) \
            .option("password", password) \
            .option("driver", "com.mysql.jdbc.Driver") \
            .mode("overwrite").save()

    else:
        readDFori.write.format("jdbc") \
            .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
            .option("dbtable", "oricrawltbl") \
            .option("user", user) \
            .option("password", password) \
            .option("driver", "com.mysql.jdbc.Driver") \
            .mode("overwrite").save() 

# pytorch 에서 cpu 사용 선택 
device = torch.device("cpu")

# 사전 훈련된 kobert model 불러옴
bertmodel, vocab = get_pytorch_kobert_model()

# 모델 파라미터 설정
max_len = 64
batch_size = 64
warmup_ratio = 0.1
num_epochs = 10
max_grad_norm = 1
log_interval = 200
learning_rate =  5e-5

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

sentimentModel = torch.load('/home/hadoop/python/sentiment_model.pt',map_location='cpu')

# kobert에서 vocab을 통해서 토큰화 진행
tokenizer = get_tokenizer()
tok = nlp.data.BERTSPTokenizer(tokenizer, vocab, lower=False)

#mecab location
mecab = Mecab('/tmp/mecab-ko-dic-2.1.1-20180720/')

database = "TTA"
user = "root"
password  = "1234"

#Tweepy Api Key
consumer_key='p3yC9Lhr2dbt5l6Izr3pXFsSR'
consumer_secret='EccWuY7mBxZAhfpYVNpL6GeVIATSPb1pK33Y2x9PNt29y0UpYy'
access_token ='998580368-a8MKHoBNFKWmw8ypMgddlcdpc3OzmUkzFMrk7rMH'
access_secret='ZaAvPc02M2W7ARg9jkCYg4RRgnyv23PkwJ6YqTwcJgbHv'

#sql setting
conf = SparkConf() \
       .setAppName("spark-sql") \
       .set("spark.driver.extraClassPath","file:/home/hadoop/spark-3.1.2/jars/mysql-connector-java-5.1.38.bin.jar")

sc = SparkContext.getOrCreate(conf=conf)
sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

# sentiment Count read
readDFsen = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
        .option("dbtable", "sentimenttbl") \
        .option("user", user) \
        .option("password", password) \
        .option("driver", "com.mysql.jdbc.Driver") \
        .load()
senPoscnt = readDFsen.filter(col("sentiment") == "긍정").collect()[0]['count']
senNegcnt = readDFsen.filter(col("sentiment") == "부정").collect()[0]['count']
senNeucnt = readDFsen.filter(col("sentiment") == "중립").collect()[0]['count']

# candidate Sentiment Count read
readDFcandi = spark.read.format("jdbc") \
        .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
        .option("dbtable", "canditbl") \
        .option("user", user) \
        .option("password", password) \
        .option("driver", "com.mysql.jdbc.Driver") \
        .load()
        
LJMPoscnt = readDFcandi.filter(col("sentiment") == "긍정").collect()[0]['LJMcnt']
LJMNegcnt = readDFcandi.filter(col("sentiment") == "부정").collect()[0]['LJMcnt']
LJMNeucnt = readDFcandi.filter(col("sentiment") == "중립").collect()[0]['LJMcnt']

ACSPoscnt = readDFcandi.filter(col("sentiment") == "긍정").collect()[0]['ACScnt']
ACSNegcnt = readDFcandi.filter(col("sentiment") == "부정").collect()[0]['ACScnt']
ACSNeucnt = readDFcandi.filter(col("sentiment") == "중립").collect()[0]['ACScnt']

YSYPoscnt = readDFcandi.filter(col("sentiment") == "긍정").collect()[0]['YSYcnt']
YSYNegcnt = readDFcandi.filter(col("sentiment") == "부정").collect()[0]['YSYcnt']
YSYNeucnt = readDFcandi.filter(col("sentiment") == "중립").collect()[0]['YSYcnt']

SSJPoscnt = readDFcandi.filter(col("sentiment") == "긍정").collect()[0]['SSJcnt']
SSJNegcnt = readDFcandi.filter(col("sentiment") == "부정").collect()[0]['SSJcnt']
SSJNeucnt = readDFcandi.filter(col("sentiment") == "중립").collect()[0]['SSJcnt']


#kmeans
kmeans_list=[]

#원본 + 감정분석 DF
class TweetsListener(StreamListener):  #클라이언트 소켓을 받음
  # tweet object listens for the tweets
    def __init__(self, csocket):
        self.client_socket = csocket    # 클라이언트 소켓을 받는 생성자
    def on_data(self, data):    # 오버라이딩
        try:
            msg = json.loads( data )      # json 문자열을 딕셔너리로 변환
            print("new message")
      
        # if tweet is longer than 140 characters
      
            if "extended_tweet" in msg:       # extended_tweet라는 key가 있는지 확인
                # add at the end of each tweet "t_end"
                self.client_socket\
                    .send(str(msg['extended_tweet']['full_text']+"t_end")\
                    .encode('utf-8'))

                text = preprocessing(str(msg['extended_tweet']['full_text']))
                mecab_text = preprocessing_mecab(text)
                kmeans_list.append(mecab_text)

                # client_socket에 인코딩 해서 보냄
                sentiment = predict(text)
        
                print(sentiment)
                readDF = spark.createDataFrame([
                    ( msg['extended_tweet']['full_text'], sentiment)
                    ],
                    ['content', 'sentiment']
                )

           
                print(msg['extended_tweet']['full_text'])
            else:
                # add at the end of each tweet "t_end"
                self.client_socket\
                    .send(str(msg['text']+"t_end")\
                    .encode('utf-8'))
                text = preprocessing(str(msg['text'])) 
                mecab_text = preprocessing_mecab(text)
                kmeans_list.append(mecab_text)
        
                sentiment = predict(text)
        
                print(sentiment)
                readDF = spark.createDataFrame([
                    ( msg['text'], sentiment)
                    ],
                    ['content', 'sentiment']
                )
                print(msg['user']['name'])
                print(msg['text'])
            
            global senPoscnt
            global senNegcnt
            global senNeucnt
            
            # sentiment Count
            if(sentiment == '긍정'):
                senPoscnt += 1
            elif(sentiment == '부정'):
                senNegcnt += 1
            else:
                senNeucnt += 1
            
            global LJMPoscnt
            global LJMNegcnt
            global LJMNeucnt
            global ACSPoscnt
            global ACSNegcnt
            global ACSNeucnt
            global YSYPoscnt
            global YSYNegcnt
            global YSYNeucnt
            global SSJPoscnt
            global SSJNegcnt
            global SSJNeucnt
            
            # candidate Sentiment Count
            if('재명' in text):
                if(sentiment == '긍정'):
                    LJMPoscnt += 1
                elif(sentiment == '부정'):
                    LJMNegcnt += 1
                else:
                    LJMNeucnt += 1
            
            if('철수' in text):
                if(sentiment == '긍정'):
                    ACSPoscnt += 1
                elif(sentiment == '부정'):
                    ACSNegcnt += 1
                else:
                    ACSNeucnt += 1
                    
            if('석열' in text):
                if(sentiment == '긍정'):
                    YSYPoscnt += 1
                elif(sentiment == '부정'):
                    YSYNegcnt += 1
                else:
                    YSYNeucnt += 1
                    
            if('상정' in text):
                if(sentiment == '긍정'):
                    SSJPoscnt += 1
                elif(sentiment == '부정'):
                    SSJNegcnt += 1
                else:
                    SSJNeucnt += 1
                    
            print()
            
            readDF.write.format("jdbc") \
                .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
                .option("dbtable", "oricrawltbl") \
                .option("user", user) \
                .option("password", password) \
                .option("driver", "com.mysql.jdbc.Driver") \
                .mode("overwrite").save()  

            candiTblRenew()

            sentiTblRenew() 
            
            # oriTblRenew()

            if(len(kmeans_list) > 10 ):
                vec = vectorization(kmeans_list)
                cluster_num = elbow_auto(vec,10)
                clustering_df = K_means_clustering(vec, cluster_num, kmeans_list)            
                visualization(clustering_df, cluster_num, '대선')
        
            return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True

    def on_error(self, status):
        print(status)
        return True

def sendData(c_socket, keyword):
    print('start sending data from Twitter to socket')
    # authentication based on the credentials
    auth = OAuthHandler(consumer_key, consumer_secret)  # 인증
    auth.set_access_token(access_token, access_secret)  # 인증
    # start sending data from the Streaming API
    twitter_stream = Stream(auth, TweetsListener(c_socket))  # stream 객체 생성
    twitter_stream.filter(track = keyword, locations=[124, 33, 130, 38], languages=["ko"])  # stream을 연결하고 실행

if __name__ == "__main__":
    # server (local machine) creates listening socket
    s = socket.socket()         # socket 객체 생성
    host = "0.0.0.0"            # localhost
    port = 5555                 # port 5555
    s.bind((host, port))         # socket binding , 소켓을 특정 네트워크 인터페이스와 포트번호에 연결하는데 사용한다.
    print('socket is ready')
    # server (local machine) listens for connections
    s.listen(4)                 # 서버가 클라이언트의 접속을 허용하도록 한다. 최대 4개를 허용하도록한다.
    print('socket is listening')
    # return the socket and the address on the other side of the connection (client side)
    c_socket, addr = s.accept()
      #연결 허용, c_socket 변수에는 클라이언트 소켓이 저장되고, addr에는 클라이언트 ip 주소가 저장된다.
    print("Received request from: " + str(addr))
    # select here the keyword for the tweet data
    sendData(c_socket, keyword = ['대선'])
      #c_socket과 keyword = 'piano'를 sendData함수의 인자로 넣음
