### Performance Tuning for the notes of the Unit 8 - Introducing Spark Streaming in the subject of STREAM PROCESSING AND ANALYTICS

- Spark Streaming is a module of Spark that allows processing of real-time data streams from various sources such as Kafka, Flume, HDFS, etc.
- Spark Streaming performance tuning is the process of making rapid and timely changes to Spark configurations to ensure all processes and resources are optimized and function smoothly.
- Spark Streaming performance tuning can be done in several ways, such as:
  - Use DataFrames/Datasets over RDDs for Spark jobs, as they have higher-level APIs and optimizations.
  - Use coalesce() over repartition() when you want to reduce the number of partitions, as coalesce() avoids a full shuffle.
  - Use persist() or cache() to reuse intermediate results of DStreams, as they can reduce recomputation and I/O costs.
  - Tune the batch interval and the level of parallelism according to the workload and the cluster resources.
  - Tune the data serialization format and the memory usage to reduce the overhead of data transfer and storage.
  - Use the adaptive query execution feature to simplify the tuning of shuffle partition number and other query optimizations.