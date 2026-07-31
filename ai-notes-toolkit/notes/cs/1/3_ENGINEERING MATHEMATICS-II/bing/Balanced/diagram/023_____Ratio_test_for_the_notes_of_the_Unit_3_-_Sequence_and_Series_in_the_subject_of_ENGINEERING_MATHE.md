### Ratio test

The ratio test is a criterion for the convergence of a series where each term is a real or complex number and an is nonzero when n is large. The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.

The ratio test states that, given a series of the form

$$\sum_{n=1}^{\infty} a_n$$

we can compute the limit

$$L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$$

and then:

- if L < 1 then the series converges absolutely;
- if L > 1 then the series diverges;
- if L = 1 or the limit fails to exist, then the test is inconclusive, because there exist both convergent and divergent series that satisfy this case.

The ratio test works by comparing the ratio of successive terms to 1. If the ratio is less than 1, then the terms are getting smaller and smaller and the series will converge. If the ratio is greater than 1, then the terms are getting larger and larger and the series will diverge. If the ratio is equal to 1, then the terms are not changing much and the test cannot determine the behavior of the series.

The ratio test is useful for series that involve factorials, exponentials, or powers of n. For example, the ratio test can be used to show that the series

$$\sum_{n=1}^{\infty} \frac{n!}{n^n}$$

converges, because

$$L = \lim_{n \to \infty} \left| \frac{(n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{n!} \right| = \lim_{n \to \infty} \frac{n+1}{(n+1)^{n+1}} \cdot n^n = \lim_{n \to \infty} \frac{1}{(n+1)^n} \cdot n^n = \lim_{n \to \infty} \left( \frac{n}{n+1} \right)^n = \frac{1}{e} < 1$$

Therefore, the series converges absolutely by the ratio test.