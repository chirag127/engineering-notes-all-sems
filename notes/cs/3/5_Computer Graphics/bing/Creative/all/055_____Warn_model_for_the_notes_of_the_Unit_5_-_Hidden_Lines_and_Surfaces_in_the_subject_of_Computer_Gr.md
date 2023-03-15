# Warn Model for Hidden Lines and Surfaces in Computer Graphics

- Hidden lines and surfaces are the parts of an object that are not visible from a given viewpoint or projection.
- Hidden line and surface removal is an important step in computer graphics to produce realistic and uncluttered images of 3D scenes.
- There are various algorithms for hidden line and surface removal, such as back-face culling, z-buffer, scan-line, painter's, BSP tree, ray tracing, etc.
- The Warn model is an area subdivision algorithm proposed by John Warnock in 1969. It is based on the concept of area coherence, which means that adjacent pixels in an image tend to have similar properties, such as depth, color, and visibility.
- The Warn model divides the viewing window into smaller rectangular areas, called subwindows, and determines the visibility of objects in each subwindow recursively.
- The algorithm works as follows:

  - Start with the entire viewing window as the initial subwindow.
  - For each subwindow, check if it satisfies one of the following conditions:
    - The subwindow is empty, i.e., it contains no objects. In this case, fill the subwindow with the background color and stop the recursion.
    - The subwindow is simple, i.e., it contains only one object or a part of an object that is entirely visible. In this case, fill the subwindow with the color of the object and stop the recursion.
    - The subwindow is complex, i.e., it contains more than one object or a part of an object that is partially visible. In this case, divide the subwindow into four equal subwindows and repeat the algorithm for each subwindow.
  - The recursion stops when the subwindows are small enough to be considered as pixels, or when a predefined depth limit is reached.
- The Warn model is efficient and easy to implement, but it has some drawbacks, such as:
  - It requires a lot of memory to store the subwindows and their properties.
  - It may produce aliasing artifacts, i.e., jagged edges, due to the discrete subdivision of the viewing window.
  - It may not handle curved surfaces or transparent objects well, as it assumes that objects are polygonal and opaque.