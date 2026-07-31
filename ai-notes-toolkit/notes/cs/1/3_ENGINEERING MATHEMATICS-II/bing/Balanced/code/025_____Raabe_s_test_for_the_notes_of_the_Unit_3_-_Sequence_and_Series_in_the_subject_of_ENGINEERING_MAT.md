### Raabe's test

Raabe's test is a test for the convergence of a series of the form

$$\sum_{n=1}^{\infty} a_n$$

where each term is a real or complex number and $a_n \neq 0$ for large $n$.

The test is based on the ratio of consecutive terms of the series, defined as

$$R_n = \frac{a_n}{a_{n+1}}$$

The test states that:

- If $\lim_{n \to \infty} (R_n - 1)n > 1$, then the series converges.
- If $\lim_{n \to \infty} (R_n - 1)n < 1$, then the series diverges.
- If $\lim_{n \to \infty} (R_n - 1)n = 1$, then the test is inconclusive.

The test was developed by Swiss mathematician Joseph Ludwig Raabe in 1832 .

Some examples of applying Raabe's test are:

- The series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges, since

$$\lim_{n \to \infty} \left(\frac{n!}{n^n} \cdot \frac{(n+1)^{n+1}}{(n+1)!} - 1\right)n = \lim_{n \to \infty} \left(\frac{(n+1)^n}{n^n} - 1\right) = \lim_{n \to \infty} \left(\left(1 + \frac{1}{n}\right)^n - 1\right) = e - 1 > 1$$

- The series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges, since

$$\lim_{n \to \infty} \left(\frac{1}{n} \cdot n - 1\right)n = \lim_{n \to \infty} (1 - n) = -\infty < 1$$

- The series $\sum_{n=1}^{\infty} \frac{1}{n^2}$ is inconclusive by Raabe's test, since

$$\lim_{n \to \infty} \left(\frac{1}{n^2} \cdot \frac{(n+1)^2}{1} - 1\right)n = \lim_{n \to \infty} \left(\frac{n^2 + 2n + 1}{n^2} - 1\right) = \lim_{n \to \infty} \left(\frac{2}{n} + \frac{1}{n^2}\right) = 0 = 1$$

However, this series converges by the p-series test.