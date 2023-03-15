### Linear differential equation of nth order with constant coefficients for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

A linear differential equation of nth order with constant coefficients is an equation of the form:

```
a_n y^(n) + a_(n-1) y^(n-1) + ... + a_1 y' + a_0 y = f(x)
```

where `a_n, a_(n-1), ..., a_1, a_0` are constants, `y^(n)` denotes the nth derivative of `y` with respect to `x`, and `f(x)` is a given function of `x`.

The general solution of such an equation can be written as the sum of the complementary function `y_c(x)` and a particular solution `y_p(x)`:

```
y(x) = y_c(x) + y_p(x)
```

The complementary function `y_c(x)` is the general solution of the corresponding homogeneous equation:

```
a_n y^(n) + a_(n-1) y^(n-1) + ... + a_1 y' + a_0 y = 0
```

The particular solution `y_p(x)` can be found using one of several methods, such as the method of undetermined coefficients or the method of variation of parameters.

The characteristic equation of the homogeneous equation is given by:

```
a_n r^n + a_(n-1) r^(n-1) + ... + a_1 r + a_0 = 0
```

The roots of the characteristic equation determine the form of the complementary function `y_c(x)`. If all the roots are distinct, then the complementary function is given by:

```
y_c(x) = C_1 e^(r_1 x) + C_2 e^(r_2 x) + ... + C_n e^(r_n x)
```

where `r_1, r_2, ..., r_n` are the distinct roots of the characteristic equation and `C_1, C_2, ..., C_n` are arbitrary constants.

If some of the roots are repeated, then the complementary function will contain additional terms involving powers of `x` multiplied by exponential functions. For example, if the root `r` has multiplicity `k`, then the complementary function will contain the terms:

```
C_1 e^(r x) + C_2 x e^(r x) + ... + C_k x^(k-1) e^(r x)
```

where `C_1, C_2, ..., C_k` are arbitrary constants.

Once the complementary function `y_c(x)` has been found, the particular solution `y_p(x)` can be determined using one of the methods mentioned above. The general solution of the non-homogeneous equation is then given by the sum of the complementary function and the particular solution.