### Solution of Linear Partial Differential Equation of Higher order with constant coefficients

- A linear partial differential equation of higher order with constant coefficients is of the form:

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The solution of such an equation consists of two parts: the complementary function and the particular integral.

- The complementary function is the general solution of the homogeneous equation, i.e., when $f(x) = 0$. It can be obtained by using the method of characteristic equation, which is similar to the method for ordinary differential equations.

- The characteristic equation is obtained by replacing $\frac{\partial u}{\partial x}$ by $r$, where $r$ is a constant. Then, the characteristic equation is:

$$
a_0 r^n + a_1 r^{n-1} + \cdots + a_n = 0
$$

- The roots of the characteristic equation determine the form of the complementary function. There are three cases to consider:

  - If the roots are distinct and real, then the complementary function is:

  $$
  u_c(x) = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}
  $$

  where $c_1, c_2, \ldots, c_n$ are arbitrary constants and $r_1, r_2, \ldots, r_n$ are the roots of the characteristic equation.

  - If the roots are repeated and real, then the complementary function is:

  $$
  u_c(x) = (c_1 + c_2 x + \cdots + c_k x^{k-1}) e^{r x}
  $$

  where $c_1, c_2, \ldots, c_k$ are arbitrary constants, $r$ is the repeated root of the characteristic equation, and $k$ is the multiplicity of the root.

  - If the roots are complex, then the complementary function is:

  $$
  u_c(x) = e^{\alpha x} (c_1 \cos \beta x + c_2 \sin \beta x) + e^{\gamma x} (c_3 \cos \delta x + c_4 \sin \delta x) + \cdots
  $$

  where $c_1, c_2, \ldots, c_n$ are arbitrary constants and $\alpha + i \beta, \gamma + i \delta, \ldots$ are the complex roots of the characteristic equation.

- The particular integral is a particular solution of the non-homogeneous equation, i.e., when $f(x) \neq 0$. It can be obtained by using the method of undetermined coefficients, which is also similar to the method for ordinary differential equations.

- The method of undetermined coefficients consists of guessing the form of the particular integral based on the form of $f(x)$, and then finding the coefficients by substituting the guess into the equation and equating the coefficients of the same terms.

- The general rule for guessing the form of the particular integral is:

  - If $f(x)$ is a polynomial of degree $m$, then the particular integral is also a polynomial of degree $m$.

  - If $f(x)$ is an exponential function of the form $A e^{B x}$, then the particular integral is also an exponential function of the same form, unless $B$ is a root of the characteristic equation, in which case the particular integral is multiplied by a factor of $x$.

  - If $f(x)$ is a trigonometric function of the form $A \cos B x + C \sin B x$, then the particular integral is also a trigonometric function of the same form, unless $B$ is a root of the characteristic equation, in which case the particular integral is multiplied by a factor of $x$.

  - If $f(x)$ is a product or sum of the above functions, then the particular integral is also a product or sum of the corresponding functions.

- The general solution of the equation is the sum of the complementary function and the particular integral, i