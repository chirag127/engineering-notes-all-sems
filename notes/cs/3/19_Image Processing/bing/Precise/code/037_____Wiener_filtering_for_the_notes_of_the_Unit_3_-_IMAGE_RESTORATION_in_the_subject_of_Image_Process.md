### Wiener filtering for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Wiener filtering is a technique used in image restoration to remove noise and blur from an image.
- It is a Mean Squared Error (MSE) filtering that incorporates both the degradation function and the statistical characteristics of noise.
- The underlying assumption is that the noise and image are uncorrelated.
- To illustrate the Wiener filtering in image restoration, a standard test image is blurred with a lowpass filter and then additive white Gaussian noise of a certain variance is added to the blurred image.
- The Wiener filtering is then applied to the image with a cascade implementation of the noise smoothing and inverse filtering.
- Image restoration is performed by reversing the process that blurred the image and is performed by imaging a point source and using the point source image, which is called the Point Spread Function (PSF), to restore the image information lost to the blurring process.