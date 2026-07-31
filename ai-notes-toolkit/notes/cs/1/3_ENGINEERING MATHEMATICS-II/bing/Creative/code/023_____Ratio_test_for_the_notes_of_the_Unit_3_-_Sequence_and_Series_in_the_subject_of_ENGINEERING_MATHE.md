### Ratio test

The ratio test is a method for testing the convergence of a series of real or complex numbers. It is based on the idea of comparing the ratio of successive terms of the series to a limit value. The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.

The ratio test can be stated as follows:

Let $\sum_{n=1}^{\infty} a_n$ be a series of nonzero terms. Define the limit

$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$

Then,

- If $L < 1$, the series converges absolutely.
- If $L > 1$, the series diverges.
- If $L = 1$ or the limit does not exist, the test is inconclusive.

The ratio test is useful for series that involve factorials, exponentials, or powers of n. However, it may not work for some series that converge conditionally, such as the alternating harmonic series.

Here are some examples of applying the ratio test:

- Consider the series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$. Using the ratio test, we have

$$L = \lim_{n \to \infty} \left| \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} \right|$$

$$= \lim_{n \to \infty} \left| \frac{n^n}{(n+1)^n} \cdot \frac{1}{n+1} \right|$$

$$= \lim_{n \to \infty} \left| \frac{1}{\left(1 + \frac{1}{n}\right)^n} \cdot \frac{1}{n+1} \right|$$

$$= \frac{1}{e} \cdot 0$$

$$= 0$$

Since $L < 1$, the series converges absolutely.

- Consider the series $\sum_{n=1}^{\infty} \frac{2^n}{n^2}$. Using the ratio test, we have

$$L = \lim_{n \to \infty} \left| \frac{2^{n+1}}{(n+1)^2} \cdot \frac{n^2}{2^n} \right|$$

$$= \lim_{n \to \infty} \left| 2 \cdot \frac{n^2}{(n+1)^2} \right|$$

$$= 2$$

Since $L > 1$, the series diverges.

- Consider the series $\sum_{n=1}^{\infty} \frac{(-1)^n}{n}$. Using the ratio test, we have

$$L = \lim_{n \to \infty} \left| \frac{(-1)^{n+1}}{n+1} \cdot \frac{n}{(-1)^n} \right|$$

$$= \lim_{n \to \infty} \left| \frac{n}{n+1} \right|$$

$$= 1$$

Since $L = 1$, the test is inconclusive. In fact, this series converges conditionally by the alternating series test, but not absolutely.