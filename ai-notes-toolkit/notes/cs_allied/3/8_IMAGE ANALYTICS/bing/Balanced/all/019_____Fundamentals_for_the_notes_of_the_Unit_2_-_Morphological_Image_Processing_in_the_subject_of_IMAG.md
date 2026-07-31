# Fundamentals for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Morphological image processing is a collection of non-linear operations that process images based on shapes or morphology of features in an image, such as boundaries, skeletons, etc.  
- Morphological operations apply a structuring element to an input image, creating an output image of the same size. The structuring element is a small binary image that defines the region of interest or neighborhood around a pixel.  
- The value of the output pixel depends on the morphological operation performed and the values of the pixels in the neighborhood. The structuring element can have different shapes and sizes, and can be positioned at any point in the image.  
- The basic morphological operations are erosion, dilation, opening, and closing. They are used to modify the shape and size of objects, remove noise, fill gaps, extract features, etc.   
- Erosion shrinks the foreground regions by removing pixels from the boundaries. It is equivalent to taking the intersection of the input image and the translated structuring element.   
- Dilation expands the foreground regions by adding pixels to the boundaries. It is equivalent to taking the union of the input image and the translated structuring element.   
- Opening is a combination of erosion followed by dilation. It removes small objects and smooths the contours of larger ones. It is equivalent to taking the erosion of the input image and then the dilation of the result.   
- Closing is a combination of dilation followed by erosion. It fills small holes and gaps and fuses narrow breaks. It is equivalent to taking the dilation of the input image and then the erosion of the result.   
- Other morphological operations include morphological gradient, top hat, black hat, hit-or-miss, thinning, thickening, skeletonization, etc. They are derived from the basic operations and have various applications in image analysis.