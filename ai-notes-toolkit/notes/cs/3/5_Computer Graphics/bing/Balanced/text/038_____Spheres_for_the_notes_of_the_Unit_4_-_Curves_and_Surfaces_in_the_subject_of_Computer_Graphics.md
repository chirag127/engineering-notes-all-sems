### Spheres

- A sphere is a three-dimensional object that has a round shape and a constant radius from its center.
- In computer graphics, spheres are often used to model natural objects such as planets, balls, bubbles, etc.
- However, spheres are not easy to represent on a computer screen, which is made of pixels arranged in a grid. Therefore, spheres are usually approximated by simpler objects constructed from flat polygons (polyhedra).
- There are different methods to approximate a sphere by polygons, such as:
  - Using lines of longitude and latitude to divide the sphere into quadrilaterals or triangles.
  - Using a subdivision algorithm to recursively split an initial polyhedron (such as a tetrahedron, an octahedron, or an icosahedron) into smaller triangles that converge to the sphere.
  - Using a ray tracing technique to compute the intersection of a ray from the camera to the pixel with the sphere equation and shade the pixel accordingly.
- The quality of the approximation depends on the number and size of the polygons used. The more polygons, the smoother and more realistic the sphere looks, but the more computation and memory are required.
- Some properties of spheres that are useful for computer graphics are:
  - The equation of a sphere centered at the origin with radius r is x^2 + y^2 + z^2 = r^2.
  - The normal vector at any point on the sphere is the same as the position vector of that point, normalized to unit length.
  - The surface area of a sphere is 4πr^2 and the volume is (4/3)πr^3.
  - The sphere is a closed and convex surface, which means that any ray that intersects the sphere does so at exactly two points, and that any point inside the sphere is closer to the center than any point outside the sphere.