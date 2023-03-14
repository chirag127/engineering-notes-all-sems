#### Execution Modes of Pig

- Apache Pig is a platform for analyzing large data sets using a high-level language called Pig Latin.
- Pig can run on a single machine or on a cluster of machines using Hadoop.
- Pig has six execution modes or exectypes, which determine how Pig scripts are executed and where the data is stored and processed.
- The six execution modes are:

  - Local Mode: In this mode, Pig runs on a single machine using the local file system. No Hadoop installation is required. This mode is useful for testing and debugging purposes.
  - Tez Local Mode: In this mode, Pig runs on a single machine using the local file system, but internally invokes the Tez execution engine, which is a framework for building high-performance batch and interactive data processing applications on Hadoop. This mode is experimental and may not support all Pig features.
  - MapReduce Mode: In this mode, Pig runs on a cluster of machines using the Hadoop Distributed File System (HDFS) and the MapReduce framework, which is a programming model for parallel processing of large data sets. This mode is the default and most common mode for running Pig scripts on production data.
  - Tez Mode: In this mode, Pig runs on a cluster of machines using HDFS and the Tez execution engine, which can optimize the execution plan of Pig scripts and improve the performance and scalability of data processing. This mode is also experimental and may not support all Pig features.
  - Spark Mode: In this mode, Pig runs on a cluster of machines using HDFS and the Spark execution engine, which is a fast and general engine for large-scale data processing that supports in-memory computations and streaming analytics. This mode is also experimental and may not support all Pig features.
  - Interactive Mode: In this mode, Pig runs in an interactive shell called Grunt, where users can enter Pig Latin statements and commands and see the results immediately. Grunt can be invoked in any of the above modes using the -x flag (e.g., pig -x local).

- A mnemonic to remember the six execution modes of Pig is: **L**et **T**he **M**onkey **T**ake **S**ome **I**ce-cream. (Local, Tez Local, MapReduce, Tez, Spark, Interactive)