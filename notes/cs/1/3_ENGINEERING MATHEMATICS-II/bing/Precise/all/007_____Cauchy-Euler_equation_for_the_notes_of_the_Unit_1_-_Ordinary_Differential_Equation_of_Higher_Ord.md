# Cauchy-Euler Equation

The Cauchy-Euler equation is a type of linear differential equation with variable coefficients. It is also known as the Euler-Cauchy equation or the equidimensional equation. It has the following form:

```
x^2y'' + axy' + by = 0
```

where `a` and `b` are constants.

The Cauchy-Euler equation can be solved using the method of undetermined coefficients. The first step is to assume a solution of the form `y = x^m`, where `m` is a constant. Substituting this into the equation, we get:

```
x^2m(m-1)x^(m-2) + axmx^(m-1) + bx^m = 0
```

Simplifying, we get:

```
x^m(m^2 + (a-1)m + b) = 0
```

Since `x^m` cannot be equal to zero for all values of `x`, we must have:

```
m^2 + (a-1)m + b = 0
```

This is a quadratic equation in `m`, and its roots `m1` and `m2` can be found using the quadratic formula. The general solution to the Cauchy-Euler equation is then given by:

```
y = C1x^(m1) + C2x^(m2)
```

where `C1` and `C2` are constants determined by the initial or boundary conditions of the problem.

In the case where the roots `m1` and `m2` are equal, the general solution is given by:

```
y = (C1 + C2ln(x))x^m
```

In the case where the roots `m1` and `m2` are complex conjugates, the general solution is given by:

```
y = x^a(C1cos(bln(x)) + C2sin(bln(x)))
```

where `a` is the real part of the roots and `b` is the imaginary part.

The Cauchy-Euler equation is commonly encountered in problems involving heat conduction, fluid flow, and electric circuits. It is an important equation in the study of engineering mathematics.