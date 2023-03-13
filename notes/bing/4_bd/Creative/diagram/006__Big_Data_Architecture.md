Big data architecture is the framework that defines the components, processes, and technologies needed to capture, store, process, and analyze big data. Big data refers to data sets that are too large or complex for traditional data processing systems to handle.

There are different types of big data architectures, depending on the requirements and goals of the data analysis. One of the most common types is the lambda architecture, which combines batch processing and stream processing to handle both historical and real-time data. Another type is the kappa architecture, which simplifies the lambda architecture by using only stream processing and treating all data as real-time.

The following diagram illustrates the basic architecture of a lambda-based big data system using ASCII art:

### Big Data Architecture

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Data Sources   |---->| Data Storage   |---->| Batch Layer    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                                      |       |
                                      |       |     +----------------+
                                      |       |     |                |
                                      |       +---->| Batch Views    |
                                      |             |                |
                                      |       +---->|                |
                                      |       |     +----------------+
                                      |       |
                                      |       |     +----------------+
                                      |       |     |                |
                                      +---->--|---->| Speed Layer    |
                                              |     |                |
                                              |     +----------------+
                                              |
                                              |     +----------------+
                                              |     |                |
                                              +---->| Serving Layer  |
                                                    |                |
                                                    +----------------+
```

The components of this architecture are:

- Data sources: These are the inputs that generate data in various formats, such as structured, semi-structured, or unstructured. Examples of data sources are web logs, social media, sensors, transactions, etc.
- Data storage: This is the layer that ingests data from the data sources and stores it in a scalable and fault-tolerant way. It also converts unstructured or semi-structured data into a structured format that can be processed by the batch layer. Examples of data storage technologies are Hadoop Distributed File System (HDFS), Amazon S3, Azure Blob Storage, etc.
- Batch layer: This is the layer that performs batch processing on the historical data stored in the data storage layer. It applies complex algorithms and transformations to the data and generates batch views, which are pre-computed results that can be queried by the serving layer. Examples of batch processing technologies are MapReduce, Spark, Hive, Pig, etc.
- Batch views: These are the outputs of the batch layer that contain the aggregated and summarized data that can answer analytical queries. They are stored in a read-optimized format that can be accessed by the serving layer. Examples of batch view technologies are HBase, Cassandra, MongoDB, etc.
- Speed layer: This is the layer that performs stream processing on the real-time data that arrives from the data sources. It applies simple algorithms and transformations to the data and generates real-time views, which are incremental updates that can be merged with the batch views by the serving layer. Examples of stream processing technologies are Storm, Spark Streaming, Kafka, etc.
- Real-time views: These are the outputs of the speed layer that contain the latest data that can answer analytical queries. They are stored in a write-optimized format that can be accessed by the serving layer. Examples of real-time view technologies are Redis, Memcached, etc.
- Serving layer: This is the layer that provides a unified view of the data to the end users or applications. It combines the batch views and the real-time views and exposes a query interface that can answer analytical queries. Examples of serving layer technologies are Druid, Impala, Presto, etc.