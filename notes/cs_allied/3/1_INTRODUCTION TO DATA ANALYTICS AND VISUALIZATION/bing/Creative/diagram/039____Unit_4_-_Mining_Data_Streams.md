## Unit 4 - Mining Data Streams

- A data stream is a sequence of data elements that arrives continuously and rapidly, and whose size is potentially unbounded.
- Examples of data streams are sensor readings, network packets, web clicks, online transactions, social media posts, etc.
- Mining data streams poses several challenges, such as:
  - The data cannot be stored or accessed randomly, due to its volume and velocity.
  - The data may be noisy, incomplete, or evolving over time, requiring adaptive and robust methods.
  - The data may have different types and formats, requiring heterogeneous and flexible methods.
  - The data may have privacy and security issues, requiring ethical and legal methods.
- Some common tasks and techniques for mining data streams are:
  - Sampling: selecting a representative subset of the data stream for analysis, using methods such as reservoir sampling, sliding window sampling, or sketching.
  - Filtering: removing irrelevant or redundant data elements from the data stream, using methods such as bloom filters, count-min sketch, or locality-sensitive hashing.
  - Aggregation: computing summary statistics or functions over the data stream, using methods such as group-by, count, sum, average, min, max, median, etc.
  - Clustering: finding groups of similar data elements in the data stream, using methods such as k-means, DBSCAN, BIRCH, or streamKM++.
  - Classification: assigning labels or categories to data elements in the data stream, using methods such as decision trees, naive Bayes, support vector machines, or online learning algorithms.
  - Outlier detection: identifying data elements that deviate significantly from the normal behavior or pattern in the data stream, using methods such as distance-based, density-based, or subspace-based methods.
  - Pattern mining: discovering frequent or interesting patterns or rules in the data stream, using methods such as frequent itemsets, association rules, sequential patterns, or episode mining.
  - Visualization: presenting the data stream or its analysis results in a graphical or interactive way, using methods such as charts, graphs, maps, dashboards, or animations.