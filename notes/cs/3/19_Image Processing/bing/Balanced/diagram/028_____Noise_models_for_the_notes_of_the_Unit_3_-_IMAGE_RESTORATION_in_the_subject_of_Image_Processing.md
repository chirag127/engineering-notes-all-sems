### Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Noise is unwanted information in digital images that degrades the quality and clarity of the image  .
- Noise can be introduced during image acquisition, coding, transmission, and processing steps .
- Noise can produce undesirable effects such as artifacts, unrealistic edges, unseen lines, corners, blurred objects and disturbs background scenes .
- To reduce these undesirable effects, prior knowledge of noise models is essential for further processing .
- Noise models describe the statistical properties of noise and how it affects the image pixels.
- Some common noise models are:
  - Gaussian noise: This noise has a normal or bell-shaped probability density function (PDF) and is characterized by its mean and variance. Gaussian noise is independent of the pixel intensity and can be caused by sensor noise, quantization noise, or thermal noise .
  - Salt-and-pepper noise: This noise has only two possible values, either very high (salt) or very low (pepper), and affects only a small fraction of pixels. Salt-and-pepper noise can be caused by transmission errors, faulty memory locations, or malfunctioning pixels .
  - Speckle noise: This noise has a multiplicative effect on the image and is proportional to the pixel intensity. Speckle noise can be caused by coherent interference, such as in ultrasound or radar imaging .
  - Poisson noise: This noise has a Poisson PDF and is dependent on the pixel intensity. Poisson noise can be caused by photon counting noise, such as in low-light imaging or X-ray imaging .
- Different noise models require different image restoration techniques to remove or reduce the noise . Some common image restoration techniques are:
  - Spatial filtering: This technique applies a filter mask or kernel to each pixel and its neighbors to compute a new pixel value based on some criteria, such as mean, median, or mode. Spatial filtering can be used to smooth or sharpen the image, or to detect edges or corners.
  - Frequency filtering: This technique applies a transform, such as Fourier transform, to the image and modifies the frequency components of the image based on some criteria, such as low-pass, high-pass, or band-pass. Frequency filtering can be used to remove periodic noise or enhance certain features of the image.
  - Inverse filtering: This technique applies the inverse of the degradation function to the image to restore the original image. Inverse filtering can be used to remove blurring or distortion caused by motion, defocus, or atmospheric turbulence.
  - Wiener filtering: This technique applies a filter that minimizes the mean square error between the original and restored image, taking into account the noise and the degradation function. Wiener filtering can be used to remove noise and blurring simultaneously.
  - Regularized filtering: This technique applies a filter that balances the fidelity and smoothness of the restored image, using a regularization parameter that controls the trade-off. Regularized filtering can be used to avoid amplifying noise or introducing artifacts in the restored image.