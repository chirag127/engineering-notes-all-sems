### Estimating Moments

- Estimating moments is a generalization of the problem of counting distinct elements in a stream.
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream, denoted by $F_p$, is defined as the sum of the $p$-th powers of the frequencies  :

$$
F_p = \sum_i m_i^p
$$

- Estimating frequency moments of data streams is of interest in estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- There are two main challenges in estimating frequency moments of data streams: space efficiency and accuracy  .
- Space efficiency means using as little memory as possible to store the sketch of the stream, which is a compact summary of the stream that allows estimating the moments  .
- Accuracy means minimizing the error between the estimated moment and the true moment, which depends on the distribution of the stream and the choice of the sketch  .
- There are different sketches for estimating frequency moments of data streams, such as the AMS sketch, the Count sketch, and the Count-Min sketch   .
- Each sketch has its own advantages and disadvantages in terms of space efficiency, accuracy, and update time   .
- The analysis of the sketches involves some important tricks in probability, such as boosting the accuracy of a random variable by considering the median of means of multiple independent copies of the variable, and using the Chernoff bound to bound the tail probability of a random variable.