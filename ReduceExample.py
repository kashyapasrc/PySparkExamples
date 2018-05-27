from pyspark import SparkContext
from operator import add

sc = SparkContext(master="local",appName="ReduceExample")
list=[]
for i in range(1,100):
    list.append(i)


numsRdd=sc.parallelize(list)
result=numsRdd.reduce(add)
print("Total Count :-> "+str(result))