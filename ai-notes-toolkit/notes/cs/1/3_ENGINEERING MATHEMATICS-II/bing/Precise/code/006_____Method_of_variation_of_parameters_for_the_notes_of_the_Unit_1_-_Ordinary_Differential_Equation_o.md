### Method of Variation of Parameters

The method of variation of parameters is a technique used to find particular solutions to non-homogeneous ordinary differential equations of higher order. This method is used when the non-homogeneous term is not of a form that can be easily solved using the method of undetermined coefficients.

Here are the steps to apply the method of variation of parameters to a non-homogeneous linear differential equation of the form y'' + p(x)y' + q(x)y = r(x):

1. Find the complementary solution, yc, by solving the associated homogeneous equation y'' + p(x)y' + q(x)y = 0.
2. Assume a particular solution of the form yp = u1(x)y1 + u2(x)y2, where y1 and y2 are two linearly independent solutions of the associated homogeneous equation.
3. Find u1 and u2 by solving the system of equations obtained by substituting yp into the original non-homogeneous equation and its derivative.
4. The particular solution is given by yp = u1(x)y1 + u2(x)y2.
5. The general solution to the non-homogeneous equation is given by y = yc + yp.

This method can be extended to higher-order linear differential equations in a similar manner. The key is to assume a particular solution of the form yp = u1(x)y1 + u2(x)y2 + ... + un(x)yn, where y1, y2, ..., yn are n linearly independent solutions of the associated homogeneous equation, and then solve for u1, u2, ..., un.