 Here is the content in markdown format for the topic -

### Noise models for the notes of the Unit 3 - IMAGE RESTORATION

The following are the common noise models that corrupt an image and need to be restored:

1. Gaussian noise: It is additive noise with zero mean and Gaussian distribution. It makes the image look grainy. It can be reduced using filters like Gaussian filter.
Advantage - Occurs naturally, easy to simulate.
Disadvantage - Difficult to remove completely.

2. Salt and pepper noise: It is impulse noise that corrupts pixels to black or white randomly. It makes the image look speckled. It can be reduced using median filter.
Advantage - Easy to simulate.
Disadvantage - Difficult to remove if noise density is high.

3. Speckle noise: It follows a multiplicative model and degrades coherent imaging systems like ultrasound or SAR. It makes the image look speckled. It can be reduced using filters like Lee filter.
Advantage - Models noise in coherent systems well.
Disadvantage - Difficult to remove completely.

[Include diagrams, examples, codes, applications, etc here if needed]

The noise has to be estimated from the corrupted image and appropriate restoration technique has to be applied based on the noise model to get a denoised output image. Proper noise estimation and modelling leads to effective image restoration.