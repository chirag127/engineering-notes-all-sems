# Counting Distinct Elements in a Stream

- A stream is a sequence of data items that are generated or processed in an online manner, without having access to the entire sequence at once.
- Counting the number of distinct elements in a stream is a fundamental problem in data stream mining, with applications in network monitoring, web analytics, database systems, and more.
- The challenge is to design algorithms that use limited memory and processing time, while providing accurate estimates of the number of distinct elements.
- There are two main approaches to solve this problem: sketching and sampling.

## Sketching

- Sketching is a technique that uses a compact data structure, called a sketch, to summarize the stream in a way that preserves some information about the distinct elements.
- A sketch is usually an array of counters or hash values that are updated as the stream elements arrive, using some hash functions or random projections.
- A sketch can be queried at any time to estimate the number of distinct elements, by applying some mathematical formula or algorithm to the sketch values.
- Some examples of sketching algorithms are:

  - Flajolet-Martin algorithm: uses a sketch of size proportional to the logarithm of the number of distinct elements, and estimates the number by counting the number of leading zeros in the sketch values .
  - HyperLogLog algorithm: improves the Flajolet-Martin algorithm by using multiple sketches and averaging their estimates, achieving a smaller relative error.
  - Count-Min sketch: uses a two-dimensional sketch and multiple hash functions, and estimates the number by taking the minimum of the sketch values for each hash function.

## Sampling

- Sampling is a technique that uses a random subset of the stream elements, called a sample, to approximate the number of distinct elements.
- A sample is usually maintained by using some random selection criteria, such as reservoir sampling, priority sampling, or min-wise hashing.
- A sample can be queried at any time to estimate the number of distinct elements, by applying some statistical formula or algorithm to the sample elements.
- Some examples of sampling algorithms are:

  - AMS algorithm: uses a sample of size proportional to the square root of the number of distinct elements, and estimates the number by using the second moment of the stream frequency distribution.
  - KMV algorithm: uses a sample of size proportional to the logarithm of the number of distinct elements, and estimates the number by using the order statistics of the sample hash values.
  - Bottom-k algorithm: uses a sample of size k, and estimates the number by using the maximum of the sample hash values.