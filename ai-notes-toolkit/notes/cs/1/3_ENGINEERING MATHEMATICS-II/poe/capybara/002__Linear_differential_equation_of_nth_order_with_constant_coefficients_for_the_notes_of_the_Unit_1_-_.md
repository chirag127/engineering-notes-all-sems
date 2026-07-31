### Linear Differential Equation of nth Order with Constant Coefficients

Ordinary Differential Equations (ODEs) are important in many fields of engineering and science. In this unit, we will focus on solving linear differential equations of higher order with constant coefficients.

#### Definition

A linear differential equation of nth order with constant coefficients is an equation of the form:

```
a_n y^(n) + a_(n-1) y^(n-1) + ... + a_1 y' + a_0 y = f(x)
```

where `y` is a function of `x`, `a_0, a_1, ..., a_n` are constants, and `f(x)` is a given function.

#### Solving Method

The general method for solving linear differential equations of nth order with constant coefficients involves finding the roots of the characteristic equation:

```
a_n r^n + a_(n-1) r^(n-1) + ... + a_1 r + a_0 = 0
```

The roots of the characteristic equation determine the form of the general solution of the differential equation.

The general solution can be expressed as:

```
y(x) = c_1 e^(r_1 x) + c_2 e^(r_2 x) + ... + c_n e^(r_n x) + y_p(x)
```

where `c_1, c_2, ..., c_n` are constants determined by the initial or boundary conditions, `r_1, r_2, ..., r_n` are the roots of the characteristic equation, and `y_p(x)` is a particular solution that satisfies the differential equation.

#### Examples

Let's consider some examples to illustrate the method of solving linear differential equations of nth order with constant coefficients.

##### Example 1

```
y'' - 4y' + 4y = e^(2x)
```

The characteristic equation is:

```
r^2 - 4r + 4 = 0
```

which has a repeated root `r = 2`.

The general solution is:

```
y(x) = c_1 e^(2x) + c_2 x e^(2x) + e^(2x)
```

where `c_1` and `c_2` are constants determined by the initial conditions.

##### Example 2

```
y''' - 3y'' + 3y' - y = 2x^2 - 1
```

The characteristic equation is:

```
r^3 - 3r^2 + 3r - 1 = 0
```

which has three roots `r = 1` (with multiplicity 3).

The general solution is:

```
y(x) = c_1 e^x + c_2 x e^x + c_3 x^2 e^x + x^2 - 2x - 1
```

where `c_1`, `c_2`, and `c_3` are constants determined by the initial conditions.

#### Conclusion

Linear differential equations of nth order with constant coefficients can be solved using the method of finding the roots of the characteristic equation. The general solution can be expressed as a linear combination of exponential functions and a particular solution that satisfies the differential equation.