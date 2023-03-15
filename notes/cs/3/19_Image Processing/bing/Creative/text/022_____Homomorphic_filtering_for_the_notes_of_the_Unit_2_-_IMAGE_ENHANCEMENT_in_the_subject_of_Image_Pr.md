### Homomorphic filtering

- Homomorphic filtering is a generalized technique for signal and image processing, involving a nonlinear mapping to a different domain in which linear filter techniques are applied, followed by mapping back to the original domain .
- Homomorphic filtering is based on the image formation model that represents an input image as the product of the illumination and the reflectance. The illumination component is related to the amount and direction of light sources, while the reflectance component is related to the properties of the objects in the scene.
- Homomorphic filtering aims to enhance an input image by reducing its dynamic range and increasing its contrast. It also helps to remove the effects of shadows, shading, and noise.
- Homomorphic filtering consists of four steps :
  - Taking the logarithm of the input image to convert the multiplicative model into an additive model.
  - Applying a high-pass filter or a band-pass filter to the logarithmic image to attenuate the low-frequency illumination component and enhance the high-frequency reflectance component.
  - Taking the exponential of the filtered image to restore the original multiplicative model.
  - Normalizing the output image to the desired range.
- Homomorphic filtering can be used for various applications, such as change detection, face recognition, medical imaging, and remote sensing .