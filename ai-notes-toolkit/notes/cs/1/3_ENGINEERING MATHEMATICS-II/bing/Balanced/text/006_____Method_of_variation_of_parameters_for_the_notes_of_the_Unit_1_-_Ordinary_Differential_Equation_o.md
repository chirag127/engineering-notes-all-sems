### Method of variation of parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous differential equation of the form Lx(t) = F(t), where L is a linear differential operator, x(t) is the unknown function, and F(t) is a given function.
- The method involves replacing the constants in the solution of the homogeneous equation Lx(t) = 0 by functions and determining these functions such that the original equation is satisfied .
- The method of variation of parameters can be applied to differential equations of any order, but it is most commonly used for second-order equations.
- The steps of the method for a second-order equation are as follows :
  - Find the complementary solution x_c(t) of the homogeneous equation Lx(t) = 0 by using the characteristic equation or other methods.
  - Find two linearly independent solutions y_1(t) and y_2(t) of the homogeneous equation, which form a fundamental set of solutions.
  - Assume that the particular solution x_p(t) has the form x_p(t) = u_1(t)y_1(t) + u_2(t)y_2(t), where u_1(t) and u_2(t) are unknown functions to be determined.
  - Substitute x_p(t) and its derivatives into the original equation and simplify to obtain an equation involving u_1(t), u_2(t) and their derivatives.
  - Use the condition that u_1'(t)y_1(t) + u_2'(t)y_2(t) = 0 to eliminate one of the unknown functions and obtain a single equation for the other function.
  - Solve the equation for the unknown function and integrate to find its general form.
  - Use the condition that u_1'(t)y_1'(t) + u_2'(t)y_2'(t) = F(t) to find the other unknown function by substituting the first function and integrating.
  - Substitute the functions u_1(t) and u_2(t) into the form of x_p(t) to obtain the particular solution.
  - Add the complementary solution and the particular solution to obtain the general solution of the non-homogeneous equation.