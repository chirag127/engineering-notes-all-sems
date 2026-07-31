## Unit 4 - Mining Data Streams

- A data stream is a sequence of data items that arrives continuously and rapidly, such as sensor readings, web clicks, tweets, etc.
- Mining data streams poses several challenges, such as:
  - The data is unbounded and potentially infinite, so it cannot be stored or processed in its entirety.
  - The data is transient and volatile, so it may not be available for future access or analysis.
  - The data is noisy and uncertain, so it may contain errors, outliers, or missing values.
  - The data is heterogeneous and evolving, so it may have different formats, sources, or distributions over time.
- To address these challenges, some techniques and methods for mining data streams are:
  - Sampling: selecting a representative subset of the data stream for analysis, based on some criteria such as random, weighted, or reservoir sampling.
  - Sketching: summarizing the data stream using a compact data structure that preserves some properties or statistics of the original data, such as count-min sketch, bloom filter, or hyperloglog.
  - Sliding window: maintaining the most recent portion of the data stream that fits in a fixed-size buffer, and discarding the older data that falls out of the window.
  - Landmark window: maintaining the data stream from a fixed starting point (landmark) until the current time, and periodically updating the summary or model based on the new data.
  - Decaying window: assigning different weights to the data items based on their recency, and using an exponential or polynomial decay function to reduce the impact of older data.
  - Algorithm output granularity: adjusting the frequency or quality of the output of the mining algorithm based on the available resources or the user's preferences, such as anytime, progressive, or approximate algorithms.
  - Algorithm adaptation: updating the parameters or structure of the mining algorithm based on the changes or trends in the data stream, such as concept drift, novelty detection, or online learning.