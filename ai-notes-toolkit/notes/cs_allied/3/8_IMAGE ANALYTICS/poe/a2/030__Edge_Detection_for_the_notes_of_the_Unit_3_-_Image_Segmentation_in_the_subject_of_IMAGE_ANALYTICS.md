 Here is the content in Markdown format without any emojis or external links:

### Edge Detection for the notes of the Unit 3 - Image Segmentation

1. Edge Detection is a method to identify sharp discontinuities in an image. The discontinuities are abrupt changes in pixel intensity which characterize boundaries of objects in a scene.

2. Edges typically occur on the boundary between two different regions in an image. Edge detection is used to simplify the image data and extract useful information.

3. Common edge detection algorithms are:

- Sobel operator: Uses two 3x3 kernels which are convolved with the original image to calculate approximations of the derivatives - one for horizontal changes and one for vertical.
- Prewitt operator: Similar to Sobel but uses different kernels.
- Robert's cross operator: Uses a 2x2 kernel and so is relatively quick but can be noisy.
- Canny edge detector: More complex and has five stages:

1. Apply Gaussian filter to smooth the image and remove noise
2. Find the intensity gradients of the image
3. Apply non-maximum suppression to thin out the edges
4. Apply double threshold to determine potential edges
5. Track edge by hysteresis: Finalize the detection of edges by suppressing all other edges that are weak and not connected to strong edges.

4. edge detection is an important pre-processing step for applications such as segmentation, object recognition and machine vision. The key requirements are:

- Good detection: Minimize false negatives (missed edges)
- Good localization: Edges should be tightly localized
- Minimal response: Avoid multiple responses to a single edge
- Robustness: Work well even with noise or imperfections in the image