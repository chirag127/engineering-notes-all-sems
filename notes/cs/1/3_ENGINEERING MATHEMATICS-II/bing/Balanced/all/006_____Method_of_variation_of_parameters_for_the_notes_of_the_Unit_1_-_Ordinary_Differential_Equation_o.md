# Method of Variation of Parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous linear differential equation of the form Lx(t) = F(t), where L is a linear differential operator, x(t) is the unknown function, and F(t) is a given function.
- The method is based on replacing the constants in the solution of the corresponding homogeneous equation Lx(t) = 0 by functions and determining these functions such that the original equation is satisfied .
- The method can be applied to differential equations of any order, but it is usually easier to use for second-order equations .
- The steps of the method for a second-order equation are as follows :
  - Find the complementary solution x_c(t) of the homogeneous equation Lx(t) = 0 by using the characteristic equation or other methods.
  - Write the complementary solution as x_c(t) = c_1 y_1(t) + c_2 y_2(t), where c_1 and c_2 are constants and y_1(t) and y_2(t) are linearly independent solutions of the homogeneous equation.
  - Assume that the particular solution x_p(t) has the same form as x_c(t), but with c_1 and c_2 replaced by functions u_1(t) and u_2(t), that is, x_p(t) = u_1(t) y_1(t) + u_2(t) y_2(t).
  - Differentiate x_p(t) once and twice to obtain x_p'(t) and x_p''(t).
  - Substitute x_p(t), x_p'(t), and x_p''(t) into the original equation Lx(t) = F(t) and simplify.
  - Use the fact that y_1(t) and y_2(t) are solutions of the homogeneous equation to eliminate some terms and obtain an equation involving only u_1(t), u_2(t), and their derivatives.
  - Impose the condition that u_1'(t) y_1(t) + u_2'(t) y_2(t) = 0, which ensures that x_p(t) and x_c(t) are linearly independent. This condition reduces the equation to a simpler one that can be solved for u_1'(t) and u_2'(t).
  - Integrate u_1'(t) and u_2'(t) to find u_1(t) and u_2(t), using F(t) as the integrand and applying the method of integration by parts if necessary.
  - Substitute u_1(t) and u_2(t) into x_p(t) to obtain the particular solution.
  - Add x_c(t) and x_p(t) to obtain the general solution x(t) = x_c(t) + x_p(t).