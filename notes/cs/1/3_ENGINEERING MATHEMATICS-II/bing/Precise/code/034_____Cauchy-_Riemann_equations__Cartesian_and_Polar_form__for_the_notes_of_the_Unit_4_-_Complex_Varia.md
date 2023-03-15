### Cauchy-Riemann Equations (Cartesian and Polar Form)

The Cauchy-Riemann equations are a set of partial differential equations that provide a necessary and sufficient condition for a function to be analytic. These equations are used in the study of complex variable differentiation, which is a topic in the subject of Engineering Mathematics-II.

#### Cartesian Form

In the Cartesian coordinate system, the Cauchy-Riemann equations are given by:

```
∂u/∂x = ∂v/∂y
∂u/∂y = -∂v/∂x
```

where `u` and `v` are the real and imaginary parts of a complex function `f(z) = u(x,y) + iv(x,y)`.

#### Polar Form

In the polar coordinate system, the Cauchy-Riemann equations are given by:

```
∂u/∂r = (1/r) ∂v/∂θ
∂v/∂r = -(1/r) ∂u/∂θ
```

where `u` and `v` are the real and imaginary parts of a complex function `f(z) = u(r,θ) + iv(r,θ)`.

These equations can be derived by converting the Cartesian form of the Cauchy-Riemann equations into polar coordinates using the following transformations:

```
x = r cos(θ)
y = r sin(θ)
```

The Cauchy-Riemann equations are an important tool in the study of complex variable differentiation and are used to determine whether a function is analytic or not. They are a fundamental concept in the subject of Engineering Mathematics-II and are covered in Unit 4 - Complex Variable-Differentiation.