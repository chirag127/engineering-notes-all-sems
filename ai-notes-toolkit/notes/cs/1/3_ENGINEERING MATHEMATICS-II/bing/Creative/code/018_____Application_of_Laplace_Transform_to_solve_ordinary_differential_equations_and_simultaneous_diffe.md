### Application of Laplace Transform to solve ordinary differential equations and simultaneous differential equations

- Laplace transform is a technique that converts a function of time, such as a solution of a differential equation, into a function of a complex variable, called the Laplace variable or the frequency variable.
- Laplace transform can simplify the process of solving differential equations by transforming them into algebraic equations that are easier to manipulate and solve.
- Laplace transform can also handle various types of initial and boundary conditions, as well as discontinuous and periodic functions, by using properties such as linearity, differentiation, integration, shifting, convolution, and inverse transform.
- Laplace transform can be applied to both ordinary differential equations (ODEs) and simultaneous differential equations (SDEs), which are systems of two or more ODEs that are coupled together.

#### Solving ordinary differential equations with Laplace transform

- To solve an ODE with Laplace transform, we follow these steps:

  1. Take the Laplace transform of both sides of the ODE, using the properties of the transform and the table of common transforms.
  2. Solve for the Laplace transform of the unknown function, denoted by a capital letter, by algebraic manipulation.
  3. Take the inverse Laplace transform of both sides, using the properties of the inverse transform and the table of common transforms, to obtain the solution of the original function, denoted by a lowercase letter.

- For example, consider the second-order linear ODE with constant coefficients:

  $$y'' + ay' + by = g(t)$$

  where $a$ and $b$ are constants and $g(t)$ is a given function of time.

  To solve this ODE with Laplace transform, we do the following:

  1. Taking the Laplace transform of both sides, we get:

     $$s^2Y(s) - sy(0) - y'(0) + a(sY(s) - y(0)) + bY(s) = G(s)$$

     where $Y(s)$ and $G(s)$ are the Laplace transforms of $y(t)$ and $g(t)$, respectively, and $y(0)$ and $y'(0)$ are the initial values of $y(t)$ and $y'(t)$, respectively.

  2. Solving for $Y(s)$, we get:

     $$Y(s) = \frac{G(s) + sy(0) + y'(0) - ay(0)}{s^2 + as + b}$$

  3. Taking the inverse Laplace transform of both sides, we get:

     $$y(t) = \mathcal{L}^{-1}\left\{\frac{G(s) + sy(0) + y'(0) - ay(0)}{s^2 + as + b}\right\}$$

     which can be simplified by using partial fraction decomposition and the table of common inverse transforms.

#### Solving simultaneous differential equations with Laplace transform

- To solve an SDE with Laplace transform, we follow these steps:

  1. Take the Laplace transform of each equation in the system, using the properties of the transform and the table of common transforms.
  2. Solve for the Laplace transform of each unknown function, denoted by a capital letter, by algebraic manipulation or matrix methods.
  3. Take the inverse Laplace transform of each equation, using the properties of the inverse transform and the table of common transforms, to obtain the solution of each original function, denoted by a lowercase letter.

- For example, consider the system of two first-order linear ODEs with constant coefficients:

  $$\begin{cases}
  x' + 2x - y = e^{-t} \\
  y' + x + 3y = \sin t
  \end{cases}$$

  where $x(t)$ and $y(t)$ are the unknown functions of time.

  To solve this SDE with Laplace transform, we do the following:

  1. Taking the Laplace transform of each equation, we get:

     $$\begin{cases}
     sX(s) - x(0) + 2X(s) - Y(s) = \frac{1}{s + 1} \\
     sY(s) - y(0) + X(s) + 3Y(s) = \frac{1}{s^2 + 1}
     \end{cases}$$

     where $X