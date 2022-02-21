from pyspark import SparkContext, SparkConf, SQLContext

# 원본 데이터 database => crawDB
# 원본 데이터 table => oriCraw
# 새롭게 크롤링된 데이터프레임 => newCraw 

# spark session 설정
conf = SparkConf() \
    .setAppName("spark-sql") \
    .set("spark.driver.extraClassPath","./jars/mysql-connector-java-5.1.38.bin.jar")

sc = SparkContext.getOrCreate(conf=conf)

sqlContext = SQLContext(sc)
spark = sqlContext.sparkSession

# mysql 변수 설정
database = "crawDB"
table = "oriCraw"
user = "root"
password  = "1234"

# mysql 기존 테이블 데이터 프레임으로 import
oriCraw = spark.read.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .load()

# - mysql에 저장할 데이터 프레임 수정

if(oriCraw.count() >= 10):
	oriCraw = spark.createDataFrame(oriCraw.tail(df.count()-1), oriCraw.schema)
	oriCraw.union(newCraw)
else:
	oriCraw.union(newCraw)


# mysql에 데이터 프레임 export
oriCraw.write.format("jdbc") \
    .option("url", "jdbc:mysql://localhost:3306/{}?serverTimezone=Asia/Seoul".format(database)) \
    .option("dbtable", table) \
    .option("user", user) \
    .option("password", password) \
    .option("driver", "com.mysql.jdbc.Driver") \
    .mode("overwrite").save()