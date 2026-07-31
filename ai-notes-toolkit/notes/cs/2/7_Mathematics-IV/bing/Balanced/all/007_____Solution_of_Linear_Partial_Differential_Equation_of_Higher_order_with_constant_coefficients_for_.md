# Solution of Linear Partial Differential Equation of Higher order with constant coefficients

- A linear partial differential equation of higher order with constant coefficients is of the form:

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The general solution of such an equation consists of two parts: the complementary function and the particular integral.

- The complementary function is the general solution of the homogeneous equation, i.e., when $f(x) = 0$. It can be obtained by using the method of characteristic equation, which is similar to the method for ordinary differential equations.

- The characteristic equation is obtained by replacing $\frac{\partial u}{\partial x}$ by $r$ in the homogeneous equation, i.e.,

$$
a_0 r^n + a_1 r^{n-1} + \cdots + a_n = 0
$$

- The roots of the characteristic equation determine the form of the complementary function. There are three possible cases:

  - Case 1: All the roots are distinct and real. In this case, the complementary function is

  $$
  u_c(x) = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}
  $$

  where $r_1, r_2, \ldots, r_n$ are the roots and $c_1, c_2, \ldots, c_n$ are arbitrary constants.

  - Case 2: Some of the roots are repeated. In this case, the complementary function is

  $$
  u_c(x) = \sum_{i=1}^k \left( c_{i1} e^{r_i x} + c_{i2} x e^{r_i x} + \cdots + c_{im_i} x^{m_i - 1} e^{r_i x} \right)
  $$

  where $r_1, r_2, \ldots, r_k$ are the distinct roots, $m_1, m_2, \ldots, m_k$ are their multiplicities, and $c_{ij}$ are arbitrary constants.

  - Case 3: Some of the roots are complex. In this case, the complementary function is

  $$
  u_c(x) = \sum_{i=1}^k \left( c_{i1} e^{\alpha_i x} \cos \beta_i x + c_{i2} e^{\alpha_i x} \sin \beta_i x \right)
  $$

  where $\alpha_i \pm i \beta_i$ are the complex roots, and $c_{i1}, c_{i2}$ are arbitrary constants.

- The particular integral is a particular solution of the non-homogeneous equation, i.e., when $f(x) \neq 0$. It can be obtained by using the method of undetermined coefficients, which is also similar to the method for ordinary differential equations.

- The method of undetermined coefficients consists of guessing the form of the particular integral based on the form of $f(x)$, and then finding the unknown coefficients by substituting the guess into the non-homogeneous equation and equating the coefficients of the same terms.

- The general form of the particular integral depends on the type of $f(x)$. There are four common types:

  - Type 1: $f(x) = P(x)$, where $P(x)$ is a polynomial of degree $m$. In this case, the particular integral is

  $$
  u_p(x) = A_0 + A_1 x + \cdots + A_m x^m
  $$

  where $A_0, A_1, \ldots, A_m$ are unknown constants.

  - Type 2: $f(x) = e^{kx} P(x)$, where $k$ is a constant and $P(x)$ is a polynomial of degree $m$. In this case, the particular integral is

  $$
  u_p(x) = e^{kx} (A_0 + A_1 x + \cdots + A