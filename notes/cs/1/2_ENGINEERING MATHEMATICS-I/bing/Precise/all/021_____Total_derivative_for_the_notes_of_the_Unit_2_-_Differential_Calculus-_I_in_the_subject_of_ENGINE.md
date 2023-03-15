### Total Derivative

The total derivative of a multivariable function is the best linear approximation of the function at a given point. It is a generalization of the concept of the derivative for functions of a single variable.

1. Let `f(x,y)` be a function of two variables `x` and `y`. The total derivative of `f` at a point `(x0,y0)` is given by the matrix `Df(x0,y0)` defined as:

```
Df(x0,y0) = [df/dx(x0,y0) df/dy(x0,y0)]
```

where `df/dx(x0,y0)` and `df/dy(x0,y0)` are the partial derivatives of `f` with respect to `x` and `y` respectively, evaluated at the point `(x0,y0)`.

2. The total derivative can be used to approximate the change in the value of the function `f` near the point `(x0,y0)` as follows:

```
f(x0+Δx,y0+Δy) ≈ f(x0,y0) + Df(x0,y0) * [Δx, Δy]^T
```

where `[Δx, Δy]^T` is the column vector of the changes in `x` and `y` respectively.

3. The total derivative can also be used to find the directional derivative of the function `f` in the direction of a unit vector `u` as follows:

```
Duf(x0,y0) = Df(x0,y0) * u
```

where `Duf(x0,y0)` is the directional derivative of `f` at `(x0,y0)` in the direction of `u`.

4. The total derivative can be extended to functions of more than two variables in a similar manner. For a function `f(x1,x2,...,xn)` of `n` variables, the total derivative at a point `(x10,x20,...,xn0)` is given by the matrix `Df(x10,x20,...,xn0)` defined as:

```
Df(x10,x20,...,xn0) = [df/dx1(x10,x20,...,xn0) df/dx2(x10,x20,...,xn0) ... df/dxn(x10,x20,...,xn0)]
```

where `df/dxi(x10,x20,...,xn0)` is the partial derivative of `f` with respect to the variable `xi`, evaluated at the point `(x10,x20,...,xn0)`. The total derivative can be used to approximate the change in the value of the function `f` near the point `(x10,x20,...,xn0)` and to find the directional derivative of `f` in the direction of a unit vector `u` in a similar manner as for functions of two variables.