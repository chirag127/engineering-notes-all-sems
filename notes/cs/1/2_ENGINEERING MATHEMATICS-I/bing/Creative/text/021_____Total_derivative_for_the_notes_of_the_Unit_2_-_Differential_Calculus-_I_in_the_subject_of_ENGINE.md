### Total derivative

- The total derivative of a function of several variables means the total change in the dependent variable due to the changes in all the independent variables.
- The total derivative is the derivative with respect to a variable that depends on the function not only directly but also via the intermediate variables.
- The formula for a total derivative is a direct result of the chain rule.
- The total derivative can be used to approximate the change in a function given small changes in the variables, or to analyze the sensitivity or error propagation of a function.

#### Example 1

Suppose z = f(x, y) = x^2 + y^3, where x and y are functions of t. Find the total derivative of z with respect to t.

Solution:

Using the chain rule, we have

dz/dt = (dz/dx)(dx/dt) + (dz/dy)(dy/dt)

To find dz/dx and dz/dy, we treat x and y as constants and differentiate z with respect to x and y, respectively.

dz/dx = 2x

dz/dy = 3y^2

To find dx/dt and dy/dt, we differentiate x and y with respect to t.

dx/dt = x'

dy/dt = y'

Substituting these values into the formula, we get

dz/dt = 2x x' + 3y^2 y'

This is the total derivative of z with respect to t.

#### Example 2

Suppose the volume of a cone is given by V = (1/3)πr^2h, where r is the radius of the base and h is the height. If r and h are both increasing at a rate of 0.1 cm/s, find the rate of change of the volume when r = 2 cm and h = 3 cm.

Solution:

Using the total differential, we have

dV = (dV/dr)dr + (dV/dh)dh

To find dV/dr and dV/dh, we treat r and h as independent variables and differentiate V with respect to r and h, respectively.

dV/dr = (2/3)πrh

dV/dh = (1/3)πr^2

To find dr and dh, we use the given rates of change of r and h.

dr = 0.1 cm/s

dh = 0.1 cm/s

Substituting these values into the formula, we get

dV = (2/3)πrh dr + (1/3)πr^2 dh

dV = (2/3)π(2)(3)(0.1) + (1/3)π(2)^2(0.1)

dV = 0.4π + 0.4π

dV = 0.8π cm^3/s

This is the rate of change of the volume when r = 2 cm and h = 3 cm.