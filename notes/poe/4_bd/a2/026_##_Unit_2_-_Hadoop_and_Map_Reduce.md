 Here is the content in markdown format for Unit 2 - Hadoop and Map Reduce:

## Unit 2 - Hadoop and Map Reduce

* Hadoop is an open-source software framework for distributed storage and processing of very large data sets on computer clusters built from commodity hardware.
* Hadoop has two main components:
** Hadoop Distributed File System (HDFS) - a distributed file system that stores data on commodity machines, providing very high aggregate bandwidth across the cluster.
** Hadoop MapReduce - a programming model for processing large data sets.
* The Hadoop framework itself is composed of the Hadoop Common module which provides file system and OS level abstractions, a MapReduce engine (either MapReduce/MR1 or YARN/MR2), and the Hadoop Distributed File System (HDFS).
* The Hadoop ecosystem contains other open-source modules and UIs on top of the core Hadoop framework to further increase its applicability like Hive, Pig, Spark, etc.
* The key benefits of Hadoop are:
** Scalability - Hadoop can scale up from single servers to thousands of machines, each offering local computation and storage.
** Fault tolerance - Hadoop automatically handles hardware faults and failures and continues operation without loss of data.
** Cost effectiveness - Hadoop runs on commodity hardware and is open source hence cost effective.
** Flexibility - Hadoop supports a wide variety of workloads including batch processing, real-time queries, and streaming analytics.

* The basic idea of MapReduce is to divide the tasks into independent chunks which are processed in parallel on different machines in a cluster. The two main tasks are:
** Map - takes a set of data and converts it into another set of data, where the individual elements are broken down into tuples (key/value pairs).
** Reduce - takes the output from the map as input and combines those data tuples into a smaller set of tuples.
* The key advantages of MapReduce are:
** Scalability - it can easily scale to large clusters of machines.
** Fault tolerance - it handles failures seamlessly by re-allocating work to other machines.
** Locality - it moves computation to the data instead of moving large amounts of data to the computation.
** Simplicity - it presents a simple programming model to the users.

[Detailed explanations, diagrams, examples, codes, applications, pros and cons can be added here for better understanding and learning.]