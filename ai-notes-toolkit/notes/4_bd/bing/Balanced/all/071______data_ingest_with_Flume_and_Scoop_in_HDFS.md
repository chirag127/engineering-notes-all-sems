#### Data ingest with Flume and Sqoop in HDFS

- Data ingestion is the process of collecting, transferring, and loading data from various sources into a data store, such as HDFS, for analysis and processing.
- Flume and Sqoop are two tools in Hadoop that are used for data ingestion from different sources and load them into HDFS.
- Flume is a distributed, reliable, and scalable service for collecting, aggregating, and moving large amounts of streaming data, such as log files, sensor data, social media data, etc.
- Sqoop is a tool for transferring bulk data between Hadoop and structured data sources, such as relational databases, data warehouses, etc.

##### Flume
- Flume consists of three main components: sources, channels, and sinks.
- A source is the component that receives data from an external source, such as a web server, a message queue, a spooling directory, etc.
- A channel is the component that temporarily stores the data received by the source until it is consumed by a sink.
- A sink is the component that delivers the data from the channel to a destination, such as HDFS, HBase, Kafka, etc.
- A Flume agent is a process that runs on a node and hosts the sources, channels, and sinks.
- A Flume flow is a data flow from a source to a sink via a channel, which can be configured using a Flume configuration file.
- A Flume topology is a network of Flume agents that are connected by data flows, which can be used to handle complex data ingestion scenarios, such as fan-in, fan-out, multiplexing, etc.

##### Sqoop
- Sqoop uses a connector-based architecture that allows it to communicate with various data sources using JDBC or other APIs.
- Sqoop supports two types of operations: import and export.
- An import operation transfers data from a data source to HDFS or Hive or HBase.
- An export operation transfers data from HDFS or Hive or HBase to a data source.
- Sqoop can perform parallel data transfer using multiple map tasks, which can be configured using the --num-mappers option.
- Sqoop can also perform incremental data transfer using the --incremental option, which can be based on an append mode or a lastmodified mode.
- Sqoop can also perform data transformation using the --query option, which allows the user to specify a SQL query to filter or join the data before importing or exporting.

##### Advantages and disadvantages of Flume and Sqoop
- Flume is a better choice when moving bulk streaming data from various sources that generate data continuously, such as web servers, sensors, social media, etc.
- Sqoop is a better choice when moving bulk data from structured data sources that store data in tables, such as relational databases, data warehouses, etc.
- Flume can handle unstructured or semi-structured data, such as log files, JSON, XML, etc.
- Sqoop can handle structured or tabular data, such as CSV, SQL, etc.
- Flume can perform data filtering, masking, or enrichment using interceptors or custom code.
- Sqoop can perform data transformation using SQL queries or custom code.
- Flume can deliver data to multiple destinations using fan-out flows or multiplexing flows.
- Sqoop can only deliver data to one destination at a time.

##### Mnemonics and learning tricks
- Flume is for streaming data, Sqoop is for structured data.
- Flume has sources, channels, and sinks, Sqoop has connectors, import, and export.
- Flume flows from source to sink, Sqoop scoops from source to destination.