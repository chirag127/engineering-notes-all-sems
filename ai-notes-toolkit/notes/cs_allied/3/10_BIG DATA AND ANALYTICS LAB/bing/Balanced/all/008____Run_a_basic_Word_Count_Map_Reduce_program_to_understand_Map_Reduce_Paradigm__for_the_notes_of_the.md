# Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

- Map Reduce is a programming model for processing large-scale data sets in parallel and distributed manner.
- Map Reduce consists of two phases: Map and Reduce.
- Map phase takes an input key-value pair and produces a set of intermediate key-value pairs.
- Reduce phase takes the intermediate key-value pairs with the same key and combines them to produce the final output.
- Word Count is a simple example of Map Reduce that counts the frequency of each word in a text file.
- The steps to run a Word Count Map Reduce program are:

  - Create a text file with some content, such as "This is an apple. Apple is red in color."
  - Write a Mapper class that implements the map method. The map method takes a line of text as input and splits it into words. For each word, it emits a key-value pair with the word as the key and 1 as the value.
  - Write a Reducer class that implements the reduce method. The reduce method takes a word and a list of values as input and sums up the values. It emits a key-value pair with the word as the key and the sum as the value.
  - Write a Driver class that configures and runs the Map Reduce job. The Driver class specifies the input and output paths, the Mapper and Reducer classes, and the output key and value types.
  - Compile and run the program using a Map Reduce framework, such as Hadoop or Spark. The program will read the input file, apply the Mapper and Reducer functions, and write the output file with the word counts.