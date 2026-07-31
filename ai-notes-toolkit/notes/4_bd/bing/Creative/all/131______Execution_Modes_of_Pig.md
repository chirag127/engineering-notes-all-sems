#### Execution Modes of Pig

Apache Pig is a high-level platform for analyzing large data sets using a scripting language called Pig Latin. Pig can run on a single machine or on a distributed environment like a cluster. Pig has different execution modes depending on where the Pig script is going to run and where the data is residing. The three main execution modes of Pig are:

- **Local mode**: In this mode, Pig runs in a single Java Virtual Machine (JVM) and accesses the local file system. This mode is useful for development, experimenting and prototyping. To run Pig in local mode, we need to specify the `-x local` flag in the command line or set the `pig.exec.type` property to `local` in the configuration file. For example:

  ```bash
  pig -x local
  ```

- **MapReduce mode**: In this mode, Pig runs on a Hadoop cluster and accesses the Hadoop Distributed File System (HDFS). This mode is used for processing large data sets in a parallel and distributed manner. To run Pig in MapReduce mode, we need to specify the `-x mapreduce` flag in the command line or set the `pig.exec.type` property to `mapreduce` in the configuration file. For example:

  ```bash
  pig -x mapreduce
  ```

- **Tez mode**: In this mode, Pig runs on a Hadoop cluster and uses Apache Tez as the execution engine. Tez is a framework for building high-performance batch and interactive data processing applications on Hadoop. Tez improves the performance of Pig by optimizing the execution plan and minimizing the data shuffling and sorting. To run Pig in Tez mode, we need to specify the `-x tez` flag in the command line or set the `pig.exec.type` property to `tez` in the configuration file. For example:

  ```bash
  pig -x tez
  ```

Pig also has other execution modes such as Tez local mode, Spark mode and Storm mode, which are experimental and not fully supported. For more details, please refer to the official documentation of Pig.

: https://www.javatpoint.com/pig-run-modes
: https://mindmajix.com/hadoop/apache-pig-execution-types
: https://data-flair.training/blogs/apache-pig-architecture/
: https://www.tutorialspoint.com/apache_pig/apache_pig_execution.htm
: https://pig.apache.org/docs/r0.17.0/start.html