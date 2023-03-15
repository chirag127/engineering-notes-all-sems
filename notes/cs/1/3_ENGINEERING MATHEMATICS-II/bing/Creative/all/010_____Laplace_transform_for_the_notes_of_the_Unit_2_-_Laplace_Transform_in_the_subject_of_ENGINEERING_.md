# Laplace Transform

## Definition

The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency). It is defined as follows:

$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t) dt
$$

where $s$ is a complex variable of the form $s = \sigma + j \omega$, and $f(t)$ is a function of time that is defined for $t \geq 0$.

The Laplace transform is useful for solving linear differential equations, as it reduces them to algebraic equations that can be solved by the formal rules of algebra. It also provides a convenient way to analyze the behavior of systems in the frequency domain, such as mechanical and electrical systems.

## Properties

The Laplace transform has many important properties that make it easier to manipulate and apply. Some of the most common properties are:

- Linearity: If $f(t)$ and $g(t)$ are two functions with Laplace transforms $F(s)$ and $G(s)$, and $a$ and $b$ are constants, then

$$
\mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)
$$

- Shift in time: If $f(t)$ has Laplace transform $F(s)$, and $a$ is a constant, then

$$
\mathcal{L}\{f(t-a)\} = e^{-as} F(s)
$$

- Shift in frequency: If $f(t)$ has Laplace transform $F(s)$, and $a$ is a constant, then

$$
\mathcal{L}\{e^{at} f(t)\} = F(s-a)
$$

- Scaling: If $f(t)$ has Laplace transform $F(s)$, and $a$ is a constant, then

$$
\mathcal{L}\{f(at)\} = \frac{1}{a} F\left(\frac{s}{a}\right)
$$

- Derivative in time: If $f(t)$ has Laplace transform $F(s)$, and $f'(t)$ is its derivative, then

$$
\mathcal{L}\{f'(t)\} = sF(s) - f(0)
$$

- Derivative in frequency: If $f(t)$ has Laplace transform $F(s)$, and $F'(s)$ is its derivative, then

$$
\mathcal{L}\{t f(t)\} = -F'(s)
$$

- Integration in time: If $f(t)$ has Laplace transform $F(s)$, and $F(t)$ is its antiderivative, then

$$
\mathcal{L}\{F(t)\} = \frac{1}{s} F(s) + \frac{F(0)}{s}
$$

- Integration in frequency: If $f(t)$ has Laplace transform $F(s)$, and $f(t)$ is integrable over $[0, \infty)$, then

$$
\mathcal{L}\{\int_0^t f(\tau) d\tau\} = \frac{1}{s} F(s)
$$

- Convolution: If $f(t)$ and $g(t)$ are two functions with Laplace transforms $F(s)$ and $G(s)$, and $f(t) * g(t)$ is their convolution, defined as

$$
f(t) * g(t) = \int_0^t f(\tau) g(t - \tau) d\tau
$$

then

$$
\mathcal{L}\{f(t) * g(t)\} = F(s) G(s)
$$

- Initial value theorem: If $f(t)$ has Laplace transform $F(s)$, and $f(t)$ is continuous and has a finite limit as $t \to 0^+$, then

$$
\lim_{t \to 0^+} f(t) = \lim_{s \to \infty} sF(s)
$$

- Final value theorem: If $f(t)$ has Laplace transform $F(s)$, and $f(t)$ and $f'(t)$ are both bounded as $t \to \infty$, then

$$
\lim_{t \to \infty} f(t) =