### Convergence of series

- A series is an expression of the form `a_1 + a_2 + a_3 + ...` where `a_n` is the n-th term of a sequence.
- A series is convergent if the sequence of its partial sums `S_n = a_1 + a_2 + ... + a_n` tends to a limit `L` as `n` goes to infinity. In this case, we write `a_1 + a_2 + a_3 + ... = L`  .
- A series is divergent if the sequence of its partial sums does not have a limit, or has a limit that is infinite  .
- A necessary condition for a series to converge is that the sequence of its terms `a_n` must tend to zero as `n` goes to infinity. This follows from the fact that if `a_n` does not tend to zero, then `S_n` cannot tend to a finite limit.
- However, this condition is not sufficient, as there are series whose terms tend to zero but the series diverges. For example, the harmonic series `1 + 1/2 + 1/3 + 1/4 + ...` diverges, even though `1/n` tends to zero as `n` goes to infinity.
- To determine whether a series converges or diverges, we need to use various tests and methods that compare the series with known convergent or divergent series, or that examine the behavior of the series terms or partial sums. Some of these tests and methods are:

  - The geometric series test: A geometric series is a series of the form `a + ar + ar^2 + ...` where `a` and `r` are constants. A geometric series converges if and only if `|r| < 1`, and in this case, the sum is `a/(1-r)`  .
  - The p-series test: A p-series is a series of the form `1/n^p` where `p` is a constant. A p-series converges if and only if `p > 1`, and in this case, the sum is `pi^2/6` for `p = 2`, and `zeta(p)` for `p > 2`, where `zeta` is the Riemann zeta function  .
  - The integral test: If `f` is a positive, continuous, and decreasing function on `[1, infinity)` and `a_n = f(n)`, then the series `a_1 + a_2 + a_3 + ...` converges if and only if the improper integral `int_1^infinity f(x) dx` converges  .
  - The comparison test: If `0 <= a_n <= b_n` for all `n`, and the series `b_1 + b_2 + b_3 + ...` converges, then the series `a_1 + a_2 + a_3 + ...` also converges. Conversely, if `0 <= b_n <= a_n` for all `n`, and the series `b_1 + b_2 + b_3 + ...` diverges, then the series `a_1 + a_2 + a_3 + ...` also diverges  .
  - The limit comparison test: If `a_n` and `b_n` are positive sequences and `lim_(n->infinity) a_n/b_n = L` where `L` is a positive finite number, then the series `a_1 + a_2 + a_3 + ...` and `b_1 + b_2 + b_3 + ...` either both converge or both diverge  .
  - The alternating series test: An alternating series is a series of the form `a_1 - a_2 + a_3 - a_4 + ...` where `a_n > 0` for all `n`. An alternating series converges if the sequence `a_n` is decreasing and tends to zero as `n` goes to infinity[^1