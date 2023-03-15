### Band pass Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Band-pass filters are filters that allow only a certain range of frequencies to pass through, while attenuating the frequencies outside the range.
- Band-pass filters can be used to enhance image features such as edges and blobs, or to reduce noise and low-frequency artifacts such as uneven illumination.
- Band-pass filters can be implemented in both spatial domain and frequency domain, depending on the application and the desired effect.
- In spatial domain, band-pass filters can be obtained by multiplying a low-pass filter with a high-pass filter, where the low-pass filter has a higher cut-off frequency than the high-pass filter.
- In frequency domain, band-pass filters can be obtained by applying a circular or elliptical mask to the Fourier transform of the image, where the mask has a radius or a major and minor axis that define the pass-band.
- Band-pass filters can be designed using different types of functions, such as Gaussian, Butterworth, Chebyshev, etc. The choice of the function affects the shape and smoothness of the filter response.
- Band-pass filters can also be adaptive, meaning that they can adjust themselves to suit the local signal conditions in the image, without prior knowledge of the signal statistics. This can improve the performance of the filter in noisy or blurred images.
- Band-pass filters have various applications in image processing, such as edge detection, blob detection, texture analysis, image segmentation, image enhancement, etc .