### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image.
- HLR and HSR are important for creating realistic and accurate images of solid objects, as well as for reducing the computational complexity and rendering time.
- There are different types of coherence that can be exploited to perform HLR and HSR efficiently, such as object coherence, image coherence, and temporal coherence.
- Object coherence refers to the spatial relationship among the objects in the scene, such as occlusion, containment, and proximity.
- Image coherence refers to the spatial relationship among the pixels in the image, such as scan-line order, adjacency, and continuity.
- Temporal coherence refers to the temporal relationship among the successive frames in an animation, such as motion, deformation, and illumination.
- There are different algorithms that can be used to perform HLR and HSR, such as back-face culling, depth sorting, z-buffer, scan-line, area subdivision, and ray tracing.
- Back-face culling is a simple technique that eliminates the faces that are facing away from the viewer, based on the orientation of their normal vectors.
- Depth sorting is a technique that sorts the objects or faces in the scene from back to front, based on their distance from the viewer, and then renders them in that order, using the painter's algorithm.
- Z-buffer is a technique that uses a buffer to store the depth value of each pixel in the image, and then compares the depth value of the incoming pixel with the stored value, and updates the buffer and the image accordingly.
- Scan-line is a technique that processes the image one scan-line at a time, and uses an active edge list and an active polygon list to determine the visible segments on each scan-line, using the coherence properties of the image.
- Area subdivision is a technique that divides the image into smaller regions, and then recursively tests each region for visibility, using the coherence properties of the objects and the image.
- Ray tracing is a technique that traces a ray from the viewer through each pixel in the image, and then determines the closest object or face that intersects the ray, using the coherence properties of the objects and the image.