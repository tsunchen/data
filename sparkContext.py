from pyspark import SparkContext
from pyspark import SparkConf

conf = SparkConf()
conf.set('master', 'local')
#conf.set('master', 'spark://65.49.225.53:28713')

sparkContext = SparkContext(conf = conf)
rdd = sparkContext.parallelize(range(100))
print(rdd.collect())
sparkContext.stop()
