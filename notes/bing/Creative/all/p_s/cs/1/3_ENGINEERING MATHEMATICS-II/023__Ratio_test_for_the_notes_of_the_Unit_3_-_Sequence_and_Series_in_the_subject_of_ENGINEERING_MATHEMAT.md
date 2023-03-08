### Ratio test

- The ratio test is a method for testing the convergence or divergence of an infinite series of real or complex numbers, where each term is nonzero when n is large.
- The test was first published by Jean le Rond d'Alembert and is sometimes known as d'Alembert's ratio test or as the Cauchy ratio test.
- The test is based on the idea that if the ratio of two consecutive terms of a series approaches a limit L as n goes to infinity, then the series behaves like a geometric series with common ratio L.
- The ratio test states that:

  - If L < 1, then the series converges absolutely.
  - If L > 1, then the series diverges.
  - If L = 1 or the limit fails to exist, then the test is inconclusive, because there exist both convergent and divergent series that satisfy this case.

- The ratio test can be applied to any series, but it may not always yield a conclusive answer.
- The ratio test is useful for series involving factorials, exponentials, or powers.

- To apply the ratio test, we need to compute the limit of the ratio of the absolute value of the (n+1)th term to the nth term of the series, as n goes to infinity. That is,

  ```
  L = lim n->inf |a_(n+1)/a_n|
  ```

- For example, consider the series

  ```
  sum n=1 to inf (n!)^2/(2n)!
  ```

- To apply the ratio test, we compute

  ```
  L = lim n->inf |((n+1)!)^2/(2(n+1))!| / |(n!)^2/(2n)!|
    = lim n->inf |(n+1)^2/(2n+1)(2n+2)|
    = lim n->inf |(n+1)^2/4(n+1)^2|
    = 1/4
  ```

- Since L < 1, the series converges absolutely by the ratio test.

Some possible mnemonics and learning tricks for the ratio test are:

- To remember the formula for the limit L, think of the word "LAR" (like a pirate), which stands for Limit of Absolute value of Ratio.
- To remember the cases for convergence and divergence, think of the acronym "CLD" (like cold), which stands for Converges if Less than one, Diverges if greater than one.
- To remember that the test is inconclusive if L = 1 or the limit does not exist, think of the phrase "One is no fun", or "No limit, no clue".
- To remember some examples of series that can be tested by the ratio test, think of the words "FEP" (like fap), which stands for Factorials, Exponentials, and Powers.