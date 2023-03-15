### Solution of wave and heat conduction equation up to two dimension

- The wave equation is a partial differential equation that describes the propagation of waves in a medium, such as sound waves, light waves, or water waves. The wave equation in two dimensions can be written as

$$\frac{\partial^2 u}{\partial t^2} = c^2 \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the displacement of the wave at position $(x,y)$ and time $t$, and $c$ is the speed of the wave.

- The heat equation is a partial differential equation that describes the diffusion of heat in a medium, such as a metal rod, a fluid, or a gas. The heat equation in two dimensions can be written as

$$\frac{\partial u}{\partial t} = k \left( \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} \right)$$

where $u(x,y,t)$ is the temperature of the medium at position $(x,y)$ and time $t$, and $k$ is the thermal conductivity of the medium.

- Both the wave equation and the heat equation can be solved by using the method of separation of variables, which assumes that the solution can be written as a product of functions that depend on only one variable, such as

$$u(x,y,t) = X(x)Y(y)T(t)$$

- By substituting this form of solution into the original equation and dividing by $XYT$, we obtain an equation that can be separated into three ordinary differential equations, one for each variable. For example, for the wave equation, we get

$$\frac{1}{c^2}\frac{T''}{T} = \frac{X''}{X} + \frac{Y''}{Y} = -\lambda$$

where $\lambda$ is a constant that can be determined by applying the boundary conditions.

- The equation for $T$ can be solved by using the characteristic equation, which gives two possible cases: $\lambda > 0$ or $\lambda < 0$. For $\lambda > 0$, the solution is

$$T(t) = A \cos(\sqrt{\lambda} c t) + B \sin(\sqrt{\lambda} c t)$$

where $A$ and $B$ are arbitrary constants. For $\lambda < 0$, the solution is

$$T(t) = A e^{\sqrt{-\lambda} c t} + B e^{-\sqrt{-\lambda} c t}$$

where $A$ and $B$ are arbitrary constants.

- The equation for $X$ can be solved by using the method of undetermined coefficients, which gives two possible cases: $\lambda > 0$ or $\lambda < 0$. For $\lambda > 0$, the solution is

$$X(x) = C \cos(\sqrt{\lambda} x) + D \sin(\sqrt{\lambda} x)$$

where $C$ and $D$ are arbitrary constants. For $\lambda < 0$, the solution is

$$X(x) = C e^{\sqrt{-\lambda} x} + D e^{-\sqrt{-\lambda} x}$$

where $C$ and $D$ are arbitrary constants.

- The equation for $Y$ can be solved in a similar way, by using the method of undetermined coefficients, which gives two possible cases: $\lambda > 0$ or $\lambda < 0$. For $\lambda > 0$, the solution is

$$Y(y) = E \cos(\sqrt{\lambda} y) + F \sin(\sqrt{\lambda} y)$$

where $E$ and $F$ are arbitrary constants. For $\lambda < 0$, the solution is

$$Y(y) = E e^{\sqrt{-\lambda} y} + F e^{-\sqrt{-\lambda} y}$$

where $E$ and $F$ are arbitrary constants.

- The general solution of the wave equation is then a linear combination of the products of the solutions for $T$, $X$, and $Y$, such as

$$u(x,y,t) = \sum_{n=1}^{\infty} \sum_{m=1}^{\infty} (A_{nm} \cos