### Method of variation of parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous differential equation of the form `L(y) = f(x)`, where `L` is a linear differential operator, by replacing the constants in the solution of the corresponding homogeneous equation by functions and determining these functions such that the original equation is satisfied .
- The method of variation of parameters can be applied to differential equations of any order, but it is usually easier to use for second-order equations  .
- The method of variation of parameters involves the following steps:
  - Find the complementary solution `y_c` of the homogeneous equation `L(y) = 0` by using the characteristic equation or other methods.
  - Assume that the particular solution `y_p` has the form `y_p = u_1 y_1 + u_2 y_2`, where `y_1` and `y_2` are two linearly independent solutions of the homogeneous equation, and `u_1` and `u_2` are unknown functions to be determined.
  - Impose the condition that `u_1' y_1 + u_2' y_2 = 0`, which ensures that `y_p` is linearly independent of `y_c`.
  - Substitute `y_p` and its derivatives into the original equation and solve for `u_1'` and `u_2'`.
  - Integrate `u_1'` and `u_2'` to obtain `u_1` and `u_2`.
  - Substitute `u_1` and `u_2` into `y_p` to obtain the particular solution.
  - Add `y_c` and `y_p` to obtain the general solution `y = y_c + y_p`.
- The method of variation of parameters can be extended to higher-order equations by using the Wronskian determinant and matrix methods.