### Properties of Laplace Transform

The Laplace transform is a powerful tool for solving linear differential equations and analyzing linear systems. It transforms a function of time, f(t), into a function of a complex variable, s, F(s). The Laplace transform has the following definition:

$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st}f(t)dt
$$

where s is a complex number, $s = \sigma + i\omega$, and $i = \sqrt{-1}$.

The Laplace transform has a number of properties that make it useful for manipulating and solving equations. Some of the most important properties are:

- **Linearity**: The Laplace transform is a linear operator, which means that it preserves the operations of addition and scalar multiplication. That is, if a and b are constants and f and g are functions, then

$$
\mathcal{L}\{af(t) + bg(t)\} = a\mathcal{L}\{f(t)\} + b\mathcal{L}\{g(t)\}
$$

- **Differentiation**: The Laplace transform transforms differentiation in the time domain to multiplication by s in the s-domain, plus some initial conditions. That is, if f and its derivatives are continuous and of exponential order, then

$$
\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0)
$$

$$
\mathcal{L}\{f''(t)\} = s^2\mathcal{L}\{f(t)\} - sf(0) - f'(0)
$$

and so on for higher order derivatives.

- **Integration**: The Laplace transform transforms integration in the time domain to division by s in the s-domain, plus some initial conditions. That is, if f is continuous and of exponential order, then

$$
\mathcal{L}\{\int_0^t f(\tau)d\tau\} = \frac{1}{s}\mathcal{L}\{f(t)\} + \frac{f(0)}{s}
$$

- **Multiplication by t**: The Laplace transform transforms multiplication by t in the time domain to differentiation with respect to s in the s-domain. That is, if f is continuous and of exponential order, then

$$
\mathcal{L}\{tf(t)\} = -\frac{d}{ds}\mathcal{L}\{f(t)\}
$$

- **Frequency shifting**: The Laplace transform transforms multiplication by $e^{at}$ in the time domain to shifting by a in the s-domain. That is, if f is continuous and of exponential order, then

$$
\mathcal{L}\{e^{at}f(t)\} = \mathcal{L}\{f(t)\}|_{s-a} = F(s-a)
$$

- **Time scaling**: The Laplace transform transforms scaling by a in the time domain to scaling by $1/a$ in the s-domain. That is, if f is continuous and of exponential order, and a is a positive constant, then

$$
\mathcal{L}\{f(at)\} = \frac{1}{a}\mathcal{L}\{f(t)\}|_{s/a} = \frac{1}{a}F\left(\frac{s}{a}\right)
$$

- **Time shifting**: The Laplace transform transforms shifting by a in the time domain to multiplication by $e^{-as}$ in the s-domain, plus some initial conditions. That is, if f is continuous and of exponential order, and a is a positive constant, then

$$
\mathcal{L}\{f(t-a)\} = e^{-as}\mathcal{L}\{f(t)\} - \int_0^a e^{-st}f(t)dt
$$

- **Convolution**: The Laplace transform transforms convolution in the time domain to multiplication in the s-domain. That is, if f and g are continuous and of exponential order, and their convolution is defined as

$$
(f * g)(t) = \int_0^t f(\tau)g(t-\tau)d\tau
$$

then

$$
\mathcal{L}\{(f * g)(t)\} = \mathcal{L}\{f(t)\}\mathcal{L}\{g(t)\} = F