from pyspark import SparkContext

sc= SparkContext(master="local",appName="MapExample")
words=["Angular","BootStrap","C","Django","Ext-js","Flask","Google Go","Hadoop","i?","Java","kafka"]

wordsRdd=sc.parallelize(words)
wordMap=wordsRdd.map(lambda x:(x,1)).collect()
print(str(wordMap))
