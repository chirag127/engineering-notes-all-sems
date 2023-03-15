### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The basic idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and self-intersecting polygons as well.
- The scan line method can be divided into two phases: initialization and scan conversion.
  - Initialization: In this phase, the polygons are sorted by their minimum y coordinates, and an active edge list (AEL) is created to store the edges that intersect the current scan line. The AEL is sorted by the x coordinates of the intersection points. Each edge in the AEL also has a flag to indicate whether it belongs to a visible surface or not, and a color intensity value to be used for shading.
  - Scan conversion: In this phase, each scan line is processed from top to bottom, and the pixels on the scan line are filled with the appropriate color intensity values according to the AEL. The AEL is updated as the scan line moves down, by adding new edges that start at the current scan line, deleting edges that end at the current scan line, and updating the x coordinates and flags of the existing edges. The color intensity values are also updated according to the shading model used.
- The scan line method has some advantages and disadvantages over other visible surface determination algorithms:
  - Advantages:
    - It is efficient and easy to implement, as it only requires sorting and scanning operations.
    - It can handle complex polygons and hidden surfaces without clipping or subdividing them.
    - It can be combined with various shading models, such as flat, Gouraud, or Phong shading, to produce realistic effects.
  - Disadvantages:
    - It requires a large amount of memory to store the sorted polygon list and the AEL, which may limit the number of polygons that can be rendered.
    - It may produce aliasing artifacts, such as jagged edges or moire patterns, due to the discrete nature of the scan lines and pixels. These can be reduced by using anti-aliasing techniques, such as supersampling or filtering.
    - It may not handle transparent or translucent surfaces well, as it only considers the frontmost surface at each pixel. This can be improved by using depth buffering or ray tracing techniques, which can account for multiple surfaces and their optical properties.