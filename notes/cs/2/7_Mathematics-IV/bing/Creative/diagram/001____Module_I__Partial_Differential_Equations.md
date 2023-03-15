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

$$\left(\frac{\partial^2 u}{\partial x^2}\right)^2+\frac{\partial u}{\partial y}=0$$

is a second-order PDE of degree two.

- The solution of a PDE is a function that satisfies the equation and any given boundary or initial conditions  . The solution may be unique, non-unique, or non-existent, depending on the equation and the conditions .
- Some common types of PDEs are:

  - The transport equation: $\frac{\partial u}{\partial t}+a\frac{\partial u}{\partial x}=0$, which models the motion of a wave or a substance with constant speed $a$.
  - The heat equation: $\frac{\partial u}{\partial t}=k\frac{\partial^2 u}{\partial x^2}$, which models the diffusion of heat in a rod with thermal conductivity $k$.
  - The wave equation: $\frac{\partial^2 u}{\partial t^2}=c^2\frac{\partial^2 u}{\partial x^2}$, which models the propagation of a wave with speed $c$ in a string or a membrane.
  - The Laplace equation: $\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}=0$, which models the potential field of a static electric charge or a steady-state heat distribution .
  - The Poisson equation: $\frac{\partial^2 u}{\partial x^2}+\frac{\partial^2 u}{\partial y^2}=f(x,y)$, which models the potential field of a non-static electric charge or a non-steady-state heat distribution .
  - The Burgers equation: $\frac{\partial u}{\partial t}+u\frac{\partial u}{\partial x}=\nu\frac{\partial^2 u}{\partial x^2}$, which models the motion of a viscous fluid with viscosity $\nu$.

- Some methods for solving PDEs are:

  - Separation of variables: a technique that reduces a PDE to a system of ordinary differential equations (ODEs) by assuming that the solution can be written as a product of functions of each variable  .
  - Fourier series: a technique that represents the solution as an infinite sum of trigonometric functions that satisfy the boundary conditions and the PDE  .
  - Fourier transform: a technique that transforms a PDE from the spatial domain to the frequency domain, where it may be