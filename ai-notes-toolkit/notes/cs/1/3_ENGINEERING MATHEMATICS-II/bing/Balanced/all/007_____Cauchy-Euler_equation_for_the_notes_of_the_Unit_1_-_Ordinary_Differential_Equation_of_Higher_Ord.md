# Cauchy-Euler Equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form :

$$a_nx^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = f(x)$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The most common Cauchy-Euler equation is the second-order equation, which appears in many physics and engineering applications, such as when solving Laplace's equation in polar coordinates . The second-order Cauchy-Euler equation is:

$$ax^2y'' + bxy' + cy = f(x)$$

- The solutions of Cauchy-Euler equations can be found using the characteristic equation :

$$ar(r-1) + br + c = 0$$

- Just like the constant coefficient differential equation, we have a quadratic equation and the nature of the roots again leads to three classes of solutions:

  - If the roots are distinct and real, say $r_1$ and $r_2$, then the general solution is:

  $$y(x) = c_1x^{r_1} + c_2x^{r_2}$$

  - If the roots are repeated, say $r_1 = r_2 = r$, then the general solution is:

  $$y(x) = c_1x^r + c_2x^r\ln x$$

  - If the roots are complex, say $r_1 = \alpha + i\beta$ and $r_2 = \alpha - i\beta$, then the general solution is:

  $$y(x) = x^\alpha(c_1\cos(\beta\ln x) + c_2\sin(\beta\ln x))$$

- The constants $c_1$ and $c_2$ can be determined by the initial or boundary conditions of the problem.

- If the given function $f(x)$ is not zero, then the equation is non-homogeneous and we need to find a particular solution using methods such as undetermined coefficients or variation of parameters. The general solution is then the sum of the complementary solution (the solution of the homogeneous equation) and the particular solution.