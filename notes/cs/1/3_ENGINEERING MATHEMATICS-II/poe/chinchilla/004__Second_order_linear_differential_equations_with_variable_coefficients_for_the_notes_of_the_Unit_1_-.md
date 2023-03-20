### Second Order Linear Differential Equations with Variable Coefficients

In the study of ordinary differential equations of higher order, second-order linear differential equations with variable coefficients play a crucial role. These types of equations can be expressed in the following form:

```math
y''(x) + p(x)y'(x) + q(x)y(x) = f(x)
```

where `p(x)` and `q(x)` are continuous functions of `x`, and `f(x)` is a given function.

Here are some important points to consider when dealing with second-order linear differential equations with variable coefficients:

- To solve this type of equation, we need to find a particular solution `y_p(x)` of the non-homogeneous equation and the general solution `y_c(x)` of the corresponding homogeneous equation.

- The homogeneous equation is obtained by setting `f(x) = 0` in the original equation. The corresponding characteristic equation is:

```math
r^2 + p(x)r + q(x) = 0
```

- The solutions of the characteristic equation determine the form of the general solution `y_c(x)` of the homogeneous equation. There are three possible cases:

  - **Distinct real roots**: If the characteristic equation has two distinct real roots `r_1` and `r_2`, then the general solution of the homogeneous equation is:

  ```math
  y_c(x) = c_1e^{r_1x} + c_2e^{r_2x}
  ```

  where `c_1` and `c_2` are constants.

  - **Repeated real roots**: If the characteristic equation has a repeated real root `r`, then the general solution of the homogeneous equation is:

  ```math
  y_c(x) = c_1e^{rx} + c_2xe^{rx}
  ```

  where `c_1` and `c_2` are constants.

  - **Complex roots**: If the characteristic equation has two complex conjugate roots `a ± bi`, then the general solution of the homogeneous equation is:

  ```math
  y_c(x) = e^{ax}(c_1\cos bx + c_2\sin bx)
  ```

  where `c_1` and `c_2` are constants.

- To find a particular solution `y_p(x)` of the non-homogeneous equation, we use the method of undetermined coefficients or the variation of parameters method.

- The method of undetermined coefficients is used when `f(x)` is a polynomial, exponential, sine, cosine, or a linear combination of these functions. This method involves guessing a particular solution `y_p(x)` that has the same form as `f(x)`.

- The variation of parameters method is used when `f(x)` is a more general function. This method involves finding a particular solution `y_p(x)` that has the form:

```math
y_p(x) = u_1(x)y_1(x) + u_2(x)y_2(x)
```

where `y_1(x)` and `y_2(x)` are linearly independent solutions of the corresponding homogeneous equation, and `u_1(x)` and `u_2(x)` are functions that need to be determined.

- Once we have found the particular solution `y_p(x)` and the general solution `y_c(x)`, the general solution of the non-homogeneous equation is:

```math
y(x) = y_c(x) + y_p(x)
```

- The constants in the general solution can be determined by applying initial or boundary conditions.

In summary, second-order linear differential equations with variable coefficients are an important topic in the study of ordinary differential equations of higher order. By understanding the methods of solving these equations, we can apply them to various real-world problems in engineering, physics, and other fields.