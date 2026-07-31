### Cauchy-Riemann Equations (Cartesian and Polar Form)

The Cauchy-Riemann equations are a set of partial differential equations that provide a necessary and sufficient condition for a complex function to be differentiable. These equations are named after Augustin-Louis Cauchy and Bernhard Riemann.

#### Cartesian Form

Let `f(z) = u(x,y) + iv(x,y)` be a complex-valued function, where `u` and `v` are real-valued functions of the real variables `x` and `y`. The Cauchy-Riemann equations in Cartesian form are given by:

```
∂u/∂x = ∂v/∂y
∂u/∂y = -∂v/∂x
```

These equations state that the partial derivatives of `u` and `v` with respect to `x` and `y` must satisfy the above conditions for `f(z)` to be differentiable.

#### Polar Form

The Cauchy-Riemann equations can also be expressed in polar coordinates. Let `z = r(cos(θ) + i sin(θ))` and `f(z) = u(r,θ) + iv(r,θ)`. Then, the Cauchy-Riemann equations in polar form are given by:

```
∂u/∂r = (1/r) ∂v/∂θ
∂v/∂r = -(1/r) ∂u/∂θ
```

These equations state that the partial derivatives of `u` and `v` with respect to `r` and `θ` must satisfy the above conditions for `f(z)` to be differentiable.

The Cauchy-Riemann equations are an important tool in the study of complex analysis and have many applications in engineering and physics. They provide a way to determine if a complex function is differentiable and can be used to derive many important results in complex analysis.