
### Design of HDFS 

* HDFS (Hadoop Distributed File System) is a distributed file system designed to run on commodity hardware. 
* It is highly fault-tolerant and is designed to be deployed on low-cost hardware. 
* HDFS is a block-structured file system, which means that files are divided into blocks of a fixed size and stored on different nodes in the cluster. 
* HDFS is designed to store large files, typically in the range of gigabytes to terabytes. 
* The NameNode is the master node of an HDFS cluster, which contains the metadata of all the files stored in HDFS. 
* The DataNode is the slave node of an HDFS cluster, which stores the actual data blocks of the files stored in HDFS. 
* The DataNodes communicate with the NameNode to send and receive heartbeats, which indicate that the DataNodes are alive and functioning properly. 
* HDFS provides high availability through replication, which means that multiple copies of the same file are stored on different nodes in the cluster. 
* HDFS also provides scalability, which means that it can easily scale up or down as the need arises. 
* HDFS also provides security, which means that it can secure the data stored in HDFS from unauthorized access.