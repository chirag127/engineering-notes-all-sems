# Spark Components

Spark components are the features that are provided by the Spark framework for big data processing with a faster approach. Spark is known for processing large amounts of data for analytics solutions. There are basically six components associated with Spark ecosystems, such as Spark Core, Spark SQL, Spark Streaming, Spark MLlib, Spark GraphX, and SparkR.

- **Spark Core**: This is the fundamental component of Spark that provides the basic functionality of Spark, such as task scheduling, memory management, fault recovery, interacting with storage systems, and more. It also contains the API that defines resilient distributed datasets (RDDs), which are the primary data abstraction in Spark.
- **Spark SQL**: This is a distributed framework for structured and semi-structured data processing. Using Spark SQL, Spark gets more information about the structure of data and the computation. With this information, Spark can perform extra optimization. It uses the same execution engine as Spark Core, but provides a SQL-like interface and supports various data sources, such as Hive, Parquet, JSON, and JDBC.
- **Spark Streaming**: This is a component that enables scalable, high-throughput, and fault-tolerant stream processing of live data streams. It can ingest data from sources such as Kafka, Flume, Twitter, and more, and process them using complex algorithms that express high-level functions like map, reduce, join, and window. The processed data can be pushed to databases, dashboards, or downstream systems.
- **Spark MLlib**: This is a component that provides a scalable machine learning library that consists of common learning algorithms and utilities, such as classification, regression, clustering, collaborative filtering, dimensionality reduction, feature extraction, and more. It also supports model evaluation, data import, and parallelization.
- **Spark GraphX**: This is a component that provides a graph processing framework that allows users to easily create and transform graph-structured data at scale. It supports both graph-parallel and data-parallel computation, and exposes a set of operators for manipulating graphs, such as subgraph, joinVertices, and aggregateMessages. It also includes a collection of graph algorithms, such as PageRank, connected components, and triangle counting.
- **SparkR**: This is a component that provides an R package that allows users to run R code on Spark. It allows users to use familiar R syntax to manipulate data frames and call Spark MLlib functions. It also supports distributed machine learning using Spark's ML pipelines API.

: https://www.educba.com/spark-components/
: https://www.interviewbit.com/blog/apache-spark-architecture/
: https://data-flair.training/blogs/apache-spark-ecosystem-components/
: https://www.geeksforgeeks.org/components-of-apache-spark/
: https://spark.apache.org/docs/latest/cluster-overview.html