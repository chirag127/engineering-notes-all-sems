### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream, denoted by $F_p$, is defined as the sum of the $p$-th powers of the frequencies  :

$$
F_p = \sum_i m_i^p
$$

- Estimating frequency moments of data streams is of interest in estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- There are two main approaches for estimating frequency moments of data streams: sketching and sampling .
- Sketching is a technique that uses a small amount of memory to store a summary of the stream, which can be used to estimate the frequency moments with some error .
- Sampling is a technique that selects a subset of the stream elements uniformly at random, and uses them to estimate the frequency moments with some confidence .
- Example: Suppose we want to estimate the second frequency moment ($F_2$) of a stream of letters using sketching. One possible sketch is to use a hash function $h$ that maps each letter to a random sign ($+1$ or $-1$), and maintain a counter $C$ that is updated as follows:

$$
C = C + h(x)
$$

where $x$ is the current stream element. At the end of the stream, we can estimate $F_2$ as $C^2$. This sketch uses only one counter, which is much smaller than storing the frequencies of all letters. However, the estimate may have some error due to the randomness of the hash function.