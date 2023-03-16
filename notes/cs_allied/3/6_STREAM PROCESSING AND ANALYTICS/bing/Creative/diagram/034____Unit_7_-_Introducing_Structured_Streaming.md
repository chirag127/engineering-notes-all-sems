## Unit 7 - Introducing Structured Streaming

Structured Streaming is a high-level API for building scalable and fault-tolerant streaming applications using Spark SQL. It allows you to express your streaming computation as a batch-like query on a table that is continuously updated with new data. Structured Streaming automatically handles the details of partitioning, distribution, fault tolerance, and consistency guarantees.

Some of the key features of Structured Streaming are:

- Unified API: You can use the same DataFrame and Dataset API to process both static and streaming data, and write the same SQL queries for both batch and streaming data sources.
- Declarative and expressive: You can specify the logic of your streaming computation using SQL or the DataFrame/Dataset operations, without worrying about the low-level details of streaming execution.
- Event-time and late data handling: You can handle out-of-order and late-arriving data using watermarking and windowing operations, and define how to deal with late data using output modes.
- Exactly-once guarantees: You can achieve end-to-end exactly-once semantics using built-in sources and sinks that support transactions, such as Kafka, Delta Lake, and JDBC.
- Incremental and continuous processing: You can choose between micro-batch or continuous processing modes, depending on the latency and throughput requirements of your application.
- Rich built-in sources and sinks: You can read and write streaming data from a variety of sources and sinks, such as Kafka, file systems, sockets, Delta Lake, JDBC, console, and memory.
- Extensible API: You can create your own custom sources and sinks using the Source and Sink interfaces, and use the ForeachWriter API to write streaming data to external systems.
- Monitoring and debugging: You can use the web UI and the StreamingQueryListener API to monitor the status and metrics of your streaming queries, and use the explain and printSchema methods to debug your query plans.