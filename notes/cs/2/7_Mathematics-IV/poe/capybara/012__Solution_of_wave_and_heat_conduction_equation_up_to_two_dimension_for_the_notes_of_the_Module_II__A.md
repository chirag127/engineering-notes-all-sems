### Solution of Wave and Heat Conduction Equation up to Two Dimension

In the field of mathematics, partial differential equations are used to model various physical phenomena. Two of the most common types of partial differential equations are the wave equation and the heat conduction equation. These equations describe the behavior of waves and heat in a given system.

#### Wave Equation

The wave equation is a partial differential equation that describes the behavior of waves in a system. It is given by:

```
∂²u/∂t² = c²(∂²u/∂x² + ∂²u/∂y²)
```

where `u` is the displacement of the wave, `t` is time, `x` and `y` are spatial coordinates, and `c` is the wave speed.

The solution to the wave equation up to two dimensions can be obtained using the method of separation of variables. This method involves assuming that the solution can be written as a product of functions of time and space:

```
u(x, y, t) = X(x)Y(y)T(t)
```

By substituting this into the wave equation and dividing both sides by `c²XYT`, we get:

```
T''(t)/c²T(t) = X''(x)/X(x) + Y''(y)/Y(y)
```

Since the left-hand side depends only on time and the right-hand side depends only on space, both sides must be equal to a constant:

```
T''(t)/c²T(t) = -λ
X''(x)/X(x) + Y''(y)/Y(y) = λ
```

Solving for `T(t)` gives us:

```
T(t) = A cos(√λct) + B sin(√λct)
```

where `A` and `B` are constants.

Solving for `X(x)` and `Y(y)` separately gives us:

```
X(x) = C cos(√λx) + D sin(√λx)
Y(y) = E cos(√λy) + F sin(√λy)
```

where `C`, `D`, `E`, and `F` are constants.

Putting everything together, we get the general solution to the wave equation up to two dimensions:

```
u(x, y, t) = ΣₙΣₘ[Anm cos(√λₙₘct) + Bnm sin(√λₙₘct)] cos(√λₙₘx) cos(√λₙₘy)
```

where `λₙₘ` is an eigenvalue and `Anm` and `Bnm` are constants.

#### Heat Conduction Equation

The heat conduction equation is a partial differential equation that describes the behavior of heat in a system. It is given by:

```
∂u/∂t = α(∂²u/∂x² + ∂²u/∂y²)
```

where `u` is the temperature, `t` is time, `x` and `y` are spatial coordinates, and `α` is the thermal diffusivity.

The solution to the heat conduction equation up to two dimensions can also be obtained using the method of separation of variables. This method involves assuming that the solution can be written as a product of functions of time and space:

```
u(x, y, t) = X(x)Y(y)T(t)
```

By substituting this into the heat conduction equation and dividing both sides by `αXYT`, we get:

```
T'(t)/αT(t) = X''(x)/X(x) + Y''(y)/Y(y)
```

Since the left-hand side depends only on time and the right-hand side depends only on space, both sides must be equal to a constant:

```
T'(t)/αT(t) = -λ
X''(x)/X(x) + Y''(y)/Y(y) = λ
```

Solving for `T(t)` gives us:

```
T(t) = A e^(-λαt)
```

where `A` is a constant.

Solving for `X(x)` and `Y(y)` separately gives us:

```
X(x) = C cos(√λx) + D sin(√λx)
Y(y) = E cos(√λy) + F sin(√λy)
```

where `C`, `D`, `E`, and `F` are constants.

Putting everything together, we get the general solution to the heat conduction equation up to two dimensions:

```
u(x, y, t) = ΣₙΣₘ[Anm