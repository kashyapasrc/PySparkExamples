from pyspark import SparkContext

logFilePath="C:/Users/chait/OneDrive/Desktop/3rd_party_library_in android.txt"
char="http"
sc=SparkContext("local","CharCounter")

def charCounter(char):
	logFile=sc.textFile(logFilePath).cache()
	numChar=logFile.filter(lambda s: char in s).count()
	


	return numChar
print("Lines with "+char+" "+str(charCounter(char)))
char="github"
print("Lines with "+char+" "+str(charCounter(char)))
sc.stop()