### Bounding Volume

- A bounding volume is a closed volume that completely contains an object or a set of objects in 3D space.
- Bounding volumes are used to improve the efficiency of geometrical operations by using simple volumes to contain more complex objects.
- Bounding volumes can be used for various applications, such as ray tracing, collision detection, frustum culling, and object detection  .
- Bounding volumes can be classified into two types: discrete and continuous.
  - Discrete bounding volumes are composed of a finite number of primitives, such as points, lines, triangles, or polygons.
  - Continuous bounding volumes are defined by mathematical equations, such as spheres, cylinders, cones, or ellipsoids.
- Bounding volumes can also be classified into two categories: exact and approximate.
  - Exact bounding volumes are the smallest possible volumes that contain the object.
  - Approximate bounding volumes are larger than the exact ones, but they are easier to compute and manipulate.
- Bounding volumes can be combined into hierarchical structures, such as bounding volume hierarchies (BVH), to speed up the traversal and intersection tests.
  - BVH are trees that store bounding volumes at each node, and the object or objects at the leaf nodes.
  - BVH can be constructed using various methods, such as top-down, bottom-up, or hybrid approaches.
  - BVH can be optimized using various criteria, such as surface area, volume, overlap, or cost.
- Bounding volumes are essential for augmented reality applications, as they enable the detection and tracking of real-world objects in 3D space .
  - Bounding volumes can be used to estimate the pose, size, and orientation of the objects.
  - Bounding volumes can be used to register virtual objects with the real scene.
  - Bounding volumes can be used to create realistic interactions and occlusions between the virtual and real objects.