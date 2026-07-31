### Introduction to Fourier Transform

The Fourier transform is a mathematical tool that allows us to decompose an image into its frequency components. The frequency components are the sine and cosine waves of different frequencies, amplitudes, and phases that make up the image. The Fourier transform can be used to analyze and manipulate images in various ways, such as:

- Enhancement: We can use the Fourier transform to modify the frequency components of an image to improve its contrast, brightness, sharpness, or remove noise.
- Analysis: We can use the Fourier transform to measure the frequency content of an image, which can reveal some properties or patterns of the image that are not visible in the spatial domain.
- Restoration: We can use the Fourier transform to recover an image that has been degraded by some distortion, such as blurring, motion, or noise, by applying an inverse filter in the frequency domain.
- Compression: We can use the Fourier transform to reduce the size of an image by discarding some of the frequency components that are less important or perceptible to the human eye.

The Fourier transform of an image can be computed using the following formula:

$$F(u,v) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) e^{-j2\pi(ux+vy)} dx dy$$

where $f(x,y)$ is the image in the spatial domain, $F(u,v)$ is the image in the frequency domain, and $u$ and $v$ are the frequency variables. The inverse Fourier transform can be computed using the following formula:

$$f(x,y) = \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} F(u,v) e^{j2\pi(ux+vy)} du dv$$

The Fourier transform of an image is a complex-valued function, which means that it has a real part and an imaginary part. The real part and the imaginary part can be combined to form two other representations of the Fourier transform: the magnitude and the phase. The magnitude of the Fourier transform indicates the amount of energy or power at each frequency, while the phase of the Fourier transform indicates the position or orientation of each frequency component. The magnitude and the phase can be computed using the following formulas:

$$|F(u,v)| = \sqrt{\text{Re}(F(u,v))^2 + \text{Im}(F(u,v))^2}$$

$$\angle F(u,v) = \tan^{-1} \frac{\text{Im}(F(u,v))}{\text{Re}(F(u,v))}$$

where $\text{Re}(F(u,v))$ and $\text{Im}(F(u,v))$ are the real and imaginary parts of the Fourier transform, respectively.

The Fourier transform of an image can be visualized using a 2D plot, where the horizontal and vertical axes represent the frequency variables $u$ and $v$, and the color or intensity of each pixel represents the magnitude or the phase of the Fourier transform. The center of the plot corresponds to the zero frequency, or the DC component, which represents the average value of the image. The farther away from the center, the higher the frequency, or the finer the details of the image. The direction of the frequency corresponds to the orientation of the edges or lines in the image. For example, a vertical edge in the image will produce a horizontal line in the Fourier transform, and vice versa.

The following figure shows an example of an image and its Fourier transform. The image is a square with a diagonal line, and the Fourier transform is a cross with two dots. The cross represents the DC component and the four corners of the square, while the two dots represent the diagonal line.

![Image and its Fourier transform](https://vincmazet.github.io/bip/filtering/img/fourier.png)