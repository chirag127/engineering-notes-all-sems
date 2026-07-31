### Morphological processing- erosion and dilation

- Morphological processing is a technique of image processing that modifies the shape and size of objects in an image using mathematical operations .
- Morphological processing can be used for image segmentation, which is the process of dividing an image into meaningful regions or objects.
- The basic morphological operations are erosion and dilation .
- Erosion is the process of removing pixels from the boundaries of objects in an image, making them smaller and smoother .
- Dilation is the process of adding pixels to the boundaries of objects in an image, making them larger and bolder .
- Erosion and dilation can be applied using a structuring element (SE), which is a small binary image that defines the neighborhood of a pixel .
- The output of erosion and dilation depends on the shape, size and position of the SE relative to the input image .
- Erosion and dilation can be combined to form more complex morphological operations, such as opening, closing, gradient, top hat and black hat .
- Opening is the process of applying erosion followed by dilation, which can remove small objects and smooth the boundaries of larger objects .
- Closing is the process of applying dilation followed by erosion, which can fill small holes and gaps and connect nearby objects .
- Gradient is the process of subtracting the eroded image from the dilated image, which can highlight the edges and boundaries of objects .
- Top hat is the process of subtracting the opened image from the original image, which can enhance the bright objects on a dark background .
- Black hat is the process of subtracting the original image from the closed image, which can enhance the dark objects on a bright background .

Here is an example of applying erosion and dilation to a binary image using a 3x3 square SE:

![Original image](https://i.imgur.com/0vZ0t7y.png)

![Eroded image](https://i.imgur.com/7w0fN0u.png)

![Dilated image](https://i.imgur.com/9cZ0Y0y.png)