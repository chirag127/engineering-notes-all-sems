### Counting Distinct Elements in a Stream

- A stream is a sequence of data items that arrive in an online fashion, i.e., one by one and not all at once.
- Counting the number of distinct elements in a stream is a fundamental problem in data stream mining, with applications in network monitoring, web analytics, database systems, etc.
- The challenge is to design algorithms that use limited memory and processing time, and can handle streams of arbitrary length and distribution.
- There are two main approaches to solve this problem: exact and approximate.
- Exact algorithms aim to compute the exact number of distinct elements in the stream, but they require memory proportional to the number of distinct elements, which can be impractical for large or unbounded streams.
- Approximate algorithms trade off accuracy for efficiency, and provide probabilistic guarantees on the error of the estimation. They use memory sublinear in the number of distinct elements, and can handle streams of any size and nature.
- Some examples of approximate algorithms are:

  - Flajolet-Martin algorithm : uses a hash function to map each element to a binary string, and counts the number of leading zeros in the hashed values. The maximum number of leading zeros observed is used to estimate the number of distinct elements.
  - HyperLogLog algorithm: improves on the Flajolet-Martin algorithm by using multiple hash functions and averaging the estimates from each hash function. It reduces the memory and variance of the estimation.
  - KMV algorithm: maintains a sorted list of the k smallest hashed values seen so far, where k is a parameter. The number of distinct elements is estimated by the inverse of the average of the k smallest hashed values.
  - Count-Min sketch: uses a two-dimensional array of counters and multiple hash functions to store the frequencies of the elements. The number of distinct elements is estimated by the minimum of the counters for each element.

- These algorithms have different trade-offs in terms of memory, accuracy, update time, and query time. They can also be extended to handle streams with expiration, i.e., where elements can be removed from the stream after a certain time.