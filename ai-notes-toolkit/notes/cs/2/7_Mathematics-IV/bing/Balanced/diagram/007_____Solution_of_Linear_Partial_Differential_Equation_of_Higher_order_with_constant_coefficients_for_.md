Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is a summary of the solution of linear partial differential equation of higher order with constant coefficients:

### Solution of Linear Partial Differential Equation of Higher order with constant coefficients

- A linear partial differential equation of higher order with constant coefficients is of the form:

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

- The solution consists of two parts: the complementary function and the particular integral.

- The complementary function is the general solution of the homogeneous equation:

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = 0
$$

- The complementary function can be obtained by assuming a solution of the form:

$$
u = e^{rx}
$$

- Substituting this into the homogeneous equation and dividing by $e^{rx}$, we get the characteristic equation:

$$
a_0 r^n + a_1 r^{n-1} + \cdots + a_n = 0
$$

- The roots of the characteristic equation determine the form of the complementary function.

- If the roots are distinct and real, the complementary function is:

$$
u_c = c_1 e^{r_1 x} + c_2 e^{r_2 x} + \cdots + c_n e^{r_n x}
$$

- If the roots are complex, the complementary function is:

$$
u_c = c_1 e^{\alpha_1 x} \cos (\beta_1 x) + c_2 e^{\alpha_1 x} \sin (\beta_1 x) + \cdots + c_{n-1} e^{\alpha_n x} \cos (\beta_n x) + c_n e^{\alpha_n x} \sin (\beta_n x)
$$

- If the roots are repeated, the complementary function is:

$$
u_c = c_1 e^{r x} + c_2 x e^{r x} + \cdots + c_n x^{n-1} e^{r x}
$$

- The particular integral is a particular solution of the non-homogeneous equation:

$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$

- The particular integral can be obtained by using the method of undetermined coefficients, the method of variation of parameters, or the method of Laplace transform.

- The method of undetermined coefficients involves guessing a solution of the same form as the right-hand side function $f(x)$ and determining the coefficients by substituting into the equation.

- The method of variation of parameters involves multiplying the complementary function by functions of $x$ and determining the functions by substituting into the equation.

- The method of Laplace transform involves applying the Laplace transform to both sides of the equation and solving for the Laplace transform of the solution, then applying the inverse Laplace transform to obtain the solution.

- The general solution of the equation is the sum of the complementary function and the particular integral:

$$
u = u_c + u_p
$$

- The constants in the general solution can be determined by using the initial or boundary conditions.