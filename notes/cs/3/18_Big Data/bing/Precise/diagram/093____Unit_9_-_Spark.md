## Unit 9 - Spark

Apache Spark is an open-source distributed computing system that can process large amounts of data quickly. It was developed in response to the limitations of the Hadoop MapReduce computing model, which is good for batch processing but not for interactive queries or iterative algorithms.

Some key features of Spark include:
- It can run on Hadoop, Mesos, standalone, or in the cloud.
- It can access diverse data sources including HDFS, Cassandra, HBase, and S3.
- It has built-in APIs in Java, Scala, Python, and R.
- It has an optimized engine that supports general execution graphs.
- It has a large standard library including SQL and DataFrames, MLlib for machine learning, GraphX for graph processing, and Stream for stream processing.

Spark's main abstraction is the Resilient Distributed Dataset (RDD), which is a distributed collection of data that can be processed in parallel. RDDs can be created from data stored in Hadoop Distributed File System (HDFS) or other storage systems, or by transforming other RDDs. RDDs are immutable, partitioned, and can be cached in memory for fast access.

Spark also provides a higher-level abstraction called DataFrames, which are similar to tables in a relational database. DataFrames can be created from structured data sources or by transforming an existing RDD. DataFrames support many relational operations such as filtering, grouping, and joining.

Spark's machine learning library, MLlib, provides many common machine learning algorithms such as classification, regression, clustering, and collaborative filtering. It also provides tools for feature extraction, transformation, and selection.

Spark Streaming is an extension of the core Spark API that enables scalable, high-throughput, fault-tolerant stream processing of live data streams. It can ingest data from many sources such as Kafka, Flume, and HDFS, and can process the data using complex algorithms expressed with high-level functions like map, reduce, join, and window.

In summary, Apache Spark is a powerful and flexible distributed computing system that can handle a wide range of data processing tasks. Its rich APIs and libraries make it easy to develop and deploy complex data processing pipelines. Its ability to cache data in memory and its optimized execution engine make it fast and efficient. Its support for multiple data sources and processing models make it a versatile tool for big data processing.