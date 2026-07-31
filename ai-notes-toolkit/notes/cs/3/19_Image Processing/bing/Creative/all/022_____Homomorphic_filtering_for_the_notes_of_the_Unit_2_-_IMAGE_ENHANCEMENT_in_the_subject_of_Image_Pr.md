# Homomorphic filtering

- Homomorphic filtering is a generalized technique for signal and image processing, involving a nonlinear mapping to a different domain in which linear filter techniques are applied, followed by mapping back to the original domain .
- Homomorphic filtering can be used to enhance an image by reducing its dynamic range and increasing its contrast, as well as removing noise and other artifacts.
- Homomorphic filtering is based on the image formation model that represents an input image as the product of the illumination and the reflectance .
- The illumination component is related to the amount and direction of light sources, and the reflectance component is related to the properties and colors of the objects in the scene.
- The illumination component is usually low-frequency and the reflectance component is usually high-frequency .
- Homomorphic filtering aims to separate the illumination and reflectance components, and apply different filtering operations to each of them .
- Homomorphic filtering can be implemented as follows :
  - Apply a logarithmic transformation to the input image to convert the multiplicative model into an additive model.
  - Apply a high-pass filter or a band-pass filter to the transformed image to attenuate the illumination component and enhance the reflectance component.
  - Apply an exponential transformation to the filtered image to convert the additive model back to the multiplicative model.
  - Adjust the output image to the desired dynamic range and contrast.
- Homomorphic filtering can be used for various applications, such as  :
  - Change detection, by comparing the reflectance components of two images taken at different times or conditions.
  - Face recognition, by removing the effects of illumination variations and enhancing the facial features.
  - Image restoration, by removing noise, blurring, and other distortions from the image.
  - Image enhancement, by improving the brightness, contrast, and sharpness of the image.