Hadoop Pipes is the C++ interface to Hadoop MapReduce. It allows you to write map and reduce functions in C++ and run them on a Hadoop cluster. Hadoop Pipes uses sockets to communicate between the tasktracker and the C++ process. The following diagram illustrates the basic architecture of a Hadoop Pipes job:

```
+----------------+      +----------------+      +----------------+
|  Tasktracker   |      |  Tasktracker   |      |  Tasktracker   |
|                |      |                |      |                |
|  +----------+  |      |  +----------+  |      |  +----------+  |
|  |  Mapper  |  |      |  |  Mapper  |  |      |  |  Reducer |  |
|  |  (Java)  |  |      |  |  (Java)  |  |      |  |  (Java)  |  |
|  +----+-----+  |      |  +----+-----+  |      |  +----+-----+  |
|       |        |      |       |        |      |       |        |
|       |        |      |       |        |      |       |        |
|  +----v-----+  |      |  +----v-----+  |      |  +----v-----+  |
|  |  Socket  |  |      |  |  Socket  |  |      |  |  Socket  |  |
|  +----+-----+  |      |  +----+-----+  |      |  +----+-----+  |
|       |        |      |       |        |      |       |        |
|       |        |      |       |        |      |       |        |
|  +----v-----+  |      |  +----v-----+  |      |  +----v-----+  |
|  |  C++    |  |      |  |  C++    |  |      |  |  C++    |  |
|  |  Mapper |  |      |  |  Mapper |  |      |  |  Reducer|  |
|  | Process |  |      |  | Process |  |      |  | Process |  |
|  +----------+  |      |  +----------+  |      |  +----------+  |
+----------------+      +----------------+      +----------------+
```