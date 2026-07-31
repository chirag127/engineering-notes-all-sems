### Two-dimensional mathematical preliminaries for digital image processing

- A digital image is an image composed of picture elements, also known as pixels, each with finite, discrete quantities of numeric representation for its intensity or gray level that is an output from its two-dimensional functions fed as input by its spatial coordinates denoted with x, y on the x-axis and y-axis, respectively.
- A digital image can be represented as a two-dimensional function, F(x,y), where x and y are spatial coordinates, and the amplitude of F at any pair of coordinates (x,y) is called the intensity or gray level of that image at that point.
- A digital image can be considered as a two-dimensional signal or system, which can be analyzed and processed using mathematical tools such as Fourier transform, convolution, correlation, filtering, etc .
- Some basic concepts and operations related to two-dimensional signals and systems are:
  - Sampling: The process of converting a continuous image into a discrete image by taking samples of the image function at regular intervals.
  - Quantization: The process of assigning a finite number of discrete values to the sampled image function, usually by rounding off the intensity values to the nearest integer.
  - Resolution: The measure of the smallest detail that can be distinguished in an image, which depends on the number of pixels and the number of gray levels in the image.
  - Histogram: A graphical representation of the frequency distribution of the gray levels in an image, which can be used to analyze the contrast and brightness of the image.
  - Spatial domain: The domain where the image function is defined in terms of its spatial coordinates and intensity values.
  - Frequency domain: The domain where the image function is defined in terms of its frequency components and their amplitudes and phases, obtained by applying the Fourier transform to the image function.
  - Convolution: A mathematical operation that combines two functions to produce a third function, which can be used to implement linear filtering on an image.
  - Correlation: A mathematical operation that measures the similarity between two functions, which can be used to perform template matching or pattern recognition on an image.
  - Filtering: A process of modifying an image function by removing or enhancing certain frequency components, which can be used to perform noise reduction, sharpening, smoothing, etc on an image.
  - Edge detection: A process of identifying and locating the boundaries of objects or regions in an image, which can be done by finding the points where the image function has high gradients or changes abruptly.
  - Inpainting: A process of filling in the missing or corrupted parts of an image by using the information from the surrounding pixels, which can be done by using variational methods or partial differential equations.