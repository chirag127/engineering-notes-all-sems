### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream is defined as $F_p = \sum_i m_i^p$ for any $p > 0$ .
- Estimating frequency moments is useful for various applications, such as measuring the diversity of a stream, estimating the number of heavy hitters, computing the entropy of a stream, and estimating the distance between two streams   .
- Estimating frequency moments on data streams is challenging because of the limited space and time available for processing the stream  .
- There are two main approaches for estimating frequency moments on data streams: sketching and sampling  .
- Sketching is a technique that uses a small amount of memory to store a summary of the stream, such that the frequency moments can be estimated from the summary with some error guarantee  .
- Sampling is a technique that selects a subset of the stream elements uniformly at random, and uses the sample to estimate the frequency moments with some confidence interval  .
- Some examples of sketching algorithms are the AMS sketch, the Count sketch, and the Count-Min sketch  .
- Some examples of sampling algorithms are the Flajolet-Martin algorithm, the Alon-Matias-Szegedy algorithm, and the Morris algorithm  .