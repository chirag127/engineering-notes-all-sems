### Partial derivatives

- A partial derivative is a derivative where we hold some variables constant and differentiate with respect to one variable .
- For example, if f(x,y) is a function of two variables, then the partial derivative of f with respect to x is denoted by f_x(x,y) or ∂f/∂x and is obtained by treating y as a constant and differentiating f with respect to x .
- Similarly, the partial derivative of f with respect to y is denoted by f_y(x,y) or ∂f/∂y and is obtained by treating x as a constant and differentiating f with respect to y .
- Partial derivatives can be used to find the slope of a surface in a given direction, the rate of change of a function with respect to one variable, and the optimization of multivariable functions .
- Partial derivatives can be calculated using the same rules and formulas as ordinary derivatives, such as the power rule, the product rule, the quotient rule, and the chain rule .
- Partial derivatives can also be combined to form higher-order derivatives, such as the second partial derivative, which is the partial derivative of a partial derivative .
- For example, the second partial derivative of f with respect to x and then y is denoted by f_xy(x,y) or ∂^2f/∂y∂x and is obtained by first differentiating f with respect to x and then differentiating the result with respect to y .
- The order of differentiation does not matter for continuous and smooth functions, meaning that f_xy(x,y) = f_yx(x,y) or ∂^2f/∂y∂x = ∂^2f/∂x∂y . This is known as Clairaut's theorem.
- Here are some examples of partial derivatives:

  - f(x,y) = x^2y^3
    - f_x(x,y) = 2xy^3
    - f_y(x,y) = 3x^2y^2
    - f_xx(x,y) = 2y^3
    - f_yy(x,y) = 6x^2y
    - f_xy(x,y) = f_yx(x,y) = 6xy^2 

  - f(x,y) = sin(xy)
    - f_x(x,y) = ycos(xy)
    - f_y(x,y) = xcos(xy)
    - f_xx(x,y) = -y^2sin(xy)
    - f_yy(x,y) = -x^2sin(xy)
    - f_xy(x,y) = f_yx(x,y) = cos(xy) - xysin(xy) 

  - f(x,y) = e^(x/y)
    - f_x(x,y) = e^(x/y)/y
    - f_y(x,y) = -e^(x/y)x/y^2
    - f_xx(x,y) = e^(x/y)/y^2
    - f_yy(x,y) = e^(x/y)x(2x-y)/y^4
    - f_xy(x,y) = f_yx(x,y) = -e^(x/y)(x+y)/y^3