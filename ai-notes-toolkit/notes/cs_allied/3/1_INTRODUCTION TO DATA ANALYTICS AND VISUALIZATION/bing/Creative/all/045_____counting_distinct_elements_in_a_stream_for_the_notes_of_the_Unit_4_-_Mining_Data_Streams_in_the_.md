# Counting Distinct Elements in a Stream

- A stream is a sequence of data items that arrive in an online fashion, i.e., one by one and not all at once.
- Counting the number of distinct elements in a stream is a fundamental problem in data stream mining, with applications in network monitoring, web analytics, database systems, etc.
- The challenge is to design algorithms that use limited memory and processing time, and can handle streams of arbitrary length and distribution.
- A naive solution is to store all the elements seen so far in a hash table, and update the count whenever a new element arrives. However, this requires O(n) memory, where n is the number of distinct elements, which can be impractical for large or unbounded streams.
- A better solution is to use probabilistic data structures, such as sketches or sampling, that can estimate the number of distinct elements with a small error and a high probability, using only sublinear memory.
- Some examples of probabilistic data structures for counting distinct elements are:

  - Flajolet-Martin sketch: This sketch uses a hash function to map each element to a binary string, and keeps track of the minimum number of leading zeros among all the hashed elements. The number of distinct elements is estimated by 2^r, where r is the minimum number of leading zeros. This sketch uses O(log log n) memory and has a relative error of O(1/sqrt(m)), where m is the number of bits in the sketch.
  - HyperLogLog sketch: This sketch is an improvement of the Flajolet-Martin sketch, that uses multiple hash functions and partitions the stream into buckets. The number of distinct elements is estimated by a harmonic mean of the 2^r values for each bucket, where r is the minimum number of leading zeros in each bucket. This sketch uses O(log log n) memory and has a relative error of O(1.04/sqrt(m)), where m is the number of buckets.
  - MinHash sketch: This sketch uses a hash function to map each element to a numerical value, and keeps track of the minimum value among all the hashed elements. The number of distinct elements is estimated by 1/p, where p is the probability that the minimum value is less than a threshold. This sketch uses O(1) memory and has a relative error of O(1/sqrt(n)), where n is the number of elements in the stream.
  - Count-Min sketch: This sketch uses multiple hash functions and a two-dimensional array of counters. For each element, the sketch increments the counters in the corresponding rows and columns of the array. The number of distinct elements is estimated by the minimum of the counters for each hash function. This sketch uses O(epsilon^-1 log delta^-1) memory and has a relative error of O(epsilon) with a probability of 1-delta, where epsilon and delta are user-defined parameters.

: https://studyres.com/doc/903767/counting-distinct-elements-in-a-stream
: https://en.wikipedia.org/wiki/Count-distinct_problem