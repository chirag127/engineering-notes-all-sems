# Solution of Wave and Heat Conduction Equation up to Two Dimension

Module II: Applications of Partial Differential Equations

Subject: Mathematics-IV KCS

The wave equation and heat conduction equation are two important partial differential equations that arise in many physical applications. In this section, we will discuss the solution of these equations in one and two dimensions.

## Wave Equation

The wave equation is a second-order linear partial differential equation that describes the propagation of waves, such as sound or light waves. In one dimension, the wave equation can be written as:

∂²u/∂t² = c² ∂²u/∂x²

where u(x,t) is the displacement of the wave at position x and time t, and c is the speed of the wave.

### Solution in One Dimension

The general solution of the one-dimensional wave equation can be written as the sum of two functions, f(x-ct) and g(x+ct), where f and g are arbitrary functions. This solution can be interpreted as the superposition of two waves traveling in opposite directions with speed c.

u(x,t) = f(x-ct) + g(x+ct)

### Solution in Two Dimensions

In two dimensions, the wave equation can be written as:

∂²u/∂t² = c² (∂²u/∂x² + ∂²u/∂y²)

The general solution of the two-dimensional wave equation can be obtained using separation of variables. Assuming that the solution can be written as the product of two functions, u(x,y,t) = X(x)Y(y)T(t), we can separate the equation into three ordinary differential equations:

T''(t) + λc²T(t) = 0
X''(x) + λX(x) = 0
Y''(y) + λY(y) = 0

where λ is a separation constant. The solutions of these equations can be written in terms of trigonometric functions or exponential functions, depending on the boundary conditions.

## Heat Conduction Equation

The heat conduction equation, also known as the heat equation, is a second-order linear partial differential equation that describes the distribution of heat in a given region over time. In one dimension, the heat equation can be written as:

∂u/∂t = k ∂²u/∂x²

where u(x,t) is the temperature at position x and time t, and k is the thermal conductivity of the material.

### Solution in One Dimension

The general solution of the one-dimensional heat equation can be obtained using separation of variables. Assuming that the solution can be written as the product of two functions, u(x,t) = X(x)T(t), we can separate the equation into two ordinary differential equations:

T'(t) - kλT(t) = 0
X''(x) + λX(x) = 0

where λ is a separation constant. The solutions of these equations can be written in terms of exponential functions or trigonometric functions, depending on the boundary conditions.

### Solution in Two Dimensions

In two dimensions, the heat equation can be written as:

∂u/∂t = k (∂²u/∂x² + ∂²u/∂y²)

The general solution of the two-dimensional heat equation can be obtained using separation of variables. Assuming that the solution can be written as the product of three functions, u(x,y,t) = X(x)Y(y)T(t), we can separate the equation into three ordinary differential equations:

T'(t) - kλT(t) = 0
X''(x) + λX(x) = 0
Y''(y) + λY(y) = 0

where λ is a separation constant. The solutions of these equations can be written in terms of exponential functions or trigonometric functions, depending on the boundary conditions.

These are the basic methods for solving the wave and heat conduction equations in one and two dimensions. More advanced techniques, such as the method of characteristics and the use of Green's functions, can also be used to solve these equations in more complex situations.