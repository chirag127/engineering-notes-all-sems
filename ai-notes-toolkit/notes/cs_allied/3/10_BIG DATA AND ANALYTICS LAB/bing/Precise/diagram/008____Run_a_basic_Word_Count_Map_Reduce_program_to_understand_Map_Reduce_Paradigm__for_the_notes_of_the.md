## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It is a key component of the Apache Hadoop ecosystem, which provides a framework for distributed storage and processing of big data.

Here are the steps to run a basic Word Count MapReduce program:

1. Install Hadoop on your system and configure it properly.
2. Write a MapReduce program for Word Count in a language of your choice, such as Java or Python.
3. Compile the program and create a JAR file if you are using Java.
4. Copy the input data to Hadoop Distributed File System (HDFS).
5. Run the MapReduce job using the `hadoop jar` command if you are using Java, or the `hadoop-streaming` command if you are using Python.
6. The MapReduce framework will automatically split the input data into chunks and assign them to different map tasks running on different nodes in the cluster.
7. The map tasks will process the data and output key-value pairs, where the key is a word and the value is the number of occurrences of that word.
8. The MapReduce framework will shuffle and sort the intermediate data and send them to the reduce tasks.
9. The reduce tasks will aggregate the values for each key and output the final result.
10. The final result will be stored in HDFS and can be retrieved using the `hadoop fs -cat` command.

By running a basic Word Count MapReduce program, you can understand the basic concepts and workflow of the MapReduce paradigm. It is a powerful tool for processing large data sets in a distributed and parallel manner.