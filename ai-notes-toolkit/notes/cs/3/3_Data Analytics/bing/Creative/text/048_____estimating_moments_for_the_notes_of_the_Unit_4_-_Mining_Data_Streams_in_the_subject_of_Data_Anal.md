### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments", involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream is defined as $F_p = \sum_i m_i^p$ for any $p > 0$ .
- Estimating frequency moments is useful for various applications, such as estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- There are two main challenges for estimating frequency moments on data streams: space efficiency and accuracy.
- Space efficiency means using as little memory as possible to store a summary of the stream, called a sketch.
- Accuracy means minimizing the error between the estimated moment and the true moment, with high probability.
- There are different algorithms for estimating frequency moments on data streams, such as the Alon-Matias-Szegedy (AMS) algorithm, the Flajolet-Martin (FM) algorithm, and the Count-Min sketch.
- The AMS algorithm uses a random sample of the stream elements and their frequencies to estimate the second moment ($F_2$), which is related to the variance of the frequency distribution.
- The FM algorithm uses a hash function to map the stream elements to binary strings and counts the number of leading zeros in the hashed values to estimate the zeroth moment ($F_0$), which is equal to the number of distinct elements in the stream.
- The Count-Min sketch uses a matrix of counters and multiple hash functions to store the frequencies of the stream elements and estimate any moment ($F_p$) by taking the minimum of the hashed values.
- The following example illustrates the AMS algorithm for estimating the second moment of a stream:

  - Suppose the stream is $a, b, c, a, d, b, a, c, e, a$ and the universal set is $\{a, b, c, d, e\}$.
  - Let $n = 10$ be the length of the stream and $k = 2$ be the size of the sample.
  - The algorithm randomly picks two positions in the stream, say $3$ and $7$, and records the elements and their frequencies at those positions: $(c, 1)$ and $(b, 2)$.
  - The algorithm estimates the second moment as $F_2 \approx n(k-1)/k \times \sum_i f_i^2$, where $f_i$ is the frequency of the $i$-th element in the sample.
  - In this case, $F_2 \approx 10(2-1)/2 \times (1^2 + 2^2) = 25$.
  - The true second moment is $F_2 = 4^2 + 2^2 + 2^2 + 1^2 + 1^2 = 26$, so the error is $1$.