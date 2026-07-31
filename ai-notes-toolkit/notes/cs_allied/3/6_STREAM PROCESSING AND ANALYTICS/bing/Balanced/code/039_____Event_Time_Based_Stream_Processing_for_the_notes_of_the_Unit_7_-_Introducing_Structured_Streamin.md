### Event Time–Based Stream Processing

- Event time–based stream processing is the process of quickly analyzing time-based data as it is being created and before it is stored, even at the instant that it is streaming from one device to another.
- Event time is the time when the event actually occurred, as opposed to processing time, which is the time when the event reaches the processing system and is observed.
- Event time–based stream processing allows for consistent time semantics, such as joins, aggregations, and handling out-of-order and late data, in stream processing.
- Event time–based stream processing requires a mechanism to track the progress of event time in the stream, such as watermarks, which are event time markers that indicate up to what point events have been ingressed to the streaming processor.
- Event time–based stream processing enables support for real-time and batch processing, as well as multiple applications to process the stream concurrently and at different speeds.