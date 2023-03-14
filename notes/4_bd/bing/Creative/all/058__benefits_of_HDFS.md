#### Benefits of HDFS

HDFS stands for Hadoop Distributed File System. It is a distributed file system that handles large data sets running on commodity hardware. It is one of the major components of Apache Hadoop, the others being MapReduce and YARN. HDFS is designed to be scalable, fault-tolerant, and suitable for applications that have large data sets and require high throughput data access. Some of the benefits of HDFS are:

- **Cost effectiveness**: HDFS can store data on inexpensive off-the-shelf hardware, which reduces the storage costs. Also, HDFS is an open source software that comes with no licensing or support cost  .
- **Large data set storage**: HDFS can store data sets that are typically gigabytes to terabytes in size, and can scale to hundreds or thousands of nodes in a single cluster  .
- **Fault tolerance**: HDFS can detect and recover from failures of nodes or disks, by storing multiple copies of data in separate systems. By default, HDFS replicates each block of data three times, but this can be configured according to the needs of the application  .
- **High throughput**: HDFS can deliver more than 2 GB of data per second thanks to its cluster architecture. It also supports streaming access to data sets, which is suitable for batch processing and analytics .
- **Data locality**: HDFS can optimize the performance of the cluster by moving the computation to the data, rather than the other way around. This reduces the network traffic and increases the processing speed. HDFS also allows the application to specify the preferred location of the data, such as the same rack or node .

A possible mnemonic to remember the benefits of HDFS is:

**C**ost effective
**L**arge data set storage
**F**ault tolerant
**H**igh throughput
**D**ata locality

CLFHD: **C**an **L**earn **F**rom **H**uge **D**ata