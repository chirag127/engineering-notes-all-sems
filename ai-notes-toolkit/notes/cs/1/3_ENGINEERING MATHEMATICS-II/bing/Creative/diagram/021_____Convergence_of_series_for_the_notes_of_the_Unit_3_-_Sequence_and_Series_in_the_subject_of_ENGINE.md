### Convergence of series

- A series is an expression of the form `a_1 + a_2 + a_3 + ...` where `a_n` is the n-th term of a sequence.
- A series is convergent if the sequence of its partial sums `S_n = a_1 + a_2 + ... + a_n` tends to a limit `L` as `n` goes to infinity. In this case, we write `a_1 + a_2 + a_3 + ... = L` or `sum_(n=1)^infty a_n = L`.
- A series is divergent if the sequence of its partial sums does not have a limit, or has a limit that is not finite. In this case, we write `a_1 + a_2 + a_3 + ... = infty` or `sum_(n=1)^infty a_n = infty`.
- The limit of a series, if it exists, is called the sum or the value of the series. It is a unique number that does not depend on the order of the terms.
- The convergence or divergence of a series depends on the behavior of the terms `a_n` as `n` goes to infinity. If `a_n` does not approach zero, then the series is divergent by the divergence test. If `a_n` approaches zero, then the series may or may not converge, depending on other factors.
- There are various tests and criteria to determine the convergence or divergence of a series, such as the comparison test, the ratio test, the root test, the integral test, the alternating series test, and others. Each test has its own conditions and limitations, and some series may require more than one test to be applied.
- Some examples of convergent and divergent series are:

  - The geometric series `sum_(n=0)^infty r^n` is convergent if `|r| < 1` and divergent if `|r| >= 1`. The sum is `1/(1-r)` if `|r| < 1`.
  - The harmonic series `sum_(n=1)^infty 1/n` is divergent by the integral test. The partial sums grow logarithmically without bound.
  - The alternating harmonic series `sum_(n=1)^infty (-1)^(n+1)/n` is convergent by the alternating series test. The sum is `ln(2)`.
  - The p-series `sum_(n=1)^infty 1/n^p` is convergent if `p > 1` and divergent if `p <= 1` by the integral test. The sum is `zeta(p)` if `p > 1`, where `zeta` is the Riemann zeta function.
  - The exponential series `sum_(n=0)^infty x^n/n!` is convergent for any `x` by the ratio test. The sum is `e^x`.