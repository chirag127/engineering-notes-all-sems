## Unit 1 - Ordinary Differential Equation of Higher Order

An ordinary differential equation (ODE) is an equation that involves one or more derivatives of an unknown function with respect to a single independent variable. The order of an ODE is the highest order of the derivatives that appear in the equation. For example, the following ODE is of order 2:

`y'' + 2y' - 3y = 0`

A solution of an ODE is a function that satisfies the equation. The general solution of an ODE is the most general form of the solution that contains arbitrary constants. The particular solution of an ODE is a specific solution that is obtained by assigning values to the arbitrary constants. For example, the general solution of the above ODE is:

`y = c1 e^(-3x) + c2 e^x`

where `c1` and `c2` are arbitrary constants. A particular solution of the above ODE is:

`y = 2 e^(-3x) - e^x`

where `c1 = 2` and `c2 = -1`.

The degree of an ODE is the power of the highest order derivative that appears in the equation. For example, the following ODE is of degree 3:

`(y'')^3 + y' - y = 0`

An ODE is linear if it can be written in the form:

`a_n(x) y^(n) + a_(n-1)(x) y^(n-1) + ... + a_1(x) y' + a_0(x) y = b(x)`

where `a_n(x), a_(n-1)(x), ..., a_0(x), b(x)` are given functions of `x`, and `y^(n)` denotes the `n`-th derivative of `y` with respect to `x`. An ODE is nonlinear if it is not linear. For example, the following ODE is nonlinear:

`y'' + y^2 = 0`

An ODE is homogeneous if it can be written in the form:

`a_n(x) y^(n) + a_(n-1)(x) y^(n-1) + ... + a_1(x) y' + a_0(x) y = 0`

where `a_n(x), a_(n-1)(x), ..., a_0(x)` are given functions of `x`. An ODE is nonhomogeneous if it is not homogeneous. For example, the following ODE is nonhomogeneous:

`y'' + 2y' - 3y = x`

An ODE is autonomous if it does not depend explicitly on the independent variable. For example, the following ODE is autonomous:

`y' = y - y^2`

An ODE is nonautonomous if it depends explicitly on the independent variable. For example, the following ODE is nonautonomous:

`y' = y - x`

The methods of solving ODEs of higher order depend on the type and characteristics of the equation. Some of the common methods are:

- Reduction of order: This method reduces an ODE of order `n` to an ODE of order `n-1` by substituting a new dependent variable that is a function of the original dependent variable and its derivatives.
- Variation of parameters: This method finds a particular solution of a nonhomogeneous linear ODE by assuming that the arbitrary constants in the general solution of the corresponding homogeneous linear ODE are functions of the independent variable and then solving for them.
- Undetermined coefficients: This method finds a particular solution of a nonhomogeneous linear ODE by assuming that the solution has the same form as the nonhomogeneous term and then solving for the undetermined coefficients.
- Power series: This method finds a solution of an ODE by assuming that the solution can be expressed as a power series and then finding the coefficients of the series by substituting it into the equation and equating the coefficients of the same powers of the independent variable.
- Laplace transform: This method transforms an ODE into an algebraic equation by applying the Laplace transform to both sides of the equation and then solving for the transformed function and applying the inverse Laplace transform to obtain the solution.