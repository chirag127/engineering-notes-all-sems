### Event Time–Based Stream Processing

- Event time is a concept that refers to the time when an event occurs in the real world, as opposed to the time when it is processed by a stream processing system .
- Event time is useful for handling out-of-order and late data, which are common in streaming scenarios, such as network delays, system failures, or different data sources.
- Event time can be extracted from a field in the event payload, such as a timestamp, or from a metadata attribute, such as the offset in a Kafka topic.
- Event time can be used to define windows, which are logical groups of events based on their event time, such as tumbling, hopping, sliding, or session windows.
- Event time can also be used to trigger computations, such as aggregations, joins, or filters, based on the arrival of events or the expiration of windows.
- Event time requires a mechanism to deal with watermarks, which are estimates of the progress of event time in a stream, and to handle late events that arrive after the watermark.
- Event time can be supported by different stream processing frameworks, such as IBM Streams, Confluent ksqlDB, or Azure Event Hubs  .
- Event time enables consistent and accurate results in stream processing, regardless of the system time or the processing speed.