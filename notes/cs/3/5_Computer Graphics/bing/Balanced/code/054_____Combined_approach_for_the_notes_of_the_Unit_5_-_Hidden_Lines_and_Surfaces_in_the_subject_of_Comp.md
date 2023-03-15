### Combined approach for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- Hidden lines and surfaces are the edges or parts of the edges and surfaces of a 3D object that are not visible from a given viewing angle.
- Hidden line and surface removal (HLR and HSR) are the processes of identifying and eliminating the hidden lines and surfaces from a 3D scene to produce a realistic and uncluttered image.
- HLR and HSR are important for rendering solid objects, as they can improve the visual quality, realism, and efficiency of the image.
- There are different types of coherence that can be exploited to reduce the computation required for HLR and HSR, such as:
  - Object coherence: the spatial and temporal relationships among the objects in the scene.
  - Surface coherence: the properties and attributes of the surfaces of the objects, such as color, texture, shading, etc.
  - Scan-line coherence: the similarity of the pixels along a scan-line or a row of the image.
  - Area coherence: the similarity of the pixels within a small region of the image.
  - Frame coherence: the similarity of the images between successive frames in an animation.
- There are different algorithms and techniques for HLR and HSR, such as:
  - Back-face culling: a simple technique that eliminates the surfaces that are facing away from the viewer, based on the surface normal vector and the viewing direction vector.
  - Depth-buffer method: a technique that uses a buffer or a memory array to store the depth or distance of each pixel from the viewer, and compares the depth of the incoming pixel with the depth of the existing pixel to determine the visibility.
  - Scan-line method: a technique that processes the image row by row, and uses a data structure called an active edge table (AET) to store the information of the edges that intersect the current scan-line, and a data structure called an edge table (ET) to store the information of all the edges in the scene.
  - Painter's algorithm: a technique that sorts the surfaces of the objects in the scene from back to front, and paints them in that order, using the depth or distance of the surfaces as the sorting criterion.
  - Z-buffer method: a technique that combines the depth-buffer method and the painter's algorithm, and sorts the surfaces of the objects in the scene from front to back, and updates the depth buffer and the image buffer accordingly.
  - BSP-tree method: a technique that uses a data structure called a binary space partitioning tree (BSP-tree) to divide the 3D space into convex regions, and traverses the tree in a specific order to determine the visibility of the surfaces in the scene.
  - Ray-casting method: a technique that traces a ray from the viewer's eye through each pixel of the image, and finds the nearest intersection point with the surfaces of the objects in the scene, and determines the color and intensity of the pixel based on the surface properties and the lighting model.
  - Ray-tracing method: a technique that extends the ray-casting method by tracing additional rays from the intersection point to simulate the effects of reflection, refraction, and shadows.