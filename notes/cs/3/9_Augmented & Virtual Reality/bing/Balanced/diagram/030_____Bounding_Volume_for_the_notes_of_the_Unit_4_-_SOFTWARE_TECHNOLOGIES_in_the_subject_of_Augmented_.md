### Bounding Volume

- A bounding volume is a closed volume that completely contains a set of objects in 3D space.
- Bounding volumes are used to improve the efficiency of geometrical operations by using simple volumes to contain more complex objects.
- Bounding volumes can be used for collision detection, visibility culling, ray tracing, and other applications that require spatial queries .
- Bounding volumes can be classified into two types: discrete and continuous.
  - Discrete bounding volumes are composed of a finite number of primitives, such as points, lines, triangles, or polygons.
  - Continuous bounding volumes are defined by mathematical equations, such as spheres, cylinders, cones, or ellipsoids.
- Bounding volumes can also be organized into hierarchical structures, such as bounding volume hierarchies (BVHs) or bounding interval hierarchies (BIHs).
  - A hierarchical structure consists of a tree of nodes, where each node has a bounding volume that encloses its children.
  - The root node of the tree has a bounding volume that encloses the entire scene, and the leaf nodes have bounding volumes that enclose individual objects or primitives.
  - A hierarchical structure can reduce the number of intersection tests or visibility tests by culling away large portions of the scene that are not relevant to the query.