## Unit 1 - Ordinary Differential Equation of Higher Order

- An ordinary differential equation (ODE) is an equation that involves one or more derivatives of an unknown function with respect to a single independent variable.
- The order of an ODE is the order of the highest derivative that occurs in the equation.
- The general form of an n-th order ODE is given as:

`F(x, y, y', ..., y^(n)) = 0`

where `y'` can be either `dy/dx` or `dy/dt` and `y^(n)` can be either `d^(n)y/dx^(n)` or `d^(n)y/dt^(n)`.

- A solution of an ODE is a function that satisfies the equation for all values of the independent variable in a given interval.
- A general solution of an ODE is a solution that contains n arbitrary constants, where n is the order of the equation.
- A particular solution of an ODE is a solution that is obtained by assigning specific values to the arbitrary constants in the general solution.
- An initial value problem (IVP) is a problem of finding a particular solution of an ODE that satisfies some given initial conditions, such as the values of the function and its derivatives at a certain point.
- A linear ODE is an ODE that can be written in the form:

`a_0(x)y^(n) + a_1(x)y^(n-1) + ... + a_n(x)y = g(x)`

where `a_0(x)`, `a_1(x)`, ..., `a_n(x)` and `g(x)` are known functions of x.

- A homogeneous linear ODE is a linear ODE with `g(x) = 0`.
- A nonhomogeneous linear ODE is a linear ODE with `g(x) ≠ 0`.
- A linear ODE is said to have constant coefficients if all the functions `a_0(x)`, `a_1(x)`, ..., `a_n(x)` are constants.
- A linear ODE is said to have variable coefficients if at least one of the functions `a_0(x)`, `a_1(x)`, ..., `a_n(x)` is not constant.

- The general solution of a homogeneous linear ODE of order n is given by:

`y = c_1y_1 + c_2y_2 + ... + c_ny_n`

where `c_1`, `c_2`, ..., `c_n` are arbitrary constants and `y_1`, `y_2`, ..., `y_n` are n linearly independent solutions of the equation.

- The general solution of a nonhomogeneous linear ODE of order n is given by:

`y = y_h + y_p`

where `y_h` is the general solution of the corresponding homogeneous equation and `y_p` is a particular solution of the nonhomogeneous equation.

- There are various methods to find the general solution or a particular solution of a linear ODE, such as:

  - The method of undetermined coefficients, which is applicable to nonhomogeneous linear ODEs with constant coefficients and `g(x)` being a polynomial, exponential, trigonometric, or a linear combination of these functions.
  - The method of variation of parameters, which is applicable to nonhomogeneous linear ODEs with variable coefficients or `g(x)` being any function.
  - The method of power series, which is applicable to linear ODEs with variable coefficients or `g(x)` being any function, provided that the equation has a power series solution in a certain interval.
  - The method of Laplace transform, which is applicable to linear ODEs with constant coefficients and `g(x)` being any function that has a Laplace transform, provided that the equation has a solution that is piecewise continuous and of exponential order.

- Some examples of higher order ODEs and their applications are:

  - The equation of motion of a simple harmonic oscillator, which is a second order homogeneous linear ODE with constant coefficients:

  `y'' + ω^2y = 0`

  where `y` is the displacement of the oscillator, `ω` is the angular frequency, and `y''` is the acceleration.

  - The equation of motion of a damped harmonic oscillator, which is a second order nonhomogeneous linear ODE with constant coefficients:

  `y'' + 2by' + ω^2y = F(t)`

  where `y` is the displacement of the

Some possible mnemonics and learning tricks for the topic are:

- To remember the general form of a linear ODE, you can use the acronym LAGS, which stands for Linear, Additive, General, and Standard. Linear means that the equation is linear in y and its derivatives, Additive means that the equation can be written as a sum of terms, General means that the equation has n arbitrary constants in the general solution, and Standard means that the equation has the highest order derivative on the left and the rest of the terms on the right.

- To remember the general solution of a homogeneous linear ODE, you can use the phrase "A homogeneous equation has a homogeneous solution", which means that the general solution is a linear combination of n linearly independent solutions, where n is the order of the equation.

- To remember the general solution of a nonhomogeneous linear ODE, you can use the phrase "A nonhomogeneous equation has a nonhomogeneous solution", which means that the general solution is the sum of the general solution of the corresponding homogeneous equation and a particular solution of the nonhomogeneous equation.

- To remember the method of undetermined coefficients, you can use the acronym GUESS, which stands for Guess, Use, Equate, Solve, and Substitute. Guess means that you guess a form of the particular solution based on the form of g(x), Use means that you use the guessed solution in the equation, Equate means that you equate the coefficients of the same terms on both sides of the equation, Solve means that you solve for the unknown coefficients, and Substitute means that you substitute the values of the coefficients in the guessed solution.

- To remember the method of variation of parameters, you can use the acronym VARY, which stands for Vary, Apply, Reduce, and Yield. Vary means that you vary the constants in the general solution of the homogeneous equation to make them functions of x, Apply means that you apply the product rule to the derivatives of the varied solution, Reduce means that you reduce the equation to a system of linear equations by setting the coefficients of y and y' to zero, and Yield means that you yield the particular solution by solving the system and integrating the functions.

- To remember the method of power series, you can use the acronym POWER, which stands for Power, Obtain, Write, Equate, and Recur. Power means that you assume a power series solution of the form y = Σa_nx^n, Obtain means that you obtain the derivatives of the power series by differentiating term by term, Write means that you write the equation in terms of the power series and their derivatives, Equate means that you equate the coefficients of the same powers of x on both sides of the equation, and Recur means that you recur to a recurrence relation that relates the coefficients a_n to each other.

- To remember the method of Laplace transform, you can use the acronym LAPS, which stands for Laplace, Apply, Partial, and Solve. Laplace means that you take the Laplace transform of both sides of the equation, Apply means that you apply the properties of the Laplace transform to simplify the equation, Partial means that you use partial fraction decomposition to split the equation into simpler fractions, and Solve means that you use the inverse Laplace transform to find the solution.