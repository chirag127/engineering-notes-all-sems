### Solution of wave and heat conduction equation up to two dimension

- The wave equation is a partial differential equation that describes the propagation of waves in a medium, such as sound waves, electromagnetic waves, or water waves. The wave equation in two dimensions can be written as

$$\frac{\partial^2 u}{\partial t^2} = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the displacement of the wave at position $(x,y)$ and time $t$, and $c$ is the speed of the wave.

- The heat equation is a partial differential equation that describes the diffusion of heat in a medium, such as a metal rod, a fluid, or the Earth's crust. The heat equation in two dimensions can be written as

$$\frac{\partial u}{\partial t} = k \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the temperature of the medium at position $(x,y)$ and time $t$, and $k$ is the thermal conductivity of the medium.

- One of the methods to solve these equations is the separation of variables, which assumes that the solution can be written as a product of functions that depend on only one variable, such as

$$u(x,y,t) = X(x)Y(y)T(t)$$

- By substituting this form of solution into the wave or heat equation, and dividing by $XYT$, we obtain an equation that can be separated into three ordinary differential equations, one for each variable. For example, for the wave equation, we get

$$\frac{1}{c^2}\frac{T''}{T} = \frac{X''}{X} + \frac{Y''}{Y} = -\lambda$$

where $\lambda$ is a constant, and the prime denotes differentiation.

- The equation for $T$ can be solved by using the characteristic equation, and the equation for $X$ and $Y$ can be solved by using the method of eigenvalues and eigenfunctions, which involves finding the values of $\lambda$ and the corresponding functions $X$ and $Y$ that satisfy the boundary conditions of the problem.

- The general solution of the wave or heat equation can then be obtained by using the principle of superposition, which states that any linear combination of solutions is also a solution. For example, for the wave equation, we can write

$$u(x,y,t) = \sum_{n,m=1}^\infty A_{nm} \sin\left(\frac{n\pi x}{L}\right) \sin\left(\frac{m\pi y}{W}\right) \cos\left(c\sqrt{\frac{n^2\pi^2}{L^2} + \frac{m^2\pi^2}{W^2}}t\right)$$

where $A_{nm}$ are constants determined by the initial conditions of the problem, and $L$ and $W$ are the lengths of the sides of the rectangular domain.

- For the heat equation, the general solution is similar, except that the cosine term is replaced by an exponential term that decays over time, such as

$$u(x,y,t) = \sum_{n,m=1}^\infty A_{nm} \sin\left(\frac{n\pi x}{L}\right) \sin\left(\frac{m\pi y}{W}\right) \exp\left(-k\left(\frac{n^2\pi^2}{L^2} + \frac{m^2\pi^2}{W^2}\right)t\right)$$

- These solutions can be used to model various physical phenomena, such as the vibration of a drum, the heat distribution in a metal plate, or the propagation of seismic waves.