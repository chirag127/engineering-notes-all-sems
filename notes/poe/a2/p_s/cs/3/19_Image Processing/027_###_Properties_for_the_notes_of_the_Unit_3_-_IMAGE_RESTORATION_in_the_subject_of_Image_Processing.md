 Here are the properties to cover in the notes for Unit 3 - Image Restoration in Image Processing:

### Point Spread Function (PSF)
- The PSF describes the blurring effect of the imaging system on a point source or point object.
- It is a measure of the response of the imaging system to a point input.
- The shape, size and nature of PSF determine the types of blurs and distortions introduced by the imaging system.
- Knowledge of the PSF is required to inverse the blurring effect and restore the original image.

### Noise
- Images obtained from imaging systems are often corrupted by noise from various sources.
- Noise can be additive, multiplicative or a combination of both.
- Some common noise types are Gaussian noise, Salt-and-pepper noise, Speckle noise, etc.
- Noise needs to be accounted for during image restoration to avoid amplifying the noise in the process of deblurring and recovering the original image.

### Image Degradation Model
- The image degradation can be modelled as a convolution of the original image with the PSF.
- This represents the effect of the imaging system on the image.
- Along with this, additive noise is also incorporated into the model.
- The image degradation model forms the basis for performing image restoration and recovering the original image from the blurred and noisy image.

### Image Restoration Methods
- Some common methods for image restoration are:
-- Wiener Filter
-- Constrained Least Squares Filter
-- Lucy-Richardson Iterative Method
-- Blind Deconvolution
-- Regularization Methods
- These methods use knowledge of the PSF and noise characteristics to undo the degradation and recover the original image.
- Each method has its own advantages and limitations which can be discussed in the notes.

[Detailed explanations, diagrams, examples, codes, applications, etc. can be included for each point to make the notes comprehensive.]