### Cauchy-Euler equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form:

$$a_nx^ny^{(n)} + a_{n-1}x^{n-1}y^{(n-1)} + \cdots + a_1xy' + a_0y = f(x)$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function .

- The Cauchy-Euler equation is also known as the Euler-Cauchy equation or the equidimensional equation .

- The Cauchy-Euler equation is important in the theory of linear differential equations because it has direct applications to Fourier's method in the study of partial differential equations.

- The most common Cauchy-Euler equation is the second-order equation, which appears in a number of physics and engineering applications, such as when solving Laplace's equation in polar coordinates . The second-order Cauchy-Euler equation is:

$$ax^2y'' + bxy' + cy = 0$$

where $a, b, c$ are constants .

- The solutions of the second-order Cauchy-Euler equation can be found using the characteristic equation:

$$ar(r-1) + br + c = 0$$

where $r$ is a constant to be determined .

- Just like the constant coefficient differential equation, the nature of the roots of the characteristic equation leads to three classes of solutions:

  - If the roots are distinct and real, say $r_1$ and $r_2$, then the general solution is:

  $$y = c_1x^{r_1} + c_2x^{r_2}$$

  where $c_1$ and $c_2$ are arbitrary constants .

  - If the roots are repeated and real, say $r_1 = r_2 = r$, then the general solution is:

  $$y = c_1x^r + c_2x^r\ln x$$

  where $c_1$ and $c_2$ are arbitrary constants .

  - If the roots are complex, say $r_1 = \alpha + i\beta$ and $r_2 = \alpha - i\beta$, then the general solution is:

  $$y = x^\alpha(c_1\cos \beta \ln x + c_2\sin \beta \ln x)$$

  where $c_1$ and $c_2$ are arbitrary constants .

- The method of solving the Cauchy-Euler equation can be extended to higher-order equations by assuming a trial solution of the form $y = x^r$ and finding the roots of the corresponding characteristic polynomial .

- The method of solving the Cauchy-Euler equation can also be applied to non-homogeneous equations by using the method of variation of parameters or the method of undetermined coefficients .