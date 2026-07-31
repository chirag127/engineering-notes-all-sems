# Linear and Non Linear Partial Equations of first order

- A partial differential equation (PDE) is an equation that involves partial derivatives of an unknown function of two or more variables.
- A PDE is said to be linear if it is linear in the unknown function and its partial derivatives, that is, if it has the form
$$
a_{11}(x,y)u_{xx} + a_{12}(x,y)u_{xy} + a_{21}(x,y)u_{yx} + a_{22}(x,y)u_{yy} + b_1(x,y)u_x + b_2(x,y)u_y + c(x,y)u = f(x,y)
$$
where $a_{ij}, b_i, c, f$ are given functions of $x$ and $y$, and $u_{ij}$ denotes the second partial derivative of $u$ with respect to $x_i$ and $x_j$.
- A PDE is said to be nonlinear if it is not linear, that is, if it involves products or powers of the unknown function or its partial derivatives, or if the coefficients of the PDE are functions of the unknown function or its partial derivatives.
- Examples of linear PDEs of first order are
$$
u_x + u_y = 0
$$
$$
xu_x + yu_y = u
$$
$$
u_x + 2yu_y = e^{x+y}
$$
- Examples of nonlinear PDEs of first order are
$$
u_x + uu_y = 0
$$
$$
u_x^2 + u_y^2 = 1
$$
$$
u_x + u_yu = e^x
$$
- Linear PDEs of first order can be solved by the method of characteristics, which involves finding curves along which the PDE reduces to an ordinary differential equation (ODE).
- Nonlinear PDEs of first order can be solved by various methods, such as the method of separation of variables, the method of integrating factors, or the method of Charpit equations.