## Unit 4 - Curves and Surfaces

- A curve is a one-dimensional object that can be represented by a function of one or more parameters, such as x(t), y(t), z(t) for a curve in three-dimensional space.
- A surface is a two-dimensional object that can be represented by a function of two or more parameters, such as x(u,v), y(u,v), z(u,v) for a surface in three-dimensional space.
- Curves and surfaces are important in computer graphics, computer-aided design, and geometric modeling, as they can be used to create and manipulate complex shapes and objects.
- Some common types of curves and surfaces are:
  - Line: a curve that has constant direction and magnitude, such as x(t) = a + bt, y(t) = c + dt, z(t) = e + ft.
  - Circle: a curve that has constant distance from a fixed point, such as x(t) = a + r cos(t), y(t) = b + r sin(t), z(t) = c.
  - Ellipse: a curve that has constant sum of distances from two fixed points, such as x(t) = a + r cos(t), y(t) = b + s sin(t), z(t) = c.
  - Parabola: a curve that has constant distance from a fixed line, such as x(t) = a + bt, y(t) = c + dt + et^2, z(t) = f.
  - Hyperbola: a curve that has constant difference of distances from two fixed points, such as x(t) = a + r cosh(t), y(t) = b + s sinh(t), z(t) = c.
  - Bezier curve: a curve that is defined by a set of control points and a polynomial basis function, such as x(t) = sum(i=0 to n) B_i^n(t) P_i_x, y(t) = sum(i=0 to n) B_i^n(t) P_i_y, z(t) = sum(i=0 to n) B_i^n(t) P_i_z, where B_i^n(t) are the Bernstein polynomials and P_i are the control points.
  - B-spline curve: a curve that is defined by a set of control points and a knot vector, such as x(t) = sum(i=0 to n) N_i,k(t) P_i_x, y(t) = sum(i=0 to n) N_i,k(t) P_i_y, z(t) = sum(i=0 to n) N_i,k(t) P_i_z, where N_i,k(t) are the B-spline basis functions and P_i are the control points.
  - NURBS curve: a curve that is defined by a set of control points, a knot vector, and a weight vector, such as x(t) = sum(i=0 to n) w_i N_i,k(t) P_i_x / sum(i=0 to n) w_i N_i,k(t), y(t) = sum(i=0 to n) w_i N_i,k(t) P_i_y / sum(i=0 to n) w_i N_i,k(t), z(t) = sum(i=0 to n) w_i N_i,k(t) P_i_z / sum(i=0 to n) w_i N_i,k(t), where w_i are the weights and N_i,k(t) and P_i are the same as in B-spline curves.
  - Plane: a surface that has constant normal vector, such as x(u,v) = a + bu + cv, y(u,v) = d + eu + fv, z(u,v) = g + hu + iv.
  - Sphere: a surface that has constant distance from a fixed point, such as x(u,v) = a + r cos(u) cos(v), y(u,v) = b + r cos(u) sin(v), z(u,v) = c + r sin(u).
  - Ellipsoid: a surface that has constant sum of squared distances from three fixed points, such as x(u,v) = a + r cos(u) cos(v), y(u,v) = b + s cos(u) sin(v), z(u,v) = c + t sin(u).
  - Cylinder: a surface that has constant distance from a fixed line, such as x(u,v) = a + r cos(u), y(u,v) = b + r sin(u), z(u,v) = c + v.
  - Cone: a surface that has constant ratio of distance from a fixed point to distance from a fixed line, such as x(u,v) = a + v