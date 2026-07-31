### Execution Modes of Pig

Apache Pig is a high-level platform for analyzing large data sets using a scripting language called Pig Latin. Pig can run on a single machine or on a distributed environment like Hadoop. Depending on where the Pig script is executed and where the data is stored, Pig has different execution modes. These are:

- **Local mode**: In this mode, Pig runs in a single Java Virtual Machine (JVM) and accesses the local file system. This mode is useful for development, testing and prototyping. To run Pig in local mode, use the `-x local` option in the command line or the `pig -x local` command in the Grunt shell .
- **MapReduce mode**: In this mode, Pig runs on a Hadoop cluster and accesses the Hadoop Distributed File System (HDFS). This mode is suitable for processing large data sets in parallel. To run Pig in MapReduce mode, use the `-x mapreduce` option in the command line or the `pig -x mapreduce` command in the Grunt shell .
- **Tez mode**: In this mode, Pig runs on a Hadoop cluster and uses Apache Tez as the execution engine. Tez is a framework for building high-performance data processing applications on Hadoop. Tez mode can improve the performance and scalability of Pig scripts by optimizing the execution plan and minimizing the data shuffling. To run Pig in Tez mode, use the `-x tez` option in the command line or the `pig -x tez` command in the Grunt shell.
- **Tez local mode**: In this mode, Pig runs in a single JVM and uses Apache Tez as the execution engine. This mode is similar to local mode, but with the benefits of Tez optimization. To run Pig in Tez local mode, use the `-x tez_local` option in the command line or the `pig -x tez_local` command in the Grunt shell.
- **Spark mode**: In this mode, Pig runs on a Hadoop cluster and uses Apache Spark as the execution engine. Spark is a fast and general engine for large-scale data processing. Spark mode can leverage the in-memory computation and fault-tolerance features of Spark to speed up Pig scripts. To run Pig in Spark mode, use the `-x spark` option in the command line or the `pig -x spark` command in the Grunt shell.
- **Embedded mode**: In this mode, Pig can be embedded in a Java application and invoked programmatically. This mode allows the user to define custom functions (UDFs) and operators in Java and use them in Pig scripts. To run Pig in embedded mode, use the `PigServer` class in the Java code .

The following diagram illustrates the different execution modes of Pig:

![Execution Modes of Pig](https://data-flair.training/blogs/wp-content/uploads/sites/2/2017/08/Apache-Pig-Architecture-1.jpg)

Source: https://data-flair.training/blogs/apache-pig-architecture/