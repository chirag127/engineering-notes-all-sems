### Limit for the notes of the Unit 4 - Complex Variable–Differentiation in the subject of ENGINEERING MATHEMATICS-II

- Complex variable–differentiation is the study of functions of a complex variable and their derivatives.
- A complex variable is a variable that can take values in the complex numbers, which are numbers of the form $z = x + iy$, where $x$ and $y$ are real numbers and $i$ is the imaginary unit such that $i^2 = -1$.
- The complex numbers can be represented geometrically as points in the complex plane, where the horizontal axis is the real axis and the vertical axis is the imaginary axis.
- A function of a complex variable is a rule that assigns a complex number to each complex number in its domain, which is a subset of the complex plane. For example, $f(z) = z^2$ is a function of a complex variable that maps each complex number $z$ to its square $z^2$.
- The derivative of a function of a complex variable is a measure of how fast the function changes with respect to a small change in the input. The definition of the complex derivative is similar to the derivative of a real function, but with some important differences.
- The complex derivative of a function $f(z)$ at a point $z_0$ in its domain is defined as
$$f'(z_0) = \lim_{\Delta z \to 0} \frac{f(z_0 + \Delta z) - f(z_0)}{\Delta z}$$
where $\Delta z$ is a complex number that approaches zero from any direction in the complex plane.
- A function of a complex variable is said to be differentiable at a point $z_0$ if the complex derivative $f'(z_0)$ exists and is independent of the direction of $\Delta z$. A function is said to be analytic or holomorphic in a domain if it is differentiable at every point in that domain.
- A remarkable feature of complex differentiation is that the existence of one complex derivative automatically implies the existence of infinitely many. This is in contrast to the case of a function of a real variable, where the derivative can exist without the existence of higher-order derivatives.
- A consequence of complex differentiability is that a function of a complex variable must satisfy the Cauchy-Riemann equations, which are a pair of partial differential equations that relate the real and imaginary parts of the function and its derivative. The Cauchy-Riemann equations are
$$\frac{\partial u}{\partial x} = \frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y} = -\frac{\partial v}{\partial x}$$
where $f(z) = u(x,y) + iv(x,y)$ and $z = x + iy$.
- The Cauchy-Riemann equations can be used to test whether a function of a complex variable is differentiable or not. They can also be used to find the complex derivative of a function if it exists.
- Another consequence of complex differentiability is that a function of a complex variable must be infinitely differentiable and have a power series expansion around any point in its domain. A power series is an infinite sum of the form
$$f(z) = \sum_{n=0}^{\infty} a_n (z - z_0)^n$$
where $a_n$ are complex coefficients and $z_0$ is a fixed complex number. The power series converges to the function $f(z)$ in a disk centered at $z_0$ with radius equal to the distance to the nearest point where $f(z)$ is not analytic.
- The power series expansion of a function of a complex variable can be used to approximate the function near a given point, to compute the values of the function and its derivatives, and to study the properties and behavior of the function. The power series can also be used to define new functions of a complex variable, such as the exponential, trigonometric, and logarithmic functions.
- The main tools for complex differentiation are the same as for real differentiation, such as the product, quotient, and chain rules. However, there are some differences and subtleties that arise from the complex nature of the variables and functions. For example, the complex derivative is linear, but not commutative, meaning that $f'(z) + g'(z) = (f + g)'(z)$, but $f'(z) g'(z) \