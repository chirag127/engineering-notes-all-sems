### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The main idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and self-intersecting polygons as well.
- The scan line method has several advantages, such as:
  - It is efficient and fast, as it avoids unnecessary calculations for hidden pixels or polygons.
  - It is easy to implement and can be parallelized for multiple processors.
  - It can handle shading, texture mapping, anti-aliasing and other effects by interpolating the attributes of the vertices along the scan line.
- The scan line method has some disadvantages, such as:
  - It requires sorting and updating the polygon list, which can be costly for complex scenes.
  - It may produce artifacts or gaps at the edges of polygons, especially if they are not aligned with the scan lines.
  - It may not handle transparency or translucency well, as it only considers the frontmost polygon at each pixel.