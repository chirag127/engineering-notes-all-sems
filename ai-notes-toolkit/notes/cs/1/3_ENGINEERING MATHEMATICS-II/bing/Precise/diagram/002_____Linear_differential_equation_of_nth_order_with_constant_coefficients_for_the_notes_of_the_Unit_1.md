### Linear differential equation of nth order with constant coefficients

A linear differential equation of nth order with constant coefficients is an equation of the form:

```
a_n y^(n) + a_(n-1) y^(n-1) + ... + a_1 y' + a_0 y = f(x)
```

where `a_n, a_(n-1), ..., a_1, a_0` are constants, `y^(n)` denotes the nth derivative of `y` with respect to `x`, and `f(x)` is a given function of `x`.

The general solution of such an equation can be obtained by finding the complementary function `y_c(x)` and a particular solution `y_p(x)`.

The complementary function `y_c(x)` is the general solution of the corresponding homogeneous equation:

```
a_n y^(n) + a_(n-1) y^(n-1) + ... + a_1 y' + a_0 y = 0
```

The particular solution `y_p(x)` can be obtained using one of several methods, such as the method of undetermined coefficients or the method of variation of parameters.

The general solution of the original equation is then given by:

```
y(x) = y_c(x) + y_p(x)
```
