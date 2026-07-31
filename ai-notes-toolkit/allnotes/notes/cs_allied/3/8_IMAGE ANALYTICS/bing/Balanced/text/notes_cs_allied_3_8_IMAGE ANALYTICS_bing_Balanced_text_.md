

# Image Analytics

Image analytics is the process of extracting meaningful information from images, mainly from digital images, by using digital image processing techniques. Image analytics can be used for various purposes, such as:

- Reading bar codes, QR codes, or text from images
- Identifying objects, faces, logos, or scenes in images
- Measuring dimensions, distances, or angles in images
- Enhancing, restoring, or segmenting images
- Detecting anomalies, defects, or changes in images
- Classifying, clustering, or indexing images
- Generating captions, descriptions, or summaries for images
- Creating new images from existing images

Image analytics can be applied to various domains, such as:

- Security and surveillance
- Medical imaging and diagnosis
- Remote sensing and geospatial analysis
- Industrial inspection and quality control
- Biometrics and face recognition
- Marketing and advertising
- Education and entertainment
- Art and culture
- Social media and web analysis

Image analytics can be performed using various methods, such as:

- Pixel-based methods: operate on individual pixels or groups of pixels in an image, such as thresholding, filtering, or edge detection
- Feature-based methods: extract salient features from an image, such as corners, keypoints, or contours, and use them for matching, recognition, or classification
- Region-based methods: segment an image into homogeneous regions, such as superpixels, blobs, or regions of interest, and use them for labeling, grouping, or analysis
- Model-based methods: use predefined models or templates to fit or detect objects or shapes in an image, such as Hough transform, active contours, or deformable models
- Learning-based methods: use machine learning or deep learning algorithms to learn from data and perform tasks such as classification, detection, segmentation, or generation, such as support vector machines, neural networks, or generative adversarial networks

Image analytics can be challenging due to various factors, such as:

- Image quality: noise, blur, distortion, or compression can affect the image quality and make it difficult to extract information
- Image variability: variations in illumination, pose, scale, orientation, or occlusion can affect the appearance and representation of objects or scenes in an image
- Image complexity: images can contain multiple objects, backgrounds, or foregrounds, which can make it hard to separate or identify them
- Image ambiguity: images can have multiple interpretations, meanings, or contexts, which can make it hard to analyze them
- Image diversity: images can come from different sources, formats, or modalities, which can make it hard to compare or integrate them

Image analytics can be improved by using various techniques, such as:

- Image preprocessing: improve the image quality or reduce the image variability by applying operations such as contrast enhancement, noise reduction, or geometric transformation
- Image augmentation: increase the image diversity or reduce the image ambiguity by applying operations such as cropping, flipping, rotating, or adding noise
- Image fusion: combine information from multiple images or modalities to enhance the image analysis, such as color, infrared, or depth images
- Image annotation: provide additional information or labels for images to facilitate the image analysis, such as bounding boxes, masks, or captions
- Image evaluation: measure the performance or accuracy of image analysis methods or algorithms by using metrics such as precision, recall, or F1-score



## Unit 1 - Fundamentals

- This unit covers the basic concepts and principles of computer science, such as data representation, algorithms, programming languages, and abstraction.
- Data representation is the process of encoding information in a form that can be stored and manipulated by a computer. There are different ways of representing data, such as binary, hexadecimal, ASCII, Unicode, etc.
- Algorithms are step-by-step instructions that describe how to solve a problem or perform a task. Algorithms can be expressed in different ways, such as pseudocode, flowcharts, or programming languages.
- Programming languages are formal languages that specify the syntax and semantics of computer programs. There are different types of programming languages, such as imperative, declarative, functional, object-oriented, etc.
- Abstraction is the process of hiding unnecessary details and focusing on the essential features of a problem or a solution. Abstraction can be applied at different levels, such as data abstraction, procedural abstraction, or object abstraction.



### Introduction for the notes of the Unit 1 - Fundamentals in the subject of IMAGE ANALYTICS

- Image analytics is the process of applying advanced techniques such as computer vision, machine learning, and deep learning to extract meaningful information from images and videos.
- Image analytics can be used for various applications such as face recognition, object detection, medical imaging, security, entertainment, and more.
- Image analytics involves the following steps:
  - Image acquisition: capturing or obtaining images from different sources such as cameras, scanners, satellites, etc.
  - Image preprocessing: enhancing or modifying images to improve their quality or suitability for further analysis, such as noise reduction, contrast enhancement, resizing, cropping, etc.
  - Image segmentation: dividing an image into regions or segments that have similar characteristics or belong to the same object or class, such as edge detection, thresholding, clustering, etc.
  - Image feature extraction: extracting relevant or distinctive features from images that can be used for representation, description, or classification, such as color, texture, shape, keypoints, descriptors, etc.
  - Image analysis: applying various methods or algorithms to analyze the features or segments of images and derive useful information or insights, such as classification, recognition, detection, tracking, matching, retrieval, etc.
  - Image visualization: displaying or presenting the results or outputs of image analysis in a clear and understandable way, such as graphs, charts, tables, maps, etc.
- Image analytics requires a solid foundation of mathematics, statistics, and computer science, as well as domain knowledge and problem-solving skills.



### Fundamental steps in image processing systems

- Image processing systems are used to manipulate and analyze digital images, such as photographs, satellite images, medical images, etc.
- Image processing systems mainly involve the following three steps :

  - **Image acquisition**: This involves capturing an image using a digital camera or scanner, or importing an existing image into a computer. The image is usually converted into a matrix of pixels, each with a numerical value representing its color or intensity.
  - **Image processing**: This involves applying various operations and algorithms to the image, such as filtering, segmentation, edge detection, feature extraction, compression, enhancement, etc. The purpose of image processing is to improve the visual quality of the image, extract useful information from the image, or transform the image into a different representation or domain.
  - **Image output**: This involves displaying the processed image on a screen, printing the image on a paper, storing the image in a file, or transmitting the image to another device or system. The output can also be a report or a decision based on the analysis of the image.

- Figure 1 shows a schematic diagram of the fundamental steps of image processing systems.

Figure 1: Fundamental steps of image processing systems

Figure 1: Fundamental steps of image processing systems



### Image Acquisition

Image acquisition is the process of capturing an image from a physical scene and converting it into a digital form that can be processed by a computer. Image acquisition is the first and essential step in digital image processing. 

Some of the fundamental concepts and steps involved in image acquisition are:

- **Image source**: The image source is the object or scene that emits or reflects some form of energy, such as light, sound, or radiation. The image source can be natural or artificial, static or dynamic, two-dimensional or three-dimensional.
- **Image sensor**: The image sensor is the device that detects and measures the energy from the image source and converts it into an electrical signal. The image sensor can be analog or digital, and can have different types of elements, such as photodiodes, charge-coupled devices (CCDs), or complementary metal-oxide-semiconductor (CMOS) transistors.
- **Image digitization**: The image digitization is the process of converting the analog signal from the image sensor into a discrete and quantized digital signal that can be stored and manipulated by a computer. The image digitization involves two steps: sampling and quantization. Sampling is the process of dividing the continuous image into a finite number of pixels or voxels, each representing a small region of the image. Quantization is the process of assigning a discrete value or intensity to each pixel or voxel, based on the amplitude of the analog signal.
- **Image enhancement**: Image enhancement is the process of manipulating the digital image to improve its appearance or suitability for a specific application. Image enhancement can involve operations such as contrast adjustment, noise reduction, sharpening, filtering, or color correction.
- **Image acquisition system**: The image acquisition system is the combination of hardware and software components that perform the image acquisition process. The image acquisition system can include components such as lenses, filters, cameras, scanners, frame grabbers, digitizers, computers, and software. The image acquisition system should be designed and configured according to the requirements and constraints of the image source, the image sensor, the image digitization, and the image enhancement.



### Sampling and Quantization

- Sampling and quantization are two basic operations for converting a continuous image into a digital image.
- Sampling is the process of digitizing the spatial coordinates (x and y) of the image. It involves dividing the image into a grid of pixels and assigning a value to each pixel based on the intensity of the image at that location.
- Quantization is the process of digitizing the amplitude values (z) of the image. It involves mapping the continuous range of pixel values into a finite set of discrete levels, usually represented by binary numbers.
- The sampling rate determines the spatial resolution of the digitized image, while the quantization level determines the number of gray levels or colors in the digitized image.
- The sampling and quantization processes introduce errors in the digitized image, which can affect the quality and accuracy of the image processing tasks.
- The sampling and quantization errors can be reduced by increasing the sampling rate and the quantization level, but this also increases the storage and computational requirements of the digitized image. Therefore, a trade-off between quality and efficiency has to be made.



### Pixel Relationships

- A pixel is a discrete unit of information that represents the intensity or color of an image at a specific location.
- Pixels are arranged in a two-dimensional grid, where each pixel has a row and column index.
- The size of the pixel grid is determined by the resolution of the image, which is the number of pixels per unit length (e.g., pixels per inch or ppi).
- The value of a pixel can range from 0 to 255 for an 8-bit grayscale image, or from 0 to 255 for each of the red, green, and blue channels for a 24-bit color image.
- The value of a pixel can also be normalized to the range [0, 1] by dividing by 255.
- The value of a pixel can be interpreted as a measure of brightness, contrast, or color, depending on the context and the type of image.
- The value of a pixel can also be affected by noise, which is any unwanted variation or distortion in the image data.
- Pixels are not isolated entities, but are related to their neighboring pixels in various ways.
- The relationship between pixels can be described by the following concepts:

  - **Neighborhood**: A neighborhood of a pixel is a set of pixels that are adjacent or close to the pixel in the pixel grid. The size and shape of the neighborhood can vary depending on the application. For example, a 3x3 square neighborhood consists of the pixel and its eight immediate neighbors, while a 5x5 circular neighborhood consists of the pixel and its 24 neighbors that are within a radius of 2 pixels from the pixel.
  - **Connectivity**: Connectivity of a pixel is the degree to which the pixel is connected to other pixels in the image. Connectivity can be defined based on the neighborhood of the pixel and the similarity of the pixel values. For example, a pixel is 4-connected to another pixel if they share an edge in the pixel grid and have the same value, while a pixel is 8-connected to another pixel if they share an edge or a corner in the pixel grid and have the same value.
  - **Region**: A region of an image is a subset of pixels that have some common property or characteristic. A region can be defined based on the connectivity of the pixels, the value of the pixels, or some other criterion. For example, a region can be a connected component of pixels that have the same value, a segment of pixels that have similar values, or an object of interest in the image.
  - **Boundary**: A boundary of a region is a set of pixels that separate the region from the rest of the image. A boundary can be defined based on the neighborhood of the pixels, the value of the pixels, or some other criterion. For example, a boundary can be a contour of pixels that have a different value from their neighbors, an edge of pixels that have a high gradient magnitude, or a border of pixels that mark the end of the region.



### Mathematical Tools Used in Digital Image Processing

- A digital image is a collection of numerical values represented in the form of a matrix. Each value corresponds to the intensity or color of a pixel in the image. 
- Digital image processing (DIP) is the manipulation of digital images using various mathematical and computational techniques to enhance, analyze, or transform them. 
- Some of the mathematical tools that are used in DIP are:

  - **Matrix operations**: Matrix operations such as addition, subtraction, multiplication, inversion, etc., are used to perform various image processing tasks, such as filtering, scaling, rotation, transformation, etc. For example, a linear filter can be applied to an image by multiplying the image matrix with a filter matrix. 
  - **Set operations**: Set operations such as union, intersection, complement, etc., are used to perform logical operations on images, such as masking, thresholding, segmentation, etc. For example, a mask can be applied to an image by taking the intersection of the image set and the mask set. 
  - **Distance functions**: Distance functions such as Euclidean, Manhattan, Chebyshev, etc., are used to measure the similarity or dissimilarity between images, pixels, regions, etc. For example, the Euclidean distance can be used to measure the difference between two images by taking the square root of the sum of the squared differences of the corresponding pixel values. 
  - **Transforms**: Transforms such as Fourier, Laplace, Wavelet, etc., are used to convert an image from one domain to another, such as from spatial domain to frequency domain, or vice versa. Transforms can help to analyze the image in different ways, such as to extract features, to compress, to denoise, to enhance, etc. For example, the Fourier transform can be used to decompose an image into its frequency components, which can be used to remove noise or to enhance edges. 
  - **Statistical methods**: Statistical methods such as mean, median, mode, standard deviation, histogram, etc., are used to describe the properties of an image, such as its brightness, contrast, color, texture, etc. Statistical methods can also be used to perform image enhancement, segmentation, classification, etc. For example, the histogram of an image can be used to adjust its contrast by stretching or equalizing it. 
  - **Optimization methods**: Optimization methods such as gradient descent, Newton's method, genetic algorithm, etc., are used to find the optimal solution for a given problem or objective function in image processing, such as to minimize the error, to maximize the similarity, to find the best fit, etc. For example, the gradient descent method can be used to find the optimal parameters for a linear filter by iteratively updating them based on the gradient of the error function. 
  - **Machine learning methods**: Machine learning methods such as neural networks, support vector machines, decision trees, etc., are used to learn from data and to perform tasks such as image recognition, classification, segmentation, etc. Machine learning methods can also be used to generate new images or to modify existing images. For example, a neural network can be trained to recognize faces in images by learning from a large dataset of labeled images.



### Some Basic Intensity Transformation Functions

- Intensity transformation is a basic digital image processing technique, where the pixel intensity levels of an image are transformed to new values using a mathematical transformation function, so as to get a new output image.
- Intensity transformations are also called point processing techniques, because they depend only on the intensity at a point.
- Intensity transformations are performed in the spatial domain, i.e. they are performed directly on the pixels of the image, as opposed to being performed on the Fourier transform of the image.
- Some common intensity transformation functions are:

  - **Linear transformation**: This is a simple transformation that maps the input intensity range to the output intensity range using a linear function. For example, the function `g(x) = a * f(x) + b`, where `a` and `b` are constants, is a linear transformation. Linear transformations can be used for brightness and contrast adjustment.
  - **Logarithmic transformation**: This is a transformation that maps the input intensity range to the output intensity range using a logarithmic function. For example, the function `g(x) = c * log(1 + f(x))`, where `c` is a constant, is a logarithmic transformation. Logarithmic transformations can be used for enhancing the details of dark regions in an image.
  - **Power-law transformation**: This is a transformation that maps the input intensity range to the output intensity range using a power-law function. For example, the function `g(x) = c * f(x)^r`, where `c` and `r` are constants, is a power-law transformation. Power-law transformations can be used for enhancing the details of bright or dark regions in an image, depending on the value of `r`.
  - **Histogram equalization**: This is a transformation that maps the input intensity range to the output intensity range such that the histogram of the output image is approximately uniform. Histogram equalization can be used for improving the contrast of an image by spreading the pixels over as many gray levels as possible.
  - **Thresholding**: This is a transformation that maps the input intensity range to a binary output range, such that the pixels below a certain threshold are assigned to one value, and the pixels above the threshold are assigned to another value. Thresholding can be used for image segmentation, i.e. separating the foreground from the background.

- The following diagram shows some examples of intensity transformation functions and their effects on an image:

Intensity transformation functions and their effects on an image



### Image Negatives

- An image negative is a type of image that has its colors inverted, or reversed, from the original image.
- An image negative can be created by subtracting each pixel value from the maximum possible value in the image format. For example, if the image is in 8-bit grayscale, the maximum value is 255, so the negative of a pixel with value x is 255 - x.
- An image negative can be used for various purposes, such as enhancing contrast, creating artistic effects, or revealing hidden details in dark or bright regions of the image.
- An image negative can be converted back to the original image by applying the same operation again, since (255 - x) - 255 = -x and -(-x) = x.



### Log Transformations

- Log transformation of an image means replacing all pixel values, present in the image, with its logarithmic values .
- Log transformation is used for image enhancement as it expands dark pixels of the image as compared to higher pixel values .
- Log transformation is a data transformation method in which it replaces each variable x with a log(x). In other words, the log transformation reduces or removes the skewness of our original data.
- The important caveat here is that the original data has to follow or approximately follow a log-normal distribution.
- The log transformation can be expressed as:

```
s = c log(1 + r)
```

where s and r are the pixel values of the output and the input image, and c is a scaling constant.

- The log transformation can be implemented using Python and OpenCV as follows:

```
# Import the libraries
import cv2
import numpy as np

# Read the image
img = cv2.imread('image.jpg')

# Apply log transformation
c = 255 / np.log(1 + np.max(img))
log_image = c * (np.log(img + 1))

# Convert the image to uint8
log_image = np.array(log_image, dtype = np.uint8)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow('Log Transformation', log_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

- The log transformation can also be applied to data collected by Azure Monitor, which can filter or modify incoming data before it's sent to a Log Analytics workspace.
- Workspace transformations provide support for ingestion-time transformations for workflows that don't yet use the Azure Monitor data ingestion pipeline.
- The log transformation is often used in statistics to reduce skewness of a measurement variable. If, after transformation, the distribution is symmetric, then the Welch t-test might be used to compare groups. If, also, the distribution becomes close to normal, then a reference interval might be determined.



### Power-Law Transformations

- Power-law transformations are a type of image enhancement technique that can be used to adjust the contrast and brightness of an image.
- The general form of power-law transformation function is  :

$$
s = c*r^\gamma
$$

where, $s$ and $r$ are the output and input pixel values, respectively and $c$ and $\gamma$ are the positive constants.

- The value of $\gamma$ determines the type and degree of enhancement. For various values of $\gamma$, different levels of enhancement can be obtained.
- If $\gamma < 1$, the transformation is called gamma correction and it increases the brightness of the image by mapping dark pixels to lighter ones.
- If $\gamma > 1$, the transformation is called gamma encoding and it decreases the brightness of the image by mapping light pixels to darker ones.
- If $\gamma = 1$, the transformation is an identity function and it does not change the image.
- The value of $c$ is usually chosen to normalize the output pixel values to the range [0, 255].
- Power-law transformations can be applied to grayscale or color images, but they may affect the color balance of the image if applied to each channel separately.
- Power-law transformations can be used to correct the effects of different types of illumination or sensors on the image, such as the nonlinearity of CRT monitors or the sensitivity of CCD cameras .
- Power-law transformations can also be used to enhance the details or edges of the image by changing the local contrast.



### Histogram Processing

- A histogram is a graphical representation of the distribution of pixel values in an image. It shows how many pixels have a certain intensity value, ranging from 0 (black) to 255 (white) for a grayscale image, or from 0 to 255 for each color channel (red, green, blue) for a color image.
- Histogram processing is the manipulation of an image's histogram to modify its appearance or enhance its features. It can be used for contrast enhancement, brightness adjustment, color correction, noise reduction, segmentation, and other applications.
- Some common histogram processing techniques are:

  - Histogram equalization: This is a method of transforming an image so that its histogram is uniformly distributed, meaning that each intensity value has the same frequency. This can improve the contrast and brightness of an image, especially if it is too dark or too light.
  - Histogram matching: This is a method of transforming an image so that its histogram matches a specified histogram, which can be from another image or a desired distribution. This can be used for color correction, style transfer, or normalization of images from different sources.
  - Histogram stretching: This is a method of transforming an image so that its histogram covers the entire range of intensity values, from 0 to 255. This can enhance the contrast and details of an image, especially if it has a narrow histogram.
  - Histogram clipping: This is a method of transforming an image so that its histogram is limited to a certain range of intensity values, by setting the values outside the range to the minimum or maximum value. This can reduce the noise and outliers in an image, especially if it has a skewed histogram.
  - Histogram smoothing: This is a method of transforming an image so that its histogram is less jagged and more continuous, by applying a low-pass filter or a moving average to the histogram. This can reduce the noise and artifacts in an image, especially if it has a noisy histogram.



### Color Fundamentals

- Color is a property of electromagnetic (EM) radiation that is perceived by human vision or measured by color sensors .
- Color depends on the wavelength and intensity of the EM radiation, as well as the characteristics of the observer or the sensor.
- Human color vision is achieved through 6 to 7 million cones in each eye, which are sensitive to different ranges of wavelengths.
- There are three principal sensing groups of cones: red-sensitive (66%), green-sensitive (33%), and blue-sensitive (2%).
- The combination of these three primary colors can produce a wide range of color sensations, such as yellow, magenta, and cyan.
- Color can be represented by different models, such as RGB (red, green, blue), CMYK (cyan, magenta, yellow, black), HSV (hue, saturation, value), and HSL (hue, saturation, lightness).
- Color models can be used to describe, manipulate, and display color images on various devices, such as monitors, printers, and cameras.
- Color images can be stored and processed as multidimensional arrays, where each pixel has one or more color components, depending on the color model used.
- Color images can be classified into different types, such as grayscale, color, multispectral, and hyperspectral.
- Grayscale images have only one color component, which represents the intensity or brightness of the pixel.
- Color images have three or more color components, which represent the primary colors or the color attributes of the pixel.
- Multispectral images have a few discrete spectral channels or wavebands (typically fewer than 10), which capture the reflectance or emission of the object at different wavelengths.
- Hyperspectral images have a sequence of contiguous wavebands covering a specific spectral region (e.g., visible and near-infrared), which provide more detailed information about the object's spectral signature.
- Color image processing involves various techniques and applications, such as color enhancement, color segmentation, color feature extraction, color recognition, color correction, and color analysis .
- Color image processing can be performed in different color spaces, depending on the task and the desired output.
- Color image processing can be used for various purposes, such as artistic expression, scientific visualization, medical diagnosis, remote sensing, security, and entertainment .



### Fundamentals of Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image by applying a filter or a mask to each pixel of the image.
- A filter or a mask is a small matrix of numbers, usually of odd size, such as 3x3, 5x5, etc.
- The filter or mask is moved over the image, pixel by pixel, and a new value for each pixel is calculated based on the values of its neighbors and the filter coefficients.
- The new value of a pixel is usually the weighted average of its neighbors, where the weights are given by the filter coefficients.
- The process of applying a filter or a mask to an image is also called convolution or correlation, depending on how the filter coefficients are arranged and multiplied with the pixel values.
- Convolution and correlation are mathematically equivalent, except for a 180-degree rotation of the filter matrix.
- Spatial filtering can be used for various purposes, such as smoothing, sharpening, edge detection, noise reduction, etc.
- Different types of filters or masks can produce different effects on the image, such as low-pass, high-pass, band-pass, etc.
- Low-pass filters are used to smooth or blur an image by removing high-frequency components, such as edges and details.
- High-pass filters are used to sharpen or enhance an image by emphasizing high-frequency components, such as edges and details.
- Band-pass filters are used to retain or extract a specific range of frequencies from an image, such as textures or patterns.
- Spatial filtering can be performed in either the spatial domain or the frequency domain, depending on the complexity and efficiency of the filter or the mask.
- Spatial domain filtering is more intuitive and simple, but may require more computations and iterations for complex filters or large images.
- Frequency domain filtering is more efficient and flexible, but may require more preprocessing and postprocessing steps, such as Fourier transform and inverse Fourier transform.



### Smoothing Spatial Filters

- Smoothing spatial filters are used for blurring and for noise reduction in digital image processing.
- Blurring is used to remove small details, bridge small gaps, or reduce the effect of camera motion.
- Noise reduction is used to improve the quality of an image by removing unwanted variations in pixel values.
- Smoothing spatial filters operate in the spatial domain, which means they use a mask or a kernel to modify each pixel value based on its neighbors.
- The mask or kernel is a small matrix that slides over the image and applies a mathematical operation to each pixel and its neighbors.
- The output pixel value is the result of the operation, which can be a linear or a non-linear function.
- Linear smoothing filters use the average or the weighted average of the pixel values in the neighborhood .
- Non-linear smoothing filters use the median, the minimum, the maximum, or other order statistics of the pixel values in the neighborhood.
- Commonly used smoothing filters include:
  - Average smoothing filter: uses a mask with equal coefficients to compute the mean of the pixel values in the neighborhood .
  - Gaussian smoothing filter: uses a mask with Gaussian coefficients to compute the weighted mean of the pixel values in the neighborhood.
  - Adaptive smoothing filter: uses a mask with variable coefficients to adjust the smoothing level based on the local variance of the pixel values in the neighborhood.
  - Median smoothing filter: uses a mask to compute the median of the pixel values in the neighborhood.
  - Max smoothing filter: uses a mask to compute the maximum of the pixel values in the neighborhood.
  - Min smoothing filter: uses a mask to compute the minimum of the pixel values in the neighborhood.
- Smoothing spatial filters can reduce noise and enhance edges, but they can also introduce blurring and lose details .
- The choice of the smoothing filter depends on the type and level of noise, the size and shape of the mask, and the desired output quality .



### Sharpening Spatial Filters

- Sharpening spatial filters are used to enhance the edges and fine details of an image by increasing the contrast between neighboring pixels.
- Sharpening spatial filters are also called high-pass filters because they attenuate the low-frequency components and preserve the high-frequency components of the image spectrum.
- Sharpening spatial filters can be implemented by using the convolution operation in the spatial domain, where an image is multiplied by a kernel or a mask of a certain size and shape.
- Sharpening spatial filters can be classified into two types: first-order derivative filters and second-order derivative filters.
- First-order derivative filters use the gradient or the rate of change of pixel intensity to detect the edges. Examples of first-order derivative filters are the Prewitt, Sobel, and Roberts filters.
- Second-order derivative filters use the Laplacian or the rate of change of the gradient to detect the edges. Examples of second-order derivative filters are the Laplacian and the Laplacian of Gaussian filters.
- Sharpening spatial filters can produce some undesirable effects, such as noise amplification, ringing artifacts, and false edges. Therefore, some techniques are used to improve the quality of the sharpened image, such as smoothing before sharpening, unsharp masking, and high-boost filtering.



## Unit 2 - Morphological Image Processing

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes or patterns that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be used to modify the boundaries, holes, and connectivity of objects in an image.
- Erosion shrinks an object by removing pixels that do not fit the structuring element, while dilation expands an object by adding pixels that fit the structuring element.
- Erosion and dilation can be combined to form more complex operations, such as opening, closing, boundary extraction, hole filling, and skeletonization.
- Opening is the erosion of an object followed by the dilation of the eroded object, which can be used to remove small noise or protrusions from the object boundary.
- Closing is the dilation of an object followed by the erosion of the dilated object, which can be used to fill small gaps or holes in the object boundary.
- Boundary extraction is the subtraction of the eroded object from the original object, which can be used to highlight the contour of the object.
- Hole filling is the complement of the dilation of the complement of the object, which can be used to fill the interior holes of the object.
- Skeletonization is the iterative erosion of the object until only a thin line remains, which can be used to represent the shape and topology of the object.



### Morphological Image Processing

- Morphological image processing is a collection of non-linear operations that process images based on shapes or morphology of features in an image, such as boundaries, skeletons, etc.  
- Morphological operations apply a structuring element to an input image, creating an output image of the same size. The structuring element is a small shape or template that defines the region of interest or neighborhood around a pixel.   
- The value of the output pixel depends on the morphological operation performed, such as erosion, dilation, opening, closing, etc.  
- Morphological operations can be used for various purposes, such as noise removal, edge detection, image enhancement, image segmentation, thinning, skeletonization, etc.    
- Morphological operations are usually performed on binary images, but can also be extended to grayscale images.



### Fundamentals for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Morphological image processing is a technique that deals with the shape and structure of objects in an image.
- It is based on the mathematical theory of sets and the concept of structuring elements, which are small shapes that are used to probe the image.
- The basic operations of morphological image processing are erosion and dilation, which can be combined to form more complex operations such as opening, closing, thinning, thickening, skeletonization, etc.
- Erosion is an operation that shrinks the foreground objects in an image by removing pixels from their boundaries. It is defined as the intersection of the image and the translated structuring element.
- Dilation is an operation that expands the foreground objects in an image by adding pixels to their boundaries. It is defined as the union of the image and the translated structuring element.
- Opening is an operation that smooths the contours of the foreground objects and removes small protrusions. It is defined as the erosion followed by the dilation of the image by the same structuring element.
- Closing is an operation that smooths the contours of the foreground objects and fills small holes. It is defined as the dilation followed by the erosion of the image by the same structuring element.
- Thinning is an operation that reduces the foreground objects to one-pixel wide skeletons. It is defined as the repeated erosion of the image until no further change occurs, while preserving the connectivity and end-points of the objects.
- Thickening is an operation that increases the thickness of the foreground objects by one pixel. It is defined as the repeated dilation of the image until no further change occurs, while preserving the connectivity and end-points of the objects.
- Skeletonization is an operation that extracts the skeleton of the foreground objects, which is the set of pixels that are equidistant from the object boundaries. It is defined as the repeated application of thinning and thickening until the skeleton is obtained.
- Morphological image processing can be applied to binary or grayscale images, depending on the type of structuring element and the definition of the operations.
- Morphological image processing can be used for various purposes, such as noise removal, edge detection, segmentation, feature extraction, shape analysis, etc.



### Erosion and Dilation for the notes of the Unit 2 - Morphological Image Processing in the subject of IMAGE ANALYTICS

- Erosion and dilation are two basic operations in morphological image processing, which is a branch of image processing that deals with the shape and structure of objects in an image.
- Erosion and dilation are applied to binary images, which are images that have only two pixel values: 0 (black) and 1 (white).
- Erosion and dilation use a structuring element, which is a small binary image that defines the neighborhood of a pixel. The shape and size of the structuring element affect the result of the operations.
- Erosion is an operation that shrinks or thins the foreground (white) regions in an image. It removes the pixels that are not covered by the structuring element when it is placed over each pixel in the image.
- Dilation is an operation that expands or thickens the foreground (white) regions in an image. It adds the pixels that are covered by the structuring element when it is placed over each pixel in the image.
- Erosion and dilation can be used for various purposes, such as noise removal, edge detection, boundary extraction, skeletonization, and morphological filtering.



### Opening and Closing

- Opening and closing are two important operations in morphological image processing that can be used to smooth the contours of an object, eliminate small holes or gaps, and fuse narrow breaks or cracks.
- Opening is defined as the erosion of an image by a structuring element, followed by the dilation of the eroded image by the same structuring element. Mathematically, opening of an image A by a structuring element B is denoted as A ○ B and is given by:

    A ○ B = (A ⊖ B) ⊕ B

- Opening has the following properties:

    - It is idempotent, i.e., A ○ B = (A ○ B) ○ B
    - It is anti-extensive, i.e., A ○ B ⊆ A
    - It is increasing, i.e., if A ⊆ C, then A ○ B ⊆ C ○ B
    - It preserves the connectivity of the foreground regions of A
    - It eliminates small objects or protrusions from A that cannot contain B

- Closing is defined as the dilation of an image by a structuring element, followed by the erosion of the dilated image by the same structuring element. Mathematically, closing of an image A by a structuring element B is denoted as A ● B and is given by:

    A ● B = (A ⊕ B) ⊖ B

- Closing has the following properties:

    - It is idempotent, i.e., A ● B = (A ● B) ● B
    - It is extensive, i.e., A ⊆ A ● B
    - It is increasing, i.e., if A ⊆ C, then A ● B ⊆ C ● B
    - It preserves the connectivity of the background regions of A
    - It fills small holes or gaps in A that can contain B

- Opening and closing are dual operations, i.e., the opening of the complement of an image A by a structuring element B is equal to the complement of the closing of A by the reflection of B, and vice versa. Mathematically, this can be expressed as:

    (Ac ○ B) = (A ● B̂)c

    (Ac ● B) = (A ○ B̂)c

    where B̂ is the reflection of B, i.e., B̂(x,y) = B(-x,-y)

- Opening and closing can be combined to create more complex morphological transformations, such as opening followed by closing, closing followed by opening, opening by reconstruction, and closing by reconstruction. These transformations can be used to enhance the image quality, remove noise, or extract features.



### Hit or Miss Transform

- Hit or miss transform is a morphological operation that detects a given configuration or pattern in a binary image, using the morphological erosion operator and a pair of disjoint structuring elements  .
- The hit or miss transform can be defined as follows :

  - Let A be the input binary image and B be the composite structuring element, which consists of two disjoint parts: B1 (the foreground) and B2 (the background).
  - The hit or miss transform of A by B, denoted by A ⊖ B, is given by:

    A ⊖ B = (A ⊖ B1) ∩ (Ac ⊖ B2)

  - where Ac is the complement of A, ⊖ is the erosion operator, and ∩ is the intersection operator.
  - The hit or miss transform indicates the positions where the pattern characterized by B occurs in the input image A.
  - The pattern is detected only if the foreground part B1 matches the image A and the background part B2 matches the complement of A simultaneously.

- The hit or miss transform can be used for various applications, such as :

  - Pruning: identifying and removing the end-points of a line to eliminate unwanted branches.
  - Thinning: iteratively applying the hit or miss transform with different structuring elements to reduce the thickness of an object to one pixel.
  - Thickening: iteratively applying the hit or miss transform with different structuring elements to increase the thickness of an object by one pixel.
  - Skeletonization: finding the medial axis of an object by iteratively applying the hit or miss transform until the object is reduced to a single pixel wide skeleton.
  - Corner detection: finding the corners of an object by applying the hit or miss transform with different structuring elements that match the shape of a corner.

- The hit or miss transform can be implemented using various libraries, such as OpenCV and Mahotas.



### Some Basic Morphological Algorithms

- Morphological operations are a set of image processing algorithms that process images based on shapes .
- Morphological operations rely only on the relative ordering of pixel values, not on their numerical values, and therefore are especially suited to the processing of binary images.
- Morphological operations use predefined kernels, known as structuring elements, that define patterns that are used to process images .
- A structuring element influences the size and shape of objects to process in the image.
- Some basic morphological operations are:
  - Dilation: It enlarges or expands the boundaries of objects in an image. It can be used to fill small holes or gaps in an image.
  - Erosion: It shrinks or reduces the boundaries of objects in an image. It can be used to remove small noise or outliers in an image.
  - Opening: It is a combination of erosion followed by dilation. It can be used to smooth the contours of objects and separate objects that are connected.
  - Closing: It is a combination of dilation followed by erosion. It can be used to fill small holes or gaps inside objects and connect objects that are close.
  - Reconstruction: It is used to extract marked objects from an image without changing the object size or shape. It can be used to restore the original shape of objects after erosion or opening.
- An example of morphological operations on a binary image is shown below:

morphological operations example

: An Introduction to Morphological Operations for Digital Image Text Classification, https://medium.com/hackernoon/an-introduction-to-morphological-operations-for-digital-image-text-classification-79cb14bab2d7
: Morphological Operations - MATLAB & Simulink - MathWorks, https://www.mathworks.com/help/images/morphological-filtering.html
: Morphological Operations in Image Processing, https://himnickson.medium.com/morphological-operations-in-image-processing-cb8045b98fcc
: Basic Morphological Algorithms, https://www.taylorfrancis.com/chapters/mono/10.1201/9781420089448-8/basic-morphological-algorithms-frank-shih



### Morphological Reconstruction

- Morphological reconstruction is a technique to extract or enhance marked objects from an image without changing their size or shape .
- Morphological reconstruction uses two images: a marker image and a mask image. The marker image specifies the regions of interest, while the mask image defines the boundaries of the objects.
- The marker image must be equal to or smaller than the mask image in a pointwise sense, i.e., each pixel value in the marker image must be less than or equal to the corresponding pixel value in the mask image.
- The basic operation of morphological reconstruction is geodesic dilation, which dilates the marker image under the constraints of the mask image. Geodesic dilation can be iterated until the image values stop changing, resulting in the reconstructed image.
- Morphological reconstruction can be used for various applications, such as filling holes, extracting the largest connected component, removing small objects, smoothing boundaries, and separating touching objects .
- Morphological reconstruction can be performed in binary or grayscale images, and can be extended to use erosion instead of dilation .



### Grayscale Morphology

- Grayscale morphology is an image processing technique used to produce a modified image from an original image by applying a set of mathematical operations.
- It is used to modify the shapes and patterns of objects in an image without changing their identities.
- Grayscale image processing can be identified by analyzing the amount of shades of gray present in the image. Generally, the more shades of gray present in the image, the higher the level of image processing. This is because the more gray values present, the more detail can be interpreted from the image.
- Grayscale morphology is based on the concepts of umbrae and structuring elements. Umbrae are sets of points in a grayscale image that have gray values greater than or equal to a given threshold. Structuring elements are small images that define the neighborhood of a pixel.
- Grayscale morphology can be performed using four basic operations: dilation, erosion, opening, and closing.
- Dilation is the process of expanding the boundaries of objects in an image by adding pixels to the edges. It can be used to fill small holes, connect disjoint parts, and smooth contours.
- Erosion is the process of shrinking the boundaries of objects in an image by removing pixels from the edges. It can be used to eliminate small objects, separate connected parts, and thin out regions.
- Opening is the process of applying erosion followed by dilation. It can be used to remove small objects and noise, while preserving the shape and size of larger objects.
- Closing is the process of applying dilation followed by erosion. It can be used to fill small gaps and holes, while preserving the shape and size of larger objects.
- Grayscale morphology can be applied to various applications, such as edge detection, image enhancement, image segmentation, and image filtering.



## Unit 3 - Image Segmentation

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, intensity, shape, etc.
- Image segmentation can be used for various applications, such as object detection, face recognition, medical imaging, scene understanding, etc.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised segmentation uses a set of labeled images as training data to learn a model that can segment new images based on the given labels.
  - Unsupervised segmentation does not use any labeled data, but instead relies on some intrinsic properties of the image, such as similarity, continuity, or compactness, to group pixels into regions.
- Some common methods for image segmentation are:
  - Thresholding: This method uses a global or local threshold value to separate the foreground and background pixels based on their intensity values.
  - Edge detection: This method uses filters or operators to detect the boundaries or edges of the objects in the image, and then segments the image based on the edge map.
  - Region growing: This method starts from a set of seed pixels and expands the regions by adding neighboring pixels that are similar to the seeds based on some criteria, such as intensity, color, or texture.
  - Clustering: This method groups pixels into clusters based on their feature vectors, such as intensity, color, or texture, using algorithms such as K-means, Fuzzy C-means, or Mean-shift.
  - Graph-based: This method models the image as a graph, where the nodes are the pixels and the edges are the similarities or distances between the pixels, and then partitions the graph into segments using algorithms such as Minimum Spanning Tree, Normalized Cuts, or Graph Cuts.
  - Deep learning: This method uses neural networks, such as Convolutional Neural Networks (CNNs), Fully Convolutional Networks (FCNs), or U-Nets, to learn a mapping from the input image to the output segmentation mask, using labeled or unlabeled data.



### Introduction for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into multiple regions or segments that have similar characteristics or features.
- Image segmentation is useful for various applications, such as object detection, face recognition, medical imaging, scene understanding, etc.
- Image segmentation can be performed using different methods, such as thresholding, clustering, edge detection, region growing, watershed, etc.
- Image segmentation can be classified into two types: supervised and unsupervised.
  - Supervised segmentation uses prior knowledge or labels to guide the segmentation process, such as ground truth masks, annotations, or training data.
  - Unsupervised segmentation does not use any prior knowledge or labels, and relies on the inherent properties or features of the image, such as intensity, color, texture, etc.
- Image segmentation can be evaluated using different metrics, such as accuracy, precision, recall, F1-score, Jaccard index, Dice coefficient, etc.
- Image segmentation is a challenging task, as it requires dealing with various issues, such as noise, occlusion, illumination, scale, shape, etc.



### Point for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of assigning a label to every pixel in an image such that pixels with the same label share certain characteristics .
- Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be classified into two main types: semantic segmentation and instance segmentation.
- Semantic segmentation assigns a class label to each pixel, such as sky, road, car, person, etc. Semantic segmentation does not distinguish between different instances of the same class.
- Instance segmentation assigns a unique label to each pixel belonging to a specific object instance, such as car1, car2, person1, person2, etc. Instance segmentation can separate overlapping objects of the same class.
- Some of the common techniques for image segmentation are: thresholding, region-based methods, edge-based methods, clustering, and deep learning.
- Thresholding is a simple technique that divides the image into foreground and background based on a predefined intensity value.
- Region-based methods are techniques that group pixels based on their similarity or proximity, such as region growing, region splitting, and region merging.
- Edge-based methods are techniques that detect the boundaries of objects based on the discontinuities in the image intensity, such as gradient, Laplacian, Canny, and Sobel operators.
- Clustering is a technique that partitions the image into clusters based on the similarity of pixel features, such as color, texture, shape, etc. Some of the popular clustering algorithms are k-means, mean-shift, and hierarchical clustering.
- Deep learning is a technique that uses neural networks to learn the features and labels of the image segments from a large amount of annotated data. Some of the popular deep learning models for image segmentation are U-Net, SegNet, Mask R-CNN, and DeepLab.



### Line for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing a digital image into subgroups called image segments, reducing the complexity of the image and enabling further processing or analysis of each image segment.
- Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images .
- Image segmentation is the assignment of labels to pixels to identify objects, people, or other important elements in the image.
- Image segmentation can be performed using various techniques, such as thresholding, clustering, edge detection, region growing, watershed, active contours, graph cuts, etc.
- Image segmentation can be classified into two types: semantic segmentation and instance segmentation.
- Semantic segmentation assigns a class label to each pixel, such as sky, road, car, person, etc. Semantic segmentation does not distinguish between different instances of the same class.
- Instance segmentation assigns a unique label to each pixel belonging to a specific object instance, such as car1, car2, person1, person2, etc. Instance segmentation can differentiate between different instances of the same class.
- Image segmentation can be applied to various domains, such as medical imaging, autonomous driving, face recognition, object detection, etc.



### Edge Detection

- Edge detection is an image processing technique for finding the boundaries of objects within images. It works by detecting discontinuities in brightness .
- Edge detection is used for image segmentation and data extraction in areas such as image processing, computer vision, and machine vision.
- Image segmentation is the process of partitioning images into sets of pixels. Pixels within the same set or “label” will share certain characteristics such as color, brightness, intensity, or texture.
- Edge detection allows users to observe the features of an image for a significant change in the gray level.
- Edge detection can be performed using various operators, such as Sobel, Prewitt, Roberts, Canny, Laplacian, etc. Each operator has its own advantages and disadvantages in terms of accuracy, speed, noise sensitivity, etc  .
- Edge detection can be applied to various applications, such as object recognition, face detection, medical imaging, video surveillance, etc .



### Thresholding for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, intensity, texture, etc.
- Image thresholding is a type of image segmentation that divides the foreground from the background in an image by using a threshold value.
- A threshold value is a pixel intensity level that separates the pixels into two classes: one class for pixels above the threshold and another class for pixels below the threshold.
- A binary image is an image whose pixels have only two values: 0 and 1. A binary image can be obtained from a grayscale image by applying a thresholding operation.
- There are different types of thresholding methods, such as global thresholding, local thresholding, adaptive thresholding, and Otsu's method.
- Global thresholding is a simple and widely used method that applies the same threshold value to the whole image. It is suitable for images with uniform illumination and contrast.
- Local thresholding is a method that applies different threshold values to different regions of the image based on the local characteristics of the image. It is suitable for images with varying illumination and contrast.
- Adaptive thresholding is a method that adjusts the threshold value dynamically according to the image content and the desired output. It is suitable for images with complex and non-uniform backgrounds.
- Otsu's method is a popular and efficient method that automatically determines the optimal threshold value by maximizing the inter-class variance of the pixel intensities. It is suitable for images with bimodal histograms.



### Foundation for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing a digital image into subgroups called image segments, reducing the complexity of the image and enabling further processing or analysis of each image segment.
- Image segmentation is typically used to locate objects and boundaries (lines, curves, etc.) in images .
- Image segmentation is the assignment of labels to pixels to identify objects, people, or other important elements in the image.
- Image segmentation can be done based on various heuristics, or high-level image features, such as color, intensity, texture, shape, etc.
- Image segmentation can be classified into two main types: semantic segmentation and instance segmentation.
- Semantic segmentation assigns a class label to each pixel, such as sky, road, car, etc., without distinguishing between different instances of the same class.
- Instance segmentation assigns a class label and an instance identifier to each pixel, such as car1, car2, etc., allowing to separate and count individual objects of the same class.
- Image segmentation can be performed using various techniques, such as thresholding, clustering, region growing, edge detection, graph-based methods, deep learning, etc.
- Image segmentation is an important and challenging task in image analytics, as it can provide useful information for various applications, such as medical imaging, autonomous driving, face recognition, object detection, etc.



### Basic Global Thresholding for Image Segmentation

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as intensity, color, texture, etc.
- Thresholding is one of the simplest and most common techniques for image segmentation, which generates a binary image from a grayscale image by separating it into two regions based on a threshold value.
- A binary image is one whose pixels have only two values: 0 (black) or 1 (white), and thus requires only one bit to store pixel intensity.
- A threshold value is a scalar that determines which pixels belong to the foreground (object) or the background, depending on whether the pixel intensity is greater or less than the threshold value.
- Global thresholding is a type of thresholding that uses a single or constant threshold value for the entire image, assuming that the intensity distribution of the object and the background are sufficiently distinct and uniform.
- The basic global thresholding algorithm iteratively finds the best threshold value that minimizes the within-class variance or maximizes the between-class variance of the object and the background pixels.
- The algorithm is as follows:

  1. Choose an initial threshold value, T, such as the mean or median of the pixel intensities.
  2. Segment the image using T, and label the pixels as object or background.
  3. Compute the mean intensities of the object and background pixels, m1 and m2, respectively.
  4. Compute a new threshold value, T', as the average of m1 and m2.
  5. Repeat steps 2 to 4 until the difference between T and T' is smaller than a predefined tolerance, or until T converges to a stable value.
  6. The final threshold value, T, is used to segment the image.

- The following figure shows an example of global thresholding applied to an image of a coin.

Global thresholding example

- The advantages of global thresholding are:

  - It is simple and fast to implement and compute.
  - It is suitable for images with high contrast and uniform illumination.
  - It can be easily extended to multilevel thresholding, which uses multiple threshold values to segment an image into more than two regions.

- The disadvantages of global thresholding are:

  - It is sensitive to noise and outliers, which can affect the threshold value and the segmentation result.
  - It is not robust to variations in illumination, which can cause uneven intensity distribution and make the object and background indistinguishable.
  - It is not applicable to images with complex or overlapping objects, which may have similar or overlapping intensity ranges.



### Optimum Global Thresholding using Otsu’s Method

- Otsu’s method is a technique of performing global thresholding on a digital image. It is optimum in the sense that it maximizes the between-class variance .
- Global thresholding is a process of converting a grayscale image into a binary image by using a single intensity value as a threshold .
- Otsu’s method assumes that the image contains two classes of pixels: foreground and background, and that the histogram of the image is bimodal .
- Otsu’s method aims to find the optimal threshold value that minimizes the within-class variance or maximizes the inter-class variance of the two classes  .
- Otsu’s method can be formulated as an optimization problem as follows  :

  - Let p(i) be the probability of pixel intensity i in the image, where i ranges from 0 to L-1, and L is the number of possible intensity levels.
  - Let T be the threshold value that separates the foreground and background classes, where 0 <= T <= L-1.
  - Let w0 and w1 be the probabilities of the foreground and background classes, respectively, defined as:

    - w0 = sum(p(i)) for i = 0 to T
    - w1 = sum(p(i)) for i = T+1 to L-1

  - Let u0 and u1 be the mean intensities of the foreground and background classes, respectively, defined as:

    - u0 = sum(i * p(i)) / w0 for i = 0 to T
    - u1 = sum(i * p(i)) / w1 for i = T+1 to L-1

  - Let u be the overall mean intensity of the image, defined as:

    - u = sum(i * p(i)) for i = 0 to L-1

  - Then, the within-class variance is given by:

    - sigma^2 = w0 * (u0 - u)^2 + w1 * (u1 - u)^2

  - And the inter-class variance is given by:

    - eta^2 = w0 * w1 * (u0 - u1)^2

  - The optimal threshold value T* is the one that minimizes sigma^2 or maximizes eta^2.

- Otsu’s method can be implemented by iterating over all possible threshold values and computing the within-class variance or inter-class variance for each value, and then selecting the value that gives the minimum or maximum result  .
- Otsu’s method can also be implemented by using the cumulative histogram of the image and applying some algebraic manipulations to simplify the computation of the within-class variance or inter-class variance .
- Otsu’s method is a one-dimensional discrete analogue of Fisher's Discriminant Analysis, is related to Jenks optimization method, and is equivalent to a globally optimal k-means performed on the intensity histogram.
- Otsu’s method is simple, fast, and effective for images with bimodal histograms, but it may not work well for images with multimodal histograms or non-uniform illumination  .
- Otsu’s method can be extended to multilevel thresholding by using a recursive approach or a dynamic programming approach .



### Multiple Thresholds

- Multiple thresholding is a technique of image segmentation that classifies the image into three or more regions based on different threshold values .
- Multiple thresholding can be used to segment images that have more than one object of interest on a background, or images that have different levels of brightness or contrast .
- Multiple thresholding can be applied by finding the peaks and valleys of the histogram of the image, and choosing the thresholds that correspond to the valleys.
- Multiple thresholding can also be done by using different methods of histogram analysis, such as entropy, variance, or clustering.
- Multiple thresholding can produce better results than single thresholding in some cases, but it also requires more computation and may introduce more noise or artifacts .



### Variable Thresholding for the notes of the Unit 3 - Image Segmentation in the subject of IMAGE ANALYTICS

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as pixel intensity, color, texture, etc.
- Image thresholding is a simple and widely used technique for image segmentation, where a grayscale or color image is converted into a binary image, i.e., one that has only two pixel values: 0 (black) or 1 (white).
- Image thresholding can be done in two ways: global or local.
  - Global thresholding applies a single threshold value to the whole image, such that any pixel with an intensity above the threshold is set to 1, and any pixel below the threshold is set to 0.
  - Local thresholding applies different threshold values to different regions of the image, depending on the local characteristics of the image, such as brightness, contrast, or noise level.
- Variable thresholding is a type of local thresholding, where the threshold value is not fixed, but varies according to some function of the pixel intensity or its neighborhood.
- Variable thresholding can be useful for images that have uneven illumination, varying background, or complex foreground objects.
- Some examples of variable thresholding methods are:
  - Adaptive thresholding: The threshold value is computed as a weighted mean of the pixel intensity and its neighborhood, with a constant offset. The weights can be uniform or Gaussian, depending on the desired smoothness of the result.
  - Otsu's method: The threshold value is determined by maximizing the between-class variance of the pixel intensities, i.e., the difference between the mean intensities of the foreground and background classes.
  - Niblack's method: The threshold value is computed as the mean of the pixel intensity and its neighborhood, plus or minus a factor times the standard deviation of the neighborhood.
  - Bernsen's method: The threshold value is computed as the midpoint of the minimum and maximum pixel intensities in the neighborhood. If the difference between the minimum and maximum is less than a contrast threshold, the pixel is set to 0 or 1 depending on a global threshold.



### Segmentation by Region Growing and by Region Splitting and Merging

- Segmentation by region growing and by region splitting and merging are two methods of image segmentation that are based on the concept of regions.
- A region is a connected set of pixels that share some common properties, such as intensity, color, texture, etc.
- The goal of segmentation by region growing and by region splitting and merging is to partition an image into homogeneous and meaningful regions that correspond to objects or parts of objects in the scene.

#### Segmentation by Region Growing

- Segmentation by region growing is a bottom-up approach that starts with a set of seed pixels and grows regions by adding neighboring pixels that are similar to the seeds.
- The similarity criterion can be based on intensity, color, texture, or any other feature that characterizes the region of interest.
- The region growing process can be iterative or recursive, and can be implemented using a queue, a stack, or a priority queue data structure.
- The advantages of segmentation by region growing are that it is simple, flexible, and adaptive to the image content.
- The disadvantages of segmentation by region growing are that it is sensitive to noise, seed selection, and similarity threshold, and that it may produce over-segmented or under-segmented results.

#### Segmentation by Region Splitting and Merging

- Segmentation by region splitting and merging is a top-down approach that starts with the whole image as a single region and recursively splits it into smaller regions or merges adjacent regions until some homogeneity criterion is satisfied.
- The splitting criterion can be based on the variance, entropy, or any other measure of heterogeneity of the region.
- The merging criterion can be based on the similarity, distance, or any other measure of proximity of the adjacent regions.
- The region splitting and merging process can be implemented using a quadtree, an octree, or a binary tree data structure.
- The advantages of segmentation by region splitting and merging are that it is robust to noise, independent of seed selection, and can handle complex shapes and boundaries.
- The disadvantages of segmentation by region splitting and merging are that it is computationally expensive, sensitive to the homogeneity threshold, and may produce over-segmented or under-segmented results.



### Image Segmentation

- Image segmentation is the process of dividing an image into multiple regions or segments that share some common characteristics, such as color, intensity, texture, or shape.
- Image segmentation can be used for various applications, such as object detection, face recognition, medical imaging, scene understanding, and image compression.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised segmentation uses some prior knowledge or labels to guide the segmentation process, such as ground truth masks, bounding boxes, or user inputs.
  - Unsupervised segmentation does not use any prior knowledge or labels, and relies on the intrinsic properties of the image data, such as pixel values, gradients, or edges.
- Image segmentation can be further categorized into different methods, such as thresholding, region-based, edge-based, clustering, graph-based, and deep learning-based methods.
  - Thresholding is the simplest method of image segmentation, which assigns pixels to different regions based on a predefined threshold value or range of values.
  - Region-based methods segment an image by growing or merging regions that have similar pixel values or features, such as region growing, region splitting, and region merging.
  - Edge-based methods segment an image by detecting the boundaries or contours of the regions, using operators such as Sobel, Canny, or Laplacian.
  - Clustering methods segment an image by grouping pixels into clusters based on their similarity or distance, using algorithms such as K-means, Fuzzy C-means, or Mean-shift.
  - Graph-based methods segment an image by modeling it as a graph, where nodes represent pixels or regions, and edges represent the similarity or dissimilarity between them, using techniques such as minimum spanning tree, normalized cuts, or graph cuts.
  - Deep learning-based methods segment an image by using neural networks, such as convolutional neural networks (CNNs), recurrent neural networks (RNNs), or generative adversarial networks (GANs), to learn the features and labels of the regions, using datasets such as PASCAL VOC, MS COCO, or Cityscapes.



### Active Contours for Image Segmentation

- Active contours, also known as snakes, are curves that can deform and move towards the boundaries of objects in an image .
- Active contours are based on minimizing an energy functional that consists of internal and external forces.
- Internal forces are derived from the curve properties, such as smoothness and continuity, and they tend to keep the curve regular and prevent it from breaking.
- External forces are derived from the image data, such as gradients, edges, and regions, and they tend to attract the curve towards the object boundaries.
- Active contours can be classified into two types: parametric and geometric.
- Parametric active contours use explicit representations of the curve, such as splines or polynomials, and they update the curve parameters iteratively using an optimization algorithm.
- Geometric active contours use implicit representations of the curve, such as level sets or signed distance functions, and they evolve the curve according to a partial differential equation.
- Active contours can handle complex shapes, topological changes, and noisy images, but they also have some limitations, such as sensitivity to initialization, parameter tuning, and local minima.
- Active contours have many applications in image segmentation, such as medical image analysis, object tracking, shape recognition, and face detection  .



### Snakes and Level Sets for Image Segmentation

- Snakes or active contour models are classical methods for boundary detection and segmentation, which deform an initial contour (for 2D image) or a surface (for 3D image) towards the boundary of the desired object.
- Snakes are parametric curves that minimize an energy functional composed of internal and external forces. Internal forces are derived from the curve's shape and smoothness, while external forces are derived from the image's gradient, edge, or region information.
- Snakes can segment one component at a time and they depend on the initial seed. They may also get stuck in local minima or be sensitive to noise.
- Level sets are implicit 3D surfaces where the zero-level represents the segmentation. Level sets are based on partial differential equations that evolve the surface according to geometric flow.
- Level sets can segment multiple components and they are more generic. They can handle topological changes and complex shapes. They are also less sensitive to noise and initial conditions.
- Level sets are computationally more expensive than snakes and they may require regularization or reinitialization to maintain numerical stability.
- Both snakes and level sets are evolving techniques that take some time to produce the segmentation and they may require user interaction or prior knowledge to guide the process .



## Unit 4 - Feature Extraction

- Feature extraction is the process of transforming raw data into a set of features that can be used for machine learning tasks, such as classification, clustering, or regression.
- Features are the attributes or properties of the data that are relevant for the task at hand. They can be numerical, categorical, binary, or text-based.
- Feature extraction can be done in different ways, depending on the type and structure of the data. Some common methods are:

  - Dimensionality reduction: reducing the number of features by applying techniques such as principal component analysis (PCA), linear discriminant analysis (LDA), or autoencoders. This can help remove noise, redundancy, and irrelevant information from the data, and improve the computational efficiency and performance of the machine learning models.
  - Feature selection: selecting a subset of features that are most informative and discriminative for the task, by using criteria such as correlation, mutual information, or chi-square test. This can help avoid overfitting, reduce complexity, and enhance interpretability of the models.
  - Feature engineering: creating new features from the existing data, by applying domain knowledge, mathematical transformations, or statistical methods. This can help capture the underlying patterns, relationships, or interactions among the data, and enhance the predictive power of the models.
  - Feature learning: learning features from the data automatically, by using unsupervised or supervised machine learning algorithms, such as clustering, dictionary learning, or deep neural networks. This can help discover hidden or latent features that are not obvious or accessible from the raw data, and adapt to the specific task and data distribution.



### Background for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Feature extraction is the process of transforming an image into a set of numerical or symbolic features that represent its characteristics or properties.
- Features can be low-level, such as pixels, edges, corners, or regions, or high-level, such as faces, objects, or scenes.
- Feature extraction can be used for various purposes, such as image compression, image enhancement, image segmentation, image classification, image retrieval, image recognition, or image understanding.
- Feature extraction can be performed in different domains, such as spatial domain, frequency domain, or transform domain.
- Feature extraction can be based on different methods, such as statistical methods, geometric methods, algebraic methods, or machine learning methods.
- Feature extraction can be influenced by different factors, such as image quality, image resolution, image noise, image contrast, image scale, image orientation, or image illumination.



### Representation for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Feature extraction is the process of transforming an initial set of measured data (such as pixel values of an image) into a set of derived values (features) that are informative, non-redundant, and suitable for subsequent learning and generalization steps .
- Features are the characteristics or attributes of an image that can be used for identification, classification, diagnosis, clustering, recognition, and detection of objects or regions of interest .
- Feature extraction can be performed by different methods, depending on the type and purpose of the data. Some common methods are:
  - Calculation-based: These methods use mathematical operations and transformations to extract features from the data. For example, edge detection, corner detection, histogram of gradients, Fourier transform, wavelet transform, etc.
  - Recognition-based: These methods use machine learning models and algorithms to learn and extract features from the data. For example, principal component analysis, linear discriminant analysis, autoencoders, convolutional neural networks, etc.
  - Simulation-based: These methods use physical or biological models and simulations to extract features from the data. For example, optical flow, saliency maps, biologically inspired features, etc.
- Feature extraction can be applied to different types of image data, such as grayscale, color, multispectral, hyperspectral, thermal, medical, etc. Each type of data may require different methods and techniques to extract relevant and meaningful features.
- Feature extraction is an important step in image analytics, as it can reduce the dimensionality, complexity, and noise of the data, and enhance the performance, accuracy, and interpretability of the subsequent analysis and modeling tasks .



### Boundary Preprocessing for Feature Extraction

- Boundary preprocessing is the process of extracting the boundary of an image region, which represents the shape and contour of the object in the image .
- Boundary preprocessing is an important step for feature extraction, which aims to detect and describe the salient characteristics of an image, such as texture, color, shape, and orientation .
- Boundary preprocessing can help to reduce the complexity and dimensionality of the image data, and to enhance the contrast and visibility of the object boundaries .
- Boundary preprocessing can be performed using various techniques, such as morphological operations, edge detection, and thresholding .
- Morphological operations are mathematical operations that modify the shape and size of the image regions based on a structuring element. Some common morphological operations are erosion, dilation, opening, closing, and skeletonization.
- Edge detection is the process of identifying the pixels where the image intensity changes abruptly, which indicate the boundaries of the image regions. Some common edge detection methods are Sobel, Canny, Prewitt, and Laplacian of Gaussian.
- Thresholding is the process of dividing the image into foreground and background regions based on a predefined threshold value. Some common thresholding methods are global, adaptive, and Otsu's thresholding.
- After boundary preprocessing, the extracted boundaries can be further processed to obtain boundary features, such as perimeter, area, compactness, convexity, and curvature . These features can be used for image analysis, such as segmentation, classification, and recognition .



### Boundary Feature Descriptors

- Boundary feature descriptors are methods that extract and represent the shape information of an object based on its boundary or contour.
- Boundary feature descriptors can be classified into two types: global and local.
- Global boundary feature descriptors use the whole boundary of the object to compute a single feature vector that describes its shape. Examples of global boundary feature descriptors are Fourier descriptors, moment invariants, and shape context.
- Local boundary feature descriptors use a part of the boundary of the object to compute a feature vector that describes its local shape. Examples of local boundary feature descriptors are curvature, chain code, and differential invariants.
- Boundary feature descriptors can be used for various applications such as shape recognition, shape matching, shape retrieval, and shape analysis.



### Some Basic Boundary Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Boundary descriptors are features that describe the shape and contour of an object or a region in an image.
- Boundary descriptors can be used for image representation and description, which are important tasks in image processing, computer vision, pattern recognition, and machine learning .
- Some basic boundary descriptors are :
  - **Boundary length**: the number of pixels along the border of the object or region. It can be computed by counting the pixels or using a chain code representation.
  - **Diameter**: the maximum distance between any two pixels on the boundary of the object or region. It can be computed by finding the pair of pixels that have the largest Euclidean distance.
  - **Curvature**: the rate of change of the slope or direction of the boundary. It can be computed by using the first or second derivative of the chain code or by fitting a curve to the boundary points.
  - **Bounding box**: the smallest rectangle that encloses the object or region. It can be computed by finding the minimum and maximum values of the x and y coordinates of the boundary pixels.
  - **Convex hull**: the smallest convex polygon that contains the object or region. It can be computed by using a convex hull algorithm, such as Graham scan or Jarvis march.
  - **Eccentricity**: the ratio of the distance between the foci of the best fitting ellipse to the object or region and its major axis length. It can be computed by using the second moment matrix of the boundary pixels or by fitting an ellipse to the boundary points.
  - **Orientation**: the angle between the major axis of the best fitting ellipse to the object or region and the x-axis. It can be computed by using the second moment matrix of the boundary pixels or by fitting an ellipse to the boundary points.
  - **Compactness**: the ratio of the area of the object or region to the area of a circle with the same perimeter as the object or region. It can be computed by using the formula `4πA/P^2`, where A is the area and P is the perimeter of the object or region.
  - **Circularity**: the inverse of the compactness. It can be computed by using the formula `P^2/4πA`, where P is the perimeter and A is the area of the object or region.



### Shape Numbers for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Shape numbers are numerical representations of the shape of an object in an image.
- Shape numbers can be used for image shape recognition and classification, as well as for content-based image retrieval (CBIR).
- Shape numbers can be derived from various shape features, such as boundary, contour, skeleton, moments, Fourier descriptors, etc.
- Shape numbers can be classified into two types: global and local.
- Global shape numbers capture the overall shape of an object, such as its area, perimeter, circularity, eccentricity, etc.
- Local shape numbers capture the local variations of an object's shape, such as its corners, edges, curvature, etc.
- Some examples of global shape numbers are:

  - Area: the number of pixels inside the object's boundary.
  - Perimeter: the length of the object's boundary.
  - Circularity: the ratio of the object's area to the area of a circle with the same perimeter.
  - Eccentricity: the ratio of the distance between the foci of an ellipse that fits the object's boundary to its major axis length.
  - Compactness: the ratio of the object's area to the square of its perimeter.

- Some examples of local shape numbers are:

  - Corners: the points where the object's boundary changes direction abruptly.
  - Edges: the segments of the object's boundary that are relatively straight.
  - Curvature: the degree of bending of the object's boundary at a given point.
  - Chain code: a sequence of numbers that encodes the direction of the object's boundary pixels.
  - Freeman code: a variant of chain code that uses only four directions (horizontal, vertical, and diagonal).
  - Differential chain code: a variant of chain code that uses the difference between consecutive directions instead of the absolute directions.



### Fourier Descriptors for Shape-Based Image Retrieval

- Fourier descriptors (FDs) are a method of representing and comparing the shapes of objects in images .
- FDs are derived from the Fourier transform of the boundary points of the object .
- FDs have the advantages of being invariant to translation, scale, rotation and starting point of the object  , which means that the shape description does not depend on the position, size, orientation or contour direction of the object.
- FDs can retain the essential information about the contour of the object while discarding the noise and irrelevant details  .
- FDs can be used for shape-based image retrieval, which is the task of finding images that contain objects with similar shapes to a given query object  .
- The steps for using FDs for shape-based image retrieval are  :
  - Extract the boundary points of the object from the image using edge detection or segmentation techniques.
  - Represent the boundary points as a complex vector, where the real and imaginary parts are the x and y coordinates of the points.
  - Apply the discrete Fourier transform (DFT) to the complex vector to obtain the FDs, which are the coefficients of the Fourier series.
  - Normalize the FDs to make them invariant to translation, scale, rotation and starting point by using the following formulas  :
    - Translation invariance: set the first FD to zero.
    - Scale invariance: divide all FDs by the absolute value of the second FD.
    - Rotation invariance: use only the magnitudes of the FDs and discard the phases.
    - Starting point invariance: rotate the complex vector by an angle that minimizes the difference between the first and last FDs.
  - Select a subset of FDs that capture the most important features of the shape, usually the low-frequency components, and discard the rest.
  - Compare the FDs of the query object with the FDs of the objects in the database using a similarity measure, such as the Euclidean distance or the cosine similarity.
  - Retrieve the images that have the most similar FDs to the query object.



### Statistical Moments for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Statistical moments are a set of numerical values that describe the shape and distribution of pixel intensities in an image or a region of an image .
- Statistical moments can be used for various purposes in image analysis, such as pattern recognition, object identification, texture analysis, image compression, and image denoising  .
- The most common types of statistical moments are the raw moments, the central moments, and the normalized central moments .
- The raw moments of order (i,j) for a greyscale image with pixel intensities I(x,y) are defined as:

$$M_{ij} = \sum_{x}\sum_{y} x^i y^j I(x,y)$$

- The raw moments can be used to calculate the centroid (x̄,ȳ) of the image, which is the center of mass of the pixel intensities:

$$\bar{x} = \frac{M_{10}}{M_{00}}$$

$$\bar{y} = \frac{M_{01}}{M_{00}}$$

- The central moments of order (i,j) are obtained by shifting the origin to the centroid of the image:

$$\mu_{ij} = \sum_{x}\sum_{y} (x-\bar{x})^i (y-\bar{y})^j I(x,y)$$

- The central moments are invariant to translation, meaning that they do not change if the image is moved to a different location.
- The normalized central moments of order (i,j) are obtained by dividing the central moments by a scaling factor:

$$\eta_{ij} = \frac{\mu_{ij}}{\mu_{00}^{(1+\frac{i+j}{2})}}$$

- The normalized central moments are invariant to both translation and scaling, meaning that they do not change if the image is moved or resized.
- The normalized central moments can be used to calculate the Hu moments, which are a set of seven values that are invariant to translation, scaling, and rotation, meaning that they do not change if the image is moved, resized, or rotated.
- The Hu moments are defined as:

$$
\begin{aligned}
&H_1 = \eta_{20} + \eta_{02} \\
&H_2 = (\eta_{20} - \eta_{02})^2 + 4\eta_{11}^2 \\
&H_3 = (\eta_{30} - 3\eta_{12})^2 + (3\eta_{21} - \eta_{03})^2 \\
&H_4 = (\eta_{30} + \eta_{12})^2 + (\eta_{21} + \eta_{03})^2 \\
&H_5 = (\eta_{30} - 3\eta_{12})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] + (3\eta_{21} - \eta_{03})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] \\
&H_6 = (\eta_{20} - \eta_{02})[(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2] + 4\eta_{11}(\eta_{30} + \eta_{12})(\eta_{21} + \eta_{03}) \\
&H_7 = (3\eta_{21} - \eta_{03})(\eta_{30} + \eta_{12})[(\eta_{30} + \eta_{12})^2 - 3(\eta_{21} + \eta_{03})^2] - (\eta_{30} - 3\eta_{12})(\eta_{21} + \eta_{03})[3(\eta_{30} + \eta_{12})^2 - (\eta_{21} + \eta_{03})^2]
\end{aligned}
$$

- The Hu moments can be used



### Regional Feature Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Regional feature descriptors are methods that extract and describe distinctive points or regions in an image, such as corners, edges, blobs, etc.
- Regional feature descriptors are useful for image analysis tasks such as object detection, recognition, matching, retrieval, etc.
- Regional feature descriptors can be classified into two categories: local and global.
  - Local feature descriptors operate on small patches of the image around the detected points or regions, and compute a signature or a vector that represents the local appearance, shape, texture, or gradient of the patch.
  - Global feature descriptors operate on the whole image or large regions of the image, and compute a signature or a vector that represents the global characteristics, statistics, or distribution of the image or region.
- Some examples of local feature descriptors are:
  - Scale-Invariant Feature Transform (SIFT): SIFT detects keypoints that are invariant to scale and orientation changes, and describes them using histograms of gradient orientations in a 16x16 neighborhood around each keypoint.
  - Speeded-Up Robust Features (SURF): SURF is similar to SIFT, but uses integral images and Haar wavelets to speed up the detection and description of keypoints.
  - Histogram of Oriented Gradients (HOG): HOG divides the image into small cells, and computes histograms of gradient orientations for each cell. The histograms are then concatenated to form a feature vector for the image or region.
- Some examples of global feature descriptors are:
  - Color Histogram: Color histogram counts the number of pixels in each color bin for the image or region, and forms a feature vector that represents the color distribution.
  - Texture Features: Texture features measure the spatial variation of pixel intensities in the image or region, and can be computed using methods such as co-occurrence matrix, local binary patterns, Gabor filters, etc.
  - Bag of Visual Words (BoVW): BoVW is a method that quantizes the local feature descriptors of an image or region into a fixed number of clusters, and counts the frequency of each cluster in the image or region. The frequency vector is then used as a feature vector that represents the visual content.
- Some recent methods that improve the regional feature descriptors are:
  - Region-Wise Deep Feature Representation (RDFR): RDFR is a method that uses a convolutional neural network (CNN) to extract deep features from different regions of the image, and then encodes them using an improved Vector of Locally Aggregated Descriptors (VLAD) algorithm. The encoded features are then concatenated to form a feature vector for the image or region .
  - Fisher Vector (FV): FV is a method that encodes the local feature descriptors of an image or region using a Gaussian mixture model (GMM), and computes the gradient of the log-likelihood of the descriptors with respect to the GMM parameters. The gradient vector is then used as a feature vector that represents the visual content.



### Some Basic Descriptors for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Feature extraction is the process of transforming an image into a set of numerical values that represent its characteristics, such as shape, color, texture, etc.
- Feature extraction can be used for various purposes, such as image classification, segmentation, retrieval, recognition, etc.
- Some basic descriptors that can be used to extract features from images are:

  - **Histograms**: A histogram is a graphical representation of the distribution of pixel values in an image. It can be used to capture the global color or intensity information of an image. A histogram can be computed for each color channel (red, green, blue) or for a single grayscale channel. A histogram can also be normalized to account for different image sizes or contrast levels.
  - **Moments**: Moments are statistical measures that describe the shape and orientation of an image region. They can be computed from the pixel values or from the binary contour of the region. Moments can be classified into geometric moments, central moments, normalized central moments, and Hu moments. Geometric moments are invariant to translation, central moments are invariant to translation and rotation, normalized central moments are invariant to translation, rotation, and scaling, and Hu moments are invariant to translation, rotation, scaling, and reflection.
  - **Fourier descriptors**: Fourier descriptors are based on the Fourier transform, which converts an image from the spatial domain to the frequency domain. Fourier descriptors can be used to describe the shape of an image region by computing the Fourier transform of its boundary. Fourier descriptors are invariant to translation and rotation, and can be made invariant to scaling by normalizing the magnitude of the coefficients. Fourier descriptors can also be used to capture the texture information of an image by computing the Fourier transform of its pixel values.
  - **Haralick features**: Haralick features are based on the gray-level co-occurrence matrix (GLCM), which measures the frequency of occurrence of pairs of pixel values at a given distance and orientation in an image. Haralick features can be used to capture the texture information of an image by computing various statistics from the GLCM, such as contrast, correlation, energy, homogeneity, entropy, etc. Haralick features can be computed for different distances and orientations to capture the spatial variations of texture in an image.



### Topological and Texture Descriptors

- Topological and texture descriptors are methods to extract and represent the structural and statistical properties of an image or a region of interest.
- Topological descriptors capture the shape, connectivity, and complexity of an image, such as the number of components, holes, boundaries, and their relations.
- Texture descriptors capture the spatial distribution, orientation, and frequency of pixel intensities or patterns, such as the contrast, smoothness, coarseness, and directionality of an image.
- Topological and texture descriptors can be used for various applications, such as image quality assessment, image segmentation, image classification, object detection, and image forensics.
- Some examples of topological and texture descriptors are:

  - Local Binary Pattern (LBP): A texture descriptor that encodes the local differences of pixel intensities into binary codes, and computes a histogram of the codes as the feature vector  .
  - Topological Attribute Pattern (TAP): A texture descriptor that extends LBP by computing a family of numerical attributes on the original LBP, such as the number of transitions, the number of bits, and the gray level difference, and concatenates them as the feature vector.
  - Topological Textural Multifractal Descriptor (TTMD): A texture descriptor that combines the concepts of multifractals and topological data analysis to estimate the fractal properties of a texture, such as the fractal dimension, the singularity spectrum, and the persistence diagram, and uses them as the feature vector.
  - Persistent Homology (PH): A topological descriptor that computes the homology groups of an image, which represent the number of connected components, holes, and voids at different scales, and summarizes them into a persistence diagram or a persistence barcode as the feature vector .



### Moment Invariants for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Moment invariants are numerical values that are derived from the moments of an image and are invariant to certain geometric transformations, such as translation, scaling and rotation  .
- Moment invariants are useful for image analysis and pattern recognition, as they can capture the shape and appearance of an object regardless of its position, size and orientation  .
- Moment invariants can be computed from different types of moments, such as geometric moments, central moments, normalized central moments, Zernike moments, Legendre moments, etc .
- One of the most widely used sets of moment invariants was proposed by Hu in 1962, which consists of seven invariant values derived from the second and third order central moments of an image  .
- Hu's moment invariants are defined as follows:

  - I1 = η20 + η02
  - I2 = (η20 - η02)^2 + 4η11^2
  - I3 = (η30 - 3η12)^2 + (3η21 - η03)^2
  - I4 = (η30 + η12)^2 + (η21 + η03)^2
  - I5 = (η30 - 3η12)(η30 + η12)[(η30 + η12)^2 - 3(η21 + η03)^2] + (3η21 - η03)(η21 + η03)[3(η30 + η12)^2 - (η21 + η03)^2]
  - I6 = (η20 - η02)[(η30 + η12)^2 - (η21 + η03)^2] + 4η11(η30 + η12)(η21 + η03)
  - I7 = (3η21 - η03)(η30 + η12)[(η30 + η12)^2 - 3(η21 + η03)^2] - (η30 - 3η12)(η21 + η03)[3(η30 + η12)^2 - (η21 + η03)^2]

  where ηij are the normalized central moments of the image, defined as:

  - ηij = μij / μ00^(1 + (i + j) / 2)

  and μij are the central moments of the image, defined as:

  - μij = ∑x∑y (x - x̄)^i (y - ȳ)^j f(x, y)

  where f(x, y) is the pixel intensity at (x, y), x̄ and ȳ are the coordinates of the centroid of the image, and μ00 is the area of the image.

- Hu's moment invariants are theoretically invariant to translation, scaling and rotation of the image, but in practice they may vary slightly due to the discretization and quantization of the image pixels .
- To minimize the fluctuation of moment invariants, some factors should be considered, such as the image resolution, the image size, the image centering, the image normalization, the image noise, the moment order, the moment type, etc .
- Moment invariants can be used as features for image classification, recognition, retrieval, segmentation, registration, etc, by comparing the similarity or distance between the moment invariants of different images  .



### Principal Components as Feature Descriptors

- Principal components are linear combinations of the original features that capture the maximum variance in the data.
- Principal components can be used as feature descriptors to reduce the dimensionality of the data and improve the efficiency and accuracy of matching algorithms.
- Principal components can be obtained by applying principal component analysis (PCA) to the data matrix, which involves finding the eigenvectors and eigenvalues of the covariance matrix.
- The eigenvectors represent the directions of the principal components, while the eigenvalues represent the amount of variance explained by each component.
- The principal components are ranked by their eigenvalues, and the first k components are chosen to form a new feature space, where k is a parameter that depends on the desired level of information preservation.
- The original features can be projected onto the new feature space by multiplying the data matrix by the matrix of the first k eigenvectors.
- Principal components can be used as feature descriptors for various types of data, such as images, text, audio, etc.
- For example, in image processing, principal components can be used to boost the performance of local feature descriptors, such as SIFT, by reducing their dimensionality and noise.
- Principal components can also be used to extract global features from images, such as shape, color, texture, etc., by applying PCA to the pixel values or histograms of the images.
- Principal components can be implemented in Python using the scikit-learn library, which provides a PCA class that can fit and transform the data matrix.
- Principal components can be visualized by plotting the projected data points or the eigenvectors on a scatter plot or a biplot.
- Principal components can be evaluated by measuring the explained variance ratio, which is the fraction of the total variance that is explained by each component.
- Principal components can also be compared with other feature selection methods, such as correlation-based or information-based methods, which select a subset of the original features based on their relevance to the target variable.



### Whole-image Features Object

- A whole-image features object is an object that is represented by a set of features that describe the image as a whole, rather than by local features that describe specific regions or elements in the image.
- Whole-image features can be used to generalize the overall appearance, shape, texture, or color of an object, and to compare different objects based on their global similarities or differences.
- Some examples of whole-image features are:
  - Contour representations: These are features that capture the outline or boundary of an object, and can be used to measure the shape or size of the object. Contour representations can be obtained by applying edge detection or segmentation algorithms to the image, and then extracting the coordinates or parameters of the resulting curves.
  - Shape descriptors: These are features that quantify the shape of an object, and can be used to classify or recognize objects based on their shape. Shape descriptors can be computed from the contour representations, or from other methods such as moments, Fourier descriptors, or shape context.
  - Texture features: These are features that characterize the surface properties or patterns of an object, and can be used to distinguish objects based on their texture. Texture features can be derived from the pixel intensity values, or from other methods such as co-occurrence matrices, local binary patterns, or wavelet transforms.
- Whole-image features can be combined into a feature vector, which is a numerical representation of the object that can be used for further analysis or processing. A feature vector can be composed of different types of features, such as color, shape, and texture features, to capture the various aspects of the object.
- Whole-image features can be used for various applications in image analytics, such as image classification, object detection, object recognition, image retrieval, or image similarity . For example, with an image classification model, one can use whole-image features to assign a label to an image based on its content, such as animal, plant, or vehicle. With an object detection model, one can use whole-image features to locate and identify multiple objects in an image, such as cars, pedestrians, or traffic signs.



### Scale-Invariant Feature Transform (SIFT) for the notes of the Unit 4 - Feature Extraction in the subject of IMAGE ANALYTICS

- Scale-Invariant Feature Transform (SIFT) is a computer vision algorithm to detect, describe, and match local features in images.
- Local features are distinctive points or regions in an image that can be used to identify or compare images, such as corners, edges, blobs, etc.
- SIFT is invariant to scale and orientation of images and robust to illumination fluctuations, noise, partial occlusion, and minor viewpoint changes in the images .
- SIFT can be used for various applications, such as object recognition, image stitching, 3D modeling, video tracking, etc.
- SIFT consists of four main steps :
  - Scale-space extrema detection: This step finds potential interest points in the image by applying a Difference of Gaussians (DoG) filter to different scales and octaves of the image and looking for local maxima and minima.
  - Keypoint localization: This step refines the location and scale of each candidate point by fitting a 3D quadratic function to the DoG values and discarding low-contrast or edge-like points.
  - Orientation assignment: This step assigns one or more orientations to each keypoint based on the gradient magnitude and direction of a local neighborhood around the keypoint. This ensures that the keypoint descriptor is rotation-invariant.
  - Keypoint descriptor: This step computes a 128-dimensional vector for each keypoint based on the gradient magnitude and orientation of a 16x16 region around the keypoint. The vector is normalized and thresholded to enhance contrast and reduce the effects of illumination changes.
- SIFT keypoints and descriptors can be matched between different images using a nearest-neighbor or a ratio test to find the best matches .
- SIFT is a powerful and popular feature extraction method, but it also has some limitations, such as high computational cost, sensitivity to blur and non-affine distortions, and patent issues .



## Unit 5 - Image Pattern Classification

- Image pattern classification is the task of assigning a label to an image based on its content, such as objects, scenes, faces, etc.
- Image pattern classification can be done using different methods, such as:
  - Handcrafted features: extracting low-level or high-level features from the image using predefined algorithms, such as edge detection, color histograms, texture descriptors, etc. and then using a classifier, such as k-nearest neighbors, support vector machines, decision trees, etc. to assign a label to the image based on the features.
  - Deep learning: using a neural network, such as a convolutional neural network, to learn features and classifiers from the image data directly, without requiring any manual feature engineering. The neural network consists of multiple layers of neurons that perform nonlinear transformations on the input image and output a probability distribution over the possible labels.
- Image pattern classification can be applied to various domains, such as:
  - Face recognition: identifying or verifying the identity of a person from their face image, such as for security, biometrics, social media, etc.
  - Scene recognition: recognizing the type of scene or environment from an image, such as indoor, outdoor, urban, natural, etc.
  - Object recognition: recognizing the type or category of an object from an image, such as animals, vehicles, furniture, etc.
  - Image retrieval: finding images that are similar or relevant to a given query image, such as for search engines, e-commerce, etc.
  - Image captioning: generating a natural language description of the content of an image, such as for accessibility, summarization, etc.



### Background for the notes of the Unit 5 - Image Pattern Classification in the subject of IMAGE ANALYTICS

- Image pattern classification is the process of assigning a label to an image based on the content or features of the image.
- Image pattern classification can be used for various applications, such as face recognition, medical diagnosis, object detection, scene understanding, etc.
- Image pattern classification can be performed using different methods, such as template matching, feature extraction, machine learning, deep learning, etc.
- Template matching is a simple method that compares an image with a set of predefined templates and selects the best match based on some similarity measure.
- Feature extraction is a method that transforms an image into a vector of numerical values that represent some characteristics or properties of the image, such as color, texture, shape, etc.
- Machine learning is a method that learns a function or a model that maps the features of an image to a label, based on a set of labeled training images.
- Deep learning is a subset of machine learning that uses multiple layers of artificial neural networks to learn complex and nonlinear patterns from the images.
- Image pattern classification can be challenging due to various factors, such as noise, occlusion, illumination, pose, scale, rotation, etc. that can affect the appearance and representation of the images.
- Image pattern classification can be evaluated using different metrics, such as accuracy, precision, recall, F1-score, confusion matrix, ROC curve, etc. that measure the performance of the classifier on a test set of images.



### Patterns and Pattern Classes

- A pattern is an arrangement of descriptors, which are numerical or symbolic values that characterize an object or an image.
- A feature is another name for a descriptor, which can be extracted from the raw data of an image, such as pixel values, colors, shapes, textures, etc .
- A pattern class is a family of patterns that share some common properties, such as belonging to the same category, having the same label, or satisfying some criteria.
- Pattern classification is the process of assigning a class to a pattern based on its features and some rules or criteria .
- Pattern classification can be used for various applications, such as object detection, face recognition, biometric authentication, medical diagnosis, etc   .
- Pattern classification can be performed using different techniques, such as statistical, syntactic, structural, or subsymbolic methods .
- Statistical methods use probabilistic models and decision boundaries to classify patterns based on their feature distributions .
- Syntactic methods use grammars and rules to describe the structure and composition of patterns based on their features.
- Structural methods use graphs and trees to represent the relationships and dependencies among the features of patterns.
- Subsymbolic methods use artificial neural networks and fuzzy logic to learn the patterns and their classes from the data without explicit rules .



### Pattern Classification by Prototype Matching

- Prototype matching is a theory of pattern recognition that describes the process by which a sensory unit registers a new stimulus and compares it to a stored prototype, or standard model, of said stimulus.
- A prototype is a kind of average of many other patterns that belong to the same category .
- Unlike template matching and featural analysis, an exact match is not expected for prototype matching, allowing for a more flexible and generalizable recognition of patterns.
- Prototype matching can be used for image pattern classification by assigning a label to an image based on the similarity of its features to the features of the prototype of each class.
- Prototype matching can be implemented using various methods, such as nearest neighbor, k-means clustering, or neural networks.
- Prototype matching has some advantages over other methods, such as being able to handle noise, distortion, and variation in the input patterns, and being able to learn from experience and update the prototypes accordingly.
- Prototype matching also has some limitations, such as being sensitive to the choice of prototypes, requiring a large amount of storage and computation, and being unable to capture the structural or relational aspects of the patterns.



### Minimum-Distance Classifier

- A minimum-distance classifier is a supervised image classification technique that assigns an unknown image pixel to the class that has the closest mean value in the feature space .
- The distance between the pixel value and the class mean value can be measured by different metrics, such as Euclidean distance, Mahalanobis distance, or spectral angle mapper .
- The minimum-distance classifier is simple and fast, but it assumes that the classes have equal variance and covariance, which may not be true in reality .
- The minimum-distance classifier can be improved by using weighted distances, adaptive distances, or fuzzy distances .
- The minimum-distance classifier can be applied to various image pattern recognition tasks, such as land cover classification, face recognition, or object detection  .



### Using Correlation for 2-D Prototype Matching

- Correlation is a measure of similarity between two signals or images.
- Correlation can be used for pattern matching, which is the process of finding a specific pattern or template in a larger image or signal.
- Correlation can be performed in the spatial domain or the frequency domain, depending on the application and the computational efficiency.
- 2-D correlation involves sliding a smaller template image over a larger input image and computing the correlation coefficient at each position.
- The correlation coefficient is a value between -1 and 1 that indicates how well the template matches the input image at that position.
- A high correlation coefficient means a good match, while a low correlation coefficient means a poor match.
- The correlation coefficient can be normalized to account for variations in the intensity and contrast of the images.
- Normalized cross-correlation is a common method for 2-D correlation that uses the mean and standard deviation of the template and the input image to normalize the correlation coefficient.
- Normalized cross-correlation can be used for target tracking, which is the process of locating and following a specific object or feature in a sequence of images.
- Target tracking can be done by defining a target region in the first image and then finding the region with the highest normalized cross-correlation in the subsequent images.
- The target region can be predefined or user specified, depending on the application and the user preference.
- The target region can also be updated dynamically to account for changes in the appearance or orientation of the target.
- The normalized cross-correlation plot shows the correlation coefficient at each position of the input image, and the peak value indicates the best match for the target region.
- The normalized cross-correlation plot can be thresholded to identify the positions that exceed a certain similarity level, and these positions can be marked as potential matches for the target region.
- The threshold value can be adjusted to control the sensitivity and specificity of the pattern matching and target tracking.



### Matching SIFT Features

- SIFT (Scale-Invariant Feature Transform) is a computer vision algorithm to detect, describe, and match local features in images.
- SIFT features are invariant to rotation, scale, and brightness changes, and are stable to some extent to perspective and affine transformations .
- SIFT features can be used for various applications, such as image stitching, object recognition, scene detection, etc.
- SIFT feature matching is the process of finding the correspondences between two sets of SIFT features extracted from two images.
- SIFT feature matching can be done by using different methods, such as brute-force matching, FLANN (Fast Library for Approximate Nearest Neighbors) matching, or RANSAC (Random Sample Consensus) matching .
- Brute-force matching is the simplest method, which compares each feature in one set with all the features in the other set and finds the best match based on some distance metric, such as Euclidean distance or Hamming distance.
- FLANN matching is a faster and more efficient method, which uses a hierarchical data structure and a randomized algorithm to find the approximate nearest neighbors for each feature in one set among the features in the other set .
- RANSAC matching is a robust method, which uses a probabilistic approach to find a subset of inliers among the matches that agree with a geometric model, such as a homography or a fundamental matrix, and discards the outliers that do not fit the model.
- SIFT feature matching can be improved by using some criteria, such as the ratio test, the symmetry test, or the cross-check test, to filter out the false or ambiguous matches .
- The ratio test, proposed by D.Lowe, compares the distance of the best match with the distance of the second best match for each feature, and rejects the match if the ratio is greater than a threshold, typically 0.8 .
- The symmetry test, proposed by Mikolajczyk and Schmid, checks if the best match for a feature in one set is also the best match for the corresponding feature in the other set, and rejects the match if it is not symmetric.
- The cross-check test, implemented in OpenCV, is similar to the symmetry test, but it only checks if the best match for a feature in one set is the same as the best match for the corresponding feature in the other set, and rejects the match if it is not consistent.



### Matching Structural Prototypes

- Matching structural prototypes is a technique for image pattern classification that involves comparing an unknown pattern with a set of known prototypes that represent different classes.
- A prototype is a sub-image or a graph that captures the essential features of a class .
- Matching structural prototypes can be done by using template matching or graph matching methods  .
- Template matching is a technique that finds the best match between a template image and a target image by using a similarity measure, such as cross-correlation or sum of squared differences .
- Graph matching is a technique that finds the best match between a graph representation of a pattern and a graph representation of a prototype by using a cost function, such as edit distance or maximum common subgraph .
- Matching structural prototypes can be used for various applications, such as object detection, edge detection, quality control, and medical imaging  .
- Matching structural prototypes can also be improved by using adversarial learning methods, such as adversarial structure matching, which can generate realistic and diverse prototypes that can better capture the variations of a class.
- Matching structural prototypes is a form of syntactic pattern recognition, which uses a description of the pattern structure to recognize entities when a simple classification is not possible.



### Optimum (Bayes) Statistical Classifiers

- Optimum (Bayes) statistical classifiers are classifiers that use the Bayes' theorem to make predictions based on the posterior probabilities of the classes given the features of a new example .
- The Bayes' theorem states that the posterior probability of a class C given a feature vector x is proportional to the product of the prior probability of the class P(C) and the likelihood of the feature vector given the class P(x|C):
  - P(C|x) ∝ P(C)P(x|C)
- The optimum (Bayes) classifier chooses the class that has the highest posterior probability for a given feature vector, i.e., the class that maximizes P(C|x). This is also known as the maximum a posteriori (MAP) estimation.
  - C* = argmax P(C|x)
- The optimum (Bayes) classifier is also called the Bayes optimal classifier, the Bayes optimal learner, the Bayes optimal decision boundary, or the Bayes optimal discriminant function .
- The optimum (Bayes) classifier is a theoretical model that assumes the true probabilities of the classes and the features are known or can be estimated from the training data. In practice, this is often not the case, and various approximation methods are used to implement the Bayes classifier, such as the naive Bayes classifier, the linear discriminant analysis, the quadratic discriminant analysis, etc .
- The optimum (Bayes) classifier is a useful benchmark for evaluating the performance of other classification methods, as it represents the lowest possible error rate that can be achieved for a given problem. The difference between the error rate of the optimum (Bayes) classifier and the error rate of another classifier is called the excess risk.



### Neural Networks and Deep Learning for Image Pattern Classification

- Image pattern classification is the task of assigning a label to an image based on its content, such as objects, scenes, faces, etc.
- Neural networks are computational models that mimic the structure and function of biological neurons, which can learn from data and perform complex tasks.
- Deep learning is a branch of machine learning that uses multiple layers of neural networks to extract high-level features and representations from raw data, such as images, text, speech, etc.
- Convolutional neural networks (CNNs) are a type of deep neural networks that are specially designed for image processing and recognition. They consist of three main types of layers: convolutional, pooling, and fully connected.
  - Convolutional layers apply a set of filters to the input image, which produce feature maps that capture local patterns and edges.
  - Pooling layers reduce the size and dimensionality of the feature maps, which makes the network more efficient and invariant to small translations.
  - Fully connected layers connect every neuron in the previous layer to every neuron in the next layer, which perform the final classification or regression task.
- CNNs can be trained using supervised learning, where the network learns from a large set of labeled images, or using unsupervised learning, where the network learns from unlabeled images by discovering latent structures and patterns.
- CNNs can also be trained using transfer learning, where the network leverages the knowledge learned from a pre-trained model on a different but related task, such as ImageNet, and fine-tunes it on a new task, such as face recognition.
- CNNs have achieved state-of-the-art results on various image classification tasks, such as object recognition, scene classification, face detection, etc. They have also been extended and combined with other deep learning techniques, such as transformers, attention mechanisms, generative adversarial networks, etc. to handle more challenging and diverse problems, such as image captioning, style transfer, image synthesis, etc.



### Background for the notes of the Unit 5 - Image Pattern Classification in the subject of IMAGE ANALYTICS

- Image pattern classification is the task of categorizing images into one or multiple predefined classes based on their content, such as objects, scenes, textures, etc.
- Image pattern classification is a subfield of computer vision and machine learning that deals with the automatic recognition and understanding of visual information.
- Image pattern classification has many applications in various domains, such as face recognition, medical imaging, biometrics, remote sensing, security, etc.
- Image pattern classification can be performed using different methods, such as supervised, unsupervised, or semi-supervised learning.
- Supervised learning is the process of learning from labeled data, where each image is associated with a class label. The goal is to learn a function that maps an image to its correct label.
- Unsupervised learning is the process of learning from unlabeled data, where the class labels are unknown. The goal is to discover the underlying structure or patterns in the data, such as clusters or groups of similar images.
- Semi-supervised learning is the process of learning from partially labeled data, where some images have class labels and some do not. The goal is to leverage the labeled data to improve the performance of unsupervised learning.
- An image pattern classification system generally consists of four parts: a camera that acquires the image samples to be classified, an image preprocessor that improves the qualities of images, a feature extraction mechanism that gains discriminative features from images for recognition, and a classification scheme that classifies the image samples based on the extracted features.
- The image preprocessor can perform various operations on the images, such as noise reduction, contrast enhancement, color conversion, etc.
- The feature extraction mechanism can use different techniques to extract features from images, such as pixel values, histograms, edges, textures, shapes, etc. 
- The classification scheme can use different algorithms to assign class labels to images, such as k-nearest neighbors, support vector machines, decision trees, neural networks, etc. 
- Image pattern classification can be evaluated using different metrics, such as accuracy, precision, recall, F1-score, confusion matrix, etc.
- Image pattern classification is a challenging and active research area, as it involves dealing with various issues, such as image variability, occlusion, illumination, scale, rotation, etc. 
- Image pattern classification can be improved using various techniques, such as data augmentation, feature selection, dimensionality reduction, ensemble methods, etc.
- Image pattern classification can also benefit from the recent advances in deep learning, such as convolutional neural networks, which can learn hierarchical and robust features from raw images and achieve state-of-the-art performance on many image classification tasks.



### The Perceptron

- The perceptron is a simple and powerful model of artificial neural networks that can perform binary classification tasks.
- The perceptron consists of a single node or neuron that takes a vector of inputs, applies a linear transformation, and outputs a binary value (0 or 1) based on a threshold function.
- The perceptron can be represented by the following equation:

Perceptron equation

where:

  - y is the output of the perceptron
  - f is the threshold function, such as the Heaviside step function
  - w is the weight vector
  - x is the input vector
  - b is the bias term

- The perceptron can be trained using the perceptron learning rule, which updates the weights and bias based on the prediction error and the learning rate.
- The perceptron learning rule can be expressed as:

Perceptron learning rule

where:

  - w_t is the weight vector at time t
  - w_t+1 is the weight vector at time t+1
  - alpha is the learning rate
  - y_t is the true output at time t
  - y_hat_t is the predicted output at time t
  - x_t is the input vector at time t

- The perceptron learning rule can be proven to converge to a solution that separates the data linearly, if such a solution exists, under some assumptions.
- The perceptron can be extended to handle multiple classes by using multiple output neurons, each representing a class, and applying a softmax function to the outputs.
- The perceptron can also be generalized to handle nonlinearly separable data by using a nonlinear activation function, such as the sigmoid or the tanh function, instead of the threshold function.
- The perceptron is the building block of more complex neural network architectures, such as the multilayer perceptron, that can perform more advanced tasks, such as image pattern recognition.



### Multilayer Feedforward Neural Networks

- A multilayer feedforward neural network is an interconnection of perceptrons in which data and calculations flow in a single direction, from the input data to the outputs.
- The number of layers in a neural network is the number of layers of perceptrons. The simplest neural network is one with a single input layer and an output layer of perceptrons.
- A multilayer feedforward neural network can have one or more hidden layers between the input and output layers. The hidden layers can extract features from the input data and transform them into a higher-level representation.
- A multilayer feedforward neural network for classifying patterns into one of only two categories is referred to as a binary classification network. It has a single output: the estimated probability that the input pattern belongs to one of the two categories.
- A multilayer feedforward neural network for classifying patterns into more than two categories is referred to as a multiclass classification network. It has as many outputs as the number of categories, and each output represents the estimated probability that the input pattern belongs to that category.
- A multilayer feedforward neural network can also be used for regression tasks, where the output is a continuous value rather than a discrete category.
- A multilayer feedforward neural network is also known as a multilayer perceptron (MLP) or a backpropagation network.
- A multilayer feedforward neural network learns from data by adjusting the weights and biases of the perceptrons using a learning algorithm, such as gradient descent or stochastic gradient descent.
- A multilayer feedforward neural network uses an activation function to introduce nonlinearity into the network, which allows it to model complex functions and patterns.
- A common activation function for multilayer feedforward neural networks is the sigmoid function, which maps any input to a value between 0 and 1.
- Another common activation function for multilayer feedforward neural networks is the rectified linear unit (ReLU) function, which maps any negative input to 0 and any positive input to itself.
- A multilayer feedforward neural network can be trained using a supervised learning method, where the network is given input-output pairs and learns to minimize the error between the predicted output and the actual output.
- A multilayer feedforward neural network can also be trained using an unsupervised learning method, where the network is given only input data and learns to extract features or patterns from the data without any labels.
- A multilayer feedforward neural network can be used for image pattern classification by taking an image as an input and producing an output that indicates the class or category of the image.
- A multilayer feedforward neural network can also be used for image segmentation, where the network divides an image into regions that correspond to different objects or parts of the image.
- A multilayer feedforward neural network can also be used for image generation, where the network produces an image that resembles the input data or satisfies some criteria.
- A multilayer feedforward neural network can also be used for image enhancement, where the network improves the quality or appearance of an image by removing noise, increasing contrast, or adding details.
- A multilayer feedforward neural network can also be used for image recognition, where the network identifies the objects or faces in an image and labels them with names or attributes.
- A multilayer feedforward neural network can also be used for image captioning, where the network generates a natural language description of the content or context of an image.
- A multilayer feedforward neural network can also be used for image style transfer, where the network transfers the style or artistic features of one image to another image while preserving the content or structure of the original image.



### Deep Convolutional Neural Networks for Image Pattern Classification

- Deep convolutional neural networks (DCNNs) are a class of deep learning models that can learn from image samples and extract features for image pattern classification .
- DCNNs consist of multiple layers of nonlinear processing units that perform convolution, pooling, activation, and normalization operations on the input image .
- Convolution is a mathematical operation that applies a filter (also called a kernel) to the input image, producing a feature map that captures the presence of certain patterns in the image .
- Pooling is a downsampling operation that reduces the size of the feature map by applying a function (such as max or average) to a local region of the feature map .
- Activation is a nonlinear function that introduces nonlinearity to the network and allows it to learn complex patterns .
- Normalization is a technique that adjusts the values of the feature map to improve the stability and performance of the network .
- DCNNs can have multiple convolutional layers, each with different filters, followed by pooling layers, activation layers, and normalization layers  .
- The final layer of a DCNN is usually a fully connected layer that performs the classification task based on the features extracted by the previous layers  .
- DCNNs can achieve high accuracy and robustness in image pattern classification tasks, such as object detection, face recognition, scene understanding, and image segmentation     .
- DCNNs can also be visualized by computing the gradient of the class score with respect to the input image, which reveals the regions of the image that contribute most to the classification decision.

