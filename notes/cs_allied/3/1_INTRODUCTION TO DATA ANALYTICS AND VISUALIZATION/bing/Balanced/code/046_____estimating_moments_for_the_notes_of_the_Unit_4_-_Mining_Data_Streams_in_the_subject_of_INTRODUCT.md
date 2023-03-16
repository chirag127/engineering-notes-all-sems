### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream. The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$. The $p$-th frequency moment of the stream is defined as $F_p = \sum_i m_i^p$ for any $p > 0$.
- Estimating frequency moments is useful for various applications, such as estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- The main challenge of estimating frequency moments is to design space-efficient algorithms that can handle large and dynamic streams of data. The algorithms should also have low error probability and small approximation error .
- Two simple sketches for estimating frequency moments are the Alon-Matias-Szegedy (AMS) sketch and the Flajolet-Martin (FM) sketch  .
- The AMS sketch is based on sampling a random position in the stream and storing the frequency of the element at that position. The sketch can estimate the second frequency moment ($F_2$) with high probability and low relative error  .
- The FM sketch is based on hashing the elements of the stream to binary strings and storing the minimum number of leading zeros in the hashed values. The sketch can estimate the zeroth frequency moment ($F_0$), which is the number of distinct elements in the stream, with high probability and low relative error  .
- Both sketches can be extended to handle multiple streams, weighted streams, and sliding windows  .