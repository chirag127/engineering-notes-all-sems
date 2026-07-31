### Counting distinct elements in a stream

- A stream is a sequence of data items that are generated continuously and possibly infinitely.
- Counting distinct elements in a stream is the problem of finding the number of different data items in the stream, without storing the entire stream in memory.
- This is a challenging problem because the stream may be very large, unbounded, or dynamic, and the memory available may be limited.
- There are several applications of counting distinct elements in a stream, such as network monitoring, web analytics, database query optimization, and data mining.
- There are two main approaches to counting distinct elements in a stream: exact and approximate.
  - Exact algorithms store all the distinct elements seen so far in a data structure, such as a hash table or a trie, and update it whenever a new element arrives. They can report the exact number of distinct elements at any time, but they require a lot of memory and may not be feasible for large or unbounded streams.
  - Approximate algorithms use probabilistic data structures, such as sketches or samples, that can estimate the number of distinct elements with some error bound and confidence level. They require much less memory and can handle large or unbounded streams, but they may not be accurate for small or skewed streams.
- Some examples of approximate algorithms are:
  - Flajolet-Martin algorithm: It uses a sketch based on the longest run of trailing zeros in the binary representation of the hashed elements. It can estimate the number of distinct elements with a relative error of 0.78/sqrt(m), where m is the size of the sketch.
  - HyperLogLog algorithm: It improves the Flajolet-Martin algorithm by using multiple sketches and a harmonic mean to reduce the variance of the estimate. It can estimate the number of distinct elements with a relative error of 1.04/sqrt(m), where m is the size of the sketch.
  - Count-Min sketch: It uses a two-dimensional sketch based on the minimum value of the hashed elements in each row. It can estimate the number of distinct elements with a relative error of epsilon and a confidence level of 1-delta, where epsilon and delta are parameters that control the size of the sketch.
  - Sampling-based algorithms: They use a random sample of the stream elements to estimate the number of distinct elements. They can estimate the number of distinct elements with a relative error of epsilon and a confidence level of 1-delta, where epsilon and delta are parameters that control the size of the sample.