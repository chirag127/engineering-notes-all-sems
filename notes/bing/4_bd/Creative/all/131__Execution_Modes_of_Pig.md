#### Execution Modes of Pig

- Apache Pig is a high-level platform for analyzing large data sets using a scripting language called Pig Latin.
- Pig can run in different execution modes depending on where the data is stored and how the Pig script is executed.
- The three main execution modes of Pig are:

  - **Local mode**: In this mode, Pig runs in a single Java Virtual Machine (JVM) on the local host and accesses the local file system. This mode is useful for development, testing and debugging of Pig scripts. To run Pig in local mode, use the `-x local` option when invoking the `pig` command.
  - **MapReduce mode**: In this mode, Pig runs on a Hadoop cluster and accesses the Hadoop Distributed File System (HDFS). This mode is suitable for processing large-scale data sets in a distributed and parallel manner. To run Pig in MapReduce mode, use the `-x mapreduce` option when invoking the `pig` command.
  - **Tez mode**: In this mode, Pig runs on a Hadoop cluster and uses Apache Tez as the execution engine. Tez is a framework for building high-performance batch and interactive data processing applications on Hadoop. Tez optimizes the execution plan of Pig scripts by minimizing data movement and reducing the number of MapReduce jobs. To run Pig in Tez mode, use the `-x tez` option when invoking the `pig` command.

- Pig also supports other execution modes such as:

  - **Interactive mode**: In this mode, Pig runs in a shell called Grunt, where the user can enter Pig Latin commands and see the results immediately. This mode is useful for exploring and analyzing data interactively. To start the Grunt shell, simply run the `pig` command without any options.
  - **Batch mode**: In this mode, Pig runs a script file that contains a sequence of Pig Latin commands. This mode is useful for automating and scheduling data processing tasks. To run a Pig script file, use the `-f` option followed by the file name when invoking the `pig` command.
  - **Embedded mode**: In this mode, Pig runs as a library within a Java program, where the user can define custom functions and operators using Java. This mode is useful for extending the functionality and performance of Pig. To run Pig in embedded mode, use the `PigServer` class in the Java program.

- A mnemonic to remember the three main execution modes of Pig is: **LMT** (Local, MapReduce, Tez).
- An example of a Pig script that counts the number of words in a text file is:

  ```
  -- Load the text file from the file system
  A = LOAD 'input.txt' AS (line:chararray);
  -- Split each line into words and flatten the result
  B = FOREACH A GENERATE FLATTEN(TOKENIZE(line)) AS word;
  -- Group the words by their value and count the occurrences
  C = GROUP B BY word;
  D = FOREACH C GENERATE group, COUNT(B);
  -- Store the output in the file system
  STORE D INTO 'output.txt';
  ```

  - To run this script in local mode, use the command: `pig -x local -f wordcount.pig`
  - To run this script in MapReduce mode, use the command: `pig -x mapreduce -f wordcount.pig`
  - To run this script in Tez mode, use the command: `pig -x tez -f wordcount.pig`