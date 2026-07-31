### Active Contours for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as color, texture, intensity, shape, etc.
- Active contours, also known as snakes, are a type of image segmentation technique that uses iterative region-growing algorithms to find the boundaries of objects in an image.
- Active contours are defined by a set of points or curves that are initialized by the user or automatically, and then deformed by internal and external forces to fit the object contours.
- Internal forces are derived from the shape and smoothness of the active contour, and external forces are derived from the image data, such as gradients, edges, regions, etc.
- The goal of active contour segmentation is to minimize the energy function that consists of the internal and external forces, and to reach a stable equilibrium state.
- Active contour segmentation can handle noisy, blurred, or occluded images, and can adapt to complex and irregular shapes.
- There are two main types of active contour models: parametric and geometric.
- Parametric active contours are represented by a parametric curve, such as a spline or a polygon, and are updated by moving the control points along the normal direction of the curve.
- Geometric active contours are represented by a level set function, such as a signed distance function, and are updated by solving a partial differential equation that evolves the level set function.
- Parametric active contours are faster and simpler to implement, but they have limitations such as fixed topology, sensitivity to initialization, and difficulty in handling concave shapes.
- Geometric active contours are more flexible and robust, but they are computationally more expensive and require more memory and numerical stability.
- Some examples of active contour models are:

  - The original snake model by Kass et al. , which uses a combination of image gradient, line, and edge energies as external forces, and a linear combination of elasticity and rigidity as internal forces.
  - The balloon model by Cohen , which adds an inflation force to the snake model to make it expand or contract towards the object boundaries, and to handle concave shapes better.
  - The gradient vector flow (GVF) model by Xu and Prince , which modifies the external force to be a vector field that is computed by solving a diffusion equation, and that can capture the object boundaries from a larger distance and with less sensitivity to initialization.
  - The Chan-Vese model by Chan and Vese , which uses a geometric active contour based on the level set method, and defines the external force as the difference between the average intensities inside and outside the contour, and that can segment images with or without edges.
  - The end-to-end deep convolutional active contour (EDAC) model by Chen et al. , which uses a deep neural network to learn the external force from the image data, and combines it with a geometric active contour based on the level set method, and that can segment images with complex and diverse shapes.