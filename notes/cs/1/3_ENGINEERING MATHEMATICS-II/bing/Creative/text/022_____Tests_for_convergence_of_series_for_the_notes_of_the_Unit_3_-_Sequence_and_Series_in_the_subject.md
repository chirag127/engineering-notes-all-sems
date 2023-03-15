### Tests for convergence of series

A series is a sum of infinitely many terms, such as

$$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$$

where $a_n$ is the n-th term of the series. A series is said to converge if the partial sums

$$S_N = \sum_{n=1}^{N} a_n$$

approach a finite limit as $N$ goes to infinity. Otherwise, the series is said to diverge.

There are various tests that can be used to determine whether a series converges or diverges. Some of the common tests are:

- **The n-th term test**: This test states that if $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ diverges. This test can only be used to show divergence, not convergence.
- **The comparison test**: This test compares a given series with another series that is known to converge or diverge. If the given series is smaller than a convergent series, then it also converges. If the given series is larger than a divergent series, then it also diverges.
- **The geometric test**: This test applies to series of the form $\sum_{n=1}^{\infty} ar^{n-1}$, where $a$ and $r$ are constants. Such series are called geometric series. The test states that the series converges if $|r| < 1$ and diverges if $|r| \geq 1$.
- **The ratio test**: This test uses the ratio of consecutive terms of the series, $\frac{a_{n+1}}{a_n}$. The test states that the series converges if $\lim_{n \to \infty} |\frac{a_{n+1}}{a_n}| < 1$ and diverges if $\lim_{n \to \infty} |\frac{a_{n+1}}{a_n}| > 1$. If the limit is equal to 1, the test is inconclusive.
- **The root test**: This test uses the n-th root of the n-th term of the series, $\sqrt[n]{|a_n|}$. The test states that the series converges if $\lim_{n \to \infty} \sqrt[n]{|a_n|} < 1$ and diverges if $\lim_{n \to \infty} \sqrt[n]{|a_n|} > 1$. If the limit is equal to 1, the test is inconclusive.
- **The alternating series test**: This test applies to series of the form $\sum_{n=1}^{\infty} (-1)^{n-1} b_n$, where $b_n$ are positive terms. Such series are called alternating series. The test states that the series converges if $b_n$ decreases to zero as $n$ goes to infinity.