### Noise models for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing

- Noise is a random variation of pixel values in an image, which degrades the quality and information content of the image.
- Noise can be introduced during image acquisition, transmission, or processing due to various factors such as sensor defects, environmental conditions, quantization errors, compression artifacts, etc.
- Noise models are mathematical representations of the statistical properties and distributions of noise in an image, which can help in analyzing, measuring, and reducing noise.
- Some common noise models in image processing are:

  - Gaussian noise: This is a type of additive noise that follows a normal or Gaussian distribution, with a mean of zero and a constant variance. Gaussian noise is independent of the pixel values and can be caused by thermal fluctuations, sensor noise, etc. The probability density function (PDF) of Gaussian noise is given by:

    ```math
    p(z) = \frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(z-\mu)^2}{2\sigma^2}}
    ```

    where z is the noise value, $\mu$ is the mean, and $\sigma$ is the standard deviation.

  - Impulse noise: This is a type of noise that affects only a small fraction of pixels in an image, by replacing them with extreme values (either 0 or 255). Impulse noise can be caused by transmission errors, faulty memory locations, etc. The PDF of impulse noise is given by:

    ```math
    p(z) = \begin{cases}
    p_a, & \text{if } z = a \\
    p_b, & \text{if } z = b \\
    0, & \text{otherwise}
    \end{cases}
    ```

    where z is the noise value, a and b are the extreme values, and $p_a$ and $p_b$ are the probabilities of occurrence of a and b, respectively.

  - Poisson noise: This is a type of noise that follows a Poisson distribution, which depends on the pixel values. Poisson noise is proportional to the square root of the pixel intensity and can be caused by photon counting errors, low-light conditions, etc. The PDF of Poisson noise is given by:

    ```math
    p(z) = \frac{\lambda^z e^{-\lambda}}{z!}
    ```

    where z is the noise value, and $\lambda$ is the mean and variance of the distribution.

  - Uniform noise: This is a type of noise that follows a uniform distribution, with a constant probability for any value in a given range. Uniform noise can be caused by quantization errors, analog-to-digital conversion, etc. The PDF of uniform noise is given by:

    ```math
    p(z) = \begin{cases}
    \frac{1}{b-a}, & \text{if } a \leq z \leq b \\
    0, & \text{otherwise}
    \end{cases}
    ```

    where z is the noise value, and a and b are the lower and upper bounds of the range, respectively.

- Noise models can be used to design and evaluate image restoration techniques, which aim to recover the original image from the noisy image. Some common image restoration techniques are:

  - Spatial filtering: This is a technique that applies a filter or a mask to the noisy image, which modifies the pixel values based on their neighborhood. Spatial filters can be linear or nonlinear, depending on the filter operation. Some examples of spatial filters are:

    - Mean filter: This is a linear filter that replaces each pixel value with the average of its neighbors. Mean filter can reduce Gaussian noise, but also blurs the image edges and details.
    - Median filter: This is a nonlinear filter that replaces each pixel value with the median of its neighbors. Median filter can reduce impulse noise, while preserving the image edges and details.
    - Bilateral filter: This is a nonlinear filter that replaces each pixel value with a weighted average of its neighbors, where the weights depend on both the spatial and intensity differences. Bilateral filter can reduce Gaussian noise, while preserving the image edges and details.

  - Frequency domain filtering: This is a technique that transforms the noisy image from the spatial domain to the frequency domain, using a transform such as Fourier transform, and applies a filter or a mask to the frequency components, which modifies the amplitude and/or phase of the components. Frequency domain filters can be low-pass, high-pass, band-pass