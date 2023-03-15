### Scan line method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Scan line method is an algorithm for visible surface determination, in 3D computer graphics, that works on a row-by-row basis rather than a polygon-by-polygon or pixel-by-pixel basis .
- The basic idea is to sort all the polygons to be rendered by the top y coordinate at which they first appear, then scan each row or scan line of the image from top to bottom, computing the intersection of the scan line with the polygons on the front of the sorted list, while updating the list to discard no-longer-visible polygons and add newly-visible polygons .
- The scan line method can be applied to both wireframe and solid models, and can handle concave and convex polygons, as well as polygons with holes .
- The scan line method can also be extended to handle hidden surface removal in 3D, by using a depth buffer or a z-buffer to store the depth or z coordinate of the closest visible surface at each pixel, and comparing the depth of the current polygon with the depth buffer to determine if it is occluded or not .
- The scan line method has some advantages and disadvantages compared to other visible surface determination algorithms, such as ray tracing, z-buffer, painter's algorithm, etc. Some of the advantages are :
  - It is fast and efficient, as it exploits the coherence between adjacent scan lines and avoids unnecessary calculations for invisible pixels or polygons.
  - It is easy to implement and can be parallelized, as each scan line can be processed independently.
  - It can handle antialiasing, shading, and texture mapping, by interpolating the color, intensity, and texture coordinates along the scan line.
- Some of the disadvantages are :
  - It requires sorting the polygons by their y coordinates, which can be costly for large or complex scenes.
  - It requires maintaining and updating the active edge list, which can be complicated for polygons with multiple intersections or shared edges.
  - It can produce artifacts or errors for polygons that are nearly horizontal or nearly vertical, as the scan line may miss some pixels or intersect the same polygon twice.