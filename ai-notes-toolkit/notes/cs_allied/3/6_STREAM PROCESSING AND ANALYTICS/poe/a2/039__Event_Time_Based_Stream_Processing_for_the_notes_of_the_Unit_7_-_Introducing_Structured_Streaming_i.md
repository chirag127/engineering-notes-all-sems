 Here is the content in markdown format without any emojis or external links and in formal tone:

### Event Time–Based Stream Processing

#### For notes of Unit 7 - Introducing Structured Streaming

- Event time: The time when an event actually occurred in the real world.
- Processing time: The time when an event is processed by a streaming application.
- In event time processing, windows are defined based on event time, not processing time. This leads to more accurate results as it accounts for out-of-order events and delays.
- Watermarks are used to keep track of the progress of event time and trigger window operations at the correct event time.
- Event time allows streaming aggregations (like counts, averages) to be accurate and not affected by delays or out-of-order events.
- Event time processing requires stateful operations as stream processors need to buffer some events to account for out-of-order events and delays.
- Event time semantics can be specified in structured streaming using `eventTime` column and `watermark` configuration.

The points cover the key aspects of event time-based stream processing. The content is written in a formal tone with no emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.