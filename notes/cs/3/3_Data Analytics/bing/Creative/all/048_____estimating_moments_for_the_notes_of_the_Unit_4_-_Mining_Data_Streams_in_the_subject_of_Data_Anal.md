# Estimating Moments for the Notes of the Unit 4 - Mining Data Streams in the Subject of Data Analytics

- Estimating moments is a generalization of the problem of counting distinct elements in a stream .
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream .
- Suppose a stream consists of elements chosen from a universal set. Let $m_i$ be the number of occurrences of the $i$-th element for any $i$.
- The $p$-th frequency moment of the stream, denoted by $F_p$, is defined as the sum of the $p$-th powers of the frequencies of the elements   , i.e.,

$$
F_p = \sum_i m_i^p
$$

- The frequency moments are of interest in estimating all-pairs distances in a large data matrix, machine learning, and in data stream computation .
- The frequency moments can also be used to measure the skewness of the data distribution, i.e., how unevenly the elements are distributed in the stream.
- For example, the zeroth frequency moment, $F_0$, is the number of distinct elements in the stream . The first frequency moment, $F_1$, is the total number of elements in the stream . The second frequency moment, $F_2$, is also known as the self-join size of the stream .
- Estimating the frequency moments of a stream is challenging because of the limited space and time available for processing the stream    .
- There are two main approaches for estimating the frequency moments of a stream: sketching and sampling   .
- Sketching is a technique that uses a small amount of memory to store a summary of the stream, such as a hash table or a vector of counters   . The sketch can then be used to estimate the frequency moments by applying some mathematical operations   .
- Sampling is a technique that selects a subset of the stream elements at random and stores them in memory   . The sample can then be used to estimate the frequency moments by applying some statistical methods   .
- Both sketching and sampling have advantages and disadvantages, depending on the accuracy, space, and time requirements of the problem   .
- Some examples of sketching algorithms for estimating the frequency moments are the Alon-Matias-Szegedy (AMS) sketch   , the Count-Min sketch   , and the Count-Sketch   .
- Some examples of sampling algorithms for estimating the frequency moments are the Flajolet-Martin (FM) algorithm   , the HyperLogLog algorithm   , and the Morris algorithm   .