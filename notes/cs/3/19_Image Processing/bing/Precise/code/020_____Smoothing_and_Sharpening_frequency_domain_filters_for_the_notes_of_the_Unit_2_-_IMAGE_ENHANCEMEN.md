### Smoothing and Sharpening frequency domain filters

Smoothing and sharpening frequency domain filters are used in image enhancement to improve the visual quality of an image. These filters operate in the frequency domain, which means that they manipulate the Fourier transform of the image.

- **Smoothing filters** are used to reduce noise and other high-frequency components in an image. This can result in a smoother, less detailed image. Common smoothing filters include the ideal low-pass filter, the Butterworth low-pass filter, and the Gaussian low-pass filter.

- **Sharpening filters** are used to enhance edges and other high-frequency components in an image. This can result in a sharper, more detailed image. Common sharpening filters include the ideal high-pass filter, the Butterworth high-pass filter, and the Gaussian high-pass filter.

Both smoothing and sharpening filters can be applied to an image by multiplying its Fourier transform by the filter's transfer function. The resulting image is obtained by taking the inverse Fourier transform of the product.

It is important to note that the choice of filter and its parameters can greatly affect the resulting image. Careful consideration should be given to the specific needs of the image enhancement task at hand.