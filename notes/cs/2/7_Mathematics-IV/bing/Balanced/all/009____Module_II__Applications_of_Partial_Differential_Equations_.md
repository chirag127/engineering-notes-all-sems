## Module II: Applications of Partial Differential Equations:

Partial differential equations (PDEs) are equations that involve partial derivatives of functions of two or more variables. They are used to model various phenomena in science, engineering, and other fields. Some of the applications of PDEs are:

- **Heat equation**: This is a second-order linear PDE that describes how the temperature of a body changes over time and space. The equation is given by

$$
\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}
$$

where $u$ is the temperature, $t$ is the time, $x$ is the spatial coordinate, and $k$ is a constant that depends on the thermal conductivity of the material. The heat equation can be used to model heat transfer in solids, liquids, and gases .

- **Wave equation**: This is another second-order linear PDE that describes how waves propagate in a medium. The equation is given by

$$
\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}
$$

where $u$ is the displacement of the wave, $t$ is the time, $x$ is the spatial coordinate, and $c$ is the speed of the wave. The wave equation can be used to model sound waves, light waves, water waves, and electromagnetic waves .

- **Laplace equation**: This is a second-order linear PDE that describes the potential function of a harmonic function. The equation is given by

$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = 0
$$

where $u$ is the potential function, and $x$ and $y$ are the spatial coordinates. The Laplace equation can be used to model electrostatics, magnetostatics, fluid flow, heat conduction, and other problems involving steady-state conditions .

- **Poisson equation**: This is a generalization of the Laplace equation that includes a source term. The equation is given by

$$
\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = f(x,y)
$$

where $u$ is the potential function, $x$ and $y$ are the spatial coordinates, and $f(x,y)$ is the source term. The Poisson equation can be used to model problems involving non-homogeneous boundary conditions, such as gravity, electric charge, and mass density .

- **Black-Scholes equation**: This is a second-order nonlinear PDE that describes the price of a financial derivative, such as an option or a futures contract. The equation is given by

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + r S \frac{\partial V}{\partial S} - r V = 0
$$

where $V$ is the value of the derivative, $t$ is the time, $S$ is the price of the underlying asset, $\sigma$ is the volatility of the asset, and $r$ is the risk-free interest rate. The Black-Scholes equation can be used to construct financial models and to hedge risk .