## Module I: Partial Differential Equations

- A partial differential equation (PDE) is an equation that relates a function of several variables to its partial derivatives  .
- A partial derivative of a function is the rate of change of the function with respect to one of its variables, while keeping the others constant.
- PDEs are used to model various phenomena in physics, engineering, biology, and other fields, such as heat, sound, fluid flow, electromagnetism, etc .
- The general form of a PDE is:

$$Lu=\sum_{\nu=1}^n A_\nu \frac{\partial u}{\partial x_\nu}+B=0$$

where $u$ is the unknown function, $x_1, x_2, \dots, x_n$ are the independent variables, $A_\nu$ are coefficient matrices, and $B$ is a vector that may depend on $x$ and $u$.

- The order of a PDE is the highest order of the partial derivatives involved in the equation . For example, the equation

$$\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}=0$$

is a second-order PDE.

- The degree of a PDE is the power of the highest-order derivative term when the equation is written as a polynomial in the derivatives . For example, the equation

$$\left(\frac{\partial u}{\partial x}\right)^2+\left(\frac{\partial u}{\partial y}\right)^2=1$$

is a first-order PDE of degree two.

- The solution of a PDE is a function that satisfies the equation and any given boundary or initial conditions  . The solution may be unique, non-unique, or non-existent, depending on the equation and the conditions .
- Some common methods for solving PDEs are separation of variables, Fourier series, Laplace transform, Green's function, finite difference, finite element, etc   .
- Some important types of PDEs are:

  - The transport equation: $\frac{\partial u}{\partial t}+c\frac{\partial u}{\partial x}=0$, which models the propagation of a wave or a signal with constant speed $c$.
  - The heat equation: $\frac{\partial u}{\partial t}=k\frac{\partial^2 u}{\partial x^2}$, which models the diffusion of heat in a one-dimensional rod with thermal conductivity $k$.
  - The wave equation: $\frac{\partial^2 u}{\partial t^2}=c^2\frac{\partial^2 u}{\partial x^2}$, which models the vibration of a string or the propagation of a wave with constant speed $c$.
  - The Laplace equation: $\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}=0$, which models the potential field or the steady-state temperature distribution in a two-dimensional region  .
  - The Poisson equation: $\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}=f(x,y)$, which models the potential field or the steady-state temperature distribution in a two-dimensional region with a source or sink term $f(x,y)$  .
  - The Burgers equation: $\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}=\nu\frac{\partial^2 u}{\partial x^2}$, which models the nonlinear dynamics of fluid flow or shock waves with viscosity $\nu$.