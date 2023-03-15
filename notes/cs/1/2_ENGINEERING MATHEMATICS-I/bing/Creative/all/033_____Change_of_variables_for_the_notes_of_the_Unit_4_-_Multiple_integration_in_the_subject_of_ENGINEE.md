# Change of variables for the notes of the Unit 4 - Multiple integration in the subject of ENGINEERING MATHEMATICS-I

- The change of variables in multiple integrals is a technique that allows us to simplify the integration of a function over a complex region by transforming it to a function over a simpler region.
- The change of variables in multiple integrals is based on the idea of planar transformations, which are functions that map one region to another by changing their variables.
- For example, we can transform a region R in the xy-plane to a region R' in the uv-plane by using the functions x = x(u, v) and y = y(u, v).
- The inverse transformation is given by u = u(x, y) and v = v(x, y).
- The change of variables formula for multiple integrals states that if x = x(u, v) and y = y(u, v) define a one-to-one mapping of R' onto R, then

$$\iint_R f(x, y) dA = \iint_{R'} f(x(u, v), y(u, v)) |J(u, v)| du dv$$

where J(u, v) is the Jacobian determinant of the transformation, given by

$$J(u, v) = \frac{\partial (x, y)}{\partial (u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

- The Jacobian determinant measures the local change of area induced by the transformation. It can be positive or negative depending on the orientation of the regions.
- The change of variables formula can be extended to higher dimensions by using more variables and larger Jacobian determinants.
- The change of variables technique can be useful for evaluating integrals that are difficult or impossible to do in the original variables, such as integrals involving polar, cylindrical, or spherical coordinates.