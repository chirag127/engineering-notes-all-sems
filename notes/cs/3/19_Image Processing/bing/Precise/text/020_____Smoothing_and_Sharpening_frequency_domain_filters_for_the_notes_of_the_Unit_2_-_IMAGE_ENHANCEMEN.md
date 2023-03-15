### Smoothing and Sharpening frequency domain filters

Smoothing and sharpening frequency domain filters are used in image enhancement to improve the visual quality of an image. These filters operate in the frequency domain, which means that they manipulate the Fourier transform of the image.

- **Smoothing filters** are used to reduce noise and other high-frequency components in an image. This can help to improve the overall appearance of the image by making it appear smoother and less grainy. Some common smoothing filters include the ideal low-pass filter, the Butterworth low-pass filter, and the Gaussian low-pass filter.

- **Sharpening filters** are used to enhance the edges and other high-frequency components in an image. This can help to improve the overall sharpness and clarity of the image. Some common sharpening filters include the ideal high-pass filter, the Butterworth high-pass filter, and the Gaussian high-pass filter.

Both smoothing and sharpening filters can be applied to an image by first taking the Fourier transform of the image, then multiplying the Fourier transform by the filter function, and finally taking the inverse Fourier transform to obtain the filtered image. The choice of filter function will depend on the specific requirements of the image enhancement task.