# Data Ingest with Flume and Scoop

## Flume
- Flume is a tool for collecting, aggregating, and moving large amounts of streaming data from various sources to a centralized data store, such as HDFS or HBase.
- Flume supports a variety of sources, such as log files, syslogs, social media, web servers, etc.
- Flume also supports a variety of sinks, such as HDFS, HBase, Kafka, etc.
- Flume has a flexible and scalable architecture, based on the concept of agents, which are composed of three components: sources, channels, and sinks.
- Sources are responsible for consuming data from external sources and passing them to channels.
- Channels are responsible for buffering and transferring data between sources and sinks.
- Sinks are responsible for delivering data to the destination data store.
- Flume agents can be configured and deployed independently, and can be chained together to form complex data pipelines.

## Scoop
- Scoop is a tool for transferring data between relational databases and Hadoop.
- Scoop supports a variety of databases, such as MySQL, Oracle, PostgreSQL, etc.
- Scoop can import data from a database table or a custom query to HDFS, Hive, or HBase.
- Scoop can also export data from HDFS, Hive, or HBase to a database table.
- Scoop can perform parallel and incremental data transfers, and can handle data types, compression, and encryption.
- Scoop can also generate code for MapReduce, Spark, or Hive to process the imported data.