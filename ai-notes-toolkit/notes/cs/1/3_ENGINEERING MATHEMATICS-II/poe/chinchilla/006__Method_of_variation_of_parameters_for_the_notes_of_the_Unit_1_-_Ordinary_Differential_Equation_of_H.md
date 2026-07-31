### Method of Variation of Parameters for Unit 1 - Ordinary Differential Equations of Higher Order

In this section, we will discuss the method of variation of parameters, which is used to solve non-homogeneous linear differential equations of higher order.

#### 1. Introduction

The method of variation of parameters is an extension of the method of undetermined coefficients. It is used to find a particular solution to a non-homogeneous linear differential equation of the form:

```
y''(x) + p(x) y'(x) + q(x) y(x) = r(x)
```

where `p(x)`, `q(x)`, and `r(x)` are continuous functions.

#### 2. Steps Involved

The following are the steps involved in using the method of variation of parameters to find a particular solution to the differential equation:

1. Find the complementary solution `y_c(x)` to the homogeneous equation `y''(x) + p(x) y'(x) + q(x) y(x) = 0`.

2. Assume that the particular solution has the form `y_p(x) = u_1(x) y_1(x) + u_2(x) y_2(x)`, where `y_1(x)` and `y_2(x)` are linearly independent solutions of the homogeneous equation, and `u_1(x)` and `u_2(x)` are functions to be determined.

3. Calculate `y_p'(x)` and `y_p''(x)`.

4. Substitute `y_p(x)`, `y_p'(x)`, and `y_p''(x)` into the differential equation and simplify.

5. Equate coefficients of `y_1(x)` and `y_2(x)` to zero to obtain two ordinary differential equations for `u_1(x)` and `u_2(x)`.

6. Solve the two differential equations for `u_1(x)` and `u_2(x)`.

7. Substitute `u_1(x)` and `u_2(x)` into the particular solution `y_p(x)`.

8. The general solution to the differential equation is `y(x) = y_c(x) + y_p(x)`.

#### 3. Example

Consider the differential equation:

```
y''(x) + 2y'(x) + y(x) = x^2
```

The homogeneous equation is `y''(x) + 2y'(x) + y(x) = 0`, which has the complementary solution `y_c(x) = c_1 e^{-x} + c_2 x e^{-x}`.

We can assume that the particular solution has the form `y_p(x) = u_1(x) e^{-x} + u_2(x) x e^{-x}`.

Taking derivatives, we have:

```
y_p'(x) = -u_1(x) e^{-x} + u_2(x) e^{-x} - u_2(x) x e^{-x}
y_p''(x) = u_1(x) e^{-x} - 2u_2(x) e^{-x} + u_2(x) x e^{-x}
```

Substituting these into the differential equation gives:

```
u_1(x) e^{-x} - 2u_2(x) e^{-x} + u_2(x) x e^{-x} + 2(-u_1(x) e^{-x} + u_2(x) e^{-x} - u_2(x) x e^{-x}) + (u_1(x) e^{-x} + u_2(x) x e^{-x}) = x^2
```

Simplifying, we get:

```
u_1(x) = -\frac{x^2}{2} e^x
u_2(x) = \frac{x^3}{3} e^x
```

Therefore, the particular solution is:

```
y_p(x) = -\frac{x^2}{2} e^{-x} + \frac{x^3}{3} e^{-x}
```

The general solution is then:

```
y(x) = c_1 e^{-x} + c_2 x e^{-x} - \frac{x^2}{2} e^{-x} + \frac{x^3}{3} e^{-x}
```

#### 4. Conclusion

The method of variation of parameters is a powerful technique for solving non-homogeneous linear differential equations of higher order. By assuming a particular solution with unknown coefficients and using the method of equating coefficients, we can determine the coefficients and obtain the general solution.