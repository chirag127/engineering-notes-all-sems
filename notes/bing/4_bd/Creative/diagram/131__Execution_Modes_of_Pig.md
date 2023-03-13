Execution Modes of Pig are the ways of running a Pig program on different environments. Pig has two main execution modes: local mode and MapReduce mode. Local mode runs on a single JVM and is used for development, experimenting and prototyping. MapReduce mode runs on a Hadoop cluster and is used for processing large-scale data. Pig also has other execution modes such as Tez mode, Spark mode and Embedded mode. Tez mode runs on a Tez engine and is used for faster and more efficient execution. Spark mode runs on a Spark engine and is used for in-memory processing. Embedded mode runs on a Java program and is used for defining custom functions.

#### Execution Modes of Pig

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Local Mode    |     |  MapReduce     |     |  Tez Mode      |
|                |     |  Mode          |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Runs on a     |     |  Runs on a     |     |  Runs on a     |
|  single JVM    |     |  Hadoop        |     |  Tez engine    |
|                |     |  cluster       |     |                |
|                |     |                |     |                |
|  Used for      |     |  Used for      |     |  Used for      |
|  development,  |     |  processing    |     |  faster and    |
|  experimenting |     |  large-scale   |     |  more efficient|
|  and           |     |  data          |     |  execution     |
|  prototyping   |     |                |     |                |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         +----------+----------+----------+----------+
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    |                     |
                    +----------+----------+
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |
                               |