### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream is defined as $F_p = \sum_i m_i^p$ for any $p > 0$ .
- Estimating frequency moments is useful for applications such as estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- There are two main approaches for estimating frequency moments: sketching and sampling .
- Sketching is a technique that uses a small amount of memory to store a summary of the stream, such that the frequency moments can be approximated from the summary .
- Sampling is a technique that selects a subset of the stream elements uniformly at random, and uses the frequencies of the sampled elements to estimate the frequency moments of the whole stream .
- Both sketching and sampling have trade-offs between space, accuracy, and update time .
- Some examples of sketching algorithms are the Alon-Matias-Szegedy (AMS) sketch, the Count-Min sketch, and the Count sketch.
- Some examples of sampling algorithms are the Flajolet-Martin (FM) algorithm, the Morris algorithm, and the HyperLogLog algorithm.