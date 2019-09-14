import re
from pyspark import SparkConf,SparkContext

def compiledWords(text):
    return re.compile(r"\W",re.UNICODE).split(text.lower())
    


conf = SparkConf().setMaster("local").setAppName("Word Count")
sc = SparkContext(conf = conf)

linesRdd = sc.textFile("H:\Practice\BigData-DataFiles\Book.txt")
wordsRdd = linesRdd.flatMap(compiledWords)
wordCountSortedRdd = wordsRdd.map(lambda x: (x,1)).reduceByKey(lambda x,y: x+y).map(lambda x: (x[1],x[0])).sortByKey()
results = wordCountSortedRdd.collect()

for result in results:
    cleanWord = result[1].encode("ascii","ignore")
    if(cleanWord):
        print(cleanWord.decode()+" - "+str(result[0]))
 
