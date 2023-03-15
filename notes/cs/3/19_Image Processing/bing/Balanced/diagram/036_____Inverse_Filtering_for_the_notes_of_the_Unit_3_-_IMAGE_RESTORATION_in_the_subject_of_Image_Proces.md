### Inverse Filtering

- Inverse filtering is a technique for image restoration that aims to undo the effects of a known blurring filter on an image .
- Inverse filtering assumes that the degradation process can be modeled as a linear and space-invariant system, such that the degraded image g(x,y) is related to the original image f(x,y) by the convolution equation:

g(x,y) = h(x,y) * f(x,y) + n(x,y)

where h(x,y) is the point spread function (PSF) of the blurring filter, * denotes convolution, and n(x,y) is the additive noise.

- In the frequency domain, the convolution equation becomes:

G(u,v) = H(u,v) F(u,v) + N(u,v)

where G(u,v), H(u,v), F(u,v), and N(u,v) are the Fourier transforms of g(x,y), h(x,y), f(x,y), and n(x,y), respectively.

- The ideal inverse filter is obtained by dividing both sides of the frequency domain equation by H(u,v), which gives:

F(u,v) = G(u,v) / H(u,v) - N(u,v) / H(u,v)

- The restored image is then obtained by taking the inverse Fourier transform of F(u,v).

- The inverse filter works well when the PSF is known and the noise is negligible, as it can recover the original image exactly.
- However, inverse filtering is very sensitive to noise, as it tends to amplify the high-frequency components of the noise when dividing by H(u,v) . This can result in ringing artifacts and loss of details in the restored image.
- To overcome the noise problem, inverse filtering can be modified by truncating the inverse filter at a certain threshold, or by using a regularized inverse filter that incorporates a priori information about the image or the noise .
- Another alternative to inverse filtering is Wiener filtering, which is a more robust technique that minimizes the mean square error between the original and restored images .