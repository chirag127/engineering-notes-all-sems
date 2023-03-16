# Counting Distinct Elements in a Stream

- A stream is a sequence of data items that arrive in an online fashion, i.e., one by one or in batches, and cannot be stored entirely in memory.
- Counting the number of distinct elements in a stream is a fundamental problem in data stream mining, with applications in network monitoring, web analytics, database query optimization, etc.
- The challenge is to design algorithms that use limited memory and processing time, and can handle stream updates and queries efficiently and accurately.
- There are two main types of algorithms for counting distinct elements in a stream: exact and approximate.
- Exact algorithms guarantee to return the exact number of distinct elements, but they require memory proportional to the cardinality of the stream, which can be impractical for large or unbounded streams.
- Approximate algorithms trade off accuracy for memory efficiency, and provide probabilistic guarantees on the error of their estimates. They use various techniques such as hashing, sketching, sampling, etc. to compress the stream information into a small data structure, called a synopsis or a sketch, that can be queried or updated in constant time.
- Some examples of approximate algorithms are:

  - Flajolet-Martin algorithm: uses a hash function and a bit array to estimate the number of distinct elements based on the longest run of trailing zeros in the hashed values .
  - HyperLogLog algorithm: improves on the Flajolet-Martin algorithm by using multiple hash functions and bit arrays, and applying a harmonic mean to reduce the variance of the estimates.
  - KMV algorithm: uses a hash function and a sorted list of k smallest hashed values to estimate the number of distinct elements based on the inverse of the k-th smallest value.
  - Count-Min sketch: uses a two-dimensional array of counters and multiple hash functions to estimate the frequency of any element in the stream, and then applies an inequality to bound the number of distinct elements.

- The choice of the algorithm depends on the trade-off between memory, accuracy, and update/query time, as well as the characteristics of the stream, such as its distribution, skewness, etc.