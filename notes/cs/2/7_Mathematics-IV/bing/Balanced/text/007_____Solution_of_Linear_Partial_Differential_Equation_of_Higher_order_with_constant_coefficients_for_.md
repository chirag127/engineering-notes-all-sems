### Solution of Linear Partial Differential Equation of Higher order with constant coefficients

- A linear partial differential equation of higher order with constant coefficients is of the form

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- The solution of such an equation consists of two parts: the complementary function and the particular integral.

- The complementary function is the general solution of the homogeneous equation, i.e., when $f(x) = 0$. It can be obtained by using the method of characteristic equation, which is similar to the method for ordinary differential equations.

- The characteristic equation is obtained by replacing $\frac{\partial}{\partial x}$ by a variable $r$, i.e.,

$$
a_0 r^n + a_1 r^{n-1} + \cdots + a_n = 0
$$

- The roots of the characteristic equation determine the form of the complementary function. Depending on whether the roots are real and distinct, real and repeated, or complex, the complementary function will have different terms involving exponentials, polynomials, sines and cosines.

- The particular integral is a specific solution of the non-homogeneous equation, i.e., when $f(x) \neq 0$. It can be obtained by using the method of undetermined coefficients, which is also similar to the method for ordinary differential equations.

- The method of undetermined coefficients involves guessing a form of the particular integral based on the form of $f(x)$, and then finding the coefficients by substituting the guess into the equation and equating the coefficients of like terms.

- The general solution of the equation is the sum of the complementary function and the particular integral. It can be verified by substituting it into the equation and simplifying.

- The general solution may contain arbitrary constants, which can be determined by using the boundary conditions or initial conditions given in the problem.