from pyspark import SparkContext

from sys import stdin


if __name__ == "__main__":

    sc = SparkContext("local[*]" , "wordcount")

    sc.setLogLevel("ERROR")
    input=sc.textFile("search_data.txt")

    words=input.flatMap(lambda x: x.split(" "))

    wordsMap=words.map( lambda x: (x.lower(),1))

    wordsMapCount=wordsMap.reduceByKey( lambda x,y: x+y)

    result=wordsMapCount.collect()

    for a in result:
        print(a)

#stdin.readline()