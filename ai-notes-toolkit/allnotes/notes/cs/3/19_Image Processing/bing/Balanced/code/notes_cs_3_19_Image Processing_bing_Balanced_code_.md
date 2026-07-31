

## Unit 1 - DIGITAL IMAGE FUNDAMENTALS

- A digital image is a representation of a two-dimensional image as a finite set of digital values, called pixels.
- Pixels are the smallest individual element of an image, holding values that represent the brightness of a given color at any specific point.
- A digital image can be created by a variety of sources, such as a digital camera, a scanner, a computer graphics program, or a medical imaging device.
- A digital image can be stored, processed, and displayed using different formats, such as bitmap, JPEG, PNG, GIF, or TIFF.
- A digital image can be characterized by its spatial resolution, which is the number of pixels in each dimension, and its color depth, which is the number of bits used to represent each pixel.
- A digital image can be manipulated by various operations, such as cropping, resizing, rotating, filtering, enhancing, or compressing.
- A digital image can be analyzed by various techniques, such as edge detection, segmentation, feature extraction, pattern recognition, or face recognition.



### Steps in Digital Image Processing

Digital image processing is the process of manipulating digital images using computer algorithms. It can be used for various purposes, such as enhancing, restoring, analyzing, compressing, and transmitting images. The following are the basic steps involved in digital image processing:

- **Image acquisition**: This involves capturing an image using a digital camera or scanner, or importing an existing image into a computer. The image is then converted into a digital format, such as pixels, using an analog-to-digital converter. The image may also undergo some preprocessing, such as filtering, cropping, resizing, or color correction.
- **Image enhancement**: This involves improving the visual quality of an image, such as increasing contrast, reducing noise, and removing artifacts. The goal of image enhancement is to make the image more suitable for a specific application or task, such as human perception, object detection, or feature extraction.
- **Image restoration**: This involves removing degradation from an image, such as blurring, noise, and distortion. The goal of image restoration is to recover the original image as much as possible, using some prior knowledge or model of the degradation process. Image restoration can be seen as a special case of image enhancement, where the enhancement is based on a specific degradation model.
- **Image segmentation**: This involves dividing an image into meaningful regions or segments, based on some criteria, such as color, intensity, texture, or shape. The goal of image segmentation is to simplify the image representation and facilitate the analysis of the image content. Image segmentation can be used for various applications, such as object recognition, face detection, medical imaging, and image compression.
- **Image representation and description**: This involves extracting features or attributes from the segmented image regions, such as shape, size, orientation, color, texture, or boundary. The goal of image representation and description is to represent the image content in a compact and meaningful way, using some data structures, such as vectors, matrices, graphs, or histograms. Image representation and description can be used for various applications, such as image classification, image retrieval, image matching, and image synthesis.
- **Image recognition and interpretation**: This involves assigning labels or meanings to the image regions or features, based on some rules, models, or algorithms. The goal of image recognition and interpretation is to understand the image content and infer some information or knowledge from it. Image recognition and interpretation can be used for various applications, such as face recognition, optical character recognition, scene understanding, and image captioning.
- **Image compression and transmission**: This involves reducing the size of the image data, using some techniques, such as encoding, quantization, or transformation. The goal of image compression and transmission is to store or transmit the image data efficiently, without losing much information or quality. Image compression and transmission can be used for various applications, such as web browsing, video streaming, and satellite communication.



### Components for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- Digital image processing is the manipulation of digital images using computer algorithms and software. It can be used for various purposes, such as enhancing, restoring, analyzing, compressing, and transmitting images.
- Digital image fundamentals are the basic concepts and principles that underlie the representation and processing of digital images. They include the following topics   :

  - Elements of visual perception: This covers how the human visual system perceives and interprets images, such as brightness, contrast, color, and spatial resolution.
  - Light and the electromagnetic spectrum: This explains the physical nature of light and its interaction with matter, such as reflection, refraction, absorption, and emission. It also introduces the concept of wavelength and frequency, and how they relate to the visible and invisible parts of the electromagnetic spectrum.
  - Image sensing and acquisition: This describes the devices and methods that capture and convert images into digital form, such as cameras, scanners, and sensors. It also covers the factors that affect the quality and resolution of images, such as sampling, quantization, noise, and distortion.
  - Image sampling and quantization: This explains the process of converting a continuous image into a discrete image, by dividing it into a grid of pixels and assigning each pixel a numerical value. It also discusses the trade-offs between the spatial and intensity resolution of images, and how they affect the image size and quality.
  - Basic relationships between pixels: This introduces the concepts of pixel neighborhoods, adjacency, connectivity, distance, and regions, and how they can be used to define and manipulate the spatial structure and content of images.
  - Image transformations: This covers the mathematical operations that can be applied to images to change their appearance, such as scaling, rotation, translation, shearing, and warping. It also introduces the concept of geometric and intensity transformations, and how they can be represented by matrices and functions.
  - Image enhancement: This involves improving the visual quality of an image, such as increasing contrast, reducing noise, and removing artifacts. It also covers the techniques and methods that can be used for image enhancement, such as histogram equalization, filtering, sharpening, and smoothing.
  - Image restoration: This involves recovering an image that has been degraded by some factors, such as blurring, noise, or distortion. It also covers the techniques and methods that can be used for image restoration, such as deconvolution, inverse filtering, and regularization.
  - Image analysis: This involves extracting useful information from an image, such as features, edges, contours, and regions. It also covers the techniques and methods that can be used for image analysis, such as segmentation, edge detection, feature extraction, and pattern recognition.
  - Image compression: This involves reducing the size of an image without losing too much information, such as quality, resolution, and content. It also covers the techniques and methods that can be used for image compression, such as lossy and lossless compression, entropy coding, and transform coding.
  - Image transmission: This involves sending and receiving images over a communication channel, such as a network or a wireless link. It also covers the factors that affect the performance and reliability of image transmission, such as bandwidth, latency, and error control.



### Elements of Visual Perception

Visual perception is the process of interpreting and understanding visual information received by the eyes. Visual perception is influenced by both physical and psychological factors. Visual perception is important for image processing, as it helps to design and evaluate techniques that enhance, restore, or analyze images.

The basic elements of visual perception are:

- **Structure of the eye**: The eye is the organ that captures light and converts it into electrical signals that are sent to the brain. The eye consists of several parts, such as the cornea, the iris, the pupil, the lens, the retina, the optic nerve, and the fovea. The retina is the inner layer of the eye that contains photoreceptor cells called rods and cones. Rods are sensitive to low light levels and provide black-and-white vision, while cones are sensitive to high light levels and provide color vision. The fovea is the central region of the retina that has the highest concentration of cones and provides the sharpest vision.
- **Image formation in the eye**: The image formed on the retina is inverted and reduced in size compared to the original scene. The image is also distorted by optical aberrations, such as spherical aberration, chromatic aberration, and astigmatism. These aberrations cause blurring, color fringing, and shape distortion of the image. The image quality also depends on the pupil size, which regulates the amount of light entering the eye. The pupil size is controlled by the iris, which contracts or dilates in response to the light intensity. The pupil size affects the depth of field, which is the range of distances that are in focus. A smaller pupil size increases the depth of field, while a larger pupil size decreases it.
- **Brightness adaptation and discrimination**: The eye can adapt to a wide range of light levels, from bright sunlight to dim starlight. The eye achieves this by adjusting the sensitivity of the rods and cones, as well as the pupil size. Brightness adaptation is the process of adjusting the overall sensitivity of the eye to the average light level. Brightness discrimination is the ability to detect differences in light intensity between adjacent regions. The eye can discriminate brightness differences better in low light levels than in high light levels. The eye can also perceive brightness differences better for achromatic (gray) stimuli than for chromatic (colored) stimuli.
- **Color perception**: The eye can perceive different colors by comparing the responses of the three types of cones, which have different spectral sensitivities. The cones are most sensitive to red, green, and blue wavelengths of light, respectively. The brain interprets the ratio of the cone responses as a color sensation. Color perception is also influenced by the context, such as the surrounding colors, the illumination, and the memory. For example, the same color may appear different under different light sources, or the same object may appear different colors depending on the background.
- **Spatial perception**: The eye can perceive the spatial properties of objects, such as their size, shape, orientation, position, and motion. Spatial perception is based on the following factors:
  - **Visual acuity**: The ability to resolve fine details in the image. Visual acuity depends on the density and distribution of the photoreceptors, the quality of the optics, and the processing of the brain. Visual acuity is highest at the fovea and decreases towards the periphery of the retina.
  - **Contrast sensitivity**: The ability to detect differences in brightness or color between adjacent regions. Contrast sensitivity depends on the spatial frequency, which is the number of cycles of brightness or color change per degree of visual angle. Contrast sensitivity is highest for medium spatial frequencies and decreases for low and high spatial frequencies.
  - **Visual field**: The extent of the visual scene that can be perceived at a given moment. The visual field is limited by the size and shape of the eye, the position of the eye, and the presence of obstacles. The visual field is divided into two halves, the left and the right, which are processed by the opposite hemispheres of the brain. The visual field is also divided into four quadrants, the upper and the lower, and the nasal and the temporal, which are processed by different regions of the brain. The visual field is wider in the horizontal direction than in the vertical direction, and wider in the temporal direction than in the nasal direction.
  - **Binocular vision**: The ability to perceive depth and distance by combining the images from the two eyes. Binocular vision is based on the principle of stereopsis, which is the perception of depth from the disparity, or the difference, between the images of the same object on the



### Image Sensing and Acquisition

- Image sensing and acquisition is the process of capturing and converting an analog image of a physical scene or object into a digital form that can be processed by a computer.
- Image sensing and acquisition involves three main steps:
  - Illumination: The scene or object is illuminated by a light source, such as the sun, a lamp, or a laser. The light reflects or absorbs by the elements of the scene, creating variations in intensity and color.
  - Sensing: The reflected or absorbed light is detected by an image sensor, such as a camera, a scanner, or a microscope. The image sensor converts the light into electrical signals that represent the intensity and color of each pixel in the image.
  - Digitization: The electrical signals are converted into digital numbers by an analog-to-digital converter (ADC). The digital numbers are stored in a memory device, such as a hard disk, a flash drive, or a cloud server.
- Image sensing and acquisition can be performed for different types of images, such as grayscale, color, binary, multispectral, hyperspectral, infrared, ultraviolet, X-ray, MRI, etc. Each type of image requires a specific image sensor and ADC that can capture and convert the corresponding range of wavelengths and intensities.
- Image sensing and acquisition can be used for various applications, such as photography, video, medical imaging, remote sensing, biometrics, security, surveillance, etc. Each application has different requirements and challenges for image sensing and acquisition, such as resolution, speed, accuracy, noise, compression, etc.



### Image Sampling and Quantization

- Image sampling and quantization are two important steps in digital image processing that convert a continuous image into a discrete image.
- Sampling is the process of digitizing the spatial coordinates (x and y) of an image. It involves dividing the image into a grid of pixels and assigning each pixel a value that represents the average intensity of the region covered by the pixel.
- Quantization is the process of digitizing the amplitude values (z) of an image. It involves mapping the continuous range of pixel values into a finite number of discrete levels, usually represented by binary bits.
- The quality of a digital image depends on the sampling rate and the quantization level. A higher sampling rate preserves more spatial details, but requires more memory and processing power. A higher quantization level preserves more tonal details, but requires more bits per pixel and may introduce quantization errors or artifacts.
- The following figure illustrates the sampling and quantization process for a grayscale image:

Sampling and quantization of a grayscale image

- The original image is a continuous function of x and y, with a continuous range of z values. The sampled image is a discrete function of x and y, with a continuous range of z values. The quantized image is a discrete function of x, y and z, with a finite number of z values. The quantized image can be stored and processed as a matrix of binary numbers.



# Relationships between pixels

- A pixel is the smallest unit of a digital image that can be displayed or manipulated.
- Pixels have coordinates that indicate their position in the image, usually starting from the top-left corner as the origin.
- Pixels can have different values depending on the color space and bit depth of the image, such as grayscale, RGB, CMYK, etc.
- Pixels can have different relationships with each other based on their spatial proximity and connectivity.
- Spatial proximity refers to how close two pixels are in terms of their coordinates, such as horizontal, vertical, or diagonal distance.
- Connectivity refers to how two pixels are linked by a path of pixels that share the same value or property, such as intensity, color, or region.
- There are different types of connectivity that can be defined for pixels, such as 4-connectivity, 8-connectivity, and m-connectivity .
  - 4-connectivity: Two pixels are 4-connected if they are horizontal or vertical neighbors, that is, they share an edge. The 4-neighbors of a pixel p are denoted by N4(p) and have the coordinates (x+1,y), (x-1,y), (x,y+1), and (x,y-1), where (x,y) are the coordinates of p.
  - 8-connectivity: Two pixels are 8-connected if they are horizontal, vertical, or diagonal neighbors, that is, they share an edge or a corner. The 8-neighbors of a pixel p are denoted by N8(p) and have the coordinates (x+1,y), (x-1,y), (x,y+1), (x,y-1), (x+1,y+1), (x-1,y+1), (x+1,y-1), and (x-1,y-1), where (x,y) are the coordinates of p.
  - m-connectivity: Two pixels are m-connected if they satisfy a specific condition that depends on the image and the application. For example, two pixels can be m-connected if they have the same intensity value, or if they belong to the same region or object.
- The relationships between pixels can be used to define and analyze the properties and features of digital images, such as regions, boundaries, edges, shapes, textures, etc.
- The relationships between pixels can also be used to perform various operations and transformations on digital images, such as filtering, segmentation, morphological processing, etc.



### Color image fundamentals

- Color is a powerful descriptor that often simplifies object identification and extraction from a scene .
- Color image processing is divided into two major areas: full-color and pseudo-color processing.
  - Full-color processing: the images are acquired with a full-color sensor, such as a color TV camera or color scanner. The images have three components, usually red, green and blue (RGB), that represent the color information at each pixel .
  - Pseudo-color processing: the images are acquired with a single sensor, such as a monochrome camera or scanner. The images have one component that represents the intensity or gray level at each pixel. A color transformation function is applied to assign a color to each intensity value, resulting in a color image .
- Color images can be represented and manipulated using different color models or spaces, such as RGB, CMYK, HSV, HSI, etc .
  - A color model is an abstract mathematical representation of colors in terms of intensity values. A color model uses a three-dimensional coordinate system to specify a color .
  - A color space is a specific instance of a color model, with a defined range of values for each component and a standard for interpreting those values .
  - Different color models and spaces have different advantages and disadvantages for different applications, such as image display, printing, compression, segmentation, etc .
- Color image processing involves various techniques and operations, such as color transformation, color enhancement, color segmentation, color edge detection, color feature extraction, color compression, etc .
  - Color transformation: changing the color representation of an image from one color space to another, such as RGB to CMYK or HSV .
  - Color enhancement: improving the appearance or quality of an image by modifying its color components, such as contrast, brightness, saturation, hue, etc .
  - Color segmentation: dividing an image into regions or objects based on their color similarity or difference .
  - Color edge detection: finding the boundaries or contours of objects or regions in an image based on their color discontinuity or gradient .
  - Color feature extraction: extracting meaningful information or characteristics from an image based on its color components, such as color histogram, color moments, color texture, etc .
  - Color compression: reducing the size or bandwidth of an image by removing or encoding its color information, such as JPEG, GIF, PNG, etc .



### RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two color models used in digital image processing to represent colors in images.
- RGB stands for red, green, blue. It is an additive color model, meaning that red, green, and blue light are added together in varying proportions to produce an extensive range of colors.
- HSI stands for hue, saturation, intensity. It is a color model that represents colors similarly how the human eye senses colors. Hue is the dominant wavelength of the color, saturation is the purity of the color, and intensity is the brightness of the color.
- The RGB color model is based on a Cartesian coordinate system, where each color is represented by a point in a 3D space. The origin (0,0,0) corresponds to black, and the point (255,255,255) corresponds to white. The three axes correspond to the red, green, and blue components of the color.
- The HSI color model is based on a cylindrical coordinate system, where each color is represented by an angle (hue), a distance from the origin (saturation), and a height (intensity). The hue ranges from 0 to 360 degrees, the saturation ranges from 0 to 1, and the intensity ranges from 0 to 255.
- The RGB color model is more suitable for hardware devices, such as monitors, scanners, and cameras, that use red, green, and blue light sources or sensors. The HSI color model is more suitable for image processing applications, such as color enhancement, segmentation, and recognition, that require human perception of colors .
- To convert an RGB pixel to an HSI pixel, the following formulas can be used:

  - Hue: H = arccos((0.5 * ((R - G) + (R - B))) / sqrt(((R - G)^2) + ((R - B) * (G - B))))
  - Saturation: S = 1 - (3 / (R + G + B)) * min(R, G, B)
  - Intensity: I = (1 / 3) * (R + G + B)

- To convert an HSI pixel to an RGB pixel, the following formulas can be used:

  - If 0 <= H < 120 degrees, then R = I * (1 + (S * cos(H)) / cos(60 - H)), G = I * (1 - S), B = I * (1 - (S * cos(H + 60)) / cos(180 - H))
  - If 120 <= H < 240 degrees, then R = I * (1 - S), G = I * (1 + (S * cos(H - 120)) / cos(180 - H)), B = I * (1 - (S * cos(H - 60)) / cos(300 - H))
  - If 240 <= H < 360 degrees, then R = I * (1 - (S * cos(H - 240)) / cos(300 - H)), G = I * (1 - (S * cos(H - 180)) / cos(420 - H)), B = I * (1 + (S * cos(H - 300)) / cos(60 - H))



### Two-dimensional mathematical preliminaries for digital image processing

- A digital image is an image composed of picture elements, also known as pixels, each with finite, discrete quantities of numeric representation for its intensity or gray level that is an output from its two-dimensional functions fed as input by its spatial coordinates denoted with x, y on the x-axis and y-axis, respectively.
- A digital image can be represented as a two-dimensional function, F(x,y), where x and y are spatial coordinates, and the amplitude of F at any pair of coordinates (x,y) is called the intensity or gray level of that image at that point.
- A digital image can be considered as a two-dimensional signal, and can be processed by using two-dimensional signal processing techniques.
- Some basic concepts and operations related to two-dimensional signals and systems are:
  - Linear and nonlinear systems: A system is linear if it satisfies the superposition principle, that is, the output of the system for a linear combination of inputs is equal to the same linear combination of the outputs for each input. A system is nonlinear if it does not satisfy this property.
  - Shift-invariant and shift-variant systems: A system is shift-invariant if the output of the system does not change when the input is shifted by any amount. A system is shift-variant if the output of the system changes when the input is shifted by any amount.
  - Convolution: Convolution is a mathematical operation that describes the output of a linear and shift-invariant system in terms of the input and the impulse response of the system. Convolution can be performed in the spatial domain or in the frequency domain, using the Fourier transform.
  - Correlation: Correlation is a measure of similarity between two signals. Correlation can be used to detect the presence of a known pattern or template in an image, or to measure the degree of alignment or registration between two images.
  - Sampling and quantization: Sampling is the process of converting a continuous signal into a discrete signal by taking samples at regular intervals. Quantization is the process of converting a continuous amplitude range into a finite number of discrete levels. Sampling and quantization are necessary steps for digital image acquisition and representation.
  - Image enhancement: Image enhancement is the process of improving the visual quality or the interpretability of an image by modifying its intensity or color values. Image enhancement can be performed in the spatial domain or in the frequency domain, using various filters or transformations.
  - Image reconstruction: Image reconstruction is the process of recovering an image from its projections or measurements, such as X-ray, MRI, or CT scans. Image reconstruction can be performed by using various algorithms, such as back-projection, filtered back-projection, or iterative methods.



# 2D transforms for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- 2D transforms are mathematical operations that change the position, size, orientation, or shape of an image or a graphical object on a 2D plane.
- 2D transforms are useful for image processing tasks such as filtering, enhancement, compression, restoration, segmentation, and recognition.
- 2D transforms can be classified into two types: spatial domain transforms and frequency domain transforms.
- Spatial domain transforms operate directly on the pixel values of the image, such as translation, scaling, rotation, shearing, reflection, and affine transformation.
- Frequency domain transforms operate on the frequency components of the image, such as Fourier transform, discrete cosine transform, wavelet transform, and discrete sine transform.
- Frequency domain transforms are often used to analyze the global characteristics of the image, such as its energy distribution, periodicity, and orientation.
- Frequency domain transforms can also be used to perform filtering operations in the frequency domain, such as low-pass, high-pass, band-pass, and notch filters.
- Frequency domain transforms can be implemented efficiently using fast algorithms, such as fast Fourier transform (FFT), fast discrete cosine transform (FDCT), and fast wavelet transform (FWT).
- 2D transforms can be represented using matrices, vectors, and complex numbers, depending on the type of the transform and the coordinate system used.
- 2D transforms can be composed by multiplying the matrices or vectors corresponding to each transform, or by adding the complex numbers corresponding to each transform.
- 2D transforms can be inverted by using the inverse matrices, vectors, or complex numbers, or by applying the inverse transform operations in the reverse order.



### DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- DFT stands for Discrete Fourier Transform, which is a technique for transforming a discrete signal into its frequency domain representation.
- DCT stands for Discrete Cosine Transform, which is a technique for transforming a real-valued signal into a sum of cosine functions of different frequencies.
- Both DFT and DCT are useful for image processing, as they can reveal the frequency components of an image, and allow for compression, filtering, enhancement, and other operations in the frequency domain.
- DFT and DCT have some similarities and differences, which are summarized below:

| DFT | DCT |
| --- | --- |
| Can handle complex-valued signals | Can only handle real-valued signals |
| Produces complex-valued coefficients | Produces real-valued coefficients |
| Symmetric with respect to the origin | Even with respect to the origin |
| Has both sine and cosine components | Has only cosine components |
| Better for general spectral analysis | Better for low-frequency content |
| Computed by FFT algorithm | Computed by DCT algorithm or DFT of even extension |

- DFT and DCT can be applied to images by using two-dimensional versions of the transforms, which operate on rows and columns of the image matrix.
- DFT and DCT can be used for image compression by discarding the high-frequency coefficients, which are less perceptible to the human eye, and retaining the low-frequency coefficients, which contain most of the image information.
- DFT and DCT can be used for image enhancement by applying filters in the frequency domain, such as low-pass, high-pass, band-pass, or notch filters, which can remove noise, sharpen edges, or emphasize certain features of the image.



## Unit 2 - IMAGE ENHANCEMENT

- Image enhancement is the process of improving the quality or appearance of an image by modifying its features, such as contrast, brightness, sharpness, noise, etc.
- Image enhancement can be done in two domains: spatial domain and frequency domain.
- Spatial domain methods operate directly on the pixels of the image, such as point processing, histogram processing, spatial filtering, etc.
- Frequency domain methods transform the image into a frequency representation, such as Fourier transform, and then manipulate the frequency components, such as filtering, compression, etc.
- Image enhancement techniques can be classified into two categories: global and local.
- Global techniques apply the same operation to all pixels of the image, such as histogram equalization, contrast stretching, etc.
- Local techniques apply different operations to different regions of the image, such as adaptive histogram equalization, unsharp masking, etc.
- Image enhancement can be used for various applications, such as medical imaging, remote sensing, security, entertainment, etc.



### Spatial Domain

- The spatial domain refers to the 2D image plane represented in terms of pixel intensities.
- Image enhancement in the spatial domain involves modifying the pixel values directly to improve the appearance or quality of the image.
- The spatial domain methods perform operations on pixels directly.
- The most common spatial domain techniques are:
  - Point processing: applying a function to each pixel individually, such as contrast stretching, histogram equalization, thresholding, etc.
  - Neighborhood processing: applying a function to a group of pixels, such as filtering, smoothing, sharpening, edge detection, etc.
  - Global processing: applying a function to the whole image, such as Fourier transform, wavelet transform, etc.
- The spatial domain methods are simple, fast, and intuitive, but they may not be able to handle complex or noisy images well.
- The spatial domain methods can be expressed as:

  `g(x,y) = T[f(x,y)]`

  where `f(x,y)` is the input image, `g(x,y)` is the output image, and `T` is the transformation function that operates on the spatial coordinates `x` and `y`.



### Gray level transformations

- Gray level transformations are methods of image enhancement that modify the pixel values of an image based on a mathematical function.
- The general form of a gray level transformation is s = T(r), where r is the input pixel value, s is the output pixel value, and T is the transformation function.
- The transformation function T can be linear or nonlinear, depending on the desired effect on the image contrast, brightness, or dynamic range.
- Some common types of gray level transformations are:

  - Identity transformation: s = T(r) = r. This transformation does not change the image at all.
  - Negative transformation: s = T(r) = L - 1 - r, where L is the number of gray levels in the image. This transformation produces a negative image, where dark and light regions are reversed.
  - Logarithmic transformation: s = T(r) = c log(1 + r), where c is a constant. This transformation compresses the dynamic range of the image, making dark regions brighter and bright regions darker. It is useful for enhancing details in low-light images or images with high contrast.
  - Power-law transformation: s = T(r) = c r^γ, where c and γ are constants. This transformation can either increase or decrease the contrast of the image, depending on the value of γ. If γ < 1, the transformation is called gamma correction, and it brightens the image. If γ > 1, the transformation is called contrast stretching, and it darkens the image.
  - Piecewise-linear transformation: s = T(r) = a r + b, where a and b are constants that vary for different ranges of r. This transformation allows for more flexibility and control over the image enhancement, as different linear functions can be applied to different regions of the image. Some examples of piecewise-linear transformations are:

    - Contrast stretching: s = T(r) = a r + b, where a > 1 and b < 0. This transformation increases the contrast of the image by expanding the range of pixel values.
    - Thresholding: s = T(r) = 0, if r < T; s = T(r) = L - 1, if r >= T, where T is a threshold value. This transformation converts a gray level image into a binary image, where pixels are either black or white, depending on whether they are below or above the threshold.
    - Clipping: s = T(r) = 0, if r < T1; s = T(r) = L - 1, if r > T2; s = T(r) = r, otherwise, where T1 and T2 are lower and upper limits. This transformation removes the pixel values that are outside a specified range, and preserves the ones that are inside.
    - Gray level slicing: s = T(r) = A, if T1 <= r <= T2; s = T(r) = r, otherwise, where A is a constant value and T1 and T2 are lower and upper limits. This transformation highlights a specific range of pixel values by assigning them a constant value, and leaves the rest of the image unchanged.



### Histogram processing for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Image enhancement is the process of adjusting digital images so that the results are more suitable for display or further image analysis  .
- Histogram processing is a widely used technique for image enhancement that modifies the dynamic range and contrast of an image by altering its intensity histogram  .
- An intensity histogram is a graphical representation of the distribution of pixel values in an image. It shows how many pixels have a certain intensity value, ranging from 0 (black) to 255 (white) for an 8-bit grayscale image.
- Histogram processing can be divided into two categories: histogram equalization and histogram specification.
- Histogram equalization is a technique that transforms the image such that its intensity histogram is approximately uniform, i.e., all intensity values have equal frequencies. This enhances the contrast of the image by spreading out the intensity values over the entire range  .
- Histogram specification is a technique that transforms the image such that its intensity histogram matches a desired histogram, which can be specified by the user or derived from another image. This allows the user to control the contrast and brightness of the image by choosing an appropriate histogram shape.
- Histogram processing can be applied to grayscale or color images. For color images, the histogram can be computed for each color channel separately or for a single luminance channel that represents the brightness of the image.
- Histogram processing can be implemented using the following steps:
  - Compute the histogram of the input image, i.e., count the number of pixels for each intensity value.
  - Compute the cumulative histogram of the input image, i.e., sum the frequencies of all intensity values up to a given value.
  - Normalize the cumulative histogram by dividing each value by the total number of pixels in the image. This gives the probability distribution function (PDF) of the input image.
  - If histogram equalization is desired, use the normalized cumulative histogram as the transformation function that maps each input intensity value to a new output intensity value. This ensures that the output image has a uniform histogram.
  - If histogram specification is desired, compute the normalized cumulative histogram of the desired histogram, which gives the PDF of the desired image. Then, find the inverse transformation function that maps each output intensity value to an input intensity value that has the same PDF. This ensures that the output image has the desired histogram.
  - Apply the transformation function to each pixel of the input image to obtain the output image.
  - Compute the histogram of the output image to verify the result.



# Basics of Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image based on the values of neighboring pixels.
- Spatial filtering can be used for various purposes, such as smoothing, sharpening, edge detection, noise reduction, etc.
- Spatial filtering involves applying a filter or a kernel to an image, which is a small matrix of numbers that defines how the output pixel value is computed from the input pixel values in a neighborhood.
- Spatial filtering can be classified into two types: linear and nonlinear.
- Linear filtering is also known as convolution, which is a mathematical operation that combines two functions to produce a third function. In image processing, convolution is performed by sliding the filter over the image and multiplying the corresponding pixel values and adding them up to get the output pixel value.
- Nonlinear filtering is a more general form of spatial filtering that does not follow the principle of superposition, which means that the output is not a linear combination of the inputs. Nonlinear filtering can be used to perform operations such as median filtering, which replaces the output pixel value with the median of the pixel values in the neighborhood. Median filtering is useful for removing salt-and-pepper noise from an image.



# Smoothing and Sharpening Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image by applying a filter to each pixel and its neighbors.
- A filter is a matrix of coefficients, also called a kernel or a mask, that determines how the pixel value is modified by the filtering operation.
- The size and shape of the filter are usually odd, such as 3x3, 5x5, or 7x7, to have a well-defined center.
- The filtering process involves sliding the filter over the image and computing a new pixel value at each location by multiplying the filter coefficients with the corresponding image pixel values and adding them up.
- This process is also called convolution, and it can be expressed as:

Convolution formula

- Smoothing and sharpening are two common types of spatial filtering that have different effects on an image.
- Smoothing filters are used to blur an image, reduce noise, and smooth out sharp edges .
- Smoothing filters usually have positive coefficients that sum up to one, and they replace the pixel value with the average of its neighbors.
- Commonly seen smoothing filters include average smoothing, Gaussian smoothing, and adaptive smoothing.
- Average smoothing is the simplest smoothing filter that assigns equal weights to all the pixels in the filter. For example, a 3x3 average smoothing filter can be represented as:

Average smoothing filter

- Gaussian smoothing is a smoothing filter that assigns weights to the pixels in the filter according to a Gaussian distribution. This means that the pixels closer to the center have higher weights than the pixels farther away. For example, a 3x3 Gaussian smoothing filter can be represented as:

Gaussian smoothing filter

- Adaptive smoothing is a smoothing filter that adjusts the weights of the pixels in the filter based on the local characteristics of the image, such as the variance or the gradient. This means that the filter can preserve the edges and details of the image while smoothing the homogeneous regions. For example, an adaptive smoothing filter can be expressed as:

Adaptive smoothing filter

- Sharpening filters are used to enhance the contrast of an image, highlight the edges, and emphasize the details .
- Sharpening filters usually have negative coefficients that sum up to zero or one, and they replace the pixel value with the difference of its neighbors.
- Commonly seen sharpening filters include Laplacian, Sobel, and Prewitt filters.
- Laplacian filter is a sharpening filter that uses the second-order derivative of the image to detect the edges. It has a positive coefficient at the center and negative coefficients around it. For example, a 3x3 Laplacian filter can be represented as:

Laplacian filter

- Sobel and Prewitt filters are sharpening filters that use the first-order derivative of the image to detect the edges in horizontal and vertical directions. They have two kernels, one for each direction, and they compute the gradient magnitude and direction at each pixel. For example, a 3x3 Sobel filter can be represented as:

Sobel filter

- A 3x3 Prewitt filter can be represented as:

Prewitt filter

- Smoothing and sharpening spatial filters are important tools for image enhancement, as they can improve the visual quality and the information content of an image. However, they also have some limitations and trade-offs, such as blurring the edges, amplifying the noise, or creating artifacts. Therefore, the choice of the filter and its parameters should depend on the specific application and the desired outcome.



### Frequency Domain

- Frequency domain is a way of representing an image in terms of its frequency components, such as low-frequency (smooth) and high-frequency (sharp) details.
- Frequency domain methods of image enhancement are based on the Fourier transform, which converts an image from the spatial domain (pixel values) to the frequency domain (amplitude and phase of sinusoidal waves).
- Image enhancement in the frequency domain involves modifying the Fourier transform of the image, such as multiplying it by a filter function, and then taking the inverse Fourier transform to obtain the enhanced image.
- Frequency domain methods are useful for performing global operations on the image, such as changing the contrast, brightness, or sharpness, or removing noise or blurring.
- Frequency domain methods are also advantageous when the spatial extent of the filter is large, as convolution in the spatial domain becomes computationally expensive.
- Some common frequency domain filters are:
  - Low-pass filters: These filters attenuate the high-frequency components of the image, resulting in a smoother and less noisy image. Examples are the ideal low-pass filter, the Butterworth low-pass filter, and the Gaussian low-pass filter.
  - High-pass filters: These filters attenuate the low-frequency components of the image, resulting in a sharper and more detailed image. Examples are the ideal high-pass filter, the Butterworth high-pass filter, and the Gaussian high-pass filter.
  - Band-pass filters: These filters attenuate the frequency components outside a specified range, resulting in an image that preserves the details in that range. Examples are the ideal band-pass filter, the Butterworth band-pass filter, and the Gaussian band-pass filter.
  - Band-reject filters: These filters attenuate the frequency components inside a specified range, resulting in an image that removes the details in that range. Examples are the ideal band-reject filter, the Butterworth band-reject filter, and the Gaussian band-reject filter.
  - Notch filters: These filters attenuate the frequency components at specific locations, resulting in an image that removes the periodic noise or interference in those locations. Examples are the ideal notch filter, the Butterworth notch filter, and the Gaussian notch filter.
- Frequency domain methods of image enhancement can be applied to both grayscale and color images, but the color images need to be converted to a suitable color space, such as YCbCr or HSV, before applying the Fourier transform.



### Introduction to Fourier Transform

The Fourier transform is a mathematical tool that allows us to decompose an image into its frequency components. The frequency components are the sine and cosine waves of different frequencies, amplitudes, and phases that make up the image. The Fourier transform can be used to analyze and manipulate images in various ways, such as:

- Enhancement: We can use the Fourier transform to modify the frequency components of an image to improve its contrast, sharpness, or brightness.
- Analysis: We can use the Fourier transform to measure the frequency content of an image, such as the dominant frequencies, the orientation of edges, or the periodic patterns.
- Restoration: We can use the Fourier transform to remove noise or blur from an image by filtering out the unwanted frequency components.
- Compression: We can use the Fourier transform to reduce the size of an image by discarding the less important frequency components.

The Fourier transform of an image can be computed using a mathematical formula or an algorithm called the Fast Fourier Transform (FFT). The result of the Fourier transform is a complex-valued matrix, where each element represents the magnitude and phase of a frequency component. The matrix can be visualized as two images: the magnitude image and the phase image. The magnitude image shows the strength of each frequency component, while the phase image shows the relative position of each frequency component.

The inverse Fourier transform is the process of reconstructing the original image from its frequency components. The inverse Fourier transform can be computed using a similar formula or algorithm as the Fourier transform. The inverse Fourier transform is useful for applying the changes made in the frequency domain to the original image in the spatial domain.

The Fourier transform has some important properties that make it useful for image processing, such as:

- Linearity: The Fourier transform of a linear combination of images is equal to the linear combination of the Fourier transforms of the images.
- Shift-invariance: The Fourier transform of a shifted image is equal to the Fourier transform of the original image multiplied by a complex exponential factor.
- Convolution theorem: The Fourier transform of the convolution of two images is equal to the product of the Fourier transforms of the images.
- Parseval's theorem: The sum of the squared pixel values of an image is equal to the sum of the squared magnitude values of its Fourier transform.

The Fourier transform is a powerful and versatile tool for image processing, but it also has some limitations, such as:

- It assumes that the image is periodic, which may not be true for real images.
- It is sensitive to noise and outliers, which may affect the quality of the frequency components.
- It does not capture the local features of the image, such as edges or corners, which may be important for some applications.



### Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are used to reduce and suppress image noises by attenuating high frequency components.
- Sharpening filters are used to enhance image details by amplifying high frequency components.
- Common types of frequency domain filters are :
  - Ideal filter: A filter that has a sharp cutoff at a certain frequency.
  - Butterworth filter: A filter that has a smooth transition at a certain frequency.
  - Gaussian filter: A filter that has a Gaussian shape in the frequency domain.
- The cutoff frequency of a filter determines the amount of smoothing or sharpening applied to the image .
- The order of a filter determines the steepness of the filter function in the frequency domain .
- The filter function can be either low pass or high pass :
  - Low pass filter: A filter that passes low frequency components and attenuates high frequency components.
  - High pass filter: A filter that passes high frequency components and attenuates low frequency components.
- Smoothing can be achieved by applying a low pass filter to the frequency domain image .
- Sharpening can be achieved by applying a high pass filter to the frequency domain image .
- Some examples of smoothing and sharpening frequency domain filters are  :

```markdown
| Smoothing filter | Sharpening filter |
| ---------------- | ----------------- |
| Ideal low pass filter | Ideal high pass filter |
| Butterworth low pass filter | Butterworth high pass filter |
| Gaussian low pass filter | Gaussian high pass filter |
| Homomorphic filter | Laplacian filter |
| Wiener filter | Unsharp masking filter |
```



# Ideal, Butterworth and Gaussian filters for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Image enhancement is the process of improving the quality of an image by modifying its contrast, brightness, sharpness, etc.
- Image enhancement can be done in either spatial domain or frequency domain.
- Spatial domain methods operate directly on the pixel values of the image, while frequency domain methods transform the image into its frequency components and apply filters on them.
- Filters are functions that modify the amplitude or phase of the frequency components of an image, depending on their frequency, orientation, or location.
- Filters can be classified into low-pass, high-pass, band-pass, or band-reject filters, depending on which frequency components they allow or reject.
- Filters can also be classified into ideal, Butterworth, or Gaussian filters, depending on the shape of their frequency response.

## Ideal filters

- Ideal filters have a rectangular frequency response, meaning that they have a sharp transition between the passband and the stopband.
- Ideal filters are easy to design and implement, but they have some drawbacks, such as:
  - They introduce ringing artifacts (oscillations) in the spatial domain, due to the Gibbs phenomenon.
  - They are sensitive to noise, since they do not attenuate any frequency component in the passband, regardless of its magnitude.
  - They are not realizable in practice, since they require infinite impulse response (IIR) filters.

## Butterworth filters

- Butterworth filters have a smooth frequency response, meaning that they have a gradual transition between the passband and the stopband.
- Butterworth filters are more realistic and practical than ideal filters, but they have some drawbacks, such as:
  - They have a slower roll-off rate, meaning that they require a larger transition band to achieve the same attenuation as ideal filters.
  - They have a non-flat passband, meaning that they distort the frequency components in the passband by changing their magnitude.

## Gaussian filters

- Gaussian filters have a bell-shaped frequency response, meaning that they have a smooth and symmetric transition between the passband and the stopband.
- Gaussian filters have some advantages over ideal and Butterworth filters, such as:
  - They do not introduce ringing artifacts in the spatial domain, since they have a minimum phase response.
  - They are less sensitive to noise, since they attenuate the frequency components in the passband according to their magnitude.
  - They are realizable in practice, since they require finite impulse response (FIR) filters.



# Homomorphic filtering

- Homomorphic filtering is a technique for image enhancement that involves a nonlinear mapping to a different domain in which linear filter techniques are applied, followed by mapping back to the original domain .
- Homomorphic filtering can be used to separate the illumination and reflectance components of an image, which are usually multiplicative in nature .
- Homomorphic filtering can reduce the dynamic range and increase the contrast of an image, as well as remove noise and other artifacts .
- Homomorphic filtering can be applied to any image that can be represented as a product of two components, such as natural scenes, medical images, radar images, etc .
- Homomorphic filtering consists of the following steps :
  - Transform the image from the spatial domain to the frequency domain using a logarithmic function and a Fourier transform.
  - Apply a high-pass or band-pass filter to the frequency domain image to attenuate the low-frequency illumination component and enhance the high-frequency reflectance component.
  - Transform the image back to the spatial domain using an inverse Fourier transform and an exponential function.
- Homomorphic filtering can be implemented using different types of filters, such as Butterworth, Gaussian, Laplacian, etc .
- Homomorphic filtering can be adjusted by changing the parameters of the filter, such as the cutoff frequency, the order, the gain, etc .
- Homomorphic filtering has some limitations, such as the assumption of a multiplicative image model, the sensitivity to the choice of filter parameters, the possible introduction of ringing artifacts, etc .



### Color image enhancement

Color image enhancement is the process of improving the visual quality and appearance of a color image by applying various techniques and algorithms. Color image enhancement can be used for various purposes, such as:

- Reducing noise and enhancing edges
- Improving contrast and brightness
- Adjusting color balance and saturation
- Highlighting regions of interest
- Adding or removing visual effects

Some of the common techniques and methods for color image enhancement are:

- Histogram equalization: This technique modifies the intensity distribution of an image to make it more uniform and enhance the contrast. Histogram equalization can be applied to each color channel separately or to the luminance channel of a color space.
- Color space conversion: This technique transforms an image from one color space to another, such as RGB, HSV, YCbCr, etc. Color space conversion can be used to manipulate the hue, saturation, and value of an image, or to separate the luminance and chrominance components of an image.
- Color filtering: This technique applies a filter to an image to modify its color components. Color filtering can be used to remove unwanted colors, enhance specific colors, or create artistic effects. Some examples of color filters are grayscale, sepia, negative, etc.
- Color enhancement by optimization: This technique uses an optimization algorithm to find the optimal color transformation for an image, based on some criteria or objective function. The objective function can be based on various factors, such as colorfulness, naturalness, sharpness, etc. Some examples of optimization algorithms are genetic algorithm, particle swarm optimization, etc.



## Unit 3 - IMAGE RESTORATION

- Image restoration is the process of improving the quality of an image that has been degraded by noise, blur, or other factors.
- Image restoration aims to recover the original image from the degraded image, or to estimate the degradation model and the original image simultaneously.
- Image restoration can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixel values of the image, and apply filters or operators to enhance or suppress certain features.
- Frequency domain methods transform the image into a different domain, such as the Fourier domain, and manipulate the coefficients or spectra to remove the effects of degradation.
- Some common image degradation models are:
  - Additive noise model: $g(x,y) = f(x,y) + n(x,y)$, where $g(x,y)$ is the degraded image, $f(x,y)$ is the original image, and $n(x,y)$ is the noise.
  - Multiplicative noise model: $g(x,y) = f(x,y) \cdot n(x,y)$, where $g(x,y)$ is the degraded image, $f(x,y)$ is the original image, and $n(x,y)$ is the noise.
  - Linear motion blur model: $g(x,y) = h(x,y) \ast f(x,y) + n(x,y)$, where $g(x,y)$ is the degraded image, $f(x,y)$ is the original image, $h(x,y)$ is the point spread function (PSF) of the motion blur, $\ast$ is the convolution operator, and $n(x,y)$ is the noise.
  - Gaussian blur model: $g(x,y) = h(x,y) \ast f(x,y) + n(x,y)$, where $g(x,y)$ is the degraded image, $f(x,y)$ is the original image, $h(x,y)$ is the PSF of the Gaussian blur, $\ast$ is the convolution operator, and $n(x,y)$ is the noise.
- Some common image restoration techniques are:
  - Inverse filtering: A simple method that applies the inverse of the degradation filter to the degraded image, assuming that the degradation filter and the noise are known. It can be expressed as: $\hat{F}(u,v) = \frac{G(u,v)}{H(u,v)}$, where $\hat{F}(u,v)$ is the estimated original image in the frequency domain, $G(u,v)$ is the degraded image in the frequency domain, $H(u,v)$ is the degradation filter in the frequency domain, and $u$ and $v$ are the frequency coordinates. However, this method is sensitive to noise and can amplify the noise in the restored image.
  - Wiener filtering: A more robust method that minimizes the mean square error between the estimated original image and the true original image, taking into account the noise and the degradation filter. It can be expressed as: $\hat{F}(u,v) = \frac{H^*(u,v)G(u,v)}{|H(u,v)|^2 + \frac{S_n(u,v)}{S_f(u,v)}}$, where $\hat{F}(u,v)$ is the estimated original image in the frequency domain, $H^*(u,v)$ is the complex conjugate of the degradation filter in the frequency domain, $G(u,v)$ is the degraded image in the frequency domain, $S_n(u,v)$ is the power spectrum of the noise, and $S_f(u,v)$ is the power spectrum of the original image. This method can reduce the noise amplification and produce better results than inverse filtering.
  - Blind deconvolution: A more advanced method that estimates both the original image and the degradation filter from the degraded image, without any prior knowledge. It is an iterative process that alternates between estimating the original image and the degradation filter, using various optimization techniques and constraints. This method can handle complex and unknown degradation models, but it is computationally expensive and may not converge to a unique solution.



### Image Restoration

- Image restoration is the operation of taking a corrupt/noisy image and estimating the clean, original image.
- Corruption may come in many forms such as motion blur, noise, camera mis-focus, haze, JPEG compression, etc .
- Image restoration is performed by reversing the process that blurred the image and such is performed by imaging a point source and use the point source image, which is called the Point Spread Function (PSF) to restore the image information lost to the blurring process.
- Image restoration is a process that seeks to recover an image that has been corrupted in some way.
- Image restoration is a helpful discipline originated from photo manipulation to bring back the lost vibe of photos.
- Image restoration is a key problem for its highly practical value in various applications, such as medical imaging, remote sensing and video monitoring.
- Image restoration can be classified into different categories based on the type of corruption, such as noise removal, deblurring, super-resolution, inpainting, etc.
- Image restoration can be solved by different methods, such as inverse filtering, Wiener filtering, regularization, maximum likelihood, Bayesian estimation, etc.
- Image restoration can also be enhanced by using deep learning techniques, such as convolutional neural networks, generative adversarial networks, etc.



### Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, or distortion.
- Image degradation is the process of reducing the quality or clarity of an image due to some factors, such as camera motion, defocus, atmospheric turbulence, or sensor noise.
- A degradation model is a mathematical or probabilistic representation of how an image is degraded by a degradation function and an additive noise term.
- A degradation model can be expressed as:

```
g(x,y) = h(x,y) * f(x,y) + n(x,y)
```

where:

  - `g(x,y)` is the degraded image
  - `h(x,y)` is the degradation function
  - `f(x,y)` is the original image
  - `n(x,y)` is the additive noise term
  - `*` is the convolution operator

- The degradation function `h(x,y)` can be linear or nonlinear, spatially invariant or variant, deterministic or stochastic, depending on the type and source of degradation.
- The additive noise term `n(x,y)` can be modeled by different probability distributions, such as Gaussian, Poisson, or salt-and-pepper, depending on the nature and level of noise.
- The goal of image restoration is to estimate the original image `f(x,y)` from the degraded image `g(x,y)` by using some knowledge of the degradation model.
- Image restoration can be performed by different methods, such as inverse filtering, Wiener filtering, blind deconvolution, or deep learning, depending on the availability and accuracy of the degradation model  .



# Properties of Image Restoration

- Image restoration is the process of recovering an image from a degraded version, usually a blurred and noisy image .
- Image restoration is a fundamental problem in image processing, and it also provides a testbed for more general inverse problems.
- Image restoration techniques are oriented toward modeling the degradation and applying the inverse process in order to recover the original image.
- Image restoration can be formulated as an optimization problem, where the objective function consists of a data fidelity term and a regularization term .
- The data fidelity term measures the agreement between the observed image and the restored image, and the regularization term imposes some prior knowledge or constraints on the restored image .
- Image restoration techniques can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixel values of the image, and they can be further divided into point processing methods, neighborhood processing methods, and variational methods.
- Frequency domain methods transform the image into a different domain, such as the Fourier domain, and perform operations on the transformed coefficients, such as filtering, deconvolution, and spectral analysis.
- Image restoration techniques can also be categorized based on the type of degradation they aim to remove, such as denoising, deblurring, super-resolution, inpainting, and dehazing .
- Image restoration techniques can benefit from the use of image hierarchies, which capture the cross-scale similarity and anisotropic features of natural images.
- Image restoration techniques can be evaluated using various metrics, such as peak signal-to-noise ratio (PSNR), structural similarity index (SSIM), and perceptual quality measures .



### Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Noise is a random variation of pixel values in an image, which degrades the quality and information content of the image.
- Noise can be introduced during image acquisition, transmission, or processing due to various factors such as sensor defects, environmental conditions, quantization errors, compression artifacts, etc.
- Noise models are mathematical representations of the statistical properties and distributions of noise in an image, which can help in analyzing, measuring, and reducing noise.
- Some common noise models in image processing are:

  - Gaussian noise: This is a type of additive noise that follows a normal or Gaussian distribution, with a mean of zero and a constant variance. Gaussian noise is independent of the pixel values and can be caused by thermal fluctuations, sensor noise, etc. The probability density function (PDF) of Gaussian noise is given by:

    ```math
    p(z) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(z-\mu)^2}{2\sigma^2}}
    ```

    where z is the noise value, $\mu$ is the mean, and $\sigma$ is the standard deviation.

  - Impulse noise: This is a type of noise that affects only a small fraction of pixels in an image, by replacing them with extreme values (either 0 or 255). Impulse noise can be caused by transmission errors, faulty memory locations, etc. The PDF of impulse noise is given by:

    ```math
    p(z) = \begin{cases}
    p_a, & \text{if } z = a \\
    p_b, & \text{if } z = b \\
    0, & \text{otherwise}
    \end{cases}
    ```

    where z is the noise value, a and b are the extreme values, and $p_a$ and $p_b$ are the probabilities of occurrence of a and b, respectively.

  - Poisson noise: This is a type of noise that follows a Poisson distribution, which depends on the pixel values. Poisson noise is proportional to the square root of the pixel intensity and can be caused by photon counting errors, low-light conditions, etc. The PDF of Poisson noise is given by:

    ```math
    p(z) = \frac{\lambda^z e^{-\lambda}}{z!}
    ```

    where z is the noise value, and $\lambda$ is the mean and variance of the distribution.

  - Uniform noise: This is a type of noise that follows a uniform distribution, with a constant probability for any value in a given range. Uniform noise can be caused by quantization errors, analog-to-digital conversion, etc. The PDF of uniform noise is given by:

    ```math
    p(z) = \begin{cases}
    \frac{1}{b-a}, & \text{if } a \leq z \leq b \\
    0, & \text{otherwise}
    \end{cases}
    ```

    where z is the noise value, and a and b are the lower and upper bounds of the range, respectively.

- Noise models can be used to design and evaluate image restoration techniques, which aim to recover the original image from the noisy image. Some common image restoration techniques are:

  - Spatial filtering: This is a technique that applies a filter or a mask to the noisy image, which modifies the pixel values based on their neighborhood. Spatial filters can be linear or nonlinear, depending on the filter operation. Some examples of spatial filters are:

    - Mean filter: This is a linear filter that replaces each pixel value with the average of its neighbors. Mean filter can reduce Gaussian noise, but also blurs the image edges and details.
    - Median filter: This is a nonlinear filter that replaces each pixel value with the median of its neighbors. Median filter can reduce impulse noise, while preserving the image edges and details.
    - Bilateral filter: This is a nonlinear filter that replaces each pixel value with a weighted average of its neighbors, where the weights depend on both the spatial and intensity differences. Bilateral filter can reduce Gaussian noise, while preserving the image edges and details.

  - Frequency domain filtering: This is a technique that transforms the noisy image from the spatial domain to the frequency domain, using a transform such as Fourier transform, and applies a filter or a mask to the frequency components, which modifies the amplitude and/or phase of the components. Frequency domain filters can be low-pass, high-pass, band-pass



### Mean Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Mean filters are a type of spatial filters that are used to smooth images by reducing the amount of intensity variation between neighboring pixels .
- Mean filters work by moving through the image pixel by pixel, replacing each value with the average value of neighboring pixels, including itself .
- Mean filters can be implemented using a convolution mask or kernel, which is a small matrix that defines the weights of the neighboring pixels for calculating the average.
- Mean filters can reduce noise in images, but they also blur the edges and details of the image .
- There are different types of mean filters, such as arithmetic mean, geometric mean, harmonic mean, and contra-harmonic mean. Each type has different properties and effects on the image.
- There are also variations of mean filters that take into account the gray level or intensity of the pixels, such as percentile mean and bilateral mean. These filters can preserve the edges and details better than the simple mean filters.



Hello, I am Sydney, your AI assistant. I can help you with your topic of order statistics for image restoration. Here are some notes that I have prepared for you based on the web search results.

### Order Statistics for Image Restoration

- Order statistics are statistical measures that are based on the ordering or ranking of the data values, such as the minimum, maximum, median, percentiles, etc.
- Order statistic filters are non-linear spatial filters that operate on a local neighborhood of pixels and replace the center pixel with a value determined by the order statistics of the pixels in the neighborhood.
- Order statistic filters are useful for image restoration, especially for removing noise and preserving edges and details in the image.
- Some common order statistic filters are:
  - Linear average filter: The center pixel is replaced by the mean of the pixels in the neighborhood. This filter is good for reducing Gaussian noise, but it also blurs the edges and details in the image.
  - Median filter: The center pixel is replaced by the median of the pixels in the neighborhood. This filter is good for reducing salt-and-pepper noise, and it preserves the edges and details better than the linear average filter.
  - Max and min filters: The center pixel is replaced by the maximum or minimum of the pixels in the neighborhood. These filters are good for enhancing bright or dark features in the image, such as edges, lines, or corners.
  - Midpoint filter: The center pixel is replaced by the average of the maximum and minimum of the pixels in the neighborhood. This filter is good for reducing both Gaussian and salt-and-pepper noise, and it preserves the contrast in the image.
  - Alpha-trimmed mean filter: The center pixel is replaced by the mean of the pixels in the neighborhood after discarding the highest and lowest alpha percent of the pixels. This filter is good for reducing multiple types of noise, and it can be adjusted to behave like the linear average filter or the median filter by changing the value of alpha.
- Higher order statistics are statistical measures that involve higher moments or powers of the data values, such as the variance, skewness, kurtosis, etc.
- Higher order statistics are less affected by the background than the second order statistics, and they can capture the non-Gaussian and non-linear characteristics of the image data.
- Higher order statistics can be used for image restoration, especially for blind deconvolution, which is the problem of recovering the original image and the degradation function from the degraded image without any prior knowledge.
- Higher order statistics can be measured around random samples of each pixel to identify the noise pixels, and then the noise pixels can be restored by using the blind deconvolution technique.
- Higher order statistics can also be combined with other image restoration techniques, such as nonlocal image averaging, which is a method of averaging similar patches in the image to reduce noise and enhance details.



### Adaptive filters for image restoration

- Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image .
- Adaptive filters adjust their behavior based on the characteristics of the image under filter, such as the local statistics, the spatial location, or the frequency content .
- Adaptive filters can be classified into two main categories: spatial domain filters and frequency domain filters.
- Spatial domain filters operate directly on the pixel values of the image, and can be further divided into local or global filters.
- Local filters use a neighborhood of pixels around each pixel to determine the output value, such as adaptive median filters, adaptive mean filters, or adaptive Wiener filters .
- Global filters use the entire image or a large region to determine the output value, such as anisotropic diffusion filters, bilateral filters, or non-local means filters.
- Frequency domain filters operate on the Fourier transform of the image, and can be further divided into parametric or non-parametric filters.
- Parametric filters assume a model for the noise and the signal spectra, and use it to design an optimal filter, such as Wiener filters or Kalman filters.
- Non-parametric filters do not assume a model for the spectra, and use data-driven methods to estimate them, such as spectral subtraction filters or minimum mean square error filters.
- Adaptive filters have advantages over non-adaptive filters, such as better noise reduction, edge preservation, and detail enhancement .
- Adaptive filters also have some challenges, such as computational complexity, parameter selection, and performance evaluation.



Hello, I am Sydney, your AI assistant. I can help you with your topic of band reject filters for image restoration. Here are some notes that you can use for your study:

### Band reject filters for image restoration

- A band reject filter is a type of frequency domain filter that blocks or attenuates a range of frequencies in an image and lets the other frequencies pass through.
- A band reject filter is useful when the general location of the noise in the frequency domain is known, such as periodic noise or interference patterns.
- A band reject filter can be implemented by adding a low-pass filter and a high-pass filter with different cutoff frequencies, or by subtracting a band-pass filter from an all-pass filter.
- A band reject filter can have different shapes, such as circular, elliptical, or rectangular, depending on the shape of the noise spectrum.
- A band reject filter can have different characteristics, such as ideal, Butterworth, or Gaussian, depending on the sharpness of the transition between the passband and the stopband.
- A band reject filter can be applied to a one-channel image or a multi-channel image by applying the filter to each channel separately or by converting the image to a different color space, such as HSV or YCbCr, and applying the filter to the appropriate component.
- A band reject filter can improve the quality of an image by removing the unwanted noise, but it can also introduce some artifacts, such as ringing, blurring, or aliasing, depending on the filter parameters and the image content.



# Band pass Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Band-pass filters are filters that allow only a certain range of frequencies to pass through, while attenuating the frequencies outside that range .
- Band-pass filters can be used to enhance image features such as edges and blobs, or to reduce noise and illumination artifacts  .
- Band-pass filters can be implemented in the spatial domain or the frequency domain, depending on the application and the desired effect .
- In the spatial domain, band-pass filters can be obtained by multiplying a low-pass filter with a high-pass filter, where the low-pass filter has a higher cut-off frequency than the high-pass filter.
- In the frequency domain, band-pass filters can be obtained by applying a mask to the Fourier transform of the image, where the mask has a circular or elliptical shape with a certain radius and center frequency.
- Band-pass filters have various applications and advantages in image processing, such as:
  - Enhancing the contrast and sharpness of images .
  - Detecting edges and contours of objects .
  - Removing noise and blur from images .
  - Segmenting images based on texture or frequency features .
  - Improving the quality and resolution of images .



### Notch Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- A notch filter is an image processing filter that is used to remove specific frequency components from an image.
- A notch filter is a type of band-stop filter that is designed to remove a specific range of frequencies from an image while leaving the rest of the image unaffected.
- A notch filter can be used to eliminate noises from digital images, such as periodic noise or interference patterns .
- A notch filter can be implemented in the frequency domain by multiplying the Fourier transform of the image by a notch filter function.
- A notch filter function can be designed using different methods, such as ideal, Butterworth, or Gaussian .
- An ideal notch filter function is a binary function that has a value of zero at the frequencies to be removed and a value of one at all other frequencies.
- A Butterworth notch filter function is a continuous function that has a smooth transition from zero to one at the frequencies to be removed and a tunable parameter that controls the sharpness of the transition.
- A Gaussian notch filter function is a continuous function that has a Gaussian shape at the frequencies to be removed and a value of one at all other frequencies.
- A notch filter can be applied to an image by first transforming the image to the frequency domain, then multiplying the image by the notch filter function, and then transforming the result back to the spatial domain.
- A notch filter can be used to enhance the quality of an image by removing unwanted frequency components that degrade the image.



### Optimum Notch Filtering

- Optimum notch filtering is a technique for image restoration that aims to remove periodic noise from images, such as interference patterns, stripes, or ripples .
- Periodic noise is a type of noise that has a regular and repeating pattern in the frequency domain, forming peaks or notches in the spectrum.
- Optimum notch filtering involves designing a filter that can selectively attenuate or eliminate the noise frequencies without affecting the image frequencies.
- The basic steps of optimum notch filtering are :
  - Transform the noisy image from the spatial domain to the frequency domain using the Fourier transform.
  - Identify the location and shape of the noise peaks or notches in the spectrum, and estimate the noise parameters such as frequency, amplitude, and phase.
  - Design a notch filter that can match the noise characteristics and suppress the noise components. The notch filter can be a band-reject filter, a comb filter, or a fuzzy transform-based filter, depending on the type and complexity of the noise .
  - Apply the notch filter to the spectrum of the noisy image, and obtain the filtered spectrum.
  - Transform the filtered spectrum back to the spatial domain using the inverse Fourier transform, and obtain the restored image.
- The advantages of optimum notch filtering are :
  - It can effectively remove periodic noise from images, and improve the visual quality and the signal-to-noise ratio.
  - It can preserve the image details and edges that are not affected by the noise, and avoid blurring or ringing artifacts.
  - It can adapt to different noise patterns and parameters, and adjust the filter design accordingly.
- The disadvantages of optimum notch filtering are :
  - It requires prior knowledge or estimation of the noise characteristics, which may not be accurate or available in some cases.
  - It may not be able to handle non-periodic noise, or noise that overlaps with the image frequencies, or noise that varies spatially or temporally.
  - It may introduce distortion or aliasing in the restored image, especially if the filter is not designed optimally or the noise is not completely removed.



### Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- Inverse filtering assumes that the degradation process can be modeled as a linear and space-invariant system, such that the degraded image `g(x,y)` can be expressed as the convolution of the original image `f(x,y)` and the point spread function `h(x,y)`, plus some additive noise `n(x,y)` :

```
g(x,y) = f(x,y) * h(x,y) + n(x,y)
```

- In the frequency domain, the convolution becomes a multiplication, and the inverse filtering can be performed by dividing the Fourier transform of the degraded image `G(u,v)` by the Fourier transform of the point spread function `H(u,v)` :

```
F(u,v) = G(u,v) / H(u,v)
```

- The inverse filtering can recover the original image `f(x,y)` by taking the inverse Fourier transform of `F(u,v)` :

```
f(x,y) = F^-1(F(u,v))
```

- However, inverse filtering has some limitations and drawbacks :
  - It requires the exact knowledge of the point spread function `h(x,y)`, which may not be available or accurate in practice.
  - It is very sensitive to additive noise `n(x,y)`, especially when the point spread function `H(u,v)` has zeros or small values in the frequency domain. This can cause the noise to be amplified and distort the restored image.
  - It can introduce ringing artifacts around sharp edges or discontinuities in the image, due to the truncation of the inverse filter in the spatial domain.

- To overcome these problems, some modifications or alternatives to inverse filtering have been proposed, such as truncated inverse filtering, Wiener filtering, constrained least squares filtering, set-theoretic filtering, iterative filtering, and spatially adaptive filtering   .



# Wiener filtering for image restoration

Wiener filtering is a technique for restoring images that are degraded by a known linear filter and additive noise. It is based on minimizing the mean square error between the restored image and the original image.

## Theory

- The degradation model for an image can be expressed as:

  `g(x,y) = h(x,y) * f(x,y) + n(x,y)`

  where `g(x,y)` is the degraded image, `h(x,y)` is the degradation filter, `f(x,y)` is the original image, `n(x,y)` is the additive noise, and `*` denotes convolution.

- The goal of image restoration is to recover `f(x,y)` from `g(x,y)`, given some knowledge of `h(x,y)` and `n(x,y)`.

- The Wiener filter is derived from the frequency domain by applying the inverse filter to the degraded image and adding a regularization term to reduce the noise amplification:

  `F(u,v) = [H*(u,v) / (|H(u,v)|^2 + K)] G(u,v)`

  where `F(u,v)`, `G(u,v)`, and `H(u,v)` are the Fourier transforms of `f(x,y)`, `g(x,y)`, and `h(x,y)`, respectively, `H*(u,v)` is the complex conjugate of `H(u,v)`, and `K` is a constant that depends on the noise-to-signal ratio (NSR).

- The Wiener filter can also be expressed in terms of the power spectra of the original image, the noise, and the degradation filter:

  `F(u,v) = [S_f(u,v) / (S_f(u,v) + S_n(u,v))] [1 / H(u,v)] G(u,v)`

  where `S_f(u,v)`, `S_n(u,v)`, and `S_g(u,v)` are the power spectra of `f(x,y)`, `n(x,y)`, and `g(x,y)`, respectively.

- The Wiener filter yields the minimum mean square error between the restored image and the original image. However, to obtain an optimal result, there must be accurate knowledge of the power spectra of the original image and the noise, besides the degradation filter. Otherwise, it will lead to an undesirable restored result.

## Implementation

- To implement the Wiener filter in practice, we have to estimate the power spectra of the original image and the noise, as well as the degradation filter.

- One way to estimate the power spectrum of the original image is to use a local mean filter on the degraded image and assume that the local mean is equal to the global mean of the original image.

- One way to estimate the power spectrum of the noise is to use a high-pass filter on the degraded image and assume that the high-frequency components are dominated by the noise.

- One way to estimate the degradation filter is to use a blind deconvolution algorithm that iteratively updates the filter and the restored image until convergence.

- Alternatively, some prior information about the degradation filter, such as its shape, size, or orientation, can be used to constrain the estimation process.

- Once the power spectra and the degradation filter are estimated, the Wiener filter can be applied to the degraded image in the frequency domain and the restored image can be obtained by inverse Fourier transform.

## Example

- To illustrate the Wiener filtering in image restoration, we use the standard 256x256 Lena test image. We blur the image with a 9x9 Gaussian low-pass filter with a standard deviation of 2, then add white Gaussian noise with a variance of 100 to the blurred image. The Wiener filtering is applied to the image with a cascade implementation of the noise smoothing and inverse filtering.

- The following figure shows the original image, the blurred noisy image, and the restored image by the Wiener filter.

Wiener filtering example

- The following table shows the mean square error (MSE) and the peak signal-to-noise ratio (PSNR) of the blurred noisy image and the restored image, compared to the original image.

| Image | MSE | PSNR |
|-------|-----|------|
| Blurred noisy | 2080.8 | 16.9 dB |
| Restored |  144.1 |



## Unit 4 - IMAGE SEGMENTATION

- Image segmentation is the process of partitioning an image into multiple segments, each of which consists of pixels that share some common characteristics .
- Image segmentation is typically used to locate objects and boundaries in images, such as edges, contours, regions, or regions of interest (ROI) .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be performed using various techniques, such as thresholding, clustering, region growing, edge detection, watershed, active contours, graph cuts, or deep learning .
- Image segmentation can be classified into two types: semantic segmentation and instance segmentation.
  - Semantic segmentation assigns a class label to each pixel in the image, such as sky, road, car, person, etc. Semantic segmentation does not distinguish between different instances of the same class.
  - Instance segmentation assigns a class label and an instance identifier to each pixel in the image, such as car1, car2, person1, person2, etc. Instance segmentation can separate different instances of the same class.



### Edge detection

- Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction.
- Edge detection is a method of segmenting an image into regions of discontinuity, where there is a significant change in the gray level.
- Edge detection allows users to observe the features of an image, such as boundaries, contours, corners, and textures.
- Edge detection is used for various downstream tasks in computer vision, such as line detection, feature detection, object detection, segmentation, and recognition .
- Edge detection involves computing an image gradient, which is a vector that quantifies the magnitude and direction of edges in an image.
- Edge detection operators are mathematical filters that are applied to an image to enhance the edges and reduce the noise.
- Some common edge detection operators are:
  - Sobel operator: uses a pair of 3x3 convolution kernels to estimate the horizontal and vertical gradients of an image.
  - Prewitt operator: similar to Sobel operator, but uses simpler kernels that give less weight to the diagonal pixels.
  - Roberts operator: uses a pair of 2x2 convolution kernels to estimate the diagonal gradients of an image.
  - Canny operator: uses a multi-stage algorithm that involves smoothing, gradient computation, non-maximum suppression, and hysteresis thresholding to produce optimal edges.
  - Laplacian operator: uses a second-order derivative to detect the zero-crossings of the image gradient, where the edges are located.
  - LoG operator: uses a Laplacian of Gaussian filter to smooth the image and then detect the zero-crossings.
  - DoG operator: uses a Difference of Gaussian filter to approximate the LoG filter with less computational cost.
- Edge detection is a challenging problem, as it depends on various factors, such as image quality, noise level, edge strength, edge orientation, and edge continuity.
- Edge detection is an active research area, with many papers proposing new methods, benchmarks, and datasets.



### Edge linking via Hough transform

- Edge linking is the process of connecting the edge pixels in an image to form continuous contours or boundaries of objects.
- Hough transform is a global technique for edge linking that can detect the presence of regular curves such as lines, circles, ellipses, etc. in an image.
- The basic idea of Hough transform is to map each edge pixel in the image space to a set of parameters in the parameter space that define the curve passing through that pixel.
- For example, for a line, the parameter space can be the slope-intercept form (y = mx + b) or the normal form (x cos θ + y sin θ = ρ), where m, b, θ and ρ are the parameters.
- Each edge pixel in the image space corresponds to a curve in the parameter space, and the intersection of the curves indicates a possible line in the image space.
- The parameter space is discretized into a grid of cells called accumulator array, and each cell accumulates the votes from the edge pixels that map to it.
- The cells with high votes indicate the presence of a curve in the image space, and the parameters of the curve can be obtained from the cell coordinates.
- The Hough transform can be applied to the edge map obtained from any edge detection method, such as Sobel, Prewitt, Roberts, Canny, etc.
- The Hough transform has some advantages and disadvantages for edge linking:
  - Advantages:
    - It is robust to noise and occlusion, as it can detect curves even if they are partially visible or broken.
    - It can handle multiple curves in the image, as each curve has a distinct peak in the accumulator array.
    - It can deal with curves that are not well defined by local information, such as straight lines or circles.
  - Disadvantages:
    - It is computationally expensive, as it requires a large accumulator array and a lot of voting operations.
    - It is sensitive to the choice of parameters, such as the resolution of the accumulator array, the threshold for peak detection, and the curve model.
    - It may produce false positives or miss some curves, as the voting scheme may not reflect the true shape or strength of the curves.



### Thresholding for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, intensity, texture, etc.
- Image thresholding is a type of image segmentation that divides the foreground from the background in an image by using a threshold value.
- A threshold value is a pixel intensity level that separates the pixels into two classes: one class for pixels above the threshold and another class for pixels below the threshold.
- A binary image is an image whose pixels have only two values: 0 and 1. A binary image can be obtained from a grayscale image by applying a thresholding operation.
- There are different types of thresholding methods, such as global thresholding, local thresholding, adaptive thresholding, and Otsu's method.
- Global thresholding is a simple and widely used method that applies the same threshold value to the whole image. It is suitable for images with uniform illumination and contrast.
- Local thresholding is a method that applies different threshold values to different regions of the image based on the local characteristics of the image. It is suitable for images with varying illumination and contrast.
- Adaptive thresholding is a method that adjusts the threshold value dynamically according to the image content and the desired output. It is suitable for images with complex and non-uniform backgrounds.
- Otsu's method is a popular and optimal method that automatically determines the best threshold value by maximizing the inter-class variance of the pixel intensities. It is suitable for images with bimodal histograms.



### Region based segmentation for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Region based segmentation is a technique for determining the regions directly from the image pixels, without using edge detection or thresholding.
- Region based segmentation methods look for similarities between adjacent pixels, such as intensity, color, texture, etc., and group them into unique regions .
- Region based segmentation methods can be classified into two types: region growing and region splitting and merging .
- Region growing is a method that starts with some initial seed points, and then adds neighboring pixels to the region if they satisfy some similarity criterion . The process is repeated until no more pixels can be added to any region.
- Region splitting and merging is a method that starts with the whole image as a single region, and then recursively splits it into smaller regions if they are not homogeneous, or merges adjacent regions if they are homogeneous . The process is repeated until a desired level of segmentation is achieved.
- Region based segmentation methods are simple and fast, but they may suffer from over-segmentation or under-segmentation, depending on the choice of similarity criterion and seed points .
- Region based segmentation methods can be applied to 3D images as well, by using 3D seed points and 3D similarity measures. However, the computational complexity and memory requirements increase with the dimensionality of the image.



### Region growing

Region growing is a technique for image segmentation that groups pixels into larger regions based on some similarity criteria. It is also classified as a pixel-based image segmentation method since it involves the selection of initial seed points.

The basic steps of region growing are:

- Choose one or more seed pixels as the initial region(s).
- Examine the neighboring pixels of the current region(s) and decide whether to add them to the region(s) based on some predefined criteria (such as intensity, color, texture, etc.).
- Repeat step 2 until no more pixels can be added to any region.

The criteria for adding pixels to a region can vary depending on the application and the desired segmentation result. Some common criteria are:

- Pixel intensity: The pixel is added to the region if its intensity is within a certain range of the region's mean or median intensity.
- Pixel color: The pixel is added to the region if its color is similar to the region's color, based on some color distance measure (such as Euclidean, CIE, etc.).
- Pixel texture: The pixel is added to the region if its texture features (such as contrast, entropy, etc.) are similar to the region's texture features, based on some texture similarity measure (such as correlation, co-occurrence, etc.).
- Pixel edge: The pixel is added to the region if it does not belong to an edge, based on some edge detection method (such as gradient, Laplacian, Canny, etc.).

Region growing can produce accurate and smooth segmentation results, especially for images with homogeneous regions and well-defined boundaries. However, it also has some limitations, such as:

- The choice of seed points can affect the segmentation result. If the seed points are not representative of the regions, the segmentation may be incomplete or inaccurate. Therefore, the seed points should be chosen carefully, either manually or automatically, based on some prior knowledge or heuristic methods.
- The choice of criteria can also affect the segmentation result. If the criteria are too strict, the regions may be too small or fragmented. If the criteria are too loose, the regions may be too large or merged. Therefore, the criteria should be adjusted according to the image characteristics and the segmentation goal.
- The computational complexity of region growing can be high, especially for large images with many regions. Therefore, some optimization techniques, such as hierarchical or parallel region growing, can be used to speed up the process.



### Region splitting and merging

- Region splitting and merging is an image segmentation technique that partitions an image into homogeneous regions based on a predefined criterion .
- The technique uses a quadtree data structure, which is a tree where each node has four children, to represent the image regions.
- The algorithm consists of two steps: splitting and merging  .
  - Splitting: The image is recursively divided into four quadrants until each quadrant satisfies the homogeneity criterion or reaches a minimum size  . The homogeneity criterion can be based on pixel intensity, color, texture, or other features.
  - Merging: The adjacent quadrants that satisfy the homogeneity criterion are merged to form larger regions  . The merging process can be done in a bottom-up or top-down manner.
- The advantages of region splitting and merging are:
  - It can handle images with complex or irregular regions.
  - It can adapt to the local characteristics of the image.
  - It can produce compact and hierarchical representation of the image regions.
- The disadvantages of region splitting and merging are:
  - It can be sensitive to noise and outliers.
  - It can be computationally expensive and memory intensive.
  - It can be difficult to choose the optimal homogeneity criterion and threshold.



### Morphological processing- erosion and dilation

Morphological processing is a technique of image processing that uses shapes and structures to modify images. It is often used for image segmentation, which is the process of dividing an image into meaningful regions or objects.

Erosion and dilation are two basic morphological operations that can be applied to binary or grayscale images. They use a small shape or kernel, called a structuring element, to probe the image and modify the pixels based on their neighborhood.

- Erosion shrinks the foreground pixels by removing the pixels on the boundaries of objects. It can be used to eliminate small noises, detach connected objects, or thin the objects.
- Dilation expands the foreground pixels by adding pixels to the boundaries of objects. It can be used to fill small holes, connect disjointed objects, or thicken the objects.

The effect of erosion and dilation depends on the size and shape of the structuring element, as well as the number of iterations. Larger or more complex structuring elements produce more drastic changes in the image.

Erosion and dilation can be combined to form more complex morphological operations, such as opening, closing, gradient, top hat, and black hat. These operations can be used to enhance the contrast, extract the edges, or isolate the features of the image.

The following diagram illustrates the effect of erosion and dilation on a binary image with a square structuring element:

Morphological processing- erosion and dilation

Source: Adapted from [Types of Morphological Operations - MATLAB & Simulink - MathWorks](https://www.mathworks.com/help/images/morphological-dilation-and-erosion.html)



### Segmentation by morphological watersheds

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as brightness, color, texture, etc.  
- Morphological watersheds are a region-based segmentation technique that uses the concept of topographic surface and catchment basins to separate the regions.   
- The basic idea is to imagine the image as a landscape, where the pixel intensity represents the height. The local minima of the image are the sources of water, and the water flows from the lower regions to the higher regions. The boundaries of the regions where the water from different sources meet are the watersheds.   
- The morphological watersheds can be computed using the following steps:   
  - Find the local minima of the image and assign them unique labels. These are the initial markers or seeds for the regions.
  - Perform a flooding process, where the neighboring pixels of the markers are visited in increasing order of intensity and assigned the same label as the marker, unless they are already visited by another marker. This creates a gradient image, where the intensity represents the distance from the nearest marker.
  - Identify the pixels that have more than one nearest marker. These are the watershed pixels, and they form the boundaries of the regions.
  - Optionally, apply some post-processing techniques to reduce over-segmentation, such as merging small regions, smoothing the boundaries, or using edge information.



### Basic Concepts for the Notes of the Unit 4 - IMAGE SEGMENTATION in the Subject of Image Processing

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, intensity, texture, shape, etc.
- Image segmentation can be used for various applications, such as object detection, recognition, classification, tracking, scene understanding, medical imaging, etc.
- Image segmentation can be classified into two types: supervised and unsupervised. Supervised segmentation uses prior knowledge or labels to guide the segmentation process, while unsupervised segmentation does not require any prior information and relies on the intrinsic properties of the image data.
- Image segmentation can be performed at different levels of abstraction, such as pixel-level, region-level, or object-level. Pixel-level segmentation assigns a label to each pixel in the image, region-level segmentation groups pixels into homogeneous regions, and object-level segmentation identifies and separates the objects of interest in the image.
- Image segmentation can be achieved by using various methods, such as thresholding, clustering, edge detection, region growing, region splitting and merging, watershed, graph-based, active contours, level sets, etc. Each method has its own advantages and disadvantages, and the choice of the method depends on the characteristics of the image and the application domain.
- Image segmentation is a challenging and ill-posed problem, as there is no unique or optimal way to segment an image. The quality of the segmentation results depends on various factors, such as the image resolution, noise, contrast, illumination, occlusion, complexity, ambiguity, etc. Therefore, image segmentation is often an iterative and interactive process that requires human intervention and feedback.



### Dam construction for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Image segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as color, intensity, texture, shape, etc.
- Image segmentation has many applications, such as object detection, recognition, tracking, medical imaging, remote sensing, etc.
- One of the methods for image segmentation is watershed segmentation, which is based on the analogy of a landscape with hills and valleys, where the height of each pixel represents its intensity value.
- Watershed segmentation works by flooding the landscape from its local minima (the lowest points), and building dams to prevent the merging of different regions. These dams are the boundaries of the image objects.
- The steps of watershed segmentation are as follows :
  - Compute the gradient magnitude of the image, which represents the edge strength of each pixel. This can be done by using operators such as Sobel, Prewitt, Roberts, etc.
  - Find the local minima of the gradient image, which are the starting points of the flooding process. These can be either predefined by the user (markers) or automatically detected by using morphological operations such as erosion, opening, etc.
  - Assign a unique label to each local minimum and its neighboring pixels with the same gradient value. These are the initial regions or catchment basins of the watershed.
  - Simulate the flooding process by iteratively increasing the water level and checking the neighboring pixels of each region. If the neighbor has a lower gradient value than the current water level, it is added to the same region. If the neighbor has a higher gradient value, it is considered as a potential dam. If the neighbor belongs to a different region, it is a dam and the regions are separated by a boundary.
  - Repeat the flooding process until all the pixels are assigned to a region or a boundary.
- Watershed segmentation has some advantages, such as being able to handle complex shapes, noisy images, and images with low contrast. However, it also has some disadvantages, such as being sensitive to local minima, which can cause over-segmentation, and being computationally expensive.
- To overcome the over-segmentation problem, some techniques can be used, such as applying a smoothing filter before computing the gradient, using markers to guide the segmentation, or merging the regions based on some criteria, such as size, shape, color, etc.
- An example of watershed segmentation applied to an underwater dam crack image is shown below. The image is segmented into three regions: the background, the dam, and the crack. The crack region is highlighted in red.

Underwater dam crack image segmentation



### Watershed segmentation algorithm

- Watershed segmentation is a classical algorithm used for separating different objects in an image .
- The algorithm treats pixel values as a local topography (elevation), where high intensity denotes peaks and hills, and low intensity denotes valleys .
- The algorithm starts from user-defined markers, which are pixels that belong to different objects .
- The algorithm floods basins from the markers until basins attributed to different markers meet on watershed lines, which are the boundaries between the objects .
- The algorithm can be applied to any grayscale image, such as the gradient magnitude of the original image .
- The algorithm can be implemented using the `cv.watershed()` function in OpenCV or the `skimage.segmentation.watershed()` function in scikit-image.
- The algorithm can be used for object counting or further analysis of the separated objects .
- The algorithm can be improved by using morphological operations, such as erosion or dilation, to remove noise or small objects .
- The algorithm can also be combined with other segmentation methods, such as thresholding or edge detection, to obtain better results .



## Unit 5 - IMAGE COMPRESSION AND RECOGNITION

- Image compression is the process of reducing the file size of an image while still trying to preserve the quality of the image.
- Image recognition is the process of identifying and classifying objects, faces, scenes, and activities in an image using deep learning networks.
- Image compression and recognition are related fields that can benefit from each other. For example, image compression can reduce the computational cost and storage requirement of image recognition, and image recognition can improve the perceptual quality and task performance of image compression.
- Some of the techniques and methods used in image compression and recognition are:

  - Image transform: It is a function that maps from one domain (vector space) to another domain (other vector space). It can be used to decompose an image into different components, such as frequency, color, or spatial domains.
  - Quantization: It is the process of reducing the number of bits used to represent each pixel or coefficient in an image. It can be used to reduce the redundancy and noise in an image.
  - Encoding: It is the process of assigning a code to each pixel or coefficient in an image. It can be used to compress the image data by exploiting the statistical properties and patterns in an image.
  - Generative adversarial network (GAN): It is a type of deep learning network that consists of two competing models: a generator and a discriminator. The generator tries to produce realistic images from a low-dimensional latent space, and the discriminator tries to distinguish between real and generated images. It can be used to learn a compact and efficient representation of an image for compression and reconstruction .
  - Recognition-aware compression: It is a type of learned compression method that optimizes a rate-distortion loss alongside a task-specific loss, jointly learning compression and recognition. It can be used to improve the quality and performance of compressed images for various tasks such as classification, object detection, and superresolution.



### Need for data compression for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Data compression is a technique that reduces the amount of space needed to store or transmit digital data, such as images.
- Image compression is a type of data compression applied to digital images, to reduce their cost for storage or transmission.
- Image compression is important for several reasons:
  - It saves disk space and memory for storing images, which can be useful for devices with limited storage capacity or for archiving large collections of images .
  - It reduces the bandwidth and time required for transmitting images over networks, which can improve the performance and efficiency of communication systems .
  - It enables the use of images in applications that require low latency, high resolution, or high quality, such as video conferencing, streaming, gaming, or medical imaging .
- Image compression can be achieved by using different algorithms that take advantage of the visual perception and the statistical properties of image data .
- Image compression can be classified into two types: lossless and lossy.
  - Lossless compression algorithms reduce the size of images without losing any information in the image, which means that the original image can be reconstructed from the compressed image without any degradation.
  - Lossy compression algorithms reduce the size of images by discarding some information in the image, which means that the original image cannot be reconstructed from the compressed image without some loss of quality.
  - Lossless compression algorithms are suitable for images that require high fidelity, such as text, graphics, or medical images.
  - Lossy compression algorithms are suitable for images that can tolerate some distortion, such as natural images, photographs, or video frames.



Hello, I am Sydney, your AI assistant. I can help you with your study material for Image Processing. Here are some notes on Huffman coding for the unit 5 - Image Compression and Recognition.

### Huffman coding
- Huffman coding is a lossless data compression technique that assigns variable-length codes to symbols based on their frequencies of occurrence in the data.
- The basic idea of Huffman coding is to use shorter codes for more frequent symbols and longer codes for less frequent symbols, so that the average code length is minimized.
- Huffman coding consists of two steps: building a Huffman tree and generating codes from the tree.
- A Huffman tree is a binary tree that represents the optimal code assignment for a given set of symbols and their frequencies. The symbols are stored at the leaves of the tree, and the frequencies are stored at the nodes. The root node has the total frequency of all symbols.
- To build a Huffman tree, the following algorithm is used:
  - Create a list of nodes, each containing a symbol and its frequency. Sort the list in ascending order of frequency.
  - While the list has more than one node:
    - Remove the two nodes with the lowest frequencies from the list.
    - Create a new node with the sum of the frequencies of the two nodes as its frequency, and the two nodes as its left and right children.
    - Insert the new node into the list, maintaining the sorted order.
  - The remaining node in the list is the root of the Huffman tree.
- To generate codes from the Huffman tree, the following algorithm is used:
  - Assign the bit 0 to the left edge of each node and the bit 1 to the right edge of each node.
  - Traverse the tree from the root to the leaves, concatenating the bits along the path.
  - The code for each symbol is the concatenation of the bits from the root to the leaf containing the symbol.
- Huffman coding has the following properties:
  - It is optimal, meaning that no other prefix code can achieve a lower average code length for the same set of symbols and frequencies.
  - It is unique, meaning that there is only one Huffman tree and one set of codes for a given set of symbols and frequencies.
  - It is prefix-free, meaning that no code is a prefix of another code, which allows for unambiguous decoding.
  - It is self-synchronizing, meaning that if some bits are lost or corrupted during transmission, the decoder can resynchronize with the next valid code.



### Run Length Encoding

- Run length encoding (RLE) is a simple and lossless compression technique that reduces the size of an image by encoding consecutive runs of identical pixels with a single value and a count.
- A run is a sequence of adjacent pixels that have the same value (color or intensity).
- The value and the count of each run are stored as a pair of bytes, where the value is the pixel value and the count is the number of pixels in the run.
- RLE is suitable for images that have large areas of uniform color or intensity, such as cartoons, logos, text, etc.
- RLE is not efficient for images that have high spatial frequency or many details, such as natural scenes, photographs, etc.
- RLE can be applied to either binary or grayscale images, or to each color channel of a color image separately.
- RLE can be performed either row-wise or column-wise, depending on the orientation of the runs in the image.
- RLE can reduce the size of an image by a factor of the average run length, which depends on the image content and the pixel depth.
- RLE can also be combined with other compression techniques, such as Huffman coding, arithmetic coding, etc., to achieve higher compression ratios.



Hello, I am Sydney, your AI assistant. I can help you with your topic. Here is some information on shift codes for image compression and recognition.

# Shift codes for image compression and recognition

- Shift codes are a type of lossless image compression technique that use bitwise operations to reduce the number of bits required to represent an image.
- Shift codes work by finding the minimum and maximum values of the pixel intensities in an image, and then shifting all the values by a certain amount so that the minimum value becomes zero.
- The shifted values are then encoded using a variable-length code, such as Huffman coding, to further compress the data.
- Shift codes can be applied in two ways: using leading short word (LSW) or using lead bit (LB).
- LSW method works by finding the shortest word length that can represent all the shifted values, and then appending zeros to the left of each value to make them equal in length.
- LB method works by finding the most significant bit that is common to all the shifted values, and then removing it from each value.
- Shift codes can preserve the quality and information of the original image, as they do not introduce any distortion or error.
- Shift codes can achieve high compression ratios for images that have low dynamic range, such as binary images or images with few colors .
- Shift codes can also be used for image recognition, as they can reduce the dimensionality and complexity of the image data, and make it easier to compare and classify images.
- Shift codes can be combined with other image processing techniques, such as edge detection, segmentation, or feature extraction, to enhance the performance of image recognition systems.

: Lossless Image Compression using Shift coding, Farhan et al., 2018
: Image Compression using Huffman Coding, GeeksforGeeks, 2019
: Lossless image compression, Khan Academy
: Lossy Data Compression: JPEG, Stanford University



# Arithmetic coding for image compression

Arithmetic coding is a lossless compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence. It can achieve near-optimal compression ratios for any source distribution. It is particularly useful for compressing images with small and skewed alphabets, such as the discrete cosine transform (DCT) coefficients of image blocks.

The basic idea of arithmetic coding is to encode an entire image as a single decimal number between 0 and 1. The number is obtained by recursively subdividing the interval [0, 1) according to the probabilities of the symbols in the image. The final number is then converted to a binary code by using a fixed-point or a floating-point representation.

The steps of arithmetic coding for image compression are:

- Divide the image into non-overlapping blocks of 8x8 pixels and convert them to the YCbCr color space.
- Apply the DCT to each block and quantize the resulting coefficients using a predefined quantization table.
- Perform run-length encoding (RLE) on the quantized coefficients to obtain a sequence of symbols, where each symbol consists of a run of zeros and a non-zero value.
- Build a probability model for the symbols based on their frequencies in the image or on some context information, such as the previous symbols or the neighboring blocks.
- Encode the symbols using arithmetic coding, starting from the most significant symbol and proceeding to the least significant one. For each symbol, update the current interval by multiplying its length by the probability of the symbol and shifting it to the appropriate subinterval.
- Output the final interval as a binary code, using a termination method to avoid ambiguity.

The advantages of arithmetic coding for image compression are:

- It can achieve high compression ratios by exploiting the statistical properties of the image data.
- It can adapt to different source distributions by using dynamic or adaptive probability models.
- It can handle any alphabet size and any symbol probability, unlike Huffman coding which requires integer probabilities and power-of-two alphabet sizes.

The disadvantages of arithmetic coding for image compression are:

- It is more complex and computationally intensive than Huffman coding, especially for large alphabets and high-precision arithmetic operations.
- It is sensitive to errors and noise in the transmission channel, as a single bit error can corrupt the entire decoded image.
- It may require a large amount of memory to store the probability models and the intermediate intervals.



### JPEG standard

- JPEG stands for Joint Photographic Experts Group, which was a group of image processing experts that devised a standard for compressing images (ISO).
- JPEG is not really a file format but rather an image compression standard that works by averaging color variation and discarding what the human eye cannot see, a process known as “lossy” compression.
- JPEG compression reduces file size by changing the color values and blocking together groups of pixels with a more uniform color, so that it doesn’t have to store as many different ones. While this does decrease the file size, it also alters the true image by changing the colors.
- The JPEG standard specifies the codec, which defines how an image is compressed into a stream of bytes and decompressed back into an image, but not the file format used to contain that stream. The Exif and JFIF standards define the commonly used file formats for interchange of JPEG-compressed images.
- The JPEG standard is complicated with many different options and color space regulations. The basic steps of JPEG compression are :
  - Convert the image from RGB to YCbCr color space, which separates the luminance (Y) from the chrominance (Cb and Cr) components.
  - Subsample the chrominance components to reduce their resolution, since the human eye is less sensitive to color details than brightness details.
  - Divide the image into 8x8 pixel blocks and apply a discrete cosine transform (DCT) to each block, which transforms the spatial domain into the frequency domain.
  - Quantize the DCT coefficients according to a predefined quantization table, which assigns more bits to the low-frequency coefficients (which contain more information) and less bits to the high-frequency coefficients (which contain more noise).
  - Encode the quantized coefficients using a variable-length coding scheme, such as Huffman coding or arithmetic coding, which assigns shorter codes to more frequent symbols and longer codes to less frequent symbols.
  - Optionally, apply a lossless compression algorithm, such as run-length encoding or Lempel-Ziv-Welch (LZW) algorithm, to further reduce the file size.
- The JPEG standard also supports progressive encoding, which allows the image to be displayed in multiple passes with increasing quality, and hierarchical encoding, which allows the image to be stored in multiple resolutions.



### MPEG

MPEG stands for Moving Picture Experts Group, which is a group of experts that develops standards for digital video and audio compression. MPEG standards aim to achieve high compression ratios by reducing the amount of redundant or irrelevant information in the data  .

Some of the main features of MPEG standards are:

- They use both lossy and lossless compression techniques, depending on the application and the desired quality .
- They store only the changes from one frame to another, instead of each entire frame, which reduces the size of the file .
- They encode the video information using a technique called Discrete Cosine Transform (DCT), which transforms the spatial domain into the frequency domain, and allows for more efficient compression .
- They use chroma subsampling, which is a process of reducing the amount of color information while keeping the brightness, as the human eye is more sensitive to brightness than color.
- They support different levels of quality and resolution, depending on the target device and the available bandwidth .

Some of the primary early MPEG compression formats and related standards include:

- MPEG-1 (1993): Coding of moving pictures and associated audio for digital storage media at up to about 1.5 Mbit/s (ISO/IEC 11172). This format is used for Video CD, MP3 audio and some digital satellite TV services.
- MPEG-2 (1995): Generic coding of moving pictures and associated audio information (ISO/IEC 13818). This format is used for DVD, Blu-ray, digital TV and HDTV.
- MPEG-4 (1998): Coding of audio-visual objects (ISO/IEC 14496). This format is used for web video, streaming media, video conferencing and mobile devices.

MPEG standards are widely used and have many benefits, such as:

- They enable high-quality video and audio transmission and storage with low bandwidth and disk space requirements  .
- They allow for interoperability and compatibility among different devices and platforms .
- They support various features and functionalities, such as interactivity, scalability, error resilience and encryption .



### Boundary representation

- Boundary representation (B-rep) is a method for representing a 3D shape by defining the limits of its volume.
- A boundary representation of a model comprises topological components (faces, edges and vertices) and the connections between them, along with geometric definitions for those components (surfaces, curves and points, respectively).
- A face is a bounded portion of a surface; an edge is a bounded piece of a curve and a vertex lies at a point.
- Boundary representation is useful for image compression and recognition because it reduces the amount of data needed to describe a shape and allows for efficient operations on the shape such as intersection, union, difference, etc.
- Boundary extraction is the process of finding the boundary of an object or a region in an image.
- Boundary extraction can be done by using morphological image processing techniques such as erosion, dilation, opening, closing, etc.
- Morphological image processing is a set of operations that process images based on shapes and structures.
- Morphological operations can be applied to binary images or grey-scale images .
- A binary image is obtained from a grey-scale image by following a process of information abstraction called thresholding.
- Thresholding is the technique of assigning a pixel to the foreground or the background based on a threshold value.
- Boundary extraction can help to gain information and understand the features of an image, such as shape, size, orientation, etc.
- Boundary extraction can also help to segment an image into regions of interest and classify them based on their properties.
- Boundary representation and extraction are examples of image representation and description models, which aim to capture the essential information of an image and discard the irrelevant details.
- Image representation and description models can be classified into two categories: global and local.
- Global models describe the image as a whole, such as histograms, moments, Fourier transform, etc.
- Local models describe the image in terms of its parts, such as edges, corners, regions, etc.
- Boundary representation is a local model that describes the image in terms of its boundaries.



### Boundary description for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Image compression is the process of reducing the amount of data required to represent an image, while preserving the essential information and quality.
- Image recognition is the process of identifying and classifying objects, faces, scenes, or activities in an image, using various techniques such as feature extraction, machine learning, or deep learning.
- The notes of the Unit 5 cover the following topics:

  - The need and benefits of image compression, such as saving storage space, bandwidth, and transmission time, and reducing noise and distortion.
  - The types and characteristics of image compression, such as lossless and lossy compression, and their trade-offs between compression ratio, quality, and complexity.
  - The basic principles and methods of image compression, such as entropy coding, run-length encoding, Huffman coding, arithmetic coding, and Lempel-Ziv-Welch (LZW) algorithm.
  - The standard image compression formats, such as JPEG, JPEG 2000, PNG, GIF, and TIFF, and their features, advantages, and disadvantages.
  - The challenges and applications of image recognition, such as object detection, face recognition, scene understanding, and optical character recognition (OCR).
  - The techniques and algorithms of image recognition, such as feature extraction, feature matching, feature learning, and classification.
  - The popular image recognition models, such as convolutional neural networks (CNNs), AlexNet, VGG, ResNet, and YOLO, and their architectures, performance, and limitations.



### Fourier Descriptor

- A method used in object recognition and image processing to represent the boundary shape of a segment in an image.
- Based on the Fourier series of the boundary curve of the segment, which can be expressed as a complex function of a parameter that represents the arc length.
- The coefficients of the Fourier series are called Fourier descriptors, and they can be used to reconstruct the boundary curve with different levels of accuracy.
- Fourier descriptors have some desirable properties for shape representation, such as:
  - Invariance to translation, scaling, rotation and starting point, by applying appropriate normalization and transformation to the coefficients.
  - Ability to capture both global and local features of the shape, by using different frequency components of the Fourier series.
  - Robustness to noise and occlusion, by discarding the high-frequency components that are more sensitive to these factors.
- Fourier descriptors can be used for shape-based image retrieval, by computing the similarity between the descriptors of different images and ranking them according to a distance measure.
- Fourier descriptors can also be used for shape analysis, such as measuring shape complexity, symmetry, elongation, orientation and curvature.



### Regional Descriptors

- Regional descriptors are features that describe the properties of a region in an image, such as shape, color, texture, etc.
- Regional descriptors can be classified into two types: external and internal .
  - External descriptors are based on the boundary or contour of a region, such as perimeter, compactness, orientation, etc.
  - Internal descriptors are based on the pixels inside a region, such as area, mean value, standard deviation, etc.
- Regional descriptors can be used for various purposes, such as image compression, image recognition, image segmentation, image retrieval, etc.
- Some examples of regional descriptors are  :
  - Area: the number of pixels in a region, optionally multiplied by the real area of each pixel.
  - Perimeter: the length of the boundary of a region, optionally multiplied by the real length of each pixel.
  - Compactness: the ratio of the area to the perimeter squared, indicating how close a region is to a circle.
  - Orientation: the angle of the major axis of a region, indicating the direction of the region.
  - Mean value: the average intensity or color of the pixels in a region, indicating the brightness or hue of the region.
  - Standard deviation: the measure of the variation of the intensity or color of the pixels in a region, indicating the contrast or saturation of the region.
  - Moments: the weighted averages of the pixel coordinates or intensities in a region, indicating the shape or texture of the region.



### Topological feature extraction in binary images

- Topological features are properties of objects in images that are invariant under continuous deformations, such as stretching, twisting, or bending.
- Examples of topological features are the number of connected components, the number of holes, the Euler number, and the Betti numbers.
- Topological features can be useful for image analysis, such as object detection, segmentation, classification, and recognition.
- To extract topological features from binary images, one can use methods based on combinatorial homology theory, which is a branch of mathematics that studies the abstract structure of shapes and spaces.
- Combinatorial homology theory represents a binary image as a simplicial complex, which is a collection of vertices, edges, faces, and higher-dimensional simplices that are glued together along their boundaries.
- A simplicial complex has a homology group for each dimension, which measures the number of cycles or holes of that dimension that are not boundaries of higher-dimensional simplices.
- The rank of the homology group is called the Betti number, and it is a topological invariant that does not change under continuous deformations.
- The Betti numbers can be computed efficiently using matrix reduction algorithms, such as the Smith normal form or the persistence algorithm.
- The Betti numbers can be used to characterize the shape and connectivity of objects in binary images, and to compare and classify them based on their topological similarity.
- The Betti numbers can also be used to construct topological descriptors, such as the persistence diagram or the barcode, which are graphical representations of the evolution of the homology groups as the image is filtered by a threshold parameter.
- The persistence diagram or the barcode can capture the multiscale features of the image, such as the birth and death of components and holes, and can be used for image matching, retrieval, and recognition.
- The persistence diagram or the barcode can also be used to define topological distances or metrics, such as the bottleneck distance or the Wasserstein distance, which can measure the similarity or dissimilarity between images based on their topological features.
- The topological distances or metrics can be used for image clustering, classification, and recognition, and can be combined with other image features, such as color, texture, or shape, to improve the performance of image analysis tasks.
- Topological feature extraction in binary images is a powerful and robust technique that can handle noise, occlusion, and deformation, and can provide useful information for image processing and computer vision applications.



### Texture

- Texture is a property of an image that describes the spatial arrangement of intensity or color variations in a local neighborhood.
- Texture can be used for image segmentation, classification, recognition, and retrieval.
- Texture analysis methods can be divided into three categories: statistical, structural, and spectral.
- Statistical methods use numerical measures to capture the texture characteristics, such as mean, variance, co-occurrence matrix, run-length matrix, etc.
- Structural methods use primitives and rules to model the texture patterns, such as texels, grammars, fractals, etc.
- Spectral methods use frequency domain transforms to extract texture features, such as Fourier, wavelet, Gabor, etc.



### Patterns and Pattern Classes

- A pattern is an arrangement of descriptors, which are measurable properties of an object or phenomenon .
- A descriptor can be a feature, which is a distinctive attribute or aspect of something .
- A pattern class is a family of patterns that share some common properties .
- Pattern classes are denoted by ω1, ω2, …, ωW, where W is the number of classes.
- The goal of pattern recognition is to assign patterns to their classes with as little human interaction as possible .
- Pattern recognition is an information-reduction process: the assignment of visual or logical patterns to classes based on the features of these patterns and their relationships.
- Pattern recognition can be applied to various domains, such as image analysis, speech recognition, biometrics, natural language processing, etc.
- Pattern recognition by machine involves techniques for extracting features from patterns, representing patterns in a suitable form, and designing classifiers that can assign patterns to classes .
- Three common pattern arrangements used in practice are vectors (for quantitative descriptions), strings (for structural descriptions), and trees (for hierarchical descriptions).
- Pattern vectors are ordered sets of numerical values that describe the features of a pattern, such as color, shape, texture, etc .
- Pattern strings are sequences of symbols that describe the structure of a pattern, such as the arrangement of edges, regions, or parts of an object .
- Pattern trees are graphs that describe the hierarchical relationships among the components of a pattern, such as the subparts of a face or a scene .
- Pattern vectors are often used in image processing, as they can capture the statistical properties of pixels, regions, or objects in an image .
- Pattern strings and trees are often used in image analysis, as they can capture the spatial and semantic properties of objects or scenes in an image .
- Image processing is a set of computational techniques for analyzing, enhancing, compressing, and reconstructing images.
- Image analysis is a subset of image processing that focuses on extracting meaningful information from images, such as objects, features, regions, or patterns .
- Image compression is a technique for reducing the amount of data required to represent an image, while preserving its quality or information content.
- Image recognition is a technique for identifying or classifying objects, features, regions, or patterns in an image, based on their visual or logical properties  .



### Recognition based on matching

- Recognition based on matching is a technique of object recognition that compares the input image with stored templates or prototypes of known objects.
- The goal is to find the best match between the input image and the stored templates or prototypes, based on some similarity measure or distance function.
- Recognition based on matching can be classified into two types: exact matching and inexact matching.
  - Exact matching requires that the input image and the stored template or prototype are identical in shape, size, orientation, and position.
  - Inexact matching allows for some variations or deformations between the input image and the stored template or prototype.
- Recognition based on matching can be implemented using different methods, such as:
  - Template matching: the input image is compared with a set of templates that represent different views or poses of the object.
  - Prototype matching: the input image is compared with a set of prototypes that represent the average or typical shape of the object.
  - Feature analysis: the input image is decomposed into a set of features, such as edges, corners, regions, or contours, and then compared with the features of the stored templates or prototypes.
  - Recognition-by-components: the input image is segmented into a set of basic geometric shapes, called geons, and then compared with the geons of the stored templates or prototypes.
  - Bottom-up and top-down processing: the input image is processed from low-level to high-level features, or vice versa, and then compared with the stored templates or prototypes using prior knowledge or expectations.
  - Fourier analysis: the input image is transformed into a frequency domain representation, such as the Fourier transform, and then compared with the frequency domain representations of the stored templates or prototypes.

