from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext, HiveContext, SparkSession
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

conf = SparkConf().setMaster("local[1]").setAppName("StreamProcessor_1")

sc = SparkContext(conf=conf)

print "Setting LOG LEVEL as ERROR"
sc.setLogLevel("ERROR")

ssc = StreamingContext(sparkContext = sc, batchDuration = 1)

kafkaStream = KafkaUtils.createStream(ssc = ssc, zkQuorum = 'localhost:2181', topics = 'test')



print(sc)