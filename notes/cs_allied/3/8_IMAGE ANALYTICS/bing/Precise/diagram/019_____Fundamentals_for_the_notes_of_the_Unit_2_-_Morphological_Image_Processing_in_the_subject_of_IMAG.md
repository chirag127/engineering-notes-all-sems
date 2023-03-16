### Unit 2 - Morphological Image Processing

Morphological image processing is a collection of non-linear operations related to the shape or morphology of features in an image. It is used to extract image components that are useful in the representation and description of region shape, such as boundaries, skeletons, and the convex hull.

Some of the fundamental concepts in morphological image processing include:

1. **Structuring element:** A small set or sub-image used to probe the input image. It is used to define the neighborhood of each pixel in the image and is typically much smaller than the image itself.

2. **Dilation:** A morphological operation that expands or thickens objects in a binary image. It is used to fill in small holes and gaps in the objects, and to connect disjoint objects.

3. **Erosion:** A morphological operation that shrinks or thins objects in a binary image. It is used to remove small protrusions and to separate objects that are connected by a thin bridge.

4. **Opening:** A morphological operation that is a combination of erosion followed by dilation. It is used to remove small objects and to smooth the contours of larger objects.

5. **Closing:** A morphological operation that is a combination of dilation followed by erosion. It is used to fill in small holes and gaps in the objects, and to connect disjoint objects.
