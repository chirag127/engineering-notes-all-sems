 Here is the content in Markdown format without any emojis or external links and in a formal tone:

### Smoothing Spatial Filters

1. Mean Filter - Computes the average of all the pixels under the kernel window and replaces the central pixel with this average value. Reduces noise but blurs edges.
2. Gaussian Filter - Uses a Gaussian kernel which gives more weight to pixels closer to the central pixel. Causes less blurring than mean filter but still reduces noise.
3. Median Filter - Replaces the central pixel with the median of all pixels under the kernel window. Effective in reducing salt-and-pepper noise while preserving edges.
4. Bilateral Filter - Combines domain and range filtering. Smooths regions while preserving edges. Edges are preserved as pixels across edges will have large differences in intensity.

These spatial filters are used as pre-processing steps in computer vision and image processing tasks to reduce noise and smoothen images while retaining important characteristics like edges. The choice of filter depends on the type of noise and desired application.

How's that? I have written the points in a formal tone without emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.