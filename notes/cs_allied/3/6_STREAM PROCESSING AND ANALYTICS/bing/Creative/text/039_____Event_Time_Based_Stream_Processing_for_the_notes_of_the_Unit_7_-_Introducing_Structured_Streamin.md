### Event Time–Based Stream Processing

- Event time is a concept that refers to the time when an event occurs in the real world, as opposed to the time when it is processed by a stream processing system .
- Event time is useful for handling out-of-order and late data, which are common in streaming scenarios, such as network delays, system failures, or different data sources.
- Event time can be extracted from a timestamp field in the event payload, or from a metadata field in the event header.
- Event time can be used to define windows, which are logical groups of events based on their event time, such as tumbling windows, sliding windows, or session windows.
- Event time can also be used to trigger output actions, such as emitting results, updating state, or applying watermarks.
- Watermarks are a mechanism to specify how late an event can be relative to the event time, and to discard events that are too late to be processed.
- Event time processing requires a consistent and reliable source of event time, which can be challenging in distributed and heterogeneous environments.
- Event time processing can provide more accurate and meaningful results than processing time, which is based on the system time of the machine that processes the event .
- Event time processing is supported by various stream processing frameworks, such as IBM Streams, ksqlDB, and Azure Event Hubs.