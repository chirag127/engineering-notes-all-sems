### Solution by changing independent variable for the notes of the Unit 1 - Ordinary Differential Equation of Higher Order in the subject of ENGINEERING MATHEMATICS-II

- An ordinary differential equation (ODE) is an equation involving an unknown function y = f(x) and one or more of its derivatives.
- A solution of an ODE is an expression of the dependent variable y with reference to the independent variable x, which satisfies the ODE.
- A general solution of an ODE is a solution that contains arbitrary constants, which can take any values.
- A particular solution of an ODE is a solution that satisfies some given boundary conditions or initial conditions, which determine the values of the arbitrary constants.
- Sometimes, an ODE can be solved by changing the independent variable x to a new variable s, and the dependent variable y to a new variable r, such that the ODE becomes simpler or separable.
- For example, consider the homogeneous ODE of the form

`y' = f(y/x)`

where f is a function of y/x only. This ODE can be solved by changing the independent variable to s = ln|x| and the dependent variable to r = y/x, such that

`y = rx` and `y' = r'x + r`

Substituting these into the ODE, we get

`r'x + r = f(r)`

Dividing by x, we get

`r' + r/x = f(r)/x`

This is a separable ODE, which can be solved by integrating both sides with respect to s, since ds = dx/x. We get

`r + C = ∫f(r)ds`

where C is an arbitrary constant. This equation can be solved for r in terms of s, and then y and x can be expressed in terms of r and s, using the original change of variables. This gives the general solution of the ODE in terms of x and y.