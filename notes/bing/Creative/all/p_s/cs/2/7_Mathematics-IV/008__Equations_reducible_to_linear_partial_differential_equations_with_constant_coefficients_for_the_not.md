### Equations reducible to linear partial differential equations with constant coefficients

- A linear partial differential equation (PDE) is an equation that involves partial derivatives of an unknown function of two or more variables, and the coefficients of the derivatives are functions or constants.
- A linear PDE has constant coefficients if only constant functions appear as coefficients in the equation.
- A linear PDE is homogeneous if the constant term is zero, otherwise it is non-homogeneous.
- A linear PDE is of order n if the highest order of partial derivatives involved is n.
- A linear PDE can be written in the form

  `L(u) = f(x,y)`

  where L is a linear differential operator, u is the unknown function, and f is a given function or zero.

- Some linear PDEs can be reduced to linear PDEs with constant coefficients by using suitable transformations of variables, such as

  - Change of independent variables: `x = x(u,v)`, `y = y(u,v)`
  - Change of dependent variable: `u = u(x,y,z)`
  - Change of both variables: `u = u(x,y,z)`, `x = x(u,v)`, `y = y(u,v)`

- The advantage of reducing a linear PDE to a linear PDE with constant coefficients is that the latter can be solved by using standard methods, such as

  - Separation of variables: `u(x,y) = X(x)Y(y)`
  - Method of characteristics: `x = x(t)`, `y = y(t)`, `u = u(t)`
  - Fourier transform: `u(x,y) = F^{-1}(U(k,l))`
  - Laplace transform: `u(x,y) = L^{-1}(U(s,t))`

- Some examples of equations reducible to linear PDEs with constant coefficients are

  - Laplace equation: `u_{xx} + u_{yy} = 0`
  - Heat equation: `u_{t} = k u_{xx}`
  - Wave equation: `u_{tt} = c^2 u_{xx}`
  - Monge-Ampère equation: `u_{xx} u_{yy} - u_{xy}^2 = f(x,y)`

- To reduce these equations to linear PDEs with constant coefficients, one can use the following transformations

  - Laplace equation: `x = r cos(theta)`, `y = r sin(theta)`, `u = u(r,theta)`
  - Heat equation: `x = x`, `t = t`, `u = v(x,t) e^{-kx^2/4t}`
  - Wave equation: `x = x`, `t = t`, `u = v(x,t) e^{-c^2t^2/4x^2}`
  - Monge-Ampère equation: `x = x`, `y = y`, `u = v(x,y) + xy`

- After applying these transformations, the resulting equations are

  - Laplace equation: `u_{rr} + (1/r) u_r + (1/r^2) u_{theta theta} = 0`
  - Heat equation: `v_t - (k/2t) v_x - (kx/t) v = 0`
  - Wave equation: `v_{tt} - (c^2/4x^2) v_{xx} - (c^2/x) v_x = 0`
  - Monge-Ampère equation: `v_{xx} v_{yy} - v_{xy}^2 = f(x,y) - 1`

- These equations are linear PDEs with constant coefficients, and can be solved by using the methods mentioned above.

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of the Laplace, heat, and wave equations, think of the acronym LHW, which sounds like "low".
- To remember the sign of the coefficients of the second-order derivatives in the heat and wave equations, think of the acronym HWP, which stands for "heat wave positive". This means that the heat equation has a positive coefficient for the second derivative in x, and the wave equation has a positive coefficient for the second derivative in t.
- To remember the transformations for the Laplace, heat, and wave equations, think of the acronym LHW, which also stands for "logarithm, hyperbolic, and wave". This means that the Laplace equation uses a logarithmic transformation (polar coordinates), the heat equation uses a hyperbolic transformation (exponential function), and the wave equation uses a wave transformation (sine or cosine function).
- To remember the Monge-Ampère equation, think of the word "mange", which means "eat" in French. This means that the equation involves the product of the second derivatives, which can be seen as "eating" the first derivatives.