### Cauchy-Euler equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form :

$$
a_nx^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = f(x)
$$

where $a_n, a_{n-1}, \ldots, a_0$ are constants and $f(x)$ is a given function.

- The Cauchy-Euler equation is also known as the Euler-Cauchy equation, or simply Euler's equation . It is sometimes referred to as an equidimensional equation because the degree of $x$ is equal to the order of the derivative in each term.

- The Cauchy-Euler equation is important in the theory of linear differential equations because it has direct applications to Fourier's method in the study of partial differential equations. In particular, the second order Cauchy-Euler equation

$$
ax^2y'' + bxy' + cy = 0
$$

accounts for almost all such applications in applied literature. It also appears in a number of physics and engineering problems, such as when solving Laplace's equation in polar coordinates.

- The solutions of Cauchy-Euler equations can be found using the characteristic equation :

$$
a_nr(r-1) + a_{n-1}r + \cdots + a_1 + a_0 = 0
$$

Just like the constant coefficient differential equation, we have a polynomial equation and the nature of the roots again leads to three classes of solutions:

  - If the characteristic equation has distinct real roots $r_1, r_2, \ldots, r_n$, then the general solution is

  $$
  y = c_1x^{r_1} + c_2x^{r_2} + \cdots + c_nx^{r_n}
  $$

  where $c_1, c_2, \ldots, c_n$ are arbitrary constants.

  - If the characteristic equation has repeated real roots $r_1 = r_2 = \cdots = r_k$, then the general solution is

  $$
  y = (c_1 + c_2\ln x + \cdots + c_k\ln^{k-1} x)x^{r_1}
  $$

  where $c_1, c_2, \ldots, c_k$ are arbitrary constants.

  - If the characteristic equation has complex roots $r = \alpha \pm i\beta$, then the general solution is

  $$
  y = x^\alpha(c_1\cos \beta \ln x + c_2\sin \beta \ln x)
  $$

  where $c_1, c_2$ are arbitrary constants.

- If the Cauchy-Euler equation is non-homogeneous, i.e., $f(x) \neq 0$, then the general solution is the sum of the complementary solution (the solution of the homogeneous equation) and a particular solution (a solution that satisfies the non-homogeneous equation). The method of variation of parameters can be used to find the particular solution.