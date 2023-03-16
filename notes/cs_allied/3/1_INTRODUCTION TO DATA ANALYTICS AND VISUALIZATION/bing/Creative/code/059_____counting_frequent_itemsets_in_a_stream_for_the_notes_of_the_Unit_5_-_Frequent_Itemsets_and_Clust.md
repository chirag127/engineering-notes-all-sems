### Counting frequent itemsets in a stream

- A data stream is a sequence of transactions that arrives continuously and cannot be stored in memory.
- A frequent itemset is a set of items that appears in more than a given threshold of transactions in a data stream.
- Counting frequent itemsets in a stream is a challenging problem because the stream is unbounded and dynamic, and the frequency of itemsets may change over time.
- Counting frequent itemsets in a stream has many applications, such as opinion and sentiment analysis, network monitoring, web mining, etc.
- There are different approaches to counting frequent itemsets in a stream, such as:
  - Sketch-based methods: These methods use a data structure called a sketch, which is a compact summary of the stream that can be updated incrementally and queried efficiently. A sketch can provide approximate frequency estimates of itemsets with provable guarantees. An example of a sketch-based method is the COUNT SKETCH algorithm .
  - Sliding window methods: These methods focus on a fixed-size window of the most recent transactions in the stream, and discard the older ones. They maintain the exact frequencies of itemsets within the window, and update them whenever a new transaction arrives or an old one expires. An example of a sliding window method is the LOSSY COUNTING algorithm.
  - Landmark window methods: These methods consider the entire stream from a fixed starting point (landmark) until the current state, and define the frequency of an itemset as the maximum frequency over all possible windows of a minimum length. They use an incremental algorithm that can produce the current frequencies of all frequent itemsets at any time. An example of a landmark window method is the LANDMARK algorithm.