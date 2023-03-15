### Laplace transform

- The Laplace transform is a technique that converts a function of time, $f(t)$, into a function of a complex variable, $F(s)$, where $s = \sigma + j\omega$ is the complex frequency.
- The Laplace transform is defined as
$$
F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) \, dt
$$
- The inverse Laplace transform is the process of finding $f(t)$ from $F(s)$, and is denoted by
$$
f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} e^{st} F(s) \, ds
$$
- The Laplace transform has many properties that make it useful for solving differential equations, such as linearity, scaling, shifting, differentiation, integration, convolution, and initial and final value theorems.
- Some common Laplace transforms of elementary functions are:

| $f(t)$ | $F(s)$ |
|:------:|:------:|
| $1$ | $\frac{1}{s}$ |
| $e^{at}$ | $\frac{1}{s-a}$ |
| $t^n$ | $\frac{n!}{s^{n+1}}$ |
| $\sin(at)$ | $\frac{a}{s^2 + a^2}$ |
| $\cos(at)$ | $\frac{s}{s^2 + a^2}$ |
| $\delta(t)$ | $1$ |