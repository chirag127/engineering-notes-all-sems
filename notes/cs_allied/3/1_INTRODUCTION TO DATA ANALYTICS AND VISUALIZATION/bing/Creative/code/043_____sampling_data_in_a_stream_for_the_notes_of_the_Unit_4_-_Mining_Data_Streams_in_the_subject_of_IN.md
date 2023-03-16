# Sampling Data in a Stream

- Stream sampling is the process of collecting a representative sample of the elements of a data stream  .
- The sample is usually much smaller than the entire stream, but can be designed to retain many important characteristics of the stream, and can be used to estimate many important aggregates on the stream  .
- Stream sampling can be useful for many applications, such as anomaly detection, clustering, classification, frequent itemset mining, and sketching .
- Stream sampling can be challenging due to the following factors :
  - The stream is unbounded and potentially infinite, so the sample size and memory usage must be bounded and independent of the stream size.
  - The stream is dynamic and evolving, so the sample must be adaptive and responsive to the changes in the stream distribution and characteristics.
  - The stream is fast and transient, so the sample must be updated efficiently and incrementally, without requiring multiple passes over the stream or storing the entire stream.
- Stream sampling can be classified into two main categories :
  - Uniform sampling: The sample is selected such that each element in the stream has an equal probability of being included in the sample. This can be achieved by using reservoir sampling, which maintains a fixed-size sample and replaces elements randomly as new elements arrive.
  - Weighted sampling: The sample is selected such that each element in the stream has a probability of being included in the sample proportional to some weight function. This can be achieved by using priority sampling, which maintains a fixed-size sample and replaces elements based on their weights and random keys as new elements arrive.
- Stream sampling can also be performed over different time windows  :
  - Landmark window: The sample is selected from the elements that arrived since the beginning of the stream or a fixed point in time. This can be achieved by using reservoir sampling or priority sampling with a fixed-size sample.
  - Sliding window: The sample is selected from the elements that arrived within a fixed time interval or a fixed number of elements before the current time. This can be achieved by using reservoir sampling or priority sampling with a variable-size sample that discards expired elements.
  - Damped window: The sample is selected from the elements that arrived within a variable time interval or a variable number of elements before the current time, where the importance of older elements decays exponentially. This can be achieved by using priority sampling with a weight function that assigns lower weights to older elements.