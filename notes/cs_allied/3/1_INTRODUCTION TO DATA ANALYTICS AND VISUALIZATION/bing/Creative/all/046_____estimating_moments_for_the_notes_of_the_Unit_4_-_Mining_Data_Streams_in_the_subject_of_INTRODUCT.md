# Estimating Moments for the Notes of the Unit 4 - Mining Data Streams in the Subject of Introduction to Data Analytics and Visualization

- Estimating moments is a generalization of the problem of counting distinct elements in a stream  .
- The problem, called computing "moments," involves the distribution of frequencies of different elements in the stream.
- Suppose a stream consists of elements chosen from a universal set. Let m_i be the number of occurrences of the i-th element for any i.
- The p-th frequency moment of the stream is defined as F_p = \sum_i m_i^p for any p > 0   .
- Estimating frequency moments is useful for various applications, such as estimating all-pairs distances in a large data matrix, machine learning, and data stream computation .
- The main challenge of estimating frequency moments is to design space-efficient algorithms that can handle large and dynamic streams of data  .
- There are two simple sketches for estimating the frequency moments of a stream: the AMS sketch and the Count sketch.
- The AMS sketch is based on the idea of randomly sampling a coordinate of the underlying vector and using it as an unbiased estimator of the second moment.
- The Count sketch is based on the idea of hashing the elements of the stream into buckets and using the sign of the hash function to reduce the variance of the estimator.
- Both sketches can be extended to estimate higher moments by using more sophisticated hash functions and linear algebra techniques.
- The analysis of the sketches involves two important tricks in probability: boosting the accuracy of a random variable by considering the median of means of multiple independent copies of the variable, and using the Cauchy-Schwarz inequality to bound the variance of a linear combination of random variables.
- An example of estimating the second moment of a stream using the AMS sketch is as follows:
  - Suppose the stream consists of elements from the set {a, b, c, d, e} and the underlying vector is (2, 3, 1, 0, 4).
  - The second moment of the stream is F_2 = 2^2 + 3^2 + 1^2 + 0^2 + 4^2 = 30.
  - To estimate F_2 using the AMS sketch, we randomly sample a coordinate of the vector, say the third one, and store its value, which is 1.
  - We also store the number of times the corresponding element, which is c, appears in the stream, which is 1.
  - The estimator of F_2 is then 1 * (2 * 1 - 1) = 1, which is an unbiased estimator of F_2.
  - To improve the accuracy of the estimator, we can repeat the sampling process multiple times and take the median of the results.