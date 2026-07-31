
#### Write Operations in HDFS

* HDFS (Hadoop Distributed File System) is a distributed file system used to store large amounts of data on a cluster of computers.
* Writing data to HDFS involves creating a file and writing data to it. The data is stored in blocks, and each block is stored on a different node in the cluster.
* HDFS provides a set of commands to write data to a file. The most commonly used commands are:
  * `hadoop fs -put` – This command is used to copy files from the local file system to HDFS.
  * `hadoop fs -copyFromLocal` – This command is used to copy files from a local file system to HDFS.
  * `hadoop fs -copyToLocal` – This command is used to copy files from HDFS to a local file system.
  * `hadoop fs -appendToFile` – This command is used to append data to an existing file in HDFS.
  * `hadoop fs -create` – This command is used to create an empty file in HDFS.
  * `hadoop fs -mkdir` – This command is used to create a directory in HDFS.
  * `hadoop fs -touchz` – This command is used to create an empty file in HDFS.
* HDFS also provides a streaming API which can be used to write data to a file. This API allows applications to write data to HDFS without having to create and manage files in HDFS.