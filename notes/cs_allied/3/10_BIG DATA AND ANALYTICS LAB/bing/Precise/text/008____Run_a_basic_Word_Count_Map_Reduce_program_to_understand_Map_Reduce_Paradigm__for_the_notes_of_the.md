## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It is a key component of the Apache Hadoop ecosystem, which provides a framework for distributed storage and processing of big data.

Here are the steps to run a basic Word Count MapReduce program:

1. Install Hadoop on your system and configure it properly.
2. Create a text file with some data that you want to count the words of.
3. Write a MapReduce program in Java, Python, or any other supported language. The program should have two main functions: a mapper function and a reducer function.
4. The mapper function takes in a key-value pair, where the key is the offset of the line in the file and the value is the line itself. The function should split the line into words and output a key-value pair for each word, where the key is the word and the value is 1.
5. The reducer function takes in a key and a list of values. The key is the word and the list of values is the list of 1s that were output by the mapper function for that word. The function should sum up the values and output a key-value pair where the key is the word and the value is the total count of that word in the file.
6. Compile and run the MapReduce program using the Hadoop command line interface. The program will run the mapper function on each line of the input file in parallel, and then run the reducer function on the output of the mappers to produce the final word count.
7. The output of the program will be a file containing the word counts for each word in the input file.

By running a basic Word Count MapReduce program, you can gain a better understanding of the MapReduce paradigm and how it can be used to process large data sets in a distributed and parallel manner. This is a fundamental concept in the field of Big Data and Analytics.