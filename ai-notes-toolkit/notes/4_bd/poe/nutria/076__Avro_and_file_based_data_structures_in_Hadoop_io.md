
##### Avro and File Based Data Structures in Hadoop io

* Avro is a data serialization system used to store and exchange data between programs written in any language. It is an open source project developed by Apache Software Foundation.
* Avro stores data in a compact binary format that is easy to serialize and deserialize. It also supports schema evolution, which allows for the data to be read and written even if the schema changes over time.
* File-based data structures are used in Hadoop to store data in the Hadoop Distributed File System (HDFS). These data structures are used to store and process large amounts of data.
* HDFS stores data in files, which are divided into blocks and stored across multiple nodes in the cluster. This allows for data to be processed in parallel, which is necessary for large-scale data processing.
* The data stored in HDFS is organized into a hierarchical structure, with directories and files nested within each other. This structure allows for data to be quickly accessed and processed.
* Hadoop provides a number of data structures, such as the SequenceFile, AvroFile, and MapFile, which are used to store data in an efficient and organized manner.
* Avro provides a number of advantages when used in conjunction with Hadoop. It supports schema evolution, which allows for data to be read and written even if the schema changes over time. It also provides a simple, compact binary format for data storage and exchange. Finally, it supports data compression, which reduces the amount of storage space required for data.