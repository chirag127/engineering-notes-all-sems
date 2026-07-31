### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The main idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be divided into two phases: initialization and scan conversion.
- Initialization phase:
  - For each polygon, compute the plane equation and the normal vector.
  - For each edge of each polygon, compute the slope and the x and z intercepts.
  - Sort the edges by the minimum y coordinate and store them in a global edge table (GET).
- Scan conversion phase:
  - Initialize an active edge list (AEL) to be empty.
  - For each scan line, do the following steps:
    - Move any edges from the GET whose minimum y coordinate is equal to the scan line to the AEL.
    - Sort the AEL by the x coordinate of the intersection with the scan line.
    - For each pair of edges in the AEL, fill the pixels between them with the color and intensity of the polygon they belong to, using the plane equation and the normal vector to compute the shading.
    - Update the x and z coordinates of each edge in the AEL by adding the slope to them.
    - Remove any edges from the AEL whose maximum y coordinate is equal to the scan line.
- The scan line method can handle concave polygons, holes, and multiple polygons overlapping on the same scan line.
- The scan line method can be optimized by using coherence, which means exploiting the spatial and temporal locality of the polygons and the pixels.
- The scan line method can be extended to handle anti-aliasing, transparency, texture mapping, and shadows by using additional buffers and techniques.