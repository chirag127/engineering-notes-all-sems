### Ratio Test

The Ratio Test is a method used to test the convergence or divergence of an infinite series. It is particularly useful for series with positive terms and factorials or exponential functions.

The test is performed as follows:

1. Given an infinite series `∑a_n`, compute the limit `L = lim_(n→∞) |a_(n+1)/a_n|`
2. If `L < 1`, the series converges absolutely.
3. If `L > 1`, the series diverges.
4. If `L = 1`, the test is inconclusive and another test must be used.

Here is an example of how to apply the Ratio Test:

Consider the series `∑(2^n)/(n!)`. To apply the Ratio Test, we compute the limit `L = lim_(n→∞) |((2^(n+1))/((n+1)!))/((2^n)/(n!))|`. Simplifying, we get `L = lim_(n→∞) (2^(n+1))/(n+1)! * n!/2^n = lim_(n→∞) 2/(n+1) = 0`. Since `L < 1`, the series converges absolutely.

It is important to note that the Ratio Test only provides information about the absolute convergence of a series. If a series converges absolutely, it also converges, but the converse is not necessarily true. If the Ratio Test is inconclusive, another test must be used to determine the convergence or divergence of the series.