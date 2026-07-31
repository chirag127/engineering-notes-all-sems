### Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- Inverse filtering assumes that the degradation process can be modeled as a linear and space-invariant system, such that the degraded image `g(x,y)` can be expressed as the convolution of the original image `f(x,y)` and the point spread function `h(x,y)`, plus some additive noise `n(x,y)` :

```
g(x,y) = f(x,y) * h(x,y) + n(x,y)
```

- In the frequency domain, the convolution becomes a multiplication, and the inverse filtering can be performed by dividing the Fourier transform of the degraded image `G(u,v)` by the Fourier transform of the point spread function `H(u,v)` :

```
F(u,v) = G(u,v) / H(u,v)
```

- The inverse filtering can recover the original image `f(x,y)` by taking the inverse Fourier transform of `F(u,v)` :

```
f(x,y) = F^-1(F(u,v))
```

- However, inverse filtering has some limitations and drawbacks :
  - It requires the exact knowledge of the point spread function `h(x,y)`, which may not be available or accurate in practice.
  - It is very sensitive to additive noise `n(x,y)`, especially when the point spread function `H(u,v)` has zeros or small values in the frequency domain. This can cause the noise to be amplified and distort the restored image.
  - It can introduce ringing artifacts around sharp edges or discontinuities in the image, due to the truncation of the inverse filter in the spatial domain.

- To overcome these problems, some modifications or alternatives to inverse filtering have been proposed, such as truncated inverse filtering, Wiener filtering, constrained least squares filtering, set-theoretic filtering, iterative filtering, and spatially adaptive filtering   .