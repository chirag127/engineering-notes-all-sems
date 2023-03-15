### Laplace transform

- The Laplace transform is an integral transform that converts a function of a real variable (usually time) to a function of a complex variable (usually frequency).
- The Laplace transform can be used to solve linear differential equations, analyze systems and signals, and study stability and control problems.
- The Laplace transform of a function f(t) is denoted by F(s) and defined by the following formula:

  F(s) = L{f(t)} = ∫∞0 f(t) e^(-st) dt

  where s is a complex variable of the form s = σ + jω, and e^(-st) is the kernel of the transform.

- The inverse Laplace transform of a function F(s) is denoted by f(t) and defined by the following formula:

  f(t) = L^(-1){F(s)} = (1/2πj) ∫c-j∞c+j∞ F(s) e^(st) ds

  where c is a real constant such that F(s) is analytic for Re(s) > c, and the integral is taken along a vertical line in the complex plane.

- The Laplace transform has many important properties, such as linearity, scaling, shifting, differentiation, integration, convolution, and initial and final value theorems. These properties can be used to simplify the calculation of Laplace transforms and inverse Laplace transforms, and to manipulate functions in the s-domain.

- Some common Laplace transforms and inverse Laplace transforms are given in the following table:

  | f(t) | F(s) | Remarks |
  | --- | --- | --- |
  | 1 | 1/s | s > 0 |
  | t^n | n! / s^(n+1) | s > 0, n = 0, 1, 2, ... |
  | e^(at) | 1 / (s-a) | s > a |
  | sin(at) | a / (s^2 + a^2) | s > 0 |
  | cos(at) | s / (s^2 + a^2) | s > 0 |
  | e^(at) sin(bt) | b / ((s-a)^2 + b^2) | s > a |
  | e^(at) cos(bt) | (s-a) / ((s-a)^2 + b^2) | s > a |
  | δ(t) | 1 | impulse function |
  | u(t) | 1/s | unit step function |
  | u(t-a) | e^(-as) / s | delayed unit step function |
  | f(t-a) u(t-a) | e^(-as) F(s) | time shifting |
  | e^(at) f(t) | F(s-a) | frequency shifting |
  | f'(t) | s F(s) - f(0) | differentiation |
  | ∫f(t) dt | F(s) / s | integration |
  | f(t) * g(t) | F(s) G(s) | convolution |