### Method of separation of variables

- The method of separation of variables is one of the most widely used techniques to solve partial differential equations (PDEs) and is based on the assumption that the solution of the equation is separable, that is, the final solution can be represented as a product of several functions, each of which is only dependent upon a single independent variable .
- The method of separation of variables relies upon the assumption that a function of the form, u(x, t) = φ(x)G(t) will be a solution to a linear homogeneous PDE in x and t. This is called a product solution and provided the boundary conditions are also linear and homogeneous this will also satisfy the boundary conditions.
- The method of separation of variables is to try to find solutions that are sums or products of functions of one variable. For example, for the heat equation, we try to find solutions of the form u(x, t) = X(x)T(t). That the desired solution we are looking for is of this form is too much to hope for.
- To recap, here are three simple steps to solve a PDE using separation of variables:
  - Separate the variables of the equation so that all the terms involving one variable are on one side of the equation and all the terms involving the other variable are on the other side of the equation.
  - Integrate each side of the equation with respect to the variable present on that side. Don’t forget to add the constant of integration to one side of the equation.
  - Simplify where necessary and apply the boundary conditions to find the unknown constants and functions.