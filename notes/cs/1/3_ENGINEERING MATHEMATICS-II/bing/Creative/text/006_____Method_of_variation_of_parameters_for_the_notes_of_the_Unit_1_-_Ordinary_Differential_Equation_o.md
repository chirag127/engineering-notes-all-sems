### Method of variation of parameters

- The method of variation of parameters is a general method to find a particular solution of a non-homogeneous linear differential equation of any order by replacing the constants in the solution of the corresponding homogeneous equation by functions and determining these functions such that the original differential equation is satisfied .
- The method is based on the idea that if y1 and y2 are two linearly independent solutions of the homogeneous equation L(y) = 0, then any solution of the non-homogeneous equation L(y) = f(x) can be written as y = u1y1 + u2y2, where u1 and u2 are unknown functions of x  .
- To find u1 and u2, we substitute y = u1y1 + u2y2 and its derivatives into the non-homogeneous equation and use the fact that y1 and y2 are solutions of the homogeneous equation to simplify the resulting expression. We then obtain a system of two equations for u1 and u2, which can be solved by using the Wronskian of y1 and y2  .
- The Wronskian of y1 and y2 is defined as W(y1,y2) = y1y2' - y1'y2, where the prime denotes differentiation with respect to x. The Wronskian is a measure of the linear independence of y1 and y2, and it is nonzero if and only if y1 and y2 are linearly independent  .
- The solution of the system of equations for u1 and u2 is given by:

u1 = - ∫ (y2f(x)/W(y1,y2)) dx

u2 = ∫ (y1f(x)/W(y1,y2)) dx

where the integration constants are chosen to be zero for simplicity  .

- The particular solution of the non-homogeneous equation is then given by:

y = u1y1 + u2y2

= -y1 ∫ (y2f(x)/W(y1,y2)) dx + y2 ∫ (y1f(x)/W(y1,y2)) dx



- The method of variation of parameters can be extended to higher-order differential equations by using more linearly independent solutions of the homogeneous equation and more unknown functions of x.