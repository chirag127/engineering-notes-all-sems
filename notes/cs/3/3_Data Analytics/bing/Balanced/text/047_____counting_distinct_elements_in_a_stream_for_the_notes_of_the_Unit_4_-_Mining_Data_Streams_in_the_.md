### Counting Distinct Elements in a Stream

- The problem of finding the number of distinct elements in a data stream with repeated elements is also known as the count-distinct problem or the cardinality estimation problem.
- This problem has numerous applications in databases, data mining, network monitoring, web analytics, etc.
- The challenge of this problem is to design algorithms that use limited memory and processing time, while providing accurate estimates of the number of distinct elements.
- There are two main approaches to solve this problem: sketching and sampling.
  - Sketching algorithms use hash functions to map the elements of the stream to a small array of counters, called a sketch, and then use the sketch to estimate the number of distinct elements.
  - Sampling algorithms randomly select a subset of the elements from the stream, and then use the subset to estimate the number of distinct elements.
- Some examples of sketching algorithms are:
  - Flajolet-Martin algorithm: This algorithm uses a bit array of size m, and sets the ith bit to 1 if the hash value of an element ends with i zeros. The number of distinct elements is estimated by 2^R, where R is the position of the leftmost zero bit in the array.
  - HyperLogLog algorithm: This algorithm improves the Flajolet-Martin algorithm by using multiple bit arrays, called registers, and averaging their estimates. The number of distinct elements is estimated by alpha * m^2 / (sum of 1/2^M_i), where alpha is a constant, m is the number of registers, and M_i is the position of the leftmost zero bit in the ith register.
  - Count-Min sketch: This algorithm uses a two-dimensional array of counters, and updates the counters in each row according to the hash value of an element in that row. The number of distinct elements is estimated by the minimum of the counters in each column.
- Some examples of sampling algorithms are:
  - Reservoir sampling: This algorithm maintains a sample of size k from the stream, and replaces each element with a new one with probability k/n, where n is the number of elements seen so far. The number of distinct elements is estimated by k * (1 - f_0), where f_0 is the fraction of elements that appear only once in the sample.
  - Bottom-k sketch: This algorithm maintains a set of k elements with the smallest hash values from the stream. The number of distinct elements is estimated by k / h_k, where h_k is the maximum hash value in the set.
  - KMV sketch: This algorithm improves the bottom-k sketch by using a sorted list of k elements with the smallest hash values, and updating the list only when a new element has a smaller hash value than the current maximum. The number of distinct elements is estimated by k / (h_k - h_0), where h_k is the maximum hash value in the list, and h_0 is the minimum possible hash value.