# Solution of wave and heat conduction equation up to two dimension

- The wave equation is a partial differential equation that describes the propagation of waves in a medium, such as sound waves, electromagnetic waves, or water waves. The general form of the wave equation in two dimensions is:

$$\frac{\partial^2 u}{\partial t^2} = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the displacement of the wave at position $(x,y)$ and time $t$, and $c$ is the speed of the wave.

- The heat equation is a partial differential equation that describes the diffusion of heat in a medium, such as a metal rod, a fluid, or a gas. The general form of the heat equation in two dimensions is:

$$\frac{\partial u}{\partial t} = k \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the temperature of the medium at position $(x,y)$ and time $t$, and $k$ is the thermal conductivity of the medium.

- Both the wave equation and the heat equation can be solved by using the method of separation of variables, which assumes that the solution can be written as a product of functions that depend on only one variable, such as:

$$u(x,y,t) = X(x)Y(y)T(t)$$

- By substituting this form of solution into the original equation and dividing by $XYT$, we obtain an equation that can be separated into three ordinary differential equations, one for each variable. For example, for the wave equation, we get:

$$\frac{1}{c^2}\frac{T''}{T} = \frac{X''}{X} + \frac{Y''}{Y} = -\lambda$$

where $\lambda$ is a constant that can be determined by applying the boundary conditions.

- The equation for $T$ can be solved by using the characteristic equation, which gives two possible cases: $\lambda > 0$, $\lambda = 0$, or $\lambda < 0$. Depending on the case, the solution for $T$ can be written as a combination of exponential, sinusoidal, or hyperbolic functions.

- The equations for $X$ and $Y$ can be solved by using the method of eigenvalues and eigenfunctions, which gives a set of possible values for $\lambda$ and corresponding functions for $X$ and $Y$ that satisfy the boundary conditions. For example, if the boundary conditions are $u(0,y,t) = u(L,y,t) = 0$ and $u(x,0,t) = u(x,W,t) = 0$, then the possible values of $\lambda$ are:

$$\lambda_{mn} = \left( \frac{m\pi}{L} \right)^2 + \left( \frac{n\pi}{W} \right)^2$$

where $m$ and $n$ are positive integers, and the corresponding eigenfunctions are:

$$X_m(x) = \sin \left( \frac{m\pi x}{L} \right)$$

$$Y_n(y) = \sin \left( \frac{n\pi y}{W} \right)$$

- The general solution for $u$ can be written as a linear combination of the products of the eigenfunctions and the solutions for $T$, such as:

$$u(x,y,t) = \sum_{m=1}^{\infty} \sum_{n=1}^{\infty} A_{mn} \sin \left( \frac{m\pi x}{L} \right) \sin \left( \frac{n\pi y}{W} \right) T_{mn}(t)$$

where $A_{mn}$ are constants that can be determined by using the initial conditions.

- The method of separation of variables can also be applied to the heat equation, with some modifications. For example, the equation for $T$ will have only one possible case: $\lambda > 0$, and the solution for $T$ will be an exponential function that decays over time. The equation for $X$ and $Y$ will have the same form as before, but the possible values of $\lambda