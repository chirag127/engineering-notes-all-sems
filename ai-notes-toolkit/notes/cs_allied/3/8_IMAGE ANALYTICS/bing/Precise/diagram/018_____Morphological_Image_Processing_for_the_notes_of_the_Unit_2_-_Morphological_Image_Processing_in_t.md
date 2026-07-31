# Unit 2 - Morphological Image Processing

Morphological Image Processing is a comprehensive set of image processing operations that process images based on shapes. It applies a structuring element to an input image, creating an output image of the same size .

Fundamentally, morphological image processing is similar to spatial filtering. The structuring element is moved across every pixel in the original image to give a pixel in a new processed image. The value of this new pixel depends on the morphological operation performed .

Morphological image processing is a collection of non-linear operations related to the shape or morphology of features in an image, such as boundaries, skeletons, etc. In any given technique, we probe an image with a small shape or template called a structuring element, which defines the region of interest or neighborhood around a pixel .

Morphology is a broad set of image processing operations that process images based on shapes. In a morphological operation, each pixel in the image is adjusted based on the value of other pixels in its neighborhood. By choosing the size and shape of the neighborhood, you can construct a morphological operation that is sensitive to specific shapes in the input image .

Some common morphological operations based on OpenCV are Erosion, Dilation, Opening, Closing, Morphological Gradient, Top hat, and Black hat .