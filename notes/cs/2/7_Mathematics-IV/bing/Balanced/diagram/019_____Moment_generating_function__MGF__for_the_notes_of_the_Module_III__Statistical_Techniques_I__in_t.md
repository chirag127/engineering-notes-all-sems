### Moment generating function (MGF)

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
- The MGF has the following properties:
  - It is uniquely determined by the distribution of $X$, i.e., if two random variables have the same MGF, they have the same distribution.
  - It can be used to easily derive the moments of $X$, i.e., the expected value of $X^n$ for any positive integer $n$. This is because the $n$-th derivative of $M_X(t)$ at $t=0$ is equal to $E[X^n]$, i.e.,

  $$
  E[X^n] = M_X^{(n)}(0) = \frac{d^n}{dt^n} M_X(t) \bigg|_{t=0}
  $$

  - It can be used to find the distribution of a linear transformation of $X$, i.e., if $Y = aX + b$, where $a$ and $b$ are constants, then the MGF of $Y$ is given by:

  $$
  M_Y(t) = E[e^{tY}] = E[e^{t(aX + b)}] = e^{tb} E[e^{taX}] = e^{tb} M_X(at)
  $$

- The MGF does not always exist for every random variable, unlike the characteristic function. It exists only if there is some positive number $h$ such that $M_X(t)$ is finite for all $t$ in the interval $(-h, h)$.