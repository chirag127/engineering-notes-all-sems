### A-buffer method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects .
- It extends the algorithm of depth-buffer (or Z-buffer) method by storing more than one depth and color value per pixel .
- It uses a linked list data structure to store the fragments of objects that cover each pixel .
- Each fragment has four attributes: depth, color, opacity, and pointer to the next fragment .
- The fragments are sorted in decreasing order of depth, so that the nearest fragment is at the head of the list .
- The final color of each pixel is computed by blending the colors of the fragments according to their opacities .
- A-buffer method can handle anti-aliasing, transparency, and shadows .
- A-buffer method requires more memory and processing time than depth-buffer method .
- A-buffer method can be implemented using hardware or software .