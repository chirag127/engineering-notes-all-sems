### Sampling Data in a Stream

- Sampling data in a stream is a technique to select a subset of data items from a continuous and potentially infinite stream of data.
- Sampling data in a stream can be useful for several purposes, such as:
  - Reducing the amount of data to be stored and processed.
  - Estimating statistics or properties of the stream, such as frequency, mean, variance, etc.
  - Detecting outliers or anomalies in the stream.
  - Testing hypotheses or performing experiments on the stream.
- Sampling data in a stream can be challenging due to the following factors:
  - The stream may be too fast or too large to store or process all the data items.
  - The stream may be dynamic or evolving, meaning that the data distribution or characteristics may change over time.
  - The stream may be noisy or uncertain, meaning that the data quality or reliability may vary or be unknown.
  - The stream may be unbounded or infinite, meaning that there is no fixed or known end to the stream.
- Sampling data in a stream can be done in different ways, depending on the sampling goal, the stream characteristics, and the available resources. Some common sampling methods are:
  - Uniform sampling: selecting data items from the stream with equal probability, regardless of their order or value.
  - Reservoir sampling: maintaining a fixed-size sample of data items from the stream, such that each data item has an equal probability of being in the sample at any time.
  - Weighted sampling: selecting data items from the stream with different probabilities, depending on their value or importance.
  - Stratified sampling: dividing the stream into different groups or strata based on some criteria, and selecting data items from each stratum with equal or proportional probability.
  - Adaptive sampling: adjusting the sampling rate or strategy based on the feedback or information obtained from the sample or the stream.