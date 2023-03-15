# Band pass Filters for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Band-pass filters are filters that allow only a certain range of frequencies to pass through, while attenuating the frequencies outside the range .
- Band-pass filters can be used to enhance image features such as edges and blobs, or to reduce noise and illumination artifacts .
- Band-pass filters can be implemented in the spatial domain or the frequency domain .
- In the spatial domain, band-pass filters can be obtained by multiplying a low-pass filter with a high-pass filter, where the low-pass filter has a higher cut-off frequency than the high-pass filter.
- In the frequency domain, band-pass filters can be obtained by applying a circular or elliptical mask to the Fourier transform of the image, where the mask has a certain radius or axes that define the pass-band.
- Band-pass filters can be designed with different shapes and characteristics, such as Gaussian, Butterworth, Chebyshev, etc .
- Band-pass filters can be adaptive, meaning that they can adjust themselves to suit the local signal conditions in the image, without prior knowledge of the signal statistics.
- Band-pass filters have various applications and advantages in image processing, such as:
  - Enhancing the contrast and sharpness of images .
  - Detecting edges and contours of objects .
  - Segmenting images based on texture or frequency features .
  - Removing noise and blur from images .
  - Improving the quality and resolution of images .