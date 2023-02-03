### Event Time–Based Stream Processing for the notes of the Unit 7 - Introducing Structured Streaming in the subject of STREAM PROCESSING AND ANALYTICS

Event Time-based Stream Processing is a method of processing data streams where events are processed based on the time that they occurred, rather than the time that they were received by the processing system.

In event time-based stream processing, events are assigned a timestamp, which represents the time that the event occurred. The processing system then processes the events in the order of their timestamps, allowing for the correct handling of late-arriving events and out-of-order events.

Key features of event time-based stream processing include:
1. Timestamp extraction: the process of extracting the timestamp from each event in the data stream.

2. Time-based windowing: the process of grouping events into windows based on their timestamps, allowing for time-based aggregations and transformations.

3. Late data handling: the process of handling late-arriving events, which may arrive after the processing system has already processed events with earlier timestamps.

4. Watermarking: the process of tracking the progress of event time and discarding events that are too old to be processed.

In summary, Event Time-based Stream Processing is a method of processing data streams where events are processed based on the time that they occurred, rather than the time that they were received by the processing system. Key features include timestamp extraction, time-based windowing, late data handling, and watermarking.
