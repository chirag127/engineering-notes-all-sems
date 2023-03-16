## Unit 4 - Mining Data Streams

- A data stream is a sequence of data items that arrives continuously and rapidly, such as sensor readings, network packets, web clicks, etc.
- Mining data streams poses several challenges, such as:
  - The data is unbounded and potentially infinite, so it cannot be stored or processed in its entirety.
  - The data is transient and volatile, so it may not be available for future access or analysis.
  - The data is noisy and uncertain, so it may contain errors, outliers, or missing values.
  - The data is dynamic and evolving, so it may change its characteristics or distribution over time.
- To address these challenges, some techniques and methods for mining data streams are:
  - Sampling: selecting a representative subset of the data stream to reduce its size and complexity.
  - Sketching: summarizing the data stream using compact data structures that preserve some properties or statistics of interest, such as frequency, similarity, or entropy.
  - Sliding windows: dividing the data stream into fixed or variable-sized segments that capture the recent or relevant history of the data stream.
  - Decaying windows: assigning different weights to the data items based on their recency or relevance, such that older or less important items have less influence on the analysis.
  - Online learning: updating the model or algorithm incrementally as new data arrives, without requiring access to the entire data stream or previous data.
  - Ensemble learning: combining multiple models or algorithms that are trained on different subsets or aspects of the data stream, to improve the accuracy or robustness of the analysis.
  - Concept drift detection: monitoring the data stream for changes in its characteristics or distribution, and adapting the model or algorithm accordingly.
  - Outlier detection: identifying data items that deviate significantly from the normal or expected behavior of the data stream.
  - Anomaly detection: identifying data items that indicate abnormal or suspicious events or activities in the data stream.