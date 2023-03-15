### Spheres

- A sphere is a three-dimensional object that has a round shape and a constant radius from its center.
- In computer graphics, spheres are often used to model objects such as balls, planets, bubbles, etc.
- Spheres can be represented mathematically by the equation: x^2 + y^2 + z^2 = r^2, where r is the radius and (x, y, z) are the coordinates of any point on the sphere.
- Spheres can also be defined parametrically by the equations: x = r * cos(u) * sin(v), y = r * sin(u) * sin(v), z = r * cos(v), where r is the radius and (u, v) are the spherical angles.
- Spheres can be approximated by simpler objects constructed from flat polygons (polyhedra) by dividing the sphere into segments along lines of longitude and latitude. The segments can be either quadrilaterals or triangles, depending on the number of divisions.
- Spheres can be rendered in computer graphics by using various techniques, such as ray tracing, rasterization, texture mapping, lighting, shading, etc.
- Spheres have some properties that make them useful in computer graphics, such as:
  - They are easy to transform, rotate, and scale by applying matrix operations to their center and radius.
  - They have a simple normal vector at any point, which is the same as the direction from the center to the point.
  - They have a simple distance function, which is the difference between the radius and the distance from the center to any point.
  - They can be used as bounding volumes, which are simple shapes that enclose more complex objects and can be used for collision detection, culling, etc.