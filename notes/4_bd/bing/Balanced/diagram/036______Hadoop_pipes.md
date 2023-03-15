Hadoop pipes is the name of the C++ interface to Hadoop MapReduce. It allows you to write map and reduce functions in C++ and run them on a Hadoop cluster. Hadoop pipes uses sockets to communicate between the tasktracker and the C++ process. Here is a diagram of how Hadoop pipes works:

#### Hadoop pipes
```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Tasktracker   |      |  Tasktracker   |      |  Tasktracker   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Java Mapper   |      |  Java Reducer  |      |  Java Reducer  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  C++ Mapper    |      |  C++ Reducer   |      |  C++ Reducer   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Socket        |      |  Socket        |      |  Socket        |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Hadoop Pipes  |      |  Hadoop Pipes  |      |  Hadoop Pipes  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  HDFS          |      |  HDFS          |      |  HDFS          |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```