### Solution of Linear Partial Differential Equation of Higher order with constant coefficients

- A linear partial differential equation (PDE) of higher order with constant coefficients is of the form

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The general solution of such a PDE consists of two parts: the complementary function and the particular integral.

- The complementary function is the general solution of the homogeneous equation, i.e., when $f(x) = 0$. It can be obtained by finding the roots of the characteristic polynomial

$$
a_0 r^n + a_1 r^{n-1} + \cdots + a_n = 0
$$

and using the method of undetermined coefficients.

- The particular integral is a particular solution of the non-homogeneous equation, i.e., when $f(x) \neq 0$. It can be obtained by using the method of variation of parameters, which involves finding the Wronskian of the complementary function and solving a system of linear equations.

- The general solution of the PDE is then the sum of the complementary function and the particular integral.