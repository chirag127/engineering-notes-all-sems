### Event Time–Based Stream Processing

- Event time is the time when an event occurs in the real world, as opposed to the time when it is processed by a stream processing system .
- Event time is useful for handling out-of-order and late data, as well as performing time-based operations such as windowing, joining, and aggregating over a stream.
- Event time can be extracted from a field in the event payload, or from a metadata field in the event header.
- Event time can be used to define watermarking, which is a mechanism to specify how late the data is expected to be in a stream .
- Event time can be used to define triggers, which are conditions that determine when to output the results of a stream operation.
- Event time can be used to define stateful processing, which is the ability to maintain and update state information across events in a stream.
- Event time can be used to define session windows, which are dynamic windows that group events based on the activity or inactivity of a key in a stream.
- Event time can be used to define event-time joins, which are joins that match events based on their event time, rather than their arrival time.
- Event time can be used to define event-time aggregations, which are aggregations that compute results based on the event time of the events, rather than their arrival time.
- Event time can be used to define event-time ordering, which is the ability to sort events by their event time, rather than their arrival time.

: Developing stream processing applications with event time. https://www.ibm.com/docs/en/streams/5.3?topic=applications-developing-event-time
: Event-Time Processing. https://developer.confluent.io/patterns/stream-processing/event-time-processing/