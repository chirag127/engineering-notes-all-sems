Big Data applications are software solutions that deal with large and complex data sets that cannot be handled by traditional database systems. They typically involve one or more of the following types of workload:

- Batch processing of big data sources at rest.
- Real-time processing of big data in motion.
- Interactive analysis of big data sources.
- Machine learning and advanced analytics on big data sources.

A common big data architecture consists of the following layers:

- Data sources: The origin of the data, such as sensors, web logs, social media, etc.
- Data ingestion: The process of collecting, validating, and moving the data from the sources to a data store or a processing engine.
- Data storage: The repository where the data is persisted, such as a distributed file system, a data lake, a data warehouse, etc.
- Data processing: The engine that performs the transformation, analysis, and computation on the data, such as MapReduce, Spark, Flink, etc.
- Data consumption: The interface that allows the users to access, visualize, and utilize the data, such as dashboards, reports, APIs, etc.

The following diagram illustrates the basic architecture of a big data application using ASCII art:

```
+-------------+     +-------------+     +-------------+
| Data Source | --> | Data Ingest | --> | Data Store  |
+-------------+     +-------------+     +-------------+
                                  |          |
                                  |          v
                                  |     +-------------+
                                  +-->  | Data Process|
                                        +-------------+
                                               |
                                               v
                                        +-------------+
                                        | Data Consume|
                                        +-------------+
```