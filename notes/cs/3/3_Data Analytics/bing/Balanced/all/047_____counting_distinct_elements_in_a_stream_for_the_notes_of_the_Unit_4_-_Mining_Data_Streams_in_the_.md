# Counting distinct elements in a stream

- Counting the number of distinct elements in a stream is a problem of finding the cardinality of a set of data that is too large or dynamic to store in memory.
- This problem has many applications in data analysis, such as estimating the number of unique visitors to a website, the number of distinct words in a document, or the number of different items sold in a store.
- There are two main types of algorithms for solving this problem: exact and approximate.
  - Exact algorithms store all the elements seen in the stream and compare each new element with the existing ones to determine if it is distinct or not. These algorithms require a lot of memory and time, and are impractical for large or unbounded streams.
  - Approximate algorithms use probabilistic data structures, such as sketches or samples, to estimate the number of distinct elements with some error bound. These algorithms require less memory and time, but sacrifice accuracy and precision.
- Some examples of approximate algorithms are:
  - Flajolet-Martin algorithm: This algorithm uses a hash function to map each element to a binary string, and then counts the number of leading zeros in the string. The maximum number of leading zeros among all the elements is used to estimate the number of distinct elements.
  - HyperLogLog algorithm: This algorithm improves the Flajolet-Martin algorithm by dividing the stream into multiple substreams and applying the Flajolet-Martin algorithm to each substream. The results of the substreams are then combined using a harmonic mean to get a more accurate estimate.
  - Datar-Gionis-Indyk-Motwani algorithm: This algorithm is designed for counting the number of distinct elements in a sliding window of a stream, that is, only the elements that arrived in the last k time units. This algorithm uses a priority queue to store a sample of the elements, and updates the sample whenever a new element arrives or an old element expires.
- Some examples of programming languages and libraries that support stream processing and counting distinct elements are:
  - Java: Java provides the Stream API, which allows creating and manipulating streams of data from various sources, such as collections, arrays, or I/O channels. The Stream API also provides methods for counting, filtering, mapping, reducing, and grouping elements of a stream. For example, to count the number of distinct elements in a stream of strings, one can use the following code:

  ```java
  Stream<String> stream = Stream.of("a", "b", "a", "c", "c", "a", "a", "d");
  long count = stream.distinct().count();
  ```
  - Python: Python provides the itertools module, which contains functions for creating and manipulating iterators, which are objects that can be used to iterate over streams of data. The itertools module also provides functions for counting, filtering, mapping, reducing, and grouping elements of an iterator. For example, to count the number of distinct elements in an iterator of strings, one can use the following code:

  ```python
  from itertools import groupby
  iterator = iter(["a", "b", "a", "c", "c", "a", "a", "d"])
  count = len(list(groupby(sorted(iterator))))
  ```