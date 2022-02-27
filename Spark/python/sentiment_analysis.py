from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as F


def preprocessing(lines):
    words = lines.select(explode(split(lines.value, "t_end")).alias("word"))
    #두개의 내장 SQL 함수(split 및 explode)를 사용하여 각 을 단어가 있는 여러 행으로 분할한다.
    # alias를 사용하여 새 열의 이름을 "word"로 지정합니다

    # words = words.replace('', None)
    # words = words.na.drop()
    # words = words.withColumn('word', F.regexp_replace('word', r'http\S+', ''))
    # words = words.withColumn('word', F.regexp_replace('word', "RT @[\w_]+: ", ''))
    # words = words.withColumn('word', F.regexp_replace('word', "@[\w_]+", ''))
    # words = words.withColumn('word', F.regexp_replace('word', "[&]+[a-z]+", ''))
    # words = words.withColumn('word', F.regexp_replace('word', "[ㄱ-ㅎㅏ-ㅣ.]+", ''))
    # words = words.withColumn('word', F.regexp_replace('word', r"[^가-힣0-9\s?!]", ''))
    # words = words.withColumn('word', F.regexp_replace('word', "[\t]+", ''))
    # words = words.replace('', None)
    # words = words.na.drop()
    # 기호 및 빈 문자 제거
    return words

if __name__ == "__main__":
    # create Spark session
    spark = SparkSession.builder.appName("TwitterSentimentAnalysis").getOrCreate()  # 어플리케이션 이름 설정
    # 데이터 프레임을 생성하기 위한 것으로 있으면 가져오고 없으면 생성한다.

    # read the tweet data from socket
    lines = spark.readStream.format("socket").option("host", "0.0.0.0").option("port", 5555).load()
    # localhost:5555에서 수신 대기하는 서버에서 수신한 텍스트 데이터를 나타내는 스트리밍 DataFrame을 만든다.
    #lines DataFrame은 스트리밍 텍스트 데이터를 포함하는 무제한 테이블을 나타냅니다
    #이 테이블에는 "value"라는 문자열의 열이 하나 포함되어 있으며 스트리밍 텍스트 데이터의 각 행은 테이블의 행이 됩니다.
    #lines.writeStream.format("csv").save("file:/home/hadoop/python/")

    # Preprocess the data
    words = preprocessing(lines)

    words = words.repartition(1)   #셔플을 수행
    query = words.writeStream.queryName("all_tweets") \
        .outputMode("append").format("parquet") \
        .option("path", "hdfs://master-node:9000/originTW/parc") \
        .option("checkpointLocation", "hdfs://master-node:9000/originTW/check") \
        .trigger(processingTime='60 seconds').start()
    query.awaitTermination()
