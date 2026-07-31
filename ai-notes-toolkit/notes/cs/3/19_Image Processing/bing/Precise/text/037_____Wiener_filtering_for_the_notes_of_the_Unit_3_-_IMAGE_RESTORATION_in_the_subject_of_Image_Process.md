### Wiener filtering

Wiener filtering is an image processing tool that is used to remove noise from images. It is based on the principle of least squares and is very effective in removing Gaussian noise. The filter works by convolving the image with a kernel that is the inverse of the noise power spectrum.

The Wiener filter performs two main functions - it inverts the blur of the image and removes extra noise. It is particularly helpful when processing images that have been through a degradation filter or when the image has been blurred by a known lowpass filter.

The most important technique for removal of blur in images due to linear motion or unfocussed optics is the Wiener filter. From a signal processing standpoint, blurring due to linear motion in a photograph is the result of poor sampling.

The Wiener filter has a variety of applications in signal processing, image processing, control systems, and digital communications. These applications generally fall into one of four main categories: System identification; Deconvolution; Noise reduction; Signal detection.

For example, to deblur an image using a Wiener filter in MATLAB, one can create a point-spread function, PSF, by using the fspecial function and specifying linear motion across 21 pixels at an angle of 11 degrees. Then, convolve the point-spread function with the image by using imfilter.