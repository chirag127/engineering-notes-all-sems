# Solution of wave and heat conduction equation up to two dimension

## Wave equation

The wave equation is a partial differential equation that describes the propagation of waves in a medium. The general form of the wave equation in two dimensions is:

$$\frac{\partial^2 u}{\partial t^2} = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the displacement of the wave at position $(x,y)$ and time $t$, and $c$ is the speed of the wave.

The wave equation can be solved by using the method of separation of variables, which assumes that the solution can be written as a product of functions that depend on only one variable:

$$u(x,y,t) = X(x)Y(y)T(t)$$

Substituting this into the wave equation and dividing by $XYT$, we get:

$$\frac{1}{c^2} \frac{T''}{T} = \frac{X''}{X} + \frac{Y''}{Y} = -\lambda$$

where $\lambda$ is a constant. This equation can be separated into three ordinary differential equations:

$$T'' + \lambda c^2 T = 0$$
$$X'' + \mu X = 0$$
$$Y'' + (\lambda - \mu) Y = 0$$

where $\mu$ is another constant. The solutions of these equations depend on the boundary conditions and the initial conditions of the problem. For example, if we consider a rectangular membrane with fixed edges, the boundary conditions are:

$$u(0,y,t) = u(a,y,t) = u(x,0,t) = u(x,b,t) = 0$$

where $a$ and $b$ are the lengths of the sides of the rectangle. The initial conditions are:

$$u(x,y,0) = f(x,y)$$
$$\frac{\partial u}{\partial t}(x,y,0) = g(x,y)$$

where $f(x,y)$ and $g(x,y)$ are given functions that describe the initial shape and velocity of the membrane.

The solutions of the ordinary differential equations are:

$$T(t) = A \cos(\sqrt{\lambda} c t) + B \sin(\sqrt{\lambda} c t)$$
$$X(x) = C \cos(\sqrt{\mu} x) + D \sin(\sqrt{\mu} x)$$
$$Y(y) = E \cos(\sqrt{\lambda - \mu} y) + F \sin(\sqrt{\lambda - \mu} y)$$

where $A, B, C, D, E, F$ are constants. Applying the boundary conditions, we get:

$$X(0) = X(a) = 0 \implies C = 0, \sqrt{\mu} a = n \pi, \mu = \left( \frac{n \pi}{a} \right)^2$$
$$Y(0) = Y(b) = 0 \implies E = 0, \sqrt{\lambda - \mu} b = m \pi, \lambda = \left( \frac{m \pi}{b} \right)^2 + \left( \frac{n \pi}{a} \right)^2$$

where $n$ and $m$ are positive integers. Therefore, the general solution of the wave equation is a linear combination of the following functions:

$$u_{mn}(x,y,t) = \left( A_{mn} \cos(\sqrt{\lambda_{mn}} c t) + B_{mn} \sin(\sqrt{\lambda_{mn}} c t) \right) \sin \left( \frac{m \pi y}{b} \right) \sin \left( \frac{n \pi x}{a} \right)$$

where $\lambda_{mn} = \left( \frac{m \pi}{b} \right)^2 + \left( \frac{n \pi}{a} \right)^2$ and $A_{mn}$ and $B_{mn}$ are constants. The coefficients $A_{mn}$ and $B_{mn}$ can be determined by using the initial conditions and the orthogonality of the sine functions. The final solution is:

$$u(x,y,t) = \sum_{m=1}^{\in