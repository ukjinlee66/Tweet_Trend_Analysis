from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import *

# database => TTA
# 감성분석 table => sentimentTbl
# 새로운 감성분석 dataframe => newSentiment
# spark 폴더에 위치할 것

# spark session 설정
conf = SparkConf() \
    .setAppName("spark-sql") \
    .set("spark.driver.extraClassPath","./jars/mysql-connector-java-5.1.38.bin.jar")

sc = SparkContext.getOrCreate(conf=conf)

sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

# 새로운 긍/부정정보 dataframe으로 생성
# cnt부분 10이 아닌 '10'으로 만들면 해당 타입 string이기때문에
# ''없이 10으로 만들어서 bigint 타입으로 생성해야함.
newSentiment = spark.createDataFrame([
        ('positive', positive_Count),('negative', negative_Count),('neutrality', neutrality_Count)
    ],
    ['sentiment','count']
)

# mysql 변수 설정
database = "TTA"
table = "sentimentTbl"
user = "root"
password  = "1234"

# mysql 기존 테이블 데이터 프레임으로 import
sentimentTbl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

# 만약 dataframe count컬럼이 string 타입일 경우 bigint타입으로 변환
# newSentiment = newSentiment.withColumn("count",newSentiment.count.cast('bigint'))

# dataframe 병합
sentimentTbl = sentimentTbl.union(newSentiment)

# dataframe 숫자 더하기
sentimentTbl = sentimentTbl.groupBy("sentiment")\
    .agg(sum("count").alias("count"))

# mysql에 데이터 프레임 export
sentimentTbl.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()