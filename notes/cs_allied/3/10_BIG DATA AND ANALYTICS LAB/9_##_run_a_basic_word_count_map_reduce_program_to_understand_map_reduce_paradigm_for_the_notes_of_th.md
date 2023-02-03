## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm. for the notes of the BIG DATA AND ANALYTICS LAB in the subject of BIG DATA AND ANALYTICS LAB

The Word Count Map Reduce program is a basic example of the Map Reduce paradigm, which is a programming model for processing large datasets in parallel across a cluster of computers. The Word Count program counts the number of occurrences of each word in a large dataset.

To run a basic Word Count Map Reduce program, you need to perform the following steps:

1. Prepare the input data: The input data for the Word Count program is a large text file, which can be stored in a Hadoop Distributed File System (HDFS).

2. Write the Map function: The Map function takes the input data and processes it to produce intermediate key-value pairs. In the case of the Word Count program, the Map function takes each line of the input text file, splits it into words, and outputs a key-value pair for each word, with the word as the key and the value set to 1.

3. Write the Reduce function: The Reduce function takes the intermediate key-value pairs produced by the Map function and aggregates them to produce the final output. In the case of the Word Count program, the Reduce function takes the key-value pairs for each word and adds up the values to produce the final count for each word.

4. Run the Map Reduce program: The Map Reduce program is run using a Map Reduce framework, such as Hadoop, which takes care of distributing the input data to the Map functions, running the Reduce functions, and aggregating the results.

In conclusion, the Word Count Map Reduce program is a basic example of the Map Reduce paradigm, which is a programming model for processing large datasets in parallel across a cluster of computers. To run a basic Word Count Map Reduce program, you need to prepare the input data, write the Map and Reduce functions, and run the Map Reduce program using a Map Reduce framework.
