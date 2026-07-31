### Spark Streaming Sinks

- In Spark Streaming, output sinks store results into external storage .
- One example of a sink is the Console sink, which displays the content of the DataFrame to the console .
- Spark Streaming engine processes incoming data from various input sources, such as Kafka, Flume, HDFS/S3/any file system, etc .
- Sinks store processed data from Spark Streaming engines like HDFS/File System, relational databases, or NoSQL DB's .
- Spark will process data in micro-batches which triggers can define .
- Sink is the extension of the BaseStreamingSink contract for streaming sinks that can add batches to an output .
- Sink is part of Data Source API V1 and used in Micro-Batch Stream Processing only .
- The Spark SQL engine will take care of running it incrementally and continuously and updating the final result as streaming data continues to arrive .
- You can use the Dataset/DataFrame API in Scala, Java, Python or R to express streaming aggregations, event-time windows, stream-to-batch joins, etc .