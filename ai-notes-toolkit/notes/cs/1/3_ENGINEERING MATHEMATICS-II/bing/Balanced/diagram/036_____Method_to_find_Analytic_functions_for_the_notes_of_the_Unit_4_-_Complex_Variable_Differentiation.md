### Method to find Analytic functions for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- A function of a complex variable is called **analytic** if it has a complex derivative at every point in its domain.
- A complex derivative of a function f(z) is defined as the limit of the difference quotient:

$$f'(z) = \lim_{\Delta z \to 0} \frac{f(z + \Delta z) - f(z)}{\Delta z}$$

- A function f(z) is analytic if and only if it satisfies the **Cauchy-Riemann equations** :

$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y} \quad \text{and} \quad \frac{\partial u}{\partial y} = - \frac{\partial v}{\partial x}$$

where $f(z) = u(x,y) + i v(x,y)$ and $z = x + i y$.

- A function f(z) is analytic if and only if it is **holomorphic**, which means that it is complex differentiable in an open set.
- A function f(z) is analytic if and only if it is **complex analytic**, which means that it can be locally represented by a convergent power series:

$$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$

where $a_n$ are complex coefficients and $z_0$ is a point in the domain of f(z).

- To find analytic functions, one can use the following methods :

  - **Harmonic conjugate method**: If u(x,y) is a harmonic function, which means that it satisfies the Laplace equation:

  $$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0$$

  then there exists a harmonic function v(x,y) such that f(z) = u(x,y) + i v(x,y) is analytic. The function v(x,y) is called the harmonic conjugate of u(x,y) and can be found by integrating the Cauchy-Riemann equations.

  - **Integration method**: If f(z) is a function of a complex variable that can be written as an integral of another function g(z), then f(z) is analytic if g(z) is analytic and the integral is well-defined. For example, the exponential function can be written as:

  $$e^z = \int_0^z e^w dw$$

  and is analytic since e^w is analytic and the integral is independent of the path of integration.

  - **Power series method**: If f(z) is a function of a complex variable that can be expressed as a power series, then f(z) is analytic if the power series converges in a disk around the center of the series. For example, the cosine function can be written as:

  $$\cos z = \sum_{n=0}^{\infty} \frac{(-1)^n z^{2n}}{(2n)!}$$

  and is analytic since the power series converges for all z.