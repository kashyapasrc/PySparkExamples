from pyspark import SparkContext

sc = SparkContext("local","JoinExample")

x = sc.parallelize([("spark", 1), ("hadoop", 4)])
y = sc.parallelize([("spark", 2), ("hadoop", 5)])


joinRdd=x.join(y)
result=joinRdd.collect()
print(str(result))

sc.stop()