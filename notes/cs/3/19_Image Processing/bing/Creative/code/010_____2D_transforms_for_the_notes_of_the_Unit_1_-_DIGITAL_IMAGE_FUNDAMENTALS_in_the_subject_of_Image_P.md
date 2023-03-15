# 2D transforms for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing

- 2D transforms are mathematical operations that map an image from one coordinate system to another, usually to modify its appearance or extract some features.
- 2D transforms can be classified into two types: spatial domain transforms and frequency domain transforms.
- Spatial domain transforms operate directly on the pixel values of the image, such as rotation, scaling, translation, shearing, etc. They can be represented by matrices or linear equations.
- Frequency domain transforms operate on the spectral components of the image, such as Fourier transform, wavelet transform, cosine transform, etc. They decompose the image into a sum of sinusoids or wavelets of different frequencies, amplitudes and phases. They can be used for filtering, compression, enhancement, etc.
- Some examples of 2D transforms are:

  - Fourier transform: a frequency domain transform that converts an image from spatial domain to frequency domain, where each pixel represents the magnitude and phase of a sinusoid. The Fourier transform can be computed efficiently using the Fast Fourier Transform (FFT) algorithm. The inverse Fourier transform converts the image back to spatial domain. The Fourier transform can be used for frequency analysis, filtering, reconstruction, etc.  

  - Wavelet transform: a frequency domain transform that converts an image from spatial domain to wavelet domain, where each pixel represents the coefficient of a wavelet. A wavelet is a localized function that has both frequency and spatial information. The wavelet transform can be computed using filter banks or recursive algorithms. The inverse wavelet transform converts the image back to spatial domain. The wavelet transform can be used for compression, denoising, edge detection, etc.  

  - Rotation: a spatial domain transform that rotates an image by a given angle around a given point. The rotation can be represented by a 2x2 matrix or a linear equation. The rotation can be used for alignment, orientation, etc.

  - Scaling: a spatial domain transform that enlarges or reduces an image by a given factor along each axis. The scaling can be represented by a 2x2 matrix or a linear equation. The scaling can be used for resizing, zooming, etc.

  - Translation: a spatial domain transform that shifts an image by a given distance along each axis. The translation can be represented by a 2x1 vector or a linear equation. The translation can be used for positioning, cropping, etc.

  - Shearing: a spatial domain transform that distorts an image by a given angle along each axis. The shearing can be represented by a 2x2 matrix or a linear equation. The shearing can be used for perspective, deformation, etc.  

- 2D transforms can be combined to form more complex transformations, such as affine transforms, projective transforms, etc. They can also be applied to different color spaces or channels of the image, such as RGB, HSV, YCbCr, etc.