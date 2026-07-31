## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm.

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed environments.
- Map Reduce consists of two phases: map and reduce.
- The map phase takes an input key-value pair and produces a set of intermediate key-value pairs.
- The reduce phase takes the intermediate key-value pairs with the same key and combines them to produce an output key-value pair.
- A Word Count Map Reduce program is a simple example of how to use Map Reduce to count the frequency of words in a text file.
- The steps to run a basic Word Count Map Reduce program are:

  1. Create a text file with some text and save it in a local directory.
  2. Copy the text file to the Hadoop Distributed File System (HDFS) using the command: `hadoop fs -put <local_file> <hdfs_file>`
  3. Write a Java class that implements the Mapper interface and overrides the map method. The map method should take a line of text as the input key-value pair and split it into words. For each word, it should emit a key-value pair with the word as the key and 1 as the value.
  4. Write a Java class that implements the Reducer interface and overrides the reduce method. The reduce method should take a word and a list of values as the input key-value pair and sum up the values. It should emit a key-value pair with the word as the key and the sum as the value.
  5. Write a Java class that defines the main method and sets up the configuration and job parameters for the Map Reduce program. The main method should specify the input and output paths, the mapper and reducer classes, the output key and value types, and the number of reducers.
  6. Compile the Java classes and create a jar file using the command: `javac -classpath <hadoop_classpath> *.java` and `jar cf wc.jar *.class`
  7. Run the Map Reduce program using the command: `hadoop jar wc.jar <main_class> <input_path> <output_path>`
  8. Check the output file in the HDFS using the command: `hadoop fs -cat <output_path>/part-r-00000`
  9. The output file should contain the words and their frequencies in the text file.