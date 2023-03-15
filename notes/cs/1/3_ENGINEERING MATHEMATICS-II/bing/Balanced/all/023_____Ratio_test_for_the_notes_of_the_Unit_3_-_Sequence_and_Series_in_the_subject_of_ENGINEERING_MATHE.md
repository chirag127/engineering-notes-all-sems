# Ratio Test

The ratio test is a method for testing the convergence of a series of real or complex numbers. It is based on the idea of comparing the ratio of successive terms of the series to a limit value. The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.

## Statement of the test

Let $\sum_{n=1}^{\infty} a_n$ be a series of nonzero terms, and let

$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$

be the limit of the ratio of consecutive terms. The ratio test states that:

- If $L < 1$, then the series converges absolutely.
- If $L > 1$, then the series diverges.
- If $L = 1$ or the limit fails to exist, then the test is inconclusive, because there exist both convergent and divergent series that satisfy this case.

## Examples

- The series $\sum_{n=1}^{\infty} \frac{1}{n^2}$ converges by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{1}{(n+1)^2}}{\frac{1}{n^2}} \right| = \lim_{n \to \infty} \left( \frac{n^2}{(n+1)^2} \right) = 1 - \lim_{n \to \infty} \frac{2n+1}{(n+1)^2} = 1 - 0 = 1 < 1$$

- The series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{(n+1)!}{(n+1)^{n+1}}}{\frac{n!}{n^n}} \right| = \lim_{n \to \infty} \left( \frac{n^n}{(n+1)^n} \right) = \lim_{n \to \infty} \left( \frac{1}{(1+\frac{1}{n})^n} \right) = \frac{1}{e} < 1$$

- The series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{1}{n+1}}{\frac{1}{n}} \right| = \lim_{n \to \infty} \left( \frac{n}{n+1} \right) = 1 - \lim_{n \to \infty} \frac{1}{n+1} = 1 - 0 = 1 = 1$$

- The series $\sum_{n=1}^{\infty} \frac{(-1)^n}{n}$ is inconclusive by the ratio test, because

$$L = \lim_{n \to \infty} \left| \frac{\frac{(-1)^{n+1}}{n+1}}{\frac{(-1)^n}{n}} \right| = \lim_{n \to \infty} \left( \frac{n}{n+1} \right) = 1 - \lim_{n \to \infty} \frac{1}{n+1} = 1 - 0 = 1 = 1$$

However, this series converges by the alternating series test.

## Advantages and disadvantages of the test

The ratio test is useful for testing the convergence of series that involve factorials, exponentials, or powers of n. It is also easy to apply, as it only requires finding the limit of a simple ratio.

However, the ratio test has some limitations. It cannot be used for series that have zero terms, or series that have terms with different signs. It also does not give any information about the rate of convergence or the value of the sum. Moreover, it is often inconclusive when the limit of the ratio is equal to one, which requires using other