### Second order linear differential equations with variable coefficients

In this unit, we will study second order linear differential equations with variable coefficients. These types of equations are commonly used in engineering and physics to model a variety of phenomena.

Here are some key points to keep in mind:

- A second order linear differential equation with variable coefficients can be written in the form:
```
y''(x) + p(x)*y'(x) + q(x)*y(x) = f(x)
```
where `y(x)` is the unknown function, `p(x)` and `q(x)` are variable coefficients, and `f(x)` is a given function.

- The characteristic equation of the differential equation is given by:
```
r^2 + p(x)*r + q(x) = 0
```
where `r` is a constant.

- Depending on the roots of the characteristic equation, the general solution of the differential equation can take different forms. These forms include:
  - Two distinct real roots: `y(x) = c1*e^(r1*x) + c2*e^(r2*x)`
  - One repeated real root: `y(x) = (c1 + c2*x)*e^(r*x)`
  - Two complex roots: `y(x) = e^(a*x)*(c1*cos(b*x) + c2*sin(b*x))`

- In some cases, the variable coefficients `p(x)` and `q(x)` can be simplified to constant coefficients by using a change of variables. This allows us to solve the differential equation using the methods we learned in earlier units.

- The method of undetermined coefficients can be used to find a particular solution to the differential equation when the right-hand side `f(x)` is a polynomial, an exponential function, or a trigonometric function.

- The method of variation of parameters can be used to find the general solution to the differential equation when the right-hand side `f(x)` is a more general function.

By understanding these key points and practicing solving problems, you will be able to successfully solve second order linear differential equations with variable coefficients in engineering and physics applications.