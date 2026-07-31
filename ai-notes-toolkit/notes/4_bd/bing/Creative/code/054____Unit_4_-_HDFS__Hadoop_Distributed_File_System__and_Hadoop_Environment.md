## Unit 4 - HDFS (Hadoop Distributed File System) and Hadoop Environment

HDFS is a distributed file system that runs on commodity hardware and is designed to store and process large amounts of data across multiple nodes. HDFS provides high fault-tolerance, scalability, and reliability by replicating data blocks on different nodes and using checksums to detect and correct errors. HDFS also supports high-throughput access to data by allowing concurrent reads and writes from multiple clients.

Hadoop Environment is the set of software components and configurations that are required to run Hadoop applications. Hadoop Environment includes the Hadoop Common, which provides the core libraries and utilities for Hadoop, the Hadoop Distributed File System (HDFS), which provides the storage layer for Hadoop, the MapReduce framework, which provides the processing layer for Hadoop, and the YARN framework, which provides the resource management and scheduling layer for Hadoop. Hadoop Environment also includes other optional components, such as Hive, Pig, HBase, Spark, etc., that provide higher-level abstractions and functionalities for Hadoop.

To write code for HDFS and Hadoop Environment, you need to use the Hadoop command-line interface (CLI), which allows you to interact with HDFS and execute Hadoop applications. The Hadoop CLI supports various commands for HDFS operations, such as creating, copying, moving, deleting, listing, and displaying files and directories. The Hadoop CLI also supports commands for running MapReduce jobs, such as jar, streaming, pipes, etc.

Here are some examples of Hadoop HDFS commands with their usage and syntax:

- `hadoop fs -ls /` : This command lists the files and directories in the root directory of HDFS.
- `hadoop fs -mkdir /newDataFlair` : This command creates a new directory named newDataFlair in the root directory of HDFS.
- `hadoop fs -put test1 /newDataFlair` : This command copies the file test1 from the local file system to the newDataFlair directory of HDFS.
- `hadoop fs -get /newDataFlair/test1 test2` : This command copies the file test1 from the newDataFlair directory of HDFS to the local file system and renames it as test2.
- `hadoop fs -cat /newDataFlair/test1` : This command displays the contents of the file test1 in the newDataFlair directory of HDFS.
- `hadoop fs -rm /newDataFlair/test1` : This command deletes the file test1 from the newDataFlair directory of HDFS.
- `hadoop fs -rmdir /newDataFlair` : This command deletes the directory newDataFlair from the root directory of HDFS.

Here are some examples of Hadoop MapReduce commands with their usage and syntax:

- `hadoop jar wordcount.jar WordCount /input /output` : This command runs the wordcount.jar file, which contains the WordCount class, as a MapReduce job on the input directory of HDFS and writes the output to the output directory of HDFS.
- `hadoop streaming -input /input -output /output -mapper mapper.py -reducer reducer.py` : This command runs a MapReduce job using the streaming API, which allows you to use any executable or script as the mapper and reducer. The input and output directories are specified on HDFS, and the mapper.py and reducer.py files are located on the local file system.
- `hadoop pipes -input /input -output /output -program wordcount` : This command runs a MapReduce job using the pipes API, which allows you to use C++ programs as the mapper and reducer. The input and output directories are specified on HDFS, and the wordcount program is located on the local file system.