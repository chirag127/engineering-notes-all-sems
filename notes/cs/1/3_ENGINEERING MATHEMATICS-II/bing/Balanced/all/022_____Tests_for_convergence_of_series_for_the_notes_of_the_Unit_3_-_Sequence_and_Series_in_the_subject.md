# Tests for convergence of series

A series is a sum of infinitely many terms, such as

$$\sum_{n=1}^{\infty} a_n = a_1 + a_2 + a_3 + \cdots$$

A series is said to converge if the partial sums

$$S_N = \sum_{n=1}^{N} a_n$$

approach a finite limit as $N$ goes to infinity. Otherwise, the series is said to diverge.

There are several tests that can be used to determine whether a series converges or diverges. Some of the most common tests are:

- **The n-th term test**: This test states that if $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ diverges. This test can only be used to show divergence, not convergence.
- **The comparison test**: This test compares a given series with another series that is known to converge or diverge. If the given series is smaller than a convergent series, then it also converges. If the given series is larger than a divergent series, then it also diverges.
- **The geometric test**: This test applies to series of the form $\sum_{n=1}^{\infty} ar^n$, where $a$ and $r$ are constants. Such a series converges if and only if $|r| < 1$.
- **The ratio test**: This test uses the limit of the ratio of consecutive terms of the series. If $\lim_{n \to \infty} \left|\frac{a_{n+1}}{a_n}\right| = L$, then the series converges if $L < 1$, diverges if $L > 1$, and the test is inconclusive if $L = 1$.
- **The root test**: This test uses the limit of the n-th root of the n-th term of the series. If $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$, then the series converges if $L < 1$, diverges if $L > 1$, and the test is inconclusive if $L = 1$.

There are other tests for convergence of series, such as the integral test, the alternating series test, the Leibniz test, the Dirichlet test, and the Cauchy condensation test, but they are beyond the scope of this note. For more details and examples, please refer to the sources     in the search results.