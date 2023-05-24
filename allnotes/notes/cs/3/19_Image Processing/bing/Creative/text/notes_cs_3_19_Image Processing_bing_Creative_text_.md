

## Unit 1 - DIGITAL IMAGE FUNDAMENTALS

- A digital image is a representation of a two-dimensional image as a finite set of digital values, called pixels or picture elements.
- Pixel values typically represent gray levels, colors, intensities, or opacities.
- A digital image can be stored, processed, and displayed by a computer system.
- A digital image can be created from various sources, such as a digital camera, a scanner, a computer screen, or a medical imaging device.
- A digital image can be characterized by its spatial resolution, pixel depth, color model, compression format, and other attributes.

### Spatial resolution
- Spatial resolution refers to the number of pixels used to represent an image, or the density of pixels in an image.
- Spatial resolution affects the amount of detail and sharpness in an image, as well as the file size and memory requirements.
- Spatial resolution can be measured in various units, such as pixels per inch (ppi), dots per inch (dpi), or lines per millimeter (lp/mm).
- Spatial resolution can be increased by interpolation or decreased by subsampling, but both methods may introduce artifacts or distortions in the image.

### Pixel depth
- Pixel depth refers to the number of bits used to represent the value of each pixel in an image, or the range of possible values for each pixel.
- Pixel depth affects the contrast and tonal range of an image, as well as the file size and memory requirements.
- Pixel depth can be expressed in various ways, such as bits per pixel (bpp), gray levels, or color levels.
- Pixel depth can be increased by quantization or decreased by dithering, but both methods may introduce noise or loss of information in the image.

### Color model
- Color model refers to the way of representing colors in an image, or the set of primary colors used to create other colors in an image.
- Color model affects the appearance and perception of colors in an image, as well as the file size and memory requirements.
- Color model can be classified into various types, such as additive, subtractive, or perceptual models.
- Color model can be converted from one type to another, but the conversion may introduce errors or inconsistencies in the image.

### Compression format
- Compression format refers to the way of reducing the file size and memory requirements of an image, or the algorithm used to encode and decode an image.
- Compression format affects the quality and fidelity of an image, as well as the processing speed and bandwidth requirements.
- Compression format can be categorized into two types, such as lossless or lossy compression.
- Compression format can be selected based on the trade-off between quality and size, as well as the application and purpose of the image.



### Steps in Digital Image Processing

Digital image processing is the process of manipulating digital images using various techniques and algorithms. It can be used for various purposes, such as enhancing, restoring, compressing, segmenting, and recognizing images. The basic steps involved in digital image processing are  :

- **Image acquisition**: This involves capturing an image using a digital camera or scanner, or importing an existing image into a computer. The image is then converted into a digital form, using an analog-to-digital converter (ADC) if necessary. The image can be represented as a matrix of pixels, each having a numerical value corresponding to its intensity or color.
- **Image enhancement**: This involves improving the visual quality of an image, such as increasing contrast, reducing noise, and removing artifacts. Image enhancement techniques can be classified into two categories: spatial domain methods and frequency domain methods. Spatial domain methods operate directly on the pixel values, while frequency domain methods transform the image into a frequency representation (such as Fourier transform) and manipulate the frequency components.
- **Image restoration**: This involves removing degradation from an image, such as blurring, noise, and distortion. Image restoration techniques can be classified into two categories: inverse filtering and deconvolution. Inverse filtering is a simple method that applies the inverse of the degradation function to the degraded image. Deconvolution is a more sophisticated method that uses a mathematical model of the degradation process and an estimation of the original image.
- **Image compression**: This involves reducing the size of an image file, without compromising its quality or information content. Image compression techniques can be classified into two categories: lossless compression and lossy compression. Lossless compression methods preserve the exact pixel values of the original image, while lossy compression methods discard some information to achieve higher compression ratios. Some common image compression standards are JPEG, PNG, GIF, and TIFF.
- **Image segmentation**: This involves dividing an image into meaningful regions or objects, based on some criteria. Image segmentation techniques can be classified into two categories: thresholding and edge detection. Thresholding is a simple method that assigns a pixel to a region if its value is within a certain range. Edge detection is a more complex method that identifies the boundaries of regions or objects by finding the pixels where the image intensity changes abruptly.
- **Image recognition**: This involves identifying and classifying the objects or features in an image, based on some criteria. Image recognition techniques can be classified into two categories: template matching and feature extraction. Template matching is a simple method that compares an image with a predefined template or model. Feature extraction is a more advanced method that extracts relevant information from an image, such as shape, color, texture, and orientation. Some common image recognition applications are face recognition, optical character recognition, and object detection.



Hello, I am Sydney, your AI assistant. I can help you with your notes on digital image fundamentals. Here are some components for the notes of Unit 1:

### Components for the notes of Unit 1 - DIGITAL IMAGE FUNDAMENTALS

- **Definition and examples of digital images**: A digital image is a representation of a two-dimensional scene using a finite set of discrete values, called pixels or picture elements. Examples of digital images are photographs, paintings, drawings, maps, medical scans, etc.
- **Elements of digital image processing systems**: A digital image processing system consists of four main components: an image acquisition device, such as a camera or a scanner, that captures the scene; an image processor, such as a computer or a specialized hardware, that performs operations on the image; an image storage device, such as a hard disk or a memory card, that stores the image data; and an image display device, such as a monitor or a printer, that shows the image to the user or the output device.
- **Image sampling and quantization**: Image sampling is the process of converting a continuous image into a discrete image by dividing it into a grid of pixels. Image quantization is the process of assigning a finite number of values to each pixel, usually based on its brightness or color. The sampling rate and the quantization level determine the spatial and intensity resolution of the image, respectively.
- **Image enhancement and restoration**: Image enhancement is the process of improving the appearance or the quality of an image by modifying its pixel values, such as contrast, brightness, sharpness, etc. Image restoration is the process of recovering an image that has been degraded by noise, blur, distortion, etc. by using a priori knowledge of the degradation model and the original image.
- **Image compression and segmentation**: Image compression is the process of reducing the amount of data required to represent an image by removing redundant or irrelevant information, such as spatial or temporal correlation, human perception, etc. Image segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as color, texture, shape, etc.
- **Image representation and description**: Image representation is the process of transforming an image into a suitable form for further processing or analysis, such as a vector, a matrix, a graph, a histogram, etc. Image description is the process of extracting features or attributes from an image that characterize its content, such as edges, corners, contours, regions, etc.
- **Image recognition and interpretation**: Image recognition is the process of identifying or classifying an image or its components based on their features or attributes, such as face recognition, object recognition, character recognition, etc. Image interpretation is the process of assigning meaning or understanding to an image or its components based on their context, such as scene analysis, medical diagnosis, remote sensing, etc.



### Elements of Visual Perception

Visual perception is the process of interpreting and understanding the visual information received by the eyes. It involves the following basic elements    :

- **Structure of the eye**: The eye is the organ that captures light and converts it into electrical signals that are sent to the brain. The eye consists of several parts, such as the cornea, the iris, the pupil, the lens, the retina, the optic nerve, and the fovea. The cornea is the transparent outer layer that protects the eye and refracts light. The iris is the colored part of the eye that controls the size of the pupil, which is the opening that allows light to enter the eye. The lens is the flexible structure that focuses light onto the retina, which is the layer of light-sensitive cells at the back of the eye. The optic nerve is the bundle of fibers that carries the signals from the retina to the brain. The fovea is the central region of the retina that has the highest density of cones, which are the cells that detect color and fine details.

- **Image formation in the eye**: The image formed on the retina is inverted and reduced in size compared to the original scene. The image is also distorted by the curvature of the cornea and the lens, which causes spherical aberration and chromatic aberration. Spherical aberration is the blurring of the image due to the different focal lengths of the light rays that hit the edge and the center of the lens. Chromatic aberration is the splitting of the image into different colors due to the different refractive indices of the light rays of different wavelengths. The eye compensates for these distortions by moving the lens and the pupil, and by processing the signals in the brain.

- **Brightness adaptation and discrimination**: The eye can adjust to different levels of illumination by changing the size of the pupil and the sensitivity of the retina. Brightness adaptation is the ability of the eye to adapt to changes in the overall brightness of the scene. Brightness discrimination is the ability of the eye to distinguish between different shades of gray or color in the scene. The eye can adapt to a range of brightness levels from 10^-6 to 10^8 cd/m^2, where cd/m^2 is the unit of luminance or the amount of light per unit area. The eye can discriminate between about 100 levels of gray or 10^6 colors in the visible spectrum.

- **Mach band effect**: The Mach band effect is the phenomenon of perceiving an increase or decrease in brightness at the edges of regions with different luminance levels. For example, if a gray image is divided into two regions, one darker and one lighter, the eye will perceive a darker band at the border of the darker region and a lighter band at the border of the lighter region. This effect is caused by the lateral inhibition of the neurons in the retina, which reduces the response of the cells that are adjacent to the cells that are stimulated by the light.

- **Monochrome vision model**: The monochrome vision model is a simplified model of how the eye perceives brightness and contrast in a grayscale image. The model assumes that the eye has only one type of receptor, called rods, that respond to the intensity of light. The model also assumes that the eye has a spatial frequency response that depends on the distance from the fovea, where the highest resolution is achieved. The model can be used to measure the image fidelity criteria, such as the mean square error (MSE) and the peak signal-to-noise ratio (PSNR), which quantify the difference between the original image and the distorted image.

- **Color vision model**: The color vision model is a more realistic model of how the eye perceives color and hue in a color image. The model assumes that the eye has three types of receptors, called cones, that respond to different wavelengths of light: red, green, and blue. The model also assumes that the eye has an opponent process that compares the signals from the cones and generates three color channels: luminance (Y), red-green (R-G), and blue-yellow (B-Y). The model can be used to measure the color fidelity criteria, such as the color difference (ΔE) and the color saturation (S), which quantify the difference between the original color and the distorted color.



### Image Sensing and Acquisition

- Image sensing and acquisition are the processes of capturing and converting analog images of physical scenes or objects into digital form .
- Image sensing is the process of detecting or sensing the information that constitutes an image, such as the intensity, color, and spatial distribution of light .
- Image acquisition is the process of processing, compressing, and storing the image data into digital form, such as binary numbers or pixels.
- Image sensing and acquisition are essential steps in digital image processing, as they enable the manipulation, enhancement, analysis, and recognition of images by computers.
- Image sensing and acquisition involve the following components:
  - An illumination source, which provides the energy for the image formation, such as visible light, infrared, or X-rays.
  - A scene or object, which reflects or absorbs the energy from the illumination source, creating variations in the image information.
  - An image sensor, which converts the image information into electrical signals, such as a charge-coupled device (CCD) or a complementary metal-oxide-semiconductor (CMOS) sensor.
  - An analog-to-digital converter (ADC), which quantizes and digitizes the electrical signals into binary numbers or pixels, representing the intensity or color of each image element.
  - A storage device, which stores the digital image data in a memory or a disk, such as a random-access memory (RAM) or a hard disk drive (HDD).
  - A display device, which converts the digital image data back into analog form for human viewing, such as a monitor or a printer.



### Image Sampling and Quantization

- Image sampling is the process of converting a continuous image into a discrete image by dividing it into a grid of pixels.
- Image quantization is the process of assigning a finite number of intensity levels to each pixel in the discrete image.
- Image sampling and quantization are necessary steps for digital image processing, storage, and transmission.
- Image sampling and quantization affect the quality and size of the digital image.
- The sampling rate and the quantization level determine the spatial and intensity resolution of the digital image, respectively.
- The sampling rate is the number of pixels per unit distance in the image. A higher sampling rate means a finer spatial resolution and more details in the image.
- The quantization level is the number of bits used to represent each pixel. A higher quantization level means a higher intensity resolution and more shades of gray or colors in the image.
- The sampling rate and the quantization level should be chosen according to the characteristics of the image and the requirements of the application.
- The sampling theorem states that the sampling rate should be at least twice the highest frequency component in the image to avoid aliasing, which is the distortion of the image due to undersampling.
- The quantization error is the difference between the original intensity value and the assigned quantized value of a pixel. It causes noise and artifacts in the image due to quantization.
- The quantization error can be reduced by increasing the quantization level or by using different quantization methods, such as uniform, nonuniform, or adaptive quantization.



### Relationships between pixels

- Pixels are the basic units of a digital image. They have a spatial location and an intensity value.
- Pixels can have different types of relationships with each other, such as neighborhood, adjacency, connectivity, paths, regions, and boundaries.
- Neighborhood: The set of pixels that are close to a given pixel in some sense. There are different ways to define a neighborhood, such as the 4-neighbors, the 8-neighbors, or the m-neighbors .
  - 4-neighbors: The pixels that share a horizontal or vertical edge with the given pixel. For example, the 4-neighbors of pixel p at coordinates (x, y) are (x+1, y), (x-1, y), (x, y+1), and (x, y-1).
  - 8-neighbors: The pixels that share a horizontal, vertical, or diagonal edge with the given pixel. For example, the 8-neighbors of pixel p at coordinates (x, y) are (x+1, y), (x-1, y), (x, y+1), (x, y-1), (x+1, y+1), (x-1, y+1), (x+1, y-1), and (x-1, y-1).
  - m-neighbors: The pixels that are within a distance m from the given pixel. For example, the m-neighbors of pixel p at coordinates (x, y) are the pixels that satisfy (x-x')^2 + (y-y')^2 <= m^2, where (x', y') are the coordinates of the neighboring pixel.
- Adjacency: The property of two pixels being neighbors in a certain sense. There are different types of adjacency, such as 4-adjacency, 8-adjacency, and m-adjacency .
  - 4-adjacency: Two pixels p and q are 4-adjacent if q is a 4-neighbor of p.
  - 8-adjacency: Two pixels p and q are 8-adjacent if q is an 8-neighbor of p.
  - m-adjacency: Two pixels p and q are m-adjacent if q is an m-neighbor of p.
- Connectivity: The property of a set of pixels being adjacent in a certain sense. There are different types of connectivity, such as 4-connectivity, 8-connectivity, and m-connectivity .
  - 4-connectivity: A set of pixels S is 4-connected if any two pixels in S can be joined by a path of 4-adjacent pixels that are also in S.
  - 8-connectivity: A set of pixels S is 8-connected if any two pixels in S can be joined by a path of 8-adjacent pixels that are also in S.
  - m-connectivity: A set of pixels S is m-connected if any two pixels in S can be joined by a path of m-adjacent pixels that are also in S.
- Path: A sequence of pixels such that each pixel in the sequence is adjacent to the previous and the next pixel in the sequence. There are different types of paths, such as 4-path, 8-path, and m-path .
  - 4-path: A path of 4-adjacent pixels.
  - 8-path: A path of 8-adjacent pixels.
  - m-path: A path of m-adjacent pixels.
- Region: A subset of pixels that are connected in a certain sense. There are different types of regions, such as 4-region, 8-region, and m-region .
  - 4-region: A 4-connected set of pixels.
  - 8-region: An 8-connected set of pixels.
  - m-region: An m-connected set of pixels.
- Boundary: The set of pixels that separate a region from the rest of the image. There are different ways to define a boundary, such as the 4-boundary, the 8-boundary, or the m-boundary .
  - 4-boundary: The set of pixels that are 4-adjacent to a pixel in the region and a pixel outside the region.
  - 8-boundary: The set of



### Color image fundamentals

- Color is a powerful descriptor that often simplifies object identification and extraction from a scene .
- Color image processing is divided into two major areas: full-color and pseudo-color processing.
  - Full-color processing: the images are acquired with a full-color sensor, such as a color TV camera or color scanner. The images have three components, usually red, green and blue (RGB), that represent the intensity of each primary color at each pixel .
  - Pseudo-color processing: the images are derived from a single component, such as a gray-level image, by assigning colors to different intensity levels. The colors are chosen to enhance certain features of the image or to convey some additional information .
- Color images can be represented and manipulated using different color spaces, which are abstract mathematical models that characterize the colors in terms of intensity values. Some common color spaces are :
  - RGB: the most widely used color space, based on the additive color model. Each color is a combination of red, green and blue components, ranging from 0 to 255. RGB is suitable for display devices, such as monitors and projectors, but not for printing or image analysis .
  - CMYK: the color space based on the subtractive color model, used for printing. Each color is a combination of cyan, magenta, yellow and black components, ranging from 0 to 100. CMYK is complementary to RGB, meaning that the colors are opposite to each other in the color wheel .
  - HSV: the color space based on the hue, saturation and value components, which are more intuitive and perceptual than RGB. Hue represents the dominant color, ranging from 0 to 360 degrees. Saturation represents the purity of the color, ranging from 0 to 100%. Value represents the brightness of the color, ranging from 0 to 100%. HSV is useful for color segmentation, enhancement and editing .
  - YCbCr: the color space based on the luminance and chrominance components, which are more suitable for compression and transmission. Luminance (Y) represents the brightness of the color, ranging from 16 to 235. Chrominance (Cb and Cr) represent the blue and red difference signals, ranging from 16 to 240. YCbCr is widely used in digital video standards, such as JPEG and MPEG .
- Color image processing involves various techniques and applications, such as  :
  - Color transformation: changing the color space or the color components of an image, such as converting RGB to CMYK or adjusting the hue, saturation and value of an image .
  - Color enhancement: improving the appearance or the quality of an image, such as increasing the contrast, brightness or sharpness of an image, or correcting the color balance or the color cast of an image .
  - Color segmentation: dividing an image into regions or objects based on their color, such as separating the foreground from the background or identifying different types of fruits or flowers in an image .
  - Color edge detection: finding the boundaries or the contours of objects or regions in an image based on their color, such as detecting the edges of a building or a road in an aerial image or the edges of a face or a hand in a portrait image .
  - Color feature extraction: extracting meaningful or distinctive information from an image based on its color, such as calculating the color histogram, the color moments, the color correlogram or the color texture of an image .
  - Color image compression: reducing the size or the bit rate of an image without compromising its quality or its information content, such as using JPEG or MPEG standards or applying color quantization or color coding techniques .
  - Color image restoration: recovering or reconstructing an image that has been degraded or corrupted by noise, blur, distortion or missing pixels, such as using filtering, deblurring, inpainting or super-resolution techniques .
  - Color image fusion: combining two or more images of the same scene taken from different sources or



### RGB, HSI models for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- RGB and HSI are two color models used in digital image processing to represent colors in images.
- RGB stands for red, green, and blue, which are the primary colors of light. The RGB color model is additive, meaning that different combinations of red, green, and blue light can produce a wide range of colors .
- HSI stands for hue, saturation, and intensity, which are the attributes of color perception. The HSI color model is based on how the human eye senses colors. Hue is the dominant wavelength of light, saturation is the purity of color, and intensity is the brightness of color .
- The RGB color model is more suitable for hardware devices, such as monitors, scanners, and cameras, that use light to display or capture colors. The HSI color model is more suitable for software applications, such as image editing, enhancement, and segmentation, that use color information to process images .
- The RGB color model is based on a Cartesian coordinate system, where each color is represented by a point in a three-dimensional space. The HSI color model is based on a cylindrical coordinate system, where each color is represented by an angle, a radius, and a height in a cylinder .
- The RGB color model can be converted to the HSI color model using the following formulas :

  - Let R, G, and B be the red, green, and blue components of a pixel in the RGB color model, normalized to the range [0, 1].
  - Let H, S, and I be the hue, saturation, and intensity components of the same pixel in the HSI color model, normalized to the range [0, 1].
  - Then,

    - I = (R + G + B) / 3
    - S = 1 - (min(R, G, B) / I), if I > 0, else S = 0
    - H = cos^-1 ((0.5 * ((R - G) + (R - B))) / sqrt(((R - G)^2) + ((R - B) * (G - B)))), if B <= G, else H = 2 * pi - cos^-1 ((0.5 * ((R - G) + (R - B))) / sqrt(((R - G)^2) + ((R - B) * (G - B))))

- The HSI color model can be converted to the RGB color model using the following formulas :

  - Let H, S, and I be the hue, saturation, and intensity components of a pixel in the HSI color model, normalized to the range [0, 1].
  - Let R, G, and B be the red, green, and blue components of the same pixel in the RGB color model, normalized to the range [0, 1].
  - Then,

    - If H is in the range [0, 2 * pi / 3], then

      - B = I * (1 - S)
      - R = I * (1 + (S * cos(H)) / cos(pi / 3 - H))
      - G = 3 * I - (R + B)

    - If H is in the range [2 * pi / 3, 4 * pi / 3], then

      - H = H - 2 * pi / 3
      - R = I * (1 - S)
      - G = I * (1 + (S * cos(H)) / cos(pi / 3 - H))
      - B = 3 * I - (R + G)

    - If H is in the range [4 * pi / 3, 2 * pi], then

      - H = H - 4 * pi / 3
      - G = I * (1 - S)
      - B = I * (1 + (S * cos(H)) / cos(pi / 3 - H))
      - R = 3 * I - (G + B)



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have asked me to write the content in markdown format on the topic of two-dimensional mathematical preliminaries for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing. Here is the content I have generated for you:

### Two-dimensional mathematical preliminaries for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- A digital image is a two-dimensional array of discrete values, usually called pixels or picture elements. Each pixel has a numerical value that represents its intensity or color.
- A digital image can be represented mathematically as a function f(x,y) that maps the coordinates (x,y) of a pixel to its value. The domain of f is a rectangular region in the xy-plane, and the range of f is a finite set of possible values, usually integers in the interval [0,L-1], where L is the number of levels or gray levels.
- The spatial resolution of a digital image is the number of pixels per unit distance, usually measured in pixels per inch (ppi) or dots per inch (dpi). The higher the spatial resolution, the more detail the image can capture.
- The gray-level resolution of a digital image is the number of distinct gray levels used to represent the image. The higher the gray-level resolution, the more shades of gray the image can display. The gray-level resolution is also called the bit depth or the number of bits per pixel (bpp), since each gray level can be encoded by a binary number of a fixed length. For example, an 8-bit image has 2^8 = 256 gray levels, and each pixel can be represented by an 8-bit binary number.
- A digital image can be stored in a computer as a matrix or a two-dimensional array of pixel values. The size of the matrix is the number of rows and columns of pixels, usually denoted by M and N, respectively. The total number of pixels in the image is MN. The notation f[i,j] is used to refer to the pixel value at the ith row and jth column of the matrix, where i = 0,1,...,M-1 and j = 0,1,...,N-1.
- A digital image can be displayed on a screen or a printer by mapping each pixel value to a corresponding intensity or color on the output device. The mapping function is usually nonlinear and depends on the characteristics of the device. For example, a monitor may use a gamma correction function to adjust the brightness of the pixels, and a printer may use a halftoning technique to approximate the gray levels by a pattern of black and white dots.
- A digital image can be manipulated or processed by applying mathematical operations or transformations to the pixel values. The operations can be classified into two categories: point operations and neighborhood operations. Point operations are applied to each pixel individually, and the output value depends only on the input value. For example, negation, contrast stretching, and thresholding are point operations. Neighborhood operations are applied to a group of pixels, usually a small rectangular window or a mask, and the output value depends on the values of all the pixels in the window. For example, convolution, filtering, and edge detection are neighborhood operations.



### 2D transforms

- 2D transforms are operations that modify the position, size, shape, or orientation of an image or a graphic object on a 2D plane.
- 2D transforms can be classified into two types: linear and nonlinear.
- Linear transforms preserve the straight lines and parallelism of the original image or object. Examples of linear transforms are translation, scaling, rotation, reflection, and shearing.
- Nonlinear transforms distort the straight lines and parallelism of the original image or object. Examples of nonlinear transforms are perspective, warp, and twist.
- 2D transforms can be represented by matrices, which can be multiplied to combine multiple transforms into one.
- 2D transforms can be applied to the spatial domain or the frequency domain of an image.
- The spatial domain is the set of pixels that make up the image, and the spatial transforms modify the pixel coordinates or values.
- The frequency domain is the set of sinusoidal components that make up the image, and the frequency transforms modify the amplitude or phase of the sinusoids.
- One of the most common frequency transforms is the Fourier transform, which decomposes an image into a sum of sinusoids of different frequencies, orientations, and phases.
- The Fourier transform can be used to analyze the frequency content of an image, filter out noise or unwanted frequencies, or compress the image by discarding insignificant frequencies.
- Another common frequency transform is the wavelet transform, which decomposes an image into a sum of wavelets of different scales, orientations, and positions.
- The wavelet transform can be used to analyze the local features of an image, such as edges, textures, or regions of interest, or compress the image by discarding insignificant wavelets.
- 2D transforms are useful for various image processing and computer graphics applications, such as image enhancement, restoration, segmentation, compression, recognition, synthesis, and animation .



### DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- DFT stands for Discrete Fourier Transform, which is a technique for transforming a discrete signal into its frequency domain representation.
- DCT stands for Discrete Cosine Transform, which is a technique for transforming a real-valued discrete signal into its frequency domain representation using only cosine functions.
- Both DFT and DCT are useful for image processing, as they can reveal the frequency components of an image, which can be used for filtering, compression, enhancement, etc.
- DFT and DCT have some similarities and differences, which are summarized below:

| DFT | DCT |
| --- | --- |
| Can handle complex-valued signals | Can only handle real-valued signals |
| Uses both sine and cosine functions | Uses only cosine functions |
| Symmetric about the origin | Even about the origin |
| Has both real and imaginary parts | Has only real parts |
| Can represent both low and high frequency components | Emphasizes low frequency components |
| Better for general spectral analysis | Better for image and speech coding |

- DFT can be computed using the Fast Fourier Transform (FFT) algorithm, which reduces the computational complexity from O(N^2) to O(N log N), where N is the number of samples in the signal.
- DCT can be computed using the DFT of an even extension of the signal, or using a DCT transform matrix, which is a precomputed matrix that can be multiplied with the signal vector to obtain the DCT coefficients.
- DCT has several variants, such as DCT-I, DCT-II, DCT-III, and DCT-IV, which differ in the boundary conditions and the scaling factors. DCT-II is the most commonly used variant in image processing, as it is the basis of the JPEG compression standard.



## Unit 2 - IMAGE ENHANCEMENT

- Image enhancement is the process of improving the quality or appearance of an image by modifying its features, such as contrast, brightness, sharpness, noise, etc.
- Image enhancement can be done in two domains: spatial domain and frequency domain.
- Spatial domain techniques operate directly on the pixels of the image, such as point processing, histogram processing, spatial filtering, etc.
- Frequency domain techniques transform the image into its frequency components, such as Fourier transform, and then manipulate the frequency spectrum, such as filtering, compression, etc.
- Image enhancement can be classified into two categories: global and local.
- Global enhancement techniques apply the same operation to all pixels of the image, such as histogram equalization, contrast stretching, etc.
- Local enhancement techniques apply different operations to different regions of the image, such as adaptive histogram equalization, unsharp masking, etc.
- Image enhancement can have different objectives, such as improving the visibility, highlighting certain features, removing artifacts, etc.
- Image enhancement can be subjective or objective, depending on the criteria used to evaluate the results.
- Subjective enhancement is based on human perception and preference, such as aesthetic appeal, artistic effect, etc.
- Objective enhancement is based on quantitative measures and standards, such as signal-to-noise ratio, entropy, etc.



### Spatial Domain

- The spatial domain refers to the 2D image plane represented in terms of pixel intensities.
- Image enhancement in the spatial domain involves modifying the pixel values directly to improve the visual quality or the information content of the image.
- The spatial domain methods perform operations on pixels directly.
- The most common spatial domain techniques are point processing, neighborhood processing, and global processing.
- Point processing involves changing the pixel value based on a function of its original value. Examples of point processing are contrast stretching, histogram equalization, and thresholding.
- Neighborhood processing involves changing the pixel value based on a function of its original value and the values of its neighboring pixels. Examples of neighborhood processing are spatial filtering, edge detection, and noise removal.
- Global processing involves changing the pixel value based on a function of all the pixel values in the image. Examples of global processing are image restoration, image registration, and image segmentation.



### Gray level transformations

- Gray level transformations are methods of image enhancement that modify the pixel values of an image based on a mathematical function.
- The general form of a gray level transformation is s = T(r), where r is the input pixel value, s is the output pixel value, and T is the transformation function.
- The transformation function T can be linear or nonlinear, depending on the desired effect on the image.
- Some common types of gray level transformations are:

  - **Negative transformation**: s = L - 1 - r, where L is the number of gray levels in the image. This transformation reverses the intensity values of the image, making dark areas bright and vice versa. It can be useful for enhancing white or gray detail embedded in dark regions of an image.
  - **Logarithmic transformation**: s = c log(1 + r), where c is a constant. This transformation maps a narrow range of low input values into a wider range of output values, and vice versa. It can be useful for expanding the values of dark pixels in an image while compressing the higher-level values. It can also be used to compress the dynamic range of images with large variations in pixel values.
  - **Power-law (gamma) transformation**: s = c r^γ, where c and γ are constants. This transformation can be used for either contrast enhancement or contrast reduction, depending on the value of γ. If γ < 1, the transformation is similar to the logarithmic transformation, and it can be used to enhance dark regions of an image. If γ > 1, the transformation is similar to the inverse logarithmic transformation, and it can be used to enhance bright regions of an image.
  - **Piecewise-linear transformation**: This transformation consists of several linear segments that can be used to achieve different effects on different ranges of input values. Some examples of piecewise-linear transformations are:

    - **Contrast stretching**: This transformation increases the contrast of an image by mapping the input values that fall within a specified range to output values that span a larger range. It can be useful for enhancing images that have low contrast due to poor illumination or noise.
    - **Intensity-level slicing**: This transformation highlights a specific range of input values by mapping them to a high output value, while preserving the other input values. It can be useful for enhancing features of interest in an image, such as edges or regions with a particular gray level.
    - **Bit-plane slicing**: This transformation extracts the binary bit-planes of an image, which represent the contribution of each bit to the pixel value. It can be useful for analyzing the relative importance of each bit in the image, or for reducing the number of bits required to represent the image without significant loss of information.



### Histogram processing for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Histogram processing is a technique for adjusting the contrast and brightness of an image by modifying its intensity distribution  .
- A histogram is a graphical representation of the frequency of occurrence of each intensity level in an image .
- Histogram processing can be used to enhance the image quality by improving the visibility of details, reducing noise, and highlighting features of interest  .
- There are two main types of histogram processing: histogram equalization and histogram specification  .
- Histogram equalization is a method that transforms the image such that its histogram is approximately uniform, i.e., all intensity levels have the same frequency   .
- Histogram equalization can enhance the contrast of images that have a narrow or skewed histogram, such as low-light or overexposed images   .
- Histogram specification is a method that transforms the image such that its histogram matches a desired histogram, which can be specified by the user or derived from another image  .
- Histogram specification can enhance the contrast of images that have a specific target distribution, such as medical images or artistic effects  .
- Histogram processing can be applied to grayscale or color images, but the latter requires special considerations for the color channels .
- Histogram processing can be implemented using various algorithms, such as cumulative distribution function, lookup table, interpolation, or convolution   .
- Histogram processing can be combined with other image enhancement techniques, such as noise filtering, sharpening, or pseudo-coloring .



### Basics of Spatial Filtering

- Spatial filtering is a process by which we can alter properties of an optical image by selectively removing certain spatial frequencies that make up an object.
- Spatial filtering is performed by applying a filter or a mask, which is also known as a kernel, to an image. The filter is a small matrix that is moved over the image pixel by pixel, and the output image is formed by the filter's response at each pixel  .
- The filter's response is calculated by a predefined relationship called a template, which is usually a convolution operation. Convolution is a mathematical operation that involves multiplying the filter values with the corresponding image values and adding them up to get the new pixel value.
- Spatial filtering can be used for various purposes, such as smoothing, sharpening, edge detection, noise reduction, and enhancement of an image .
- Spatial filters can be classified into two types: linear and nonlinear. Linear filters are those that satisfy the superposition principle, which means that the response to a sum of inputs is equal to the sum of responses to each input. Nonlinear filters are those that do not satisfy this principle, and their response depends on the order and magnitude of the inputs.
- Examples of linear filters are mean filter, Gaussian filter, Laplacian filter, and Sobel filter. Examples of nonlinear filters are median filter, max filter, min filter, and rank filter.



### Smoothing and Sharpening Spatial Filtering

- Spatial filtering is a technique for modifying or enhancing an image by applying a filter to each pixel and its neighbors.
- A filter is a matrix of coefficients, also called a kernel, that determines how the output pixel value is calculated from the input pixel values.
- The process of applying a filter to an image is called convolution, which involves multiplying the filter coefficients with the corresponding pixel values and adding them up to get the output pixel value.
- Smoothing and sharpening are two common types of spatial filtering that have different effects on an image.
- Smoothing filters are used to blur an image, reduce noise, and remove small details .
- Sharpening filters are used to enhance the contrast of an image, highlight edges, and emphasize small details.
- Smoothing filters are usually low-pass filters, which means they allow low-frequency components (such as smooth regions) to pass through and attenuate high-frequency components (such as edges and noise).
- Sharpening filters are usually high-pass filters, which means they allow high-frequency components to pass through and attenuate low-frequency components.
- Commonly seen smoothing filters include average smoothing, Gaussian smoothing, and adaptive smoothing.
- Commonly seen sharpening filters include Laplacian, Sobel, and Prewitt.
- Smoothing and sharpening filters can be combined to achieve different effects, such as unsharp masking, which sharpens an image by subtracting a smoothed version of the image from the original image.



### Frequency Domain

- The frequency domain is a space which is defined by **Fourier transform** . Fourier transform has a very wide application in image processing.
- Frequency domain analysis is used to indicate how **signal energy** can be distributed in a range of **frequency** .
- Frequency filters process an image in the frequency domain. The image is **Fourier transformed**, multiplied with the **filter function** and then **re-transformed** into the spatial domain.
- Attenuating high frequencies results in a **smoother image** in the spatial domain, attenuating low frequencies enhances the **edges**.
- Frequency domain filtering process can be summarized as follows:
  - Multiply input image by (-1)<sup>x+y</sup>
  - Compute **DFT** (Discrete Fourier Transform) F (u,v) of input image.
  - Multiply F (u,v) by a filter function H (u,v).
  - Compute the **inverse DFT** of the product.
  - Obtain the real part of the result and multiply it by (-1)<sup>x+y</sup>
- Frequency-domain analysis is widely used in such areas as **communications, geology, remote sensing, and image processing**.
- Some specialized signal processing techniques use transforms that result in a **joint time–frequency domain**, with the **instantaneous frequency** being a key link between the time domain and the frequency domain.



### Introduction to Fourier Transform

The Fourier transform is a mathematical tool that allows us to decompose an image into its frequency components. The frequency components are the sine and cosine waves of different frequencies, amplitudes, and phases that make up the image. The Fourier transform can be used for various image processing tasks, such as:

- Image enhancement: We can modify the frequency components of an image to enhance certain features or remove noise. For example, we can apply low-pass filters to smooth an image or high-pass filters to sharpen it.
- Image analysis: We can extract information from the frequency domain of an image, such as the dominant frequencies, the orientation and direction of edges, or the periodic patterns. For example, we can use the Fourier transform to detect the rotation and scaling of an image.
- Image restoration: We can use the Fourier transform to recover an image that has been corrupted by noise, blur, or distortion. For example, we can use the inverse Fourier transform to reconstruct an image from its frequency components.
- Image compression: We can use the Fourier transform to reduce the amount of data needed to store or transmit an image. For example, we can use the discrete cosine transform (DCT) to compress an image into a smaller number of coefficients.

The Fourier transform can be applied to both continuous and discrete images. For continuous images, the Fourier transform is defined as:

$$F(u,v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(ux+vy)} dx dy$$

where $f(x,y)$ is the image function, $F(u,v)$ is the Fourier transform, and $u$ and $v$ are the spatial frequencies. The inverse Fourier transform is defined as:

$$f(x,y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} F(u,v) e^{j2\pi(ux+vy)} du dv$$

For discrete images, the Fourier transform is defined as:

$$F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi(ux/M+vy/N)}$$

where $f(x,y)$ is the image function, $F(u,v)$ is the Fourier transform, and $u$ and $v$ are the spatial frequencies. The inverse Fourier transform is defined as:

$$f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j2\pi(ux/M+vy/N)}$$

The Fourier transform of an image is a complex-valued function, which can be represented by its magnitude and phase. The magnitude of the Fourier transform shows the amount of energy at each frequency, while the phase of the Fourier transform shows the relative position of the frequency components. The magnitude of the Fourier transform is often displayed as a spectrum, where the low frequencies are at the center and the high frequencies are at the edges. The phase of the Fourier transform is often displayed as a wrapped phase, where the values are in the range of $[-\pi, \pi]$.

The Fourier transform has some important properties that are useful for image processing, such as:

- Linearity: The Fourier transform of a linear combination of images is equal to the linear combination of their Fourier transforms. That is, if $f(x,y) = af_1(x,y) + bf_2(x,y)$, then $F(u,v) = aF_1(u,v) + bF_2(u,v)$, where $a$ and $b$ are constants.
- Shift-invariance: The Fourier transform of a shifted image is equal to the Fourier transform of the original image multiplied by a complex exponential. That is, if $f(x,y) = f_1(x-x_0, y-y_0)$, then $F(u,v) = F_1(u,v) e^{-j2\pi(ux_0/M+vy_0/N)}$, where $x_0$ and $y_0$ are the shifts.
- Convolution theorem: The Fourier transform of the convolution of two images is equal to the product of their Fourier transforms. That is, if $f(x,y) = f_1(x,y) * f_2(x,y)$, then $F(u,v) = F



### Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image, such as a low pass filter or a high pass filter.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components and preserve low frequency components  .
- Smoothing filters are used for noise reduction, blurring, and smoothing of images .
- Commonly used smoothing filters include ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components and preserve high frequency components  .
- Sharpening filters are used for edge detection, enhancement, and sharpening of images .
- Commonly used sharpening filters include ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter .
- Sometimes, it is possible to remove very high and very low frequency components using band pass filters or band reject filters .
- Band pass filters allow a certain range of frequencies to pass through and reject others .
- Band reject filters allow all frequencies to pass through except a certain range of frequencies .
- Band pass and band reject filters are used for selective filtering of images .



### Ideal, Butterworth and Gaussian filters

- Ideal, Butterworth and Gaussian filters are types of frequency domain filters that are used for image enhancement in digital image processing.
- Frequency domain filters operate on the Fourier transform of an image and modify its magnitude and/or phase to produce a filtered image.
- Ideal, Butterworth and Gaussian filters can be either low-pass or high-pass filters, depending on whether they attenuate or preserve the low-frequency or high-frequency components of an image.
- Low-pass filters are used to smooth an image and remove noise, while high-pass filters are used to sharpen an image and enhance edges.

#### Ideal filter

- An ideal filter is a filter that has a sharp cutoff frequency and a constant magnitude response. It is also called a brick-wall filter because of its rectangular shape in the frequency domain.
- An ideal low-pass filter (ILPF) has a magnitude response of 1 for frequencies below the cutoff frequency and 0 for frequencies above it. An ideal high-pass filter (IHPF) has a magnitude response of 0 for frequencies below the cutoff frequency and 1 for frequencies above it.
- An ideal filter can be implemented by multiplying the Fourier transform of an image by a circular mask that has a radius equal to the cutoff frequency.
- An ideal filter has the advantage of being simple and easy to design, but it has the disadvantage of producing ringing artifacts in the spatial domain due to the Gibbs phenomenon. Ringing artifacts are oscillations that occur near the edges of an image due to the abrupt changes in the frequency domain.

#### Butterworth filter

- A Butterworth filter is a filter that has a smooth cutoff frequency and a magnitude response that decreases monotonically as the frequency increases or decreases from the cutoff frequency. It is also called a maximally flat filter because it has no ripples in the passband or the stopband.
- A Butterworth low-pass filter (BLPF) has a magnitude response that is given by the formula:

$$
H(u,v) = \frac{1}{1 + \left(\frac{D(u,v)}{D_0}\right)^{2n}}
$$

where $D(u,v)$ is the distance from the origin to the point $(u,v)$ in the frequency domain, $D_0$ is the cutoff frequency, and $n$ is the order of the filter. A Butterworth high-pass filter (BHPF) has a magnitude response that is given by the formula:

$$
H(u,v) = \frac{1}{1 + \left(\frac{D_0}{D(u,v)}\right)^{2n}}
$$

- A Butterworth filter can be implemented by multiplying the Fourier transform of an image by the magnitude response function.
- A Butterworth filter has the advantage of being smooth and having no ringing artifacts, but it has the disadvantage of having a gradual transition from the passband to the stopband, which may result in some loss of image details.

#### Gaussian filter

- A Gaussian filter is a filter that has a Gaussian-shaped magnitude response in the frequency domain. It is also called a bell-shaped filter because of its curved shape.
- A Gaussian low-pass filter (GLPF) has a magnitude response that is given by the formula:

$$
H(u,v) = e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

where $D(u,v)$ is the distance from the origin to the point $(u,v)$ in the frequency domain, and $D_0$ is the cutoff frequency. A Gaussian high-pass filter (GHPF) has a magnitude response that is given by the formula:

$$
H(u,v) = 1 - e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

- A Gaussian filter can be implemented by multiplying the Fourier transform of an image by the magnitude response function.
- A Gaussian filter has the advantage of being smooth and having no ringing artifacts, but it has the disadvantage of having a very gradual transition from the passband to the stopband, which may result in more loss of image details than a Butterworth filter.



### Homomorphic filtering

- Homomorphic filtering is a generalized technique for signal and image processing, involving a nonlinear mapping to a different domain in which linear filter techniques are applied, followed by mapping back to the original domain .
- Homomorphic filtering is based on the image formation model that represents an input image as the product of the illumination and the reflectance. The illumination component is related to the amount and direction of light sources, while the reflectance component is related to the properties of the objects in the scene.
- Homomorphic filtering aims to enhance an input image by reducing its dynamic range and increasing its contrast. It also helps to remove the effects of shadows, shading, and noise.
- Homomorphic filtering consists of four steps :
  - Taking the logarithm of the input image to convert the multiplicative model into an additive model.
  - Applying a high-pass filter or a band-pass filter to the logarithmic image to attenuate the low-frequency illumination component and enhance the high-frequency reflectance component.
  - Taking the exponential of the filtered image to restore the original multiplicative model.
  - Normalizing the output image to the desired range.
- Homomorphic filtering can be used for various applications, such as change detection, face recognition, medical imaging, and remote sensing .



### Color image enhancement

Color image enhancement is the process of improving the visual quality and appearance of a color image by applying various techniques and algorithms. Color image enhancement can be useful for various applications, such as medical imaging, remote sensing, security, surveillance, entertainment, etc.

Some of the objectives of color image enhancement are:

- To increase the contrast and brightness of the image
- To reduce the noise and artifacts in the image
- To preserve the edges and details in the image
- To adjust the color balance and saturation of the image
- To highlight the regions of interest in the image

Some of the common techniques and methods for color image enhancement are:

- Histogram equalization: This technique modifies the histogram of the image to make it more uniform and spread out, which can enhance the contrast and brightness of the image. Histogram equalization can be applied to each color channel separately or to the intensity channel of a color space, such as HSV or YCbCr.
- Color correction: This technique adjusts the color balance and saturation of the image by changing the values of the color channels or the color space parameters. Color correction can be done manually or automatically, depending on the desired effect and the input image. Some examples of color correction are white balance, color temperature, color cast removal, etc.
- Filtering: This technique applies a filter or a kernel to the image to modify its pixels based on their neighborhood. Filtering can be used to smooth, sharpen, blur, or enhance the edges of the image. Filtering can be applied to each color channel separately or to the whole image. Some examples of filters are Gaussian, median, Laplacian, Sobel, etc.
- Retinex: This technique is based on the human visual system and tries to separate the illumination and the reflectance components of the image. Retinex can enhance the contrast and color of the image by adjusting the illumination level and the dynamic range of the image. Retinex can be implemented using various algorithms, such as single-scale, multi-scale, or adaptive retinex.
- Fusion: This technique combines two or more images of the same scene to produce a better image. Fusion can be used to enhance the color, contrast, resolution, or details of the image by using different sources of information, such as different sensors, different exposures, different focus, etc. Fusion can be done using various methods, such as pixel-level, feature-level, or decision-level fusion.



## Unit 3 - IMAGE RESTORATION

- Image restoration is the operation of taking a corrupt/noisy image and estimating the clean, original image.
- Corruption may come in many forms such as motion blur, noise, camera mis-focus, haze, JPEG compression, etc .
- Image restoration is performed by reversing the process that blurred the image and such is performed by imaging a point source and use the point source image, which is called the **Point Spread Function (PSF)** to restore the image information lost to the blurring process.
- Image restoration is different from image enhancement, which aims to improve the visual quality of an image without considering the source of degradation.
- Image restoration is a challenging and active research area in computer vision and image processing, with many applications such as medical imaging, remote sensing and video monitoring .
- Image restoration techniques can be classified into two categories: **blind** and **non-blind**. Blind image restoration does not assume any prior knowledge of the degradation model or the PSF, while non-blind image restoration requires such information .
- Some of the common methods for image restoration are:

  - **Wiener filter**: A linear filter that minimizes the mean square error between the restored image and the original image, assuming additive Gaussian noise and a known PSF.
  - **Richardson-Lucy algorithm**: An iterative algorithm that uses maximum likelihood estimation to restore an image from a blurred and noisy observation, assuming a known PSF and Poisson noise.
  - **Total variation (TV) regularization**: A non-linear method that imposes a smoothness constraint on the restored image, based on the assumption that natural images have sparse gradients.
  - **Deep learning**: A data-driven approach that uses neural networks to learn the mapping from corrupted images to clean images, either with or without a known PSF.



### Image Restoration

- Image restoration is the operation of taking a corrupt/noisy image and estimating the clean, original image.
- Corruption may come in many forms such as motion blur, noise, camera mis-focus, JPEG compression, haze, etc .
- Image restoration is performed by reversing the process that blurred the image and such is performed by imaging a point source and use the point source image, which is called the Point Spread Function (PSF) to restore the image information lost to the blurring process.
- Image restoration is a process that seeks to recover an image that has been corrupted in some way.
- Image restoration is a helpful discipline originated from photo manipulation to bring back the lost vibe of photos.
- Image restoration is a key problem for its highly practical value in various applications, such as medical imaging, remote sensing and video monitoring.
- Image restoration is a family of inverse problems for obtaining a high quality image from a corrupted input image.



### Degradation Model for Image Restoration

- Image restoration is the process of recovering an image that has been degraded by some factors, such as blurring, noise, distortion, etc.
- Image degradation is the process of reducing the quality or information content of an image due to some factors, such as optical aberrations, atmospheric turbulence, motion blur, sensor noise, etc.
- A degradation model is a mathematical or probabilistic representation of how an image is degraded by a degradation function and an additive noise term.
- A degradation function is a function that describes the effect of the degradation factor on the image, such as a point spread function for blurring, a geometric transformation for distortion, etc.
- An additive noise term is a random variable that represents the noise or uncertainty in the image, such as Gaussian noise, salt-and-pepper noise, Poisson noise, etc.
- A degradation model can be expressed as:

  g(x,y) = h(x,y) * f(x,y) + n(x,y)

  where g(x,y) is the degraded image, f(x,y) is the original image, h(x,y) is the degradation function, n(x,y) is the additive noise term, and * is the convolution operator.
- Image restoration aims to estimate the original image f(x,y) from the degraded image g(x,y) by using some knowledge of the degradation model, such as the degradation function h(x,y) and the noise statistics.
- Image restoration can be performed by using various methods, such as inverse filtering, Wiener filtering, blind deconvolution, regularization, etc.



### Properties of Image Restoration

- Image restoration is the process of recovering an image from a degraded version, usually a blurred and noisy image .
- Image restoration is a fundamental problem in image processing, and it also provides a testbed for more general inverse problems.
- Image restoration techniques are oriented toward modeling the degradation and applying the inverse process in order to recover the original image.
- Image restoration techniques can be classified into two categories: spatial domain methods and frequency domain methods.
- Spatial domain methods operate directly on the pixels of the image, while frequency domain methods transform the image into its frequency components and then apply filters to remove the noise and blur.
- Image restoration techniques can also be categorized into deterministic methods and probabilistic methods.
- Deterministic methods assume that the degradation model and the parameters are known or can be estimated, and they use mathematical formulas or algorithms to obtain the restored image.
- Probabilistic methods assume that the degradation model and the parameters are unknown or uncertain, and they use statistical or Bayesian methods to infer the restored image based on prior knowledge and likelihood functions.
- Ideally, an image restoration technique will deliver an image that is consistent with available data and constraints (e.g., positivity), and which is free of obvious artifacts.
- Any technique that achieves this should be taken seriously, regardless of whether it is based on an ad hoc procedure or justified by a formalism such as maximum entropy.
- Image restoration techniques should also consider the properties of natural images, such as cross-scale similarity and anisotropic image features, and model them explicitly or implicitly in the restoration process.



### Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Noise is unwanted information in digital images that degrades the quality and clarity of the image .
- Noise can be introduced during image acquisition, coding, transmission, and processing steps   .
- Noise can produce undesirable effects such as artifacts, unrealistic edges, unseen lines, corners, blurred objects and disturbs background scenes.
- To reduce these undesirable effects, prior knowledge of noise models is essential for further processing  .
- Noise models describe the statistical properties of noise and how it affects the image pixels.
- Some common noise models are:
  - Gaussian noise: This noise model assumes that the noise follows a normal or Gaussian distribution with a mean of zero and a standard deviation of sigma. This noise model is suitable for modeling thermal noise or sensor noise .
  - Salt-and-pepper noise: This noise model assumes that the noise is either very high (white) or very low (black) with a certain probability, and unaffected otherwise. This noise model is suitable for modeling transmission errors or faulty pixels.
  - Poisson noise: This noise model assumes that the noise follows a Poisson distribution, which depends on the intensity of the image. This noise model is suitable for modeling photon counting noise or low-light conditions .
  - Speckle noise: This noise model assumes that the noise is multiplicative, meaning that it is proportional to the image intensity. This noise model is suitable for modeling coherent imaging systems such as ultrasound or radar.
  - Uniform noise: This noise model assumes that the noise is uniformly distributed over a certain range. This noise model is suitable for modeling quantization noise or analog-to-digital conversion noise.



### Mean Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Mean filters are a type of spatial filters that are used to smooth images by reducing the amount of intensity variation between neighboring pixels .
- Mean filters work by moving through the image pixel by pixel, replacing each value with the average value of neighboring pixels, including itself .
- Mean filters can be implemented using a kernel or a mask, which is a small matrix that defines the size and shape of the neighborhood to be averaged.
- Mean filters can be classified into different types, such as arithmetic mean, geometric mean, harmonic mean, and contra-harmonic mean, depending on the way the average is calculated.
- Mean filters are useful for reducing noise in images, especially random or Gaussian noise .
- Mean filters can also preserve the edges and details of the image, if the kernel size is small enough.
- However, mean filters can also introduce some drawbacks, such as blurring the image, reducing the contrast, and creating artifacts .
- Mean filters can be improved by using adaptive or bilateral mean filters, which take into account the local variation of the image intensity and the similarity of the pixels.



### Order Statistics for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Image restoration is the process of recovering an image that has been degraded by a degradation phenomenon, such as noise, blur, or distortion.
- Order statistics are the values obtained by sorting a set of data in ascending or descending order. For example, the minimum, maximum, and median are order statistics of a data set.
- Order statistic filters are non-linear spatial filters that operate on the order statistics of the pixels in a local neighborhood of the image. They can be used to remove noise, enhance edges, or smooth regions in an image.
- Some common order statistic filters are:
  - Linear average filter: This filter replaces the center pixel with the average of all the pixels in the neighborhood. It is equivalent to an order statistic filter with equal coefficients for all the pixels. It can reduce noise, but also blurs edges and details.
  - Median filter: This filter replaces the center pixel with the median of the pixels in the neighborhood. It is equivalent to an order statistic filter with coefficients of 1 for the middle pixel and 0 for the rest. It can preserve edges and remove salt-and-pepper noise, but also reduces contrast and sharpness.
  - Max and min filters: These filters replace the center pixel with the maximum or minimum of the pixels in the neighborhood. They are equivalent to order statistic filters with coefficients of 1 for the max or min pixel and 0 for the rest. They can enhance edges and contrast, but also introduce noise and artifacts.
  - Midpoint filter: This filter replaces the center pixel with the average of the maximum and minimum of the pixels in the neighborhood. It is equivalent to an order statistic filter with coefficients of 0.5 for the max and min pixels and 0 for the rest. It can reduce noise and preserve edges, but also reduces contrast and sharpness.
  - Alpha-trimmed mean filter: This filter replaces the center pixel with the average of the pixels in the neighborhood after discarding the highest and lowest alpha percent of the pixels. It is equivalent to an order statistic filter with coefficients of 1/(n-2a) for the remaining pixels and 0 for the rest, where n is the number of pixels in the neighborhood and a is the number of pixels to be trimmed. It can reduce noise and preserve edges, but also reduces contrast and sharpness.
- Higher order statistics are the statistics that involve more than two moments of a data set, such as skewness, kurtosis, or cumulants. They can capture the non-Gaussian features of the data, such as asymmetry, outliers, or dependencies.
- Higher order statistics can be used for image restoration by measuring the deviation of the pixels from the background or the expected distribution. For example, blind deconvolution can be used to restore color images by using higher order statistics to identify the noise pixels and estimate the blur kernel. Higher order statistics can also be used to detect and restore the statistical properties of stego images, which are images that contain hidden messages.



### Adaptive filters for image restoration

- Adaptive filters are commonly used in image processing to enhance or restore data by removing noise without significantly blurring the structures in the image .
- Adaptive filters adjust their parameters or coefficients according to the characteristics of the input image or the noise model.
- Adaptive filters can be classified into two categories: spatial domain filters and frequency domain filters.
- Spatial domain filters operate directly on the pixel values of the image and use a local neighborhood to estimate the noise level and the filter output.
- Frequency domain filters transform the image into the frequency domain and apply a filter function that depends on the frequency components and the noise spectrum.
- Some examples of spatial domain adaptive filters are adaptive median filter, adaptive Wiener filter, adaptive bilateral filter, and adaptive anisotropic diffusion filter  .
- Some examples of frequency domain adaptive filters are adaptive notch filter, adaptive bandpass filter, adaptive lowpass filter, and adaptive highpass filter.
- The main advantage of adaptive filters is that they can adapt to the varying noise conditions and image features, and achieve better performance than fixed filters .
- The main challenge of adaptive filters is to design a suitable criterion or algorithm for updating the filter parameters or coefficients, and to balance the trade-off between noise reduction and detail preservation .



### Band reject Filters

- A band reject filter is a type of frequency domain filter that blocks or attenuates a range of frequencies in an image and lets the other frequencies pass through .
- A band reject filter is useful when the general location of the noise in the frequency domain is known .
- A band reject filter can be implemented by adding a low-pass filter and a high-pass filter with different cutoff frequencies.
- A band reject filter can be either ideal, Gaussian, or Butterworth, depending on the shape and smoothness of the filter function.
- A band reject filter can be applied to a one-channel image by using the BANDREJECT_FILTER function in IDL.
- A band reject filter can be used to remove periodic noise or interference patterns from an image .



Hello, I am Sydney, your AI assistant. I can help you with your topic of band pass filters for image processing. Here are some notes that you can use for your study material:

### Band pass filters for image processing

- Band pass filters are filters that allow only a certain range of frequencies to pass through, while attenuating the frequencies below and above that range.
- Band pass filters can be used to enhance image features such as edges and blobs, or to reduce noise and illumination artifacts.
- Band pass filters can be implemented in the spatial domain or the frequency domain, depending on the application and the desired effect.
- In the spatial domain, band pass filters can be obtained by multiplying a low pass filter with a high pass filter, where the low pass filter has a higher cut off frequency than the high pass filter.
- In the frequency domain, band pass filters can be obtained by applying a circular or elliptical mask to the Fourier transform of the image, where the mask has a radius or a major and minor axis that correspond to the desired frequency range.
- Band pass filters can be designed with different shapes and characteristics, such as Gaussian, Butterworth, Chebyshev, etc., depending on the trade-off between the sharpness of the cut-off and the amount of ripple in the passband.
- Band pass filters can also be adaptive, meaning that they can adjust themselves to suit the local signal conditions in the image, without prior knowledge of the signal statistics. This can improve the performance of the filter in the presence of noise or varying illumination.



### Notch Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- A notch filter is an image processing filter that is used to remove specific frequency components from an image .
- A notch filter is a type of band-stop filter that is designed to remove a specific range of frequencies from an image while leaving the rest of the image unaffected.
- A notch filter can be used to remove periodic noise or unwanted patterns from an image .
- A notch filter can be implemented in the frequency domain by multiplying the Fourier transform of the image by a notch filter function .
- A notch filter function can be designed using different methods, such as ideal, Butterworth, or Gaussian .
- An ideal notch filter function has a value of zero at the frequencies to be removed and a value of one at all other frequencies.
- A Butterworth notch filter function has a smooth transition between the passband and the stopband, and its sharpness can be controlled by a parameter called the order .
- A Gaussian notch filter function has a bell-shaped curve that attenuates the frequencies to be removed, and its width can be controlled by a parameter called the standard deviation .
- A notch filter can be applied to an image by creating a notch filter function that matches the frequency and orientation of the noise or pattern to be removed, and then multiplying it with the Fourier transform of the image.
- A notch filter can be applied to multiple frequencies or patterns by creating a composite notch filter function that combines multiple notch filter functions .
- A notch filter can improve the quality of an image by removing unwanted frequency components, but it can also introduce artifacts or distortions if the notch filter function is not designed properly .



### Optimum Notch Filtering

- Optimum notch filtering is a technique for reducing periodic noise in images by minimizing the local variance of the restored image .
- Periodic noise is a type of noise that has a regular pattern in the spatial or frequency domain, such as interference lines, moiré patterns, or screen flicker.
- Optimum notch filtering consists of three steps :
  - Identifying the regions of noise frequencies by analyzing the spectrum of the noisy image.
  - Extracting the repetitive pattern of the periodic noise by applying a notch-pass filter on every noise frequency and then applying an inverse 2-D Fourier transform.
  - Restoring the output image by subtracting a variable weighted portion of the repetitive pattern from the contaminated image.
- A notch-pass filter is a type of filter that passes a very narrow set of frequencies around a center frequency, while rejecting all other frequencies.
- A notch-pass filter can be designed by multiplying a low-pass filter and a high-pass filter, both with the same center frequency and bandwidth.
- A notch-pass filter can also be designed by using a Gaussian function with a negative amplitude and a specified center frequency and standard deviation.
- The optimum weight for subtracting the repetitive pattern from the noisy image can be determined by minimizing the mean square error between the original image and the restored image .
- Optimum notch filtering can effectively remove periodic noise from images without affecting the image details or introducing artifacts .



### Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- The basic idea of inverse filtering is to apply the inverse of the blurring filter to the blurred image, assuming that the filter is invertible .
- Inverse filtering can be performed in the frequency domain, by multiplying the Fourier transform of the blurred image by the inverse of the Fourier transform of the blurring filter .
- Inverse filtering can produce accurate results when the blurring filter is known and there is no noise in the image .
- However, inverse filtering is very sensitive to additive noise, as it tends to amplify the high-frequency components of the noise .
- To overcome this problem, some variations of inverse filtering have been proposed, such as truncated inverse filtering, Wiener filtering, and least squares filtering  .
- Truncated inverse filtering sets the inverse filter to zero for frequencies where the blurring filter is very small, to avoid dividing by very small numbers.
- Wiener filtering incorporates a prior model of the noise and the original image, and minimizes the mean squared error between the restored image and the original image.
- Least squares filtering minimizes the squared difference between the blurred image and the filtered image, subject to some regularization constraints.



### Wiener filtering

- Wiener filtering is a technique for image restoration that aims to reduce the mean square error between the restored image and the original image .
- Wiener filtering can be applied to images that are degraded by a known linear filter and additive noise .
- Wiener filtering involves estimating the power spectra of the original image and the noise, and using them to design a filter that minimizes the restoration error .
- Wiener filtering can be implemented in the frequency domain by multiplying the Fourier transform of the degraded image by a Wiener filter function .
- The Wiener filter function is given by :

$$
H_w(u,v) = \frac{H^*(u,v)S_f(u,v)}{|H(u,v)|^2S_f(u,v)+S_n(u,v)}
$$

where $H(u,v)$ is the degradation function, $H^*(u,v)$ is its complex conjugate, $S_f(u,v)$ is the power spectrum of the original image, and $S_n(u,v)$ is the power spectrum of the noise.

- Wiener filtering can also be implemented in the spatial domain by using a convolution kernel that approximates the inverse of the degradation function.
- Wiener filtering can improve the quality of images that are blurred and noisy, but it requires accurate knowledge of the degradation function and the noise characteristics .
- Wiener filtering can also be extended to blind deconvolution, where the degradation function is unknown and has to be estimated from the degraded image.



## Unit 4 - IMAGE SEGMENTATION

- Image segmentation is the process of partitioning an image into multiple segments, each of which consists of pixels that share some common characteristics .
- Image segmentation is typically used to locate objects and boundaries in images, such as edges, contours, regions, or regions of interest (ROI) .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be performed using various techniques, such as thresholding, clustering, region growing, edge detection, watershed, active contours, graph cuts, or deep learning  .
- Image segmentation can be classified into two types: semantic segmentation and instance segmentation.
  - Semantic segmentation assigns a class label to each pixel in the image, such as sky, road, car, person, etc. Semantic segmentation does not distinguish between different instances of the same class.
  - Instance segmentation assigns a class label and an instance identifier to each pixel in the image, such as car1, car2, person1, person2, etc. Instance segmentation can separate different instances of the same class.



### Edge detection

- Edge detection is a fundamental tool in image processing, machine vision and computer vision, particularly in the areas of feature detection and feature extraction.
- Edge detection is a method of segmenting an image into regions of discontinuity, where there is a significant change in the gray level.
- Edge detection allows users to observe the features of an image, such as boundaries, contours, outlines, and shapes.
- Edge detection is one of the steps in image analysis, image pattern recognition, and computer vision techniques.
- Edge detection involves computing an image gradient, which quantifies the magnitude and direction of edges in an image.
- Image gradients are used in various downstream tasks in computer vision, such as line detection, feature detection, object detection, segmentation, and recognition.
- Edge detection can be classified as either viewpoint dependent or viewpoint independent, depending on whether the edges extracted from a two-dimensional image of a three-dimensional scene are affected by the perspective or not.
- Edge detection can be performed using various operators, such as Sobel, Prewitt, Roberts, Canny, Laplacian of Gaussian, and Zero-crossing .
- Edge detection operators work by applying a filter or a mask to the image, which calculates the difference between neighboring pixels or regions .
- Edge detection operators have different characteristics, such as sensitivity, noise suppression, localization, and detection of thin or thick edges .
- Edge detection operators can be evaluated based on various criteria, such as accuracy, completeness, consistency, and computational complexity .



### Edge linking via Hough transform

- Edge linking is the process of connecting edge pixels in an image to form continuous curves or contours that represent the boundaries of objects or regions.
- Edge linking can be done by local or global methods. Local methods analyze the neighborhood of each edge pixel and link it to another edge pixel based on some criteria, such as gradient direction, intensity difference, or distance. Global methods use a parameter space to represent all possible curves that can pass through the edge pixels, and then find the optimal curves that maximize some objective function, such as the number of edge pixels or the smoothness of the curve.
- Hough transform is a global method for edge linking that can detect lines, circles, ellipses, or other shapes in an image. The basic idea of Hough transform is to map each edge pixel in the image space to a set of curves in the parameter space, and then find the peaks or maxima in the parameter space that correspond to the most likely curves in the image space.
- For example, to detect lines in an image, the parameter space can be defined by the polar coordinates of the lines, i.e., the distance r and the angle θ from the origin. Each edge pixel (x, y) in the image space can be mapped to a sinusoidal curve in the parameter space, given by r = x cos θ + y sin θ. The intersection of the curves from different edge pixels indicates a possible line in the image space. The more edge pixels that map to the same intersection, the higher the value of the parameter space at that point, and the more likely that a line exists in the image space.
- The steps of Hough transform for line detection are as follows:

  1. Apply an edge detector to the input image and obtain a binary edge map.
  2. Define the parameter space by discretizing the range of r and θ into a two-dimensional array or accumulator.
  3. For each edge pixel (x, y) in the edge map, compute the corresponding curve r = x cos θ + y sin θ in the parameter space, and increment the accumulator value for each (r, θ) pair along the curve.
  4. Find the local maxima or peaks in the accumulator that exceed a certain threshold, and obtain the corresponding (r, θ) pairs that represent the detected lines in the image space.
  5. Optionally, apply some post-processing techniques to refine the detected lines, such as merging, splitting, or smoothing.

- Hough transform can be extended to detect other shapes, such as circles, ellipses, or arbitrary curves, by using different parameterizations of the curves and different accumulator structures. However, the complexity and memory requirements of the Hough transform increase with the number of parameters and the resolution of the parameter space. Therefore, some variations and optimizations of the Hough transform have been proposed, such as the randomized Hough transform, the progressive probabilistic Hough transform, or the generalized Hough transform.



### Thresholding for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Image segmentation is the process of dividing an image into meaningful regions or segments based on some criteria, such as color, intensity, texture, etc.
- Image thresholding is a type of image segmentation that divides the foreground from the background in an image by using a threshold value.
- A threshold value is a pixel intensity level that separates the pixels into two groups: those above the threshold (foreground) and those below the threshold (background).
- A binary image is one whose pixels have only two values: 0 and 1. A binary image can be obtained from a grayscale image by applying a thresholding operation.
- There are different types of thresholding methods, such as global thresholding, local thresholding, adaptive thresholding, etc.
- Global thresholding is a simple and widely used method that applies the same threshold value to the whole image. It is suitable for images with uniform illumination and contrast.
- Local thresholding is a method that applies different threshold values to different regions of the image based on the local characteristics of the image. It is suitable for images with varying illumination and contrast.
- Adaptive thresholding is a method that adjusts the threshold value dynamically according to the image content and context. It is suitable for images with complex and non-uniform backgrounds.
- Some examples of thresholding algorithms are Otsu's method, Kapur's method, entropy-based method, etc.
- Otsu's method is a global thresholding method that chooses the threshold value that minimizes the within-class variance of the pixel intensities.
- Kapur's method is an entropy-based method that chooses the threshold value that maximizes the sum of the entropies of the foreground and background regions.
- Entropy is a measure of the uncertainty or randomness of a system. Higher entropy means more information content and less predictability.



### Region based segmentation for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Region based segmentation is a technique for determining the regions directly from the image pixels, without using edge detection.
- Region based segmentation methods look for similarities between adjacent pixels, such as intensity, color, texture, etc., and group them into unique regions .
- Region based segmentation methods can be classified into two types: region growing and region splitting and merging .
- Region growing is a method that starts with some initial seed points, and grows the regions by adding neighboring pixels that satisfy some homogeneity criteria. The process stops when no more pixels can be added to any region.
- Region splitting and merging is a method that starts with the whole image as a single region, and recursively splits it into smaller regions if they are not homogeneous, or merges adjacent regions if they are homogeneous. The process stops when no more splitting or merging can be done.
- Region based segmentation methods are simple and fast, but they may suffer from over-segmentation or under-segmentation, depending on the choice of seed points, homogeneity criteria, and stopping conditions.
- Region based segmentation methods are also sensitive to noise and image artifacts, which may affect the region boundaries and homogeneity.
- Region based segmentation methods can be improved by using edge information, multi-resolution analysis, or adaptive thresholding.



### Region growing

- Region growing is a region-based image segmentation method that involves the selection of initial seed points and the expansion of regions based on predefined criteria.
- The basic steps of region growing are :
  - Choose one or more seed pixels as the starting points for the regions.
  - Define a similarity measure or a predicate function to determine whether a pixel belongs to a region or not.
  - For each seed pixel, examine its neighboring pixels and add them to the region if they satisfy the similarity measure.
  - Repeat the previous step for the newly added pixels until no more pixels can be added to any region.
  - Optionally, merge adjacent regions that have weak boundaries or similar characteristics.
- Region growing is a simple and intuitive method, but it has some drawbacks :
  - The choice of seed pixels can affect the quality and efficiency of the segmentation. If the seed pixels are not representative of the regions, the segmentation may be inaccurate or incomplete.
  - The similarity measure or the predicate function may be difficult to define for complex or noisy images. If the similarity measure is too strict, the regions may be fragmented. If the similarity measure is too loose, the regions may be overgrown or merged.
  - The computational cost of region growing may be high, especially for large images or images with many regions. The algorithm may require multiple passes over the image or a large amount of memory to store the regions.



### Region splitting and merging for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Image segmentation is the process of partitioning a digital image into multiple regions (sets of pixels) that are homogeneous and meaningful.
- Region splitting and merging is an image segmentation technique that uses a divide and conquer approach.
- The technique involves the following steps :
  - Start with the whole image as a single region.
  - Split the region into four subregions if it is not homogeneous, i.e., if it does not satisfy a predefined criterion of similarity or uniformity.
  - Repeat the splitting process recursively for each subregion until no more splitting is possible or a minimum size is reached.
  - Merge adjacent regions that are similar, i.e., if they satisfy a predefined criterion of compatibility or closeness.
  - Repeat the merging process until no more merging is possible or a desired level of detail is achieved.
- The technique uses a quadtree data structure to store the regions and their relationships.
- The technique can handle images with different types of regions, such as smooth, textured, or noisy.
- The technique can be implemented using different homogeneity and compatibility criteria, such as intensity, color, texture, shape, or edge strength .
- The technique can be improved by using adaptive splitting and merging, i.e., adjusting the criteria based on the local characteristics of the image.
- The technique has some advantages and disadvantages :
  - Advantages:
    - It can produce accurate and detailed segmentation results for complex images.
    - It can handle images with different types of regions and noise levels.
    - It can be easily parallelized and distributed.
  - Disadvantages:
    - It can be computationally expensive and time-consuming.
    - It can be sensitive to the choice of criteria and parameters.
    - It can produce over-segmentation or under-segmentation depending on the criteria and parameters.



### Morphological processing- erosion and dilation

- Morphological processing is a technique of image processing that uses the shape and structure of the image objects to modify or enhance the image .
- The most basic morphological operations are erosion and dilation .
- Erosion is the process of removing pixels from the boundaries of the foreground objects in an image . It can be used to eliminate small noises, detach two connected objects, or thin out an object.
- Dilation is the process of adding pixels to the boundaries of the foreground objects in an image . It can be used to fill small holes, connect disjointed objects, or thicken an object.
- The amount of erosion or dilation depends on the size and shape of the structuring element, which is a small binary image that defines the neighborhood of each pixel .
- Erosion and dilation can be combined to form more complex morphological operations, such as opening, closing, gradient, top-hat, and black-hat .
- Morphological processing can be used for image segmentation, which is the process of dividing an image into meaningful regions or objects . It can help to separate the foreground from the background, or to identify different objects in the image .
- Morphological processing can also be used for image enhancement, which is the process of improving the quality or appearance of an image . It can help to reduce noise, sharpen edges, or highlight features in the image .



### Segmentation by morphological watersheds

- Segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as brightness, color, texture, etc.  
- Morphological watersheds are a segmentation technique that uses the concept of topographic relief to partition an image into catchment basins and watershed lines.  
- A catchment basin is a region where all the water flows to a single minimum point, and a watershed line is a boundary that separates adjacent catchment basins.  
- The idea of morphological watersheds is to imagine the image as a landscape, where the pixel intensity represents the height, and to flood the landscape from its local minima with water of different colors.   
- The water from different minima will eventually meet at some points, forming the watershed lines. These lines mark the boundaries of the segmented regions.   
- The morphological watersheds can be computed using various methods, such as distance transform, gradient magnitude, markers, or image smoothing.    
- The advantages of morphological watersheds are that they are fast, robust, and can handle complex shapes and textures.  
- The disadvantages of morphological watersheds are that they are sensitive to noise and can produce over-segmentation or under-segmentation depending on the choice of parameters.



### Basic Concepts for the Notes of the Unit 4 - Image Segmentation in the Subject of Image Processing

- Image segmentation is the process of partitioning an image into multiple segments, each of which consists of pixels that share some common characteristics .
- Image segmentation is typically used to locate objects and boundaries in images, such as lines, curves, edges, regions, etc .
- Image segmentation can reduce the complexity of the image and enable further processing or analysis of each image segment.
- Image segmentation can be performed based on different criteria, such as pixel intensity, color, texture, shape, etc .
- Image segmentation can be classified into two main types: supervised and unsupervised .
  - Supervised image segmentation is based on prior knowledge or training data, such as labels, masks, or annotations, that specify the desired segments or classes for each pixel .
  - Unsupervised image segmentation is based on intrinsic properties or features of the image, such as clustering, thresholding, or region growing, that group pixels into segments without any external guidance .
- Image segmentation can be evaluated using different metrics, such as accuracy, precision, recall, F1-score, IoU, etc., that measure the similarity or overlap between the predicted segments and the ground truth segments .
- Image segmentation can be applied to various domains and applications, such as medical imaging, remote sensing, face recognition, object detection, etc .



### Dam construction for the notes of the Unit 4 - IMAGE SEGMENTATION in the subject of Image Processing

- Image segmentation is the process of dividing an image into meaningful regions or objects based on some criteria, such as color, intensity, texture, shape, etc.
- Image segmentation has many applications, such as object detection, recognition, tracking, medical imaging, remote sensing, etc.
- One of the methods for image segmentation is watershed segmentation, which is based on the analogy of a landscape with hills and valleys, where the height of each pixel represents its intensity value.
- Watershed segmentation works by flooding the landscape from its local minima (the lowest points), and building dams to prevent the merging of different regions. These dams are the boundaries of the image objects.
- Watershed segmentation can be implemented by using different techniques, such as distance transform, gradient, markers, etc.
- Distance transform is a method that assigns each pixel a value equal to its distance to the nearest boundary pixel. This can help to identify the local minima and the catchment basins (the regions that are flooded by the same source).
- Gradient is a method that computes the rate of change of intensity at each pixel. This can help to identify the edges and the ridges (the highest points) of the landscape.
- Markers are a method that uses some prior information or user input to specify the seeds (the starting points) of the flooding process. This can help to avoid over-segmentation and noise.
- Watershed segmentation can be performed by using monographical procedure or Matlab. Monographical procedure is a step-by-step graphical illustration of the flooding and dam building process. Matlab is a software that can execute the watershed segmentation algorithm by using built-in functions or custom codes.
- An example of watershed segmentation by monographical procedure is shown below:

Watershed segmentation by monographical procedure

- An example of watershed segmentation by Matlab is shown below:

Watershed segmentation by Matlab

- Some of the advantages of watershed segmentation are that it is simple, fast, and can handle complex shapes and topologies. Some of the disadvantages are that it is sensitive to noise, over-segmentation, and parameter selection.



### Watershed segmentation algorithm

- Watershed segmentation is a classical algorithm used for separating different objects in an image .
- The algorithm treats pixel values as a local topography (elevation), where high intensity denotes peaks and hills, and low intensity denotes valleys  .
- The algorithm starts from user-defined markers, which are pixels that belong to different objects .
- The algorithm floods basins from the markers until basins attributed to different markers meet on watershed lines, which are the boundaries of the objects .
- The algorithm can be applied to any grayscale image, such as the gradient magnitude of the original image  .
- The algorithm can be implemented using the OpenCV library, which provides the cv.watershed() function .
- The algorithm can be used for various applications, such as counting the objects, measuring their size and shape, or performing further analysis on the separated objects .



## Unit 5 - IMAGE COMPRESSION AND RECOGNITION

- Image compression is the process of reducing the file size of an image while still trying to preserve the quality of the image.
- Image compression is useful for saving storage space, reducing bandwidth requirements, and improving the efficiency of image processing algorithms.
- Image compression can be classified into two types: lossless and lossy.
  - Lossless compression preserves the exact information of the original image, but achieves a lower compression ratio.
  - Lossy compression discards some information of the original image, but achieves a higher compression ratio.
- Image compression can be performed by applying the following basic steps:
  - Applying an image transform to convert the image from the spatial domain to another domain, such as the frequency domain or the wavelet domain.
  - Quantizing the transformed coefficients to reduce the number of bits required to represent them.
  - Encoding the quantized coefficients using a suitable coding scheme, such as Huffman coding or arithmetic coding.
- Image recognition is the process of identifying and classifying objects, faces, scenes, or actions in an image.
- Image recognition is a subfield of computer vision and machine learning that has many applications, such as face recognition, object detection, scene understanding, and image retrieval.
- Image recognition can be performed by applying the following basic steps:
  - Preprocessing the image to enhance the quality, normalize the size, and extract features.
  - Applying a recognition model to classify the image or detect the regions of interest.
  - Postprocessing the recognition results to refine the accuracy, eliminate the false positives, and generate the output.
- Image recognition can be based on traditional methods, such as template matching, histogram of oriented gradients, or scale-invariant feature transform.
- Image recognition can also be based on deep learning methods, such as convolutional neural networks, generative adversarial networks, or transformers.
- Deep learning methods have achieved remarkable performance in image recognition, surpassing the traditional methods in many tasks.
- Deep learning methods can also be used for image compression, by learning the optimal transform, quantization, and encoding functions from the data.
- Deep learning methods can also be used for recognition-aware image compression, by optimizing the compression quality for a specific recognition task, such as classification, object detection, or superresolution.



### Need for data compression

- Data compression is the process of reducing the number of bits needed to represent data by using encoding techniques.
- Data compression can be either lossless or lossy. Lossless compression preserves the original information without any distortion, while lossy compression discards some information to achieve higher compression ratios.
- Data compression is needed for various reasons, such as:
  - Saving storage space and cost: Compressing data can reduce the amount of memory or disk space required to store the data, which can lower the hardware expenses and maintenance costs.
  - Improving transmission speed and efficiency: Compressing data can reduce the amount of bandwidth or time needed to transmit the data over a network or a communication channel, which can improve the performance and reliability of the system.
  - Enhancing security and privacy: Compressing data can make the data more difficult to access or interpret by unauthorized parties, which can protect the confidentiality and integrity of the data.
- Data compression is especially important for image processing, because images typically contain a large amount of data that can be redundant or irrelevant for certain applications. Some examples of image compression techniques are:
  - Run-length encoding: A simple lossless compression method that replaces consecutive identical pixels with a single value and a count of how many times it occurs.
  - Huffman coding: A lossless compression method that assigns variable-length codes to pixels based on their frequencies, such that more common pixels have shorter codes and less common pixels have longer codes.
  - JPEG: A lossy compression standard that divides an image into blocks and applies discrete cosine transform (DCT) and quantization to each block, followed by Huffman coding or arithmetic coding to the resulting coefficients.
  - PNG: A lossless compression standard that applies a filter to each row of pixels to reduce the correlation between adjacent pixels, followed by Huffman coding or deflate algorithm to the filtered data.
  - GIF: A lossy compression standard that reduces the number of colors in an image to a maximum of 256, followed by Lempel-Ziv-Welch (LZW) algorithm to the indexed data.



### Huffman Coding for Image Compression

Huffman coding is a lossless data compression technique that assigns variable-length codes to the symbols based on their frequencies of occurrence. The symbols with higher frequencies are assigned shorter codes, while the symbols with lower frequencies are assigned longer codes. This reduces the average code length and the number of bits required to store or transmit the data.

The steps involved in Huffman coding for image compression are:

- **Step 1**: Obtain the image and convert it to grayscale if it is colored. This reduces the number of possible pixel values from 256^3 to 256.
- **Step 2**: Calculate the frequency of each pixel value in the image. This can be done by creating a histogram of the pixel values and counting the number of pixels for each value.
- **Step 3**: Sort the pixel values in ascending order of their frequencies. The pixel values with the lowest frequencies are placed at the bottom of the list, while the pixel values with the highest frequencies are placed at the top of the list.
- **Step 4**: Create a binary tree by combining the two pixel values with the lowest frequencies into a single node. The node is assigned a frequency equal to the sum of the frequencies of its children. The left child is assigned a bit value of 0, while the right child is assigned a bit value of 1. Repeat this process until there is only one node left, which is the root of the tree.
- **Step 5**: Traverse the binary tree from the root to the leaves and assign a code to each pixel value by concatenating the bit values along the path. The code for a pixel value is the sequence of bits from the root to the leaf corresponding to that value.
- **Step 6**: Encode the image by replacing each pixel value with its code. The encoded image is a sequence of bits that can be stored or transmitted using less space than the original image.
- **Step 7**: Decode the image by traversing the binary tree from the root to the leaves and matching the codes with the pixel values. The decoded image is a grayscale image that is identical to the original image.



### Run Length Encoding

- Run length encoding (RLE) is a simple and lossless compression technique that reduces the size of an image by replacing consecutive identical pixels with a single code that indicates the pixel value and the number of repetitions.
- RLE is suitable for images that have large areas of uniform color or intensity, such as line drawings, cartoons, or text documents.
- RLE can be applied to either binary or grayscale images, but the compression ratio depends on the image characteristics and the coding scheme used.
- RLE can be performed in either row-wise or column-wise direction, depending on the image orientation and the pixel distribution.
- RLE can be classified into two types: fixed-length and variable-length coding.
  - Fixed-length coding uses a fixed number of bits to represent the pixel value and the run length. For example, if each pixel value is 8 bits and the run length is 4 bits, then each run can be encoded with 12 bits. The advantage of fixed-length coding is that it is easy to implement and decode, but the disadvantage is that it may waste bits if the run length is shorter than the maximum value allowed by the code.
  - Variable-length coding uses a variable number of bits to represent the pixel value and the run length, depending on the frequency of occurrence. For example, a common scheme is to use one bit to indicate whether the pixel value is the same as the previous one or not, and then use a variable number of bits to encode the run length if the pixel value is different. The advantage of variable-length coding is that it can achieve higher compression ratios for images with long runs, but the disadvantage is that it is more complex to implement and decode, and it may require additional bits to indicate the end of the code.



### Shift codes for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Image compression is the process of reducing the amount of data required to represent an image, without compromising its quality or information content.
- Image compression can be classified into two types: lossless and lossy.
- Lossless image compression preserves the exact pixel values of the original image, and allows perfect reconstruction of the image after decompression.
- Lossy image compression discards some of the pixel values of the original image, and introduces some distortion or error in the reconstructed image after decompression.
- Shift coding is a technique for lossless image compression, based on the idea of shifting the pixel values of an image to reduce the number of bits required to represent them.
- Shift coding can be applied in two ways: using leading short word (LSW) or using lead bit (LB).
- LSW shift coding works by finding the minimum and maximum pixel values in the image, and subtracting the minimum value from all the pixel values. This shifts the pixel values to the range [0, max-min]. Then, the number of bits required to represent the maximum value (which is also the range) is appended to the beginning of the compressed data, followed by the shifted pixel values.
- LB shift coding works by finding the most significant bit (MSB) position of the pixel values in the image, and shifting all the pixel values to the right by that position. This shifts the pixel values to the range [0, 2^MSB]. Then, the MSB position is appended to the beginning of the compressed data, followed by the shifted pixel values.
- Shift coding can reduce the number of bits required to represent an image, especially if the image has a small dynamic range (i.e., the difference between the minimum and maximum pixel values is small).
- Shift coding can be combined with other techniques, such as run-length encoding (RLE) or Huffman coding, to further compress the image data. RLE works by encoding the repeated pixel values as a pair of value and count, while Huffman coding works by assigning variable-length codes to the pixel values based on their frequencies.



### Arithmetic coding for image compression

- Arithmetic coding is a lossless compression technique that assigns variable-length codes to symbols based on their probabilities of occurrence.
- Arithmetic coding can achieve higher compression ratios than Huffman coding, especially for small and skewed alphabets.
- Arithmetic coding encodes an entire file or image as a single decimal number between 0 and 1, by recursively subdividing the interval according to the symbol probabilities.
- Arithmetic coding can be combined with other compression methods, such as discrete cosine transform (DCT) and run-length encoding (RLE), to improve the performance for image compression .
- Arithmetic coding can be adapted to the context of the image, by using different probability models for different regions or blocks of pixels.
- Arithmetic coding requires more computation and memory than Huffman coding, and may suffer from precision issues for very long sequences.



### JPEG standard

- JPEG stands for Joint Photographic Experts Group, which was a group of image processing experts that devised a standard for compressing images (ISO) .
- JPEG is not really a file format but rather an image compression standard that specifies the codec, which defines how an image is compressed into a stream of bytes and decompressed back into an image.
- JPEG is a lossy image compression method, which means that some information is discarded during the compression process, resulting in a smaller file size but also a loss of quality .
- JPEG compression works by averaging color variation and blocking together groups of pixels with a more uniform color, so that it doesn’t have to store as many different ones .
- JPEG compression has many different options and color space regulations, such as the level of compression, the quality factor, the subsampling ratio, the block size, the quantization matrix, the Huffman coding, etc  .
- JPEG compression is suitable for natural images that have smooth variations of tone and color, but not for images that have sharp edges or text, as they may introduce artifacts or blurring .
- JPEG compression is widely used for storing and transmitting digital images, such as photographs, web graphics, etc .



### MPEG

- MPEG stands for Moving Picture Experts Group, a group of experts that develops standards for digital video and audio compression.
- MPEG formats are designed to compress and transmit moving images and sound with high quality and efficiency.
- MPEG compression algorithms exploit both spatial and temporal redundancy in video data to reduce the amount of bits required to represent them.
- Spatial redundancy refers to the similarity of neighboring pixels within a frame, while temporal redundancy refers to the similarity of successive frames in a video sequence.
- MPEG compression methods use the following steps :
  - Mode selection: The input frame is divided into 16x16 pixel blocks called macroblocks, which can be encoded in different modes depending on the content and motion of the block.
  - Motion estimation and compensation: For each macroblock, the encoder searches for a matching block in the previous and/or future frames, and calculates the motion vector that represents the displacement of the block. The motion vector is encoded and transmitted, along with the difference between the current block and the predicted block.
  - Discrete cosine transform (DCT): The difference block is transformed from the spatial domain to the frequency domain using the DCT, which converts the pixel values into a set of coefficients that represent the amplitude and phase of cosine waves of different frequencies.
  - Quantization: The DCT coefficients are scaled and rounded to integer values, which reduces the precision and the number of bits needed to represent them. The quantization step is the main source of loss in MPEG compression, as some information is discarded during this process.
  - Zig-zag scan and run-length encoding: The quantized coefficients are scanned in a zig-zag order, which groups the low-frequency coefficients (which tend to have larger values) at the beginning and the high-frequency coefficients (which tend to have smaller or zero values) at the end. The coefficients are then encoded using run-length encoding, which replaces sequences of zeros with a pair of values that indicate the length and the value of the run.
  - Variable-length coding (VLC): The run-length encoded coefficients and the motion vectors are encoded using VLC, which assigns shorter codes to more frequent symbols and longer codes to less frequent symbols. This reduces the average number of bits per symbol and increases the compression ratio.
- MPEG formats also use chroma subsampling to reduce the color information in the video, as the human eye is more sensitive to brightness than to color. Chroma subsampling separates the brightness (luma) and the color (chroma) components of the video, and reduces the resolution of the chroma components.
- MPEG has several versions, each with different features and applications. Some of the most common ones are:
  - MPEG-1: The first MPEG standard, which supports video and audio compression at up to 1.5 Mbps. It is mainly used for video CDs and digital audio broadcasting.
  - MPEG-2: An extension of MPEG-1, which supports higher bit rates and resolutions, as well as interlaced video and multiple audio channels. It is mainly used for digital TV, DVD and Blu-ray discs.
  - MPEG-4: A more advanced and versatile standard, which supports object-based coding, scalability, error resilience, and various types of media (such as video, audio, text, graphics, etc.). It is mainly used for streaming, multimedia messaging, and interactive applications.



### Boundary representation

- Boundary representation is a method for representing a 3D shape by defining the limits of its volume.
- A boundary representation of a model comprises topological components (faces, edges and vertices) and the connections between them, along with geometric definitions for those components (surfaces, curves and points, respectively).
- A face is a bounded portion of a surface; an edge is a bounded piece of a curve and a vertex lies at a point.
- Boundary representation is useful for solid modeling and computer-aided design, as it allows for efficient manipulation and analysis of 3D shapes.
- Boundary representation can also be applied to 2D images, where the boundary is the line or location dividing the two surfaces.
- Extracting the boundary is an important process to gain information and understand the feature of an image.
- It is the first process in preprocessing to present the image’s characteristics.
- This process can help the researcher to acquire data from the image.
- Boundary extraction can be done using various techniques, such as thresholding, morphological operations, edge detection, contour tracing, etc  .
- Boundary extraction can be used for various applications, such as object recognition, segmentation, shape analysis, compression, etc  .



### Boundary description for the notes of the Unit 5 - IMAGE COMPRESSION AND RECOGNITION in the subject of Image Processing

- Image compression is the process of reducing the amount of data required to represent an image, while maintaining its quality and information content.
- Image recognition is the process of identifying and classifying objects, faces, scenes, or activities in an image, using machine learning algorithms and models.
- The notes of the Unit 5 cover the following topics:

  - The need and benefits of image compression, such as saving storage space, bandwidth, and transmission time, and enhancing security and privacy.
  - The types and methods of image compression, such as lossless and lossy compression, run-length encoding, Huffman coding, arithmetic coding, Lempel-Ziv-Welch (LZW) algorithm, JPEG standard, discrete cosine transform (DCT), quantization, entropy coding, JPEG 2000 standard, wavelet transform, embedded zerotree wavelet (EZW) algorithm, and fractal compression.
  - The evaluation and comparison of image compression techniques, such as compression ratio, bit rate, peak signal-to-noise ratio (PSNR), mean squared error (MSE), structural similarity index (SSIM), and subjective quality assessment.
  - The applications and challenges of image compression, such as medical imaging, satellite imaging, video conferencing, digital photography, and image watermarking.
  - The basic concepts and techniques of image recognition, such as feature extraction, feature selection, feature matching, classification, and recognition.
  - The types and methods of image recognition, such as template matching, correlation, histogram of oriented gradients (HOG), scale-invariant feature transform (SIFT), speeded up robust features (SURF), local binary patterns (LBP), convolutional neural networks (CNN), deep learning, and transfer learning.
  - The evaluation and comparison of image recognition techniques, such as accuracy, precision, recall, F1-score, confusion matrix, receiver operating characteristic (ROC) curve, and area under the curve (AUC).
  - The applications and challenges of image recognition, such as face recognition, optical character recognition (OCR), scene understanding, object detection, segmentation, and tracking.



### Fourier Descriptor

- Fourier descriptor is a method used in object recognition and image processing to represent the boundary shape of a segment in an image .
- It is based on the Fourier series of the boundary curve of the segment, which can be obtained by sampling the boundary points and applying the discrete Fourier transform .
- The Fourier coefficients of the boundary curve are called the Fourier descriptors, and they can be used as features for shape analysis and comparison .
- Fourier descriptors have some advantages over other shape representation methods, such as:
  - They can be made invariant to translation, scale, rotation and starting point by applying some normalization techniques .
  - They can capture both global and local shape information by using different frequency components .
  - They can reduce the dimensionality of the shape representation by selecting only the most significant descriptors .
- Fourier descriptors also have some limitations, such as:
  - They are sensitive to noise and boundary irregularities, which may affect the accuracy of the shape recognition .
  - They are not suitable for representing shapes with holes or multiple components, as they require a closed boundary curve .
  - They may lose some shape details when reducing the number of descriptors, which may lead to false matches .



### Regional Descriptors

- Regional descriptors are features that describe the properties of a region in an image, such as its shape, size, color, texture, etc.
- Regional descriptors can be classified into two types: external and internal.
  - External descriptors are based on the boundary or contour of a region, such as perimeter, compactness, eccentricity, orientation, etc.
  - Internal descriptors are based on the pixels inside a region, such as area, mean value, standard deviation, moments, etc.
- Regional descriptors can be used for various purposes, such as image segmentation, object recognition, classification, retrieval, etc.
- Some examples of regional descriptors are :
  - Area: the number of pixels in a region, optionally multiplied by the real area of each pixel.
  - Perimeter: the length of the boundary of a region, optionally weighted by the edge strength or orientation.
  - Compactness: the ratio of the area to the perimeter squared, indicating how close a region is to a circle.
  - Eccentricity: the ratio of the major axis to the minor axis of the best-fitting ellipse of a region, indicating how elongated a region is.
  - Orientation: the angle of the major axis of the best-fitting ellipse of a region, indicating the direction of a region.
  - Mean value: the average intensity or color of the pixels in a region, indicating the brightness or hue of a region.
  - Standard deviation: the measure of the variation of the intensity or color of the pixels in a region, indicating the contrast or saturation of a region.
  - Moments: the weighted averages of the pixel coordinates or intensities in a region, indicating the shape, position, and orientation of a region. Moments can be computed in different orders and bases, such as geometric, central, normalized, or Hu moments.



### Topological feature extraction in binary images

- Topological features are properties of objects in images that are invariant under continuous deformations, such as translation, rotation, scaling, or bending.
- Examples of topological features are the number of connected components, the number of holes, the Euler number, or the Betti numbers of an object.
- Topological features can be useful for image analysis, such as object detection, segmentation, classification, or recognition.
- To extract topological features from binary images, one needs to define a suitable representation of the objects and their boundaries, such as pixels, voxels, or simplices.
- One also needs to define a notion of adjacency or connectivity between these elements, such as 4-connectivity, 8-connectivity, or k-connectivity for pixels, or face-to-face, edge-to-edge, or vertex-to-vertex connectivity for simplices.
- Based on these definitions, one can apply methods from combinatorial topology or algebraic topology to compute the topological features of the objects in the image.
- Combinatorial topology uses graph-theoretic concepts, such as cycles, trees, or spanning trees, to compute the number of components, holes, or tunnels of an object.
- Algebraic topology uses algebraic structures, such as groups, rings, or modules, to compute the homology or cohomology groups of an object, which capture its higher-dimensional holes or voids.
- Some of the algorithms for topological feature extraction are based on the following concepts or techniques:
  - Euler characteristic: a scalar quantity that equals the number of vertices minus the number of edges plus the number of faces of an object. It can be computed by counting the number of black and white pixels in the image, or by using a lookup table for each pixel configuration.
  - Betti numbers: a sequence of integers that measure the rank of the homology groups of an object. They can be computed by counting the number of independent cycles, boundaries, or generators of the homology groups, or by using a matrix reduction technique.
  - Persistent homology: a method that tracks the changes in the homology groups of an object as a function of a parameter, such as the level of noise, the scale, or the threshold. It can be computed by constructing a filtration of the object, which is a nested sequence of sub-objects, and applying the standard homology algorithms to each sub-object. The output is a persistence diagram or a barcode, which shows the birth and death of each homology class along the parameter.
  - Morse theory: a method that relates the topology of an object to the critical points of a real-valued function defined on the object, such as the height, the curvature, or the intensity. It can be computed by finding the critical points and the gradient flow of the function, and applying the Morse inequalities or the Morse-Smale complex to obtain the topological features of the object.



### Texture

- Texture is a property of an image that describes the spatial arrangement of color or intensity values in a local neighborhood.
- Texture analysis is the process of extracting meaningful information from an image based on its texture features, such as contrast, coarseness, directionality, regularity, etc .
- Texture analysis can be used for various applications, such as image segmentation, classification, retrieval, synthesis, enhancement, etc  .
- Texture analysis methods can be broadly classified into three categories: statistical, structural, and spectral .
  - Statistical methods use numerical measures to quantify the texture properties of an image, such as gray-level histograms, co-occurrence matrices, run-length matrices, etc .
  - Structural methods use rules or grammar to describe the texture patterns of an image, such as primitives, texels, fractals, etc .
  - Spectral methods use frequency domain transformations to analyze the texture characteristics of an image, such as Fourier transform, wavelet transform, Gabor filter, etc .
- Texture synthesis is the process of generating new images that have the same or similar texture as a given sample image.
  - Texture synthesis methods can be classified into two categories: parametric and non-parametric.
    - Parametric methods use a statistical model to capture the texture features of the sample image and then generate new images by sampling from the model, such as Markov random fields, Gaussian fields, etc.
    - Non-parametric methods use the sample image directly as a source of texture patches and then generate new images by stitching the patches together, such as pixel-based, patch-based, example-based, etc.



### Patterns and Pattern Classes

- A pattern is an arrangement of descriptors that characterizes an object or a concept .
- A descriptor is a feature or an attribute that can be measured or observed, such as color, shape, size, texture, etc .
- A pattern class is a family of patterns that share some common properties, such as belonging to the same category, having the same function, or satisfying some criteria .
- Pattern classes are denoted by ω1, ω2, …, ωW, where W is the number of classes.
- The goal of pattern recognition is to assign patterns to their classes with as little human interaction as possible .
- Three common pattern arrangements used in practice are vectors (for quantitative descriptions), strings (for structural descriptions), and trees (for hierarchical descriptions).
- Pattern vectors are ordered sets of numerical values that represent the descriptors of a pattern, such as pixel intensities, color histograms, edge orientations, etc .
- Pattern vectors are also called feature vectors, and they can be represented as points in a multidimensional space called the feature space .
- Pattern strings are sequences of symbols that represent the descriptors of a pattern, such as letters, words, codes, etc.
- Pattern strings are useful for describing patterns that have a linear structure, such as text, DNA, speech, etc.
- Pattern trees are graphs that represent the descriptors of a pattern as nodes and their relationships as edges.
- Pattern trees are useful for describing patterns that have a hierarchical or recursive structure, such as sentences, molecules, images, etc.
- Pattern recognition by machine involves techniques for extracting, selecting, and transforming the descriptors of a pattern, and then using a classifier to assign the pattern to a class .
- A classifier is a function or a rule that maps a pattern to a class, such as a threshold, a distance measure, a neural network, a decision tree, etc .
- A classifier can be supervised, meaning that it is trained with labeled patterns, or unsupervised, meaning that it is trained with unlabeled patterns .
- Image processing is a set of computational techniques for analyzing, enhancing, compressing, and reconstructing images.
- Image analysis is a subfield of image processing that focuses on extracting information from images, such as objects, regions, features, etc.
- Image recognition is a subfield of image analysis that focuses on identifying and classifying the objects or concepts in an image, such as faces, animals, logos, etc .
- Image recognition can be based on patterns, meaning that it uses descriptors that are derived from the image itself, such as edges, corners, contours, etc .
- Image recognition can also be based on models, meaning that it uses descriptors that are derived from a prior knowledge of the objects or concepts, such as shape, color, texture, etc .
- Image recognition can be performed at different levels of abstraction, such as pixel-level, region-level, object-level, or scene-level .
- Image recognition can be applied to various domains, such as biometrics, security, medical imaging, robotics, computer vision, etc .



### Recognition based on matching

- Recognition based on matching is a technique of image processing that aims to find and identify objects or scenes in an image by comparing them with a template or a model.
- Matching can be performed at different levels of abstraction, such as pixel-level, feature-level, or semantic-level.
- Matching can also be classified into different types, such as exact matching, inexact matching, rigid matching, or non-rigid matching, depending on the degree of similarity and deformation between the image and the template.
- Some of the applications of recognition based on matching are computer vision, moving target tracking and recognition, motion compensation in sequence image compression, and medical image processing.
- Some of the challenges of recognition based on matching are dealing with occlusion, illumination, scale, rotation, perspective, and noise in the image.
- Some of the algorithms of recognition based on matching are template matching, feature matching, correlation matching, and genetic algorithm matching .

