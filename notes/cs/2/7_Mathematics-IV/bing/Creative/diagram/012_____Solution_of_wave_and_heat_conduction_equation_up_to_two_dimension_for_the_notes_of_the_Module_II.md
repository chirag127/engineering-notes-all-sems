### Solution of wave and heat conduction equation up to two dimension

- The wave equation is a partial differential equation that describes the propagation of waves in a medium, such as sound waves, electromagnetic waves, or water waves. The wave equation in two dimensions can be written as

$$\frac{\partial^2 u}{\partial t^2} = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the displacement of the wave at position $(x,y)$ and time $t$, and $c$ is the speed of the wave.

- The heat equation is a partial differential equation that describes the diffusion of heat in a medium, such as a metal rod, a fluid, or the Earth's crust. The heat equation in two dimensions can be written as

$$\frac{\partial u}{\partial t} = k \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the temperature of the medium at position $(x,y)$ and time $t$, and $k$ is the thermal conductivity of the medium.

- One of the methods to solve these equations is the separation of variables, which assumes that the solution can be written as a product of functions that depend on only one variable, such as

$$u(x,y,t) = X(x)Y(y)T(t)$$

- By substituting this form of solution into the equation and dividing by $XYT$, we obtain an equation that can be separated into three ordinary differential equations, one for each variable. For example, for the wave equation, we get

$$\frac{1}{c^2}\frac{T''}{T} = \frac{X''}{X} + \frac{Y''}{Y} = -\lambda$$

where $\lambda$ is a constant that can be determined by the boundary conditions.

- The equation for $T$ is a second-order linear homogeneous equation with constant coefficients, which has the general solution

$$T(t) = A \cos(\sqrt{\lambda} c t) + B \sin(\sqrt{\lambda} c t)$$

where $A$ and $B$ are arbitrary constants.

- The equations for $X$ and $Y$ are also second-order linear homogeneous equations with constant coefficients, which have the general solutions

$$X(x) = C \cos(\sqrt{\lambda} x) + D \sin(\sqrt{\lambda} x)$$

$$Y(y) = E \cos(\sqrt{\lambda} y) + F \sin(\sqrt{\lambda} y)$$

where $C$, $D$, $E$, and $F$ are arbitrary constants.

- The boundary conditions will determine the values of these constants and the value of $\lambda$. For example, if the wave is confined in a rectangular region with fixed ends, such as a vibrating membrane, then the boundary conditions are

$$u(0,y,t) = u(a,y,t) = u(x,0,t) = u(x,b,t) = 0$$

where $a$ and $b$ are the lengths of the sides of the rectangle.

- These boundary conditions imply that $C = F = 0$ and that $\lambda$ must be of the form

$$\lambda = \lambda_{mn} = \left( \frac{m \pi}{a} \right)^2 + \left( \frac{n \pi}{b} \right)^2$$

where $m$ and $n$ are positive integers.

- Therefore, the solution of the wave equation can be written as

$$u(x,y,t) = \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} A_{mn} \sin\left( \frac{m \pi x}{a} \right) \sin\left( \frac{n \pi y}{b} \right) \cos\left( \sqrt{\lambda_{mn}} c t \right) + B_{mn} \sin\left( \frac{m \pi x}{a} \right) \sin\left( \frac{n \pi y}{b} \right) \sin\left( \sqrt{\lambda_{mn}} c t \right)$$

where $A_{mn