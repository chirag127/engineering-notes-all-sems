### Ratio test

The ratio test is a method for testing the convergence of an infinite series of real or complex numbers, where each term is nonzero when n is large. The test is based on the ratio of consecutive terms of the series and the limit of this ratio as n approaches infinity. The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.

The ratio test states that:

- Given a series $\sum_{n=1}^{\infty} a_n$, where $a_n \neq 0$ for large n, let $L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$ be the limit of the ratio of consecutive terms.
- If $L < 1$, then the series converges absolutely, meaning that $\sum_{n=1}^{\infty} |a_n|$ is finite.
- If $L > 1$, then the series diverges, meaning that $\sum_{n=1}^{\infty} a_n$ is either infinite or undefined.
- If $L = 1$ or the limit fails to exist, then the test is inconclusive, meaning that there exist both convergent and divergent series that satisfy this case.

The ratio test is useful for testing the convergence of series that involve factorials, exponentials, or powers of n. However, the test cannot be applied to series that have zero terms or alternating signs. Also, the test does not give any information about the value or the rate of convergence of the series.

Here is an example of applying the ratio test to a series:

- Consider the series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$, where $n!$ is the factorial of n.
- To use the ratio test, we need to find the limit of the ratio of consecutive terms: $L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \left| \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} \right|$
- Simplifying the expression, we get: $L = \lim_{n \to \infty} \left| \frac{n^n}{(n+1)^n} \right| = \lim_{n \to \infty} \left| \frac{1}{(1 + \frac{1}{n})^n} \right|$
- Applying the result that $\lim_{n \to \infty} (1 + \frac{1}{n})^n = e$, where e is the base of the natural logarithm, we get: $L = \frac{1}{e} < 1$
- Since $L < 1$, the ratio test tells us that the series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges absolutely.