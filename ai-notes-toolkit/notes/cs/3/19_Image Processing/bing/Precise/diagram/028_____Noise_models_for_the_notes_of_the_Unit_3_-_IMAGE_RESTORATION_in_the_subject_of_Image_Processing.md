### Noise Models in Image Restoration

Image restoration is the process of obtaining a close replica of the original image by removing the external noise that is probabilistic in nature. There are several noise models used frequently in the field of digital image processing, which are modeled as known probability density functions .

The principal source of noise in digital images arises during image acquisition and transmission. The performance of imaging sensors is affected by a variety of environmental and mechanical factors of the instrument, resulting in the addition of undesirable noise in the image.

Some common noise models are:
- **Gaussian**: poor illumination
- **Rayleigh**: range image
- **Gamma/Exp**: laser imaging
- **Impulse**: faulty switch during imaging
- **Uniform**: least used

To restore an image, we must model the degradation process so that the reverse process can be applied. The model consists of a degradation function and an additive noise component. The objective of restoration is to obtain an estimate of the original image.