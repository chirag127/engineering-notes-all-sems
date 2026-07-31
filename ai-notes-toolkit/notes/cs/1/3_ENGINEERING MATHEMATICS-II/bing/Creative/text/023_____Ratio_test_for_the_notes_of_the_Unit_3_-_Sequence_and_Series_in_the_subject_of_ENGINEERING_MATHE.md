### Ratio test

- The ratio test is a test for the convergence of a series where each term is a real or complex number and an is nonzero when n is large.
- The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.
- The test is based on the comparison of the ratio of consecutive terms of the series with a limit L as n approaches infinity.
- The ratio test states that:

  - if L < 1 then the series converges absolutely;
  - if L > 1 then the series diverges;
  - if L = 1 or the limit fails to exist, then the test is inconclusive, because there exist both convergent and divergent series that satisfy this case.

- The ratio test can be applied to any series, but it may not always yield a conclusive answer.
- The ratio test is useful for series involving factorials, exponentials, or powers.
- The ratio test can be derived from the comparison test by using the limit comparison test.

- An example of applying the ratio test is:

  - Consider the series ∑ n = 1 ∞ n ! n n
  - To apply the ratio test, we need to find the limit of the ratio of consecutive terms as n approaches infinity:

    - lim n → ∞ | a n + 1 a n | = lim n → ∞ | ( n + 1 ) ! ( n + 1 ) n + 1 n ! n n | = lim n → ∞ | ( n + 1 ) n n | = lim n → ∞ | ( 1 + 1 n ) n | = e

  - Since the limit is greater than 1, the ratio test tells us that the series diverges.