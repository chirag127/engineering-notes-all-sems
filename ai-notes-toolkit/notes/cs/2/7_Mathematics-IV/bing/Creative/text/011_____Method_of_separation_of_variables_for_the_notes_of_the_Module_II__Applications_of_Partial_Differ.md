### Method of separation of variables

- The method of separation of variables is one of the most widely used techniques to solve partial differential equations (PDEs) and is based on the assumption that the solution of the equation is separable, that is, the final solution can be represented as a product of several functions, each of which is only dependent upon a single independent variable .
- The method of separation of variables relies upon the assumption that a function of the form, u(x, t) = φ(x)G(t) will be a solution to a linear homogeneous PDE in x and t. This is called a product solution and provided the boundary conditions are also linear and homogeneous this will also satisfy the boundary conditions.
- The method of separation of variables can be summarized as follows  :
  - Assume that the solution of the PDE is separable, that is, u(x, t) = φ(x)G(t).
  - Substitute the product solution into the PDE and simplify to obtain an equation that involves only one independent variable on each side.
  - Equate each side of the equation to a constant, say -λ, and solve the resulting ordinary differential equations (ODEs) for φ(x) and G(t) separately. This constant is called the separation constant and it can be positive, negative, or zero depending on the problem.
  - Apply the boundary conditions to obtain the possible values of λ and the corresponding eigenfunctions φ(x) and G(t).
  - Use the principle of superposition to construct the general solution of the PDE as a linear combination of the product solutions, that is, u(x, t) = ∑c_nφ_n(x)G_n(t), where c_n are arbitrary constants.
  - Apply the initial condition to determine the values of c_n and obtain the particular solution of the PDE.