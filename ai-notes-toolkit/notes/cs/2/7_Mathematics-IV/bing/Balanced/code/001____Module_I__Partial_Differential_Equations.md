## Module I: Partial Differential Equations

Partial differential equations (PDEs) are equations that involve a function of more than one variable and its partial derivatives. Partial derivatives measure how a function changes when one of its variables is varied, while the others are held constant. PDEs are used to model various phenomena in physics, engineering, biology, and other fields.

Some examples of PDEs are:

- The heat equation: `u_t = k u_xx`, which describes how the temperature `u` of a thin rod changes over time `t` and position `x`, depending on the thermal conductivity `k` of the rod.
- The wave equation: `u_tt = c^2 u_xx`, which describes how the displacement `u` of a vibrating string changes over time `t` and position `x`, depending on the wave speed `c` of the string.
- The Laplace equation: `u_xx + u_yy = 0`, which describes the potential `u` of a harmonic function in two dimensions `x` and `y`.

To solve a PDE, one needs to find a function `u` that satisfies the equation and some boundary and initial conditions that specify the values or behavior of `u` on the edges or at the initial time of the domain of interest. There are various methods to solve PDEs, such as separation of variables, Fourier series, transform methods, numerical methods, and others.

Some important concepts and techniques in PDEs are:

- The order of a PDE is the highest order of partial derivatives that appear in the equation. For example, the heat equation is a second-order PDE, while the transport equation `u_t + a u_x = 0` is a first-order PDE.
- The linearity of a PDE is determined by whether the equation is linear or nonlinear in the unknown function `u` and its partial derivatives. For example, the heat equation is a linear PDE, while the Burgers equation `u_t + u u_x = 0` is a nonlinear PDE.
- The classification of a second-order PDE is based on the sign of the discriminant `B^2 - 4AC` of the general form `A u_xx + B u_xy + C u_yy + D u_x + E u_y + F u = G`, where `A, B, C, D, E, F, G` are functions of `x` and `y`. The PDE is called elliptic if the discriminant is negative, parabolic if the discriminant is zero, and hyperbolic if the discriminant is positive. For example, the Laplace equation is an elliptic PDE, the heat equation is a parabolic PDE, and the wave equation is a hyperbolic PDE.
- The characteristic curves of a first-order PDE are the curves along which the equation can be reduced to an ordinary differential equation by the method of characteristics. For example, the characteristic curves of the transport equation are the straight lines `x - at = c`, where `c` is a constant.
- The solution of a PDE may not be unique or may not exist, depending on the equation and the boundary and initial conditions. For example, the Laplace equation has a unique solution if the boundary conditions are given on a closed curve, but may have infinitely many solutions if the boundary conditions are given on an open curve. The existence and uniqueness of solutions can be studied by various theorems, such as the maximum principle, the energy method, and the Cauchy-Kowalevski theorem.