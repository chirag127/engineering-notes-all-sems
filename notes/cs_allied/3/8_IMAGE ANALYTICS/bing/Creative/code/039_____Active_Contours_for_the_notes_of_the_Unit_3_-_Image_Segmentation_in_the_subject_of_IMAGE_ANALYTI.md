### Active Contours for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as color, intensity, texture, shape, etc.
- Active contours, also known as snakes, are a type of image segmentation technique that uses iterative region-growing algorithms to find the boundaries of objects in an image.
- Active contours are defined by a set of points or curves that are initialized by the user or automatically, and then deformed by internal and external forces to fit the object contours.
- Internal forces are derived from the shape and smoothness of the active contour, and external forces are derived from the image data, such as gradients, edges, regions, etc.
- The goal of active contour segmentation is to minimize the energy function that balances the internal and external forces, and to reach a stable state that conforms to the object boundaries.
- Active contours can be classified into two categories: parametric and geometric.
- Parametric active contours are represented by a parametric curve, such as a spline or a polygon, and are updated by moving the control points along the normal direction of the curve.
- Geometric active contours are represented by a level set function, such as a signed distance function, and are updated by solving a partial differential equation that evolves the level set function.
- Parametric active contours are faster and simpler to implement, but they have limitations such as topological changes, initialization sensitivity, and parameter tuning.
- Geometric active contours are more flexible and robust to noise, but they are more computationally expensive and complex to implement.
- Active contours have many applications in computer vision, such as object tracking, shape recognition, medical image analysis, etc.