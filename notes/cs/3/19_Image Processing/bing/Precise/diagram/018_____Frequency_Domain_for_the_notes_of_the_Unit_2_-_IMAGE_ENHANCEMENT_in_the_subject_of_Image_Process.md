### Frequency Domain

- Image enhancement in the frequency domain is based on modifying the Fourier transform of an image.
- The Fourier transform is a mathematical tool that decomposes an image into its sine and cosine components.
- The process of image enhancement in the frequency domain involves the following steps:
  1. Compute the Fourier transform of the image.
  2. Modify the Fourier transform to enhance certain image characteristics.
  3. Compute the inverse Fourier transform to obtain the enhanced image.
- The most common technique for modifying the Fourier transform is filtering.
- Filtering involves multiplying the Fourier transform of the image by a filter function.
- The filter function is designed to attenuate or amplify certain frequency components of the image.
- Low-pass filters attenuate high-frequency components, resulting in a smoothing or blurring effect.
- High-pass filters attenuate low-frequency components, resulting in a sharpening effect.
- Band-pass filters attenuate both low- and high-frequency components, preserving only a certain band of frequencies.
- Notch filters attenuate a specific frequency or range of frequencies, which can be useful for removing periodic noise from an image.
- The choice of filter function depends on the specific enhancement goal and the characteristics of the image.