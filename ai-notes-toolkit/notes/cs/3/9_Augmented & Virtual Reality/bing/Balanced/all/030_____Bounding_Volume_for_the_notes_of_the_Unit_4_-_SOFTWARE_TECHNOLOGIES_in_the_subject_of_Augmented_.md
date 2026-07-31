# Bounding Volume

- A bounding volume is a closed volume that completely contains a set of objects in computer graphics and computational geometry .
- Bounding volumes are used to improve the efficiency of geometrical operations by using simple volumes to contain more complex objects .
- Bounding volumes can be used for visibility culling, collision detection, ray tracing, occlusion queries, and other applications  .
- Bounding volumes can be classified into two types: discrete and continuous .
  - Discrete bounding volumes are composed of a finite number of primitives, such as points, lines, triangles, or polygons .
  - Continuous bounding volumes are defined by mathematical equations, such as spheres, cylinders, cones, or ellipsoids .
- Bounding volumes can also be classified into two categories: exact and approximate .
  - Exact bounding volumes are the smallest possible volumes that contain the objects .
  - Approximate bounding volumes are larger than the exact ones, but easier to compute and manipulate .
- Bounding volumes can be nested into hierarchies to speed up the queries and reduce the number of tests  .
  - Bounding volume hierarchies (BVHs) are trees of bounding volumes, where each node encloses its children nodes  .
  - BVHs can be constructed top-down or bottom-up, depending on the criteria and the data structure used  .
- Bounding volumes can be chosen based on several factors, such as the shape, size, and orientation of the objects, the type and frequency of the queries, and the trade-off between accuracy and performance  .
  - Bounding spheres are the simplest and most symmetric bounding volumes, but they may overestimate the volume of the objects  .
  - Bounding boxes are the most common and versatile bounding volumes, but they may be sensitive to the orientation of the objects .
  - Bounding cylinders, cones, and ellipsoids are more complex and less common bounding volumes, but they may fit better to some objects than spheres or boxes .