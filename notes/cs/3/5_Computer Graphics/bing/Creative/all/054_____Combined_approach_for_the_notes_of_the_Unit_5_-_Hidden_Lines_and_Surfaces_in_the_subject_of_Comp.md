# Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image .
- HLR and HSR are important for creating realistic and accurate images of solid objects and avoiding visual clutter and confusion .
- There are different types of coherence that can be exploited to reduce the computation required for HLR and HSR, such as object coherence, image coherence, and temporal coherence.
- Object coherence refers to the spatial relationship among the objects in the scene, such as occlusion, containment, and adjacency.
- Image coherence refers to the spatial relationship among the pixels in the image, such as scan-line continuity, area coherence, and span coherence.
- Temporal coherence refers to the temporal relationship among the successive frames in an animation, such as object motion, camera motion, and illumination change.
- There are different algorithms for HLR and HSR, such as back-face culling, depth-buffer method, scan-line method, painter's algorithm, z-buffer algorithm, and BSP-tree algorithm  .
- Back-face culling is a simple technique that eliminates the faces that are oriented away from the viewer, based on the sign of the surface normal vector .
- Depth-buffer method is a technique that assigns a depth value to each pixel in the image, and compares the depth values of the overlapping pixels to determine the visible pixel .
- Scan-line method is a technique that processes the image one scan-line at a time, and maintains an active edge list and an active polygon list to determine the visible pixels .
- Painter's algorithm is a technique that sorts the polygons in the scene from back to front, and paints them on the image in that order, overwriting the previously painted pixels .
- Z-buffer algorithm is a technique that assigns a z-value to each pixel in the image, and compares the z-values of the overlapping pixels to determine the visible pixel .
- BSP-tree algorithm is a technique that partitions the scene into convex regions using binary space partitioning, and traverses the BSP-tree in a back-to-front or front-to-back order to determine the visible polygons .
- Each algorithm has its own advantages and disadvantages, such as complexity, memory requirement, accuracy, and speed .
- A combined approach for HLR and HSR can use a combination of different algorithms to achieve a balance between performance and quality .
- For example, a combined approach can use back-face culling to eliminate the invisible faces, depth-buffer method to handle the overlapping polygons, and scan-line method to fill the visible pixels .