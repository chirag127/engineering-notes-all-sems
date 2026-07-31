#### Data ingest with Flume and Sqoop in HDFS

Flume and Sqoop are two tools in Hadoop that can be used to gather data from different sources and load them into HDFS. Flume is mainly used for streaming data, such as log files, while Sqoop is mainly used for structured data, such as relational databases.

To ingest data with Flume, you need to configure a Flume agent that consists of three components: a source, a channel, and a sink. The source is the component that receives the data from the data source, such as a web server. The channel is the component that buffers the data before sending it to the sink. The sink is the component that writes the data to the destination, such as HDFS. A Flume agent can have multiple sources, channels, and sinks, and they can be connected in various ways to form a data flow.

To ingest data with Sqoop, you need to use the sqoop import command that specifies the source database, the destination HDFS directory, and other options, such as the table name, the query, the number of mappers, etc. Sqoop will connect to the source database, execute the query, and transfer the data in parallel to HDFS.

Here is an example of a Flume configuration file that ingests data from a spooling directory and writes it to HDFS:

```properties
# Define a spooling directory source
agent.sources.spool.type = spooldir
agent.sources.spool.spoolDir = /var/log/spool

# Define a memory channel
agent.channels.mem.type = memory
agent.channels.mem.capacity = 1000
agent.channels.mem.transactionCapacity = 100

# Define a HDFS sink
agent.sinks.hdfs.type = hdfs
agent.sinks.hdfs.hdfs.path = hdfs://namenode:8020/user/flume/spool
agent.sinks.hdfs.hdfs.fileType = DataStream
agent.sinks.hdfs.hdfs.writeFormat = Text
agent.sinks.hdfs.hdfs.rollSize = 0
agent.sinks.hdfs.hdfs.rollCount = 10000
agent.sinks.hdfs.hdfs.rollInterval = 600

# Connect the source, channel, and sink
agent.sources.spool.channels = mem
agent.sinks.hdfs.channel = mem
```

Here is an example of a Sqoop command that ingests data from a MySQL table and writes it to HDFS:

```bash
sqoop import \
  --connect jdbc:mysql://mysqlserver:3306/mydb \
  --username myuser \
  --password mypass \
  --table mytable \
  --target-dir /user/sqoop/mytable \
  --num-mappers 4
```