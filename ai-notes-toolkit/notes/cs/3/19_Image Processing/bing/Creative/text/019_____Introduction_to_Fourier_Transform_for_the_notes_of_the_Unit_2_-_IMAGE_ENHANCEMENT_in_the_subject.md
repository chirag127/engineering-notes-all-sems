### Introduction to Fourier Transform

The Fourier transform is a mathematical tool that allows us to decompose an image into its frequency components. The frequency components are the sine and cosine waves of different frequencies, amplitudes, and phases that make up the image. The Fourier transform can be used for various image processing tasks, such as:

- Image enhancement: We can modify the frequency components of an image to enhance certain features or remove noise. For example, we can apply low-pass filters to smooth an image or high-pass filters to sharpen it.
- Image analysis: We can extract information from the frequency domain of an image, such as the dominant frequencies, the orientation and direction of edges, or the periodic patterns. For example, we can use the Fourier transform to detect the rotation and scaling of an image.
- Image restoration: We can use the Fourier transform to recover an image that has been corrupted by noise, blur, or distortion. For example, we can use the inverse Fourier transform to reconstruct an image from its frequency components.
- Image compression: We can use the Fourier transform to reduce the amount of data needed to store or transmit an image. For example, we can use the discrete cosine transform (DCT) to compress an image into a smaller number of coefficients.

The Fourier transform can be applied to both continuous and discrete images. For continuous images, the Fourier transform is defined as:

$$F(u,v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(ux+vy)} dx dy$$

where $f(x,y)$ is the image function, $F(u,v)$ is the Fourier transform, and $u$ and $v$ are the spatial frequencies. The inverse Fourier transform is defined as:

$$f(x,y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} F(u,v) e^{j2\pi(ux+vy)} du dv$$

For discrete images, the Fourier transform is defined as:

$$F(u,v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x,y) e^{-j2\pi(ux/M+vy/N)}$$

where $f(x,y)$ is the image function, $F(u,v)$ is the Fourier transform, and $u$ and $v$ are the spatial frequencies. The inverse Fourier transform is defined as:

$$f(x,y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} F(u,v) e^{j2\pi(ux/M+vy/N)}$$

The Fourier transform of an image is a complex-valued function, which can be represented by its magnitude and phase. The magnitude of the Fourier transform shows the amount of energy at each frequency, while the phase of the Fourier transform shows the relative position of the frequency components. The magnitude of the Fourier transform is often displayed as a spectrum, where the low frequencies are at the center and the high frequencies are at the edges. The phase of the Fourier transform is often displayed as a wrapped phase, where the values are in the range of $[-\pi, \pi]$.

The Fourier transform has some important properties that are useful for image processing, such as:

- Linearity: The Fourier transform of a linear combination of images is equal to the linear combination of their Fourier transforms. That is, if $f(x,y) = af_1(x,y) + bf_2(x,y)$, then $F(u,v) = aF_1(u,v) + bF_2(u,v)$, where $a$ and $b$ are constants.
- Shift-invariance: The Fourier transform of a shifted image is equal to the Fourier transform of the original image multiplied by a complex exponential. That is, if $f(x,y) = f_1(x-x_0, y-y_0)$, then $F(u,v) = F_1(u,v) e^{-j2\pi(ux_0/M+vy_0/N)}$, where $x_0$ and $y_0$ are the shifts.
- Convolution theorem: The Fourier transform of the convolution of two images is equal to the product of their Fourier transforms. That is, if $f(x,y) = f_1(x,y) * f_2(x,y)$, then $F(u,v) = F