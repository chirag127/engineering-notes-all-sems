## Run a Basic Word Count Map Reduce Program to Understand Map Reduce Paradigm

MapReduce is a programming model used for processing large volumes of data in parallel. It divides the input data into chunks, processes them in a parallel and distributed manner, and then combines the results to provide the final output. Here is a step-by-step guide to running a basic Word Count MapReduce program to understand the MapReduce paradigm.

### Step 1: Setting up the Environment

Before starting with the MapReduce program, you need to set up the environment. Follow these steps:

1. Install Hadoop on your system.
2. Set up a Hadoop cluster with at least one master node and one slave node.
3. Configure the Hadoop environment variables.

### Step 2: Writing the MapReduce Program

1. Open a text editor and create a new file.
2. Write the code for the MapReduce program. The code should have at least two classes, Mapper and Reducer.
3. In the Mapper class, write the code to read the input data, split it into words, and output the words with a count of 1.
4. In the Reducer class, write the code to sum up the counts for each word and output the final count for each word.

### Step 3: Compiling the Program

1. Save the MapReduce program file with a .java extension.
2. Open the command prompt and navigate to the directory where the file is saved.
3. Compile the program using the following command:
   ```
   javac -classpath $HADOOP_HOME/hadoop-core.jar WordCount.java
   ```
   Make sure to replace $HADOOP_HOME with the path to your Hadoop installation directory.

### Step 4: Creating the Input File

1. Create an input file with some text data. For example, you can create a file named input.txt with the following content:
   ```
   hello world
   hello hadoop
   world is big
   hadoop is awesome
   ```

### Step 5: Running the MapReduce Program

1. Copy the input file to the Hadoop file system using the following command:
   ```
   hadoop fs -put input.txt /input
   ```
2. Run the MapReduce program using the following command:
   ```
   hadoop jar $HADOOP_HOME/hadoop-examples.jar WordCount /input /output
   ```
   The first argument is the input directory, and the second argument is the output directory.
3. Wait for the program to finish running.
4. Check the output directory for the output file. You can view the output file using the following command:
   ```
   hadoop fs -cat /output/part-r-00000
   ```
   The output should be:
   ```
   hadoop 2
   hello 2
   is 2
   big 1
   awesome 1
   world 2
   ```

Congratulations! You have successfully run a basic Word Count MapReduce program to understand the MapReduce paradigm.