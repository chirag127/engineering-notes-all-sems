### Blobby Objects

- Blobby objects are a type of **implicit modeling** technique in computer graphics .
- Implicit modeling is a way of representing surfaces by **distance functions** .
- A distance function is a function that gives the **minimum distance** from a point to a surface .
- A surface is defined as the set of points where the distance function is **zero** .
- Blobby objects are also known as **metaballs** .
- Metaballs are a way of modeling **non-rigid** objects that change their shape and size based on their states  .
- Examples of non-rigid objects are cloth, rubber, liquids, water droplets, etc.
- Metaballs are composed of **spheres** that have a **field strength** and a **radius** .
- The field strength is a measure of how much the sphere **influences** the surrounding space .
- The radius is the distance from the center of the sphere to the **boundary** of its influence .
- The distance function of a metaball is calculated as the **sum** of the field strengths of all the spheres .
- The surface of a metaball is the set of points where the distance function is equal to a **threshold** value .
- The threshold value determines the **smoothness** and **roundness** of the surface .
- The surface of a metaball can be rendered using **isosurface extraction** algorithms, such as **marching cubes** .
- Isosurface extraction algorithms are methods of finding and drawing the surface of an implicit model .
- Marching cubes is an algorithm that divides the space into **cubic cells** and finds the **intersections** of the surface with the edges of the cells .
- The intersections are then used to form **triangles** that approximate the surface .
- The triangles are then **shaded** and **displayed** on the screen .
- Metaballs can be used to create **organic** and **fluid** shapes, such as blobs, drops, flames, etc .
- Metaballs can also be **animated** by changing the positions, radii, and field strengths of the spheres over time .

Here is a diagram of how metaballs are formed and rendered:

![Metaballs diagram](https://i.imgur.com/9cJm7Z1.png)