### D’ Alembert’s test for convergence of series

- D’ Alembert’s test, also known as the ratio test, is a criterion for the convergence of a series of real or complex numbers, where each term is nonzero when n is large .
- The test was first published by Jean le Rond d'Alembert in 1768.
- The test is based on the limit of the ratio of consecutive terms of the series .
- The test can be stated as follows:

  - Let $\sum_{n=1}^{\infty} a_n$ be a series of real or complex numbers, and let the sequence $a_n$ satisfy: $$\lim_{n \to \infty} \frac{a_{n+1}}{a_n} = L$$
  - If $L > 1$, then the series diverges.
  - If $L < 1$, then the series converges absolutely.
  - If $L = 1$, then the test is inconclusive and the series may converge or diverge.

- The test can be applied to series of positive terms by taking the absolute value of the ratio.
- The test can also be modified to use the root of the terms instead of the ratio, which is known as the Cauchy root test.
- The test is useful for series involving factorials, exponentials, or powers.
- The test can be proved using the comparison test and the squeeze theorem.
- The test can be illustrated by some examples:

  - The series $\sum_{n=1}^{\infty} \frac{1}{n}$ diverges, since $$\lim_{n \to \infty} \frac{\frac{1}{n+1}}{\frac{1}{n}} = \lim_{n \to \infty} \frac{n}{n+1} = 1$$
  - The series $\sum_{n=1}^{\infty} \frac{1}{n^2}$ converges, since $$\lim_{n \to \infty} \frac{\frac{1}{(n+1)^2}}{\frac{1}{n^2}} = \lim_{n \to \infty} \frac{n^2}{(n+1)^2} = \frac{1}{1 + \frac{2}{n} + \frac{1}{n^2}} < 1$$
  - The series $\sum_{n=1}^{\infty} \frac{n!}{n^n}$ converges, since $$\lim_{n \to \infty} \frac{\frac{(n+1)!}{(n+1)^{n+1}}}{\frac{n!}{n^n}} = \lim_{n \to \infty} \frac{n^n}{(n+1)^n} \cdot \frac{1}{n+1} = \lim_{n \to \infty} \frac{1}{(1 + \frac{1}{n})^n} \cdot \frac{1}{n+1} = \frac{1}{e} \cdot 0 = 0 < 1$$