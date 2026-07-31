# Degradation Model

In the context of image restoration, a degradation model is a mathematical representation of the degradation process that has occurred to an image. The goal of image restoration is to recover the original image from the degraded image, and the degradation model is used to describe how the original image was transformed into the degraded image.

There are several factors that can contribute to the degradation of an image, including:

1. **Noise:** Random variations in the pixel values of an image can be introduced during the image acquisition process or during transmission and storage. This noise can be modeled using various probability distributions, such as Gaussian or Poisson distributions.

2. **Blur:** The image may be blurred due to motion of the camera or the object being imaged, or due to the limitations of the imaging system. This blur can be modeled using a point spread function (PSF), which describes how a point source of light is spread out by the imaging system.

3. **Geometric distortions:** The image may be distorted due to the perspective of the imaging system or due to the curvature of the imaging surface. These distortions can be modeled using geometric transformations, such as affine or projective transformations.

The degradation model is typically represented as a linear system, where the degraded image is the result of the original image being convolved with the PSF and then corrupted by noise. The goal of image restoration is to solve this linear system to recover the original image.