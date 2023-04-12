

# Image Analytics

Image analytics is the process of extracting meaningful information from images, mainly from digital images, by using digital image processing techniques. Image analytics can be used for various purposes, such as:

- Reading bar codes, QR codes, or text from images.
- Identifying objects, faces, logos, or scenes from images .
- Measuring dimensions, distances, angles, or areas from images.
- Enhancing, restoring, or segmenting images.
- Detecting anomalies, defects, or changes from images.
- Classifying, clustering, or indexing images based on their content or features.

Image analytics can be applied to various domains, such as:

- Security and surveillance: for face recognition, biometric authentication, or threat detection.
- Healthcare and medicine: for diagnosis, treatment, or monitoring of diseases or injuries from medical images.
- Marketing and advertising: for brand recognition, sentiment analysis, or customer behavior analysis from social media images.
- Manufacturing and engineering: for quality control, inspection, or automation from industrial images.
- Education and research: for learning, teaching, or exploring new concepts or phenomena from scientific images.

Image analytics can be performed using various methods, such as:

- Pixel-based methods: that operate on the individual pixels of an image, such as thresholding, filtering, or morphological operations.
- Feature-based methods: that extract and analyze specific features from an image, such as edges, corners, or keypoints.
- Region-based methods: that divide an image into homogeneous or meaningful regions, such as segmentation, clustering, or region growing.
- Model-based methods: that use predefined or learned models to represent or interpret an image, such as template matching, shape analysis, or machine learning.

Image analytics can be challenging due to various factors, such as:

- Image quality: that can be affected by noise, blur, distortion, or compression.
- Image variability: that can result from different lighting, perspective, occlusion, or background conditions.
- Image complexity: that can depend on the number, size, shape, or appearance of the objects or features in an image.
- Image ambiguity: that can arise from multiple interpretations, meanings, or contexts of an image.



## Unit 1 - Fundamentals

- This unit covers the basic concepts and principles of computer science, such as data representation, algorithms, programming languages, and abstraction.
- Data representation is the process of encoding information in a form that can be stored and manipulated by a computer. There are different types of data, such as numbers, text, images, sound, and video, and each type has a specific way of being represented in binary, which is the language of computers.
- Algorithms are step-by-step instructions that describe how to solve a problem or perform a task. Algorithms can be expressed in different ways, such as natural language, pseudocode, flowcharts, or programming languages. Algorithms can be evaluated based on their correctness, efficiency, and readability.
- Programming languages are formal languages that allow humans to communicate with computers and create software. There are different types of programming languages, such as low-level, high-level, imperative, declarative, functional, object-oriented, and scripting languages. Each type has its own syntax, semantics, and features, and each has its own advantages and disadvantages for different applications.
- Abstraction is the process of simplifying complex problems or systems by ignoring irrelevant details and focusing on the essential features. Abstraction allows us to create models, generalizations, and classifications that help us understand and solve problems. Abstraction can be applied at different levels, such as data abstraction, procedural abstraction, and object abstraction.



### Introduction for the notes of the Unit 1 - Fundamentals in the subject of IMAGE ANALYTICS

- Image analytics is the process of extracting meaningful information from digital images using computer vision, machine learning, and artificial intelligence techniques.
- Image analytics can be used for various applications, such as face recognition, medical imaging, security, surveillance, biometrics, autonomous driving, etc.
- Image analytics involves several steps, such as image acquisition, preprocessing, segmentation, feature extraction, classification, and interpretation.
- Image acquisition is the process of capturing an image from a source, such as a camera, a scanner, or a file.
- Preprocessing is the process of enhancing the quality of an image, such as removing noise, adjusting contrast, resizing, etc.
- Segmentation is the process of dividing an image into meaningful regions, such as objects, backgrounds, edges, etc.
- Feature extraction is the process of extracting relevant information from an image, such as color, texture, shape, etc.
- Classification is the process of assigning a label to an image or a region, such as face, car, cat, etc.
- Interpretation is the process of understanding the meaning and context of an image, such as emotion, identity, action, etc.



### Fundamental steps in image processing systems

Image processing is the process of manipulating and analyzing digital images using various techniques and algorithms. Image processing can be used for various applications, such as enhancing the quality of images, detecting and recognizing objects, extracting information, and generating new images.

According to  , image processing mainly involves the following three steps:

- **Image acquisition**: This involves capturing an image using a digital camera or scanner, or importing an existing image into a computer. Image acquisition can also include preprocessing, such as scaling, cropping, filtering, and color conversion.
- **Image analysis and manipulation**: This involves applying various techniques and algorithms to the image, such as segmentation, feature extraction, edge detection, morphological operations, histogram equalization, and Fourier transform. Image analysis and manipulation can also include data compression, encryption, and watermarking.
- **Image output**: This involves displaying or storing the image, or using the image for further processing or decision making. Image output can also include postprocessing, such as interpolation, restoration, and enhancement.

Figure 1 shows a schematic diagram of the fundamental steps of image processing .

Figure 1: Fundamental steps of image processing

: https://www.geeksforgeeks.org/digital-image-processing-basics/
: https://www.mygreatlearning.com/blog/introduction-to-image-processing-what-is-image-processing/
: https://developer.ibm.com/articles/learn-the-basics-of-computer-vision-and-object-detection/



### Image Acquisition

- Image acquisition is the first step in image processing. It involves retrieving the image from a source, usually a hardware-based source.
- Image acquisition can be done by various devices, such as cameras, scanners, microscopes, sensors, etc. The devices convert the optical signals into electrical signals, which can be stored and processed by a computer.
- Image acquisition can be done for different types of images, such as grayscale, color, binary, thermal, infrared, etc. The type of image depends on the wavelength range of the optical signals and the number of channels used to represent the image.
- Image acquisition can be affected by various factors, such as noise, distortion, illumination, resolution, etc. These factors can degrade the quality of the image and affect the subsequent processing steps.
- Image acquisition can be improved by using appropriate techniques, such as filtering, enhancement, segmentation, etc. These techniques can reduce the noise, increase the contrast, separate the regions of interest, etc. in the image.



### Sampling and Quantization

- Sampling is the process of converting a continuous signal into a discrete signal by taking samples at regular intervals.
- Quantization is the process of assigning discrete values to the samples based on their amplitude levels.
- Sampling and quantization are essential steps for digital image processing, as they allow the representation and manipulation of images using binary numbers.
- The sampling rate and the quantization level determine the quality and the size of the digital image.
- The sampling rate is the number of samples taken per unit distance along the image. It affects the spatial resolution of the image, which is the ability to distinguish fine details.
- The quantization level is the number of bits used to represent each sample. It affects the intensity resolution of the image, which is the ability to distinguish different shades of gray or colors.
- The higher the sampling rate and the quantization level, the better the quality of the digital image, but also the larger the amount of data required to store and process the image.
- The lower the sampling rate and the quantization level, the poorer the quality of the digital image, but also the smaller the amount of data required to store and process the image.
- There is a trade-off between quality and size when choosing the sampling rate and the quantization level for a digital image.
- The sampling rate and the quantization level should be chosen according to the characteristics of the original image and the intended application of the digital image.



### Pixel Relationships

- Pixel relationships are the ways that pixels in an image are related to each other based on their spatial location, intensity, color, or other attributes.
- Pixel relationships are important for image analysis because they can help to identify objects, regions, boundaries, patterns, and features in an image.
- Some common pixel relationships are:

  - **Neighborhood**: The set of pixels that are adjacent to a given pixel in a specified direction or distance. For example, a 4-neighborhood of a pixel p consists of the pixels above, below, left, and right of p. A 8-neighborhood of a pixel p consists of the pixels in the 4-neighborhood plus the pixels in the four diagonal directions of p.
  - **Connectivity**: The property of pixels that are connected by a path of pixels with the same or similar attributes. For example, two pixels p and q are said to be connected in a set S if there exists a path between them consisting entirely of pixels in S. Connectivity can be used to define connected components, which are sets of pixels that are connected to each other in a given image or region.
  - **Distance**: The measure of how far apart two pixels are in an image. Distance can be defined in different ways, such as Euclidean distance, Manhattan distance, or chessboard distance. Distance can be used to compute the similarity or dissimilarity between pixels or regions, or to perform operations such as dilation, erosion, or morphological filtering.
  - **Attribution**: The assignment of a value or a label to a pixel based on its attributes or its relationship to other pixels. Attribution can be used to perform tasks such as image segmentation, classification, or recognition. Attribution can be done by using rules, thresholds, or machine learning models  .



### Mathematical Tools Used in Digital Image Processing

- A digital image is a collection of numerical values represented in the form of a matrix. Each value corresponds to the intensity or color of a pixel in the image.
- Digital image processing (DIP) is the manipulation of digital images using various mathematical and computational techniques to enhance, analyze, or transform them for various purposes.
- Some of the mathematical tools that are used in DIP are:

  - **Matrix operations**: Matrix operations such as addition, subtraction, multiplication, inversion, transpose, etc. are used to perform various image processing activities such as filtering, scaling, rotation, transformation, etc. 
  - **Set operations**: Set operations such as union, intersection, complement, difference, etc. are used to perform image processing activities such as segmentation, region of interest extraction, morphological operations, etc. 
  - **Distance functions**: Distance functions such as Euclidean, Manhattan, Chebyshev, etc. are used to measure the similarity or dissimilarity between pixels, regions, or images. They are useful for image processing activities such as clustering, classification, edge detection, etc. 
  - **Statistical methods**: Statistical methods such as mean, median, mode, standard deviation, variance, histogram, etc. are used to analyze the distribution and characteristics of the pixel values in an image. They are useful for image processing activities such as noise removal, contrast enhancement, thresholding, etc. 
  - **Fourier transform**: Fourier transform is a mathematical tool that converts a signal or an image from the spatial domain to the frequency domain. It is useful for image processing activities such as frequency filtering, compression, restoration, etc. 
  - **Wavelet transform**: Wavelet transform is a mathematical tool that converts a signal or an image from the spatial domain to the wavelet domain. It is useful for image processing activities such as multi-resolution analysis, edge detection, compression, denoising, etc. 
  - **Linear filtering**: Linear filtering is a mathematical tool that applies a linear operator to an image to produce a filtered image. It is useful for image processing activities such as smoothing, sharpening, edge detection, etc. 
  - **Nonlinear filtering**: Nonlinear filtering is a mathematical tool that applies a nonlinear operator to an image to produce a filtered image. It is useful for image processing activities such as median filtering, morphological filtering, anisotropic diffusion, etc. 
  - **Hidden Markov models**: Hidden Markov models are mathematical tools that model the stochastic behavior of a system with hidden states. They are useful for image processing activities such as segmentation, recognition, restoration, etc. 
  - **Independent component analysis**: Independent component analysis is a mathematical tool that decomposes a signal or an image into independent components. It is useful for image processing activities such as blind source separation, feature extraction, etc. 
  - **Neural networks**: Neural networks are mathematical tools that simulate the structure and function of biological neural networks. They are useful for image processing activities such as learning, classification, recognition, etc. 
  - **Partial differential equations**: Partial differential equations are mathematical tools that model the evolution of a system with respect to space and time. They are useful for image processing activities such as image inpainting, image segmentation, image restoration, etc.



### Some Basic Intensity Transformation Functions for the notes of the Unit 1 - Fundamentals in the subject of IMAGE ANALYTICS

- Intensity transformation functions are used to modify the pixel values of an image according to a mathematical expression.
- The general form of an intensity transformation function is s = T(r), where r is the input pixel value and s is the output pixel value.
- Some basic intensity transformation functions are:

  - **Identity function**: s = T(r) = r. This function does not change the pixel values of the image. It is useful for preserving the original image or for comparison purposes.
  - **Negative function**: s = T(r) = L - 1 - r, where L is the number of possible intensity levels in the image. This function creates a negative image by reversing the pixel values. It is useful for enhancing white or gray detail embedded in dark regions of an image.
  - **Logarithmic function**: s = T(r) = c log(1 + r), where c is a constant. This function maps a narrow range of low-intensity values to a wider range of output values. It is useful for expanding the values of dark pixels in an image while compressing the higher-level values. It can also be used for enhancing the details of an image taken in dark environments.
  - **Power-law function**: s = T(r) = c r^γ, where c and γ are constants. This function can be used for either contrast enhancement or contrast reduction, depending on the value of γ. If γ < 1, the function maps a narrow range of high-intensity values to a wider range of output values. It is useful for enhancing the details of an image taken in bright environments. If γ > 1, the function maps a wide range of low-intensity values to a narrow range of output values. It is useful for enhancing the details of an image with low contrast.
  - **Piecewise-linear function**: s = T(r) = a r + b, where a and b are constants. This function performs a linear transformation on the pixel values of an image. It can be used for brightness adjustment, contrast stretching, or thresholding. Brightness adjustment changes the overall intensity of an image by adding or subtracting a constant value. Contrast stretching increases the dynamic range of an image by mapping the pixel values to a larger range. Thresholding converts an image to a binary image by assigning a fixed value to pixels above or below a certain threshold.



### Image Negatives

- An image negative is a type of image that has its colors inverted, or reversed, from the original image.
- An image negative can be created by subtracting each pixel value from the maximum possible value in the image format. For example, if the image is in 8-bit grayscale, the maximum value is 255, so the negative of a pixel with value x is 255 - x.
- An image negative can be used for various purposes, such as:
  - Enhancing the contrast or visibility of low-light or dark images.
  - Creating artistic effects or filters.
  - Detecting edges or contours in images.
  - Performing image subtraction or difference operations.



### Log Transformations

- Log transformations are a type of point operations that are used to enhance the contrast of an image, especially in the dark regions.
- Log transformations map a narrow range of low intensity values in the input image to a wider range of output values, while compressing the high intensity values.
- Log transformations are useful for images with large dynamic range, such as astronomical images, medical images, or images captured in low-light conditions.
- The general formula for log transformations is:

$$s = c \log(1 + r)$$

where $s$ is the output pixel value, $r$ is the input pixel value, and $c$ is a constant that controls the slope of the transformation curve.

- The constant $c$ can be determined by the desired output range, such as $[0, L-1]$, where $L$ is the number of gray levels in the image. In that case, $c = \frac{L-1}{\log(1 + r_{\max})}$, where $r_{\max}$ is the maximum input pixel value.
- Log transformations have the following properties:
  - They are monotonic, meaning that they preserve the order of pixel values in the image.
  - They are invertible, meaning that they can be reversed by applying the inverse transformation, which is:

  $$r = \exp(\frac{s}{c}) - 1$$

  - They are nonlinear, meaning that they change the relative brightness of different regions in the image.



### Power-Law Transformations for the notes of the Unit 1 - Fundamentals in the subject of IMAGE ANALYTICS

- Power-law transformations are a class of image enhancement techniques that modify the pixel values of an image according to a mathematical function of the form `s = c * r^gamma`, where `s` and `r` are the output and input pixel values, respectively, `c` is a positive constant, and `gamma` is a parameter that controls the shape of the transformation.
- Power-law transformations are also known as **gamma corrections** or **contrast adjustments** because they can be used to change the contrast of an image by altering the distribution of pixel values.
- Power-law transformations can be applied to grayscale or color images, but they are more commonly used for grayscale images. For color images, the transformation can be applied to each color channel separately or to a single channel that represents the luminance or intensity of the image.
- Power-law transformations can be implemented using a lookup table (LUT) that maps each input pixel value to an output pixel value according to the power-law function. The LUT can be precomputed and stored in memory for fast processing.
- Power-law transformations can be visualized using a plot of the output pixel values versus the input pixel values, which is called a **transformation function** or a **transformation curve**. The shape of the curve depends on the value of `gamma` and the range of the input and output pixel values.
- Power-law transformations have different effects on the image depending on the value of `gamma`:
  - If `gamma` is equal to 1, the transformation is a linear function that does not change the image.
  - If `gamma` is less than 1, the transformation is a concave function that maps a narrow range of low input values to a wider range of output values, and a wide range of high input values to a narrow range of output values. This increases the contrast of the dark regions and decreases the contrast of the bright regions of the image. This is useful for enhancing images that are too bright or have low contrast.
  - If `gamma` is greater than 1, the transformation is a convex function that maps a wide range of low input values to a narrow range of output values, and a narrow range of high input values to a wider range of output values. This decreases the contrast of the dark regions and increases the contrast of the bright regions of the image. This is useful for enhancing images that are too dark or have low contrast.
- Power-law transformations can be combined with other image enhancement techniques, such as histogram equalization, to achieve better results. For example, applying a power-law transformation with `gamma` less than 1 before histogram equalization can improve the contrast of the dark regions of the image, while applying a power-law transformation with `gamma` greater than 1 after histogram equalization can improve the contrast of the bright regions of the image.



### Histogram Processing

- Histogram processing is a technique for enhancing the contrast and brightness of an image by manipulating its histogram.
- A histogram is a graphical representation of the distribution of pixel values in an image. It shows how many pixels have a certain intensity value, ranging from 0 (black) to 255 (white) for a grayscale image.
- Histogram processing can be divided into two categories: histogram equalization and histogram specification.
- Histogram equalization is a method that transforms the histogram of an image so that it becomes more uniform, meaning that all intensity values have roughly the same frequency. This can improve the contrast and visibility of the image features.
- Histogram specification is a method that transforms the histogram of an image so that it matches a desired histogram, which can be derived from another image or a predefined function. This can modify the appearance and mood of the image according to the desired histogram.
- Histogram processing can be applied to the whole image or to local regions of the image, depending on the desired effect and the characteristics of the image.



### Color Fundamentals

- Color is a property of light that depends on the wavelength and intensity of the electromagnetic (EM) radiation.
- Color can be perceived by the human eye or measured by a device, such as a camera or a spectrometer.
- Color can be represented and processed in different ways, depending on the application and the device.
- Some of the common color models are:
  - RGB: Red, Green, and Blue are the primary colors of light. Any color can be obtained by mixing different amounts of these three colors. RGB is used for displaying images on monitors, TVs, and projectors.
  - CMYK: Cyan, Magenta, Yellow, and Black are the primary colors of ink. Any color can be obtained by subtracting different amounts of these four colors from white. CMYK is used for printing images on paper, magazines, and books.
  - HSV: Hue, Saturation, and Value are the attributes of color perception. Hue is the color name, such as red, green, or blue. Saturation is the intensity or purity of the color. Value is the brightness or darkness of the color. HSV is used for selecting and adjusting colors in image editing software.
  - YCbCr: Luminance, Chrominance Blue, and Chrominance Red are the components of color video signals. Luminance is the brightness or grayscale information of the image. Chrominance Blue and Chrominance Red are the color difference signals that indicate how much blue and red are present in the image. YCbCr is used for compressing and transmitting color video data.
- Color image processing involves manipulating and analyzing color images for various purposes, such as enhancement, segmentation, recognition, and compression.
- Some of the common techniques for color image processing are:
  - Color space conversion: Changing the color representation of an image from one model to another, such as from RGB to HSV or from YCbCr to RGB.
  - Color correction: Adjusting the color balance, contrast, brightness, and saturation of an image to improve its appearance or match a reference image.
  - Color quantization: Reducing the number of colors in an image to save memory or bandwidth, or to create a stylized effect.
  - Color segmentation: Partitioning an image into regions that have similar or homogeneous colors, such as skin, hair, or background.
  - Color feature extraction: Computing numerical or statistical descriptors of the color distribution, variation, or pattern of an image or a region, such as color histogram, color moments, or color texture.
  - Color classification: Assigning a label or a category to an image or a region based on its color features, such as face detection, fruit recognition, or traffic sign identification.



### Fundamentals of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering is the process of assigning the value of a pixel based on its neighbors. The filters or masks, which are also known as kernels, used in the process are small matrices run in the entire image through a convolution process.
- Spatial filtering can be used for various purposes, such as enhancing, smoothing, sharpening, or detecting edges in an image.
- Spatial filtering can be classified into two types: linear and nonlinear.
  - Linear spatial filtering is based on the principle of superposition, which means that the output of the filter is a linear combination of the input pixels and the filter coefficients.
  - Nonlinear spatial filtering does not follow the principle of superposition, and the output of the filter depends on the rank, order, or magnitude of the input pixels.
- Some examples of linear spatial filters are averaging filter, weighted averaging filter, Gaussian filter, and Laplacian filter.
  - Averaging filter is used to reduce the detail or noise in an image by replacing each pixel with the average of its neighboring pixels.
  - Weighted averaging filter is similar to averaging filter, but it assigns different weights to the neighboring pixels according to their distance from the center pixel.
  - Gaussian filter is a weighted averaging filter that uses a Gaussian function as the weight function. It is used to smooth an image while preserving the edges.
  - Laplacian filter is a second-order derivative filter that is used to enhance or sharpen an image by highlighting the regions of rapid intensity change.
- Some examples of nonlinear spatial filters are median filter, max filter, min filter, and adaptive filter.
  - Median filter is used to remove salt-and-pepper noise or impulse noise from an image by replacing each pixel with the median of its neighboring pixels.
  - Max filter is used to enhance the bright regions or highlight the maximum values in an image by replacing each pixel with the maximum of its neighboring pixels.
  - Min filter is used to enhance the dark regions or highlight the minimum values in an image by replacing each pixel with the minimum of its neighboring pixels.
  - Adaptive filter is a filter that adjusts its parameters according to the local characteristics of the image, such as noise level, contrast, or edge strength.



### Smoothing Spatial Filters

- Smoothing spatial filters are used for reducing and suppressing image noise, such as random variations in pixel values, salt-and-pepper noise, or Gaussian noise .
- Smoothing spatial filters can also be used for blurring and removing small details from an image, such as edges, corners, or textures. This can be useful for preprocessing steps before object extraction, segmentation, or recognition.
- Smoothing spatial filters operate in the spatial domain, which means they use a mask or a kernel that slides over the image and applies a mathematical operation to the pixels in the neighborhood of the mask . The output pixel value is the result of the operation, which can be a linear or a non-linear function of the input pixels  .
- Smoothing spatial filters can be classified into two main types: linear filters and order-statistics filters .
  - Linear filters, also known as mean filters, use a simple average of the pixels in the neighborhood of the mask to compute the output pixel value . Linear filters are easy to implement and fast to compute, but they tend to blur the edges and produce ringing artifacts . Examples of linear filters are box filter, Gaussian filter, and bilateral filter .
  - Order-statistics filters, also known as non-linear filters, use a sorting operation on the pixels in the neighborhood of the mask to compute the output pixel value . Order-statistics filters are more robust to noise and can preserve the edges better than linear filters, but they are more complex and slower to compute . Examples of order-statistics filters are median filter, min filter, max filter, and alpha-trimmed mean filter .
- Smoothing spatial filters can be applied to grayscale or color images, but the mask size and shape, and the operation function may vary depending on the image characteristics and the desired effect  . Smoothing spatial filters can also be combined with other image processing techniques, such as sharpening, edge detection, or thresholding, to enhance the image quality or extract features .



### Sharpening Spatial Filters

- Sharpening spatial filters are used to enhance the edges and fine details of an image by removing blur and smoothing  .
- Sharpening spatial filters operate in the spatial domain by directly manipulating the image pixels.
- Sharpening spatial filters are based on the first and second order derivatives of the image intensity function .
- The first order derivative sharpening filters, such as the gradient and the Laplacian filters, highlight the transitions in intensity and produce thicker edges .
- The second order derivative sharpening filters, such as the Laplacian of Gaussian and the difference of Gaussian filters, highlight the fine details and produce thinner edges .
- Sharpening spatial filters can be implemented by using convolution with a kernel that has a negative central coefficient and positive peripheral coefficients .
- Sharpening spatial filters can enhance the image contrast and visibility, but they can also introduce noise and artifacts .



## Unit 2 - Morphological Image Processing

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be combined to form more complex operations such as opening, closing, boundary extraction, and skeletonization.
- Erosion is the operation that shrinks an object by removing pixels from its boundary, while dilation is the operation that expands an object by adding pixels to its boundary.
- Opening is the operation that smooths the contour of an object and removes small protrusions, while closing is the operation that fills small gaps and holes in an object.
- Boundary extraction is the operation that extracts the edge of an object by subtracting the eroded image from the original image, while skeletonization is the operation that reduces an object to a thin line that preserves its topology and shape.
- Morphological image processing can be applied to binary images, which have only two pixel values (0 and 1), or to grayscale images, which have a range of pixel values (0 to 255).
- For binary images, the structuring element is also binary, and the operations are defined by set operations such as intersection, union, and complement.
- For grayscale images, the structuring element is also grayscale, and the operations are defined by the minimum and maximum values of the pixels under the structuring element.



### Morphological Image Processing

- Morphological image processing is a collection of non-linear operations that process images based on shapes or morphology of features in an image  .
- Morphological operations apply a structuring element to an input image, creating an output image of the same size. The structuring element is a small binary image that defines the region of interest or neighborhood around a pixel.
- The value of each pixel in the output image depends on the morphological operation performed and the values of the pixels in the neighborhood defined by the structuring element .
- Morphological operations can be classified into two categories: basic and advanced.
- Basic morphological operations include erosion, dilation, opening, and closing  .
  - Erosion shrinks the foreground regions by removing pixels from the boundaries  . It can be used to remove noise, detach connected objects, and thin out objects.
  - Dilation expands the foreground regions by adding pixels to the boundaries  . It can be used to fill holes, connect disjoint objects, and thicken objects.
  - Opening is a combination of erosion followed by dilation  . It can be used to remove small objects, smooth boundaries, and separate objects.
  - Closing is a combination of dilation followed by erosion  . It can be used to fill small gaps, smooth boundaries, and merge objects.
- Advanced morphological operations include morphological gradient, top hat, black hat, hit-or-miss, skeletonization, and watershed  .
  - Morphological gradient is the difference between dilation and erosion of an image  . It can be used to highlight the boundaries of objects.
  - Top hat is the difference between the input image and its opening  . It can be used to enhance bright objects on a dark background.
  - Black hat is the difference between the closing and the input image  . It can be used to enhance dark objects on a bright background.
  - Hit-or-miss is a morphological operation that matches a specific pattern in the input image . It can be used to find particular shapes or features in an image.
  - Skeletonization is a morphological operation that reduces an object to a thin skeleton that preserves its topology and connectivity . It can be used to represent the shape and structure of an object in a compact way.
  - Watershed is a morphological operation that segments an image based on the intensity gradients . It can be used to separate touching or overlapping objects in an image.
- Morphological image processing can be applied to various domains such as biomedical imaging, document analysis, industrial inspection, and remote sensing .



### Fundamentals for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be combined to form more complex operations such as opening, closing, thinning, thickening, skeletonization, etc.
- Erosion is the operation that shrinks an object by removing pixels from its boundary, while dilation is the operation that expands an object by adding pixels to its boundary.
- Opening is the operation that smooths the contour of an object and removes small protrusions, while closing is the operation that fills small gaps and holes in an object.
- Thinning is the operation that reduces an object to a one-pixel wide skeleton, while thickening is the operation that adds pixels to the skeleton to make it thicker.
- Skeletonization is the operation that extracts the skeleton of an object, which is the set of pixels that are equidistant from the object's boundary.
- Morphological image processing can be applied to binary images, which have only two pixel values (0 and 1), or to grayscale images, which have a range of pixel values (0 to 255).
- For binary images, the structuring element is also binary, and the operations are defined by set operations such as intersection, union, complement, etc.
- For grayscale images, the structuring element can be binary or grayscale, and the operations are defined by minima and maxima of pixel values.



### Erosion and Dilation

- Erosion and dilation are basic morphological processing operations that produce contrasting results when applied to either gray-scale or binary images.
- Erosion involves the removal of pixels at the edges of the region, while dilation involves the addition of pixels to the boundaries of the region .
- The number of pixels added or removed from the objects in an image depends on the size and shape of the structuring element used to process the image .
- Erosion and dilation are often used in combination to implement image processing operations, such as opening, closing, top-hat, and bottom-hat.
- Erosion and dilation have a wide array of uses, such as removing noise, isolating individual elements, joining disparate elements, enhancing edges, and extracting features in an image.



### Opening and Closing

- Opening and closing are two important operations in morphological image processing that can be used to smooth the contours of an object, eliminate small holes or gaps, and join narrow breaks or cracks.
- Opening is defined as the erosion of an image by a structuring element, followed by the dilation of the eroded image by the same structuring element. Opening can remove small objects or protrusions from an image, while preserving the shape and size of larger objects.
- Closing is defined as the dilation of an image by a structuring element, followed by the erosion of the dilated image by the same structuring element. Closing can fill small holes or gaps in an image, while preserving the shape and size of larger objects.
- Opening and closing are dual operations, meaning that the opening of the complement of an image by a structuring element is equal to the complement of the closing of the image by the same structuring element, and vice versa.
- Opening and closing are idempotent operations, meaning that applying them repeatedly does not change the result. They are also increasing operations, meaning that they do not decrease the value of any pixel in the image.
- Opening and closing can be combined to create more complex morphological transformations, such as opening by reconstruction, closing by reconstruction, morphological gradient, top-hat transform, and bottom-hat transform. These transformations can enhance or extract specific features from an image, such as edges, peaks, or valleys.



### Hit or Miss Transform

- Hit or miss transform is a morphological operation that detects a given configuration or pattern in a binary image, using the morphological erosion operator and a pair of disjoint structuring elements .
- The hit or miss transform can be defined as follows:

  - Let \\(A\\) be a binary image and \\(B = (B_1, B_2)\\) be a pair of disjoint structuring elements, such that \\(B_1 \cap B_2 = \emptyset\\).
  - The hit or miss transform of \\(A\\) by \\(B\\) is given by:

    \\[A \otimes B = (A \ominus B_1) \cap (A^c \ominus B_2)\\]

  - where \\(A^c\\) is the complement of \\(A\\), \\(\ominus\\) is the erosion operator, and \\(\cap\\) is the intersection operator.
  - The hit or miss transform indicates the positions where a certain pattern (characterized by the composite structuring element \\(B\\)) occurs in the input image.
- The hit or miss transform can be used for various applications, such as :

  - Pruning: identifying and removing the end-points of a line to eliminate unwanted branches.
  - Thinning: iteratively applying the hit or miss transform with different structuring elements to reduce the thickness of an object to one pixel.
  - Thickening: iteratively applying the hit or miss transform with different structuring elements to increase the thickness of an object by one pixel.
  - Skeletonization: finding the medial axis of an object by applying the hit or miss transform with structuring elements of increasing size until the object disappears.
  - Pattern matching: finding the locations of a template in an image by using the hit or miss transform with the template as the structuring element.

- The hit or miss transform can be implemented using various libraries, such as OpenCV or Mahotas.



### Some Basic Morphological Algorithms

Morphological image processing is a set of techniques that process images based on their shapes. It is useful for extracting features, describing shapes, and recognizing patterns in images. Morphological operations act on image pixels using predefined kernels, called structuring elements, that define patterns to be matched or modified in the image. Some of the basic morphological algorithms are:

- **Dilation**: This operation enlarges or expands the foreground regions (usually white pixels) in an image. It can be used to fill small holes, connect gaps, or increase the size of objects. The dilation of an image A by a structuring element B is defined as the set of all pixels x such that B, translated by x, overlaps with at least one pixel in A .
- **Erosion**: This operation shrinks or reduces the foreground regions in an image. It can be used to remove small noise, detach connected objects, or thin the boundaries of objects. The erosion of an image A by a structuring element B is defined as the set of all pixels x such that B, translated by x, is contained in A .
- **Opening**: This operation is a combination of erosion followed by dilation. It can be used to remove small objects or noise from an image, while preserving the shape and size of larger objects. The opening of an image A by a structuring element B is defined as the dilation of the erosion of A by B .
- **Closing**: This operation is a combination of dilation followed by erosion. It can be used to fill small holes or gaps in an image, while preserving the shape and size of larger objects. The closing of an image A by a structuring element B is defined as the erosion of the dilation of A by B .
- **Hit-or-miss transform**: This operation is a special case of erosion that uses two structuring elements, one for the foreground and one for the background. It can be used to find specific patterns or shapes in an image that match the structuring elements. The hit-or-miss transform of an image A by two structuring elements B1 and B2 is defined as the intersection of the erosion of A by B1 and the erosion of the complement of A by B2 .
- **Boundary extraction**: This operation is used to find the edges or contours of objects in an image. It can be done by subtracting the erosion of an image from the original image. The boundary extraction of an image A by a structuring element B is defined as A minus the erosion of A by B .
- **Morphological gradient**: This operation is used to find the difference between the dilation and the erosion of an image. It can be used to highlight the regions of rapid intensity change in an image. The morphological gradient of an image A by a structuring element B is defined as the dilation of A by B minus the erosion of A by B .
- **Morphological reconstruction**: This operation is used to extract connected components or regions of interest from an image, based on a marker image that specifies the seeds or starting points. It can be done by iteratively dilating the marker image until it reaches the boundary of the original image. The morphological reconstruction of an image A from a marker image F by a structuring element B is defined as the geodesic dilation of F in A by B .
- **Watershed transform**: This operation is used to segment an image into regions based on the local minima or catchment basins of the image gradient. It can be done by flooding the image from the minima and creating dams or boundaries when different regions meet. The watershed transform of an image A is defined as the set of pixels that belong to the boundaries of the catchment basins of A .



### Morphological Reconstruction

- Morphological reconstruction is a technique to extract or enhance marked objects from an image without changing their size or shape .
- Morphological reconstruction uses two images: a marker image and a mask image. The marker image specifies the regions of interest, while the mask image defines the boundaries of the objects.
- Morphological reconstruction is based on the concept of geodesic dilation, which is a dilation operation that is constrained by the mask image. Geodesic dilation can be iterated until the image values stop changing, resulting in the morphological reconstruction of the marker image by the mask image .
- Morphological reconstruction can be used for various applications, such as:
  - Filling holes and gaps in objects.
  - Smoothing object boundaries while preserving their size and shape.
  - Extracting the image foreground from the background.
  - Removing noise and small details from an image.
  - Segmenting objects based on their connectivity.
- Morphological reconstruction can be performed using different methods, such as:
  - Binary reconstruction, which operates on binary images and uses logical operations.
  - Grayscale reconstruction, which operates on grayscale images and uses arithmetic operations.
  - Hybrid reconstruction, which combines binary and grayscale reconstruction to process color images.



### Grayscale Morphology

- Grayscale morphology is an image processing technique used to produce a modified image from an original image by applying a set of mathematical operations.
- It is used to modify the shapes and patterns of objects in an image without changing their identities.
- Grayscale image processing can be identified by analyzing the amount of shades of gray present in the image. Generally, the more shades of gray present in the image, the higher the level of image processing. This is because the more gray values present, the more detail can be interpreted from the image.
- Grayscale morphology is based on the concepts of umbrae and structuring elements. Umbrae are sets of points in a grayscale image that have gray values greater than or equal to a given threshold. Structuring elements are small shapes that are used to probe the image and perform the morphological operations.
- The basic morphological operations are dilation and erosion. Dilation is the process of expanding the boundaries of the objects in an image by adding pixels to the edges. Erosion is the process of shrinking the boundaries of the objects in an image by removing pixels from the edges.
- Dilation and erosion can be combined to form more complex operations, such as opening and closing. Opening is the process of applying erosion followed by dilation to an image. It is used to remove small objects and noise from an image. Closing is the process of applying dilation followed by erosion to an image. It is used to fill small holes and gaps in an image.
- Grayscale morphology can be applied to various applications, such as edge detection, noise removal, image enhancement, image segmentation, and image analysis.



## Unit 3 - Image Segmentation

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, intensity, shape, etc.
- Image segmentation can be used for various applications, such as object detection, face recognition, medical imaging, scene understanding, etc.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised segmentation uses labeled data to train a model that can segment new images based on the learned features and classes.
  - Unsupervised segmentation does not use any labels, but relies on clustering or grouping pixels based on their similarity or dissimilarity.
- Some common methods for image segmentation are:
  - Thresholding: This method uses a global or local threshold value to separate the foreground and background pixels based on their intensity values.
  - Edge detection: This method uses filters or operators to detect the boundaries or edges of the regions in an image based on the changes in intensity or gradient.
  - Region growing: This method starts from a seed pixel and expands the region by adding neighboring pixels that satisfy some homogeneity criterion, such as color, texture, etc.
  - Region splitting and merging: This method recursively divides an image into smaller regions until each region is homogeneous or meets some stopping criterion, and then merges adjacent regions that are similar or compatible.
  - Watershed: This method treats an image as a topographic surface, where the intensity values represent the height, and finds the catchment basins or valleys that separate the regions based on the local minima or maxima.
  - K-means clustering: This method partitions the pixels into K clusters based on their feature vectors, such as color, intensity, location, etc., by minimizing the within-cluster variance and maximizing the between-cluster variance.
  - Mean shift clustering: This method iteratively shifts each pixel to the mode or peak of the feature space density, which represents the cluster center, by using a kernel function and a bandwidth parameter.
  - Graph cut: This method models an image as a weighted graph, where the nodes are the pixels and the edges are the pairwise similarities or dissimilarities, and finds the minimum cut or partition that separates the regions based on some energy function or cost function.
  - Neural networks: This method uses deep learning models, such as convolutional neural networks (CNNs) or recurrent neural networks (RNNs), to learn the features and labels of the regions from a large amount of training data, and then applies them to segment new images.



### Introduction for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, intensity, shape, etc.
- Image segmentation is useful for many applications, such as object detection, recognition, tracking, medical imaging, scene understanding, etc.
- Image segmentation can be classified into two types: supervised and unsupervised.
  - Supervised segmentation uses prior knowledge or labels to guide the segmentation process, such as edge detection, region growing, watershed, etc.
  - Unsupervised segmentation does not use any prior knowledge or labels, but relies on the inherent properties of the image, such as clustering, thresholding, histogram analysis, etc.
- Image segmentation can also be classified into two levels: pixel-level and region-level.
  - Pixel-level segmentation assigns a label to each pixel in the image, such as binary segmentation, gray-level segmentation, color segmentation, etc.
  - Region-level segmentation groups pixels into larger regions based on some similarity or homogeneity measure, such as region merging, region splitting, graph-based segmentation, etc.
- Image segmentation is a challenging task, as there is no unique or optimal way to segment an image, and the segmentation results may depend on the application, the user, and the context.



### Points for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing a digital image into subgroups called image segments, reducing the complexity of the image and enabling further processing or analysis of each image segment.
- Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images .
- Image segmentation is the assignment of labels to pixels to identify objects, people, or other important elements in the image.
- Image segmentation can be done based on different criteria, such as color, intensity, texture, shape, or semantic meaning.
- Image segmentation can be classified into two main types: supervised and unsupervised.
- Supervised image segmentation uses a predefined set of labels or classes and a training dataset to learn how to segment an image.
- Unsupervised image segmentation does not use any prior knowledge or labels and relies on clustering or grouping pixels based on their similarity or dissimilarity.
- Some of the common techniques for image segmentation are:
  - Thresholding: This technique divides an image into two or more regions based on a predefined threshold value or range of values for the pixel intensity or color.
  - Region-based: This technique grows or merges regions based on some homogeneity or similarity criteria, such as pixel intensity, color, or texture.
  - Edge-based: This technique detects the edges or boundaries of objects or regions in an image using filters, gradients, or edge detectors.
  - Clustering: This technique groups pixels into clusters based on their feature vectors, such as color, intensity, or texture, using algorithms such as K-means, Fuzzy C-means, or Mean-shift.
  - Graph-based: This technique models an image as a graph, where nodes represent pixels or regions and edges represent the similarity or dissimilarity between them, and uses algorithms such as Graph-cut, Normalized-cut, or Markov Random Field to partition the graph into segments.
  - Deep learning: This technique uses neural networks, such as Convolutional Neural Networks (CNNs), Fully Convolutional Networks (FCNs), or U-Nets, to learn the features and labels for image segmentation from a large amount of data.



### Line for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, intensity, shape, etc.
- Image segmentation has many applications, such as object detection, face recognition, medical imaging, scene understanding, etc.
- Image segmentation can be classified into two types: supervised and unsupervised.
  - Supervised segmentation uses a labeled dataset to train a model that can segment new images based on the learned features and classes.
  - Unsupervised segmentation does not use any labels, but relies on clustering or grouping pixels based on their similarity or dissimilarity.
- Some common methods for image segmentation are:
  - Thresholding: This method uses a global or local threshold value to separate the foreground and background pixels based on their intensity values.
  - Edge detection: This method uses filters or operators to detect the boundaries or edges of the regions in an image based on the changes in intensity or gradient.
  - Region growing: This method starts from a seed pixel and expands the region by adding neighboring pixels that satisfy some homogeneity criterion, such as color, texture, etc.
  - Region splitting and merging: This method recursively divides an image into smaller regions until each region is homogeneous or meets some stopping criterion, and then merges adjacent regions that are similar or compatible.
  - Watershed: This method treats an image as a topographic surface, where the intensity values represent the height, and finds the catchment basins or valleys that correspond to the regions, and the watershed lines or ridges that correspond to the boundaries.
  - K-means clustering: This method partitions the pixels into k clusters based on their feature vectors, such as color, texture, etc., by minimizing the within-cluster variance and maximizing the between-cluster variance.
  - Mean shift clustering: This method iteratively shifts each pixel to the mode or peak of the feature space density, which represents the cluster center, by using a kernel function and a bandwidth parameter.
  - Graph cut: This method models an image as a weighted graph, where the nodes represent the pixels and the edges represent the similarity or dissimilarity between the pixels, and finds the minimum cut or partition that separates the graph into two or more subgraphs that correspond to the regions.
  - Neural networks: This method uses deep learning models, such as convolutional neural networks (CNNs), recurrent neural networks (RNNs), or generative adversarial networks (GANs), to learn the features and the segmentation map from the input image, either in a pixel-wise or a region-wise manner.



### Edge Detection

- Edge detection is an image processing technique for finding the boundaries of objects within images .
- It works by detecting discontinuities in brightness or color .
- Edge detection is used for image segmentation and data extraction in areas such as image processing, computer vision, and machine vision .
- Image segmentation is the process of partitioning images into sets of pixels that share certain characteristics such as color, brightness, intensity, or texture.
- Edge detection allows users to observe the features of an image that have a significant change in the gray level.
- Edge detection operators are mathematical filters that are applied to an image to enhance the edges and reduce the noise.
- Some common edge detection operators are:
  - Sobel operator: It performs a 2-D spatial gradient measurement on an image and emphasizes regions of high spatial gradient that correspond to edges.
  - Prewitt operator: It is similar to the Sobel operator, but uses a simpler mask to approximate the gradient.
  - Roberts operator: It uses a pair of 2x2 masks to compute the diagonal gradient of an image.
  - Canny operator: It is a multi-stage algorithm that combines noise reduction, gradient estimation, non-maximum suppression, and hysteresis thresholding to produce optimal edges.
  - Laplacian operator: It is a second-order derivative operator that detects edges by finding the zero crossings of the Laplacian of an image.
- Edge detection techniques can be classified into two categories: gradient-based and laplacian-based.
  - Gradient-based techniques use the first-order derivative of the image intensity to locate the edges, such as Sobel, Prewitt, Roberts, and Canny operators.
  - Laplacian-based techniques use the second-order derivative of the image intensity to locate the edges, such as Laplacian, Laplacian of Gaussian, and Difference of Gaussian operators.
- Edge detection techniques have some limitations, such as:
  - They are sensitive to noise and may produce false or missing edges.
  - They may not be able to detect curved or thin edges.
  - They may not be able to distinguish between edges of different objects or regions.
  - They may not be able to handle complex or textured images.
- Edge detection techniques can be improved by using some methods, such as:
  - Applying noise reduction techniques before edge detection, such as Gaussian smoothing or median filtering.
  - Using adaptive or dynamic thresholding to select the optimal edge strength.
  - Using edge linking or contour tracing algorithms to connect the edge pixels into meaningful boundaries.
  - Using edge enhancement techniques to sharpen the edges, such as unsharp masking or high-boost filtering.
  - Using edge fusion techniques to combine the results of different edge detection operators.
  - Using edge evaluation techniques to measure the quality of the edge detection, such as edge density, edge strength, edge orientation, or edge localization.



### Thresholding for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, intensity, texture, etc.
- Image thresholding is a type of image segmentation that divides the foreground from the background in an image by using a threshold value.
- A threshold value is a pixel intensity level that separates the pixels into two classes: one class for pixels above the threshold and another class for pixels below the threshold.
- A binary image is an image whose pixels have only two values: 0 and 1. A binary image can be obtained from a grayscale image by applying a thresholding operation.
- Thresholding can be used for various applications, such as edge detection, object detection, text recognition, medical image analysis, etc.
- There are different types of thresholding methods, such as global thresholding, local thresholding, adaptive thresholding, Otsu's method, etc.
- Global thresholding is a simple and widely used method that applies the same threshold value to the whole image. It is suitable for images with uniform illumination and contrast.
- Local thresholding is a method that applies different threshold values to different regions of the image based on the local characteristics of the image. It is suitable for images with non-uniform illumination and contrast.
- Adaptive thresholding is a method that adjusts the threshold value dynamically according to the image content and context. It is suitable for images with complex and varying backgrounds.
- Otsu's method is a popular and efficient method that automatically determines the optimal threshold value by maximizing the inter-class variance of the pixel intensities. It is suitable for images with bimodal histograms.

- The following diagram illustrates the concept of thresholding:

Thresholding

- The following code snippet shows how to perform global thresholding using OpenCV in Python:

```python
import cv2
# Read the grayscale image
img = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
# Apply global thresholding with a threshold value of 127
ret, thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# Display the original and thresholded images
cv2.imshow('Original', img)
cv2.imshow('Thresholded', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
```



### Foundation for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, intensity, shape, etc.
- Image segmentation can be used for various applications, such as object detection, face recognition, medical imaging, scene understanding, etc.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised segmentation uses prior knowledge or labels to guide the segmentation process, such as edge detection, region growing, watershed, etc.
  - Unsupervised segmentation does not use any prior knowledge or labels, but relies on the intrinsic properties of the image, such as clustering, thresholding, histogram analysis, etc.
- Image segmentation can be further categorized into four levels: pixel-level, region-level, object-level, and semantic-level.
  - Pixel-level segmentation assigns a label to each pixel in the image, such as binary segmentation, gray-level segmentation, color segmentation, etc.
  - Region-level segmentation groups pixels into homogeneous regions based on some similarity measure, such as region growing, region splitting and merging, etc.
  - Object-level segmentation identifies and separates the objects of interest from the background, such as contour-based segmentation, shape-based segmentation, etc.
  - Semantic-level segmentation assigns a meaningful label to each region or object in the image, such as scene segmentation, face segmentation, etc.
- Image segmentation can be evaluated using various metrics, such as accuracy, precision, recall, F1-score, IoU, etc.



### Basic Global Thresholding for Image Segmentation

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as intensity, color, texture, etc.
- Thresholding is one of the simplest and most common techniques for image segmentation, which generates a binary image from a grayscale image by separating it into two regions based on a threshold value.
- A binary image is one whose pixels have only two values - 0 and 1 - and thus requires only one bit to store pixel intensity.
- A threshold value is a scalar that determines which pixels belong to the foreground (object) or the background of the image, based on their intensity values.
- Global thresholding is a method that uses a single or constant threshold value for the entire image, assuming that the intensity distribution of the object and the background are sufficiently distinct and uniform.
- The basic global thresholding algorithm iteratively finds the best threshold value that minimizes the within-class variance or maximizes the between-class variance of the segmented regions.
- The algorithm is explained below :

  1. Select an initial threshold value, T, such as the mean or median of the image intensity values.
  2. Segment the image using T, that is, label each pixel as 0 (background) if its intensity is less than or equal to T, or 1 (object) otherwise.
  3. Compute the mean intensity values of the background and object regions, denoted by m0 and m1, respectively.
  4. Compute a new threshold value, T', as the average of m0 and m1, that is, T' = (m0 + m1) / 2.
  5. Repeat steps 2 to 4 until the difference between T and T' is less than a predefined tolerance, such as 1 or 0.1.
  6. The final threshold value, T, is the optimal one for segmenting the image.

- An example of global thresholding is shown below, where the original image is a grayscale image of a coin on a dark background, and the threshold value is 128.

Original image

Binary image

- Global thresholding is simple, fast, and easy to implement, but it has some limitations, such as:

  - It may not work well if the image has uneven illumination, noise, or overlapping intensity distributions of the object and the background.
  - It may not be able to segment multiple objects with different intensity levels or complex shapes.
  - It may not be robust to changes in the image acquisition conditions, such as lighting, contrast, or resolution.

- To overcome these limitations, other thresholding methods, such as adaptive, local, or multilevel thresholding, can be used, which adjust the threshold value according to the local or global characteristics of the image.



### Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance .
- Global thresholding is a process of converting a grayscale image into a binary image by using a single intensity value as a threshold .
- Otsu’s method assumes that the image contains two classes of pixels: foreground and background, and that the intensity histogram of the image is bimodal  .
- Otsu’s method finds the optimal threshold value that minimizes the within-class variance or maximizes the inter-class variance of the two classes   .
- Otsu’s method can be formulated as an optimization problem as follows :

  - Let $p_i$ be the probability of pixel intensity $i$ in the image, where $i = 0, 1, ..., L-1$ and $L$ is the number of possible intensity levels.
  - Let $T$ be the threshold value that separates the foreground and background classes, where $0 \leq T \leq L-1$.
  - Let $w_0$ and $w_1$ be the probabilities of the foreground and background classes, respectively, defined as:

    $$w_0 = \sum_{i=0}^{T-1} p_i$$

    $$w_1 = \sum_{i=T}^{L-1} p_i$$

  - Let $\mu_0$ and $\mu_1$ be the mean intensities of the foreground and background classes, respectively, defined as:

    $$\mu_0 = \frac{1}{w_0} \sum_{i=0}^{T-1} i p_i$$

    $$\mu_1 = \frac{1}{w_1} \sum_{i=T}^{L-1} i p_i$$

  - Let $\mu_T$ be the mean intensity of the entire image, defined as:

    $$\mu_T = \sum_{i=0}^{L-1} i p_i$$

  - Then, the within-class variance $\sigma_W^2$ and the inter-class variance $\sigma_B^2$ are given by:

    $$\sigma_W^2 = w_0 (\mu_0 - \mu_T)^2 + w_1 (\mu_1 - \mu_T)^2$$

    $$\sigma_B^2 = w_0 w_1 (\mu_0 - \mu_1)^2$$

  - Otsu’s method aims to find the optimal threshold value $T^*$ that minimizes $\sigma_W^2$ or maximizes $\sigma_B^2$, which are equivalent objectives. This can be done by iterating over all possible values of $T$ and computing the corresponding variances, and then choosing the value that gives the minimum or maximum variance.

- Otsu’s method has some advantages and disadvantages  :

  - Advantages:

    - It is simple and fast to implement and does not require any prior knowledge of the image characteristics.
    - It is robust to noise and illumination variations in the image.
    - It can handle images with complex and non-uniform backgrounds.

  - Disadvantages:

    - It assumes that the image histogram is bimodal, which may not be true for some images.
    - It may not perform well for images with overlapping intensity distributions of the foreground and background classes.
    - It may not be suitable for images with multiple objects or regions of interest that require different threshold values.



### Multiple Thresholds

- Multiple thresholds are a technique for image segmentation that divides an image into three or more regions based on different intensity levels .
- Multiple thresholds can be used to separate two or more objects from the background, or to highlight different parts of an object .
- Multiple thresholds can be determined by analyzing the histogram of the image, which shows the frequency of each intensity value .
- The histogram of an image with multiple thresholds usually shows three or more peaks and two or more valleys between them .
- The valleys correspond to the thresholds that separate the regions, and the peaks correspond to the dominant intensity values in each region .
- The segmented image can be obtained by assigning different labels to the pixels that fall within each threshold range .
- For example, if the thresholds are T1 and T2, then the pixels with intensity values less than T1 are labeled as 0, the pixels with intensity values between T1 and T2 are labeled as 1, and the pixels with intensity values greater than T2 are labeled as 2 .
- Multiple thresholds can be chosen manually or automatically using various methods, such as histogram sampling, entropy maximization, or clustering .
- Multiple thresholds can improve the accuracy and robustness of image segmentation, especially for images with complex or noisy backgrounds .
- Multiple thresholds can also be combined with other segmentation techniques, such as edge detection, region growing, or watershed transform, to achieve better results .



### Variable Thresholding for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as pixel intensity, color, texture, etc. 
- Image thresholding is one of the simplest and most common techniques of image segmentation, which converts a grayscale image into a binary image by assigning pixels to either foreground or background based on a threshold value.  
- Variable thresholding is a type of image thresholding that uses different threshold values for different regions of the image, instead of a single global value for the whole image. 
- Variable thresholding is useful when the image has uneven illumination or contrast, and a global threshold cannot separate the foreground and background effectively. 
- Variable thresholding can be classified into two categories: adaptive thresholding and local thresholding. 
- Adaptive thresholding is a method that determines the optimal threshold value for each pixel based on its local neighborhood, such as the mean or median intensity, standard deviation, entropy, etc.  
- Local thresholding is a method that divides the image into smaller regions or windows, and applies a global thresholding algorithm to each region separately, using either a fixed or a variable threshold value for each region.  
- Some examples of adaptive thresholding algorithms are Otsu's method, Sauvola's method, Bradley's method, etc. 
- Some examples of local thresholding algorithms are Niblack's method, Bernsen's method, Phansalkar's method, etc. 
- Image thresholding segmentation based on weighted Parzen-window estimation is a recent bi-level thresholding approach that uses a non-parametric density estimation technique to model the histogram of the image and find the optimal threshold value.



### Segmentation by Region Growing and by Region Splitting and Merging

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as color, intensity, texture, etc.
- Region-based segmentation is a type of segmentation that groups pixels into regions that are similar or homogeneous according to some predefined measure.
- Region growing and region splitting and merging are two common methods of region-based segmentation.

#### Region Growing

- Region growing is a bottom-up approach that starts with a set of seed pixels and grows regions by adding neighboring pixels that are similar to the seed pixels.
- The similarity criterion can be based on color, intensity, texture, or other features of the pixels.
- The region growing process stops when no more pixels can be added to any region, or when some predefined condition is met, such as region size, shape, or contrast.
- Region growing can be applied to gray-scale or color images, and can produce compact and smooth regions.
- Region growing can be sensitive to the choice of seed pixels and the similarity criterion, and can be affected by noise and irregular boundaries.

#### Region Splitting and Merging

- Region splitting and merging is a top-down approach that starts with the whole image as a single region and recursively splits it into smaller regions or merges adjacent regions based on some homogeneity criterion.
- The homogeneity criterion can be based on color, intensity, texture, or other features of the regions.
- The region splitting and merging process stops when no more regions can be split or merged, or when some predefined condition is met, such as region size, shape, or contrast.
- Region splitting and merging can be applied to gray-scale or color images, and can produce regions that are not necessarily compact or smooth.
- Region splitting and merging can be efficient and flexible, but can also produce over-segmentation or under-segmentation depending on the homogeneity criterion.



### Image Segmentation

- Image segmentation is the process of dividing an image into multiple regions or segments that share some common characteristics, such as color, intensity, texture, or shape.
- Image segmentation can be used for various applications, such as object detection, face recognition, medical imaging, scene understanding, and image editing.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised segmentation uses some prior knowledge or labels to guide the segmentation process, such as ground truth masks, bounding boxes, or keypoints. Supervised segmentation methods include pixel classification, region growing, graph cut, and deep learning.
  - Unsupervised segmentation does not use any prior knowledge or labels, and relies on the intrinsic properties of the image to group pixels or regions. Unsupervised segmentation methods include thresholding, clustering, edge detection, and watershed.
- Image segmentation can be evaluated using various metrics, such as accuracy, precision, recall, F1-score, IoU (intersection over union), and Dice coefficient. These metrics compare the segmented regions with the ground truth regions and measure how well they match.



### Active Contours for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Active contours, also known as snakes, are curves that can deform and move towards the boundaries of objects in an image  .
- Active contours are based on minimizing an energy functional that consists of internal and external forces  .
- Internal forces are derived from the curve properties, such as smoothness and continuity, and they tend to shrink or expand the curve  .
- External forces are derived from the image data, such as gradients, edges, and regions, and they tend to attract the curve towards the object boundaries  .
- Active contours can be classified into two types: parametric and geometric  .
- Parametric active contours use explicit representations of the curve, such as splines or polynomials, and update the curve parameters iteratively using an optimization scheme  .
- Geometric active contours use implicit representations of the curve, such as level sets or signed distance functions, and evolve the curve using partial differential equations  .
- Active contours can handle complex shapes, topological changes, and noisy images, but they also have some limitations, such as sensitivity to initialization, local minima, and parameter tuning  .
- Active contours can be combined with other techniques, such as deep learning, to improve their performance and robustness.



### Snakes and Level Sets

- Snakes or active contour models are classical methods for boundary detection and segmentation, which deform an initial contour (for 2D image) or a surface (for 3D image) towards the boundary of the desired object .
- Snakes are parametric curves that minimize an energy functional composed of internal and external forces. Internal forces are derived from the curve's shape and smoothness, while external forces are derived from the image's gradient, edge, or region information.
- Snakes can segment one component at a time and require a good initial guess of the contour or surface. They are also sensitive to noise and local minima .
- Level sets are implicit 3D surfaces where the zero-level represents the segmentation. Level sets are defined by a signed distance function that evolves according to a partial differential equation (PDE) based on geometric flow .
- Level sets can segment multiple components and handle topological changes. They are more generic and robust than snakes, but they are also more computationally expensive and require careful initialization .
- Level sets can be seen as a geometric replacement for snakes, where the contour or surface is embedded in a higher-dimensional function and evolves according to the level set equation .
- Both snakes and level sets are evolving techniques that take some time to produce the segmentation and they depend on the initial seed. They can be combined with machine learning methods to improve their performance and accuracy .



## Unit 4 - Feature Extraction

- Feature extraction is the process of transforming raw data into a set of features that can be used for machine learning tasks, such as classification, clustering, or regression.
- Features are the attributes or characteristics of the data that are relevant for the task at hand. They can be numerical, categorical, or textual.
- Feature extraction can be done in different ways, depending on the type and structure of the data. Some common methods are:

  - Dimensionality reduction: reducing the number of features by applying techniques such as principal component analysis (PCA), linear discriminant analysis (LDA), or autoencoders.
  - Feature selection: selecting a subset of features that are most informative or discriminative for the task, using methods such as filter, wrapper, or embedded approaches.
  - Feature engineering: creating new features from existing ones, using domain knowledge, mathematical transformations, or feature combinations.
  - Feature learning: learning features from the data automatically, using methods such as deep neural networks, convolutional neural networks (CNNs), or recurrent neural networks (RNNs).

- Feature extraction is an important step in machine learning, as it can improve the performance, efficiency, and interpretability of the models. It can also help to deal with issues such as high dimensionality, noise, redundancy, or missing values in the data.



### Background for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Feature extraction is the process of transforming raw image data into a more compact and meaningful representation that can be used for further analysis, such as classification, segmentation, or retrieval.
- Feature extraction aims to reduce the dimensionality and redundancy of the image data, while preserving the relevant information and discriminating power of the features.
- Feature extraction can be performed at different levels of abstraction, such as pixel-level, region-level, or object-level, depending on the application and the desired output.
- Feature extraction can be categorized into two main types: low-level and high-level features.
  - Low-level features are derived directly from the pixel values of the image, such as color, texture, shape, or edges. They are usually invariant to translation, rotation, and scaling of the image, but sensitive to noise, illumination, and occlusion. They are useful for describing the local properties and appearance of the image regions, but not the semantic meaning or the global structure of the image.
  - High-level features are derived from the low-level features or the image regions, such as keypoints, descriptors, histograms, or graphs. They are usually invariant to noise, illumination, and occlusion, but sensitive to translation, rotation, and scaling of the image. They are useful for describing the global properties and structure of the image, as well as the semantic meaning and the relationships between the image regions or objects.



### Representation for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Feature extraction is the process of transforming an initial set of measured data (such as pixel values of an image) into a set of derived values (features) that are informative, non-redundant, and suitable for subsequent learning and generalization tasks .
- Feature extraction can be performed by different methods, depending on the type and purpose of the features. Some common methods are  :
  - Calculation-based: These methods use mathematical operations and transformations to compute features from the raw data. Examples are edge detection, corner detection, histogram of oriented gradients, scale-invariant feature transform, etc.
  - Recognition-based: These methods use machine learning models to learn features from the data that are relevant for a specific task, such as classification, detection, or segmentation. Examples are convolutional neural networks, autoencoders, deep belief networks, etc.
  - Simulation-based: These methods use physical or biological models to simulate the features that are perceived by humans or animals. Examples are saliency maps, gist descriptors, biologically inspired features, etc.
- Feature extraction can be applied to various domains of image analytics, such as medical image analysis, remote sensing, face recognition, object detection, etc. Different domains may require different types of features and methods to extract them .
- Feature extraction can improve the performance and efficiency of image analytics by reducing the dimensionality, noise, and redundancy of the data, and by enhancing the discriminative and descriptive power of the features  .



### Boundary Preprocessing for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Boundary preprocessing is the process of enhancing, detecting, and extracting the boundaries of regions or objects in an image.
- Boundaries are important features that can represent the shape, size, and location of an image region or object.
- Boundary preprocessing can be divided into three main steps: boundary enhancement, boundary detection, and boundary extraction.

#### Boundary Enhancement
- Boundary enhancement is the process of improving the contrast and sharpness of the boundaries in an image.
- Boundary enhancement can be achieved by applying various filters, such as edge enhancement, gradient, Laplacian, or morphological filters.
- Boundary enhancement can help to reduce noise, blur, and ambiguity in the image and make the boundaries more visible and distinct.

#### Boundary Detection
- Boundary detection is the process of identifying the pixels that belong to the boundaries of regions or objects in an image.
- Boundary detection can be performed by applying various methods, such as thresholding, edge detection, region growing, or watershed segmentation.
- Boundary detection can help to separate the foreground from the background and to group the pixels into homogeneous regions or objects.

#### Boundary Extraction
- Boundary extraction is the process of extracting the coordinates, shape, and topology of the boundaries of regions or objects in an image.
- Boundary extraction can be performed by applying various techniques, such as contour tracing, chain coding, polygonal approximation, or Fourier descriptors.
- Boundary extraction can help to represent the boundaries in a compact and efficient way and to extract useful features, such as perimeter, area, centroid, orientation, or curvature.



### Boundary Feature Descriptors

- Boundary feature descriptors are methods that extract and represent the shape information of an object based on its boundary or contour.
- Boundary feature descriptors can be classified into two types: global and local.
- Global boundary feature descriptors use the whole boundary of the object to compute a single feature vector that characterizes the shape. Examples of global boundary feature descriptors are Fourier descriptors, moment invariants, and shape context.
- Local boundary feature descriptors use segments or points of the boundary to compute multiple feature vectors that describe the local shape properties. Examples of local boundary feature descriptors are curvature, chain code, and boundary signature.
- Boundary feature descriptors can be used for various applications such as shape recognition, shape matching, shape retrieval, and shape analysis.



### Some Basic Boundary Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Boundary descriptors are numerical or graphical features that describe the shape and contour of an object or a region in an image.
- Boundary descriptors can be used for image representation, description, classification, recognition, and matching.
- Some basic boundary descriptors are :
  - Length of the boundary: the number of pixels along the border of the object or region. It can be computed by counting the pixels or using a chain code representation.
  - Diameter of the boundary: the maximum distance between any two points on the boundary. It can be computed by finding the pair of points that have the largest Euclidean distance.
  - Curvature of the boundary: the rate of change of the slope or direction of the boundary. It can be computed by finding the angle between adjacent segments of the boundary or using a curvature scale space representation.
  - Bounding box of the boundary: the smallest rectangle that encloses the boundary. It can be computed by finding the minimum and maximum coordinates of the boundary points along the horizontal and vertical axes.
  - Convex hull of the boundary: the smallest convex polygon that contains the boundary. It can be computed by finding the extreme points of the boundary and connecting them with straight lines.



### Shape Numbers for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Shape numbers are numerical representations of the shape of an object in an image, which can be used for shape recognition and classification .
- Shape numbers can be derived from various shape features, such as boundary, contour, region, moments, Fourier descriptors, etc .
- Shape numbers can be classified into two types: global and local .
  - Global shape numbers capture the overall shape of an object, such as its area, perimeter, circularity, eccentricity, etc .
  - Local shape numbers capture the local variations of an object's boundary or contour, such as its curvature, angle, length, etc .
- Shape numbers can be computed using different methods, such as chain codes, polygonal approximation, signature, skeleton, etc .
  - Chain codes encode the direction of the boundary pixels of an object using a fixed number of symbols, such as 4 or 8 .
  - Polygonal approximation simplifies the boundary of an object by approximating it with a polygon of minimum vertices .
  - Signature represents the boundary of an object by plotting the distance or angle of each boundary pixel from a reference point or axis .
  - Skeleton reduces the object to a thin line that preserves its topology and shape features .
- Shape numbers can be used for shape-based image retrieval (SBIR), which is a technique of finding images that contain objects of similar shape to a given query image  .
  - SBIR can be performed by comparing the shape numbers of the query image and the database images using a similarity measure, such as Euclidean distance, cosine similarity, etc  .
  - SBIR can be improved by using feature selection, dimensionality reduction, and machine learning techniques, such as principal component analysis (PCA), multilayer perceptron (MLP), etc.



### Fourier Descriptors for Shape-Based Image Retrieval

- Fourier descriptors are a method of representing the shape of an object in an image by using the Fourier transform of its boundary points .
- Fourier descriptors are invariant to translation, scale, rotation and starting point of the boundary, which makes them suitable for shape matching and recognition  .
- Fourier descriptors are computed by first extracting the boundary points of the object, then converting them to a complex-valued sequence, and then applying the discrete Fourier transform (DFT) to obtain the coefficients .
- The DFT coefficients are called Fourier descriptors, and they capture the frequency components of the boundary shape. The low-frequency descriptors represent the global shape features, while the high-frequency descriptors represent the local shape details  .
- Fourier descriptors can be normalized to achieve invariance to translation, scale, rotation and starting point. Translation invariance is achieved by setting the first descriptor to zero, scale invariance is achieved by dividing all descriptors by the absolute value of the second descriptor, rotation invariance is achieved by taking the magnitude of the descriptors, and starting point invariance is achieved by shifting the phase of the descriptors  .
- Fourier descriptors can be used for shape-based image retrieval by computing the similarity between two shapes based on their descriptors. A common similarity measure is the Euclidean distance between the normalized descriptors .
- Fourier descriptors have some advantages and disadvantages. Some advantages are that they are easy to compute, they can handle complex shapes, and they can be reduced to a low-dimensional feature vector by selecting a subset of descriptors. Some disadvantages are that they are sensitive to noise, they cannot handle occlusion or deformation, and they may not capture the semantic meaning of the shape  .



### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Statistical moments are a set of numerical values that describe the shape and distribution of pixel intensities in an image or a region of an image .
- Statistical moments can be used for various purposes in image analysis, such as texture classification, object recognition, shape description, image segmentation, and image compression .
- Statistical moments can be computed for different types of images, such as grayscale, binary, color, or multispectral images.
- Statistical moments can be classified into different types, such as geometric moments, central moments, normalized central moments, Hu moments, Zernike moments, Legendre moments, etc.
- Statistical moments can be calculated for different orders, such as zeroth, first, second, third, etc. The order of a moment indicates the degree of the polynomial function that is used to weight the pixel intensities .
- Statistical moments can be calculated for different axes, such as x, y, xy, etc. The axis of a moment indicates the direction of the pixel coordinates that are used to weight the pixel intensities.
- Statistical moments can be calculated for different regions, such as the whole image, a sub-image, a contour, a mask, etc. The region of a moment indicates the spatial extent of the pixel intensities that are used to weight the pixel intensities.
- Statistical moments can be calculated using different formulas, depending on the type, order, axis, and region of the moment. The general formula for a moment of order (i,j) for a grayscale image with pixel intensities I(x,y) is given by :

M_ij = sum_x sum_y x^i y^j I(x,y)

- Statistical moments can be transformed into different forms, such as invariant moments, orthogonal moments, complex moments, etc. The transformed moments have some desirable properties, such as rotation invariance, scale invariance, translation invariance, etc .
- Statistical moments can be used to derive different features, such as mean, variance, skewness, kurtosis, entropy, etc. The features can be used to characterize the image or the region of the image in terms of its intensity distribution, contrast, smoothness, symmetry, etc .



### Regional Feature Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Regional feature descriptors are methods to extract and describe distinctive points or regions in an image that can be used for image analysis tasks such as matching, retrieval, and classification .
- Regional feature descriptors consist of two steps: feature detection and feature description .
- Feature detection is the process of finding and locating salient regions or points in an image that are invariant to changes in scale, rotation, illumination, and viewpoint  .
- Feature description is the process of computing a signature or a vector for each detected feature that captures its local appearance and neighborhood information  .
- Some examples of feature detection algorithms are Harris corner detector, SIFT, SURF, FAST, ORB, etc  .
- Some examples of feature description algorithms are SIFT, SURF, ORB, BRIEF, FREAK, LBP, etc  .
- Regional feature descriptors can be classified into two types: hand-crafted and learned .
- Hand-crafted feature descriptors are designed based on human knowledge and intuition, such as using gradients, histograms, or binary patterns to represent local patches .
- Learned feature descriptors are obtained by training deep neural networks on large-scale datasets to learn the optimal representation for each feature .
- Regional feature descriptors can be further encoded by methods such as Bag of Words (BoW), Vector of Locally Aggregated Descriptors (VLAD), or Fisher Vector (FV) to generate a global feature representation for the whole image .



### Some Basic Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Feature extraction is the process of transforming an image into a set of numerical or symbolic features that can be used for further analysis, classification, or recognition.
- Features can be extracted from different levels of the image, such as pixels, edges, regions, or objects.
- Some basic descriptors for features are:

  - **Color**: Color is one of the most intuitive and widely used features in image analysis. Color can be represented by different color spaces, such as RGB, HSV, or CIELAB. Color features can be computed by using color histograms, color moments, color correlograms, or color descriptors.
  - **Texture**: Texture is the property of the image that describes the spatial arrangement and variation of pixel intensities. Texture can be characterized by using statistical, structural, or spectral methods. Texture features can be computed by using gray-level co-occurrence matrices, local binary patterns, Gabor filters, or wavelet transforms.
  - **Shape**: Shape is the property of the image that describes the contour or boundary of an object or a region. Shape can be represented by using parametric, polygonal, or free-form models. Shape features can be computed by using shape descriptors, such as Fourier descriptors, moment invariants, Hu moments, or Zernike moments.
  - **Size**: Size is the property of the image that describes the area or volume of an object or a region. Size can be measured by using simple metrics, such as pixel count, perimeter, or diameter. Size features can be normalized by using scale-invariant methods, such as scale-invariant feature transform (SIFT) or speeded up robust features (SURF).
  - **Orientation**: Orientation is the property of the image that describes the angle or direction of an object or a region. Orientation can be estimated by using gradient, edge, or line detectors. Orientation features can be computed by using orientation histograms, orientation tensors, or orientation descriptors.



### Topological and Texture Descriptors

- Topological and texture descriptors are methods to extract and represent the structural and statistical properties of an image or a region of interest.
- Topological descriptors capture the shape, connectivity, and complexity of the image components, such as edges, contours, regions, and holes. They are often based on graph theory, homology, or topology.
- Texture descriptors capture the spatial distribution, orientation, and frequency of the image intensity or color values. They are often based on filters, histograms, or transforms.
- Topological and texture descriptors can be used for various applications, such as image quality assessment, image segmentation, image classification, image retrieval, and image forensics.

Some examples of topological and texture descriptors are:

- Local Binary Pattern (LBP): A texture descriptor that assigns a binary code to each pixel based on the comparison of its intensity with its neighboring pixels. The histogram of the LBP codes can be used as a feature vector for texture analysis  .
- Topological Attribute Pattern (TAP): A topological descriptor that extends the LBP by computing a set of numerical attributes on the LBP codes, such as the number of transitions, the number of uniform patterns, and the local binary count. These attributes are invariant to rotation and can capture the local structure of the image.
- Topological Image Modification (TIM): A topological descriptor that modifies the image by applying a threshold and a dilation operation to extract the connected components and their boundaries. The number, size, and shape of the components and boundaries can be used as features for object detection and topological analysis.
- Multifractal Descriptors: A texture descriptor that measures the fractal dimension of the image at different scales and orientations. The fractal dimension reflects the self-similarity and complexity of the image texture. The histogram of the multifractal dimensions can be used as a feature vector for texture recognition .



### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are derived from the moments of an image and are invariant to certain geometric transformations, such as translation, scaling and rotation .
- Moments are scalar quantities that describe the distribution of pixel intensities in an image. They can be computed for the whole image or for a region of interest.
- Moments can be classified into different types, such as geometric moments, central moments, normalized central moments, Zernike moments, Legendre moments, etc.
- Moment invariants are useful for image analysis and pattern recognition, as they can capture the shape and appearance of an object regardless of its position, size and orientation .
- One of the most widely used sets of moment invariants was proposed by Hu in 1962, which consists of seven invariant values derived from the second and third order central moments .
- Hu's moment invariants are defined as follows :

$$
\begin{aligned}
I_1 &= \eta_{20} + \eta_{02} \\
I_2 &= (\eta_{20} - \eta_{02})^2 + 4\eta_{11}^2 \\
I_3 &= (\eta_{30} - 3\eta_{12})^2 + (3\eta_{21} - \eta_{03})^2 \\
I_4 &= (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2 \\
I_5 &= (\eta_{30} - 3\eta_{12})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] + (3\eta_{21} - \eta_{03})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] \\
I_6 &= (\eta_{20} - \eta_{02})[(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] + 4\eta_{11}(\eta_{30} + \eta_{12})(\eta_{21} + \eta_{03}) \\
I_7 &= (3\eta_{21} - \eta_{03})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] - (\eta_{30} - 3\eta_{12})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2]
\end{aligned}
$$

where $\eta_{pq}$ are the normalized central moments of order $(p+q)$, defined as:

$$
\eta_{pq} = \frac{\mu_{pq}}{\mu_{00}^{(1 + (p+q)/2)}}
$$

and $\mu_{pq}$ are the central moments of order $(p+q)$, defined as:

$$
\mu_{pq} = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} (x - \bar{x})^p (y - \bar{y})^q f(x,y)
$$

where $f(x,y)$ is the pixel intensity at $(x,y)$, $\bar{x}$ and $\bar{y}$ are the coordinates of the centroid of the image, and $M$ and $N$ are the dimensions of the image.

- Hu's moment invariants are not strictly invariant for discrete images, as they may change over image geometric transformations due to discretization errors . Therefore, some methods have been proposed to improve the accuracy and robustness of moment invariants, such as using higher order moments, applying normalization or weighting schemes, or combining different types of moments  .



### Principal Components as Feature Descriptors

- Principal components are linear combinations of the original features that capture the maximum variance in the data.
- Principal components can be used as feature descriptors to reduce the dimensionality of the data and improve the performance of feature matching algorithms.
- Principal components can be obtained by applying principal component analysis (PCA) to the data, which is an unsupervised machine learning technique that transforms the data into a new coordinate system .
- The steps of PCA are :
  - Standardize the data to have zero mean and unit variance.
  - Compute the covariance matrix of the standardized data.
  - Compute the eigenvalues and eigenvectors of the covariance matrix.
  - Sort the eigenvalues in descending order and select the top k eigenvalues and their corresponding eigenvectors, where k is the number of principal components to retain.
  - Project the standardized data onto the k eigenvectors to obtain the principal components.
- The principal components are ranked by their explained variance, which is the proportion of the total variance in the data that is explained by each component.
- Each original feature contributes with varying degree to each principal component, and the contribution can be measured by the magnitude of the corresponding element in the eigenvector.
- Principal components can be used as new features instead of the original features, which can reduce the noise, redundancy, and complexity of the data.
- Principal components can also be used to compare and match feature descriptors from different images, such as SIFT, by computing the Euclidean distance or cosine similarity between them.
- Principal components can enhance the robustness and accuracy of feature descriptors, especially when the images have variations in illumination, scale, rotation, or perspective .



### Whole-image Features Object

- A whole-image feature object is a representation of an image that captures its global characteristics, such as shape, color, texture, or contour.
- A whole-image feature object can be used to classify, compare, or index images based on their overall appearance or similarity.
- A whole-image feature object can be obtained by applying various feature extraction methods to the image, such as:
  - Histograms: A histogram is a graphical representation of the distribution of pixel values or colors in an image. A histogram can capture the color or intensity information of an image as a whole.
  - Moments: Moments are numerical values that describe the shape or geometry of an image region. Moments can capture the orientation, eccentricity, or symmetry of an image as a whole.
  - Fourier transform: Fourier transform is a mathematical operation that decomposes an image into its frequency components. Fourier transform can capture the periodicity, directionality, or texture of an image as a whole.
  - Wavelet transform: Wavelet transform is a mathematical operation that decomposes an image into its spatial and frequency components. Wavelet transform can capture the multi-scale, multi-resolution, or multi-orientation features of an image as a whole.
- A whole-image feature object can be represented as a feature vector, which is a one-dimensional array of numerical values that encode the information of the feature object. A feature vector can be used as an input to a machine learning model or a similarity measure for image retrieval or comparison.



### Scale-Invariant Feature Transform (SIFT) for Image Feature Extraction

- Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm to detect and describe local features in images.
- Local features are distinctive points or regions in an image that can be used for matching, recognition, or other tasks.
- SIFT features are invariant to scale and orientation of images and robust to illumination fluctuations, noise, partial occlusion, and minor viewpoint changes in the images.
- SIFT algorithm consists of four main steps:
  - Scale-space extrema detection: finding potential interest points across different scales and locations in the image using a Difference of Gaussians (DoG) function.
  - Keypoint localization: refining the location and scale of each candidate point and discarding low-contrast or edge points.
  - Orientation assignment: assigning one or more orientations to each keypoint based on the local image gradient directions.
  - Keypoint descriptor: computing a 128-dimensional vector for each keypoint that captures the local image gradient magnitudes and orientations around the keypoint.
- SIFT features can be used for various applications, such as object recognition, image stitching, 3D modeling, gesture recognition, video tracking, individual identification, etc.



## Unit 5 - Image Pattern Classification

- Image pattern classification is the task of categorizing images into one or multiple predefined classes based on their content, such as objects, scenes, textures, etc.
- Image pattern classification is a subfield of computer vision and machine learning that deals with the recognition and analysis of visual patterns in images.
- Image pattern classification can be performed using different methods, such as supervised, unsupervised, or semi-supervised learning.
- Supervised learning is the process of training a classifier with labeled images, where each image has a known class. The classifier learns to map the input images to the output classes and can then predict the class of new images.
- Unsupervised learning is the process of grouping images into clusters based on their similarities, without using any labels. The clusters represent the latent patterns or categories in the images. The number of clusters can be predefined or determined automatically.
- Semi-supervised learning is the process of combining labeled and unlabeled images to train a classifier. The unlabeled images can provide additional information or regularization to improve the classifier's performance.
- Image pattern classification can be achieved using different techniques, such as classic or deep learning methods.
- Classic methods are based on extracting handcrafted features from images, such as color, shape, texture, etc., and using them as inputs for a classifier, such as k-nearest neighbors, support vector machines, decision trees, etc.
- Deep learning methods are based on using neural networks, such as convolutional neural networks (CNNs), to learn features and classifiers from images in an end-to-end manner. CNNs consist of multiple layers of filters that convolve with the input images and produce feature maps that capture the patterns and semantics in the images.
- Image pattern classification can be applied to various domains and applications, such as face recognition, object detection, scene understanding, medical image analysis, etc.
- Image pattern classification can be evaluated using different metrics, such as accuracy, precision, recall, F1-score, etc., depending on the task and the dataset.
- Image pattern classification can be improved by using different strategies, such as data augmentation, regularization, transfer learning, ensemble learning, etc.



### Background for the notes of the Unit 5 - Image Pattern Classification in the subject of IMAGE ANALYTICS

- Image pattern classification is the process of assigning a label to an image based on its content, such as objects, scenes, faces, etc.
- Image pattern classification is a fundamental task in image analytics, which aims to extract useful information and insights from large collections of images.
- Image pattern classification can be applied to various domains, such as biometrics, security, medical imaging, remote sensing, social media, etc.
- Image pattern classification can be formulated as a supervised learning problem, where a classifier is trained on a set of labeled images and then used to predict the labels of new images.
- Image pattern classification can also be formulated as an unsupervised learning problem, where a classifier is trained on a set of unlabeled images and then used to cluster or segment the images based on their similarities or differences.
- Image pattern classification can be performed at different levels of abstraction, such as pixel-level, region-level, object-level, or scene-level.
- Image pattern classification can be challenging due to the high dimensionality, variability, and complexity of image data, as well as the ambiguity and subjectivity of image labels.
- Image pattern classification can be improved by using various techniques, such as feature extraction, dimensionality reduction, feature selection, feature fusion, classifier design, classifier fusion, etc.
- Image pattern classification can be evaluated by using various metrics, such as accuracy, precision, recall, F1-score, ROC curve, AUC, confusion matrix, etc.



### Patterns and Pattern Classes

- A **pattern** is an arrangement of descriptors, which are numerical or symbolic values that characterize an object or an event.
- A **descriptor** is also called a **feature** or an **attribute** .
- A **pattern class** is a family of patterns that share some common properties.
- The goal of **pattern classification** is to assign a class label to a pattern based on a numerical representation of the pattern's properties that is most suitable for the problem at hand.
- Pattern classification techniques can be divided into two categories: **supervised** and **unsupervised**.
- **Supervised** pattern classification involves learning from a set of labeled training patterns and then applying the learned model to classify new patterns.
- **Unsupervised** pattern classification involves finding natural groups or clusters of patterns without any prior knowledge of their labels.
- Pattern classification techniques can be further classified into three types: **statistical**, **structural**, and **syntactic**.
- **Statistical** pattern classification relies on the probabilistic description of the patterns and their classes, and uses decision rules based on Bayes' theorem, likelihood ratio, or discriminant functions.
- **Structural** pattern classification uses the spatial or temporal relationships among the descriptors to form complex structures, such as graphs, trees, or strings, and uses graph matching, tree matching, or string matching algorithms to compare and classify patterns.
- **Syntactic** pattern classification combines the structural and statistical approaches, and uses grammars and automata to generate and recognize patterns based on their syntactic rules.
- The process of pattern classification usually involves four steps: **image acquisition**, **image preprocessing**, **image feature extraction**, and **classification**.
- **Image acquisition** is the process of capturing an image using a sensor, such as a camera, a scanner, or a microscope.
- **Image preprocessing** is the process of enhancing, transforming, or reducing the noise in the image to improve its quality and suitability for further analysis.
- **Image feature extraction** is the process of extracting relevant and discriminative descriptors from the image, such as color, texture, shape, or local patterns.
- **Classification** is the process of assigning a class label to the image or a region of interest in the image based on the extracted features and a classification model.



### Pattern Classification by Prototype Matching

- Pattern classification is the task of assigning a label to an input pattern based on some criteria or rules.
- Prototype matching is a method of pattern classification that compares the input pattern to a set of stored prototypes, which are representative or average examples of each class.
- Prototype matching can be seen as a generalization of template matching, which requires an exact match between the input pattern and a stored template.
- Prototype matching allows for some variation and noise in the input pattern, as long as it is similar enough to one of the prototypes.
- Prototype matching can be implemented using different measures of similarity or distance, such as Euclidean distance, cosine similarity, or Mahalanobis distance.
- Prototype matching can also be combined with other techniques, such as feature extraction, dimensionality reduction, or clustering, to improve the performance and efficiency of the classification.
- Prototype matching can be applied to various domains, such as image recognition, face recognition, speech recognition, handwriting recognition, or medical diagnosis.



### Minimum-Distance Classifier

- A minimum-distance classifier is a type of supervised learning algorithm that assigns a new sample to the class that is closest to it in a feature space.
- The distance between a sample and a class can be measured by various metrics, such as Euclidean distance, Mahalanobis distance, or cosine similarity.
- The minimum-distance classifier can be seen as a special case of the k-nearest neighbor (k-NN) classifier, where k = 1.
- The minimum-distance classifier is simple and fast, but it may not be very accurate or robust to noise and outliers.
- The minimum-distance classifier can be applied to image pattern classification tasks, such as face recognition, digit recognition, or object recognition.
- To use the minimum-distance classifier for image pattern classification, the following steps are usually involved:
  - Preprocess the images to reduce noise, enhance contrast, and normalize size and orientation.
  - Extract features from the images, such as color, texture, shape, or local descriptors.
  - Represent the images as feature vectors in a high-dimensional feature space.
  - Divide the feature vectors into training and testing sets.
  - Train the minimum-distance classifier by computing the mean or centroid of each class in the feature space.
  - Test the minimum-distance classifier by computing the distance between each test sample and each class centroid, and assigning the test sample to the class with the minimum distance.
  - Evaluate the performance of the minimum-distance classifier by calculating the accuracy, precision, recall, or F1-score.



### Using Correlation for 2-D Prototype Matching

- Correlation is a measure of similarity between two signals or images.
- Correlation can be used for pattern matching, which is the process of finding a specific pattern or template in a larger image or signal.
- Correlation can be performed in the spatial domain or the frequency domain, depending on the application and the computational efficiency.
- 2-D correlation involves sliding a smaller template image over a larger input image and computing the correlation coefficient at each position.
- The correlation coefficient is a value between -1 and 1 that indicates how well the template matches the input image at that position.
- A high correlation coefficient means a good match, while a low correlation coefficient means a poor match.
- The correlation coefficient can be normalized to account for different scales and intensities of the images.
- Normalized cross-correlation is a common method for 2-D prototype matching, which uses the following formula:

![formula](https://wikimedia.org/api/rest_v1/media/math/render/svg/6a8f6f0f6f3a6a9f7f9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9c9a0a7a9



### Matching SIFT Features

- SIFT stands for Scale-Invariant Feature Transform, a computer vision algorithm to detect, describe, and match local features in images.
- SIFT features are invariant to rotation, scale, and brightness changes, and are stable to some extent to perspective and affine transformations .
- SIFT features have a large amount of information and are suitable for fast and accurate matching in massive databases.
- SIFT feature matching can be used for various applications, such as image stitching, object recognition, scene detection, gesture recognition, video tracking, etc .
- SIFT feature matching can be done in the following steps :
  - Extract SIFT features from the input images using the SIFT detector and descriptor.
  - Create a feature matcher object, such as a brute-force matcher or a FLANN-based matcher, to compare the features of the images.
  - Use the matcher object to find the best matches or the k nearest neighbors for each feature, based on some distance metric, such as Euclidean distance or Hamming distance.
  - Apply some filtering criteria, such as the ratio test or the symmetry test, to remove the false matches and keep only the good matches.
  - Optionally, use a homography matrix or a fundamental matrix to estimate the geometric transformation between the images and refine the matches.



### Matching Structural Prototypes

- Matching structural prototypes is a technique for image pattern classification that involves comparing an unknown pattern with a set of known prototypes that represent different classes.
- A prototype is a sub-image or a graph that captures the essential features of a class .
- Matching structural prototypes can be done by using template matching or graph matching methods  .
- Template matching is a technique that finds the best match between a template image and a target image by using a similarity measure, such as cross-correlation or mean squared error .
- Graph matching is a technique that finds the best correspondence between the nodes and edges of two graphs that represent the patterns, by using a cost function, such as edit distance or maximum common subgraph .
- Matching structural prototypes can be used for various applications, such as object detection, edge detection, quality control, navigation, and medical imaging  .
- Matching structural prototypes can also be improved by using adversarial learning, which generates hard examples that challenge the classifier and force it to learn more discriminative features.
- Matching structural prototypes can be combined with syntactic pattern recognition, which uses a description of the pattern structure to recognize complex patterns that cannot be classified by simple features.



### Optimum (Bayes) Statistical Classifiers

- Optimum (Bayes) statistical classifiers are classifiers that use the Bayes' theorem to make predictions based on the posterior probabilities of the classes given the features of a new example .
- The Bayes' theorem states that the posterior probability of a class C given a feature vector x is proportional to the product of the prior probability of the class P(C) and the likelihood of the feature vector given the class P(x|C):
  - P(C|x) ∝ P(C)P(x|C)
- The optimum (Bayes) classifier chooses the class that has the highest posterior probability for a given feature vector, i.e., the class that maximizes P(C|x) . This is also known as the maximum a posteriori (MAP) estimation or the Bayes optimal decision rule.
- The optimum (Bayes) classifier can be seen as a benchmark for the performance of other classifiers, since it has the lowest possible error rate among all classifiers. The error rate of the optimum (Bayes) classifier is called the Bayes error rate, and it is the minimum achievable error rate given the distribution of the data.
- The optimum (Bayes) classifier can be applied to image pattern classification problems, where the goal is to assign a label to an image based on its features, such as pixels, edges, shapes, colors, etc. The features can be extracted from the image using various methods, such as filters, transforms, descriptors, etc. The prior probabilities of the classes can be estimated from the frequency of the labels in the training data, and the likelihoods of the features given the classes can be modeled using various probability distributions, such as Gaussian, multinomial, etc. The optimum (Bayes) classifier can then use the Bayes' theorem to compute the posterior probabilities of the classes given the features of a new image, and assign the label with the highest posterior probability to the image .



### Neural Networks and Deep Learning for Image Pattern Classification

- Image pattern classification is the task of assigning a label to an image based on its content, such as objects, scenes, faces, etc.
- Neural networks are computational models that consist of multiple layers of interconnected units called neurons, which can learn from data and perform complex tasks.
- Deep learning is a branch of machine learning that uses neural networks with many layers, often hundreds or thousands, to learn high-level features and representations from data.
- Convolutional neural networks (CNNs) are a type of deep neural network that are specially designed for image processing and recognition. They use convolutional layers that apply filters to the input image and produce feature maps that capture local patterns and structures.
- CNNs can be trained using large datasets of labeled images, such as ImageNet, to learn generalizable features that can be used for various image classification tasks. They can also be fine-tuned or adapted to specific domains or tasks using smaller datasets.
- CNNs have achieved state-of-the-art results in many image classification challenges, such as the ImageNet Large Scale Visual Recognition Challenge (ILSVRC), surpassing human performance in some cases.
- Some of the common architectures of CNNs for image classification are:

  - LeNet: The first successful CNN, proposed by Yann LeCun et al. in 1998, for handwritten digit recognition. It consists of two convolutional layers, two pooling layers, and two fully connected layers.
  - AlexNet: The CNN that won the ILSVRC 2012 challenge, proposed by Alex Krizhevsky et al. in 2012, for natural image recognition. It consists of five convolutional layers, three pooling layers, two fully connected layers, and a softmax layer. It also uses dropout, relu activation, and data augmentation techniques to improve performance and prevent overfitting.
  - VGG: A family of CNNs, proposed by Karen Simonyan and Andrew Zisserman in 2014, for natural image recognition. They consist of multiple convolutional layers with small filters (3x3), followed by pooling layers, and three fully connected layers. They vary in the number of layers, from 11 to 19, and are named as VGG11, VGG13, VGG16, and VGG19.
  - ResNet: A family of CNNs, proposed by Kaiming He et al. in 2015, for natural image recognition. They consist of multiple residual blocks, which are composed of two or more convolutional layers and a shortcut connection that bypasses the layers and adds the input to the output. They use this technique to overcome the problem of vanishing gradients and enable the training of very deep networks, up to 152 layers.
  - Inception: A family of CNNs, proposed by Christian Szegedy et al. in 2014, for natural image recognition. They consist of multiple inception modules, which are composed of parallel branches of convolutional, pooling, and fully connected layers with different filter sizes and types. They use this technique to increase the width and depth of the network while reducing the number of parameters and computational cost.
  - Transformer: A type of neural network, proposed by Ashish Vaswani et al. in 2017, for natural language processing. It consists of multiple encoder and decoder blocks, which are composed of self-attention and feed-forward layers. It uses this technique to capture long-range dependencies and context information from sequential data. Recently, it has been adapted and applied to image classification tasks, such as Vision Transformer (ViT) by Alexey Dosovitskiy et al. in 2020, and has shown promising results.



### Background for the notes of the Unit 5 - Image Pattern Classification in the subject of IMAGE ANALYTICS

- Image pattern classification is the task of assigning a label to an image based on its content, such as objects, scenes, faces, etc.
- Image pattern classification is a fundamental problem in computer vision and has many applications, such as face recognition, medical diagnosis, security, surveillance, etc.
- Image pattern classification can be formulated as a supervised learning problem, where a classifier is trained on a set of labeled images and then tested on new images.
- Image pattern classification can be divided into two subtasks: feature extraction and classification.
  - Feature extraction is the process of transforming the raw pixel values of an image into a more compact and informative representation, such as edges, corners, blobs, histograms, etc.
  - Classification is the process of assigning a label to an image based on its feature representation, using a decision rule, such as nearest neighbor, linear discriminant, support vector machine, neural network, etc.
- Image pattern classification can be challenging due to the high dimensionality, variability, and complexity of image data, such as noise, occlusion, illumination, pose, scale, rotation, etc.
- Image pattern classification can be improved by using various techniques, such as dimensionality reduction, feature selection, feature fusion, feature learning, data augmentation, ensemble methods, etc.



### The Perceptron for the notes of the Unit 5 - Image Pattern Classification in the subject of IMAGE ANALYTICS

- A perceptron is a type of neural network model that can perform binary classification tasks on visual inputs .
- A perceptron consists of a single node or neuron that takes a row of data as input and predicts a class label.
- The input data can be numerical or visual, such as images or patterns .
- The perceptron uses a linear function to compute a weighted sum of the input data and a bias term, and then applies a threshold function to produce the output label .
- The output label can be either 0 or 1, representing the two classes .
- The perceptron can be trained using the perceptron learning rule, which updates the weights and bias based on the prediction errors .
- The perceptron learning rule is guaranteed to converge to a solution if the data is linearly separable, meaning that there exists a line that can separate the two classes.
- The perceptron can be extended to perform multi-category classification by using multiple output neurons, each representing a different class.
- The perceptron can also be combined with other perceptrons to form a multi-layer perceptron, which can learn non-linear functions and perform more complex tasks .



### Multilayer Feedforward Neural Networks

- A multilayer feedforward neural network is an interconnection of perceptrons in which data and calculations flow in a single direction, from the input data to the outputs.
- The number of layers in a neural network is the number of layers of perceptrons. The simplest neural network is one with a single input layer and an output layer of perceptrons.
- A multilayer feedforward neural network for classifying patterns into one of only two categories is referred to as a binary classification network. It has a single output: the estimated probability that the input pattern belongs to one of the two categories.
- A multilayer feedforward neural network can also be used for multiclass classification, where the output layer has more than one neuron, each representing a different class. The output values can be interpreted as the probabilities of the input pattern belonging to each class.
- A multilayer feedforward neural network can learn complex nonlinear functions by adjusting the weights and biases of the neurons using a learning algorithm, such as gradient descent or backpropagation.
- The hidden layers of a multilayer feedforward neural network can extract features from the input data and transform them into a higher-level representation that is more suitable for classification.
- A multilayer feedforward neural network can be applied to various domains, such as image recognition, natural language processing, speech recognition, etc.



### Deep Convolutional Neural Networks for Image Pattern Classification

- Deep convolutional neural networks (DCNNs) are a type of artificial neural networks that can learn from image samples and extract features for image pattern classification .
- DCNNs consist of multiple layers of processing units, each of which performs a convolution operation on the input, followed by a nonlinear activation function and an optional pooling operation .
- The convolution operation applies a set of filters to the input, which can capture local patterns of pixels, such as edges, corners, textures, etc. The activation function introduces nonlinearity to the network, which enables it to learn complex functions. The pooling operation reduces the spatial dimension of the input, which makes the network more robust to translation and scale variations .
- The output of the last convolutional layer is typically fed to one or more fully connected layers, which perform the final classification task. The fully connected layers learn global features from the input, such as the shape, pose, identity, etc. of the object .
- DCNNs can be trained using backpropagation and stochastic gradient descent, which update the filter weights and biases based on the error between the network output and the ground truth labels .
- DCNNs have achieved state-of-the-art results on various image pattern classification tasks, such as object recognition, face recognition, scene classification, etc. Some of the well-known DCNN architectures are AlexNet, VGGNet, ResNet, Inception, etc.
- DCNNs can also be visualized to understand how they learn and what they learn. Some of the visualization techniques are based on computing the gradient of the class score with respect to the input image, which shows the regions that contribute most to the classification decision. Another technique is to generate synthetic images that maximize the activation of a certain filter or neuron, which shows the preferred patterns of the network.

