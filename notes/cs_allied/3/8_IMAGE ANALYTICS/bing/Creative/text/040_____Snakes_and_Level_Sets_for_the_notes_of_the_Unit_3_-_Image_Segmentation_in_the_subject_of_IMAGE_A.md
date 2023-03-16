### Snakes and Level Sets

- Snakes or active contour models are classical methods for boundary detection and segmentation, which deform an initial contour (for 2D image) or a surface (for 3D image) towards the boundary of the desired object .
- Snakes are parametric curves that minimize an energy functional composed of internal and external forces. Internal forces are derived from the curve's shape and smoothness, while external forces are derived from the image's gradient, edge, or region information.
- Snakes can segment one component at a time and require a good initial guess of the contour or surface. They are also sensitive to noise and local minima .
- Level sets are implicit 3D surfaces where the zero-level represents the segmentation. Level sets are defined by a signed distance function that evolves according to a partial differential equation (PDE) based on geometric flow .
- Level sets can segment multiple components and handle topological changes. They are more generic and robust than snakes, but they are also more computationally expensive and require careful initialization .
- Level sets can be seen as a geometric replacement for snakes, where the contour or surface is embedded in a higher-dimensional function and evolves according to the level set equation .
- Both snakes and level sets are evolving techniques that take some time to produce the segmentation and they depend on the initial seed. They can be combined with machine learning methods to improve their performance and accuracy .