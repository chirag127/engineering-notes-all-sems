## Unit 4 - Mining Data Streams

- A data stream is a sequence of data items that arrives continuously and rapidly, such as sensor readings, network packets, web clicks, etc.
- Mining data streams poses several challenges, such as:
  - The data is unbounded and potentially infinite, so it cannot be stored or processed in its entirety.
  - The data is transient and volatile, so it may not be available for future access or analysis.
  - The data is noisy and uncertain, so it may contain errors, outliers, or missing values.
  - The data is dynamic and evolving, so it may change its characteristics or distribution over time.
- To address these challenges, some techniques and methods for mining data streams are:
  - Sampling: selecting a representative subset of the data stream that preserves its essential properties and statistics.
  - Sketching: summarizing the data stream using compact data structures that support efficient queries and operations.
  - Sliding windows: dividing the data stream into fixed or variable-sized segments that capture the recent or relevant history of the stream.
  - Synopsis structures: maintaining concise representations of the data stream that can be updated incrementally and queried efficiently, such as histograms, quantiles, frequent items, etc.
  - Stream classification: building predictive models that can classify new data items in the stream based on their features and labels.
  - Stream clustering: grouping similar data items in the stream into clusters that reflect the underlying patterns or structures of the stream.
  - Stream anomaly detection: identifying data items in the stream that deviate significantly from the normal or expected behavior of the stream.
  - Stream evolution analysis: detecting and tracking changes in the data stream over time, such as concept drift, outliers, trends, etc.