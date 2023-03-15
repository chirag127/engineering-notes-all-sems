# Equations reducible to linear partial differential equations with constant coefficients

- A linear partial differential equation (PDE) with constant coefficients is an equation of the form
$$
a_1 \frac{\partial u}{\partial x_1} + a_2 \frac{\partial u}{\partial x_2} + \cdots + a_n \frac{\partial u}{\partial x_n} + b u = f(x_1, x_2, \ldots, x_n)
$$
where $a_1, a_2, \ldots, a_n, b$ are constants and $f$ is a given function.
- A linear PDE with constant coefficients is homogeneous if $f$ is identically zero, and non-homogeneous otherwise.
- A linear PDE with constant coefficients can be solved by using the method of characteristics, which involves finding a set of curves along which the equation reduces to an ordinary differential equation (ODE).
- A linear PDE with constant coefficients can also be solved by using the method of Fourier transform, which involves transforming the equation into an algebraic equation in the frequency domain and then applying the inverse transform to obtain the solution in the spatial domain.
- Some nonlinear PDEs can be reduced to linear PDEs with constant coefficients by using suitable transformations of variables. For example, the Burgers' equation
$$
\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = \nu \frac{\partial^2 u}{\partial x^2}
$$
where $\nu$ is a constant, can be transformed into the linear heat equation
$$
\frac{\partial v}{\partial t} = \nu \frac{\partial^2 v}{\partial x^2}
$$
by using the transformation $v = -2 \nu \ln u$.
- Another example of a nonlinear PDE that can be reduced to a linear PDE with constant coefficients is the Monge-Ampère equation
$$
\frac{\partial^2 u}{\partial x^2} \frac{\partial^2 u}{\partial y^2} - \left( \frac{\partial^2 u}{\partial x \partial y} \right)^2 = f(x, y)
$$
which can be transformed into the Laplace equation
$$
\frac{\partial^2 v}{\partial x^2} + \frac{\partial^2 v}{\partial y^2} = 0
$$
by using the transformation $v = \frac{\partial u}{\partial x} \frac{\partial u}{\partial y}$.
- The advantage of reducing a nonlinear PDE to a linear PDE with constant coefficients is that the latter can be solved by using well-known methods and techniques, and the solution of the original equation can be obtained by applying the inverse transformation.