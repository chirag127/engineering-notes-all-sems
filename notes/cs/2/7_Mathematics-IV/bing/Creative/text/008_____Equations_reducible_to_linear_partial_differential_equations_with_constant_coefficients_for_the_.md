### Equations reducible to linear partial differential equations with constant coefficients

- A linear partial differential equation (PDE) with constant coefficients is an equation of the form
$$
a_0 \frac{\partial^n u}{\partial x^n} + a_1 \frac{\partial^{n-1} u}{\partial x^{n-1}} + \cdots + a_n u = f(x)
$$
where $a_0, a_1, \ldots, a_n$ are constants and $f(x)$ is a given function.

- A linear PDE with constant coefficients can be solved by finding a particular solution and a general solution of the homogeneous equation (the equation with $f(x) = 0$).

- A particular solution can be found by using the method of undetermined coefficients, which involves guessing a solution of the same form as $f(x)$ and then finding the coefficients by substituting into the equation.

- A general solution of the homogeneous equation can be found by using the method of characteristic equations, which involves finding the roots of the polynomial
$$
a_0 m^n + a_1 m^{n-1} + \cdots + a_n = 0
$$
and then forming linear combinations of the functions $e^{mx}$.

- Some equations that are not linear PDEs with constant coefficients can be reduced to such equations by using suitable transformations of variables. For example, the equation
$$
\frac{\partial^2 u}{\partial x \partial y} = 0
$$
can be transformed into
$$
\frac{\partial^2 v}{\partial z^2} = 0
$$
by using the change of variables $z = x + y$ and $v = u(x, y)$. This equation can then be solved by the method of characteristic equations.

- Another example of an equation that can be reduced to a linear PDE with constant coefficients is the Lagrange equation
$$
P(x, y) \frac{\partial u}{\partial x} + Q(x, y) \frac{\partial u}{\partial y} = R(x, y)
$$
where $P, Q, R$ are given functions. This equation can be transformed into
$$
\frac{\partial v}{\partial z} = S(z, w)
$$
by using the change of variables $z = \phi(x, y)$ and $w = \psi(x, y)$, where $\phi$ and $\psi$ are solutions of the system
$$
\frac{d\phi}{dx} = P(x, y), \quad \frac{d\phi}{dy} = Q(x, y), \quad \frac{d\psi}{dx} = -Q(x, y), \quad \frac{d\psi}{dy} = P(x, y)
$$
and $S(z, w) = R(x, y) \sqrt{P^2(x, y) + Q^2(x, y)}$. This equation can then be solved by the method of integration.