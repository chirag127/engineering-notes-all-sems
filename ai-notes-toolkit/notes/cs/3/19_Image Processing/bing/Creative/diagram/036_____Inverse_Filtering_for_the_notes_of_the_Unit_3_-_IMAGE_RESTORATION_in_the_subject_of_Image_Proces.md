### Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to recover the original image from a blurred image by inversing the blurring filter .
- The blurring filter is assumed to be known and linear, and the image degradation is modeled as a convolution process: `g(x,y) = h(x,y) * f(x,y)`, where `g(x,y)` is the blurred image, `h(x,y)` is the blurring filter, and `f(x,y)` is the original image .
- In the frequency domain, the convolution becomes a multiplication: `G(u,v) = H(u,v) F(u,v)`, where `G(u,v)`, `H(u,v)`, and `F(u,v)` are the Fourier transforms of `g(x,y)`, `h(x,y)`, and `f(x,y)`, respectively .
- The inverse filtering method tries to estimate `F(u,v)` by dividing `G(u,v)` by `H(u,v)`: `F(u,v) = G(u,v) / H(u,v)` .
- The inverse filtering method works well when the blurring filter `H(u,v)` is non-zero for all frequencies, and when there is no noise in the system .
- However, in practice, the blurring filter may have zeros or very small values for some frequencies, and the system may be corrupted by additive noise .
- In these cases, the inverse filtering method may amplify the noise and produce ringing artifacts in the restored image .
- To overcome these problems, other methods such as truncated inverse filtering, Wiener filtering, and constrained least squares filtering can be used  .