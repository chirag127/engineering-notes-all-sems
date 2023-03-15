### Homomorphic filtering

- Homomorphic filtering is a generalized technique for signal and image processing, involving a nonlinear mapping to a different domain in which linear filter techniques are applied, followed by mapping back to the original domain .
- Homomorphic filtering can be used to split low-frequency illumination and high-frequency reflectance from an image, and enhance the image by reducing its dynamic range and increasing its contrast .
- Homomorphic filtering is based on the image formation model that represents an input image as the product of the illumination and the reflectance:
  - `g(x,y) = i(x,y) * r(x,y)`
  - where `g(x,y)` is the input image, `i(x,y)` is the illumination, and `r(x,y)` is the reflectance.
- Homomorphic filtering consists of four steps:
  - 1. Taking the logarithm of the input image to convert the multiplicative model into an additive model:
    - `ln g(x,y) = ln i(x,y) + ln r(x,y)`
  - 2. Applying a high-pass filter to the logarithmic image to attenuate the low-frequency illumination and enhance the high-frequency reflectance:
    - `H(u,v) * ln g(x,y) = H(u,v) * ln i(x,y) + H(u,v) * ln r(x,y)`
    - where `H(u,v)` is the frequency response of the high-pass filter.
  - 3. Taking the exponential of the filtered image to restore the original multiplicative model:
    - `exp(H(u,v) * ln g(x,y)) = i(x,y) * exp(H(u,v) * ln r(x,y))`
  - 4. Scaling the output image to the desired range:
    - `s * exp(H(u,v) * ln g(x,y)) = s * i(x,y) * exp(H(u,v) * ln r(x,y))`
    - where `s` is a scaling factor.
- Homomorphic filtering can be implemented using different types of high-pass filters, such as Gaussian, Butterworth, or Laplacian. The choice of the filter parameters depends on the characteristics of the input image and the desired enhancement effect.