### Noise Models

Noise is always present in digital images during image acquisition, coding, transmission, and processing steps. It is very difficult to remove it from the digital images without the prior knowledge of noise model. That is why, review of noise models is essential in the study of image denoising techniques.

Image restoration is the operation of taking a corrupt/noisy image and estimating the clean, original image. Corruption may come in many forms such as motion blur, noise, and camera misfocus. Image restoration is hence more sophisticated techniques, such as regularized deblurring, have been developed to offer robust recovery under different types of noises and blurring functions.

Generally, a mathematical model of image degradation and its restoration is used for processing. The presence of a degradation function h(x,y) and an external noise n(x,y) component coming into the original image signal f(x,y) thereby producing a final degraded image g(x,y). This part composes the degradation model.

In a simplest image degradation model, the degradation function is modeled as a low pass filter, which resulted in a blurry effect. Fundamentally, the image restoration process involves in reversing the distortion effects.