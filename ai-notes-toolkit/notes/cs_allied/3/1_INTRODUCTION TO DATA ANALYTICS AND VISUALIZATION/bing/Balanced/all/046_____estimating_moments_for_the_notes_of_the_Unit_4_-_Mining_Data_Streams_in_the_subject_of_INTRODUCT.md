# Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream is defined as $F_p = \sum_i m_i^p$ for any $p > 0$ .
- Estimating frequency moments is useful for various applications, such as estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- Estimating frequency moments on data streams is challenging because of the limited space and time available for processing the stream   .
- Data streams are transient and can arrive at a high speed. Furthermore, the stream size may not be known apriori.
- Streaming computations therefore require single pass algorithms with small space requirement and which are able to handle arbitrary sized streams.
- There are various algorithms for estimating frequency moments on data streams, such as the Alon-Matias-Szegedy (AMS) algorithm, the Flajolet-Martin (FM) algorithm, and the Count-Min sketch   .
- These algorithms use different techniques, such as random sampling, hashing, and sketching, to reduce the space complexity and achieve probabilistic guarantees on the accuracy of the estimation   .
- Example: Suppose we want to estimate the second frequency moment ($F_2$) of a stream of integers from the set $\{1, 2, 3, 4, 5\}$. One possible algorithm is the AMS algorithm, which works as follows:

  - Pick a random index $r$ from $\{1, 2, \dots, n\}$, where $n$ is the stream length.
  - Initialize a counter $c$ to zero.
  - For each element $x$ in the stream, do the following:
    - If the index of $x$ is $r$, increment $c$ by one.
    - If the index of $x$ is greater than $r$, stop the algorithm and output $c^2 - c$ as the estimate of $F_2$.
  - The expected value of the output is $F_2$, and the variance is $O(F_2^2 / n)$.

- Example: Suppose the stream is $1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5$. The true value of $F_2$ is $75$. If we pick $r = 7$, then the algorithm will output $(2^2 - 2) = 2$ as the estimate of $F_2$. This is a bad estimate, but the algorithm has a low probability of picking such a bad index.