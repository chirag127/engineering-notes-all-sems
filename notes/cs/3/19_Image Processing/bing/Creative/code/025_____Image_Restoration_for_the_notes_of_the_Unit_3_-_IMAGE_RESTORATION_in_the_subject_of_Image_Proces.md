### Image Restoration

Image restoration is the operation of taking a corrupt or noisy image and estimating the clean, original image. Corruption may occur due to the image-capture process (e.g., noise, lens blur), post-processing (e.g., JPEG compression), or photography in non-ideal conditions (e.g., haze, motion blur). Image restoration is performed by reversing the process that blurred the image and such is performed by imaging a point source and use the point source image, which is called the Point Spread Function (PSF) to restore the image information lost to the blurring process.

Some of the topics covered in image restoration are:

- Noise models: These are mathematical models that describe the characteristics of the noise present in the image, such as Gaussian noise, salt-and-pepper noise, speckle noise, etc.
- Noise reduction: These are techniques that aim to reduce or remove the noise from the image, such as spatial filtering, frequency domain filtering, adaptive filtering, etc.
- Deblurring: These are techniques that aim to restore the sharpness of the image that has been blurred due to motion, defocus, atmospheric turbulence, etc. Some of the methods are inverse filtering, Wiener filtering, blind deconvolution, etc.
- Super-resolution: These are techniques that aim to increase the resolution of the image by combining multiple low-resolution images of the same scene, such as interpolation, reconstruction, learning-based methods, etc.
- Inpainting: These are techniques that aim to fill in the missing or damaged regions of the image by using the information from the surrounding pixels, such as diffusion, exemplar-based, patch-based, etc.