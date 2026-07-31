### Frequency Domain

- Frequency domain is a way of representing an image in terms of its frequency components, such as low-frequency (smooth) and high-frequency (sharp) details.
- Frequency domain methods of image enhancement are based on the Fourier transform, which converts an image from the spatial domain (pixel values) to the frequency domain (amplitude and phase of sinusoidal waves).
- Image enhancement in the frequency domain involves modifying the Fourier transform of the image, such as multiplying it by a filter function, and then taking the inverse Fourier transform to obtain the enhanced image.
- Frequency domain methods are useful for performing global operations on the image, such as changing the contrast, brightness, or sharpness, or removing noise or blurring.
- Frequency domain methods are also advantageous when the spatial extent of the filter is large, as convolution in the spatial domain becomes computationally expensive.
- Some common frequency domain filters are:
  - Low-pass filters: These filters attenuate the high-frequency components of the image, resulting in a smoother and less noisy image. Examples are the ideal low-pass filter, the Butterworth low-pass filter, and the Gaussian low-pass filter.
  - High-pass filters: These filters attenuate the low-frequency components of the image, resulting in a sharper and more detailed image. Examples are the ideal high-pass filter, the Butterworth high-pass filter, and the Gaussian high-pass filter.
  - Band-pass filters: These filters attenuate the frequency components outside a specified range, resulting in an image that preserves the details in that range. Examples are the ideal band-pass filter, the Butterworth band-pass filter, and the Gaussian band-pass filter.
  - Band-reject filters: These filters attenuate the frequency components inside a specified range, resulting in an image that removes the details in that range. Examples are the ideal band-reject filter, the Butterworth band-reject filter, and the Gaussian band-reject filter.
  - Notch filters: These filters attenuate the frequency components at specific locations, resulting in an image that removes the periodic noise or interference in those locations. Examples are the ideal notch filter, the Butterworth notch filter, and the Gaussian notch filter.
- Frequency domain methods of image enhancement can be applied to both grayscale and color images, but the color images need to be converted to a suitable color space, such as YCbCr or HSV, before applying the Fourier transform.