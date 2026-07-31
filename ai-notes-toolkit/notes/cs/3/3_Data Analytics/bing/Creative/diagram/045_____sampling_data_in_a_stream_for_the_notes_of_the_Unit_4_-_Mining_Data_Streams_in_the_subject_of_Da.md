Hello, I am Sydney, your AI assistant. I can help you with your study material for Data Analytics. Here is the content for the topic of sampling data in a stream:

### Sampling Data in a Stream

- Sampling data in a stream is a technique to select a subset of data items from a continuous and potentially infinite stream of data.
- Sampling data in a stream can be useful for several purposes, such as:
  - Reducing the storage and processing requirements for data analysis.
  - Estimating the properties and statistics of the stream, such as frequency, mean, variance, etc.
  - Detecting outliers and anomalies in the stream.
  - Finding frequent or rare items in the stream.
- Sampling data in a stream can be challenging because of the following characteristics of data streams:
  - The stream is unbounded and dynamic, so the sample size and composition may need to be adjusted over time.
  - The stream may have unknown or changing distribution, so the sample may not be representative of the stream.
  - The stream may have high arrival rate and volume, so the sample may need to be selected in a fast and efficient manner.
- Sampling data in a stream can be classified into two types: reservoir sampling and sketch-based sampling.
  - Reservoir sampling is a technique to maintain a fixed-size sample of the stream, such that each item in the stream has an equal probability of being in the sample. Reservoir sampling works as follows:
    - Initialize an empty array of size k, called the reservoir, where k is the desired sample size.
    - For each item i in the stream, do the following:
      - If the reservoir is not full, insert i into the reservoir.
      - If the reservoir is full, generate a random number r between 1 and the number of items seen so far, inclusive. If r is less than or equal to k, replace the r-th item in the reservoir with i.
    - Return the reservoir as the sample of the stream.
  - Sketch-based sampling is a technique to maintain a summary or sketch of the stream, such that the sample can be extracted from the sketch. Sketch-based sampling works as follows:
    - Initialize an empty data structure, called the sketch, that can store some information about the stream, such as counts, hashes, frequencies, etc.
    - For each item i in the stream, do the following:
      - Update the sketch with the information of i, such as incrementing a counter, computing a hash, etc.
    - Return a sample of the stream by querying the sketch, such as selecting items with high counts, hashes, frequencies, etc.