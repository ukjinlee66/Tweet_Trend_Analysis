from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import *

# database => TTA
# 후보자별 감성분석 table => candiTbl
# 새로운 감성분석 dataframe => newCandidateSenti
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
newCandidateSenti = spark.createDataFrame([
        ('positive', LJM_positiveCnt, ACS_positiveCnt, YSY_positiveCnt, SSJ_positiveCnt, HGY_positiveCnt),
        ('negative', LJM_negativeCnt, ACS_negativeCnt, YSY_negativeCnt, SSJ_negativeCnt, HGY_negativeCnt),
        ('neutrality', LJM_neutralityCnt, ACS_neutralityCnt, YSY_neutralityCnt, SSJ_neutralityCnt, HGY_neutralityCnt)
    ],
    ['sentiment','LJMcnt','ACScnt','YSYcnt','SSJcnt','HGYcnt']
)

# mysql 변수 설정
database = "TTA"
table = "candiTbl"
user = "root"
password  = "1234"

# mysql 기존 테이블 데이터 프레임으로 import
candiTbl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

# dataframe 병합
candiTbl = candiTbl.union(newCandidateSenti)

# dataframe 숫자 더하기
candiTbl = candiTbl.groupBy("sentiment")\
    .agg(sum("LJMcnt").alias("LJMcnt"),\
         sum("ACScnt").alias("ACScnt"),\
         sum("YSYcnt").alias("YSYcnt"),\
         sum("SSJcnt").alias("SSJcnt"),\
         sum("HGYcnt").alias("HGYcnt"))

# mysql에 데이터 프레임 export
candiTbl.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()