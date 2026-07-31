### HDFS

- HDFS stands for Hadoop Distributed File System. It is a distributed file system that handles large data sets running on commodity hardware. It is one of the major components of Apache Hadoop, the others being MapReduce and YARN .
- HDFS is designed to be fault-tolerant, scalable, and reliable. It can store data across thousands of nodes and provide high throughput access to the data. It also supports replication and recovery of data in case of node failures  .
- HDFS has a master-slave architecture, where one node acts as the NameNode (master) and the rest of the nodes act as DataNodes (slaves). The NameNode manages the file system namespace, the metadata of files and directories, and the mapping of files to blocks. The DataNodes store the actual data blocks and serve read and write requests from the clients.
- HDFS follows a write-once-read-many model, where files are split into fixed-size blocks (typically 64 MB or 128 MB) and distributed across the DataNodes. Each block is replicated to a configurable number of DataNodes (default is 3) for fault tolerance. Once a file is written, it cannot be modified, only appended or deleted.
- HDFS provides a Java API and a command-line interface for interacting with the file system. It also supports a web-based interface for browsing the file system and monitoring the cluster status. HDFS can be accessed by other applications using the Hadoop FileSystem API, which supports multiple file system implementations, such as local, FTP, S3, etc.
- HDFS is suitable for storing and processing large volumes of unstructured or semi-structured data, such as text, images, audio, video, etc. It is not suitable for low-latency or random access, or for storing small files that can cause metadata overhead. HDFS is widely used by companies and organizations that need to handle and store big data, such as Facebook, Yahoo, Netflix, etc .

#### Mnemonics and learning tricks

- A possible mnemonic to remember the components of HDFS is **N**ame**N**ode, **D**ata**N**ode, **B**lock, **R**eplication (NN-DN-BR).
- A possible learning trick to understand the write-once-read-many model of HDFS is to compare it to a CD-ROM, where data can be written once and read many times, but not modified or overwritten.