### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image.
- HLR and HSR are important for creating realistic and accurate images of solid objects, as well as for reducing the computational complexity and rendering time.
- There are different types of coherence that can be exploited to perform HLR and HSR efficiently, such as object coherence, image coherence, surface coherence, and temporal coherence.
- Object coherence refers to the spatial relationship among the objects in the scene, such as occlusion, containment, and proximity.
- Image coherence refers to the spatial relationship among the pixels in the image, such as scan-line order, adjacency, and continuity.
- Surface coherence refers to the properties of the surfaces in the scene, such as planarity, convexity, and orientation.
- Temporal coherence refers to the relationship between successive frames in an animation, such as motion, deformation, and visibility.
- There are different algorithms for HLR and HSR, such as back-face culling, depth-buffer method, scan-line method, painter's algorithm, z-buffer algorithm, BSP-tree method, ray-tracing method, and area-subdivision method.
- Back-face culling is a simple technique that eliminates the faces that are facing away from the viewer, based on the surface normal vector and the viewing direction vector.
- Depth-buffer method is a technique that assigns a depth value to each pixel in the image, and compares it with the depth values of the objects in the scene, to determine the visible pixel.
- Scan-line method is a technique that processes the image one scan-line at a time, and maintains a list of active edges and surfaces, to determine the visible pixel.
- Painter's algorithm is a technique that sorts the surfaces in the scene from back to front, and paints them in that order, to create the final image.
- Z-buffer algorithm is a technique that maintains a z-buffer (or depth buffer) and a frame buffer for each pixel in the image, and updates them with the depth and color values of the closest surface, to create the final image.
- BSP-tree method is a technique that partitions the scene into convex regions using binary space partitioning (BSP) trees, and traverses the tree in a back-to-front or front-to-back order, to determine the visible surfaces.
- Ray-tracing method is a technique that traces a ray from the eye to each pixel in the image, and finds the closest intersection with the objects in the scene, to determine the visible pixel.
- Area-subdivision method is a technique that divides the image into smaller regions, and tests the visibility of the surfaces in each region, to determine the visible pixels.