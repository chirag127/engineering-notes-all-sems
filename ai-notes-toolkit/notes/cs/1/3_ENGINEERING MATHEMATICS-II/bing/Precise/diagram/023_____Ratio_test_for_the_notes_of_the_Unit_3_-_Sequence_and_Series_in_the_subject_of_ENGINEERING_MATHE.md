### Ratio Test

The Ratio Test is a method used to determine the convergence or divergence of an infinite series. It is particularly useful for series with positive terms and factorials or exponential functions.

Here are the steps to apply the Ratio Test:

1. Given an infinite series `∑a_n`, consider the limit `L = lim_(n→∞) |a_(n+1)/a_n|`
2. If `L < 1`, the series converges absolutely.
3. If `L > 1` or `L = ∞`, the series diverges.
4. If `L = 1`, the test is inconclusive and another test must be used.

It is important to note that the Ratio Test only provides information about the absolute convergence of a series. If a series converges absolutely, it also converges, but the converse is not necessarily true.

Example:

Consider the series `∑(n!)/(n^n)`. To apply the Ratio Test, we need to find the limit `L = lim_(n→∞) |a_(n+1)/a_n|`.

`L = lim_(n→∞) |((n+1)!)/(n+1)^(n+1)| / |(n!)/(n^n)|`

`= lim_(n→∞) |((n+1)!)/(n+1)^(n+1)| * |(n^n)/(n!)|`

`= lim_(n→∞) |(n+1)/(n+1)| * |(n^n)/(n+1)^n|`

`= lim_(n→∞) |(n^n)/(n+1)^n|`

`= lim_(n→∞) |(n/(n+1))^n|`

`= lim_(n→∞) |(1/(1+1/n))^n|`

`= 1/e`

Since `L < 1`, the series `∑(n!)/(n^n)` converges absolutely by the Ratio Test.