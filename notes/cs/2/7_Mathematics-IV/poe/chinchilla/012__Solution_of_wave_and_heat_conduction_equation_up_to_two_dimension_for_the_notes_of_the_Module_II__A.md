### Solution of wave and heat conduction equation up to two dimension

Partial differential equations (PDEs) are widely used in modeling various physical phenomena. In this module, we will study the applications of partial differential equations in various fields, such as physics, engineering, and finance. In this section, we will focus on the solution of wave and heat conduction equation up to two dimensions.

#### Wave Equation

The wave equation is a second-order linear partial differential equation that describes the propagation of waves in a medium. It is given by:

$$\frac{\partial^2 u}{\partial t^2}=c^2\nabla^2 u$$

where $u(x,y,t)$ is the displacement of the wave at position $(x,y)$ and time $t$, $\nabla^2$ is the Laplacian operator, and $c$ is the wave speed.

##### Solution of 1D Wave Equation

The solution of the 1D wave equation is given by:

$$u(x,t)=f(x-ct)+g(x+ct)$$

where $f$ and $g$ are arbitrary functions that represent the initial and boundary conditions.

##### Solution of 2D Wave Equation

The solution of the 2D wave equation is given by:

$$u(x,y,t)=\frac{1}{2}\left(f(x-ct,y)+f(x+ct,y)\right)+\frac{1}{2}\left(f(x,y-ct)+f(x,y+ct)\right)$$

where $f(x,y)$ is the initial displacement of the wave.

#### Heat Conduction Equation

The heat conduction equation is a second-order linear partial differential equation that describes the flow of heat in a medium. It is given by:

$$\frac{\partial u}{\partial t}=k\nabla^2 u$$

where $u(x,y,t)$ is the temperature at position $(x,y)$ and time $t$, $\nabla^2$ is the Laplacian operator, and $k$ is the thermal conductivity.

##### Solution of 1D Heat Conduction Equation

The solution of the 1D heat conduction equation is given by:

$$u(x,t)=\frac{1}{\sqrt{4\pi k t}}\int_{-\infty}^{\infty}f(y)\exp\left(-\frac{(x-y)^2}{4kt}\right)dy$$

where $f(y)$ is the initial temperature distribution.

##### Solution of 2D Heat Conduction Equation

The solution of the 2D heat conduction equation is given by:

$$u(x,y,t)=\frac{1}{4\pi k t}\int_{-\infty}^{\infty}\int_{-\infty}^{\infty}f(x',y')\exp\left(-\frac{(x-x')^2+(y-y')^2}{4kt}\right)dx'dy'$$

where $f(x,y)$ is the initial temperature distribution.

#### Conclusion

In this section, we have studied the solution of wave and heat conduction equation up to two dimensions. These equations are widely used in modeling various physical phenomena and have numerous applications. It is important to understand the solution of these equations to analyze and solve problems in physics, engineering, and other fields.