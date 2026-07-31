# Quadric Surfaces

- Quadric surfaces are common modeling primitives for a variety of computer graphics and computer-aided-design applications.
- Quadric surfaces are the graphs of equations that can be expressed in the form `Ax^2 + By^2 + Cz^2 + Dxy + Exz + Fyz + Gx + Hy + Jz + K = 0`.
- Quadric surfaces are the 3D counterparts of conic sections and have six distinct types:
  - Ellipsoid: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 + z^2/c^2 = 1`. It is a closed surface that is symmetric about the three coordinate axes and the origin. It looks like a stretched sphere.
  - Elliptic paraboloid: a surface described by an equation of the form `z = x^2/a^2 + y^2/b^2`. It is an open surface that is symmetric about the z-axis and the origin. It looks like a parabolic bowl.
  - Hyperbolic paraboloid: a surface described by an equation of the form `z = x^2/a^2 - y^2/b^2`. It is an open surface that has two opposite corners pointing up and two opposite corners pointing down. It looks like a saddle or a Pringles chip.
  - Hyperboloid of one sheet: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 1`. It is an open surface that is symmetric about the three coordinate axes and the origin. It looks like an hourglass or a cooling tower.
  - Hyperboloid of two sheets: a surface described by an equation of the form `x^2/a^2 - y^2/b^2 - z^2/c^2 = 1`. It is a closed surface that consists of two disjoint parts that are symmetric about the x-axis and the origin. It looks like two hyperboloids of one sheet facing away from each other.
  - Cone: a surface described by an equation of the form `x^2/a^2 + y^2/b^2 - z^2/c^2 = 0`. It is an open surface that is symmetric about the z-axis and the origin. It looks like a cone or an ice cream cone.
- When a quadric surface intersects a coordinate plane, the trace is a conic section. For example, a sphere intersects a plane in a circle, an ellipsoid intersects a plane in an ellipse, a cone intersects a plane in a parabola or a hyperbola, etc.
- Ray tracing or ray firing is a popular method used for realistic renderings of quadric surfaces. It involves finding the intersection points of rays of light with the surface and calculating the color and intensity of the reflected or refracted light.