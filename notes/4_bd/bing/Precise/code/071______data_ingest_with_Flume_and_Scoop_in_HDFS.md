#### Data Ingest with Flume and Sqoop in HDFS

Here is an example of how you can ingest data into HDFS using Flume and Sqoop:

1. **Flume**: Flume is a distributed, reliable, and available service for efficiently collecting, aggregating, and moving large amounts of log data. Here is an example of a Flume configuration file that can be used to ingest data into HDFS:

```
# Define a memory channel called ch1 on agent1
agent1.channels.ch1.type = memory

# Define an HDFS sink that writes to HDFS
agent1.sinks.sink1.type = hdfs
agent1.sinks.sink1.hdfs.path = /path/to/hdfs
agent1.sinks.sink1.hdfs.fileType = DataStream
agent1.sinks.sink1.channel = ch1

# Define a source that reads data from an external source
agent1.sources.source1.type = netcat
agent1.sources.source1.bind = localhost
agent1.sources.source1.port = 12345
agent1.sources.source1.channels = ch1
```

2. **Sqoop**: Sqoop is a tool designed for efficiently transferring bulk data between Apache Hadoop and structured datastores such as relational databases. Here is an example of a Sqoop command that can be used to import data from a relational database into HDFS:

```
sqoop import \
--connect jdbc:mysql://database.example.com/db \
--username user \
--password pass \
--table tablename \
--target-dir /path/to/hdfs \
--num-mappers 4
```

This command will import data from the `tablename` table in the `db` database on the `database.example.com` server into the `/path/to/hdfs` directory in HDFS using 4 mappers. You can adjust the number of mappers to optimize the performance of the data transfer.