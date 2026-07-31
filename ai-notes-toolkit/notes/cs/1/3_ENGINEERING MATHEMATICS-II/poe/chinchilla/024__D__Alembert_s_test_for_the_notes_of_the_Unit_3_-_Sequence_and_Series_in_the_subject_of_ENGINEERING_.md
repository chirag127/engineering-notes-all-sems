### D’ Alembert’s test for the notes of the Unit 3 - Sequence and Series in the subject of ENGINEERING MATHEMATICS-II

D’ Alembert’s test is a method used to determine the convergence or divergence of an infinite series. It is named after the French mathematician Jean le Rond d'Alembert who introduced this test in 1741. This test is also known as the ratio test and is widely used in engineering mathematics to analyze infinite series.

#### Definition
D’ Alembert’s test states that if the limit of the ratio of the absolute values of consecutive terms of a series exists and is less than 1, then the series converges absolutely. If the limit is greater than 1 or does not exist, then the series diverges. If the limit is equal to 1, then the test is inconclusive.

#### Mathematical Representation
The test can be mathematically represented as follows:

Suppose we have an infinite series of real numbers a_n. The limit of the ratio of absolute values of consecutive terms is given by:

lim┬(n→∞)⁡〖|a_(n+1)/a_n|〗 = L

Then, the series converges absolutely if L < 1 and diverges if L > 1 or if L does not exist.

#### Steps to apply D’ Alembert’s Test
To apply D’ Alembert’s test, follow the given steps:

1. Take an infinite series a_n.
2. Calculate the ratio of the absolute values of consecutive terms, |a_(n+1)/a_n|.
3. Find the limit of the ratio as n tends to infinity, lim┬(n→∞)⁡〖|a_(n+1)/a_n|〗 = L.
4. Determine the convergence or divergence of the series based on the value of L.

#### Example
Let's consider the following infinite series:

∑_(n=1)^∞▒〖(n^2+1)/(n^3+2)〗

We have to determine whether this series converges or diverges using D’ Alembert’s test.

The ratio of the absolute values of consecutive terms is:

|a_(n+1)/a_n| = |((n+1)^2+1)/((n+1)^3+2)| * |(n^3+2)/(n^2+1)|

Taking the limit as n tends to infinity, we get:

lim┬(n→∞)⁡〖|a_(n+1)/a_n|〗= lim┬(n→∞)⁡〖((n+1)^2+1)/(n^2+1) * (n^2+1)/((n+1)^3+2)〗
= lim┬(n→∞)⁡〖(n^2+2n+2)/(n^3+3n^2+3n+3)〗
= 0

Since the limit is less than 1, the series converges absolutely.

#### Conclusion
D’ Alembert’s test provides a simple and effective method to determine the convergence or divergence of an infinite series. It is widely used in engineering mathematics to analyze infinite series and to determine the behavior of complex systems. It is important for students of engineering mathematics to understand and apply this test to solve problems related to infinite series.