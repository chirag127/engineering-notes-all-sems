# Counting Frequent Itemsets in a Stream

- A data stream is a sequence of transactions that arrives continuously and cannot be stored in memory.
- A frequent itemset is a set of items that appears in more than a given threshold of transactions in a data stream.
- Counting frequent itemsets in a stream is a challenging problem because of the following reasons:
  - The stream is unbounded and dynamic, so the frequencies of itemsets may change over time.
  - The stream is fast and massive, so it is impossible to scan the stream multiple times or store all the transactions in memory.
  - The stream is noisy and uncertain, so the itemsets may contain errors or missing values.
- Counting frequent itemsets in a stream has many applications, such as:
  - Opinion and sentiment analysis from social networks.
  - Network traffic monitoring and anomaly detection.
  - Market basket analysis and recommendation systems.
- There are different approaches to count frequent itemsets in a stream, such as:
  - Sketch-based methods: These methods use a compact data structure called a sketch to store a summary of the stream and estimate the frequencies of itemsets. For example, the COUNT SKETCH algorithm uses a hash function and a sign function to map each item to a position and a sign in a sketch matrix, and updates the sketch matrix by adding or subtracting the sign for each item in a transaction. The frequency of an itemset is estimated by taking the minimum value of the sketch matrix for the items in the itemset.
  - Sliding window methods: These methods focus on a recent portion of the stream, called a sliding window, and discard the older transactions. The sliding window can be defined by a fixed size or a time interval. For example, the FREQ algorithm maintains a set of candidate itemsets and their current frequencies in a sliding window, and updates the candidates and their frequencies by adding new transactions and deleting expired transactions from the window. The frequent itemsets are those candidates whose frequencies are above the threshold in the window.
  - Sampling methods: These methods select a random subset of transactions from the stream and store them in memory, and use them to approximate the frequencies of itemsets in the stream. For example, the LOSSY COUNTING algorithm divides the stream into buckets of equal size, and maintains a set of itemsets and their approximate frequencies in each bucket. The algorithm periodically deletes the itemsets whose frequencies are below a certain threshold in each bucket, and merges the buckets to reduce the memory usage. The frequent itemsets are those whose approximate frequencies are above the threshold in the stream.