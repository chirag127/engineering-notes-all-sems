## Unit 2 - Laplace Transform

- The Laplace transform is a mathematical technique that converts a function of time, f(t), into a function of a complex variable, F(s), where s is the Laplace variable.
- The Laplace transform is useful for solving linear differential equations, analyzing linear systems, and studying the frequency response of circuits and signals.
- The Laplace transform is defined as:

```math
F(s) = \int_{0}^{\infty} f(t) e^{-st} dt
```

- The inverse Laplace transform is defined as:

```math
f(t) = \frac{1}{2\pi i} \int_{\gamma - i\infty}^{\gamma + i\infty} F(s) e^{st} ds
```

- The Laplace transform has some important properties, such as:

  - Linearity: If f(t) and g(t) are two functions with Laplace transforms F(s) and G(s), then for any constants a and b, the Laplace transform of a f(t) + b g(t) is a F(s) + b G(s).
  - Time shifting: If f(t) has Laplace transform F(s), then the Laplace transform of f(t - a) is e^{-as} F(s), where a is a positive constant.
  - Frequency shifting: If f(t) has Laplace transform F(s), then the Laplace transform of e^{at} f(t) is F(s - a), where a is any constant.
  - Scaling: If f(t) has Laplace transform F(s), then the Laplace transform of f(at) is \frac{1}{a} F(\frac{s}{a}), where a is a nonzero constant.
  - Differentiation: If f(t) has Laplace transform F(s), then the Laplace transform of f'(t) is s F(s) - f(0), where f'(t) is the derivative of f(t) with respect to t.
  - Integration: If f(t) has Laplace transform F(s), then the Laplace transform of \int_{0}^{t} f(\tau) d\tau is \frac{1}{s} F(s), where \int_{0}^{t} f(\tau) d\tau is the integral of f(t) from 0 to t.
  - Convolution: If f(t) and g(t) are two functions with Laplace transforms F(s) and G(s), then the Laplace transform of f(t) * g(t) is F(s) G(s), where f(t) * g(t) is the convolution of f(t) and g(t) defined as:

```math
f(t) * g(t) = \int_{0}^{t} f(\tau) g(t - \tau) d\tau
```

- The Laplace transform can be used to solve linear differential equations with constant coefficients, such as:

```math
a_n y^{(n)} + a_{n-1} y^{(n-1)} + ... + a_1 y' + a_0 y = f(t)
```

- The steps are:

  - Take the Laplace transform of both sides of the equation, using the properties of the Laplace transform.
  - Solve for the Laplace transform of the unknown function, Y(s), in terms of F(s) and the initial conditions of y(t) and its derivatives.
  - Take the inverse Laplace transform of Y(s) to obtain y(t), using the methods of partial fraction decomposition, completing the square, or using a table of Laplace transforms and inverse Laplace transforms.