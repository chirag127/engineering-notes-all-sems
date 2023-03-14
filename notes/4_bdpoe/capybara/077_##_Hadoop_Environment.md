## Hadoop Environment

Hadoop is an open-source framework that stores and processes big data in a distributed manner. It consists of four main components: Hadoop Distributed File System (HDFS), Yet Another Resource Negotiator (YARN), MapReduce, and Hadoop Common.

### Hadoop Distributed File System (HDFS)

HDFS is the primary storage system of Hadoop. It is designed to handle large amounts of data and provides high availability and fault tolerance. Some key features of HDFS include:

- Data is stored in blocks and replicated across multiple nodes in the cluster for fault tolerance.
- HDFS supports large files and is optimized for streaming data access.
- HDFS provides a command-line interface (CLI) and a web-based graphical user interface (GUI) for managing files.

### Yet Another Resource Negotiator (YARN)

YARN is the resource manager of Hadoop. It manages the resources (CPU, memory, and disk) of the cluster and schedules jobs to run on the nodes. Some key features of YARN include:

- YARN allows different types of applications to run on the same cluster, including MapReduce, Apache Spark, and Apache Flink.
- YARN provides a centralized platform for managing and monitoring resources in the cluster.
- YARN supports dynamic allocation of resources based on the workload.

### MapReduce

MapReduce is a programming model used for processing large datasets in Hadoop. It consists of two main phases: map and reduce. The map phase processes input data and produces intermediate key-value pairs, while the reduce phase combines the intermediate results to produce the final output. Some key features of MapReduce include:

- MapReduce is fault-tolerant and can handle node failures during processing.
- MapReduce can be parallelized across multiple nodes in the cluster to improve performance.
- MapReduce provides a simple programming model for processing large datasets.

### Hadoop Common

Hadoop Common provides the common utilities and libraries used by the other components of Hadoop. It includes things like the Hadoop shell and utilities for managing HDFS and YARN. Some key features of Hadoop Common include:

- Hadoop Common provides a consistent API for interacting with HDFS and YARN.
- Hadoop Common includes libraries for processing data in various formats, including Avro, Parquet, and ORC.
- Hadoop Common supports authentication and authorization through Kerberos and other security mechanisms.

## Mnemonics and Learning Tricks

- Remember the acronym HYMN (HDFS, YARN, MapReduce, Hadoop Common) to remember the main components of Hadoop.
- Think of HDFS as the storage system, YARN as the resource manager, and MapReduce as the processing engine. This can help you remember the role of each component.
- Remember that Hadoop is designed to handle big data, so think of the "big" in big data as representing the "B" in Hadoop.