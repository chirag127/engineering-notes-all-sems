### Snakes and Level Sets

- Snakes or active contour models are classical methods for boundary detection and segmentation, which deform an initial contour (for 2D image) or a surface (for 3D image) towards the boundary of the desired object.
- Snakes can be formulated as an energy minimization problem, where the energy consists of internal forces that smooth the contour and external forces that attract the contour to the image features.
- Snakes can segment one component at a time and they depend on the initial seed .
- Level sets are implicit 3D surfaces where the zero-level represents the segmentation .
- Level sets can segment multiple components and they are more generic .
- Level sets are based on the concept of geometric flow, which encompasses both internal and external geometric measures in the region of interest.
- Level sets can handle topological changes and complex shapes, but they are computationally expensive and sensitive to noise.
- Learned snakes are a recent approach that combines the advantages of snakes and level sets, by using deep neural networks to learn the optimal deformation of the contour or surface .
- Learned snakes can achieve state-of-the-art performance on 3D image segmentation tasks, such as organ segmentation and lesion segmentation .