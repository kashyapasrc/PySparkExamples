from pyspark import SparkContext
logFilePath="./datasets/iris.txt"

def filterExample():
	sc=SparkContext(master="local",appName="FilterExample")
	logFileRdd=sc.textFile(logFilePath)
	wordRdd=logFileRdd.filter(lambda s: "1" in s)
	wordFilter=wordRdd.collect()
	wordCounter=wordRdd.count()
	sc.stop()
	print("kashyap"+str(wordCounter))
	return wordFilter,wordCounter

print("Word counter::::::"+str(filterExample()))
		
