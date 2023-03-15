# Introduction to Fourier Transform

The Fourier transform is a mathematical technique that allows us to decompose an image into its frequency components. The frequency components are the sine and cosine waves of different frequencies, amplitudes, and phases that make up the image. The Fourier transform can be used for various image processing tasks, such as:

- Image enhancement: We can modify the frequency components of an image to enhance certain features or remove unwanted noise.
- Image analysis: We can measure the frequency content of an image to characterize its texture, shape, or periodicity.
- Image restoration: We can reconstruct an image from its frequency components, even if some of them are missing or corrupted.
- Image compression: We can reduce the size of an image by discarding some of the frequency components that are less important or redundant.

The Fourier transform can be applied to both one-dimensional (1D) signals, such as audio or time series, and two-dimensional (2D) signals, such as images. In this section, we will focus on the 2D Fourier transform and how it works for images.

## 2D Fourier Transform

The 2D Fourier transform of an image f(x,y) is defined as:

F(u,v) = ∫∫ f(x,y) e^(-j2π(ux+vy)) dx dy

where F(u,v) is the complex-valued frequency spectrum of the image, u and v are the spatial frequencies along the x and y axes, respectively, and j is the imaginary unit. The exponential term e^(-j2π(ux+vy)) is a complex exponential that represents a 2D sinusoid of frequency (u,v) and phase -2π(ux+vy).

The inverse 2D Fourier transform of F(u,v) is defined as:

f(x,y) = (1/MN) ∫∫ F(u,v) e^(j2π(ux+vy)) du dv

where M and N are the dimensions of the image, and f(x,y) is the reconstructed image from the frequency spectrum.

The 2D Fourier transform and its inverse can be computed efficiently using the Fast Fourier Transform (FFT) algorithm, which reduces the computational complexity from O(MN)^2 to O(MN log(MN)).

## Properties of the 2D Fourier Transform

The 2D Fourier transform has some important properties that are useful for image processing, such as:

- Linearity: The Fourier transform of a linear combination of images is equal to the linear combination of their Fourier transforms, i.e., F(a f1(x,y) + b f2(x,y)) = a F(f1(x,y)) + b F(f2(x,y)), where a and b are constants.
- Shift-invariance: The Fourier transform of a shifted image is equal to the Fourier transform of the original image multiplied by a phase factor, i.e., F(f(x-x0,y-y0)) = F(f(x,y)) e^(-j2π(ux0+vy0)), where (x0,y0) is the shift vector.
- Convolution theorem: The Fourier transform of the convolution of two images is equal to the product of their Fourier transforms, i.e., F(f(x,y) * g(x,y)) = F(f(x,y)) F(g(x,y)), where * denotes the convolution operation. Conversely, the Fourier transform of the product of two images is equal to the convolution of their Fourier transforms, i.e., F(f(x,y) g(x,y)) = F(f(x,y)) * F(g(x,y)).
- Parseval's theorem: The total energy of an image is equal to the total energy of its frequency spectrum, i.e., ∫∫ |f(x,y)|^2 dx dy = ∫∫ |F(u,v)|^2 du dv, where |.| denotes the magnitude.

## Frequency Domain Representation of Images

The frequency domain representation of an image is a complex-valued function that contains both the magnitude and the phase information of the frequency components. The magnitude of F(u,v) indicates the strength or amplitude of the frequency component (u,v), while the phase of F(u,v) indicates the position or orientation of the frequency component (u,v).

The magnitude of F(u,v) can be visualized as an image, where the brightness of each pixel corresponds to the amplitude of the frequency component. The phase of F(u,v) can also be visualized as an image, where the hue of each pixel corresponds to the angle of the frequency component.

The frequency domain representation of an image has some important characteristics, such as:

- Sym