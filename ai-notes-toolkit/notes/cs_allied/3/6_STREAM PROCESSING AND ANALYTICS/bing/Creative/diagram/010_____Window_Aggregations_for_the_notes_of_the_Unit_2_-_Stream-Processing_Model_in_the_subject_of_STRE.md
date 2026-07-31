### Window Aggregations

- Window aggregation is a core operation in data stream processing that computes summary statistics (e.g., count, sum, average, median, etc.) over a sliding or fixed window of events .
- Window aggregation can be used for various purposes, such as anomaly detection, trend analysis, traffic monitoring, etc.
- Window aggregation can be challenging due to the following factors :
  - Complex window types: windows can be defined by time (e.g., every 10 seconds), count (e.g., every 100 events), or session (e.g., based on user activity).
  - Complex aggregation functions: some functions are easy to compute incrementally (e.g., sum, count, min, max), while others require sorting or hashing (e.g., median, top-k, distinct count).
  - Concurrent queries: multiple queries may share the same input stream and have different window specifications or aggregation functions.
  - Out-of-order events: events may arrive late or out of their original order, which can affect the correctness and completeness of the window results.
- Window aggregation techniques can be classified into two categories :
  - Slicing-based techniques: these techniques divide the input stream into slices (or segments) and maintain partial aggregates for each slice. The final window results are computed by combining the relevant slices. Slicing-based techniques can reduce latency and memory usage, but they may incur redundant computations or storage for overlapping windows.
  - Pane-based techniques: these techniques divide the input stream into panes (or batches) and maintain full aggregates for each pane. The final window results are computed by applying the aggregation function to the relevant panes. Pane-based techniques can eliminate redundant computations and storage, but they may incur higher latency and memory usage for large or frequent panes.
- Window aggregation algorithms can be evaluated based on the following metrics :
  - Latency: the time difference between the arrival of the last event in a window and the output of the window result.
  - Memory usage: the amount of memory required to store the partial or full aggregates for the windows.
  - Throughput: the number of events processed per unit time.
  - Accuracy: the degree of correctness and completeness of the window results, especially in the presence of out-of-order events.