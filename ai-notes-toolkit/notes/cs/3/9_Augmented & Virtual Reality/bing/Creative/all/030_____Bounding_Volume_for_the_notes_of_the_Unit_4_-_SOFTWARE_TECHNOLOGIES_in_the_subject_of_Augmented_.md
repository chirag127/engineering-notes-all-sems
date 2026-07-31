# Bounding Volume

- A bounding volume is a closed volume that completely contains an object or a set of objects in 3D space.
- Bounding volumes are used to improve the efficiency of geometrical operations by using simple volumes to contain more complex objects.
- Bounding volumes can be used for various applications, such as ray tracing, collision detection, frustum culling, and object detection in augmented reality   .
- Bounding volumes can be classified into two types: discrete and continuous.
  - Discrete bounding volumes are composed of a finite number of primitives, such as points, lines, triangles, or polygons.
  - Continuous bounding volumes are defined by mathematical equations, such as spheres, cylinders, cones, or ellipsoids.
- Bounding volumes can also be organized into hierarchical structures, such as bounding volume hierarchies (BVH), to further improve the performance of spatial queries.
  - A BVH is a tree structure that recursively subdivides the space and the objects into smaller and tighter bounding volumes.
  - A BVH can be constructed using different criteria, such as surface area, volume, overlap, or cost.
  - A BVH can be traversed using different algorithms, such as depth-first, breadth-first, or hybrid.