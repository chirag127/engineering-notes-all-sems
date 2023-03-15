### Properties of Laplace Transform

The Laplace transform is a powerful tool for solving linear differential equations and analyzing linear systems. It transforms a function of time, f(t), into a function of a complex variable, s, F(s). The Laplace transform has the following definition:

$$
F(s) = \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
$$

where s is a complex number, $s = \sigma + i\omega$, and $e^{-st}$ is the kernel of the transform.

The Laplace transform has a number of properties that make it useful for manipulating and solving equations. Some of the most important properties are:

- **Linearity**: The Laplace transform is a linear operator, which means that it preserves the operations of addition and scalar multiplication. That is, if a and b are constants and f and g are functions, then

$$
\mathcal{L}\{af(t) + bg(t)\} = a\mathcal{L}\{f(t)\} + b\mathcal{L}\{g(t)\}
$$

- **Differentiation**: The Laplace transform transforms differentiation in the time domain to multiplication by s in the frequency domain. That is, if f and its derivative f' are both piecewise continuous on $[0, \infty)$ and of exponential order, then

$$
\mathcal{L}\{f'(t)\} = s\mathcal{L}\{f(t)\} - f(0)
$$

More generally, for any positive integer n,

$$
\mathcal{L}\{f^{(n)}(t)\} = s^n\mathcal{L}\{f(t)\} - s^{n-1}f(0) - s^{n-2}f'(0) - \cdots - f^{(n-1)}(0)
$$

- **Integration**: The Laplace transform transforms integration in the time domain to division by s in the frequency domain. That is, if f is piecewise continuous on $[0, \infty)$ and of exponential order, then

$$
\mathcal{L}\left\{\int_{0}^{t} f(\tau) d\tau\right\} = \frac{1}{s}\mathcal{L}\{f(t)\}
$$

- **Multiplication by t**: The Laplace transform transforms multiplication by t in the time domain to differentiation with respect to s in the frequency domain. That is, if f is piecewise continuous on $[0, \infty)$ and of exponential order, then

$$
\mathcal{L}\{tf(t)\} = -\frac{d}{ds}\mathcal{L}\{f(t)\}
$$

More generally, for any positive integer n,

$$
\mathcal{L}\{t^nf(t)\} = (-1)^n\frac{d^n}{ds^n}\mathcal{L}\{f(t)\}
$$

- **Frequency shifting**: The Laplace transform transforms a function multiplied by an exponential factor in the time domain to a function shifted by the same factor in the frequency domain. That is, if f is piecewise continuous on $[0, \infty)$ and of exponential order, and a is any constant, then

$$
\mathcal{L}\{e^{at}f(t)\} = F(s-a)
$$

- **Time scaling**: The Laplace transform transforms a function scaled by a factor in the time domain to a function scaled by the inverse factor in the frequency domain. That is, if f is piecewise continuous on $[0, \infty)$ and of exponential order, and a is any positive constant, then

$$
\mathcal{L}\{f(at)\} = \frac{1}{a}F\left(\frac{s}{a}\right)
$$

- **Time shifting**: The Laplace transform transforms a function shifted by a factor in the time domain to a function multiplied by an exponential factor in the frequency domain. That is, if f is piecewise continuous on $[0, \infty)$ and of exponential order, and a is any positive constant, then

$$
\mathcal{L}\{f(t-a)\} = e^{-as}F(s)
$$

- **Convolution**: The Laplace transform transforms the convolution of two functions in the time domain to the product