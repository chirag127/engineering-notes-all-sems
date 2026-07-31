### Convergence of series

- A series is the sum of the terms of a sequence, denoted by $\sum_{n=1}^{\infty} a_n$ or $a_1 + a_2 + a_3 + \cdots$.
- A series is said to be convergent if the sequence of its partial sums, denoted by $S_n = \sum_{k=1}^{n} a_k$, approaches a finite limit as $n$ tends to infinity, i.e., $\lim_{n \to \infty} S_n = L$, where $L$ is a finite number.
- A series is said to be divergent if the sequence of its partial sums does not approach a finite limit as $n$ tends to infinity, i.e., $\lim_{n \to \infty} S_n$ does not exist or is infinite.
- A series can be tested for convergence or divergence using various methods, such as the following:

  - The **nth term test**: If $\lim_{n \to \infty} a_n \neq 0$, then the series $\sum_{n=1}^{\infty} a_n$ is divergent. If $\lim_{n \to \infty} a_n = 0$, then the test is inconclusive and another method is needed.
  - The **integral test**: If $f(x)$ is a positive, continuous and decreasing function on $[1, \infty)$ and $a_n = f(n)$ for all $n \geq 1$, then the series $\sum_{n=1}^{\infty} a_n$ and the improper integral $\int_{1}^{\infty} f(x) dx$ have the same behavior, i.e., they are both convergent or both divergent.
  - The **comparison test**: If $0 \leq a_n \leq b_n$ for all $n \geq 1$, then
    - If $\sum_{n=1}^{\infty} b_n$ is convergent, then $\sum_{n=1}^{\infty} a_n$ is also convergent.
    - If $\sum_{n=1}^{\infty} a_n$ is divergent, then $\sum_{n=1}^{\infty} b_n$ is also divergent.
  - The **limit comparison test**: If $a_n > 0$ and $b_n > 0$ for all $n \geq 1$, and $\lim_{n \to \infty} \frac{a_n}{b_n} = c$, where $c$ is a positive finite number, then $\sum_{n=1}^{\infty} a_n$ and $\sum_{n=1}^{\infty} b_n$ have the same behavior, i.e., they are both convergent or both divergent.
  - The **ratio test**: If $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = L$, then
    - If $L < 1$, then the series $\sum_{n=1}^{\infty} a_n$ is absolutely convergent, and hence convergent.
    - If $L > 1$, then the series $\sum_{n=1}^{\infty} a_n$ is divergent.
    - If $L = 1$, then the test is inconclusive and another method is needed.
  - The **root test**: If $\lim_{n \to \infty} \sqrt[n]{|a_n|} = L$, then
    - If $L < 1$, then the series $\sum_{n=1}^{\infty} a_n$ is absolutely convergent, and hence convergent.
    - If $L > 1$, then the series $\sum_{n=1}^{\infty} a_n$ is divergent.
    - If $L = 1$, then the test is inconclusive and another method is needed.
  - The **alternating series test**: If $a_n$ is a sequence of positive terms that satisfies
    - $a_n \geq a_{n+1}$ for all $n \geq 1$, i.e., the sequence is decreasing, and
    - $\lim_{n \to \infty} a_n = 0$, i.e., the sequence approaches zero,
    then the alternating series $\sum_{n=1}^{\infty} (-1)^{n