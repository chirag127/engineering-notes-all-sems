### Scan line method

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The main idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image and compute the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons.
- The scan line method can be applied to both solid and wireframe models, and can handle concave and convex polygons, as well as polygons with holes.
- The scan line method has several advantages, such as:
  - It is efficient and fast, as it avoids unnecessary calculations for hidden pixels or polygons.
  - It is easy to implement and can be parallelized.
  - It can handle shading, texture mapping, and anti-aliasing techniques by interpolating the attributes of the vertices along the scan line.
- The scan line method has some disadvantages, such as:
  - It requires sorting and updating the polygon list, which can be costly for complex scenes.
  - It can produce artifacts or errors when dealing with polygons that share edges or vertices, or when the scan line coincides with a polygon edge.
  - It can be difficult to handle non-planar polygons, as they may need to be subdivided into smaller planar polygons.
- The scan line method can be extended to handle 3D hidden surface removal by using a depth buffer or a z-buffer, which stores the depth or distance of each pixel from the viewpoint, and compares it with the depth of the incoming polygon fragments.
- The scan line method can also be combined with other algorithms, such as ray tracing or radiosity, to produce more realistic images with shadows, reflections, and global illumination effects.