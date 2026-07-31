## Unit 2 - Laplace Transform

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform can be used to solve linear differential equations, analyze systems and signals, and study stability and control problems.
- The Laplace transform of a function f(t) is denoted by F(s) and defined by the following formula:

$$
F(s) = \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
$$

- where s is a complex variable of the form s = σ + jω, and e^{-st} is the kernel of the transform.
- The inverse Laplace transform of a function F(s) is denoted by f(t) and defined by the following formula:

$$
f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} e^{st} F(s) ds
$$

- where σ is a real constant such that F(s) is analytic in the region Re(s) > σ, and the integral is taken along a vertical line in the complex plane.
- The Laplace transform has many important properties, such as linearity, scaling, shifting, differentiation, integration, convolution, and initial and final value theorems. These properties can be used to simplify the calculation of Laplace transforms and inverse Laplace transforms, and to manipulate functions in the s-domain.
- Some common Laplace transforms and inverse Laplace transforms are given in the following table:

| f(t) | F(s) | Remarks |
| --- | --- | --- |
| 1 | $\frac{1}{s}$ | s > 0 |
| $e^{at}$ | $\frac{1}{s-a}$ | s > a |
| $t^n$ | $\frac{n!}{s^{n+1}}$ | s > 0, n = 0, 1, 2, ... |
| $\sin(at)$ | $\frac{a}{s^2 + a^2}$ | s > 0 |
| $\cos(at)$ | $\frac{s}{s^2 + a^2}$ | s > 0 |
| $\delta(t)$ | 1 | Dirac delta function |
| $u(t)$ | $\frac{1}{s}$ | Unit step function |
| $u(t-a)$ | $\frac{e^{-as}}{s}$ | Unit step function shifted by a |
| $f(t-a)u(t-a)$ | $e^{-as}F(s)$ | Time shifting property |
| $e^{at}f(t)$ | $F(s-a)$ | Frequency shifting property |
| $f'(t)$ | $sF(s) - f(0)$ | Differentiation property |
| $\int_{0}^{t} f(\tau) d\tau$ | $\frac{F(s)}{s}$ | Integration property |
| $f(t) * g(t)$ | $F(s)G(s)$ | Convolution property |
| $\lim_{t \to 0^+} f(t)$ | $\lim_{s \to \infty} sF(s)$ | Initial value theorem |
| $\lim_{t \to \infty} f(t)$ | $\lim_{s \to 0} sF(s)$ | Final value theorem |