### Method of Variation of Parameters

The method of variation of parameters is a technique used to find particular solutions to non-homogeneous ordinary differential equations of higher order. This method is used when the non-homogeneous term is not of a form that can be easily solved using the method of undetermined coefficients.

Here are the steps to apply the method of variation of parameters to a non-homogeneous ordinary differential equation of the form y'' + p(x)y' + q(x)y = r(x):

1. Find the complementary solution, yc, by solving the associated homogeneous equation y'' + p(x)y' + q(x)y = 0.
2. Assume a particular solution of the form yp = u1(x)y1 + u2(x)y2, where y1 and y2 are two linearly independent solutions to the homogeneous equation, and u1 and u2 are unknown functions to be determined.
3. Differentiate yp to obtain yp' = u1'y1 + u1y1' + u2'y2 + u2y2'.
4. Substitute yp and yp' into the non-homogeneous equation to obtain an equation in terms of u1', u2', and their products with y1, y1', y2, and y2'.
5. Solve for u1' and u2' by equating the coefficients of y1 and y2 to zero.
6. Integrate u1' and u2' to find u1 and u2.
7. Substitute u1 and u2 into the assumed form of yp to obtain the particular solution.

This method can be extended to higher-order non-homogeneous ordinary differential equations by assuming a particular solution of the form yp = u1(x)y1 + u2(x)y2 + ... + un(x)yn, where y1, y2, ..., yn are n linearly independent solutions to the associated homogeneous equation, and u1, u2, ..., un are unknown functions to be determined.

This is a brief overview of the method of variation of parameters for solving non-homogeneous ordinary differential equations of higher order. It is an important topic in the subject of Engineering Mathematics-II, particularly in the unit on Ordinary Differential Equations of Higher Order. It is recommended to practice solving problems using this method to gain a better understanding of the concept.