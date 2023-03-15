# Laplace transform of derivatives and integrals

## Definition

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform of a function f(t) is defined as

$$
F(s) = \mathcal{L}\{f(t)\} = \int_{0}^{\infty} e^{-st} f(t) dt
$$

- where s is a complex variable and the integral is taken over the positive real axis.
- The Laplace transform is a linear operator, meaning that if f and g are functions and a and b are constants, then

$$
\mathcal{L}\{af(t) + bg(t)\} = a\mathcal{L}\{f(t)\} + b\mathcal{L}\{g(t)\}
$$

## Properties

- The Laplace transform has several properties that make it useful for solving differential and integral equations. Some of the most important ones are:

### Laplace transform of derivatives

- If f(t) is a function that has n derivatives, then the Laplace transform of the nth derivative is given by

$$
\mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - s^{n-1} f(0) - s^{n-2} f'(0) - \cdots - f^{(n-1)}(0)
$$

- This property allows us to convert differential equations in the time domain to algebraic equations in the frequency domain.

### Laplace transform of integrals

- If f(t) is a function, then the Laplace transform of its integral from 0 to t is given by

$$
\mathcal{L}\{\int_{0}^{t} f(\tau) d\tau\} = \frac{1}{s} F(s)
$$

- This property allows us to convert integral equations in the time domain to algebraic equations in the frequency domain.

### Laplace transform of exponential functions

- If f(t) is a function and a is a constant, then the Laplace transform of the function e^at f(t) is given by

$$
\mathcal{L}\{e^{at} f(t)\} = F(s-a)
$$

- This property allows us to shift the function f(t) in the frequency domain by a units.

### Laplace transform of periodic functions

- If f(t) is a periodic function with period T, then the Laplace transform of f(t) is given by

$$
\mathcal{L}\{f(t)\} = \frac{1}{1-e^{-sT}} \int_{0}^{T} e^{-st} f(t) dt
$$

- This property allows us to simplify the Laplace transform of periodic functions by using only one period of the function.

## Examples

- Here are some examples of how to use the Laplace transform of derivatives and integrals to solve equations.

### Example 1

- Find the Laplace transform of the function f(t) = t^2.

- Solution:

- Using the definition of the Laplace transform, we have

$$
\begin{aligned}
F(s) &= \mathcal{L}\{f(t)\} \\
&= \int_{0}^{\infty} e^{-st} t^2 dt \\
&= \left[ -\frac{e^{-st}}{s} t^2 \right]_{0}^{\infty} + \frac{2}{s} \int_{0}^{\infty} e^{-st} t dt \\
&= 0 + \frac{2}{s} \left[ -\frac{e^{-st}}{s} t \right]_{0}^{\infty} + \frac{2}{s^2} \int_{0}^{\infty} e^{-st} dt \\
&= 0 + 0 + \frac{2}{s^2} \left[ -\frac{e^{-st}}{s} \right]_{0}^{\infty} \\
&= 0 + 0 + \frac{2}{s^3} \left( 0 - (-1) \right) \\
&= \frac{2}{s^3}
\end{aligned}
$$

- Therefore, the Laplace transform of f(t) = t^