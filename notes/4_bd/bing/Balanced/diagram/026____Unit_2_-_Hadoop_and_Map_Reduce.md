## Unit 2 - Hadoop and Map Reduce

Hadoop and Map Reduce are part of the Apache Hadoop ecosystem, a framework that develops large-scale data processing. Hadoop uses a distributed storage layer called Hadoop Distributed File System (HDFS) to store data across multiple nodes in a cluster. Hadoop also uses a processing layer called Map Reduce to process the data using parallel and distributed algorithms. Map Reduce works on tasks related to a job, which is a user-defined program that consists of two phases: map and reduce. The map phase takes the input data and transforms it into key-value pairs. The reduce phase takes the key-value pairs and aggregates them based on the key. The following diagram shows the data flow of a Map Reduce job in Hadoop.

```
+----------------+       +----------------+       +----------------+
|                |       |                |       |                |
|   Input Data   +------>+     Mapper     +------>+   Partitioner  |
|                |       |                |       |                |
+----------------+       +----------------+       +----------------+
                                                 /   |   |   |   \
                                                /    |   |   |    \
                                               /     |   |   |     \
                                              /      |   |   |      \
                                             /       |   |   |       \
                                            /        |   |   |        \
                                           /         |   |   |         \
                                          /          |   |   |          \
                                         /           |   |   |           \
                                        /            |   |   |            \
                                       /             |   |   |             \
                                      /              |   |   |              \
                                     /               |   |   |               \
                                    /                |   |   |                \
                                   /                 |   |   |                 \
                                  /                  |   |   |                  \
                                 /                   |   |   |                   \
                                /                    |   |   |                    \
                               /                     |   |   |                     \
                              /                      |   |   |                      \
                             /                       |   |   |                       \
                            /                        |   |   |                        \
                           /                         |   |   |                         \
                          /                          |   |   |                          \
                         /                           |   |   |                           \
                        /                            |   |   |                            \
                       /                             |   |   |                             \
                      /                              |   |   |                              \
                     /                               |   |   |                               \
                    /                                |   |   |                                \
                   /                                 |   |   |                                 \
                  /                                  |   |   |                                  \
                 /                                   |   |   |                                   \
                /                                    |   |   |                                    \
               /                                     |   |   |                                     \
              /                                      |   |   |                                      \
             /                                       |   |   |                                       \
            /                                        |   |   |                                        \
           /                                         |   |   |                                         \
          /                                          |   |   |                                          \
         /                                           |   |   |                                           \
        /                                            |   |   |                                            \
       /                                             |   |   |                                             \
      /                                              |   |   |                                              \
     /                                               |   |   |                                               \
    /                                                |   |   |                                                \
   /                                                 |   |   |                                                 \
  /                                                  |   |   |                                                  \
 /                                                   |   |   |                                                   \
/                                                    |   |   |                                                    \
+----------------+       +----------------+       +----------------+       +----------------+       +----------------+
|                |       |                |       |                |       |                |       |                |
|   Shuffle &    +------>+     Sorter     +------>+    Reducer     +------>+    Combiner    +------>+   Output Data  |
|    Copy Data   |       |                |       |                |       |                |       |                |
+----------------+       +----------------+       +----------------+       +----------------+       +----------------+
```