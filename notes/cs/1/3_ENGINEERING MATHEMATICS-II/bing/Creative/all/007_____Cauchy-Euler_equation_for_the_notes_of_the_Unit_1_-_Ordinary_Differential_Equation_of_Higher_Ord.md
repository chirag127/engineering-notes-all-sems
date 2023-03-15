# Cauchy-Euler equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form :

$$a_nx^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = 0$$

where $a_n, a_{n-1}, \ldots, a_0$ are constants and $x > 0$.

- The Cauchy-Euler equation is also known as the Euler-Cauchy equation or the equidimensional equation .

- The Cauchy-Euler equation is important in the theory of linear differential equations because it has direct applications to Fourier's method in the study of partial differential equations. In particular, the second order Cauchy-Euler equation

$$ax^2y'' + bxy' + cy = 0$$

accounts for almost all such applications in applied literature.

- The solutions of Cauchy-Euler equations can be found using the characteristic equation :

$$a_nr(r-1) + a_{n-1}r + \cdots + a_1 + a_0 = 0$$

- Just like the constant coefficient differential equation, we have a polynomial equation and the nature of the roots again leads to three classes of solutions:

  - If the characteristic equation has distinct real roots $r_1, r_2, \ldots, r_n$, then the general solution is

  $$y = c_1x^{r_1} + c_2x^{r_2} + \cdots + c_nx^{r_n}$$

  where $c_1, c_2, \ldots, c_n$ are arbitrary constants.

  - If the characteristic equation has repeated real roots $r_1 = r_2 = \cdots = r_k$, then the general solution is

  $$y = (c_1 + c_2\ln x + \cdots + c_k\ln^{k-1} x)x^{r_1} + \cdots + c_nx^{r_n}$$

  where $c_1, c_2, \ldots, c_n$ are arbitrary constants and $r_{k+1}, \ldots, r_n$ are the distinct real roots.

  - If the characteristic equation has complex roots $r = \alpha \pm i\beta$, then the general solution is

  $$y = x^\alpha(c_1\cos \beta \ln x + c_2\sin \beta \ln x) + \cdots + c_nx^{r_n}$$

  where $c_1, c_2, \ldots, c_n$ are arbitrary constants and $r_1, \ldots, r_n$ are the real roots.

- The method of solving the Cauchy-Euler equation can be summarized as follows:

  - Step 1: Assume that $y = x^r$ is a solution of the given equation, where $r$ is a constant to be determined.

  - Step 2: Differentiate $y$ with respect to $x$ as many times as the order of the equation.

  - Step 3: Substitute $y, y', y'', \ldots$ into the equation and simplify.

  - Step 4: Solve the resulting polynomial equation for $r$, which is the characteristic equation.

  - Step 5: Find the general solution based on the nature of the roots of the characteristic equation.

  - Step 6: Apply the initial or boundary conditions, if any, to find the particular solution.