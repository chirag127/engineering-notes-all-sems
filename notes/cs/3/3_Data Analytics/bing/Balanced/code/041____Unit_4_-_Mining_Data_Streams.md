## Unit 4 - Mining Data Streams

- Data streams are continuous and unbounded sequences of data elements that arrive at high speed and need to be processed in real time.
- Data stream mining is the process of extracting useful information and patterns from data streams, such as trends, outliers, correlations, etc.
- Data stream mining poses several challenges, such as:
  - Limited memory and processing resources: Data streams cannot be stored or revisited, so algorithms need to be efficient and incremental.
  - Concept drift: The underlying distribution or pattern of the data stream may change over time, so algorithms need to be adaptive and robust.
  - Data quality: Data streams may contain noise, missing values, duplicates, etc., so algorithms need to be tolerant and resilient.
- Data stream mining techniques can be classified into four categories, depending on the type of information or task they perform:
  - Data stream summarization: These techniques aim to compress or represent the data stream using compact data structures, such as sketches, histograms, synopses, etc. They can be used to answer queries or perform analysis on the data stream efficiently and approximately.
  - Data stream classification: These techniques aim to assign labels or categories to the data elements in the data stream, based on a predefined set of classes or rules. They can be used to perform prediction, detection, or recommendation tasks on the data stream.
  - Data stream clustering: These techniques aim to group or partition the data elements in the data stream, based on their similarity or distance. They can be used to discover patterns, outliers, or anomalies in the data stream.
  - Data stream frequent pattern mining: These techniques aim to find frequent or recurring patterns or items in the data stream, such as itemsets, subsequences, subgraphs, etc. They can be used to discover associations, correlations, or causations in the data stream.