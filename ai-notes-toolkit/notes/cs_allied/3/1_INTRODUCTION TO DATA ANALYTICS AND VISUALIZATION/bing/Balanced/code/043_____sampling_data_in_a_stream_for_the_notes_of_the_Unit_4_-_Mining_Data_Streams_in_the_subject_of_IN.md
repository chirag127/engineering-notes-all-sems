### Sampling data in a stream

- Stream sampling is the process of collecting a representative sample of the elements of a data stream  .
- The sample is usually much smaller than the entire stream, but can be designed to retain many important characteristics of the stream, and can be used to estimate many important aggregates on the stream  .
- Stream sampling can be useful for many applications, such as anomaly detection, clustering, classification, frequent itemset mining, and sketching .
- Stream sampling can be challenging because of the following reasons :
  - The stream is potentially infinite and unbounded, so it is impossible to store or process all the elements.
  - The stream may be non-stationary, meaning that the data distribution may change over time, so the sample needs to be updated accordingly.
  - The stream may be noisy, incomplete, or corrupted, so the sample needs to be robust and reliable.
- Stream sampling can be classified into two main categories :
  - Uniform sampling, where each element of the stream has an equal probability of being selected into the sample.
  - Weighted sampling, where each element of the stream has a different probability of being selected into the sample, depending on some criteria, such as frequency, recency, or importance.
- Stream sampling can be implemented using different techniques, such as reservoir sampling, sliding window sampling, landmark window sampling, and synopsis sampling  .
  - Reservoir sampling is a technique that maintains a fixed-size sample of the stream elements, and replaces them randomly with new elements as they arrive.
  - Sliding window sampling is a technique that maintains a sample of the stream elements that fall within a fixed time interval, and discards the elements that are older than the window.
  - Landmark window sampling is a technique that maintains a sample of the stream elements that arrive after a fixed point in time, and does not discard any elements.
  - Synopsis sampling is a technique that maintains a sample of the stream elements that are summarized by some data structure, such as a histogram, a sketch, or a synopsis.