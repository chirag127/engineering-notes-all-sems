### Method to find Analytic functions

- A function of a complex variable is said to be **analytic** if it has a complex derivative at each point of its domain and is single valued.
- A complex function can be written as f(z) = u(x,y) + iv(x,y), where z = x + iy is the complex variable, u and v are real functions of x and y, and i is the imaginary unit.
- A necessary condition for a complex function to be analytic is the **Cauchy-Riemann equations**, which state that the partial derivatives of u and v must satisfy:

  - u_x = v_y and u_y = -v_x

- A sufficient condition for a complex function to be analytic is that it satisfies the Cauchy-Riemann equations and that its partial derivatives are continuous in its domain.
- To find analytic functions, one can use the following methods:

  - **Harmonic conjugate method**: If u(x,y) is a harmonic function, i.e., it satisfies the Laplace equation u_xx + u_yy = 0, then there exists a harmonic function v(x,y) such that f(z) = u(x,y) + iv(x,y) is analytic. The function v(x,y) is called the harmonic conjugate of u(x,y) and can be found by integrating the Cauchy-Riemann equations.

  - **Power series method**: If f(z) can be expressed as a power series of the form f(z) = a_0 + a_1 z + a_2 z^2 + ... in a disk centered at z_0, then f(z) is analytic in that disk and the coefficients a_n can be found by the formula a_n = f^(n)(z_0) / n!, where f^(n) denotes the n-th derivative of f.

  - **Conformal mapping method**: If f(z) is an analytic function that maps a domain D onto another domain D', then f(z) is called a conformal mapping. Conformal mappings preserve angles and shapes locally, and can be used to transform complex problems into simpler ones. For example, the function f(z) = e^z maps the complex plane onto the upper half-plane, and the function f(z) = z^2 maps the upper half-plane onto the whole plane except the negative real axis.