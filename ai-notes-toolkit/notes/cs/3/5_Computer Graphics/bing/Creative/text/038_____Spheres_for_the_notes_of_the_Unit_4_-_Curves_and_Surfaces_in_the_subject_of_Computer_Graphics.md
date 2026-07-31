### Spheres

- A sphere is a three-dimensional object that has a round shape and a constant radius from its center.
- In computer graphics, spheres are often used to model objects such as balls, planets, bubbles, etc.
- Spheres can be represented mathematically by the equation: x^2 + y^2 + z^2 = r^2, where r is the radius and (x, y, z) are the coordinates of any point on the sphere.
- Spheres can also be defined parametrically by the equations: x = r cos(u) cos(v), y = r cos(u) sin(v), z = r sin(u), where u and v are the angles of longitude and latitude, respectively, and r is the radius.
- Spheres can be approximated by simpler objects constructed from flat polygons (polyhedra) by dividing the surface into small patches and drawing triangles or quadrilaterals that connect the vertices of the patches.
- A bounding sphere is a special type of bounding volume that encloses a set of points or objects in a sphere. It is used in computer graphics and computational geometry to perform collision detection, visibility testing, and other operations .
- A bounding sphere can be constructed by finding the smallest sphere that contains all the points or objects, or by finding the sphere that minimizes some criterion such as the volume or the surface area. There are several fast and simple bounding sphere construction algorithms with a high practical value in real-time computer graphics applications .