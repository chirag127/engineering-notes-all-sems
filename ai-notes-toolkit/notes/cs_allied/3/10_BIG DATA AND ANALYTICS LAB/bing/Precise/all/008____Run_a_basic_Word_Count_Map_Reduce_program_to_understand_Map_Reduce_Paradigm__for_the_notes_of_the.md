## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

MapReduce is a programming model for processing large datasets in parallel across a distributed computing environment. It is commonly used in big data and analytics applications.

One of the simplest examples of a MapReduce program is a word count program. This program counts the number of occurrences of each word in a given input dataset.

Here are the steps to run a basic Word Count MapReduce program:

1. **Prepare the input data**: The input data for the word count program should be in the form of text files. These files should be placed in the Hadoop Distributed File System (HDFS) so that they can be accessed by the MapReduce program.

2. **Write the Map function**: The Map function takes in a key-value pair as input, where the key is the offset of the line in the input file and the value is the line of text itself. The Map function then splits the line into words and outputs a key-value pair for each word, where the key is the word and the value is 1.

3. **Write the Reduce function**: The Reduce function takes in a key and a list of values as input, where the key is a word and the values are the counts of that word output by the Map function. The Reduce function then sums up the counts and outputs a key-value pair where the key is the word and the value is the total count of that word.

4. **Run the MapReduce program**: To run the MapReduce program, you need to use the Hadoop command line interface. You need to specify the input and output directories in HDFS, as well as the location of the Map and Reduce functions.

After the MapReduce program has completed, the output directory in HDFS will contain the final word counts for each word in the input dataset.

By running a basic Word Count MapReduce program, you can gain a better understanding of the MapReduce paradigm and how it can be used to process large datasets in parallel. This knowledge can be applied to more complex big data and analytics applications.