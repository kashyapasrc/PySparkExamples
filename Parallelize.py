from pyspark import SparkContext

def wordCounter(listString):
	sc =SparkContext("local",appName="WordCounter")
	listRdd=sc.parallelize(listString)
	listRdd.collect()
	wordCount=listRdd.count()
	listRdd.foreach(f)	
	sc.stop()
	return wordCount

def f(x):print(x)


listString=["ApacheSpark","Java","Python","Scala","Hadoop"]

print("WordCounter "+str(wordCounter(listString)))




