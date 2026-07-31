# Method of Variation of Parameters

The method of variation of parameters is a technique used to find particular solutions to non-homogeneous ordinary differential equations of higher order. This method is used when the non-homogeneous term is not of a form that can be easily solved using the method of undetermined coefficients.

Here are the steps to follow when using the method of variation of parameters:

1. Find the complementary solution to the associated homogeneous equation.
2. Assume that the particular solution is of the form yp = u1y1 + u2y2 + ... + unyn, where y1, y2, ..., yn are the n linearly independent solutions to the associated homogeneous equation.
3. Find the Wronskian of y1, y2, ..., yn.
4. Solve for u1, u2, ..., un using the formula ui' = (-1)^(i+1) * f(x) * W(i) / W, where f(x) is the non-homogeneous term, W is the Wronskian of y1, y2, ..., yn, and W(i) is the Wronskian of y1, y2, ..., yn with the ith column replaced by [0, 0, ..., 1]^T.
5. Integrate ui' to find ui.
6. Substitute ui into the assumed form of the particular solution to find the particular solution.

This method can be applied to solve non-homogeneous ordinary differential equations of higher order in the subject of Engineering Mathematics-II. It is an important topic in Unit 1 - Ordinary Differential Equation of Higher Order. It is recommended to practice solving problems using this method to gain a better understanding of the topic.