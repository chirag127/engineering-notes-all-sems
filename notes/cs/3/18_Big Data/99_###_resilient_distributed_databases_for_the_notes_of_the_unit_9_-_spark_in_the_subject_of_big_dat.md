### Resilient Distributed Databases for the notes of the Unit 9 - Spark in the subject of Big Data

Resilient Distributed Databases (RDDs) are a fundamental data structure in Apache Spark, a fast and flexible big data processing framework. The following are some of the key concepts related to RDDs:

1. Immutable: RDDs are immutable, meaning that once created, the data in an RDD cannot be changed.

2. Partitioned: RDDs are partitioned, meaning that the data in an RDD is divided into smaller chunks called partitions, which can be processed in parallel.

3. Resilient: RDDs are resilient, meaning that they can recover from failures in the underlying cluster, and can continue processing even if one or more nodes fail.

4. Lazy Evaluation: RDDs use lazy evaluation, meaning that transformations on RDDs are not executed until an action is performed on the RDD.

5. Caching: RDDs can be cached in memory, which can significantly improve the performance of Spark applications by reducing the amount of data that needs to be read from disk.

6. Transformations: RDDs support a wide range of transformations, including map, filter, reduce, and others, which can be used to process and analyze large data sets.

In this unit, you will learn about RDDs, including their immutability, partitioning, resilience, lazy evaluation, caching, and transformations.

This unit will provide a foundation for understanding the principles and practices of RDDs, and for exploring the various concepts and techniques used in the field of big data processing with Apache Spark.
