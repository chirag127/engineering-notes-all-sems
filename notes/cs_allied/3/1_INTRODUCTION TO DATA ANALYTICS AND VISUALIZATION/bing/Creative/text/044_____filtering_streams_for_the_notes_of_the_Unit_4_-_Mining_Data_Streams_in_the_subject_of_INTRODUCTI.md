### Filtering Streams

- Filtering streams is a common task in data mining, where we want to select a subset of data from a large and potentially infinite stream of data.
- Filtering streams can be useful for various purposes, such as sampling, cleaning, transforming, aggregating, or querying data in a stream.
- Filtering streams can be challenging because of the following characteristics of data streams:
  - High volume and velocity: Data streams can generate a large amount of data at a fast rate, which may exceed the memory or processing capacity of the system.
  - Unbounded and dynamic: Data streams can be infinite and unpredictable, which may require adaptive and incremental algorithms that can handle changes in the data distribution or concept drift.
  - One-pass and online: Data streams can only be accessed once and in a sequential order, which may require efficient and approximate algorithms that can produce results with a single scan and minimal delay.
- Filtering streams can be performed by using different techniques, such as:
  - Filters: Filters are conditions or expressions that can be applied to a data stream to select or exclude data that satisfy certain criteria. Filters can be defined by using the filter editor dialog boxes in Data Mining Designer, the Filter property of the mining model, or programmatically by using AMO.
  - Sampling: Sampling is a technique that can be used to reduce the size of a data stream by selecting a representative subset of data that preserves the essential characteristics of the original stream. Sampling can be performed by using various methods, such as uniform sampling, reservoir sampling, stratified sampling, or weighted sampling .
  - Sketching: Sketching is a technique that can be used to summarize a data stream by using a compact data structure that can support various queries or operations on the stream. Sketching can be performed by using various methods, such as count-min sketch, bloom filter, hyperloglog, or distinct sampling .
  - Sliding windows: Sliding windows are a technique that can be used to divide a data stream into finite and overlapping segments that capture the recent or relevant data in the stream. Sliding windows can be defined by using various parameters, such as size, duration, or expiration time .