### Laplace transform of derivatives and integrals

- Laplace transform is a technique that converts a function of a real variable (usually time) into a function of a complex variable (usually frequency).
- Laplace transform can be used to solve differential equations and integral equations by transforming them into algebraic equations in the frequency domain.
- Laplace transform is defined as

$$
\mathcal{L}\{f(t)\} = F(s) = \int_{0}^{\infty} e^{-st} f(t) dt
$$

where $s$ is a complex variable and $f(t)$ is a function of a real variable $t$.

- Laplace transform has some properties that make it useful for solving differential and integral equations. Some of these properties are:

  - Linearity: $\mathcal{L}\{a f(t) + b g(t)\} = a \mathcal{L}\{f(t)\} + b \mathcal{L}\{g(t)\}$ for any constants $a$ and $b$.
  - First derivative: $\mathcal{L}\{f'(t)\} = s \mathcal{L}\{f(t)\} - f(0)$
  - Second derivative: $\mathcal{L}\{f''(t)\} = s^2 \mathcal{L}\{f(t)\} - s f(0) - f'(0)$
  - Higher order derivatives: $\mathcal{L}\{f^{(n)}(t)\} = s^n \mathcal{L}\{f(t)\} - s^{n-1} f(0) - s^{n-2} f'(0) - \cdots - f^{(n-1)}(0)$
  - Integral: $\mathcal{L}\{\int_{0}^{t} f(\tau) d\tau\} = \frac{1}{s} \mathcal{L}\{f(t)\}$

- Laplace transform can be used to solve differential equations by applying the properties of the transform to both sides of the equation and then solving for the unknown function in the frequency domain. For example, to solve the equation

$$
y'' + 2 y' + y = e^{-t}
$$

with initial conditions $y(0) = 0$ and $y'(0) = 1$, we can take the Laplace transform of both sides and get

$$
s^2 Y(s) - s y(0) - y'(0) + 2 s Y(s) - 2 y(0) + Y(s) = \frac{1}{s + 1}
$$

where $Y(s) = \mathcal{L}\{y(t)\}$. Simplifying and solving for $Y(s)$, we get

$$
Y(s) = \frac{s + 2}{(s + 1)(s^2 + 2 s + 1)}
$$

To find the solution $y(t)$, we need to apply the inverse Laplace transform, which can be done by using partial fraction decomposition and the table of Laplace transforms. We get

$$
y(t) = \mathcal{L}^{-1}\{Y(s)\} = e^{-t} - e^{-t} \cos t - e^{-t} \sin t
$$

- Laplace transform can also be used to solve integral equations by transforming them into algebraic equations in the frequency domain. For example, to solve the equation

$$
y(t) = \int_{0}^{t} e^{-\tau} y(t - \tau) d\tau + \sin t
$$

we can take the Laplace transform of both sides and get

$$
Y(s) = \frac{1}{s} Y(s) \frac{1}{s + 1} + \frac{1}{s^2 + 1}
$$

where $Y(s) = \mathcal{L}\{y(t)\}$. Simplifying and solving for $Y(s)$, we get

$$
Y(s) = \frac{s + 1}{s^2 (s + 1) - 1} + \frac{1}{s^2 + 1}
$$

To find the solution $y(t)$, we need to apply the inverse Laplace transform, which can be done by using partial fraction decomposition and the table of Laplace transforms. We get