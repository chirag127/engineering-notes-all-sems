According to the information I found, Pig has two execution modes: local mode and MapReduce mode. In local mode, Pig runs on a single machine without Hadoop, and uses the local file system as input and output. In MapReduce mode, Pig runs on a Hadoop cluster, and uses the Hadoop Distributed File System (HDFS) as input and output. Pig also has three execution mechanisms: interactive mode, batch mode, and embedded mode. In interactive mode, Pig runs in the Grunt shell, where you can enter Pig Latin statements and commands. In batch mode, Pig runs a script file that contains Pig Latin statements. In embedded mode, Pig runs user-defined functions that are written in Java or other languages.

#### Execution Modes of Pig

```
+-----------------+    +-----------------+
|                 |    |                 |
|  Local Mode     |    |  MapReduce Mode |
|                 |    |                 |
+-----------------+    +-----------------+
|                 |    |                 |
|  Local File     |    |  HDFS File      |
|  System         |    |  System         |
|                 |    |                 |
+-----------------+    +-----------------+
|                 |    |                 |
|  Single JVM     |    |  Hadoop Cluster |
|                 |    |                 |
+-----------------+    +-----------------+
|                 |    |                 |
|  Pig Latin      |    |  Pig Latin      |
|  Statements     |    |  Statements     |
|                 |    |                 |
+-----------------+    +-----------------+
|                 |    |                 |
|  Grunt Shell    |    |  Grunt Shell    |
|  (Interactive)  |    |  (Interactive)  |
|                 |    |                 |
+-----------------+    +-----------------+
|                 |    |                 |
|  Script File    |    |  Script File    |
|  (Batch)        |    |  (Batch)        |
|                 |    |                 |
+-----------------+    +-----------------+
|                 |    |                 |
|  UDFs           |    |  UDFs           |
|  (Embedded)     |    |  (Embedded)     |
|                 |    |                 |
+-----------------+    +-----------------+
```