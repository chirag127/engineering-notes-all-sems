## Module I: Partial Differential Equations

- A partial differential equation (PDE) is an equation that relates a function of several variables to its partial derivatives  .
- A partial derivative of a function is the rate of change of the function with respect to one of its variables, while keeping the others constant.
- PDEs are used to model various phenomena in physics, engineering, biology, and other fields, such as heat, sound, fluid flow, electromagnetism, etc .
- The general form of a PDE is:

`Lu = ∑ν=1nAν∂u∂xν+B=0`

where `u` is the unknown function, `x1, x2, ..., xn` are the independent variables, `Aν` are coefficient matrices, and `B` is a vector that may depend on `x` and `u`.

- The order of a PDE is the highest order of the partial derivatives involved in the equation . For example, the equation `∂u∂x+∂2u∂y2=0` is a second-order PDE.
- The degree of a PDE is the power of the highest-order derivative in the equation . For example, the equation `∂2u∂x2+∂2u∂y2=0` is a second-degree PDE.
- The linearity of a PDE depends on whether the equation is linear or nonlinear in `u` and its derivatives . A PDE is linear if it can be written as a sum of terms, each of which is a constant or a product of a constant and `u` or one of its derivatives. A PDE is nonlinear if it contains any other terms, such as products or powers of `u` or its derivatives. For example, the equation `∂u∂x+u2=0` is a nonlinear PDE.
- The solution of a PDE is a function that satisfies the equation for all values of the independent variables in a given domain . The solution may be unique or non-unique, depending on the initial and boundary conditions imposed on the problem .
- Some common types of PDEs are:

  - The transport equation: `∂u∂t+c∂u∂x=0`, which models the propagation of a wave or a signal with constant speed `c`.
  - The heat equation: `∂u∂t=k∂2u∂x2`, which models the diffusion of heat in a one-dimensional rod with thermal conductivity `k`.
  - The wave equation: `∂2u∂t2=c2∂2u∂x2`, which models the vibration of a string or a membrane with constant tension `c2`.
  - The Laplace equation: `∂2u∂x2+∂2u∂y2=0`, which models the potential or steady-state temperature in a two-dimensional region .
  - The Poisson equation: `∂2u∂x2+∂2u∂y2=f(x,y)`, which models the potential or steady-state temperature in a two-dimensional region with a source or sink term `f(x,y)` .
  - The Burgers equation: `∂u∂t+u∂u∂x=ν∂2u∂x2`, which models the motion of a viscous fluid with viscosity `ν`.