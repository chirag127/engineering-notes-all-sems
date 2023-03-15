# Method of variation of parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous linear differential equation of the form `Lx(t) = F(t)`, where `L` is a linear differential operator, `x(t)` is the unknown function, and `F(t)` is a given function.
- The method is based on the idea of replacing the constants in the solution of the corresponding homogeneous equation `Lx(t) = 0` by functions and determining these functions such that the original equation is satisfied .
- The method can be applied to differential equations of any order, but it is most commonly used for second-order equations of the form `a(x)y'' + b(x)y' + c(x)y = f(x)`, where `a(x)`, `b(x)`, `c(x)`, and `f(x)` are continuous functions and `a(x) != 0`.
- The steps of the method for second-order equations are as follows :
  - Find the complementary solution `yc(x)` of the homogeneous equation `a(x)y'' + b(x)y' + c(x)y = 0` by using the characteristic equation or other methods.
  - Find two linearly independent solutions `y1(x)` and `y2(x)` of the homogeneous equation, such that `yc(x) = c1y1(x) + c2y2(x)`, where `c1` and `c2` are constants.
  - Assume that the particular solution `yp(x)` of the non-homogeneous equation has the form `yp(x) = u1(x)y1(x) + u2(x)y2(x)`, where `u1(x)` and `u2(x)` are unknown functions to be determined.
  - Substitute `yp(x)` and its derivatives into the non-homogeneous equation and use the fact that `y1(x)` and `y2(x)` are solutions of the homogeneous equation to simplify the equation.
  - Use the condition that `u1'(x)y1(x) + u2'(x)y2(x) = 0` to eliminate one of the unknown functions and obtain an equation involving only the other unknown function and its derivative.
  - Solve this equation for the unknown function and integrate it to find its expression.
  - Repeat the same process for the other unknown function and integrate it to find its expression.
  - Substitute the expressions for `u1(x)` and `u2(x)` into the assumed form of `yp(x)` and simplify it to obtain the particular solution.
  - Add the complementary solution and the particular solution to get the general solution of the non-homogeneous equation.