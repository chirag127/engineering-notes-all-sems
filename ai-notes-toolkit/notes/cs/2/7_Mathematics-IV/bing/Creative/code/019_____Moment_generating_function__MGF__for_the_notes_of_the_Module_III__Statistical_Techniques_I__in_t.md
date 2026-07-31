# Moment generating function (MGF)

- A moment generating function (MGF) is a function that characterizes the probability distribution of a random variable.
- It is defined as the expected value of $e^{tX}$, where $t$ is a real parameter and $X$ is the random variable.
- The MGF of a random variable $X$ is denoted by $M_X(t)$ and is given by:

$$
M_X(t) = E[e^{tX}] = \begin{cases}
\sum_{x} e^{tx} p(x) & \text{if $X$ is discrete}\\
\int_{-\infty}^{\infty} e^{tx} f(x) dx & \text{if $X$ is continuous}
\end{cases}
$$

- where $p(x)$ is the probability mass function (PMF) of $X$ and $f(x)$ is the probability density function (PDF) of $X$.
- The MGF has the following properties and applications:
  - It is unique for a given distribution, i.e., if two random variables have the same MGF, they have the same distribution.
  - It can be used to derive the moments of a random variable, i.e., the $n$-th moment of $X$ is equal to the $n$-th derivative of $M_X(t)$ evaluated at $t=0$:

  $$
  E[X^n] = M_X^{(n)}(0) = \frac{d^n}{dt^n} M_X(t) \bigg|_{t=0}
  $$

  - It can be used to find the distribution of a linear transformation of a random variable, i.e., if $Y = aX + b$, where $a$ and $b$ are constants, then the MGF of $Y$ is:

  $$
  M_Y(t) = E[e^{tY}] = E[e^{t(aX+b)}] = e^{tb} E[e^{taX}] = e^{tb} M_X(at)
  $$

  - It can be used to find the distribution of a sum of independent random variables, i.e., if $X_1, X_2, \dots, X_n$ are independent random variables and $Y = X_1 + X_2 + \dots + X_n$, then the MGF of $Y$ is:

  $$
  M_Y(t) = E[e^{tY}] = E[e^{t(X_1 + X_2 + \dots + X_n)}] = E[e^{tX_1} e^{tX_2} \dots e^{tX_n}] = E[e^{tX_1}] E[e^{tX_2}] \dots E[e^{tX_n}] = M_{X_1}(t) M_{X_2}(t) \dots M_{X_n}(t)
  $$

- Some examples of MGFs of common distributions are:

  - Binomial distribution: $X \sim \text{Bin}(n, p)$

  $$
  M_X(t) = E[e^{tX}] = \sum_{x=0}^n e^{tx} \binom{n}{x} p^x (1-p)^{n-x} = (1-p + pe^t)^n
  $$

  - Poisson distribution: $X \sim \text{Pois}(\lambda)$

  $$
  M_X(t) = E[e^{tX}] = \sum_{x=0}^{\infty} e^{tx} \frac{\lambda^x e^{-\lambda}}{x!} = e^{-\lambda} \sum_{x=0}^{\infty} \frac{(\lambda e^t)^x}{x!} = e^{-\lambda} e^{\lambda e^t} = e^{\lambda (e^t - 1)}
  $$

  - Normal distribution: $X \sim \mathcal{N}(\mu, \sigma^2)$

  $$
  M_X(t) = E[e^{tX}] = \int_{-\infty}^{\infty} e^{tx} \frac{1}{\sqrt{2\pi\sigma^2}} e^{-\frac{(x-\mu)^2}{2\sigma^2}} dx = e^{\mu t + \frac{1}{2} \sigma^2 t^2}
  $$