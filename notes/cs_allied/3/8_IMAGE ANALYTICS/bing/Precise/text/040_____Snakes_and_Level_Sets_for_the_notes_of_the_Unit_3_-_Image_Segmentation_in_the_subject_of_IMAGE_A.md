### Snakes and Level Sets for Image Segmentation

- Snakes and Level Sets are two techniques used for image segmentation.
- Snakes are evolving 2D curves (open or closed) that are based on updating the points of the curve.
- Snakes can segment one component.
- Level Sets are implicit 3D surfaces where the zero-level represents the segmentation.
- Level Sets can segment multiple components and they are more generic.
- Both Snakes and Level Sets are evolving techniques that take some time to produce the segmentation and they depend on the initial seed.
- Active contour is the main technique and it can be realized using Snakes or Level Sets.
- The snakes model is popular in computer vision, and snakes are widely used in applications like object tracking, shape recognition, segmentation, edge detection and stereo matching.
- A snake is an energy minimizing, deformable spline influenced by constraint and image forces that pull it towards object contours and internal forces that resist deformation.