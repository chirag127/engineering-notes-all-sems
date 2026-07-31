### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream is defined as $F_p = \sum_i m_i^p$ for any $p > 0$ .
- Estimating the frequency moments of a stream is useful for various applications, such as measuring the diversity of the stream, estimating the number of heavy hitters, computing the entropy of the stream, and estimating the all-pairs distances in a large data matrix  .
- However, estimating the frequency moments of a stream is challenging because of the limited space and time available for processing the stream  .
- There are two main approaches for estimating the frequency moments of a stream: sketching and sampling.
- Sketching is a technique that maintains a compact summary of the stream, such as a hash table or a vector of counters, that can be used to estimate the frequency moments with some error.
- Sampling is a technique that selects a subset of the stream elements, such as a reservoir or a min-wise sample, that can be used to estimate the frequency moments with some variance.
- Both sketching and sampling have trade-offs between the space complexity, the accuracy, and the update time of the estimation algorithms.
- Some examples of sketching algorithms are the AMS sketch, the Count sketch, and the Count-Min sketch.
- Some examples of sampling algorithms are the Alon-Matias-Szegedy (AMS) sample, the Morris sample, and the Flajolet-Martin (FM) sample.