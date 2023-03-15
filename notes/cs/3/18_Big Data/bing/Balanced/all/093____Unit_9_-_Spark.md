## Unit 9 - Spark

- Spark is an open source framework for distributed data processing that supports several big data scenarios, such as extract, transform, and load (ETL), machine learning, real-time analytics, and graph processing .
- Spark was introduced by Apache Software Foundation in 2014 to speed up the Hadoop computational process, which relies on the MapReduce paradigm that is slow for iterative and interactive applications.
- Spark is not a modified version of Hadoop and does not depend on Hadoop, because it has its own cluster management system. However, Spark can run on top of Hadoop and access Hadoop data sources, such as HDFS, Hive, and HBase.
- Spark provides a faster and more general data processing platform than Hadoop, because it allows data to be cached in memory across multiple parallel operations, whereas Hadoop writes intermediate data to disk.
- Spark also supports a rich set of higher-level tools, such as Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for incremental computation and stream processing.
- Spark can be programmed in Scala, Python, Java, R, and SQL, and provides a unified and expressive API for manipulating data. Spark also provides a shell for interactive data analysis in Scala and Python.