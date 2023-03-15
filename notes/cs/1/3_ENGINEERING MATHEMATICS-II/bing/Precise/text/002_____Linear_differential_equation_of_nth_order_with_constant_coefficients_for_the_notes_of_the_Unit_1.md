### Linear differential equation of nth order with constant coefficients

A linear differential equation of nth order with constant coefficients is a differential equation of the form:

a_n y^(n) + a_(n-1) y^(n-1) + ... + a_1 y' + a_0 y = f(x)

where a_n, a_(n-1), ..., a_1, a_0 are constants, y^(n) denotes the nth derivative of y with respect to x, and f(x) is a given function of x.

The general solution of such an equation can be written as the sum of the complementary function and a particular integral. The complementary function is the general solution of the corresponding homogeneous equation:

a_n y^(n) + a_(n-1) y^(n-1) + ... + a_1 y' + a_0 y = 0

The particular integral is a particular solution of the non-homogeneous equation, which can be found using methods such as undetermined coefficients or variation of parameters.

The characteristic equation of the homogeneous equation is given by:

a_n r^n + a_(n-1) r^(n-1) + ... + a_1 r + a_0 = 0

The roots of the characteristic equation determine the form of the complementary function. If all the roots are distinct, the complementary function is given by:

y_c = c_1 e^(r_1 x) + c_2 e^(r_2 x) + ... + c_n e^(r_n x)

where c_1, c_2, ..., c_n are arbitrary constants and r_1, r_2, ..., r_n are the roots of the characteristic equation.

If some of the roots are repeated, the complementary function will contain terms of the form x^k e^(r x), where k is a non-negative integer and r is a repeated root.

Once the complementary function and the particular integral have been found, the general solution of the non-homogeneous equation can be written as:

y = y_c + y_p

where y_c is the complementary function and y_p is the particular integral.