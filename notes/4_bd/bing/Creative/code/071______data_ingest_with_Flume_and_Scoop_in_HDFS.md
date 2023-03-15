#### Data ingest with Flume and Sqoop in HDFS

Flume and Sqoop are two tools in Hadoop that can be used to gather data from different sources and load them into HDFS. Flume is mainly used for streaming data, such as log files, while Sqoop is mainly used for structured data, such as relational databases.

To ingest data with Flume, you need to configure a Flume agent that consists of three components: a source, a channel, and a sink. The source is responsible for receiving data from the data producer, such as a web server. The channel is responsible for buffering and transferring data between the source and the sink. The sink is responsible for writing data to the destination, such as HDFS.

A sample Flume configuration file for ingesting data from a spooling directory to HDFS is shown below:

```properties
# Define the agent name
agent1.sources = src1
agent1.channels = ch1
agent1.sinks = sink1

# Configure the source to read files from a spooling directory
agent1.sources.src1.type = spooldir
agent1.sources.src1.spoolDir = /var/log/flume/spool
agent1.sources.src1.fileHeader = true

# Configure the channel to use a file-based queue
agent1.channels.ch1.type = file
agent1.channels.ch1.checkpointDir = /var/log/flume/checkpoint
agent1.channels.ch1.dataDirs = /var/log/flume/data

# Configure the sink to write files to HDFS
agent1.sinks.sink1.type = hdfs
agent1.sinks.sink1.hdfs.path = hdfs://namenode:8020/flume/data
agent1.sinks.sink1.hdfs.fileType = DataStream
agent1.sinks.sink1.hdfs.writeFormat = Text
agent1.sinks.sink1.hdfs.rollInterval = 300

# Bind the source, channel, and sink
agent1.sources.src1.channels = ch1
agent1.sinks.sink1.channel = ch1
```

To ingest data with Sqoop, you need to use the sqoop import command that can connect to a relational database and transfer data to HDFS. You can specify various options, such as the database connection string, the table name, the target directory, the number of mappers, the delimiter, etc.

A sample Sqoop command for ingesting data from a MySQL table to HDFS is shown below:

```bash
sqoop import \
--connect jdbc:mysql://mysqlserver:3306/database \
--username user \
--password pass \
--table employees \
--target-dir /user/hadoop/employees \
--num-mappers 4 \
--fields-terminated-by ','
```