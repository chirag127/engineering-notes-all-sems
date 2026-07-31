### Cauchy-Euler equation

- A Cauchy-Euler equation is a linear homogeneous ordinary differential equation with variable coefficients of the form :

$$
a_n x^n y^{(n)} + a_{n-1} x^{n-1} y^{(n-1)} + \cdots + a_1 x y' + a_0 y = f(x)
$$

where $a_n, a_{n-1}, \ldots, a_0$ are constants and $f(x)$ is a given function.

- The most common Cauchy-Euler equation is the second-order equation, which appears in many physics and engineering applications, such as when solving Laplace's equation in polar coordinates . The second-order Cauchy-Euler equation is:

$$
a x^2 y'' + b x y' + c y = f(x)
$$

- The solutions of Cauchy-Euler equations can be found using the characteristic equation :

$$
a r (r-1) + b r + c = 0
$$

- Just like the constant coefficient differential equation, we have a quadratic equation and the nature of the roots again leads to three classes of solutions:

  - If the roots are distinct and real, say $r_1$ and $r_2$, then the general solution is:

  $$
  y(x) = C_1 x^{r_1} + C_2 x^{r_2}
  $$

  - If the roots are repeated and real, say $r$, then the general solution is:

  $$
  y(x) = C_1 x^r + C_2 x^r \ln x
  $$

  - If the roots are complex, say $r = \alpha \pm i \beta$, then the general solution is:

  $$
  y(x) = x^\alpha (C_1 \cos \beta \ln x + C_2 \sin \beta \ln x)
  $$

- The constants $C_1$ and $C_2$ can be determined by using the initial or boundary conditions, if given.

- If the equation is non-homogeneous, i.e., $f(x) \neq 0$, then we can use the method of variation of parameters or the method of undetermined coefficients to find a particular solution, and then add it to the general solution of the homogeneous equation to get the complete solution .

: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Euler_equation
: https://www.cfm.brown.edu/people/dobrush/am33/Mathematica/ch4/CEuler.html
: https://www.math.utah.edu/~gustafso/s2014/3150/slides/cauchy-euler-de.pdf
: https://math.libretexts.org/Bookshelves/Differential_Equations/A_First_Course_in_Differential_Equations_for_Scientists_and_Engineers_(Herman)/02%3A_Second_Order_ODEs/2.05%3A_Cauchy-Euler_Equations
: https://byjus.com/maths/cauchy-euler-equation/