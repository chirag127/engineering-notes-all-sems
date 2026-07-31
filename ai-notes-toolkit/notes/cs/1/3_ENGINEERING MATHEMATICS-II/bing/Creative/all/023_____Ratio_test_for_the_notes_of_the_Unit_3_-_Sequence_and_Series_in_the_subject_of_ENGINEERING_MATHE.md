# Ratio Test

The ratio test is a method for testing the convergence of an infinite series of real or complex numbers. The test is based on the ratio of successive terms of the series and the limit of that ratio as the index of the terms goes to infinity. The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.

The ratio test can be stated as follows:

Let $\sum_{n=1}^{\infty} a_n$ be an infinite series of nonzero terms. Define the ratio $L$ as

$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$

Then,

- If $L < 1$, the series converges absolutely.
- If $L > 1$, the series diverges.
- If $L = 1$ or the limit does not exist, the test is inconclusive.

The ratio test can be used to test the convergence of any series, but it may not always give a definitive answer. Some examples of series that satisfy the inconclusive case are:

- The harmonic series $\sum_{n=1}^{\infty} \frac{1}{n}$, which diverges.
- The alternating harmonic series $\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{n}$, which converges conditionally.
- The geometric series $\sum_{n=1}^{\infty} \frac{1}{2^n}$, which converges absolutely.

The ratio test is useful for testing the convergence of series that involve factorials, exponentials, or powers of $n$. For example, the ratio test can be used to show that the series

$$\sum_{n=1}^{\infty} \frac{n!}{n^n}$$

converges absolutely, since

$$L = \lim_{n \to \infty} \left| \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} \right| = \lim_{n \to \infty} \frac{n+1}{(n+1)^{n+1}} \cdot n^n = \lim_{n \to \infty} \frac{1}{(n+1)^n} = 0 < 1$$