#### Map Reduce types in map reduce
```
+---------------------+
|   MapReduce Types   |
+----------+----------+
|          |          |
|  Batch   |  Stream  |
|          |          |
+----------+----------+
```
MapReduce is a programming model for processing large data sets with a parallel, distributed algorithm on a cluster. There are two main types of MapReduce: Batch and Stream.

Batch MapReduce is used for processing large amounts of static data, where the data is divided into chunks and processed in parallel by multiple machines. The results are then combined to produce the final output.

Stream MapReduce, on the other hand, is used for processing data in real-time as it is generated. The data is processed in parallel by multiple machines as it arrives, and the results are continuously updated.
