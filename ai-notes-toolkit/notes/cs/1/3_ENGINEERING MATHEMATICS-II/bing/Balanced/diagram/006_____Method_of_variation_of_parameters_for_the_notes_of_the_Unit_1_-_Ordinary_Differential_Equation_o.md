### Method of variation of parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous differential equation of the form L(x) = F(t), where L is a linear differential operator and F is a given function.
- The method involves replacing the constants in the solution of the homogeneous equation L(x) = 0 by functions and determining these functions such that the original equation L(x) = F(t) is satisfied .
- The method of variation of parameters can be applied to differential equations of any order, but it is most commonly used for second-order equations.
- The steps of the method for a second-order equation are as follows :
  - Find the complementary solution x_c of the homogeneous equation L(x) = 0 by using the characteristic equation or other methods.
  - Assume a particular solution x_p of the form x_p = u_1 y_1 + u_2 y_2, where y_1 and y_2 are the fundamental solutions of the homogeneous equation and u_1 and u_2 are unknown functions to be determined.
  - Substitute x_p and its derivatives into the original equation L(x) = F(t) and simplify.
  - Use the condition that u'_1 y_1 + u'_2 y_2 = 0 to eliminate one of the unknown functions and obtain a single equation for the other function.
  - Solve the equation for u'_1 or u'_2 and integrate to find u_1 or u_2.
  - Repeat the same steps for the other unknown function using the condition that u'_1 y'_1 + u'_2 y'_2 = F(t).
  - Substitute the values of u_1 and u_2 into x_p and simplify to obtain the particular solution.
  - Add the complementary solution and the particular solution to get the general solution of the non-homogeneous equation.