### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges that are not visible from a given viewpoint in a 3D scene.
- Hidden line and surface removal (HLR and HSR) are the techniques to identify and eliminate the hidden lines and surfaces from the final image.
- HLR and HSR are important for creating realistic and accurate images of solid objects, as well as for reducing the computational complexity and rendering time.
- There are different types of coherence that can be exploited to perform HLR and HSR efficiently, such as object coherence, image coherence, area coherence, and span coherence.
- There are different algorithms for HLR and HSR, which can be classified into two main categories: object-space methods and image-space methods .
- Object-space methods compare the objects and their parts in the scene to determine which are visible and which are hidden. They operate on the geometric model of the scene and use techniques such as back-face culling, depth sorting, and binary space partitioning.
- Image-space methods compare the depth values of the pixels in the image to determine which are closer to the viewer and which are farther away. They operate on the rasterized image of the scene and use techniques such as z-buffer, scan-line, and ray tracing.
- A combined approach for HLR and HSR can use both object-space and image-space methods to achieve a balance between accuracy and efficiency. For example, one can use back-face culling and depth sorting to eliminate some hidden surfaces in the object-space, and then use z-buffer or scan-line to resolve the remaining hidden surfaces in the image-space.