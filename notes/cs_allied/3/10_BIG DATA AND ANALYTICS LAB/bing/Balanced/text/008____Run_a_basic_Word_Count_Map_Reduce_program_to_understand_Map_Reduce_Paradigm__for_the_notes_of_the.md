## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Map Reduce consists of two phases: Map and Reduce.
- Map phase takes an input key-value pair and produces a set of intermediate key-value pairs.
- Reduce phase takes the intermediate key-value pairs with the same key and combines them to produce the final output.
- Word Count is a simple example of Map Reduce that counts the frequency of each word in a text file.
- The steps to run a Word Count Map Reduce program are:

  - Write a Mapper class that implements the `map` method. The `map` method takes an input key-value pair, where the key is the line number and the value is the line of text, and emits intermediate key-value pairs, where the key is a word and the value is 1.
  - Write a Reducer class that implements the `reduce` method. The `reduce` method takes an intermediate key and a list of values, where the key is a word and the values are 1s, and emits the final key-value pair, where the key is the word and the value is the sum of the values.
  - Write a Driver class that configures and runs the Map Reduce job. The Driver class sets the input and output paths, the mapper and reducer classes, the output key and value types, and the number of reducers.
  - Compile and package the classes into a jar file.
  - Run the jar file on a Hadoop cluster or a local machine using the `hadoop jar` command. The command takes the jar file name, the driver class name, the input path, and the output path as arguments.
  - Check the output file for the word count results.