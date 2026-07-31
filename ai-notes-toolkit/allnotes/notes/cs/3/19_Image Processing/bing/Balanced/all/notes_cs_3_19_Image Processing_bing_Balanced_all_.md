

## Unit 1 - DIGITAL IMAGE FUNDAMENTALS

- A digital image is a representation of a two-dimensional image as a finite set of digital values, called pixels or picture elements.
- Each pixel has a numeric value that corresponds to its brightness, color, or intensity.
- The size of a digital image is determined by the number of pixels along its rows and columns, also known as its resolution.
- The number of possible values for each pixel is called the bit depth or color depth of the image. The higher the bit depth, the more colors or shades of gray can be represented.
- A digital image can be classified into two types: binary and grayscale. A binary image has only two possible values for each pixel: 0 or 1, representing black or white. A grayscale image has more than two values, usually ranging from 0 to 255, representing different shades of gray.
- A digital image can also be represented in different color models, such as RGB, CMYK, HSV, or YCbCr. Each color model has a different way of encoding the color information of each pixel, using different components or channels.
- A digital image can be processed by various techniques, such as enhancement, restoration, segmentation, compression, or recognition. Each technique has a different goal and method of manipulating the pixel values of the image.



# Steps in Digital Image Processing

Digital image processing is the process of manipulating digital images using various techniques and algorithms. It can be used for various purposes, such as enhancing, restoring, compressing, segmenting, and recognizing images.

The basic steps involved in digital image processing are:

- **Image acquisition**: This involves capturing an image using a digital camera or scanner, or importing an existing image into a computer. The image is then converted into a digital form, using analog-to-digital converters, if necessary. The image may also be pre-processed, such as cropping, resizing, or filtering, to prepare it for further processing.   
- **Image enhancement**: This involves improving the visual quality of an image, such as increasing contrast, reducing noise, and removing artifacts. The goal of image enhancement is to make the image more suitable for a specific application or task, such as human perception, analysis, or interpretation. Image enhancement techniques can be classified into spatial domain methods, which operate directly on the pixels of the image, and frequency domain methods, which transform the image into a different domain, such as Fourier or wavelet, and manipulate the coefficients.  
- **Image restoration**: This involves removing degradation from an image, such as blurring, noise, and distortion. The goal of image restoration is to recover the original image from the degraded image, as closely as possible. Image restoration techniques can be classified into inverse filtering, which assumes a known degradation model and tries to invert it, and iterative methods, which use optimization algorithms to minimize a cost function that measures the difference between the original and the degraded image.  
- **Image compression**: This involves reducing the size of an image, while maintaining its quality and information content. The goal of image compression is to save storage space and transmission bandwidth, and to speed up processing and transmission. Image compression techniques can be classified into lossless methods, which preserve the exact pixel values of the image, and lossy methods, which allow some distortion or loss of information in exchange for higher compression ratios. Some common image compression methods are run-length encoding, Huffman coding, JPEG, and JPEG 2000. 
- **Image segmentation**: This involves dividing an image into meaningful regions or objects, based on some criteria, such as color, intensity, texture, or shape. The goal of image segmentation is to simplify or change the representation of an image, so that it is easier to analyze or understand. Image segmentation techniques can be classified into thresholding, which separates the image into foreground and background based on a threshold value, edge-based methods, which detect the boundaries of the regions or objects, region-based methods, which group the pixels based on their similarity or proximity, and clustering methods, which partition the image into clusters based on some features or distance measures. 
- **Image representation and description**: This involves extracting features or attributes from the segmented image, such as shape, size, color, texture, or orientation. The goal of image representation and description is to represent the image in a compact and meaningful way, that can be used for further processing, such as recognition, classification, or retrieval. Image representation and description techniques can be classified into boundary-based methods, which use the contours or edges of the regions or objects, and region-based methods, which use the properties or statistics of the regions or objects. 
- **Image recognition and interpretation**: This involves assigning labels or meanings to the regions or objects in the image, based on their features or attributes. The goal of image recognition and interpretation is to understand the content and context of the image, and to perform tasks such as identification, classification, or retrieval. Image recognition and interpretation techniques can be classified into template matching, which compares the image with a set of predefined templates, feature-based methods, which use the features or attributes of the image, and machine learning methods, which use algorithms that learn from data, such as neural networks, support vector machines, or deep learning.



# Components for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- **Elements of digital image processing systems**: A digital image processing system consists of the following components:
  - **Image acquisition device**: This is the device that captures or generates the image, such as a camera, a scanner, a microscope, etc. The image acquisition device converts the analog signal (light, sound, etc.) into a digital signal (a sequence of numbers) that can be stored and processed by a computer.
  - **Image storage device**: This is the device that stores the digital image, such as a hard disk, a flash drive, a CD-ROM, etc. The image storage device allows the image to be retrieved and modified later.
  - **Image processing unit**: This is the device that performs the operations and transformations on the digital image, such as filtering, enhancement, segmentation, compression, etc. The image processing unit can be a software program, a hardware device, or a combination of both.
  - **Image display device**: This is the device that shows the digital image to the user, such as a monitor, a printer, a projector, etc. The image display device converts the digital signal back into an analog signal that can be perceived by the human eye or other sensors.
  - **Image communication device**: This is the device that transmits or receives the digital image from another location, such as a modem, a network card, a wireless device, etc. The image communication device enables the image to be shared and distributed across different platforms and devices.

- **Elements of a digital image**: A digital image is a representation of a two-dimensional scene using a finite number of discrete values, called pixels or picture elements. Each pixel has a spatial location (row and column) and an intensity value (gray level or color). A digital image can be characterized by the following elements:
  - **Resolution**: This is the number of pixels in the image, usually expressed as width x height. The resolution determines the amount of detail and information that can be captured and displayed by the image. Higher resolution means more pixels and more detail, but also more storage space and processing time.
  - **Bit depth**: This is the number of bits used to represent the intensity value of each pixel, usually expressed as bits per pixel (bpp). The bit depth determines the range and precision of the intensity values that can be represented by the image. Higher bit depth means more intensity levels and more contrast, but also more storage space and processing time.
  - **Color model**: This is the way of representing the color information of each pixel, using a combination of primary colors or color components. The most common color models are RGB (red, green, blue), CMYK (cyan, magenta, yellow, black), HSV (hue, saturation, value), and YCbCr (luminance, blue chrominance, red chrominance). The color model determines the appearance and perception of the image, as well as the compatibility and conversion between different devices and formats.

- **Image sampling and quantization**: Image sampling is the process of converting a continuous image (analog signal) into a discrete image (digital signal) by dividing the image into a grid of pixels and assigning an intensity value to each pixel. Image quantization is the process of reducing the number of intensity levels of each pixel by rounding or truncating the intensity values to a finite set of discrete values. Image sampling and quantization are necessary for storing and processing digital images, but they also introduce errors and distortions, such as aliasing, quantization noise, and loss of information. Image sampling and quantization can be controlled by adjusting the resolution and bit depth of the image, as well as applying filters and compression techniques.



# Elements of Visual Perception

Visual perception is the process of interpreting and understanding the visual information received by the eyes. It involves various elements that affect how humans perceive and process images. Some of the elements of visual perception are:

- **Structure of the eye**: The eye is the organ that captures light and converts it into electrical signals that are sent to the brain. The eye consists of several parts, such as the cornea, the iris, the pupil, the lens, the retina, the optic nerve, and the fovea. The cornea is the transparent outer layer that protects the eye and refracts light. The iris is the colored part of the eye that controls the size of the pupil, which is the opening that allows light to enter the eye. The lens is the flexible structure that focuses light onto the retina, which is the layer of light-sensitive cells at the back of the eye. The retina contains two types of photoreceptors: rods and cones. Rods are responsible for low-light and peripheral vision, while cones are responsible for color and high-resolution vision. The optic nerve is the bundle of nerve fibers that carries the signals from the retina to the brain. The fovea is the central part of the retina that has the highest concentration of cones and provides the sharpest vision.

- **Image formation in the eye**: The image formed on the retina is inverted and reversed from left to right, due to the refraction of light by the cornea and the lens. The brain compensates for this inversion and reversal by processing the signals from the retina and reconstructing the image in the correct orientation and position. The image formed on the retina is also distorted by various factors, such as the curvature of the cornea and the lens, the shape and size of the pupil, the movement of the eye, and the presence of optical defects, such as myopia, hyperopia, astigmatism, and presbyopia. The brain also corrects for these distortions by using prior knowledge, context, and expectations to fill in the gaps and smooth out the edges of the image.

- **Brightness adaptation and discrimination**: Brightness is the subjective perception of the intensity of light, while luminance is the objective measure of the amount of light reflected or emitted by a surface. The eye can adapt to a wide range of luminance levels, from bright sunlight to dim starlight, by adjusting the size of the pupil and the sensitivity of the rods and cones. The eye can also discriminate between different levels of brightness, by comparing the luminance of a region with the luminance of its surroundings. However, the eye's ability to adapt and discriminate is limited by several factors, such as the contrast, the spatial frequency, the temporal frequency, and the color of the stimuli. For example, the eye can perceive a higher contrast when the stimuli have low spatial frequency (large features) and high temporal frequency (fast changes), and when the stimuli have different colors. The eye can also be fooled by various optical illusions, such as the Mach band effect, the simultaneous contrast effect, and the brightness constancy effect, that exploit the eye's adaptation and discrimination mechanisms.



# Image Sensing and Acquisition

- Image sensing and acquisition are used for processing the analog images of physical scenes or the interior structure of an object, and converting it into digital .
- Image sensing is a process to detect or sense the information that constitutes an image .
- Image acquisition includes processing, compression, and finally storing of image into digital form.
- The types of images in which we are interested are generated by the combination of an illumination source and the reflection or absorption of energy from that source by the elements of the scene being imaged.
- The image sensing and acquisition process can be divided into three main steps:
  - Image formation: The interaction of the illumination source and the scene elements, resulting in the generation of an optical image.
  - Image capture: The conversion of the optical image into an electrical signal by a sensor device, such as a camera or a scanner.
  - Image digitization: The sampling and quantization of the electrical signal, resulting in a digital image representation that can be stored and processed by a computer.
- The image sensing and acquisition process can be influenced by various factors, such as the wavelength range of the illumination source, the properties of the scene elements, the characteristics of the sensor device, the resolution and bit depth of the digital image, and the noise and distortion introduced by the environment and the devices.
- The image sensing and acquisition process can be applied to various domains, such as medical imaging, remote sensing, biometrics, security, industrial inspection, and entertainment.
- Image Sensing Systems, Inc. is an example of a company that provides image sensing and acquisition solutions for traffic management, law enforcement, and tolling applications.



# Image Sampling and Quantization

- Image sampling and quantization are two important steps in digital image processing that convert a continuous image into a discrete image.
- Sampling is the process of digitizing the coordinate values (x and y) of the image, while quantization is the process of digitizing the amplitude values (f) of the image.
- Sampling can be done by dividing the image into a grid of pixels, and assigning each pixel a coordinate value based on its position in the grid.
- Quantization can be done by dividing the range of amplitude values into a finite number of levels, and assigning each level a discrete value based on its position in the range.
- The quality of the digital image depends on the sampling rate and the quantization level. A higher sampling rate and a higher quantization level can preserve more details and information of the original image, but also require more storage space and processing time.
- A lower sampling rate and a lower quantization level can reduce the storage space and processing time, but also introduce errors and distortions in the digital image, such as aliasing and quantization noise.



# Relationships between pixels

- A pixel is the smallest unit of a digital image that can be displayed or manipulated.
- Pixels have coordinates that indicate their position in the image, usually starting from the top-left corner as the origin (0,0).
- Pixels have values that represent their intensity or color, depending on the image format and color space.
- Pixels can have different types of relationships with each other, such as adjacency, connectivity, distance, and similarity.
- These relationships are useful for defining and analyzing regions, objects, boundaries, and features in an image.

## Adjacency

- Adjacency is the simplest relationship between pixels, which means that they are next to each other in a certain direction.
- There are three types of adjacency: 4-adjacency, 8-adjacency, and m-adjacency.
- 4-adjacency: Two pixels are 4-adjacent if they share a common side (horizontal or vertical). For example, the pixel p at (x,y) has four 4-neighbors: (x+1,y), (x-1,y), (x,y+1), and (x,y-1).
- 8-adjacency: Two pixels are 8-adjacent if they share a common side or a common vertex (diagonal). For example, the pixel p at (x,y) has eight 8-neighbors: (x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1).
- m-adjacency: Two pixels are m-adjacent if they are 8-adjacent but not 4-adjacent. For example, the pixel p at (x,y) has four m-neighbors: (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1).

## Connectivity

- Connectivity is a more complex relationship between pixels, which means that there is a path between them that consists of pixels with the same property (such as value, color, or region).
- There are two types of connectivity: binary connectivity and grayscale connectivity.
- Binary connectivity: This applies to binary images, where pixels have only two possible values: 0 (background) or 1 (foreground). Two pixels are binary connected if they have the same value and are adjacent in a certain way. For example, two pixels are 4-connected if they are 4-adjacent and have the same value. Similarly, two pixels are 8-connected if they are 8-adjacent and have the same value.
- Grayscale connectivity: This applies to grayscale images, where pixels have a range of values from 0 (black) to 255 (white). Two pixels are grayscale connected if they are adjacent in a certain way and their values are within a specified threshold. For example, two pixels are 4-connected if they are 4-adjacent and their values differ by less than or equal to T, where T is a positive constant. Similarly, two pixels are 8-connected if they are 8-adjacent and their values differ by less than or equal to T.

## Distance

- Distance is a numerical measure of how far apart two pixels are in an image.
- There are different ways to calculate the distance between two pixels, depending on the type of adjacency and the image geometry.
- Some common distance metrics are: Euclidean distance, city-block distance, and chessboard distance.
- Euclidean distance: This is the most natural and intuitive way to measure the distance between two pixels, which is the length of the straight line that connects them. For example, the Euclidean distance between the pixel p at (x,y) and the pixel q at (s,t) is given by: d(p,q) = sqrt((x-s)^2 + (y-t)^2).
- City-block distance: This is also known as Manhattan distance, which is the sum of the horizontal and vertical distances between two pixels. For example, the city-block distance between the pixel p at (x,y) and the pixel q at (s,t) is given by: d(p,q) = |x-s| + |y-t|.
- Chessboard distance: This is also known as Chebyshev distance, which is the maximum of the horizontal and vertical distances between two pixels. For example, the chessboard distance between the pixel p



# Color image fundamentals

- Color is a powerful descriptor that often simplifies object identification and extraction from a scene.
- Color image processing is divided into two major areas: full-color and pseudo-color processing.
- Full-color processing involves the manipulation of color images that have multiple color components, such as RGB (red, green, blue) or CMYK (cyan, magenta, yellow and black) .
- Pseudo-color processing involves the assignment of colors to gray-level images to enhance their visual appearance or highlight certain features.
- Color images can be represented and processed in different color models, which are mathematical frameworks for describing the properties of colors  .
- Some common color models are:
  - RGB: based on a Cartesian coordinate system, where each color is a combination of red, green and blue components . It is widely used for color display devices, such as monitors and cameras.
  - CMY and CMYK: based on subtractive color mixing, where each color is a combination of cyan, magenta and yellow components (and optionally black) . It is widely used for color printing devices, such as printers and scanners.
  - HSI: based on a cylindrical coordinate system, where each color is described by its hue (color tone), saturation (color purity) and intensity (brightness) . It is widely used for color analysis and segmentation, as it separates the chromatic and achromatic information of colors.
- Color image processing involves various techniques and applications, such as:
  - Color transformation: changing the color representation of an image from one model to another, such as RGB to HSI or vice versa .
  - Color enhancement: improving the visual quality or contrast of an image by adjusting its color components, such as brightness, contrast, saturation, etc. .
  - Color segmentation: dividing an image into regions or objects based on their color similarity or difference .
  - Color edge detection: finding the boundaries of regions or objects in an image based on their color discontinuity .
  - Color feature extraction: extracting useful information or characteristics from an image based on its color properties, such as color histogram, color moments, color texture, etc. .
  - Color image compression: reducing the size of an image by removing redundant or irrelevant color information, such as color quantization, color coding, color space reduction, etc. .
  - Color image restoration: removing noise or distortion from an image by applying filters or models that preserve or enhance its color information, such as color smoothing, color inpainting, color deblurring, etc. .
  - Color image fusion: combining two or more images with different color information to produce a new image that contains more or better color information, such as color stereo, color panorama, color multispectral, etc. .
  - Color image recognition: identifying or classifying objects or scenes in an image based on their color features, such as color face recognition, color object recognition, color scene recognition, etc. .



# RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two color models used in digital image processing to represent colors in images.
- RGB stands for red, green, and blue, which are the primary colors of light. The RGB color model is additive, meaning that different combinations of red, green, and blue light can produce a wide range of colors. The RGB color model is based on a Cartesian coordinate system, where each color is represented by a point in a three-dimensional space. The origin (0,0,0) corresponds to black, and the point (255,255,255) corresponds to white. The RGB color model is commonly used in computer graphics, display devices, and digital cameras .
- HSI stands for hue, saturation, and intensity, which are the three components of color perception in the human eye. The HSI color model is based on a cylindrical coordinate system, where each color is represented by an angle (hue), a distance from the center (saturation), and a height (intensity). The hue component measures the dominant wavelength of the color, ranging from 0 to 360 degrees. The saturation component measures the purity of the color, ranging from 0 (gray) to 1 (full color). The intensity component measures the brightness of the color, ranging from 0 (black) to 1 (white). The HSI color model is useful for image processing applications that require color manipulation, such as segmentation, enhancement, and compression .
- The RGB and HSI color models are related by mathematical formulas that can convert one model to another. For example, to convert an RGB pixel to an HSI pixel, the following steps are performed :
  - Normalize the RGB values by dividing them by 255, so that they range from 0 to 1.
  - Calculate the intensity component as the average of the normalized RGB values: I = (R + G + B) / 3
  - Calculate the hue component as the angle between the normalized RGB values in the RG plane, using the following formula: H = arccos[(R - G + R - B) / 2 * sqrt((R - G)^2 + (R - B) * (G - B))]
  - Calculate the saturation component as the ratio of the difference between the maximum and minimum normalized RGB values to the intensity component, using the following formula: S = 1 - [min(R, G, B) / I]
  - Convert the hue component from radians to degrees, and adjust it to the range of 0 to 360 degrees.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of two-dimensional mathematical preliminaries for the notes of the unit 1 - digital image fundamentals in the subject of image processing.

# Two-dimensional mathematical preliminaries

- A digital image is a two-dimensional array of discrete values, usually called pixels or picture elements. The pixels are arranged in rows and columns, and each pixel has a numerical value that represents its brightness or color.
- The size of a digital image is determined by the number of rows and columns of pixels, also known as the image resolution. For example, an image with 512 rows and 512 columns has a resolution of 512 x 512 pixels, or 262,144 pixels in total.
- The range of values that a pixel can have is called the image depth or bit depth. For example, a binary image has only two possible values for each pixel: 0 or 1, corresponding to black or white. A grayscale image has more values, usually 256, ranging from 0 (black) to 255 (white). A color image has three components for each pixel: red, green, and blue, each with a range of values, usually 256. The total number of colors that an image can display is the product of the ranges of the three components, for example, 256 x 256 x 256 = 16,777,216 colors.
- A digital image can be represented as a function f(x,y), where x and y are the spatial coordinates of a pixel, and f(x,y) is the pixel value at that location. The domain of f is a rectangular region in the xy plane, and the range of f is a finite set of discrete values.
- A digital image can also be represented as a matrix, where each element of the matrix corresponds to a pixel value. For example, a 3 x 3 binary image can be written as:

```
| 0 1 0 |
| 1 0 1 |
| 0 1 0 |
```

- A digital image can be manipulated by applying mathematical operations to the pixel values, such as addition, subtraction, multiplication, division, etc. These operations can be performed on a single image or on two or more images of the same size. For example, adding two images f(x,y) and g(x,y) results in a new image h(x,y) = f(x,y) + g(x,y), where the pixel values are added element-wise.
- A digital image can also be transformed by applying geometric operations to the pixel coordinates, such as translation, rotation, scaling, shearing, etc. These operations can change the size, shape, orientation, or position of the image. For example, rotating an image f(x,y) by an angle θ results in a new image g(x,y) = f(x cos θ + y sin θ, -x sin θ + y cos θ), where the pixel coordinates are rotated by θ.
- A digital image can also be analyzed by applying various techniques to extract information from the pixel values, such as histogram, statistics, filtering, edge detection, segmentation, feature extraction, etc. These techniques can reveal the properties, patterns, or regions of interest in the image. For example, computing the histogram of an image f(x,y) results in a plot of the frequency of occurrence of each pixel value in the image, which can show the contrast, brightness, or distribution of the image.



# 2D Transforms

2D transforms are operations that modify the position, size, shape, or orientation of an image on a 2D plane. They are useful for image processing and computer graphics applications, such as resizing, rotating, cropping, filtering, or enhancing images.

There are different types of 2D transforms, such as:

- **Translation**: This is the simplest 2D transform, which shifts an image by a certain amount of pixels in the horizontal and vertical directions. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
1 & 0 & t_x \\
0 & 1 & t_y \\
0 & 0 & 1
\end{bmatrix}
$$

where $t_x$ and $t_y$ are the translation parameters.

- **Scaling**: This is a 2D transform that changes the size of an image by a certain factor in the horizontal and vertical directions. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
s_x & 0 & 0 \\
0 & s_y & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

where $s_x$ and $s_y$ are the scaling factors.

- **Rotation**: This is a 2D transform that rotates an image by a certain angle around a fixed point, usually the origin. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
\cos \theta & -\sin \theta & 0 \\
\sin \theta & \cos \theta & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

where $\theta$ is the rotation angle.

- **Shearing**: This is a 2D transform that distorts an image by a certain amount in the horizontal or vertical direction, creating a slanted effect. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
1 & sh_x & 0 \\
sh_y & 1 & 0 \\
0 & 0 & 1
\end{bmatrix}
$$

where $sh_x$ and $sh_y$ are the shearing parameters.

- **Affine**: This is a general 2D transform that combines any of the above transforms, or any other linear transformation, into a single matrix. It can be represented by a 2x2 matrix of the form:

$$
\begin{bmatrix}
a & b & c \\
d & e & f \\
0 & 0 & 1
\end{bmatrix}
$$

where $a, b, c, d, e, f$ are the affine parameters.

- **Fourier**: This is a special 2D transform that converts an image from the spatial domain to the frequency domain, or vice versa. It decomposes an image into a sum of sinusoidal components, each with a certain amplitude, frequency, and phase. It can be used for image filtering, compression, enhancement, or analysis. It can be represented by a complex-valued function of the form:

$$
F(u, v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) e^{-j 2 \pi (ux + vy)} dx dy
$$

where $f(x, y)$ is the spatial image, $F(u, v)$ is the frequency image, $u$ and $v$ are the frequency variables, and $j$ is the imaginary unit.

- **Wavelet**: This is another special 2D transform that converts an image from the spatial domain to the wavelet domain, or vice versa. It decomposes an image into a set of wavelet functions, each with a certain scale, location, and orientation. It can be used for image compression, denoising, segmentation, or analysis. It can be represented by a real-valued function of the form:

$$
W(a, b, \theta) = \frac{1}{\sqrt{a}} \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x, y) \psi \left( \frac{x - b_x}{a}, \frac{y - b_y}{a}, \theta \right) dx



# DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- DFT stands for Discrete Fourier Transform, which is a mathematical operation that transforms a discrete sequence of values into another domain, such as frequency or spatial domain. DFT can be used to analyze the frequency components of an image, or to perform filtering, enhancement, or compression of an image.
- DCT stands for Discrete Cosine Transform, which is a special case of DFT, where the input sequence is assumed to be real and even. DCT can be used to transform an image into a domain where most of the energy is concentrated in a few coefficients, which makes it suitable for image compression. DCT is widely used in JPEG and other image compression standards.
- Some of the basic differences between DFT and DCT are:
  - DFT is complex, while DCT is real. This means that DCT requires less storage and computation than DFT.
  - DFT is symmetric, while DCT is asymmetric. This means that DCT can exploit the redundancy in the image better than DFT.
  - DFT has poor energy compaction, while DCT has excellent energy compaction. This means that DCT can represent an image with fewer coefficients than DFT, which reduces the amount of data to be transmitted or stored.
- Some of the advantages of using DFT and DCT for image processing are:
  - DFT and DCT can separate the low-frequency and high-frequency components of an image, which can be useful for image enhancement, restoration, or segmentation.
  - DFT and DCT can reduce the noise and artifacts in an image, by discarding or attenuating the coefficients that correspond to the noisy or irrelevant frequencies.
  - DFT and DCT can reduce the dimensionality of an image, by retaining only the most significant coefficients that capture the essential features of the image. This can improve the efficiency and performance of image processing algorithms, such as classification, recognition, or retrieval.
- Some of the methods to compute DFT and DCT for an image are:
  - DFT can be computed using the Fast Fourier Transform (FFT) algorithm, which reduces the complexity of the computation from O(N^2) to O(N log N), where N is the number of pixels in the image. FFT can be applied to any size of image, but it is more efficient when the image size is a power of 2.
  - DCT can be computed using a similar algorithm to FFT, which is called Fast Cosine Transform (FCT). FCT can also reduce the complexity of the computation from O(N^2) to O(N log N), but it requires the image size to be a power of 2. Alternatively, DCT can be computed using a DCT transform matrix, which is a matrix that contains the cosine values for each pair of pixels. The DCT transform matrix can be applied to any size of image, but it might be more efficient for small square images, such as 8-by-8 or 16-by-16.



## Unit 2 - IMAGE ENHANCEMENT

- Image enhancement is the process of improving the quality or appearance of an image by modifying its features, such as contrast, brightness, sharpness, noise, etc.
- Image enhancement can be done in two domains: spatial domain and frequency domain.
- Spatial domain techniques operate directly on the pixels of the image, while frequency domain techniques transform the image into its frequency components and manipulate them.
- Some common spatial domain techniques are:
  - Point processing: applying a function to each pixel independently, such as negative, log, power-law, etc.
  - Histogram processing: adjusting the distribution of pixel values, such as histogram equalization, specification, etc.
  - Spatial filtering: applying a mask or kernel to a neighborhood of pixels, such as smoothing, sharpening, edge detection, etc.
- Some common frequency domain techniques are:
  - Fourier transform: converting an image from spatial domain to frequency domain, where each pixel represents a sinusoidal component of the image.
  - Filtering: applying a filter to the frequency components, such as low-pass, high-pass, band-pass, etc.
  - Inverse Fourier transform: converting an image from frequency domain to spatial domain, where each pixel represents the intensity of the image.
- Image enhancement can be used for various applications, such as medical imaging, remote sensing, security, etc.



# Spatial Domain

- The spatial domain refers to the 2D image plane represented in terms of pixel intensities.
- Image enhancement in the spatial domain involves modifying the pixel values directly to improve the appearance or quality of the image .
- The general form of a spatial domain operation is:

$$g(x,y) = T[f(x,y)]$$

where $f(x,y)$ is the input image, $g(x,y)$ is the output image, and $T$ is an operator on $f$ defined over a neighborhood of $(x,y)$.

- There are two main types of spatial domain operations: point processing and neighborhood processing.
- Point processing is when the output pixel value depends only on the input pixel value at the same location, such as:

$$g(x,y) = T[f(x,y)]$$

where $T$ is a function of one variable.
- Examples of point processing are contrast stretching, histogram equalization, and thresholding.
- Neighborhood processing is when the output pixel value depends on the input pixel values in a neighborhood of the same location, such as:

$$g(x,y) = T[f(x,y),f(x-1,y),f(x+1,y),f(x,y-1),f(x,y+1),...]$$

where $T$ is a function of multiple variables.
- Examples of neighborhood processing are filtering, smoothing, sharpening, and edge detection.
- Spatial domain methods are simple, fast, and intuitive, but they may not be able to handle complex or global image features.



# Gray level transformations

Gray level transformations are image enhancement techniques that operate directly on the pixels of an image. They can be used to modify the contrast, brightness, or dynamic range of an image. They can also be used to create negative images, threshold images, or inverse-logarithmic images.

There are three basic types of gray level transformations:

- Linear transformations
- Logarithmic transformations
- Power-law transformations

## Linear transformations

Linear transformations are the simplest form of gray level transformations. They map the input gray level, r, to the output gray level, s, using a linear function of the form:

s = ar + b

where a and b are constants. The slope, a, determines the contrast of the output image, and the intercept, b, determines the brightness. If a = 1 and b = 0, the output image is identical to the input image. If a = -1 and b = 255, the output image is the negative of the input image.

Linear transformations can be used to adjust the contrast and brightness of an image by changing the range of gray levels. For example, if the input image has gray levels in the range [0, 100], and the output image has gray levels in the range [50, 200], the linear transformation is:

s = 1.5r + 50

This transformation increases the contrast and brightness of the image by stretching the gray level histogram.

## Logarithmic transformations

Logarithmic transformations are nonlinear transformations that map the input gray level, r, to the output gray level, s, using a logarithmic function of the form:

s = c log(1 + r)

where c is a constant. The logarithmic function compresses the high gray levels and expands the low gray levels. This can be useful for enhancing the details in dark regions of an image, such as X-ray images or astronomical images.

Logarithmic transformations can also be used to create inverse-logarithmic images, which are the negative of the logarithmic images. This can be done by subtracting the logarithmic image from the maximum gray level, 255. The inverse-logarithmic image has the opposite effect of the logarithmic image: it compresses the low gray levels and expands the high gray levels. This can be useful for enhancing the details in bright regions of an image, such as infrared images or thermal images.

## Power-law transformations

Power-law transformations are nonlinear transformations that map the input gray level, r, to the output gray level, s, using a power function of the form:

s = cr^γ

where c and γ are constants. The exponent, γ, determines the shape of the curve. If γ > 1, the curve is convex and the output image is darker than the input image. If γ < 1, the curve is concave and the output image is brighter than the input image. If γ = 1, the curve is linear and the output image is identical to the input image.

Power-law transformations can be used to correct the gamma of an image, which is the relation between the input intensity and the output brightness. Different devices, such as cameras, monitors, or printers, may have different gamma values, which can affect the appearance of an image. By applying a power-law transformation with the inverse gamma value, the image can be restored to its original brightness.

Power-law transformations can also be used to create threshold images, which are binary images that have only two gray levels: 0 or 255. This can be done by setting γ to a very large value, such as 10. This makes the curve very steep and the output image very sensitive to the input gray level. If the input gray level is above a certain threshold, the output gray level is 255; otherwise, it is 0. Threshold images can be useful for segmentation, edge detection, or object recognition.



# Histogram processing for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Histogram processing is a technique for adjusting the contrast and brightness of an image by modifying its intensity distribution  .
- A histogram is a graphical representation of the frequency of occurrence of each intensity level in an image .
- Histogram processing can be used to enhance the image quality by improving the visibility of details, reducing noise, and highlighting features of interest   .
- Histogram processing can be classified into two categories: histogram equalization and histogram specification  .

## Histogram equalization
- Histogram equalization is a method that transforms an image such that its histogram is approximately uniform, i.e., all intensity levels have equal probability   .
- Histogram equalization can enhance the contrast of an image by spreading out the intensity values over the entire range   .
- Histogram equalization can be performed by using the cumulative distribution function (CDF) of the original image as a mapping function to assign new intensity values to each pixel   .
- Histogram equalization can be applied to grayscale or color images, but it may affect the color balance and saturation of color images .
- Histogram equalization can be extended to adaptive histogram equalization, which divides the image into sub-regions and performs local histogram equalization on each sub-region .
- Histogram equalization can also be modified to contrast-limited adaptive histogram equalization, which limits the contrast enhancement in each sub-region to avoid amplifying noise .

## Histogram specification
- Histogram specification is a method that transforms an image such that its histogram matches a desired histogram, i.e., a specified probability distribution  .
- Histogram specification can be used to modify the contrast and brightness of an image by adjusting its intensity distribution to a desired shape  .
- Histogram specification can be performed by using the inverse CDF of the desired histogram and the CDF of the original image as mapping functions to assign new intensity values to each pixel  .
- Histogram specification can be applied to grayscale or color images, but it may affect the color balance and saturation of color images .
- Histogram specification can be used to perform histogram matching, which is a technique for aligning the histograms of two images for comparison or fusion  .
- Histogram specification can also be used to perform histogram stretching, which is a technique for increasing the dynamic range of an image by mapping its intensity values to the full range  .

## Examples of histogram processing
- The following figure shows an example of histogram equalization applied to a grayscale image:

Histogram equalization example

- The following figure shows an example of histogram specification applied to a color image:

Histogram specification example



# Basics of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering can be used for various purposes, such as enhancing, smoothing, sharpening, or detecting edges in an image   .
- Spatial filtering involves the use of a filter or a mask, which is a small matrix of coefficients that is applied to each pixel and its neighbors in an image  .
- The filter or mask is moved point-by-point in the image so that the center of the filter coincides with the pixel of interest  .
- At each point, the filter's response is calculated based on the specific content of the filter and through a predefined relationship called a template.
- The template defines how the filter coefficients are multiplied and summed with the pixel values in the image.
- The result of the filter's response is then assigned to the pixel of interest, creating a new image  .
- The process of moving the filter over the image and applying the template is called convolution  .
- Convolution can be expressed mathematically as:

$$g(x,y) = \sum_{s=-a}^{a} \sum_{t=-b}^{b} w(s,t) f(x+s, y+t)$$

where $g(x,y)$ is the filtered image, $f(x,y)$ is the original image, $w(s,t)$ is the filter coefficients, and $(2a+1) \times (2b+1)$ is the size of the filter.

- Spatial filters can be classified into two types: linear and nonlinear  .
- Linear filters are those that satisfy the superposition principle, which means that the filtered image is a linear combination of the original image and the filter  .
- Nonlinear filters are those that do not satisfy the superposition principle, which means that the filtered image depends on some nonlinear function of the original image and the filter  .
- Examples of linear filters are average, Gaussian, and Laplacian filters  .
- Examples of nonlinear filters are median, max, and min filters  .
- Linear filters are easier to implement and analyze, but they may produce undesirable effects such as blurring or ringing  .
- Nonlinear filters are more complex and difficult to analyze, but they may preserve edges and remove noise better than linear filters  .



# Smoothing and Sharpening Spatial Filtering

- Smoothing and sharpening are two types of spatial filtering techniques that can be applied to enhance digital images.
- Spatial filtering is the process of modifying the pixel values of an image based on a mathematical operation involving a neighborhood of pixels, called a filter or a kernel.
- Smoothing filters are used to reduce noise and blur details, while sharpening filters are used to enhance edges and contrast.

## Smoothing Filters

- Smoothing filters are also known as low-pass filters, because they allow low-frequency components of the image to pass through, while attenuating high-frequency components, such as noise and edges.
- Smoothing filters can be linear or nonlinear. Linear smoothing filters perform a weighted average of the pixel values in the neighborhood, while nonlinear smoothing filters use a different function, such as median or mode, to determine the output value.
- Common linear smoothing filters include:

  - Average filter: The output value is the mean of the pixel values in the neighborhood. The filter kernel is a matrix of ones divided by the number of elements. For example, a 3x3 average filter kernel is:

    ```
    1/9 1/9 1/9
    1/9 1/9 1/9
    1/9 1/9 1/9
    ```

  - Gaussian filter: The output value is the weighted mean of the pixel values in the neighborhood, where the weights are determined by a Gaussian function. The filter kernel is a matrix of Gaussian values, which can be computed using the formula:

    ```
    G(x,y) = (1/(2*pi*sigma^2))*exp(-((x-x0)^2+(y-y0)^2)/(2*sigma^2))
    ```

    where x0 and y0 are the coordinates of the center of the kernel, and sigma is the standard deviation of the Gaussian function. For example, a 3x3 Gaussian filter kernel with sigma = 1 is:

    ```
    0.075 0.124 0.075
    0.124 0.204 0.124
    0.075 0.124 0.075
    ```

- Common nonlinear smoothing filters include:

  - Median filter: The output value is the median of the pixel values in the neighborhood. The filter kernel is a matrix of ones. For example, a 3x3 median filter kernel is:

    ```
    1 1 1
    1 1 1
    1 1 1
    ```

  - Mode filter: The output value is the mode of the pixel values in the neighborhood. The filter kernel is a matrix of ones. For example, a 3x3 mode filter kernel is:

    ```
    1 1 1
    1 1 1
    1 1 1
    ```

- Smoothing filters can be applied to grayscale or color images. For color images, the smoothing operation can be performed on each color channel separately, or on a different color space, such as HSV or Lab.

## Sharpening Filters

- Sharpening filters are also known as high-pass filters, because they allow high-frequency components of the image to pass through, while attenuating low-frequency components, such as smooth regions.
- Sharpening filters can be linear or nonlinear. Linear sharpening filters perform a weighted difference of the pixel values in the neighborhood, while nonlinear sharpening filters use a different function, such as Laplacian or Sobel, to determine the output value.
- Common linear sharpening filters include:

  - Unsharp masking: The output value is the sum of the original pixel value and a scaled difference between the original pixel value and a smoothed pixel value. The filter kernel is a matrix of negative values, except for the center element, which is positive. For example, a 3x3 unsharp masking filter kernel is:

    ```
    -1 -1 -1
    -1  9 -1
    -1 -1 -1
    ```

  - High-boost filtering: The output value is the sum of the original pixel value and a scaled difference between the original pixel value and a smoothed pixel value, where the scale factor is greater than one. The filter kernel is a matrix of negative values, except for the center element, which is positive and larger than the sum of the absolute values of the other elements. For example, a 3x3 high-boost filter kernel with a scale factor of 2



# Frequency Domain

- Frequency domain is a way of representing an image in terms of its spatial frequencies, which are the rates of change of pixel values in different directions.
- Frequency domain methods of image enhancement are based on the Fourier transform, which converts an image from the spatial domain to the frequency domain, and vice versa.
- The Fourier transform of an image F(u,v) is a complex function that contains both the magnitude and the phase of the frequency components of the image.
- The magnitude of F(u,v) represents the amount of energy at each frequency, while the phase of F(u,v) represents the spatial location of the frequency components.
- Image enhancement in the frequency domain involves modifying the magnitude and/or the phase of F(u,v) and then applying the inverse Fourier transform to obtain the enhanced image.
- The advantage of frequency domain methods is that they can perform filtering operations more efficiently and intuitively than spatial domain methods, especially for large kernels.
- The disadvantage of frequency domain methods is that they may introduce artifacts or distortions in the enhanced image due to the loss of spatial information or the violation of the convolution theorem.

## Frequency Domain Filters

- Frequency domain filters are functions that modify the Fourier transform of an image according to some criteria, such as enhancing or attenuating certain frequency components, or removing noise or blurring effects.
- Frequency domain filters can be classified into two types: low-pass filters and high-pass filters.
- Low-pass filters are filters that preserve the low-frequency components of an image and attenuate the high-frequency components. They are used to smooth or blur an image, or to reduce noise or sharp edges.
- High-pass filters are filters that preserve the high-frequency components of an image and attenuate the low-frequency components. They are used to sharpen or enhance an image, or to emphasize edges or fine details.
- Frequency domain filters can also be designed based on the properties of the frequency spectrum of an image, such as its orientation, shape, or symmetry.
- Some examples of frequency domain filters are:

  - Ideal low-pass filter: a filter that has a circular region of radius D0 in the frequency domain, where all the frequencies within the region are preserved and all the frequencies outside the region are attenuated. This filter produces a sharp cutoff in the frequency domain, but it introduces ringing artifacts in the spatial domain due to the Gibbs phenomenon.
  - Butterworth low-pass filter: a filter that has a circular region of radius D0 in the frequency domain, where the frequencies within the region are preserved and the frequencies outside the region are attenuated gradually according to a parameter n, which controls the smoothness of the transition. This filter produces a smoother cutoff in the frequency domain, but it also reduces the contrast of the image in the spatial domain.
  - Gaussian low-pass filter: a filter that has a circular region of radius D0 in the frequency domain, where the frequencies within the region are preserved and the frequencies outside the region are attenuated exponentially according to a parameter σ, which controls the standard deviation of the Gaussian function. This filter produces the smoothest cutoff in the frequency domain, and it preserves the shape of the image in the spatial domain, but it also blurs the image more than the other filters.
  - Ideal high-pass filter: a filter that has a circular region of radius D0 in the frequency domain, where all the frequencies within the region are attenuated and all the frequencies outside the region are preserved. This filter produces a sharp cutoff in the frequency domain, but it introduces ringing artifacts in the spatial domain due to the Gibbs phenomenon.
  - Butterworth high-pass filter: a filter that has a circular region of radius D0 in the frequency domain, where the frequencies within the region are attenuated gradually and the frequencies outside the region are preserved according to a parameter n, which controls the smoothness of the transition. This filter produces a smoother cutoff in the frequency domain, but it also reduces the contrast of the image in the spatial domain.
  - Gaussian high-pass filter: a filter that has a circular region of radius D0 in the frequency domain, where the frequencies within the region are attenuated exponentially and the frequencies outside the region are preserved according to a parameter σ, which controls the standard deviation of the Gaussian function. This filter produces the smoothest cutoff in the frequency domain, and it preserves the shape of the image in the spatial domain, but it also blurs the image less than the other filters.
  - Laplacian filter: a filter that has a negative value at the origin and positive values elsewhere in the frequency domain, where the magnitude of the values is proportional to the square of the distance from the origin. This filter



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Introduction to Fourier Transform for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing.

# Introduction to Fourier Transform

- Fourier transform is a mathematical tool that converts a signal from its original domain (often time or space) to a representation in the frequency domain and vice versa.
- Fourier transform can be used to analyze the frequency components of a signal, such as an image, and to modify them for various purposes, such as image enhancement, compression, filtering, etc.
- Fourier transform can be applied to both continuous and discrete signals, but in image processing, we usually deal with discrete signals, such as digital images, which are represented by a matrix of pixel values.
- The discrete Fourier transform (DFT) is the discrete version of the Fourier transform, which operates on a finite number of samples of a signal. The DFT can be computed efficiently using a fast algorithm called the fast Fourier transform (FFT).
- The DFT of a one-dimensional signal, such as a row or a column of an image, is given by the formula:

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2 \pi k n / N}, \quad k = 0, 1, \dots, N-1
$$

where $x[n]$ is the $n$-th sample of the signal, $X[k]$ is the $k$-th frequency component of the DFT, $N$ is the number of samples, and $j$ is the imaginary unit.

- The inverse DFT of a one-dimensional signal is given by the formula:

$$
x[n] = \frac{1}{N} \sum_{k=0}^{N-1} X[k] e^{j 2 \pi k n / N}, \quad n = 0, 1, \dots, N-1
$$

where $X[k]$ is the $k$-th frequency component of the DFT, $x[n]$ is the $n$-th sample of the reconstructed signal, and $N$ is the number of samples.

- The DFT of a two-dimensional signal, such as an image, is given by the formula:

$$
X[u, v] = \sum_{m=0}^{M-1} \sum_{n=0}^{N-1} x[m, n] e^{-j 2 \pi (u m / M + v n / N)}, \quad u = 0, 1, \dots, M-1, \quad v = 0, 1, \dots, N-1
$$

where $x[m, n]$ is the pixel value at the coordinates $(m, n)$ of the image, $X[u, v]$ is the frequency component at the coordinates $(u, v)$ of the DFT, $M$ and $N$ are the number of rows and columns of the image, respectively.

- The inverse DFT of a two-dimensional signal is given by the formula:

$$
x[m, n] = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} X[u, v] e^{j 2 \pi (u m / M + v n / N)}, \quad m = 0, 1, \dots, M-1, \quad n = 0, 1, \dots, N-1
$$

where $X[u, v]$ is the frequency component at the coordinates $(u, v)$ of the DFT, $x[m, n]$ is the pixel value at the coordinates $(m, n)$ of the reconstructed image, and $M$ and $N$ are the number of rows and columns of the image, respectively.

- The DFT of an image can be visualized as a complex matrix, where each element has a real part and an imaginary part. The real part represents the cosine component of the frequency, and the imaginary part represents the sine component of the frequency. The magnitude of each element represents the amplitude of the frequency, and the angle of each element represents the phase of the frequency.
- The magnitude of the DFT of an image can be displayed as an image, where the brightness of each pixel corresponds to the amplitude of the frequency. The phase of the DFT of an image can also be displayed as an image, where the hue of each pixel corresponds to the phase of the frequency.
- The DFT of an image has



# Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components and preserve low frequency components  .
- Smoothing filters are used for noise reduction, contrast enhancement, and blurring of images  .
- Commonly seen smoothing filters include ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components and preserve high frequency components  .
- Sharpening filters are used for edge detection, enhancement of details, and sharpening of images  .
- Commonly seen sharpening filters include ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter .
- The choice of filter function depends on the characteristics of the image and the desired output .
- The filter function can be designed in the frequency domain or in the spatial domain and then converted to the frequency domain using Fourier transform .
- The filter function can be applied to the frequency domain image by multiplying it with the image or by convolving it with the image .
- The filter function can be modified by adding or subtracting a constant term to adjust the brightness of the output image .
- The filter function can be combined with other filter functions to achieve different effects, such as band pass filter, band reject filter, notch filter, etc .



# Ideal, Butterworth and Gaussian filters

- Ideal, Butterworth and Gaussian filters are types of frequency domain filters that are used for image enhancement in image processing.
- Frequency domain filters modify the Fourier transform of an image to achieve a desired effect, such as sharpening, smoothing, or removing noise.
- Ideal, Butterworth and Gaussian filters differ in the shape and smoothness of their transfer functions, which affect the quality and performance of the filtering.

## Ideal filter

- An ideal filter is a filter that has a sharp cutoff frequency and a constant magnitude response. It is also called a brick-wall filter or a rectangular filter.
- An ideal filter can be either a low-pass filter (ILPF) or a high-pass filter (IHPF), depending on whether it passes or blocks low-frequency components of the image.
- An ideal filter has the advantage of being simple and easy to implement, but it has the disadvantage of introducing ringing artifacts and aliasing in the filtered image, due to the abrupt changes in the frequency domain.

## Butterworth filter

- A Butterworth filter is a filter that has a smooth and monotonic magnitude response that approaches the ideal filter as the order of the filter increases. It is also called a maximally flat filter or a smooth filter.
- A Butterworth filter can be either a low-pass filter (BLPF) or a high-pass filter (BHPF), depending on whether it passes or blocks low-frequency components of the image.
- A Butterworth filter has the advantage of being more realistic and natural than the ideal filter, but it has the disadvantage of having a slower rolloff and a larger transition band, which may result in some unwanted frequencies being passed or blocked.

## Gaussian filter

- A Gaussian filter is a filter that has a bell-shaped magnitude response that follows the Gaussian distribution. It is also called a normal filter or a Gaussian bell filter.
- A Gaussian filter can be either a low-pass filter (GLPF) or a high-pass filter (GHPF), depending on whether it passes or blocks low-frequency components of the image.
- A Gaussian filter has the advantage of being smooth and continuous in both the spatial and frequency domains, which reduces the ringing artifacts and aliasing in the filtered image, but it has the disadvantage of having a wider bandwidth and a lower cutoff frequency than the ideal filter, which may result in some loss of image details.



# Homomorphic filtering

- Homomorphic filtering is a technique for image enhancement that can separate the illumination and reflectance components of an image.
- Illumination is the amount of light falling on the scene, which affects the brightness and contrast of the image. Reflectance is the property of the objects in the scene, which affects the color and texture of the image.
- Homomorphic filtering can improve the appearance of an image by reducing the effects of uneven illumination and enhancing the contrast and details of the reflectance.
- Homomorphic filtering involves the following steps:
  - Transform the image from the spatial domain to the frequency domain using the Fourier transform.
  - Apply a logarithmic function to the frequency domain image to convert the multiplicative components of illumination and reflectance into additive components.
  - Apply a high-pass filter to the logarithmic image to attenuate the low-frequency illumination component and enhance the high-frequency reflectance component.
  - Apply an exponential function to the filtered image to undo the logarithmic transformation and restore the multiplicative relationship between illumination and reflectance.
  - Transform the image back to the spatial domain using the inverse Fourier transform.
- Homomorphic filtering can be applied to various types of images, such as grayscale, color, infrared, and medical images, to improve their quality and visibility.



# Color image enhancement

Color image enhancement is the process of improving the visual quality and appearance of a color image by applying various techniques and algorithms. Color image enhancement can be used for various purposes, such as:

- Reducing noise and enhancing edges and details
- Adjusting contrast and brightness
- Correcting color balance and saturation
- Applying filters and effects
- Enlarging and sharpening images

Some of the common techniques and methods for color image enhancement are:

- Histogram equalization: This technique modifies the intensity distribution of an image to make it more uniform and enhance the contrast. Histogram equalization can be applied to each color channel separately or to the luminance component of a color space.
- Retinex theory: This theory proposes that the human visual system perceives the color and brightness of an object by comparing it with the surrounding illumination. Retinex-based algorithms aim to mimic this process by decomposing an image into reflectance and illumination components and enhancing the reflectance component.
- Color constancy: This technique adjusts the color of an image to make it consistent with a reference white point or a standard illuminant. Color constancy can be used to correct the color cast or tint caused by different lighting conditions or camera settings.
- Color transfer: This technique transfers the color characteristics of a source image to a target image, such as the hue, saturation, and tone. Color transfer can be used to create artistic effects or to match the color style of different images.
- Color enhancement by optimization: This technique formulates the color enhancement problem as an optimization problem, where an objective function is defined to measure the quality of an enhanced image and a set of constraints is imposed to preserve the naturalness and realism of the image. The optimization problem can be solved by various methods, such as gradient descent, genetic algorithms, or neural networks.



## Unit 3 - IMAGE RESTORATION

- Image restoration is the process of improving the quality of an image that has been degraded by noise, blur, or other factors.
- Image restoration aims to recover the original image from the degraded image, or to estimate the degradation model and the original image simultaneously.
- Image restoration can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixels of the image, and apply filters or operators to enhance or suppress certain features of the image.
- Frequency domain methods transform the image into a different domain, such as the Fourier domain, and manipulate the coefficients or spectra of the image to remove or reduce the effects of degradation.
- Image restoration can be further divided into two types: deterministic methods and probabilistic methods.
- Deterministic methods assume that the degradation model and the original image are known or can be estimated, and use mathematical techniques to solve an inverse problem or an optimization problem.
- Probabilistic methods assume that the degradation model and the original image are unknown or uncertain, and use statistical techniques to model the prior knowledge and the likelihood of the image, and infer the most probable or optimal solution.
- Some common image restoration techniques are:
  - Inverse filtering: a frequency domain method that applies the inverse of the degradation filter to the degraded image, assuming that the degradation filter and the noise are known or negligible.
  - Wiener filtering: a frequency domain method that applies a filter that minimizes the mean squared error between the restored image and the original image, assuming that the degradation filter and the noise power spectrum are known or estimated.
  - Regularized filtering: a frequency domain method that applies a filter that balances the fidelity and smoothness of the restored image, assuming that the degradation filter is known or estimated, and using a regularization parameter to control the trade-off.
  - Blind deconvolution: a method that estimates the degradation filter and the original image simultaneously, using an iterative algorithm that alternates between deconvolution and filter estimation, and using some constraints or priors to guide the solution.
  - Maximum likelihood estimation: a probabilistic method that estimates the original image that maximizes the likelihood of the degraded image, assuming that the degradation model and the noise distribution are known or specified.
  - Maximum a posteriori estimation: a probabilistic method that estimates the original image that maximizes the posterior probability of the original image given the degraded image, assuming that the degradation model, the noise distribution, and the prior distribution of the original image are known or specified.
  - Bayesian estimation: a probabilistic method that estimates the posterior distribution of the original image given the degraded image, assuming that the degradation model, the noise distribution, and the prior distribution of the original image are known or specified, and using a Bayesian inference technique such as Markov chain Monte Carlo or variational inference.



# Image Restoration

Image restoration is the process of improving the quality of an image that has been degraded by noise, blur, or other factors. Image restoration aims to recover the original image from the degraded one, or to produce an image that is close to the original in some sense.

Some of the objectives of image restoration are:

- To remove noise and artifacts from the image, such as salt-and-pepper noise, Gaussian noise, speckle noise, etc.
- To deblur the image, such as motion blur, defocus blur, atmospheric blur, etc.
- To enhance the contrast and sharpness of the image, such as histogram equalization, unsharp masking, etc.
- To correct the geometric distortions of the image, such as perspective correction, lens distortion correction, etc.
- To restore the color and brightness of the image, such as white balance, color correction, gamma correction, etc.

Some of the methods of image restoration are:

- Spatial domain methods, which operate directly on the pixel values of the image, such as spatial filtering, median filtering, etc.
- Frequency domain methods, which transform the image into the frequency domain, such as Fourier transform, discrete cosine transform, etc., and apply filtering or inverse transformation to the frequency components of the image, such as low-pass filtering, high-pass filtering, etc.
- Model-based methods, which assume a mathematical model of the degradation process, such as linear or nonlinear, additive or multiplicative, etc., and use inverse or iterative techniques to estimate the original image, such as Wiener filtering, Richardson-Lucy algorithm, etc.
- Learning-based methods, which use machine learning or deep learning techniques to learn the mapping from the degraded image to the restored image, such as convolutional neural networks, generative adversarial networks, etc.



# Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, distortion, etc.
- Image degradation is the process of reducing the quality or information content of an image due to various sources of degradation.
- A degradation model is a mathematical or probabilistic representation of how an image is degraded by a degradation function and an additive noise term.
- A degradation model can be expressed as:

  `g(x,y) = h(x,y) * f(x,y) + n(x,y)`

  where:

  - `g(x,y)` is the degraded image
  - `f(x,y)` is the original image
  - `h(x,y)` is the degradation function
  - `n(x,y)` is the additive noise term
  - `*` denotes the convolution operation

- The degradation function `h(x,y)` can be spatially invariant or spatially variant, depending on whether it is constant or varying across the image.
- The additive noise term `n(x,y)` can be modeled by different distributions, such as Gaussian, Poisson, salt-and-pepper, etc.
- The goal of image restoration is to estimate the original image `f(x,y)` from the degraded image `g(x,y)` and the degradation model.
- Image restoration can be performed by different methods, such as inverse filtering, Wiener filtering, blind deconvolution, regularization, etc.



# Properties of Image Restoration

Image restoration is the process of recovering an image that has been degraded by a degradation phenomenon, such as blurring, noise, or distortion. Image restoration is a fundamental problem in image processing, and it also provides a testbed for more general inverse problems.

Some of the properties of image restoration are:

- Image restoration is different from image enhancement, which aims to improve the visual quality of an image without considering the degradation process. Image restoration is based on a mathematical model of the degradation and the inverse process, while image enhancement is based on heuristic or empirical methods.
- Image restoration can be classified into two categories: spatial domain methods and frequency domain methods. Spatial domain methods operate directly on the pixel values of the image, while frequency domain methods transform the image into a frequency representation (such as Fourier transform) and perform operations on the frequency components.
- Image restoration can be formulated as an optimization problem, where the objective is to find the restored image that minimizes a cost function that measures the discrepancy between the degraded image and the restored image, and possibly incorporates some prior knowledge or regularization terms. The cost function can be based on different criteria, such as least squares, maximum likelihood, or maximum a posteriori.
- Image restoration can be influenced by several factors, such as the accuracy of the degradation model, the availability of the point-spread function (PSF) that characterizes the blurring effect, the noise level and distribution, and the computational complexity and stability of the restoration algorithm.
- Image restoration can benefit from exploiting some properties of natural images, such as cross-scale similarity and anisotropic image features. These properties can help to preserve the image structure and details, and to avoid artifacts such as ringing or oversmoothing.



# Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Image restoration is the process of recovering an original image from a degraded image that has been corrupted by noise, blur, or other distortions.
- Image degradation can be modeled as a linear system, where the degraded image g(x,y) is the result of the convolution of the original image f(x,y) with a degradation function h(x,y), plus an additive noise term n(x,y):

  g(x,y) = h(x,y) * f(x,y) + n(x,y)

- In the frequency domain, the degradation model can be written as:

  G(u,v) = H(u,v) F(u,v) + N(u,v)

- The goal of image restoration is to estimate the original image f(x,y) or F(u,v) from the degraded image g(x,y) or G(u,v), given some knowledge of the degradation function h(x,y) or H(u,v) and the noise term n(x,y) or N(u,v).
- The noise term n(x,y) or N(u,v) represents the random fluctuations in the image intensity that are not part of the original image. The noise can be introduced during the image acquisition or transmission process, and can be affected by various factors such as sensor quality, lighting conditions, atmospheric interference, etc. .
- There are several noise models that are commonly used in digital image processing, each with a different probability density function (PDF) that describes the distribution of the noise values. Some of the most widely used noise models are :

  - Gaussian noise: The noise values follow a normal or Gaussian distribution with a mean of zero and a standard deviation of sigma. The PDF of Gaussian noise is given by:

    p(z) = (1 / sqrt(2 pi sigma^2)) exp(-z^2 / 2 sigma^2)

  - Rayleigh noise: The noise values follow a Rayleigh distribution with a mode of zero and a parameter of sigma. The PDF of Rayleigh noise is given by:

    p(z) = (z / sigma^2) exp(-z^2 / 2 sigma^2), z >= 0

  - Gamma noise: The noise values follow a gamma distribution with a shape parameter of alpha and a scale parameter of beta. The PDF of gamma noise is given by:

    p(z) = (beta^alpha / Gamma(alpha)) z^(alpha-1) exp(-beta z), z >= 0

  - Exponential noise: The noise values follow an exponential distribution with a parameter of lambda. The PDF of exponential noise is given by:

    p(z) = lambda exp(-lambda z), z >= 0

  - Uniform noise: The noise values follow a uniform distribution with a lower bound of a and an upper bound of b. The PDF of uniform noise is given by:

    p(z) = 1 / (b - a), a <= z <= b

  - Salt-and-pepper noise: The noise values are either 0 (black) or 255 (white) with a probability of p/2 each, and the original image values with a probability of 1-p. The PDF of salt-and-pepper noise is given by:

    p(z) = p/2, z = 0 or 255
    p(z) = 1 - p, 0 < z < 255

  - Speckle noise: The noise values are multiplicative, meaning that they are proportional to the original image values. The noise values follow a Gaussian distribution with a mean of zero and a variance of sigma^2. The PDF of speckle noise is given by:

    p(z) = (1 / sqrt(2 pi sigma^2)) exp(-(z - f)^2 / 2 sigma^2)

- Different noise models have different effects on the image quality and require different restoration techniques. Some of the common restoration methods are inverse filtering, Wiener filtering, constrained least squares filtering, maximum likelihood estimation, maximum a posteriori estimation, etc. .
- Image restoration is an important and challenging task in image processing, as it can improve the visual quality and usability of the images for various applications such as medical imaging, remote sensing, astronomy, etc. .



# Mean Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Mean filters are a type of spatial filters that are used to smooth images by reducing the amount of intensity variation between neighboring pixels .
- Mean filters work by moving through the image pixel by pixel, replacing each value with the average value of neighboring pixels, including itself .
- Mean filters can be implemented using a convolution mask or kernel, which is a small matrix that defines the weights of the neighboring pixels for calculating the average.
- Mean filters can reduce noise in images, but they also blur the edges and details of the image .
- There are different types of mean filters, such as arithmetic mean, geometric mean, harmonic mean, and contra-harmonic mean, which use different formulas for calculating the average.
- There are also adaptive mean filters, such as median filter, percentile filter, and bilateral filter, which use different criteria for selecting the neighboring pixels for calculating the average.
- Mean filters are simple, intuitive, and easy to implement, but they may not be effective for removing some types of noise, such as salt-and-pepper noise or impulse noise .



# Order Statistics for Image Restoration

- Order statistics are statistical measures that depend on the ordering or ranking of the data values, such as the minimum, maximum, median, and percentiles.
- Order statistic filters are non-linear spatial filters that operate on the ranked pixels in a local neighborhood of an image, and replace the center pixel with a value determined by the ranking result.
- Order statistic filters are useful for image restoration when the image is corrupted by noise or other degradation phenomena that affect the pixel values in a random or unpredictable way.
- Some common order statistic filters are:
  - The linear average filter, which computes the arithmetic mean of the pixels in the neighborhood.
  - The median filter, which selects the middle value of the pixels in the neighborhood.
  - The minimum filter, which selects the smallest value of the pixels in the neighborhood.
  - The maximum filter, which selects the largest value of the pixels in the neighborhood.
  - The alpha-trimmed mean filter, which discards the highest and lowest alpha percent of the pixels in the neighborhood, and computes the mean of the remaining pixels.
  - The mid-point filter, which computes the average of the minimum and maximum values of the pixels in the neighborhood.
- Order statistic filters have different properties and effects on the image, such as smoothing, sharpening, edge preservation, noise reduction, and outlier removal .
- Order statistic filters can be designed and optimized for specific types of noise or degradation, such as Gaussian noise, salt-and-pepper noise, speckle noise, impulse noise, etc .
- Order statistic filters can also be extended to higher order statistics, which involve moments or cumulants of higher than second order, such as skewness and kurtosis.
- Higher order statistics are less affected by the background than the second order measures, and can be used to identify the noise pixels or the edges in the image.
- Higher order statistics can also be used for blind deconvolution, which is a technique to restore an image that has been blurred by an unknown point spread function.
- Higher order statistics can be combined with other image restoration techniques, such as nonlocal image averaging, to achieve better results.



# Adaptive filters for image restoration

- Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image .
- Adaptive filters adjust their parameters or coefficients according to the characteristics of the input image or the noise model.
- Adaptive filters can be classified into two categories: spatial domain filters and frequency domain filters.
- Spatial domain filters operate directly on the pixel values of the image and use a local neighborhood of pixels to estimate the noise-free value.
- Frequency domain filters transform the image into the frequency domain and apply a filter function to the frequency components of the image.
- Some examples of spatial domain adaptive filters are adaptive median filter, adaptive Wiener filter, adaptive bilateral filter, and adaptive anisotropic diffusion filter  .
- Some examples of frequency domain adaptive filters are adaptive notch filter, adaptive bandpass filter, and adaptive Wiener filter.
- The main advantage of adaptive filters is that they can adapt to the varying noise and image characteristics and provide better results than fixed filters .
- The main challenge of adaptive filters is to design an appropriate filter function or algorithm that can adjust the filter parameters or coefficients according to the input image or the noise model .



# Band reject filters

- A band reject filter is a type of filter that attenuates a range of frequencies and passes the rest.
- A band reject filter is useful when the general location of the noise in the frequency domain is known.
- A band reject filter can be implemented by adding a low-pass filter and a high-pass filter with different cutoff frequencies.
- A band reject filter can be designed using different methods, such as Butterworth, Gaussian, or ideal filters.
- A band reject filter can be applied to an image by transforming the image to the frequency domain, multiplying the image with the filter, and transforming back to the spatial domain.
- A band reject filter can be used to remove periodic noise, such as moire patterns, from an image.



# Band Pass Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Band-pass filters are filters that allow only a certain range of frequencies to pass through, while attenuating the frequencies outside the range.
- Band-pass filters can be used to enhance or extract specific features from an image, such as edges, blobs, textures, etc .
- Band-pass filters can also be used to reduce noise and blur from an image, by eliminating the low-frequency and high-frequency components that are usually associated with these artifacts .
- Band-pass filters can be implemented in both spatial domain and frequency domain, depending on the application and the desired effect .
- In spatial domain, band-pass filters can be obtained by multiplying a low-pass filter with a high-pass filter, where the low-pass filter has a higher cut-off frequency than the high-pass filter.
- In frequency domain, band-pass filters can be obtained by applying a mask or a window to the Fourier transform of the image, where the mask or the window has a non-zero value only for the desired frequency range .
- Some examples of band-pass filters are:
  - Difference of Gaussians (DoG) filter, which is obtained by subtracting two Gaussian filters with different standard deviations.
  - Butterworth filter, which is a smooth filter that has a gradual transition from passband to stopband.
  - Gabor filter, which is a sinusoidal wave modulated by a Gaussian envelope, and can capture both frequency and orientation information.
- Band-pass filters have many applications and advantages in image processing, such as:
  - Edge detection, which is the process of identifying and locating sharp discontinuities in an image .
  - Blob detection, which is the process of finding regions of interest that are brighter or darker than the surrounding .
  - Texture analysis, which is the process of characterizing the surface properties of an image, such as coarseness, smoothness, regularity, etc .
  - Image enhancement, which is the process of improving the quality or the appearance of an image, such as contrast, sharpness, brightness, etc .
  - Image restoration, which is the process of recovering the original image from a degraded image, such as removing noise, blur, distortion, etc .



# Notch Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- A notch filter is an image processing filter that is used to remove specific frequency components from an image.
- A notch filter is a type of band-stop filter that is designed to remove a specific range of frequencies from an image while leaving the rest of the image unaffected.
- A notch filter can be used to eliminate noises from digital images, such as periodic noise or interference patterns .
- A notch filter can be implemented in the frequency domain by multiplying the Fourier transform of the image by a notch filter function .
- A notch filter function can be designed using different methods, such as ideal, Butterworth, or Gaussian .
- An ideal notch filter function is a binary function that has a value of zero at the frequencies to be removed and a value of one elsewhere.
- A Butterworth notch filter function is a smooth function that has a value of zero at the frequencies to be removed and a value of one elsewhere, with a gradual transition between the two values. The order of the Butterworth filter determines the sharpness of the transition.
- A Gaussian notch filter function is a bell-shaped function that has a value of zero at the frequencies to be removed and a value of one elsewhere, with a smooth transition between the two values. The standard deviation of the Gaussian function determines the width of the transition.
- A notch filter can be applied to an image by creating a notch filter function that matches the frequency components of the noise or interference in the image, and then multiplying the Fourier transform of the image by the notch filter function .
- A notch filter can be used to improve the quality of an image by removing unwanted frequency components that degrade the image .



# Optimum Notch Filtering

- Optimum notch filtering is a technique for image restoration that aims to remove periodic noise from images.
- Periodic noise is a type of noise that creates repetitive patterns on images, such as stripes, grids, or interference fringes.
- Periodic noise can be caused by various factors, such as electrical interference, sensor defects, or scanning artifacts.
- Periodic noise can degrade the visual quality of images and affect the performance of image processing tasks, such as segmentation, edge detection, or feature extraction.
- Optimum notch filtering is based on the idea that periodic noise can be localized in the frequency domain, and can be suppressed by applying a notch filter that attenuates the noise frequencies while preserving the image frequencies.
- A notch filter is a type of band-reject filter that has a narrow stopband around a specific frequency and a wide passband elsewhere.
- A notch filter can be designed by using a low-pass filter and a high-pass filter with the same cutoff frequency, and subtracting their outputs.
- A notch filter can be applied to an image by performing the following steps:
  - Transform the image from the spatial domain to the frequency domain using the Fourier transform.
  - Identify the noise frequencies in the frequency spectrum of the image, and mark their locations as notches.
  - Design a notch filter that has zeros at the notch locations and ones elsewhere, and multiply it with the frequency spectrum of the image.
  - Transform the filtered frequency spectrum back to the spatial domain using the inverse Fourier transform, and obtain the restored image.
- Optimum notch filtering can be adaptive or non-adaptive, depending on whether the notch locations and widths are fixed or variable.
- Adaptive notch filtering can adjust to the variations of the noise frequencies and the image characteristics, and can achieve better noise reduction and image preservation than non-adaptive notch filtering.
- Adaptive notch filtering can be implemented by using various methods, such as comb-type notch filtering, fuzzy transform-based notch filtering, or dynamic restoration using the upper-half spectrum .



# Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- Inverse filtering assumes that the degradation process can be modeled as a linear and space-invariant system, and that the blurring filter and the noise characteristics are known .
- Inverse filtering can be performed in the frequency domain, by applying the inverse of the blurring filter's frequency response to the degraded image's spectrum .
- Inverse filtering can be expressed as:

$$\hat{F}(u,v) = \frac{G(u,v)}{H(u,v)}$$

where $\hat{F}(u,v)$ is the restored image spectrum, $G(u,v)$ is the degraded image spectrum, and $H(u,v)$ is the blurring filter's frequency response .

- Inverse filtering can recover the original image exactly if the blurring filter is invertible and there is no noise in the degraded image .
- However, inverse filtering is very sensitive to additive noise, as it tends to amplify the high-frequency components of the noise, resulting in ringing artifacts and noise amplification in the restored image .
- To reduce the noise sensitivity of inverse filtering, some modifications can be applied, such as truncated inverse filtering, Wiener filtering, constrained least squares filtering, or iterative methods   .
- Truncated inverse filtering sets the inverse filter to zero for frequencies where the blurring filter is close to zero, to avoid dividing by very small numbers .
- Wiener filtering incorporates a priori knowledge of the noise and the original image spectra, and minimizes the mean square error between the restored and the original image .
- Constrained least squares filtering imposes a smoothness constraint on the restored image, and minimizes a cost function that balances the fidelity and the smoothness terms .
- Iterative methods update the restored image iteratively, using gradient descent or other optimization techniques, until a convergence criterion is met  .



# Wiener filtering for image restoration

Wiener filtering is a technique for restoring images that are degraded by a known linear filter and additive noise. It is based on minimizing the mean square error between the restored image and the original image.

## Theory

The degradation model for an image can be expressed as:

$$
g(x,y) = h(x,y) \ast f(x,y) + n(x,y)
$$

where $g(x,y)$ is the degraded image, $h(x,y)$ is the degradation filter, $f(x,y)$ is the original image, $n(x,y)$ is the additive noise, and $\ast$ denotes convolution.

The goal of image restoration is to recover $f(x,y)$ from $g(x,y)$. One possible solution is to use inverse filtering, which is based on applying the inverse of the degradation filter to the degraded image:

$$
\hat{f}(x,y) = \frac{G(u,v)}{H(u,v)}
$$

where $\hat{f}(x,y)$ is the restored image, $G(u,v)$ and $H(u,v)$ are the Fourier transforms of $g(x,y)$ and $h(x,y)$, respectively.

However, inverse filtering is very sensitive to noise, since it can amplify the high-frequency components of the noise. A better solution is to use Wiener filtering, which is based on applying a filter that minimizes the mean square error between the restored image and the original image:

$$
\hat{f}(x,y) = \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2 + S_n(u,v)/S_f(u,v)}G(u,v)
$$

where $H^*(u,v)$ is the complex conjugate of $H(u,v)$, $S_f(u,v)$ and $S_n(u,v)$ are the power spectra of the original image and the noise, respectively.

## Implementation

To implement the Wiener filter in practice, we have to estimate the power spectra of the original image and the noise. One possible method is to use the local mean and variance of the degraded image as estimates of the signal and noise power, respectively. Another possible method is to use a blind-Wiener filter, which iteratively estimates the degradation filter and the power spectra of the original image and the noise.

## Example

To illustrate the Wiener filtering in image restoration, we use the standard 256x256 Lena test image. We blur the image with a 9x9 Gaussian filter with a standard deviation of 2, then add white Gaussian noise with a variance of 100. The Wiener filtering is applied to the image with a cascade implementation of the noise smoothing and inverse filtering. The results are shown below.

Original image:

Original image

Degraded image:

Degraded image

Restored image:

Restored image

## References

: [WIENER FILTERING - Rice University](https://www.owlnet.rice.edu/~elec539/Projects99/BACH/proj2/wiener.html)

: [Deblur Images Using a Wiener Filter - MATLAB & Simulink Example - MathWorks](https://www.mathworks.com/help/images/deblurring-images-using-a-wiener-filter.html)

: [Image restoration by blind‐Wiener filter - Yoo - 2014 - IET Image Processing](https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/iet-ipr.2013.0693)



## Unit 4 - IMAGE SEGMENTATION

- Image segmentation is the process of partitioning an image into multiple segments, each of which has a label or a class  .
- Image segmentation is typically used to locate objects and boundaries in images, such as people, animals, buildings, roads, etc .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be based on various heuristics or high-level image features, such as color, intensity, texture, shape, edge, region, etc.
- Image segmentation can be classified into two main types: supervised and unsupervised.
  - Supervised image segmentation uses a set of labeled images as training data to learn a model that can segment new images.
  - Unsupervised image segmentation does not use any labeled images, but relies on clustering or grouping algorithms to find the natural segments in the image.
- Image segmentation can be further divided into several subtypes, such as semantic segmentation, instance segmentation, panoptic segmentation, etc.
  - Semantic segmentation assigns a class label to each pixel in the image, such as person, car, sky, etc.
  - Instance segmentation assigns a class label and an instance identifier to each pixel in the image, such as person 1, person 2, car 1, car 2, etc.
  - Panoptic segmentation combines semantic and instance segmentation, and also assigns a class label to the background pixels, such as road, grass, wall, etc.
- Image segmentation can be implemented using various techniques, such as thresholding, region growing, edge detection, watershed, graph-based methods, neural networks, etc.
  - Thresholding is a simple technique that divides the image into two or more segments based on a predefined or adaptive threshold value.
  - Region growing is a technique that starts from a seed pixel and expands the segment by adding neighboring pixels that have similar properties.
  - Edge detection is a technique that finds the boundaries of the segments by detecting the discontinuities in the image.
  - Watershed is a technique that treats the image as a topographic surface and finds the segments by flooding the surface from the local minima.
  - Graph-based methods are techniques that model the image as a graph and find the segments by partitioning the graph into subgraphs.
  - Neural networks are techniques that use deep learning models, such as convolutional neural networks (CNNs), to learn the features and the labels of the segments from the data.



# Edge detection

- Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction.
- Edge detection is a method of segmenting an image into regions of discontinuity, where there is a significant change in the gray level.
- Edge detection allows users to observe the features of an image, such as boundaries, contours, and outlines of objects.
- Edge detection is also used in various downstream tasks in computer vision, such as line detection, feature detection, and image classification.

## Edge properties

- The edges extracted from a two-dimensional image of a three-dimensional scene can be classified as either viewpoint dependent or viewpoint independent.
- Viewpoint dependent edges are those that change as the viewpoint changes, such as occlusion boundaries, shadows, and specular reflections.
- Viewpoint independent edges are those that remain constant regardless of the viewpoint, such as object boundaries, surface markings, and texture changes.
- Viewpoint independent edges are more desirable for image analysis and interpretation, as they are more robust and invariant to illumination and perspective changes.

## Edge detection operators

- Edge detection operators are mathematical functions that compute an image gradient to quantify the magnitude and direction of edges in an image.
- Image gradient is a vector that points in the direction of the most rapid change in intensity, and whose magnitude is the rate of change in that direction.
- Edge detection operators can be classified into two categories: first-order and second-order.
- First-order edge detection operators use the first derivative of the image intensity to detect edges, such as Sobel, Prewitt, and Roberts operators.
- Second-order edge detection operators use the second derivative of the image intensity to detect edges, such as Laplacian, Laplacian of Gaussian (LoG), and Canny operators.
- First-order edge detection operators are more sensitive to noise, as noise can cause rapid changes in intensity.
- Second-order edge detection operators are more robust to noise, as they can suppress noise by smoothing the image before applying the second derivative.
- Canny edge detection operator is one of the most widely used and optimal edge detection operators, as it satisfies the following criteria:
  - Good detection: the operator should detect as many real edges as possible.
  - Good localization: the detected edges should be as close as possible to the true edges.
  - Minimal response: the operator should return one response per edge and avoid multiple responses to a single edge.



# Edge linking via Hough transform

- Edge linking is the process of connecting edge pixels in an image to form continuous edge contours.
- Edge linking can be done by local or global methods.
- Local methods analyze the characteristics of pixels in a small neighborhood around each edge pixel and link them based on criteria such as gradient direction, intensity, or continuity.
- Global methods use a parameter space to represent all possible curves that can pass through the edge pixels and find the optimal ones that maximize some objective function.
- Hough transform is a global method that can detect lines, circles, ellipses, or other shapes in an image.
- Hough transform works by mapping each edge pixel in the image space to a set of curves in the parameter space, where each curve corresponds to a possible shape that passes through the pixel.
- The parameter space is discretized into cells, called accumulator cells, and each cell counts the number of curves that pass through it.
- The cells with high counts indicate the presence of a shape in the image space, and the parameters of the shape can be obtained from the coordinates of the cell.
- For example, to detect lines in an image, the parameter space is defined by the slope and intercept of the line, and each edge pixel is mapped to a sinusoidal curve in the parameter space.
- The accumulator cells that lie on the peaks of the sinusoids indicate the lines in the image, and the slope and intercept of the line can be obtained from the cell coordinates.
- Hough transform can be used to link edge pixels that belong to the same shape, by finding the accumulator cells that correspond to the shape and tracing back the edge pixels that map to those cells.
- Hough transform can handle noisy, incomplete, or broken edges, and can detect multiple shapes in an image.
- However, Hough transform also has some limitations, such as requiring a priori knowledge of the shape to be detected, being sensitive to the choice of parameter space and accumulator resolution, and being computationally expensive.



# Thresholding for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Thresholding is one of the segmentation techniques that generates a binary image (a binary image is one whose pixels have only two values – 0 and 1 and thus requires only one bit to store pixel intensity) from a given grayscale image by separating it into two regions based on a threshold value.
- Image thresholding is a type of image segmentation that divides the foreground from the background in an image. In this technique, the pixel values are assigned corresponding to the provided threshold values. In computer vision, thresholding is done in grayscale images.
- Image thresholding segmentation is a simple form of image segmentation. It is a way to create a binary or multi-color image based on setting a threshold value on the pixel intensity of the original image. In this thresholding process, we will consider the intensity histogram of all the pixels in the image.
- In digital image processing, thresholding is the simplest method of segmenting images. From a grayscale image, thresholding can be used to create binary images.
- Image segmentation by thresholding is an important and fundamental task in image processing and computer vision. In this paper, a new bi-level thresholding approach based on weighted Parzen window estimation is proposed.

## Types of Thresholding
- There are different types of thresholding methods, such as global, local, adaptive, and dynamic thresholding.
- Global thresholding is a simple and widely used method, where a single threshold value is applied to the whole image. The pixels with intensity values above the threshold are assigned to one region, and the pixels with intensity values below the threshold are assigned to another region. Global thresholding works well when the image has a bimodal histogram, i.e., when the foreground and background pixels have distinct intensity distributions  .
- Local thresholding is a method where the threshold value is determined for each pixel based on its local neighborhood. This method can handle images with varying illumination or contrast, where a global threshold may not be suitable. Local thresholding can be done by using a sliding window, a circular window, or a Gaussian window to compute the local statistics of the pixel intensity, such as mean, median, or standard deviation  .
- Adaptive thresholding is a method where the threshold value is adjusted dynamically according to the image characteristics. This method can handle complex images with multiple regions, textures, or noise. Adaptive thresholding can be done by using a clustering algorithm, such as k-means or Otsu's method, to group the pixels into different classes based on their intensity values, and then assign a threshold value for each class  .
- Dynamic thresholding is a method where the threshold value is updated over time based on the changes in the image. This method can handle images with moving objects, occlusions, or background variations. Dynamic thresholding can be done by using a feedback mechanism, such as a Kalman filter or a particle filter, to track the state of the image and estimate the optimal threshold value for each frame .

## Advantages and Disadvantages of Thresholding
- The advantages of thresholding are:
  - It is a simple and fast method that can be easily implemented and parallelized.
  - It can reduce the complexity and size of the image by converting it into a binary or multi-color image.
  - It can enhance the contrast and visibility of the image by separating the foreground and background regions.
- The disadvantages of thresholding are:
  - It may not work well for images with low contrast, noise, or overlapping intensity distributions of the foreground and background regions.
  - It may lose some information or introduce some artifacts in the image by binarizing the pixel values.
  - It may require manual tuning or selection of the threshold value or method for different images or applications.



# Region based segmentation

Region based segmentation is a technique for determining the regions in an image directly, based on the similarity or homogeneity of the pixels within the regions. A region is a connected set of pixels that share some common properties, such as intensity, color, texture, etc. Region based segmentation methods can be classified into two categories:

- Region growing methods: These methods start with some initial seed points (usually selected by the user or randomly) and grow the regions by adding neighboring pixels that satisfy some predefined criteria (such as intensity difference, distance, etc.). The process continues until no more pixels can be added to any region. Region growing methods are simple and intuitive, but they depend on the choice of seed points and the criteria for region expansion. They may also produce over-segmented or under-segmented results if the image has noise or complex boundaries. 

- Region splitting and merging methods: These methods start with the whole image as a single region and recursively split it into smaller regions if they are not homogeneous enough, or merge adjacent regions if they are similar enough. The splitting and merging criteria can be based on some statistical measures, such as mean, variance, histogram, etc. Region splitting and merging methods are more robust to noise and can handle complex boundaries, but they may require more computation and memory than region growing methods. They may also produce over-segmented or under-segmented results if the criteria are not well defined.  

Region based segmentation methods are suitable for images that have distinct and homogeneous regions, such as medical images, satellite images, etc. However, they may fail to capture the semantic meaning of the regions, such as objects, faces, etc. Therefore, region based segmentation methods are often combined with other techniques, such as edge detection, feature extraction, classification, etc., to obtain more meaningful and accurate segmentation results.



# Region Growing

Region growing is a region-based image segmentation method that involves the selection of initial seed points and the expansion of regions around them based on some similarity criteria. The main steps of region growing are:

- Select one or more seed pixels as the initial regions.
- Compare the neighboring pixels of each region with the region's properties, such as mean, variance, color, texture, etc.
- If the neighboring pixels are similar enough to the region, add them to the region and update the region's properties.
- Repeat steps 2 and 3 until no more pixels can be added to any region.
- Optionally, merge adjacent regions that are similar enough to form larger regions.

Region growing is a simple and intuitive method, but it has some drawbacks, such as:

- The choice of seed pixels can affect the final segmentation result.
- The similarity criteria and the threshold values can be difficult to determine and may vary for different images or regions.
- The method can be sensitive to noise and outliers, which can cause over-segmentation or under-segmentation.
- The method can be computationally expensive, especially for large images or complex regions.



# Region splitting and merging

- Region splitting and merging is an image processing technique used to segment an image into homogeneous regions.
- The image is recursively divided into smaller regions (quadrants) until each region satisfies a predefined criterion of homogeneity .
- The homogeneity criterion can be based on pixel intensity, color, texture, or other features of the image.
- The regions are stored in a quadtree data structure, which is a tree where each node has four children.
- The quadtree allows efficient access and manipulation of the regions.
- After splitting, the regions are merged by applying a similarity criterion that determines whether two adjacent regions should be combined or not .
- The similarity criterion can also be based on pixel intensity, color, texture, or other features of the image.
- The merging process reduces the number of regions and produces the final segmentation result .
- The advantages of region splitting and merging are that it can handle complex images with multiple regions and it can adapt to the local characteristics of the image .
- The disadvantages of region splitting and merging are that it can be sensitive to noise and it can produce over-segmentation or under-segmentation depending on the choice of the homogeneity and similarity criteria .



# Morphological processing- erosion and dilation

- Morphological processing is a technique of image processing that uses erosion and dilation operations to modify the shape and size of objects in an image .
- Erosion is an operation that removes pixels from the boundaries of objects in an image, making them smaller and thinner. Erosion can be used to eliminate noise, separate objects, and smooth boundaries.
- Dilation is an operation that adds pixels to the boundaries of objects in an image, making them larger and thicker. Dilation can be used to fill gaps, connect objects, and enhance features.
- The effect of erosion and dilation depends on the size and shape of the structuring element, which is a small binary image that defines the neighborhood of each pixel. The structuring element is usually a square, a circle, or a cross.
- Erosion and dilation can be combined to perform other morphological operations, such as opening, closing, gradient, black hat, and top hat . These operations can be used for various image processing tasks, such as preprocessing for OCR algorithms, detecting barcodes, detecting license plates, and more.
- Image segmentation is the process of dividing an image into meaningful regions or objects. Morphological processing can be used to perform image segmentation by applying erosion and dilation to extract the foreground or background of an image. For example, morphological reconstruction can be used to segment an image based on markers that indicate the regions of interest.



# Segmentation by morphological watersheds

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as brightness, color, texture, etc.  
- Segmentation by morphological watersheds is a region-based technique that uses the concept of watershed lines to separate the regions of an image.  
- A watershed line is a boundary that separates two adjacent catchment basins, which are regions where water flows towards a common point.  
- The idea of morphological watersheds is to treat the image as a topographic surface, where the intensity of each pixel represents the height or depth of the surface.  
- The local minima of the surface are considered as markers or seeds, which are the starting points of the regions. The water level is gradually raised from the markers, and the regions grow until they meet at the watershed lines.  
- The watershed lines form the boundaries of the segmented regions, which are labeled with different colors or numbers.  
- The morphological watersheds can be computed using different methods, such as distance transform, gradient magnitude, image smoothing, etc.   
- The morphological watersheds can be implemented using different algorithms, such as flooding, immersion, hierarchical queue, etc.   
- The morphological watersheds can be applied to different types of images, such as grayscale, color, binary, etc.   
- The morphological watersheds have some advantages, such as being robust to noise, preserving thin structures, and being easy to parallelize.   
- The morphological watersheds have some disadvantages, such as being sensitive to markers, producing over-segmentation, and being computationally expensive.   
- The morphological watersheds can be improved by using some techniques, such as marker selection, marker refinement, region merging, post-processing, etc.



# Basic Concepts for the Notes of the Unit 4 - Image Segmentation in the Subject of Image Processing

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, texture, intensity, shape, etc.  
- Image segmentation is useful for many applications, such as medical image analysis, autonomous driving, face recognition, video surveillance, and satellite image analysis.   
- Image segmentation can be classified into two types: semantic segmentation and instance segmentation. 
  - Semantic segmentation assigns a class label to each pixel in the image, such as sky, road, car, person, etc. Semantic segmentation does not distinguish between different objects of the same class. 
  - Instance segmentation assigns a class label and an instance identifier to each pixel in the image, such as car1, car2, person1, person2, etc. Instance segmentation can separate different objects of the same class. 
- Image segmentation can be performed using various techniques, such as thresholding, clustering, region growing, edge detection, graph-based methods, deep learning, etc.   
  - Thresholding is a simple technique that divides the image into foreground and background based on a predefined intensity value. 
  - Clustering is a technique that groups pixels with similar features, such as color, texture, intensity, etc. into clusters or segments. 
  - Region growing is a technique that starts from a seed pixel and expands the region by adding neighboring pixels that satisfy some similarity criteria. 
  - Edge detection is a technique that finds the boundaries or contours of the objects in the image by detecting the changes in intensity or gradient. 
  - Graph-based methods are techniques that model the image as a graph, where the nodes are pixels and the edges are the similarity or dissimilarity between pixels. Graph-based methods partition the graph into segments using some criteria, such as minimum cut, normalized cut, etc. 
  - Deep learning is a technique that uses neural networks to learn the features and the segmentation function from the data. Deep learning can achieve state-of-the-art results for both semantic and instance segmentation.



# Dam construction for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Dam construction is a morphological approach to image segmentation that is based on the concept of watershed segmentation .
- Watershed segmentation is a technique that treats an image as a topographic surface, where the intensity of each pixel represents its height, and segments the image into different regions corresponding to the catchment basins of the surface .
- The basic idea of dam construction is to simulate a flooding process on the image surface, where water rises from the local minima (the lowest pixels) and fills the neighboring pixels according to their intensity values .
- When the water from different regions meets, a dam is built to prevent them from merging. These dams are the boundaries of the image segments, and also the boundaries of the catchment basins .
- The dam construction algorithm can be summarized as follows :
  - Compute the gradient magnitude of the image using an edge operator, such as Sobel, to enhance the edges and reduce the noise.
  - Label the local minima of the gradient image as different regions, and assign them a unique label.
  - Initialize a priority queue with the labeled pixels, sorted by their intensity values.
  - Repeat until the queue is empty:
    - Pop the pixel with the lowest intensity value from the queue.
    - For each of its unlabeled neighbors, assign them the same label as the current pixel, and push them to the queue.
    - If the neighbor has a different label than the current pixel, mark the current pixel as a boundary pixel, and do not push the neighbor to the queue.
  - Output the labeled image and the boundary image as the segmentation result.
- The dam construction algorithm can segment images into meaningful regions, but it may also suffer from over-segmentation, where too many small regions are produced  .
- To overcome this problem, some post-processing steps can be applied, such as merging regions based on some criteria, such as size, shape, color, texture, etc  .
- The dam construction algorithm can also be extended to handle different types of images, such as underwater images, by using transfer learning techniques to adapt the model to the target domain.
- The dam construction algorithm is a useful tool for image segmentation, but it also requires careful parameter tuning and post-processing to achieve satisfactory results   .



# Watershed segmentation algorithm

- Watershed segmentation is a classical algorithm used for separating different objects in an image .
- The algorithm treats pixel values as a local topography (elevation), where high intensity denotes peaks and hills, and low intensity denotes valleys .
- The algorithm starts from user-defined markers, which are pixels that belong to different regions or objects .
- The algorithm floods basins from the markers until basins attributed to different markers meet on watershed lines, which are the boundaries between the regions .
- The algorithm can be applied to any grayscale image, such as the gradient magnitude of the original image .
- The algorithm can be used for object segmentation purposes, such as counting the objects or for further analysis of the separated objects .
- The algorithm can handle cases where the objects are touching each other, which are difficult for other segmentation methods.
- The algorithm requires careful selection of markers and parameters to avoid over-segmentation or under-segmentation  .
- The algorithm can be implemented using various libraries, such as OpenCV or scikit-image  .



# Unit 5 - IMAGE COMPRESSION AND RECOGNITION

- Image compression is the process of reducing the file size of an image while still trying to preserve the quality of the image.
- Image compression can be lossless or lossy, depending on whether the original image can be exactly reconstructed from the compressed data or not.
- Image compression can be based on traditional methods such as JPEG, PNG, GIF, etc., or on learned methods that use deep neural networks to optimize the compression performance.
- Image recognition is the process of identifying and classifying objects, faces, scenes, etc. in an image using machine learning algorithms.
- Image recognition can be based on handcrafted features such as SIFT, SURF, HOG, etc., or on learned features that use deep neural networks to extract high-level semantic information from the image.
- Image recognition can be applied to various tasks such as classification, object detection, face recognition, segmentation, superresolution, etc.
- Image compression and recognition are related in the sense that both involve processing and encoding images in a compact and efficient way.
- Image compression and recognition can also be jointly learned and optimized, such that the compressed image can be directly used as an input to a recognition network, without the need for decompression .
- Image compression and recognition can benefit from each other, as compression can reduce the computational cost and storage requirement of recognition, and recognition can improve the perceptual quality and task-specific performance of compression .



# Need for data compression for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Data compression is a technique that reduces the amount of space needed to store or transmit digital data, such as images.
- Image compression is a type of data compression applied to digital images, to reduce their cost for storage or transmission.
- Image compression is important for several reasons, such as:
  - Saving disk space and memory for storing more images or other data.
  - Reducing bandwidth and time for transmitting images over networks or the internet.
  - Enhancing the performance and efficiency of image processing applications, such as recognition, analysis, or editing.
  - Preserving the quality and fidelity of images while reducing their size.
- Image compression can be classified into two categories: lossless and lossy .
  - Lossless compression algorithms reduce the size of images without losing any information in the images, which means that the original images can be reconstructed from the compressed images without any distortion or degradation.
  - Lossy compression algorithms reduce the size of images by discarding some information in the images, which means that the original images cannot be reconstructed from the compressed images without some loss of quality or accuracy.
  - Lossless compression algorithms are suitable for images that require high precision and detail, such as medical or scientific images.
  - Lossy compression algorithms are suitable for images that can tolerate some degradation and distortion, such as natural or artistic images.
- Image compression techniques can be based on different methods, such as:
  - Image transform: a mathematical function that maps an image from one domain (vector space) to another domain (other vector space), where the image can be represented more compactly or efficiently.
  - Quantization: a process that reduces the number of levels or values that represent an image, such as the number of colors or shades of gray.
  - Encoding: a process that assigns codes or symbols to the values or sequences of values that represent an image, such as binary or hexadecimal codes.
- Image compression techniques can be evaluated based on different criteria, such as:
  - Compression ratio: the ratio of the size of the original image to the size of the compressed image, which indicates the degree of compression achieved.
  - Bit rate: the number of bits required to represent one pixel of an image, which indicates the amount of information contained in an image.
  - Quality: the measure of how well the compressed image preserves the visual appearance and features of the original image, which can be subjective or objective.
  - Complexity: the measure of how much computation and memory are required to perform the compression and decompression algorithms, which affects the speed and efficiency of the image processing system.



# Huffman Coding for Image Compression

Huffman coding is a lossless data compression technique that assigns variable-length codes to the symbols based on their frequencies of occurrence. It is one of the basic compression methods that have proven useful in image and video compression standards.

## Steps of Huffman Coding for Image Compression

1. Analyze the pixel values or the output of an intensity mapping function of the image and calculate their probabilities.
2. Sort the symbols in ascending order of their probabilities and create a series of source reductions by combining the two lowest probability symbols into a single symbol that replaces them in the next source reduction.
3. Construct a binary tree with the symbols as the leaves and the combined symbols as the internal nodes. The root node represents the entire source. Assign 0 and 1 to the two branches of each node.
4. Generate the Huffman codes by traversing the tree from the root to the leaves and concatenating the branch labels along the path.
5. Encode the image by replacing each symbol with its corresponding Huffman code.
6. Decode the image by using the Huffman tree or a lookup table to map each code back to its original symbol.

## Example of Huffman Coding for Image Compression

Consider a 4x4 grayscale image with the following pixel values:

| 15 | 15 | 15 | 15 |
| -- | -- | -- | -- |
| 15 | 15 | 15 | 15 |
| 15 | 15 | 15 | 15 |
| 15 | 15 | 15 | 15 |

The probabilities of the symbols are:

| Symbol | Probability |
| ------ | ----------- |
| 15     | 1.0         |

The Huffman tree for this image is:

```
  15
 /  \
0    1
```

The Huffman code for the symbol 15 is 0 or 1 (both are equivalent). The encoded image is:

| 0 | 0 | 0 | 0 |
| - | - | - | - |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |
| 0 | 0 | 0 | 0 |

The decoded image is the same as the original image. The compression ratio is 4:1, since each pixel is represented by one bit instead of four bits.

## Advantages and Disadvantages of Huffman Coding for Image Compression

Some of the advantages of Huffman coding are:

- It is optimal, meaning that no other lossless compression method can achieve a better compression ratio for the same source.
- It is simple and easy to implement.
- It is widely used in various image and video compression standards, such as JPEG, MPEG, and PNG.

Some of the disadvantages of Huffman coding are:

- It requires a priori knowledge of the source statistics or a separate transmission of the Huffman tree or table.
- It is not efficient for sources with non-integer or large alphabet sizes, such as continuous-tone images.
- It is sensitive to noise and errors in the transmission channel.



# Run Length Encoding

- Run Length Encoding (RLE) is a form of lossless data compression in which runs of data (sequences in which the same data value occurs in many consecutive data elements) are stored as a single data value and count, rather than as the original run.
- RLE is most efficient on data that contains many such runs, for example, simple graphic images such as icons, line drawings, Conway's Game of Life, and animations.
- RLE compression algorithm works as follows :
  - For each row of pixels in the image, check for the consecutive runs of the current pixel value.
  - Replace each run with a pair of numbers: the length of the run and the pixel value.
  - For example, the first row of the image below contains 3 white pixels, 2 red pixels, 5 white pixels, 2 red pixels, then 4 white pixels:

  image

  - The RLE representation of this row would be: 3 0 2 1 5 0 2 1 4 0, where 0 represents white and 1 represents red.
  - Repeat this process for each row of the image and concatenate the results to get the final RLE representation of the image.
- RLE has some advantages and disadvantages:
  - Advantages:
    - It is simple and easy to implement.
    - It can achieve high compression ratios for images with large areas of uniform color or repeated patterns.
    - It preserves the original quality of the image without any loss of information.
  - Disadvantages:
    - It is not effective for images with complex details or many color variations.
    - It can increase the size of the image if there are few runs or many single pixels.
    - It does not take advantage of any spatial or frequency correlations in the image.



# Shift codes for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Image compression is the process of reducing the amount of data required to represent an image, without compromising its quality or information content.
- Image compression can be classified into two types: lossless and lossy.
- Lossless image compression preserves the exact pixel values of the original image, and allows perfect reconstruction of the image after decompression.
- Lossy image compression discards some of the pixel values of the original image, and introduces some distortion or error in the reconstructed image after decompression.
- Lossy image compression can achieve higher compression ratios than lossless image compression, but at the cost of image quality.
- Shift coding is a technique for lossless image compression, based on the idea of shifting the pixel values of an image by a certain amount, and then encoding the shifted values using a variable-length code, such as Huffman coding.
- Shift coding can exploit the spatial correlation and redundancy in an image, and reduce the entropy or average number of bits per pixel of the image.
- Shift coding can be applied in two ways: using a leading short word (LSW) or using a lead bit (LB).
- LSW shift coding shifts the pixel values of an image by the minimum value in the image, and then encodes the shifted values using a variable-length code that assigns shorter codes to smaller values.
- LB shift coding shifts the pixel values of an image by the most significant bit (MSB) of the maximum value in the image, and then encodes the shifted values using a variable-length code that assigns shorter codes to values with fewer bits.
- Shift coding can achieve better compression performance than other lossless image compression techniques, such as run-length encoding (RLE) or Lempel-Ziv-Welch (LZW) coding, for images with low dynamic range or high spatial correlation.



# Arithmetic coding for image compression

Arithmetic coding is a lossless compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence. Unlike Huffman coding, which assigns codes to individual symbols, arithmetic coding encodes the entire message into a single fraction between 0 and 1.

The main steps of arithmetic coding are:

- Define a probability model for the source symbols. This can be static (fixed for the entire message) or adaptive (updated after each symbol).
- Initialize an interval [low, high) to [0, 1).
- For each symbol in the message, do the following:
  - Divide the interval into subintervals proportional to the symbol probabilities.
  - Narrow the interval to the subinterval corresponding to the current symbol.
  - If the interval becomes too small, output some bits and rescale the interval.
- Output the final interval as the code for the message.

Arithmetic coding can be applied to image compression by encoding the pixels or the coefficients of a transform (such as DCT) of the image. The probability model can be based on the pixel values, the neighboring pixels, or the previous coefficients. The advantage of arithmetic coding is that it can achieve near-optimal compression ratios, especially for skewed or small alphabets. The disadvantage is that it is more complex and slower than Huffman coding, and it is more sensitive to errors or loss of synchronization.



# JPEG standard

- JPEG stands for Joint Photographic Experts Group, which was a group of image processing experts that devised a standard for compressing images (ISO) .
- JPEG is not really a file format but rather an image compression standard . The JPEG standard specifies the codec, which defines how an image is compressed into a stream of bytes and decompressed back into an image.
- JPEG is a lossy image compression method, which means that some information is discarded during the compression process, resulting in a loss of quality .
- JPEG compression works by averaging color variation and blocking together groups of pixels with a more uniform color, so that it doesn’t have to store as many different ones .
- JPEG compression involves the following steps :
  - Convert the image from RGB to YCbCr color space, which separates the luminance (Y) from the chrominance (Cb and Cr) components.
  - Subsample the chrominance components to reduce their resolution, since the human eye is less sensitive to color details than brightness details.
  - Divide the image into 8x8 blocks of pixels and apply a discrete cosine transform (DCT) to each block, which converts the spatial domain into the frequency domain.
  - Quantize the DCT coefficients using a quantization matrix, which assigns smaller values to higher frequencies and larger values to lower frequencies. This reduces the number of bits needed to represent the coefficients, but also introduces errors due to rounding.
  - Encode the quantized coefficients using a variable-length coding scheme, such as Huffman coding or arithmetic coding, which assigns shorter codes to more frequent coefficients and longer codes to less frequent coefficients. This further reduces the file size, but also adds some overhead for the code table.
  - Optionally, add some metadata to the compressed file, such as the Exif or JFIF standards, which define the file format and contain information about the image, such as the resolution, orientation, date, etc.

- JPEG compression allows the user to adjust the level of compression and quality by changing the quantization matrix or the subsampling ratio . Higher compression leads to smaller file size but lower quality, and vice versa.
- JPEG compression is suitable for natural images, such as photographs, that have smooth variations of color and brightness . However, it is not suitable for images that have sharp edges, text, or graphics, as it may introduce artifacts, such as blocking, ringing, or blurring .



# MPEG

MPEG stands for Moving Picture Experts Group, which is a group of experts that develops standards for digital video and audio compression. MPEG standards aim to achieve high compression ratios by reducing the amount of redundant or irrelevant information in the data  .

Some of the main concepts and techniques used by MPEG standards are:

- **Frames**: A video is composed of a sequence of frames, which are still images that represent the state of the scene at a given time. Each frame has a certain number of pixels, which are the smallest units of color and brightness information. The more pixels a frame has, the higher its resolution and quality, but also the larger its size.
- **Temporal redundancy**: Many frames in a video are similar or identical to each other, especially if the scene is static or the motion is slow. This means that there is a lot of repeated information that can be eliminated or reduced without affecting the perception of the video. MPEG standards exploit this temporal redundancy by storing only the changes from one frame to another, instead of each entire frame .
- **Spatial redundancy**: Within a frame, there may be regions that have the same or similar color and brightness values, such as a uniform background or a smooth surface. This means that there is a lot of information that can be approximated or simplified without affecting the quality of the image. MPEG standards exploit this spatial redundancy by dividing the frame into smaller blocks of pixels, and applying a mathematical transformation called Discrete Cosine Transform (DCT) to each block. DCT converts the pixel values into a set of coefficients that represent the frequency and amplitude of the variations in the block. The coefficients that have low frequency and low amplitude are discarded or quantized, as they are less noticeable to the human eye .
- **Chroma subsampling**: The human eye is more sensitive to changes in brightness than changes in color. This means that the color information in an image can be reduced without affecting the visual quality. MPEG standards use a technique called chroma subsampling, which separates the brightness information from the color information, and reduces the resolution of the color information by averaging or discarding some of the pixels.

These techniques allow MPEG standards to achieve a compression ratio of about 52:1, which means that a video file can be reduced to about 2% of its original size. However, this also means that some information is lost in the process, which may result in artifacts or distortions in the compressed video. Therefore, MPEG standards are considered lossy compression methods, as they trade off quality for size.



# Boundary representation

Boundary representation is a method for representing a 3D shape by defining the limits of its volume. A solid is represented as a collection of connected surface elements, which define the boundary between interior and exterior points.

Some of the topics related to boundary representation in image processing are:

- Boundary extraction: This is the process of finding the boundary line or location dividing the two surfaces in an image. It can help to gain information and understand the feature of an image .
- Boundary encoding: This is the process of representing the boundary of an image region by a sequence of codes that describe the direction and length of the boundary segments. It can help to reduce the storage space and facilitate the manipulation of the boundary.
- Boundary approximation: This is the process of simplifying the boundary of an image region by using fewer segments or points to represent it. It can help to reduce the noise and complexity of the boundary.
- Boundary description: This is the process of characterizing the boundary of an image region by using some features or measures that describe its shape, size, orientation, curvature, etc. It can help to classify and recognize the image region.



# Boundary description for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Image compression is the process of reducing the amount of data required to represent an image, while preserving the quality and information content as much as possible.
- Image recognition is the process of identifying and classifying objects, faces, scenes, or activities in an image, using various techniques such as feature extraction, machine learning, or deep learning.
- The notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing cover the following topics:

  - The need and benefits of image compression, such as saving storage space, bandwidth, and transmission time, and enhancing security and privacy.
  - The types and characteristics of image compression, such as lossless and lossy compression, and their trade-offs between compression ratio, quality, and complexity.
  - The common image compression standards and algorithms, such as JPEG, JPEG 2000, PNG, GIF, and TIFF, and their advantages and disadvantages.
  - The principles and methods of image recognition, such as feature extraction, feature matching, feature selection, and feature classification.
  - The applications and challenges of image recognition, such as face recognition, object recognition, scene recognition, and activity recognition, and their issues such as accuracy, robustness, scalability, and security.



# Fourier Descriptor

- Fourier descriptor is a method used in object recognition and image processing to represent the boundary shape of a segment in an image.
- It is based on the Fourier series, which is a mathematical tool to decompose a periodic function into a sum of simple sinusoidal functions.
- The boundary shape of an image segment can be considered as a periodic function, and the coefficients of the Fourier series can be used as the features to describe the shape.
- Fourier descriptor has some advantages over other shape representation methods, such as:
  - It can be designed to be invariant to scaling, translation, rotation and starting point  , which are common transformations in image processing.
  - It can capture both global and local shape information by using different frequency components of the Fourier series.
  - It can reduce the dimensionality of the shape feature vector by selecting only the most significant coefficients of the Fourier series.
- The basic steps to compute the Fourier descriptor of an image segment are:
  - Extract the boundary pixels of the image segment and store them in a complex vector, where the real and imaginary parts are the x and y coordinates of the pixels.
  - Apply the discrete Fourier transform (DFT) to the complex vector and obtain another complex vector, which contains the Fourier coefficients of the boundary function.
  - Normalize the Fourier coefficients to make them invariant to scaling, translation, rotation and starting point, by using the following formulas:

    - Translation invariance: set the first coefficient to zero.
    - Scale invariance: divide all the coefficients by the absolute value of the second coefficient.
    - Rotation invariance: use only the magnitudes of the coefficients and discard the phases.
    - Starting point invariance: shift the coefficients by a certain amount to align the starting point with the first coefficient.

  - Select a subset of the normalized coefficients as the Fourier descriptor, usually the low-frequency ones, which contain the global shape information.
- The Fourier descriptor can be used for shape-based image retrieval, which is the task of finding images that contain similar shapes to a given query image.
- The similarity between two shapes can be measured by the Euclidean distance between their Fourier descriptors, or by other metrics such as cosine similarity or correlation coefficient.
- The Fourier descriptor can also be used for shape classification, which is the task of assigning a label to an image segment based on its shape.
- The shape label can be determined by using a classifier, such as k-nearest neighbors, support vector machines, neural networks, etc., which are trained on a set of labeled shape examples.



# Regional Descriptors

- Regional descriptors are features that describe the properties of a region in an image, such as its shape, color, texture, etc.
- Regional descriptors can be classified into two types: external and internal.
  - External descriptors are based on the boundary or contour of a region, such as perimeter, compactness, orientation, etc.
  - Internal descriptors are based on the pixels inside a region, such as area, mean value, standard deviation, etc.
- Regional descriptors can be used for various purposes, such as image compression, image recognition, image segmentation, etc.
- Some examples of regional descriptors are  :
  - Area: the number of pixels in a region, optionally multiplied by the real area of each pixel.
  - Perimeter: the length of the boundary of a region, optionally weighted by the edge strength or orientation.
  - Compactness: the ratio of the area to the perimeter squared, indicating how close a region is to a circle.
  - Orientation: the angle of the major axis of the best-fitting ellipse to a region, indicating the direction of the region.
  - Mean value: the average intensity or color of the pixels in a region, indicating the brightness or hue of the region.
  - Standard deviation: the measure of the variation of the intensity or color of the pixels in a region, indicating the contrast or saturation of the region.
  - Moments: the weighted averages of the pixel coordinates or intensities in a region, which can be used to compute other descriptors such as centroid, eccentricity, etc.



# Topological feature for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- A topological feature is a property of an image that is invariant under continuous deformations, such as stretching, twisting, or bending .
- Examples of topological features are the number of connected components, the number of holes, the Euler number, the genus, and the Betti numbers .
- Topological features can be used to describe the shape and structure of objects in images, and to distinguish different classes of objects  .
- Topological features can be extracted from binary images using methods based on combinatorial homology theory, which is a branch of mathematics that studies the abstract properties of shapes .
- Combinatorial homology theory uses concepts such as simplices, complexes, chains, boundaries, cycles, and homology groups to define and compute topological features .
- One of the advantages of using combinatorial homology theory is that it can handle noisy or incomplete images, and it can deal with different types of connectivity (4-, 8-, or n-connectivity) in digital images .
- One of the challenges of using combinatorial homology theory is that it requires a lot of computation and memory, and it can be difficult to implement efficiently .
- Topological features can be used for various applications in image processing and computer vision, such as object detection, segmentation, classification, recognition, matching, retrieval, and flow estimation  .
- Topological features can complement other types of features, such as geometric, color, texture, or deep learning features, to provide more robust and accurate results .
- Topological features can also be combined with other methods, such as graph theory, machine learning, or convolutional neural networks, to enhance the performance and interpretability of the algorithms .



# Texture

- Texture is a property of an image that describes the spatial arrangement of color or intensity values in a local neighborhood.
- Texture can be used to characterize the surface quality of an object, such as roughness, smoothness, coarseness, etc.
- Texture can also be used to segment images into regions of interest, such as foreground and background, or different types of materials, such as wood, metal, fabric, etc.
- Texture analysis is the process of extracting features from an image that capture the texture information.
- Texture synthesis is the process of generating new images that have the same or similar texture as a given sample image.
- Texture analysis and synthesis have many applications in computer vision, such as image compression, image enhancement, image inpainting, image retrieval, image classification, etc.

: Image texture - Wikipedia
: Texture synthesis - Wikipedia
: What Is Texture Analysis In Computer Vision? - Analytics India Magazine
: Image Processing: Dealing with Texture, 2nd Edition | Wiley



# Patterns and Pattern Classes

- A pattern is an arrangement of descriptors, which are numerical or symbolic attributes that characterize an object or an event .
- A descriptor is also called a feature in the pattern recognition literature.
- A pattern class is a family of patterns that share some common properties .
- Pattern classes are denoted by ω1, ω2, ..., ωW, where W is the number of classes.
- The goal of pattern recognition is to assign patterns to their classes with as little human interaction as possible .
- Pattern recognition is an information-reduction process: the assignment of visual or logical patterns to classes based on the features of these patterns and their relationships.
- Pattern recognition uses image processing techniques for analyzing, enhancing, compressing, and reconstructing images .
- Pattern recognition also uses machine learning algorithms for automatic recognition of patterns and irregularities in data.
- Three common pattern arrangements used in practice are vectors (for quantitative descriptions), strings (for sequential descriptions), and trees (for hierarchical descriptions) .
- Pattern vectors are ordered sets of numerical or symbolic values that represent the features of a pattern .
- Pattern strings are sequences of symbols that represent the structure of a pattern .
- Pattern trees are graphs that represent the hierarchical relationships among the components of a pattern .
- An example of a pattern vector is the RGB color values of a pixel in an image .
- An example of a pattern string is the DNA sequence of a gene .
- An example of a pattern tree is the parse tree of a sentence .



# Recognition based on matching

- Recognition based on matching is a technique of image processing that aims to find and identify objects or regions in an image that match a given template or pattern.
- Matching can be performed at different levels of abstraction, such as pixel-level, feature-level, or semantic-level.
- Matching can also be classified into two types: exact matching and inexact matching.
  - Exact matching requires the template and the target to be identical in shape, size, orientation, and appearance.
  - Inexact matching allows for some variations or distortions between the template and the target, such as noise, occlusion, scaling, rotation, or illumination changes.
- Some of the applications of recognition based on matching are:
  - Computer vision, such as face recognition, object detection, and scene understanding.
  - Moving target tracking and recognition, such as surveillance, security, and military.
  - Motion compensation in sequence image compression, such as video coding and transmission.
  - Medical image processing, such as diagnosis, surgery, and registration.
- Some of the algorithms or methods for recognition based on matching are:
  - Template matching, which compares the template with every possible location in the image and measures the similarity or dissimilarity using a metric, such as cross-correlation, sum of squared differences, or normalized cross-correlation.
  - Feature-based matching, which extracts salient features from the template and the image, such as edges, corners, keypoints, or descriptors, and matches them using a criterion, such as distance, ratio, or consensus.
  - Semantic-based matching, which uses high-level knowledge or context to infer the meaning or category of the template and the image, such as labels, attributes, or ontologies.
  - Optimization-based matching, which formulates the matching problem as an optimization problem and uses a technique, such as genetic algorithm, simulated annealing, or gradient descent, to find the optimal solution.

