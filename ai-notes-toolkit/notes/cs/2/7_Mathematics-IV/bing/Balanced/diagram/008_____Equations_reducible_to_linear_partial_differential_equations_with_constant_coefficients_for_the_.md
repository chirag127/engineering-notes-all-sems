### Equations reducible to linear partial differential equations with constant coefficients

- A linear partial differential equation (PDE) with constant coefficients is of the form
$$
a_0 u + a_1 u_x + a_2 u_y + a_3 u_{xx} + a_4 u_{xy} + a_5 u_{yy} + \cdots = f(x,y)
$$
where $a_0, a_1, \ldots$ are constants and $f(x,y)$ is a given function.
- A PDE that is not of this form may be reducible to a linear PDE with constant coefficients by a change of variables.
- One method to find such a change of variables is to use the characteristic curves of the PDE, which are the curves along which the PDE becomes an ordinary differential equation (ODE).
- The characteristic curves are obtained by solving the equation
$$
a_1 dy - a_2 dx = 0
$$
which is called the characteristic equation of the PDE.
- If the characteristic equation has two distinct real roots, say $m_1$ and $m_2$, then the characteristic curves are given by
$$
y - m_1 x = c_1 \quad \text{and} \quad y - m_2 x = c_2
$$
where $c_1$ and $c_2$ are arbitrary constants.
- The change of variables is then given by
$$
\xi = y - m_1 x \quad \text{and} \quad \eta = y - m_2 x
$$
which transforms the PDE into a linear PDE with constant coefficients in terms of $u, \xi, \eta$.
- If the characteristic equation has a repeated real root, say $m$, then the characteristic curves are given by
$$
y - m x = c_1 \quad \text{and} \quad x = c_2
$$
where $c_1$ and $c_2$ are arbitrary constants.
- The change of variables is then given by
$$
\xi = y - m x \quad \text{and} \quad \eta = x
$$
which transforms the PDE into a linear PDE with constant coefficients in terms of $u, \xi, \eta$.
- If the characteristic equation has complex conjugate roots, say $m = p \pm iq$, then the characteristic curves are given by
$$
y - p x = c_1 \cos(q x) + c_2 \sin(q x) \quad \text{and} \quad y - p x = -c_1 \sin(q x) + c_2 \cos(q x)
$$
where $c_1$ and $c_2$ are arbitrary constants.
- The change of variables is then given by
$$
\xi = y - p x \quad \text{and} \quad \eta = c_1 \cos(q x) + c_2 \sin(q x)
$$
which transforms the PDE into a linear PDE with constant coefficients in terms of $u, \xi, \eta$.
- Once the PDE is reduced to a linear PDE with constant coefficients, the method of finding the general solution depends on the order and type of the PDE.
- For first order linear PDEs, the method of integrating factors can be used.
- For second order linear PDEs, the method of separation of variables or the method of characteristics can be used.
- For higher order linear PDEs, the method of Fourier transforms or the method of Laplace transforms can be used.