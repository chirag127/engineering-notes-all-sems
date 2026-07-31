### Counting frequent itemsets in a stream

- A data stream is a sequence of transactions that arrive continuously and cannot be stored in memory.
- A frequent itemset is a set of items that appears in more than a given threshold of transactions in a data stream.
- Counting frequent itemsets in a stream is a challenging problem because the stream is unbounded and dynamic, and the frequency of itemsets may change over time.
- Counting frequent itemsets in a stream has many applications, such as opinion and sentiment analysis, network monitoring, web mining, etc.
- There are different approaches to counting frequent itemsets in a stream, such as:

  - Sketch-based methods: These methods use a data structure called a sketch, which is a compact summary of the stream that can be updated incrementally and queried efficiently. A sketch can provide approximate frequency estimates of itemsets with provable error bounds. Examples of sketch-based methods are COUNT SKETCH , GROUP TESTING, and FREQUENT.
  - Sliding window methods: These methods focus on a fixed-size window of the most recent transactions in the stream, and discard older transactions. A sliding window can capture the current trends and patterns in the stream, but may miss some itemsets that are frequent in the whole stream. Examples of sliding window methods are LOSSY COUNTING, STICKY SAMPLING, and D-CLUE.
  - Landmark window methods: These methods consider all the transactions in the stream from a fixed starting point (landmark) until the current time. A landmark window can provide the exact frequency of itemsets in the stream, but may require a lot of space and time to maintain and update. Examples of landmark window methods are FP-STREAM, FP-STREAM-2, and FP-STREAM-3.