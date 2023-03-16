## Run a basic Word Count Map Reduce program to understand Map Reduce Paradigm

MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. It is commonly used for big data processing.

Here are the steps to run a basic Word Count MapReduce program:

1. **Install Hadoop**: Hadoop is an open-source software framework for distributed storage and processing of big data. It is necessary to install Hadoop to run a MapReduce program.

2. **Write the MapReduce program**: The MapReduce program consists of two main functions: the map function and the reduce function. The map function takes in a set of data and converts it into key-value pairs. The reduce function takes the output of the map function and combines the values with the same key.

3. **Compile the program**: The MapReduce program needs to be compiled before it can be run. This can be done using the `javac` command.

4. **Create input data**: The input data for the MapReduce program should be in the form of text files. These files should be placed in the Hadoop Distributed File System (HDFS).

5. **Run the MapReduce program**: The MapReduce program can be run using the `hadoop jar` command. This command takes the compiled MapReduce program and the input data as arguments.

6. **View the output**: The output of the MapReduce program is stored in the HDFS. It can be viewed using the `hadoop fs -cat` command.

By following these steps, you can run a basic Word Count MapReduce program and understand the MapReduce paradigm. This can be useful for processing large data sets in a distributed manner.