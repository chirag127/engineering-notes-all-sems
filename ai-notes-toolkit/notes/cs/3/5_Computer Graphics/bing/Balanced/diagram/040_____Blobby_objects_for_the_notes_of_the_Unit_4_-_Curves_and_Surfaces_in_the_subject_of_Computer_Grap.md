### Blobby objects

- Blobby objects are a type of implicit modeling technique that can represent non-rigid and fluid-like objects in computer graphics .
- Blobby objects are defined by a set of **metaballs**, which are spheres with a scalar field that represents their influence or potential.
- The scalar field of a metaball is usually a function of the distance from its center, such as `f(r) = 1/(1 + r^2)` or `f(r) = e^(-r^2)`.
- The surface of a blobby object is then defined by an **isosurface**, which is a set of points that have the same scalar value, called the **threshold**.
- The scalar value at any point in space is computed by summing up the contributions of all the metaballs in the blobby object.
- The isosurface can be rendered using various algorithms, such as **marching cubes**, **ray tracing**, or **polygonization**.
- Blobby objects can be used to model organic shapes, such as water droplets, clouds, fire, smoke, or soft bodies .
- Blobby objects can also be animated by changing the positions, sizes, or scalar functions of the metaballs over time.
- Blobby objects have some advantages and disadvantages over other modeling techniques, such as:
  - Advantages: easy to create and manipulate, smooth and seamless, can blend and merge with each other, can handle topological changes .
  - Disadvantages: computationally expensive, hard to control the shape and detail, hard to texture map, hard to interact with other objects .