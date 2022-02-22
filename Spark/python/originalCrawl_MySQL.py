from pyspark import SparkContext, SparkConf, SQLContext

# database => TTA
# 원본 데이터 table => oriCrawl
# 새롭게 크롤링된 데이터프레임 => newCrawl 
# spark 폴더에 위치할 것

# spark session 설정
conf = SparkConf() \
    .setAppName("spark-sql") \
    .set("spark.driver.extraClassPath","./jars/mysql-connector-java-5.1.38.bin.jar")

sc = SparkContext.getOrCreate(conf=conf)

sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

# mysql 변수 설정
database = "TTA"
table = "oriCrawl"
user = "root"
password  = "1234"

# mysql 기존 테이블 데이터 프레임으로 import
oriCrawl = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

# mysql에 저장할 데이터 프레임 수정
if(oriCrawl.count() >= 10):
	oriCrawl = spark.createDataFrame(oriCrawl.tail(oriCrawl.count()-1), oriCrawl.schema)
	oriCrawl.union(newCrawl)
else:
	oriCrawl.union(newCrawl)

# mysql에 데이터 프레임 export
oriCrawl.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()