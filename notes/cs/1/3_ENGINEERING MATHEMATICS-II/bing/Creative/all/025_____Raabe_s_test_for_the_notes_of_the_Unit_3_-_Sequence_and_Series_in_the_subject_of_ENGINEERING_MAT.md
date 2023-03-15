# Raabe's test

Raabe's test is a test for the convergence of a series of the form

$$\sum_{n=1}^{\infty} a_n$$

where each term is a real or complex number and $a_n \neq 0$ for large $n$.

The test was developed by Swiss mathematician Joseph Ludwig Raabe in 1832.

The test is based on the ratio of consecutive terms of the series, and compares it with a constant.

The test can be stated as follows:

- Let $L$ be the limit

$$L = \lim_{n \to \infty} n \left( \frac{a_n}{a_{n+1}} - 1 \right)$$

- If $L > 1$, then the series converges absolutely.
- If $L < 1$, then the series diverges.
- If $L = 1$ or the limit does not exist, then the test is inconclusive.

## Example

Consider the series

$$\sum_{n=1}^{\infty} \frac{n!}{n^n}$$

To apply Raabe's test, we compute the limit

$$L = \lim_{n \to \infty} n \left( \frac{n!}{n^n} \cdot \frac{(n+1)^{n+1}}{(n+1)!} - 1 \right)$$

Using the fact that

$$\lim_{n \to \infty} \frac{(n+1)^{n+1}}{n^n} = e$$

we get

$$L = \lim_{n \to \infty} n \left( \frac{e}{n+1} - 1 \right)$$

Simplifying, we obtain

$$L = \lim_{n \to \infty} \frac{e - n - 1}{n+1} = -1$$

Since $L < 1$, Raabe's test tells us that the series diverges.