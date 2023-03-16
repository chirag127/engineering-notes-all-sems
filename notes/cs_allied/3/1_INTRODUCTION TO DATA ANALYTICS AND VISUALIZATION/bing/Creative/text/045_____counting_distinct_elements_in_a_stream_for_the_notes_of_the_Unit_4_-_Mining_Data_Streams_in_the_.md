### Counting Distinct Elements in a Stream

- A data stream is a sequence of data items that arrive in an online fashion, and only a limited amount of memory is available to process them.
- The count-distinct problem is the problem of finding the number of distinct elements in a data stream with repeated elements.
- This problem has numerous applications in databases, network monitoring, web analytics, etc.
- A naive solution is to store all the elements seen so far in a hash table and update the count whenever a new element arrives. However, this requires a lot of memory and is not feasible for large or unbounded streams.
- A better solution is to use probabilistic data structures that can estimate the number of distinct elements with a small memory footprint and a low error rate. Some examples of such data structures are:

  - Flajolet-Martin sketch: This is a bitmap that uses a hash function to map each element to a bit position, and sets the bit to 1 if it is the first time the element is seen. The number of distinct elements is estimated by counting the number of leading zeros in the bitmap and applying a correction factor.
  - HyperLogLog: This is an improvement over the Flajolet-Martin sketch that uses multiple hash functions and partitions the bitmap into buckets. The number of distinct elements is estimated by averaging the estimates from each bucket and applying a bias correction.
  - MinHash: This is a sketch that uses a hash function to map each element to a value, and keeps track of the minimum value seen so far. The number of distinct elements is estimated by inverting the hash function and applying a correction factor.
  - Count-Min sketch: This is a sketch that uses multiple hash functions and a two-dimensional array to count the frequency of each element. The number of distinct elements is estimated by taking the minimum count from each hash function and applying a correction factor.