Hadoop Pipes is the name of the C++ interface to Hadoop MapReduce. It allows users to write map and reduce functions in C++ and run them on a Hadoop cluster. Hadoop Pipes uses sockets to communicate between the tasktracker and the C++ process. Here is a simplified diagram of how Hadoop Pipes works:

#### Hadoop pipes
```
+-----------------+        +-----------------+
|  Tasktracker    |        |  C++ process    |
|                 |        |                 |
|  Java code      |        |  C++ code       |
|                 |        |                 |
|  +-----------+  |        |  +-----------+  |
|  |  MapTask  |  |        |  |  Mapper   |  |
|  +-----------+  |        |  +-----------+  |
|  |  ReduceTask|  |        |  |  Reducer  |  |
|  +-----------+  |        |  +-----------+  |
|                 |        |                 |
+-----------------+        +-----------------+
       |  |                     |  |
       |  +---------------------+  |
       |        Socket              |
       +---------------------+  |
              HDFS              |
       +---------------------+  |
       |  |                     |  |
+-----------------+        +-----------------+
|  InputSplit     |        |  OutputFormat   |
|                 |        |                 |
|  InputFormat    |        |  RecordWriter   |
|                 |        |                 |
|  RecordReader   |        |                 |
|                 |        |                 |
+-----------------+        +-----------------+
```