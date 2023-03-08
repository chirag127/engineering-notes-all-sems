### Map Reduce framework and basics

Map Reduce is a programming model that allows for processing and generating large data sets with a parallel and distributed algorithm on a cluster. It is a framework that is used to write applications to process huge amounts of data in parallel on large clusters of commodity hardware. Here are some of the basics of the Map Reduce framework:

1. **Map Function:** The map function is responsible for taking an input record and generating a set of intermediate key-value pairs. The map function is executed in parallel across a cluster of machines.

2. **Reduce Function:** The reduce function takes the output from the map function and combines all the intermediate values associated with the same intermediate key. The reduce function is also executed in parallel across a cluster of machines.

3. **Input Data:** The input data for a Map Reduce job is typically stored in a distributed file system like Hadoop Distributed File System (HDFS).

4. **Output Data:** The output data for a Map Reduce job is also stored in a distributed file system like HDFS.

5. **Job Tracker and Task Tracker:** Map Reduce jobs are managed by a Job Tracker and executed by a set of Task Trackers. The Job Tracker is responsible for coordinating the Map Reduce job and monitoring its progress, while the Task Trackers are responsible for executing the individual tasks.

6. **Advantages of Map Reduce:** The Map Reduce framework offers several advantages, including scalability, fault tolerance, and parallel processing. It can process large amounts of data in parallel on a cluster of machines and can recover from failures without losing any data.

7. **Disadvantages of Map Reduce:** Map Reduce can be slow for small datasets due to the overhead of setting up the Map Reduce job. It also requires a significant amount of disk I/O, which can be a bottleneck for some applications.

8. **Example Applications:** Map Reduce is commonly used for applications like data warehousing, data mining, log processing, and web indexing.

In summary, the Map Reduce framework is a powerful tool for processing large amounts of data in parallel on a cluster of machines. It allows for scalability, fault tolerance, and parallel processing and is commonly used for applications like data warehousing, data mining, log processing, and web indexing.