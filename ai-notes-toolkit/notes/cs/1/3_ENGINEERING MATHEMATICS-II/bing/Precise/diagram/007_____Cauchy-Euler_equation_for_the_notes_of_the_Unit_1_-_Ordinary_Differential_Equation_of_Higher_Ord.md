### Cauchy-Euler equation

The Cauchy-Euler equation is a type of linear differential equation with variable coefficients. It is also known as the Euler-Cauchy equation or the equidimensional equation. It has the following form:

```
x^n * y^(n) + a_(n-1) * x^(n-1) * y^(n-1) + ... + a_1 * x * y' + a_0 * y = 0
```

where `n` is a positive integer, `a_(n-1)`, `a_(n-2)`, ..., `a_1`, and `a_0` are constants, and `y^(n)` denotes the `n`-th derivative of `y` with respect to `x`.

The Cauchy-Euler equation can be solved using the method of undetermined coefficients. This involves assuming a solution of the form `y = x^m` and substituting it into the differential equation to determine the value of `m`. The resulting characteristic equation is a polynomial equation of degree `n`, which can be solved to find the `n` values of `m`. These values can then be used to construct the general solution of the Cauchy-Euler equation.

The Cauchy-Euler equation is commonly encountered in problems involving heat conduction, fluid flow, and electric circuits. It is also used in the study of Laplace transforms and Bessel functions.