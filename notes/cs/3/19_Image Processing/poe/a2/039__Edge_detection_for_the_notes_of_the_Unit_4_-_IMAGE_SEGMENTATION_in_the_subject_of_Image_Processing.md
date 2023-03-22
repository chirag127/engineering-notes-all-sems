 Here is the content in Markdown format without any emojis or external links:

### Edge detection for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing.

1. Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature extraction and feature detection.
2. The purpose of edge detection is to identify points in a digital image at which the image brightness changes sharply or more formally has discontinuities.
3. Common types of edges:
- Step edges - Sudden change in intensity
- Roof edges - Rapid brightening followed by leveling off
- Ridge edges - Gradual increase followed by rapid darkening
4. Edge detection algorithms:
- Gradient-based - Look for maximum and minimum in gradient of image (Prewitt, Sobel, Canny)
- Laplacian-based - Look for zero crossings in the Laplacian of the image
- Contour-based - Follow continuous contours/outlines in the image
5. Canny edge detector - Most commonly used
- Apply Gaussian filter to smooth image and remove noise
- Find intensity gradients of the image
- Apply non-maximum suppression to thin out edges
- Apply double threshold to determine potential edges
- Track edge by hysteresis: Final edge pixels are those that are connected to strong edge pixels

The content is written in a formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the answer.