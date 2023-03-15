### Properties of Laplace Transform

The Laplace transform is a powerful tool for solving linear differential equations and analyzing linear systems. It transforms a function of time, $f(t)$, into a function of a complex variable, $F(s)$, where $s = \sigma + i\omega$ is the frequency parameter. The Laplace transform of $f(t)$ is defined as

$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt
$$

The Laplace transform has several properties that make it useful for manipulating and solving equations. Some of the most important properties are:

- **Linearity**: The Laplace transform is a linear operator, which means that if $a$ and $b$ are constants and $f(t)$ and $g(t)$ are functions, then

$$
\mathcal{L}\{af(t) + bg(t)\} = a\mathcal{L}\{f(t)\} + b\mathcal{L}\{g(t)\}
$$

This property allows us to transform linear combinations of functions easily.

- **Differentiation**: The Laplace transform transforms differentiation in time to multiplication by $s$ in the frequency domain. If $f(t)$ and its derivative $f'(t)$ are both Laplace transformable, then

$$
\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0)
$$

This property allows us to transform differential equations into algebraic equations.

- **Integration**: The Laplace transform transforms integration in time to division by $s$ in the frequency domain. If $f(t)$ is Laplace transformable and $F(s) = \mathcal{L}\{f(t)\}$, then

$$
\mathcal{L}\left\{\int_0^t f(\tau) d\tau\right\} = \frac{F(s)}{s}
$$

This property allows us to transform integral equations into algebraic equations.

- **Multiplication by $t^n$**: The Laplace transform transforms multiplication by a power of time to differentiation with respect to $s$ in the frequency domain. If $f(t)$ is Laplace transformable and $F(s) = \mathcal{L}\{f(t)\}$, then

$$
\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n}{ds^n} F(s)
$$

This property allows us to transform functions that involve powers of time.

- **Frequency shifting**: The Laplace transform shifts the frequency parameter by a constant amount. If $f(t)$ is Laplace transformable and $F(s) = \mathcal{L}\{f(t)\}$, then

$$
\mathcal{L}\{e^{at} f(t)\} = F(s-a)
$$

This property allows us to transform functions that involve exponential factors.

- **Time scaling**: The Laplace transform scales the time variable by a constant factor. If $f(t)$ is Laplace transformable and $F(s) = \mathcal{L}\{f(t)\}$, then

$$
\mathcal{L}\{f(at)\} = \frac{1}{a} F\left(\frac{s}{a}\right)
$$

This property allows us to transform functions that involve scaling of time.

- **Time shifting**: The Laplace transform shifts the time variable by a constant amount. If $f(t)$ is Laplace transformable and $F(s) = \mathcal{L}\{f(t)\}$, then

$$
\mathcal{L}\{f(t-a)\} = e^{-as} F(s)
$$

This property allows us to transform functions that involve delays or advances of time.

- **Convolution**: The Laplace transform transforms the convolution of two functions to the product of their Laplace transforms. If $f(t)$ and $g(t)$ are Laplace transformable and $F(s) = \mathcal{L}\{f(t)\}$ and $G(s) = \mathcal{L}\{g(t)\}$, then

$$
\mathcal{L}\{f(t) * g(t)\} = F(s) G(s)
$$

where $f(t) * g(t)$ denotes the convolution of $f(t)$ and $g(t)$, defined as

$$
f(t)