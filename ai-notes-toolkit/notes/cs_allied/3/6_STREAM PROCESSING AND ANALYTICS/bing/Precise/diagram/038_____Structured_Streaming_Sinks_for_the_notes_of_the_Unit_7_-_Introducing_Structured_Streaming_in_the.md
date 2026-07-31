### Structured Streaming Sinks

Structured Streaming supports several types of sinks for writing the output of a streaming query:

1. **File Sink**: Writes the output of the streaming query to a file system, such as HDFS or a local file system. The output can be written in various formats, including Parquet, JSON, CSV, and ORC.

2. **Kafka Sink**: Writes the output of the streaming query to a Kafka topic. The output can be written in various formats, including Avro, JSON, and CSV.

3. **Foreach Sink**: Allows the user to specify a custom sink by providing a function that is called for each row in the output. This can be used to write the output to a custom data store or to perform custom processing on the output.

4. **Console Sink**: Writes the output of the streaming query to the console. This is mainly used for debugging purposes.

5. **Memory Sink**: Writes the output of the streaming query to memory. This is mainly used for testing purposes.

Each sink has its own set of options and configurations that can be used to customize its behavior. It is important to choose the appropriate sink for the specific use case and to configure it correctly to ensure that the streaming query performs as expected.