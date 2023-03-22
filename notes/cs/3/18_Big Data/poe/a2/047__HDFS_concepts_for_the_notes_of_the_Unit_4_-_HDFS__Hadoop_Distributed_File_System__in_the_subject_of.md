 Here is the formal content in Markdown format without any emojis or external links for the topic HDFS concepts for the notes of the Unit 4 - HDFS (Hadoop Distributed File System) in the subject of Big Data:

### HDFS concepts

1. HDFS is the primary storage system used by Hadoop applications. It is designed to store very large data sets reliably, and to stream those data sets at high bandwidth to user applications.

2. HDFS has a master-slave architecture. The HDFS Cluster consists of a single NameNode, a master server that manages the file system namespace and regulates access to files by clients. In addition, there are a number of DataNodes, usually one per node in the cluster, which manage storage attached to the nodes that they run on.

3. HDFS exposes a file system interface that allows data to be organized in a file hierarchy, though the full power of the file system is exposed through the Hadoop distributed processing framework that is built on top of it.

4. Files in HDFS are broken into block-sized chunks, which are stored redundantly for fault tolerance. The default block size is 64MB. HDFS is designed for portability across various hardware and software platforms.

5. The NameNode manages the file system namespace. It maintains the file system tree and the metadata for all the files and directories in the tree. This information is stored persistently on the local disk in the form of two files: the Namespace image and the Edit log.

6. The DataNodes are responsible for serving read and write requests from the file system's clients. The DataNodes also perform block creation, deletion, and replication upon instruction from the NameNode.

7. HDFS has a master-slave architecture. The master (NameNode) manages the file system namespace and regulates access to files by clients. The slaves (DataNodes) are responsible for serving read/write requests by clients. The slaves also perform block creation, deletion, and replication upon instruction from the master.

8. The benefits of HDFS are:
- HDFS is highly fault-tolerant.
- HDFS is designed for portability across various hardware and software platforms.
- HDFS provides high throughput access to application data.
- HDFS is suitable for applications that have large data sets.
- HDFS is designed to be deployed on low-cost hardware.