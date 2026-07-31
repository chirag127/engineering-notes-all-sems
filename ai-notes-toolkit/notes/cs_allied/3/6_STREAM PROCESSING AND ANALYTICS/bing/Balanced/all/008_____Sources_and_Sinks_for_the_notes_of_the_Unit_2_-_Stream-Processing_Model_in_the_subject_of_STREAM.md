# Sources and Sinks

- Sources and sinks are the components of a stream processing application that interact with the external data sources and destinations.
- A source is the component that consumes data from an external source and emits it to the stream processing application. A source can be a message broker, a database, a web service, a sensor, or any other data producer.
- A sink is the component that consumes data from the stream processing application and writes it to an external destination. A sink can be a message broker, a database, a web service, a file system, or any other data consumer.
- Sources and sinks can be configured to use different protocols, formats, and schemas for data ingestion and egress. For example, a source can consume data from Kafka in JSON format and a sink can write data to Hadoop in Parquet format.
- Sources and sinks can also perform some basic transformations on the data, such as filtering, mapping, or aggregating, before sending or receiving it. For example, a source can filter out unwanted events based on some criteria and a sink can aggregate data into batches before writing it.
- Sources and sinks are usually stateless and scalable, meaning they can handle large volumes of data and can be replicated or partitioned to increase throughput and availability.