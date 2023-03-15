### Raabe's test

Raabe's test is a test for the convergence of a series of the form

$$\sum_{n=1}^{\infty} a_n$$

where each term $a_n$ is a real or complex number. The test was developed by Swiss mathematician Joseph Ludwig Raabe in 1832.

The test is based on the ratio of consecutive terms of the series, and compares it with a constant $r$. The test states that:

- If $\lim_{n\to\infty} n(r - \frac{a_{n+1}}{a_n}) > 1$, then the series converges.
- If $\lim_{n\to\infty} n(r - \frac{a_{n+1}}{a_n}) < 1$, then the series diverges.
- If $\lim_{n\to\infty} n(r - \frac{a_{n+1}}{a_n}) = 1$, then the test is inconclusive.

The test can be derived from Kummer's test, which is a more general test for convergence of series. Raabe's test is a special case of Kummer's test when $b_n = n$.

To apply Raabe's test, we need to find the limit of $n(r - \frac{a_{n+1}}{a_n})$ as $n$ approaches infinity. This can be done by using L'Hopital's rule, or by using some algebraic manipulation.

For example, consider the series

$$\sum_{n=1}^{\infty} \frac{n!}{n^n}$$

To apply Raabe's test, we need to find the limit of

$$n(r - \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!})$$

as $n$ approaches infinity. Simplifying, we get

$$n(r - \frac{n^n}{(n+1)^n})$$

Using L'Hopital's rule, we get

$$\lim_{n\to\infty} n(r - \frac{n^n}{(n+1)^n}) = \lim_{n\to\infty} \frac{r - \frac{n^n}{(n+1)^n}}{\frac{1}{n}} = \lim_{n\to\infty} (r - \frac{n^n}{(n+1)^n})n^2$$

Using L'Hopital's rule again, we get

$$\lim_{n\to\infty} (r - \frac{n^n}{(n+1)^n})n^2 = \lim_{n\to\infty} \frac{-\frac{n^n}{(n+1)^{n+1}}(\ln(n+1) - \ln n)}{\frac{-2}{n^3}} = \lim_{n\to\infty} \frac{n^n}{(n+1)^{n+1}}(\ln(n+1) - \ln n)n^4$$

Using L'Hopital's rule one more time, we get

$$\lim_{n\to\infty} \frac{n^n}{(n+1)^{n+1}}(\ln(n+1) - \ln n)n^4 = \lim_{n\to\infty} \frac{\frac{n^n}{(n+1)^{n+1}}(\frac{1}{n+1} - \frac{1}{n})n^4 + \frac{n^n}{(n+1)^{n+1}}(\ln(n+1) - \ln n)4n^3}{\frac{12}{n^5}}$$

Simplifying, we get

$$\lim_{n\to\infty} \frac{\frac{n^n}{(n+1)^{n+1}}(\frac{1}{n+1} - \frac{1}{n})n^4 + \frac{n^n}{(n+1)^{n+1}}(\ln(n+1) - \ln n)4n^3}{\frac{12}{n^5}} = \lim_{n\to\infty} \frac{n^n}{(n+1)^{n+1}}(\frac{n^5}{n+1} - n^5