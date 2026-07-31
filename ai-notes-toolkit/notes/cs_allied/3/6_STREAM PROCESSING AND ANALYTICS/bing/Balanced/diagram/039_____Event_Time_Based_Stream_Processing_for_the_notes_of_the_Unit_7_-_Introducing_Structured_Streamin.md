### Event Time–Based Stream Processing

- Event time is a concept that refers to the time when an event occurs in the real world, as opposed to the time when it is processed by a stream processing system .
- Event time is often embedded in the event data as a timestamp attribute, which can be used by the stream processing system to order and group events based on their logical occurrence .
- Event time is useful for handling out-of-order and late events, which are common in distributed and asynchronous systems, as well as for performing time-based operations such as windowing and joining .
- Event time–based stream processing requires the stream processing system to support event time semantics, such as watermarking, triggers, and allowed lateness .
- Watermarking is a mechanism that estimates the progress of event time in a stream, and allows the system to discard late events that arrive after the watermark .
- Triggers are rules that specify when to emit the results of a time-based operation, such as at the end of a window, or when a certain number of events have arrived, or when the watermark passes a certain threshold .
- Allowed lateness is a parameter that defines how long the system will wait for late events after the watermark, and how to update the results if late events arrive within the allowed lateness .
- Event time–based stream processing can provide more accurate and consistent results than processing time–based stream processing, which relies on the system time of the machine that processes the events  .
- Event time–based stream processing can also enable stateful stream processing, which allows the system to maintain and update the state of an event or a group of events over time, such as a counter, a list, or a map .
- Event time–based stream processing can be implemented using various frameworks and platforms, such as IBM Streams, ksqlDB, and Azure Event Hubs.