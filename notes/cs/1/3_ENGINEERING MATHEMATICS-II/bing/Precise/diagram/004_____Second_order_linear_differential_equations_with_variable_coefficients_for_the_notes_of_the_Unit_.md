### Second Order Linear Differential Equations with Variable Coefficients

A second-order linear differential equation with variable coefficients is an equation of the form:

```
a(x)y'' + b(x)y' + c(x)y = f(x)
```

where `a(x)`, `b(x)`, `c(x)`, and `f(x)` are continuous functions of `x` on some interval `I`.

- The general solution of a second-order linear differential equation with variable coefficients is given by:

```
y = C1*y1 + C2*y2 + yp
```

where `C1` and `C2` are arbitrary constants, `y1` and `y2` are linearly independent solutions of the corresponding homogeneous equation, and `yp` is a particular solution of the non-homogeneous equation.

- The method of undetermined coefficients can be used to find a particular solution `yp` if `f(x)` is a polynomial, an exponential function, or a sine or cosine function.

- The method of variation of parameters can be used to find a particular solution `yp` for any continuous function `f(x)`.

- The Wronskian `W(y1, y2)` of two solutions `y1` and `y2` of the corresponding homogeneous equation is given by:

```
W(y1, y2) = y1*y2' - y2*y1'
```

- If the Wronskian `W(y1, y2)` is not equal to zero on the interval `I`, then `y1` and `y2` are linearly independent on `I`.

- The Wronskian can be used to determine whether two solutions of the corresponding homogeneous equation are linearly independent.

- The Wronskian can also be used to find a particular solution `yp` using the method of variation of parameters.
