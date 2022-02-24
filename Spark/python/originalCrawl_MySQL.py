from pyspark import SparkContext, SparkConf, SQLContext
from pyspark.sql.functions import *

# database => TTA
# 원본 데이터 table => oriCrawlTbl
# 새롭게 크롤링된 데이터프레임 => newCrawl 
# spark 폴더에 위치할 것

# spark session 설정
conf = SparkConf() \
    .setAppName("spark-sql") \
    .set("spark.driver.extraClassPath","./jars/mysql-connector-java-5.1.38.bin.jar")

sc = SparkContext.getOrCreate(conf=conf)

sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

# 새로운 크롤링정보 dataframe으로 생성
newCrawl = spark.createDataFrame([
        (crawling_content, content_sentiment)
    ],
    ['content', 'sentiment']
)

# mysql 변수 설정
database = "TTA"
table = "oriCrawlTbl"
user = "root"
password  = "1234"

# mysql 기존 테이블 데이터 프레임으로 import
oriCrawlTbl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

if(oriCrawlTbl.count() >= 10):
	oriCrawlTbl = spark.createDataFrame(oriCrawlTbl.tail(oriCrawlTbl.count()-1), oriCrawlTbl.schema)
	oriCrawlTbl = oriCrawlTbl.union(newCrawl)
else:
	oriCrawlTbl = oriCrawlTbl.union(newCrawl)

# mysql에 데이터 프레임 export
oriCrawlTbl.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()