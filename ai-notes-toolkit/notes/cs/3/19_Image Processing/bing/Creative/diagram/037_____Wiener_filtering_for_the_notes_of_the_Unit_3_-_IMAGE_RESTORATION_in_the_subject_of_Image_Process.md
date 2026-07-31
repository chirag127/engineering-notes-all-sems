### Wiener filtering

Wiener filtering is a technique for image restoration that aims to reduce the mean square error between the restored image and the original image. It is based on the assumption that the image degradation can be modeled as a linear and space-invariant process, and that the noise and the original image are statistically independent and have known power spectra.

Some advantages of Wiener filtering are:

- It can handle both blur and noise in the degraded image.
- It can adapt to the local characteristics of the image, such as edges and textures.
- It can avoid the amplification of noise that occurs in inverse filtering.

Some disadvantages of Wiener filtering are:

- It requires the knowledge of the degradation function and the power spectra of the noise and the original image, which are often difficult to estimate in practice.
- It may introduce artifacts such as ringing or blurring in the restored image.

The Wiener filter can be expressed as:

$$
\hat{H}(u,v) = \frac{H^*(u,v)}{|H(u,v)|^2 + \frac{S_\eta(u,v)}{S_f(u,v)}}
$$

where:

- $\hat{H}(u,v)$ is the Wiener filter in the frequency domain.
- $H(u,v)$ is the degradation function in the frequency domain.
- $H^*(u,v)$ is the complex conjugate of $H(u,v)$.
- $S_\eta(u,v)$ is the power spectrum of the noise in the frequency domain.
- $S_f(u,v)$ is the power spectrum of the original image in the frequency domain.
- $\frac{S_\eta(u,v)}{S_f(u,v)}$ is the noise-to-signal ratio (NSR) in the frequency domain.

The restored image can be obtained by applying the Wiener filter to the degraded image in the frequency domain:

$$
\hat{F}(u,v) = \hat{H}(u,v)G(u,v)
$$

where:

- $\hat{F}(u,v)$ is the restored image in the frequency domain.
- $G(u,v)$ is the degraded image in the frequency domain.

The restored image can be converted back to the spatial domain by applying the inverse Fourier transform:

$$
\hat{f}(x,y) = \mathcal{F}^{-1}[\hat{F}(u,v)]
$$

where:

- $\hat{f}(x,y)$ is the restored image in the spatial domain.
- $\mathcal{F}^{-1}$ is the inverse Fourier transform operator.

The following diagram illustrates the steps of Wiener filtering:

```mermaid
graph LR
f[Original image] -->|Degradation| g[Degraded image]
g -->|Fourier transform| G[Degraded image in frequency domain]
G -->|Wiener filter| F[Restored image in frequency domain]
F -->|Inverse Fourier transform| fhat[Restored image]
```