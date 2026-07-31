# Counting distinct elements in a stream

- A stream is a sequence of data items that are generated continuously and possibly infinitely.
- Counting distinct elements in a stream is the problem of finding the number of different data items in the stream, without storing the entire stream in memory.
- This problem has many applications in data analysis, such as estimating the number of unique visitors to a website, the number of distinct words in a document, or the number of different IP addresses in a network traffic.
- There are two main types of algorithms for counting distinct elements in a stream: exact algorithms and approximate algorithms.
- Exact algorithms guarantee to return the exact number of distinct elements in the stream, but they require a lot of memory and time to process the stream.
- Approximate algorithms trade off some accuracy for efficiency, and they return an estimate of the number of distinct elements in the stream, with some error bound or confidence interval.
- Some examples of approximate algorithms are Flajolet-Martin algorithm, HyperLogLog algorithm, and Count-Min sketch algorithm.
- Flajolet-Martin algorithm uses a hash function to map each data item to a binary string, and then counts the number of leading zeros in the hash values to estimate the number of distinct elements.
- HyperLogLog algorithm improves on Flajolet-Martin algorithm by using multiple hash functions and keeping track of the maximum number of leading zeros for each hash function, and then averaging them to get a more accurate estimate.
- Count-Min sketch algorithm uses a two-dimensional array of counters and multiple hash functions to store the frequency of each data item, and then estimates the number of distinct elements by taking the minimum of the counters for each hash function.
- Some variations of the problem are counting distinct elements in a sliding window, where only the most recent data items are considered, or counting distinct elements with expiration, where data items have a limited lifetime and are discarded after a certain time.
- These variations require more sophisticated algorithms that can update the counters or hash values dynamically, and handle the deletion or expiration of data items.