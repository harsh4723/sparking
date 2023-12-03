from pyspark import SparkContext

# Create a SparkContext
sc = SparkContext("local", "Word Count App")

# Create an RDD (Resilient Distributed Dataset) from a text file
text_rdd = sc.textFile("text.txt")

# Transformations: Split each line into words and count the occurrences
word_counts = text_rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a, b: a + b)

# Actions: Collect the results and print them
results = word_counts.collect()
for result in results:
    print(result)


sc.stop()
