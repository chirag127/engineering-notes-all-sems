### Convergence of series

- A series is an expression of the form `∑ a_n` where `a_n` is a sequence of terms.
- A series is convergent if the sequence of its partial sums `s_n = ∑ a_i` from `i = 1` to `n` tends to a limit `s` as `n` goes to infinity. That means that the sum of the terms gets closer and closer to a finite number `s`.
- A series is divergent if the sequence of its partial sums does not tend to a limit, or tends to an infinite limit, as `n` goes to infinity. That means that the sum of the terms either oscillates or grows without bound.
- To determine if a series is convergent or divergent, we can use various tests, such as the nth term test, the comparison test, the ratio test, the root test, the integral test, the alternating series test, etc.
- Some examples of convergent series are:
  - The geometric series `∑ r^n` for `|r| < 1`, which converges to `1/(1-r)`.
  - The harmonic series `∑ 1/n^p` for `p > 1`, which converges to a constant called the p-th harmonic number.
  - The exponential series `∑ x^n/n!` for any `x`, which converges to `e^x`.
- Some examples of divergent series are:
  - The geometric series `∑ r^n` for `|r| >= 1`, which diverges to infinity or oscillates.
  - The harmonic series `∑ 1/n` for `p = 1`, which diverges to infinity.
  - The alternating harmonic series `∑ (-1)^(n+1)/n` for `p = 1`, which converges conditionally but not absolutely.

Some possible mnemonics and learning tricks for the topic are:

- To remember the formula for the sum of a geometric series, you can use the acronym SIR: `S = a/(1-r)`, where `S` is the sum, `I` is the initial term, and `R` is the common ratio.
- To remember the conditions for the ratio test, you can use the acronym LIM: `L = lim |a_(n+1)/a_n|`, where `L` is the limit of the ratio of consecutive terms. If `L < 1`, the series converges absolutely. If `L > 1`, the series diverges. If `L = 1`, the test is inconclusive.
- To remember the conditions for the root test, you can use the acronym LIM again: `L = lim |a_n|^(1/n)`, where `L` is the limit of the nth root of the absolute value of the terms. If `L < 1`, the series converges absolutely. If `L > 1`, the series diverges. If `L = 1`, the test is inconclusive.
- To remember the formula for the p-th harmonic number, you can use the approximation `H_p ~ ln(p) + gamma`, where `H_p` is the sum of the harmonic series `∑ 1/n^p` for `p > 1`, `ln` is the natural logarithm, and `gamma` is the Euler-Mascheroni constant, which is approximately `0.5772`.