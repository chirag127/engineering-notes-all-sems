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