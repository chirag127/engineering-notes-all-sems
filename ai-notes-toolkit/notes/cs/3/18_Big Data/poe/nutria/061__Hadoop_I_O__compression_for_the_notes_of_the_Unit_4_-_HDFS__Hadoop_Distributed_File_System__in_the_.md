
### Hadoop I/O: Compression for the Notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the Subject of Big Data

* Hadoop I/O is the process of reading and writing data from and to HDFS (Hadoop Distributed File System). 
* Compression is a way of reducing the amount of data stored on HDFS by using algorithms to identify patterns in the data and reduce its size.
* There are two types of compression available in Hadoop: splittable and non-splittable.
* Splittable compression algorithms, such as LZO and Snappy, are designed to compress and decompress data in a way that allows it to be split into multiple parts and processed in parallel.
* Non-splittable compression algorithms, such as Gzip, are designed to compress and decompress data in a way that requires it to be processed in one piece.
* The most commonly used compression algorithm in Hadoop is Snappy, as it provides a good balance between compression ratio and performance.
* Compression can reduce the amount of storage space required and can improve the performance of Hadoop jobs by reducing the amount of data that needs to be transferred.