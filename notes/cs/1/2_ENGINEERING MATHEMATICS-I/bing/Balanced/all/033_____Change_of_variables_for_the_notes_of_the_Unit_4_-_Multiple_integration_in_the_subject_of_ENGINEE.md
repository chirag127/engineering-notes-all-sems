# Change of variables for the notes of the Unit 4 - Multiple integration in the subject of ENGINEERING MATHEMATICS-I

- The change of variables in multiple integrals is a technique that allows us to simplify the integration of a function over a complex region by transforming it to a function over a simpler region.
- The change of variables in multiple integrals is based on the idea of planar transformations, which are functions that map one region to another by changing their variables.
- For example, a planar transformation can map a region H in the uv-plane to a region S in the xy-plane by using the functions x = x(u, v) and y = y(u, v).
- The change of variables formula for multiple integrals states that if x = x(u, v) and y = y(u, v) define a one-to-one mapping of a region R' in the uv-plane onto a region R in the xy-plane, then

$$\iint_R f(x, y) dA = \iint_{R'} f(x(u, v), y(u, v)) |J(u, v)| du dv$$

where J(u, v) is the Jacobian determinant given by

$$J(u, v) = \frac{\partial (x, y)}{\partial (u, v)} = \begin{vmatrix} \frac{\partial x}{\partial u} & \frac{\partial x}{\partial v} \\ \frac{\partial y}{\partial u} & \frac{\partial y}{\partial v} \end{vmatrix}$$

- The Jacobian determinant measures the factor by which the area element dA changes under the transformation. It can be positive or negative depending on the orientation of the regions.
- The change of variables formula can be extended to higher dimensions by using more variables and higher-order Jacobians.
- The change of variables technique can be useful for evaluating multiple integrals that are difficult or impossible to do by direct methods, such as when the integrand involves trigonometric, exponential, or rational functions, or when the region of integration is curved, polar, or cylindrical.