# 2D transforms for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- A 2D transform is a mathematical operation that changes the position, size, orientation, or shape of a 2D object, such as an image.
- 2D transforms are useful for image processing tasks such as repositioning, resizing, rotating, cropping, warping, filtering, or compressing images .
- Some common types of 2D transforms are:
  - Translation: moving an image by a certain amount of pixels in the horizontal and vertical directions.
  - Scaling: changing the size of an image by a certain factor in the horizontal and vertical directions.
  - Rotation: rotating an image by a certain angle around a fixed point.
  - Shearing: skewing an image by a certain amount in the horizontal or vertical direction.
  - Affine: a combination of translation, scaling, rotation, and shearing.
  - Perspective: a transformation that simulates the effect of viewing an image from a different point of view.
- To perform 2D transforms, we need to use a coordinate system to represent the position of each pixel in an image. A common coordinate system is the Cartesian system, where the origin is at the top-left corner of the image, the x-axis is horizontal, and the y-axis is vertical.
- To simplify the computation of 2D transforms, we can use homogeneous coordinates, which are a way of representing a 2D point with three numbers instead of two. A 2D point (x, y) can be represented as a homogeneous vector [x, y, 1] or any multiple of it, such as [2x, 2y, 2] or [0.5x, 0.5y, 0.5].
- Using homogeneous coordinates, we can express 2D transforms as matrix multiplications. For example, the translation of an image by (tx, ty) pixels can be expressed as:

  ```
  [x', y', 1] = [x, y, 1] * [1 0 tx; 0 1 ty; 0 0 1]
  ```

  where x' and y' are the new coordinates of the pixel after translation.
- Some 2D transforms have special properties, such as preserving the shape, size, or angles of the image. These are called geometric transforms. For example, translation, rotation, and scaling are geometric transforms, while shearing and perspective are not.
- Some 2D transforms can be applied in the frequency domain instead of the spatial domain. The frequency domain is a representation of an image that shows the amount and direction of periodic patterns in the image. The most common way of converting an image from the spatial domain to the frequency domain is the Fourier transform.
- The Fourier transform decomposes an image into a sum of sinusoids of different frequencies, amplitudes, and phases. The inverse Fourier transform reconstructs the image from the sinusoids. The Fourier transform and its inverse can be computed efficiently using the Fast Fourier Transform (FFT) algorithm.
- The Fourier transform has many applications in image processing, such as filtering, compression, enhancement, restoration, or analysis. For example, we can use the Fourier transform to remove noise, blur, or unwanted frequencies from an image, or to enhance the contrast, sharpness, or edges of an image .
- The 2D Fourier transform can be extended to other types of transforms, such as the discrete cosine transform (DCT), the discrete wavelet transform (DWT), or the discrete Karhunen-Loeve transform (DKLT). These transforms have different properties and advantages for different image processing tasks .
- The DCT is a transform that decomposes an image into a sum of cosine functions of different frequencies and amplitudes. The DCT is widely used for image compression, especially in the JPEG standard, because it can compact most of the energy of an image into a few coefficients.
- The DWT is a transform that decomposes an image into a sum of wavelets of different scales and positions. A wavelet is a function that has a finite duration and zero mean. The DWT is useful for image compression, enhancement, denoising, or segmentation, because it can capture both the global and local features of