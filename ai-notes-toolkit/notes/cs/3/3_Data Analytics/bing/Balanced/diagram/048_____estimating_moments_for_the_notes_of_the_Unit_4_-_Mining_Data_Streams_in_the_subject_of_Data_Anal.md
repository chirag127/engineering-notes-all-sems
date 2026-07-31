### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments", involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream, denoted by $F_p$, is defined as the sum of the $p$-th powers of the frequencies, i.e., $F_p = \sum_i m_i^p$  .
- Estimating frequency moments of data streams is of interest in estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- Estimating frequency moments of data streams is challenging because of the limited space and time available for processing the stream .
- There are two main approaches for estimating frequency moments of data streams: sketching and sampling .
- Sketching is a technique that uses a small amount of memory to store a summary of the stream, which can be used to estimate the frequency moments with some error .
- Sampling is a technique that selects a subset of the stream elements uniformly at random, and uses them to estimate the frequency moments with some confidence .
- Some examples of sketching algorithms are the AMS sketch, the Count sketch, and the Count-Min sketch.
- Some examples of sampling algorithms are the Flajolet-Martin algorithm, the Alon-Matias-Szegedy algorithm, and the Morris algorithm.