from pyspark import SparkFiles
import os
import numpy as np
from pyspark import SparkContext, SparkConf

tmpdir = '/root/workspace/'
path = os.path.join(tmpdir, 'num_init')

with open(path, 'w') as f:
    f.write('1000')

conf = SparkConf()
conf.set('master', 'local')
#
context = SparkContext(conf = conf)
context.addFile(path)

rdd = context.parallelize(np.arange(8))

def func(iterable):
    with open(SparkFiles.get('num_init')) as f:
        value = int(f.readline())
        return [x * value for x in iterable]

print(rdd.mapPartitions(func).collect())
context.stop()
