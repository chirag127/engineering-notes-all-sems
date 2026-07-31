
### Solution of Linear Partial Differential Equation of Higher Order with Constant Coefficients

1. A linear partial differential equation (PDE) of higher order with constant coefficients can be written in the form: 
$$a_n \frac{\partial^n y}{\partial x^n} + a_{n-1} \frac{\partial^{n-1} y}{\partial x^{n-1}} + \cdots + a_1 \frac{\partial y}{\partial x} + a_0 y = g(x)$$

2. The general solution of the PDE can be written as: $$y(x) = \sum_{i=1}^{n} c_i \phi_i(x) + \int_a^x \frac{g(t)}{\prod_{i=1}^n (t-x_i)}\,dt$$
where $\phi_i(x)$ is the $i$th linearly independent solution of the homogeneous equation $a_n \frac{\partial^n y}{\partial x^n} + a_{n-1} \frac{\partial^{n-1} y}{\partial x^{n-1}} + \cdots + a_1 \frac{\partial y}{\partial x} + a_0 y = 0$ and $x_i$ are the roots of the characteristic equation $a_n \lambda^n + a_{n-1} \lambda^{n-1} + \cdots + a_1 \lambda + a_0 = 0$.

3. To find the particular solution of the PDE, we can use the method of undetermined coefficients. This method involves finding a particular solution of the form $y(x) = \sum_{i=1}^n b_i \phi_i(x)$, where $b_i$ are constants to be determined. 

4. The constants $b_i$ can be found by substituting the particular solution into the PDE and solving for the constants. 

5. Once the constants $b_i$ have been determined, the particular solution of the PDE is given by $y(x) = \sum_{i=1}^n b_i \phi_i(x)$.