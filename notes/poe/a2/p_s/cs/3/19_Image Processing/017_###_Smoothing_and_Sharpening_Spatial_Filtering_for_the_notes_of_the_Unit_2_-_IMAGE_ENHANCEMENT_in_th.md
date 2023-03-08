 Here is the content written in markdown format for the topic ### Smoothing and Sharpening Spatial Filtering for the notes of Unit 2 - Image Enhancement:

### Smoothing and Sharpening Spatial Filtering

- Spatial filtering is a neighborhood operation where the value of each pixel in an image is modified by combining it with neighboring pixel values.
- This is done to either smooth out or sharpen the details in an image.
- **Smoothing** is done to remove noise and spurious gradients/details. It is achieved by averaging or weighting neighboring pixels. This has the effect of blurring edges and details.
- **Sharpening** is done to enhance edges and details. It is achieved by amplifying gradients/details in the image. This has the effect of increasing the contrast around edges and details.

**Smoothing Spatial Filters**
- Mean filter: Replaces each pixel value with the average of its neighbors. Reduces noise but blurs edges.
- Gaussian filter: Weights neighboring pixels using a Gaussian weighting function. Causes less blurring than mean filter.
- Median filter: Replaces each pixel value with the median of its neighbors. Effective at removing salt-and-pepper noise while preserving edges.

**Sharpening Spatial Filters**
- Laplacian filter: Enhances edges/details by finding the Laplacian (2nd derivative) of the image intensity function.
- Unsharp masking: Creates a blurred version of the image, subtracts it from the original and adds a scaled version of the difference back to the original. Enhances edges/details.
- High-boost filtering: Similar to unsharp masking but uses a ratio of low-pass and high-pass filtered images. Adjustable amount of sharpening.

**Advantages**: Simple to implement, can be effective at noise removal/edge enhancement
**Disadvantages**: Can introduce artifacts, does not perform well on images with fine details/textures, choice of filter parameters can be difficult
**Applications**: Pre-processing step for edge detection, segmentation, object recognition, etc.

[Detailed diagrams and examples can be added here]