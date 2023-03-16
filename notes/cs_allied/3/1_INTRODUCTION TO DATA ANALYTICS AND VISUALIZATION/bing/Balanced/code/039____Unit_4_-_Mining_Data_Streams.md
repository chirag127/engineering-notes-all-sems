## Unit 4 - Mining Data Streams

- A data stream is a sequence of data elements that arrives continuously and rapidly, and whose size is potentially unbounded.
- Examples of data streams are sensor readings, network packets, web clicks, online transactions, social media posts, etc.
- Mining data streams poses several challenges, such as:
  - The data cannot be stored or accessed randomly, due to its volume and velocity.
  - The data may be noisy, incomplete, or evolving over time, requiring adaptive and robust methods.
  - The data may have privacy or security issues, requiring encryption or anonymization techniques.
- Some common tasks and techniques for mining data streams are:
  - Sampling: selecting a representative subset of the data stream for analysis or storage, using methods such as reservoir sampling, sliding window sampling, or weighted sampling.
  - Filtering: removing irrelevant or redundant data elements from the data stream, using methods such as bloom filters, sketches, or synopsis data structures.
  - Aggregation: computing summary statistics or functions over the data stream, such as count, sum, average, min, max, median, etc., using methods such as sliding window aggregation, synopsis data structures, or online algorithms.
  - Clustering: grouping similar data elements in the data stream into clusters, using methods such as micro-clustering, density-based clustering, or stream clustering algorithms.
  - Classification: assigning labels or categories to data elements in the data stream, using methods such as decision trees, naive Bayes, or online learning algorithms.
  - Outlier detection: identifying data elements in the data stream that deviate significantly from the normal or expected behavior, using methods such as distance-based, density-based, or subspace-based outlier detection algorithms.
  - Frequent pattern mining: finding patterns or associations that occur frequently in the data stream, such as frequent items, itemsets, subsequences, or subgraphs, using methods such as sliding window frequent pattern mining, synopsis data structures, or stream mining algorithms.
  - Topic modeling: discovering the main topics or themes that emerge from the data stream, such as keywords, phrases, or concepts, using methods such as latent Dirichlet allocation, online topic modeling, or streaming variational inference.