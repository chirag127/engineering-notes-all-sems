### A-buffer method for the notes of the Unit 5 - Hidden Lines and Surfaces in the subject of Computer Graphics

- The A-buffer method is a general hidden surface mechanism suited to medium scale virtual memory computers .
- It resolves visibility among an arbitrary collection of opaque, transparent, and intersecting objects.
- It extends the algorithm of depth-buffer (or Z-buffer) method .
- It uses an A-buffer (or accumulation buffer) to store multiple fragments per pixel, each with its own depth and color values .
- It sorts the fragments in each pixel by depth and computes the final color by blending the fragments from front to back .
- It can handle anti-aliasing, area averaging, motion blur, depth of field, translucency, and shadows .
- It requires more memory and processing time than the depth-buffer method .
- It can be implemented using linked lists, arrays, or fixed-size buffers .