### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible to the viewer in a 3D scene, because they are occluded by other objects or by the object itself.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image, to improve the realism and efficiency of the rendering process .
- There are different types of coherence that can be exploited to reduce the computation required for HLR and HSR, such as object coherence, image coherence, area coherence, and span coherence.
- Object coherence means that the relative positions and orientations of the objects in the scene do not change significantly from one frame to the next, so the visibility information can be reused.
- Image coherence means that the pixels in the image have similar properties, such as color, depth, and visibility, so they can be processed in groups.
- Area coherence means that the regions of the image that are covered by a single surface have the same visibility, so they can be filled with a uniform color.
- Span coherence means that the pixels along a scan line that are covered by a single surface have the same visibility, so they can be drawn with a single line.
- There are different algorithms for HLR and HSR, such as back-face culling, depth-buffer method, scan-line method, painter's algorithm, z-buffer algorithm, BSP-tree method, ray tracing, and area subdivision method  .
- Back-face culling is a simple technique that eliminates the polygons that are facing away from the viewer, based on the sign of the dot product of the polygon normal and the view vector.
- Depth-buffer method is a technique that assigns a depth value to each pixel in the image, and compares it with the depth value of the incoming polygon, to determine which one is closer to the viewer.
- Scan-line method is a technique that processes the image one scan line at a time, and maintains a list of active edges and surfaces, to determine the visibility of each pixel.
- Painter's algorithm is a technique that sorts the polygons in the scene from back to front, and draws them in that order, so that the closer polygons overwrite the farther ones.
- Z-buffer algorithm is a technique that uses a z-buffer (or depth buffer) to store the depth value of the closest polygon at each pixel, and updates it whenever a closer polygon is encountered.
- BSP-tree method is a technique that uses a binary space partitioning tree to divide the scene into convex regions, and traverses the tree in a back-to-front or front-to-back order, depending on the view position, to draw the polygons.
- Ray tracing is a technique that traces a ray from the eye to each pixel in the image, and finds the closest intersection with the scene objects, to determine the visibility and color of the pixel.
- Area subdivision method is a technique that divides the image into smaller regions, and tests the visibility of each region against the scene objects, to determine which regions are fully visible, fully hidden, or partially visible.