### Sources and Sinks

- In stream processing, data is continuously generated and consumed by different applications in a pipeline.
- A source is the application that produces or publishes data to the stream, such as sensors, web servers, or message brokers.
- A sink is the application that consumes or subscribes to data from the stream, such as databases, dashboards, or analytics platforms.
- A source can be a sink for another stream, and vice versa. For example, a stream processing application can consume data from one source, transform it, and emit it to another sink.
- Sources and sinks can be classified into two paradigms: publisher/subscriber (pub/sub) and source/sink.
- In the pub/sub paradigm, the source and sink are decoupled by a message broker, such as Apache Kafka, that handles the delivery and persistence of data. The source publishes data to a topic, and the sink subscribes to the same topic. The sink can consume data at its own pace, and can replay or rewind the data if needed.
- In the source/sink paradigm, the source and sink are coupled by a direct connection, such as a TCP socket or a file. The source writes data to the sink, and the sink reads data from the source. The sink has to consume data as fast as the source produces it, and cannot replay or rewind the data if missed.
- Sources and sinks can have different characteristics, such as data format, schema, reliability, scalability, and latency. Stream processing applications have to handle these differences and ensure data quality and consistency.