## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm.

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Map Reduce consists of two phases: Map and Reduce.
- In the Map phase, the input data is split into smaller chunks and assigned to different workers (mappers) that process them independently and produce intermediate key-value pairs.
- In the Reduce phase, the intermediate key-value pairs are shuffled and sorted by their keys and sent to different workers (reducers) that aggregate them and produce the final output.
- A Word Count Map Reduce program is a simple example that counts the frequency of each word in a given text file.
- The steps to run a basic Word Count Map Reduce program are:

  1. Create a text file with some text and save it as input.txt in a local directory.
  2. Install and configure Hadoop on your system or use a cloud service that provides Hadoop.
  3. Create a Hadoop user and a Hadoop file system (HDFS) directory for the user.
  4. Copy the input.txt file from the local directory to the HDFS directory using the command: `hadoop fs -put input.txt /user/hadoop/input`
  5. Write a Java program that implements the Mapper and Reducer interfaces and defines the map and reduce methods for the Word Count program. Save it as WordCount.java in a local directory.
  6. Compile the Java program and create a jar file using the command: `javac -classpath $(hadoop classpath) WordCount.java && jar cf wc.jar WordCount*.class`
  7. Run the Word Count Map Reduce program using the command: `hadoop jar wc.jar WordCount /user/hadoop/input /user/hadoop/output`
  8. Check the output of the program in the HDFS directory using the command: `hadoop fs -cat /user/hadoop/output/part-r-00000`
  9. The output file will contain the words and their frequencies in the input file, such as:

```
Hello 1
World 1
This 1
is 1
a 1
test 1
file 1
for 1
word 1
count 1
program 1
```