MapReduce is a software framework and programming model used for processing huge amounts of data in a distributed and parallel fashion over a cluster of machines  . MapReduce program work in two phases, namely, Map and Reduce. Map tasks deal with splitting and mapping of data while Reduce tasks shuffle and reduce the data  .

The MapReduce framework consists of a single master ResourceManager, one worker NodeManager per cluster-node, and MRAppMaster per application. The ResourceManager is responsible for allocating resources and scheduling tasks. The NodeManager is responsible for launching and monitoring the tasks on each node. The MRAppMaster is responsible for coordinating the execution of a MapReduce job.

#### Map Reduce framework and basics

```
+----------------+      +-----------------+      +-----------------+
|                |      |                 |      |                 |
|  Input Data    +----->+    Map Tasks    +----->+   Intermediate  |
|                |      |                 |      |     Data        |
+----------------+      +-----------------+      +-----------------+
                                                       |
                                                       |
                                                       v
+----------------+      +-----------------+      +-----------------+
|                |      |                 |      |                 |
|  Output Data   +<-----+   Reduce Tasks  +<-----+   Shuffled Data |
|                |      |                 |      |                 |
+----------------+      +-----------------+      +-----------------+
    ^                                                    ^
    |                                                    |
    |                                                    |
    +----------------+      +-----------------+      +---+
    |                |      |                 |      |
    |  Application   +----->+  MRAppMaster    +----->+ ResourceManager
    |                |      |                 |      |
    +----------------+      +-----------------+      +---+
                                                       |
                                                       |
                                                       v
+----------------+      +-----------------+      +-----------------+
|                |      |                 |      |                 |
|  Client        +----->+  JobClient      +----->+  NodeManager    |
|                |      |                 |      |                 |
+----------------+      +-----------------+      +-----------------+
```

: https://www.guru99.com/introduction-to-mapreduce.html
: https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
: https://www.talend.com/resources/what-is-mapreduce/
: https://www.edureka.co/blog/mapreduce-tutorial/
: https://hci.stanford.edu/courses/cs448g/a2/files/map_reduce_tutorial.pdf