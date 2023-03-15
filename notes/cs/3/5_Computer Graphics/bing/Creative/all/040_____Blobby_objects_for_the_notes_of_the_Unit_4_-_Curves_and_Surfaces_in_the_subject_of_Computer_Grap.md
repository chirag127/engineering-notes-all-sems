# Blobby Objects

- Blobby objects are a type of **implicit modeling technique** that can represent non-rigid and fluid-like objects in computer graphics.
- Blobby objects are defined by a set of **metaballs**, which are spherical regions of influence that have a scalar field value that decreases with distance from the center.
- The surface of a blobby object is the **isosurface** of the scalar field, which is the set of points where the field value is equal to a given threshold.
- The scalar field value at any point is computed by summing the contributions of all the metaballs, which can be weighted by different factors.
- Blobby objects can be used to model objects such as cloth, rubber, liquids, water droplets, clouds, etc .
- Blobby objects can exhibit **metamorphosis**, which is the smooth transformation of one shape into another, by changing the positions, sizes, and weights of the metaballs.
- Blobby objects can also exhibit **blending**, which is the merging or splitting of two or more shapes, by adjusting the threshold value of the isosurface.
- Blobby objects can be rendered using **ray tracing** or **polygonization** techniques.
- Ray tracing involves finding the intersection of a ray with the isosurface, which can be done by solving a nonlinear equation or using a root-finding method.
- Polygonization involves approximating the isosurface by a mesh of polygons, which can be done by using a **marching cubes** algorithm or a **marching tetrahedra** algorithm.