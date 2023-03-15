# Data Ingest with Flume and Sqoop

- Data ingest is the process of transferring data from various sources to a data storage system, such as Hadoop Distributed File System (HDFS).
- Flume and Sqoop are two popular tools for data ingest in the big data world.
- Flume is a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data from various sources to HDFS or HBase .
- Sqoop is a tool designed to transfer data between relational databases and Hadoop. It supports importing data from SQL databases to HDFS or Hive, and exporting data from HDFS or Hive to SQL databases .

## Flume

- Flume has a flexible and scalable architecture based on streaming data flows. It consists of three main components: sources, channels, and sinks .
- Sources are the entities that consume data from external sources, such as HTTP, Twitter, or log files. They convert the data into Flume events and send them to one or more channels .
- Channels are the intermediaries that store the events until they are consumed by sinks. They provide reliability and fault tolerance by buffering the events in memory or on disk .
- Sinks are the entities that deliver the events to the final destination, such as HDFS, HBase, or Kafka. They can also perform transformations or filtering on the events before sending them .
- Flume supports complex and multiplexed data flows through the use of interceptors, selectors, and multiplexing .
- Interceptors are components that can modify or drop events as they travel from source to channel or from channel to sink .
- Selectors are components that can route events to different channels or sinks based on certain criteria .
- Multiplexing is the ability to send events to multiple channels or sinks from a single source or channel .

## Sqoop

- Sqoop uses MapReduce to perform parallel data transfer between relational databases and Hadoop. It can import data from a single table, a set of tables, or a custom query to HDFS or Hive, and export data from HDFS or Hive to a single table in a relational database .
- Sqoop can perform incremental imports by specifying a column that contains the last-modified timestamp or a primary key that can be used to identify new or updated rows .
- Sqoop can also perform imports or exports in batches by splitting the data into multiple chunks and assigning them to different mappers or reducers .
- Sqoop can handle various data types and formats, such as text, binary, delimited, or sequence files. It can also perform compression, encryption, or validation on the data during the transfer .
- Sqoop can integrate with other tools, such as Flume, Oozie, or Pig, to create complex data pipelines or workflows .

## References

: https://www.educba.com/sqoop-vs-flume/
: https://www.udemy.com/course/flume-and-sqoop/
: https://www.hongyusu.com/amt/data-ingestion.html
: https://stackoverflow.com/questions/19521655/whats-the-difference-between-flume-and-sqoop
: https://medium.com/xnewdata/hadoop-data-capture-flume-and-sqoop-a791435c1c27