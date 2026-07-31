# Event Time–Based Stream Processing

- Event time is a concept that refers to the time when an event occurs in the real world, as opposed to the time when it is processed by a stream processing system .
- Event time is useful for handling out-of-order and late data, which are common in streaming scenarios, such as network delays, system failures, or different data sources.
- Event time can be extracted from a field in the event payload, such as a timestamp, or from a metadata attribute, such as the offset in a Kafka topic.
- Event time can be used to define windows, which are logical groups of events based on their event time, such as tumbling windows, sliding windows, or session windows.
- Event time can also be used to implement watermarks, which are markers that indicate how much event time has passed in the stream, and how much late data can be expected.
- Event time can enable consistent and accurate results in stream processing, regardless of the system time or the processing speed .
- Event time can be supported by various stream processing frameworks, such as IBM Streams, Confluent ksqlDB, or Azure Event Hubs  .