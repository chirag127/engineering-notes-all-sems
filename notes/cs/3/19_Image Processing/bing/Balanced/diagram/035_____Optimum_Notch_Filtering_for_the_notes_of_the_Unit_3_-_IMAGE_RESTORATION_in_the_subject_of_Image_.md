### Optimum Notch Filtering

- Optimum notch filtering is a technique for reducing periodic noise in images by minimizing the local variance of the restored image .
- Periodic noise is a type of noise that has a regular pattern in the spatial or frequency domain, such as interference lines, moire patterns, or halftone dots.
- Optimum notch filtering consists of three steps :
  - Identifying the regions of noise frequencies in the frequency domain by analyzing the spectrum of the noisy image.
  - Extracting the repetitive pattern of the periodic noise by applying a notch-pass filter on every noise frequency and then applying an inverse 2-D Fourier transform to obtain the pattern in the spatial domain.
  - Restoring the output image by subtracting a variable weighted portion of the noise pattern from the noisy image.
- A notch-pass filter is a type of filter that passes a very narrow range of frequencies around a center frequency, while rejecting all other frequencies. It is the opposite of a notch-reject filter, which rejects a narrow range of frequencies and passes all other frequencies.
- A notch-pass filter can be designed by using a Gaussian function or a Butterworth function as the transfer function. The center frequency and the bandwidth of the filter can be adjusted to match the noise frequency and the noise width.
- Optimum notch filtering can effectively remove periodic noise from images without affecting the image details or introducing artifacts . However, it requires accurate estimation of the noise frequencies and the noise pattern, which may not be easy in some cases .