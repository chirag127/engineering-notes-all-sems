# Application of Laplace Transform to solve ordinary differential equations and simultaneous differential equations

- Laplace transform is a technique that converts a function of time, such as a solution of a differential equation, into a function of a complex variable, called the Laplace variable or the frequency variable.
- Laplace transform can simplify the process of solving differential equations by transforming them into algebraic equations that are easier to manipulate and solve.
- Laplace transform can also handle various types of initial and boundary conditions, as well as discontinuous and periodic functions, by using properties such as linearity, differentiation, integration, shifting, convolution, and inverse transform.
- Laplace transform can be applied to both ordinary differential equations (ODEs) and simultaneous differential equations (SDEs) with constant or variable coefficients.

## Solving ODEs with Laplace transform

- To solve an ODE with Laplace transform, we follow these steps:

  1. Take the Laplace transform of both sides of the ODE, using the properties of the transform and the initial conditions (if any).
  2. Solve for the Laplace transform of the unknown function, denoted by a capital letter, by algebraic manipulation.
  3. Take the inverse Laplace transform of the result, using the tables of common transforms and the properties of the inverse transform.
  4. Check the solution by substituting it into the original ODE.

- For example, consider the second order linear ODE with constant coefficients:

  $$y'' + ay' + by = g(t), \quad y(0) = y_0, \quad y'(0) = y_1$$

  Taking the Laplace transform of both sides, we get:

  $$s^2Y(s) - sy(0) - y'(0) + a(sY(s) - y(0)) + bY(s) = G(s)$$

  where $Y(s)$ and $G(s)$ are the Laplace transforms of $y(t)$ and $g(t)$, respectively.

  Solving for $Y(s)$, we get:

  $$Y(s) = \frac{G(s) + (as + b)y_0 + (s + a)y_1}{s^2 + as + b}$$

  Taking the inverse Laplace transform of both sides, we get:

  $$y(t) = \mathcal{L}^{-1}\left\{\frac{G(s) + (as + b)y_0 + (s + a)y_1}{s^2 + as + b}\right\}$$

  which can be simplified by using the tables of common transforms and the properties of the inverse transform.

  For example, if $g(t) = e^{-t}$, then $G(s) = \frac{1}{s + 1}$, and we get:

  $$y(t) = \mathcal{L}^{-1}\left\{\frac{\frac{1}{s + 1} + (as + b)y_0 + (s + a)y_1}{s^2 + as + b}\right\}$$

  $$y(t) = \mathcal{L}^{-1}\left\{\frac{1}{(s + 1)(s^2 + as + b)} + \frac{(as + b)y_0 + (s + a)y_1}{s^2 + as + b}\right\}$$

  $$y(t) = \mathcal{L}^{-1}\left\{\frac{A}{s + 1} + \frac{B}{s + r_1} + \frac{C}{s + r_2}\right\}$$

  where $A$, $B$, and $C$ are constants determined by partial fraction decomposition, and $r_1$ and $r_2$ are the roots of the characteristic equation $s^2 + as + b = 0$.

  Using the tables of common transforms, we get:

  $$y(t) = Ae^{-t} + Be^{r_1t} + Ce^{r_2t}$$

  which is the general solution of the ODE.

  We can check the solution by substituting it into the original ODE and verifying that it satisfies the initial conditions.

## Solving SDEs with Laplace transform

- To solve an SDE with Laplace transform, we follow these steps:

  1. Take the Laplace transform of each equation in the system