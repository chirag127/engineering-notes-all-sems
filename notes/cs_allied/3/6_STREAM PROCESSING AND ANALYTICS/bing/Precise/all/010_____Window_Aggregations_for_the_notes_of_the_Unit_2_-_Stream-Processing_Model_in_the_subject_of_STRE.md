# Window Aggregations

Window Aggregations are a type of operation in stream processing that allows you to perform calculations on a specific window of data. This window can be defined by time or by the number of events. Some common types of window aggregations include:

1. **Tumbling Windows**: A tumbling window is a fixed-size, non-overlapping, and contiguous window. It divides the data into distinct time segments and performs the aggregation on each segment.

2. **Sliding Windows**: A sliding window is a fixed-size, overlapping, and contiguous window. It slides along the data stream and performs the aggregation on each window.

3. **Session Windows**: A session window is a dynamic, non-overlapping, and non-contiguous window. It groups events into sessions based on a specified gap of inactivity.

4. **Global Windows**: A global window is a window that spans the entire data stream. It performs the aggregation on the entire data stream.

Window aggregations can be used to perform various calculations such as sum, average, count, minimum, maximum, etc. on the data within the window. They are commonly used in stream processing applications to derive insights from real-time data.