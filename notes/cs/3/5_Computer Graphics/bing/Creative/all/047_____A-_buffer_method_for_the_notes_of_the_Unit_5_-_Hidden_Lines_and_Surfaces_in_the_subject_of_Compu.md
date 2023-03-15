# A-Buffer Method for Hidden Lines and Surfaces

- A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects .
- It extends the algorithm of depth-buffer (or Z-buffer) method by storing more than one depth and color value per pixel.
- It uses a linked list data structure to store the fragments of objects that overlap a pixel.
- Each fragment has four attributes: depth, color, opacity, and pointer to the next fragment.
- The fragments are sorted in decreasing order of depth and stored in the A-buffer.
- The final color of a pixel is computed by blending the colors of the fragments from front to back, using the opacity values as weights.
- A-buffer method can handle anti-aliasing, transparency, and complex intersections.
- A-buffer method requires more memory and processing time than depth-buffer method.
- A-buffer method can be implemented using hardware or software.