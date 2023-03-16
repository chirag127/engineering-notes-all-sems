# Fundamentals for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

Morphological image processing is a collection of non-linear operations related to the shape or morphology of features in an image. It is used to extract image components that are useful in the representation and description of region shape, such as boundaries, skeletons, and the convex hull.

Some of the fundamental concepts in morphological image processing include:

1. **Structuring element**: A structuring element is a small set or sub-image used to probe an image under test for properties of interest. It is positioned at all possible locations in the image and it is compared with the corresponding neighborhood of pixels.

2. **Dilation**: Dilation is a morphological operation that combines two sets using vector addition of set elements. It is used to gradually enlarge the boundaries of regions of foreground pixels.

3. **Erosion**: Erosion is a morphological operation that combines two sets using vector subtraction of set elements. It is used to gradually erode away the boundaries of regions of foreground pixels.

4. **Opening**: Opening is a morphological operation that is obtained by the erosion of an image followed by dilation. It is used to remove small objects from an image while preserving the shape and size of larger objects in the image.

5. **Closing**: Closing is a morphological operation that is obtained by the dilation of an image followed by erosion. It is used to fill small holes in an image while preserving the shape and size of larger objects in the image.

These are some of the fundamental concepts in morphological image processing. It is important to understand these concepts in order to effectively apply morphological operations to image analysis tasks.