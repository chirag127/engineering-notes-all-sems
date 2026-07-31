### Optimum Notch Filtering

- Optimum notch filtering is a technique for reducing periodic noise in images by minimizing the local variance of the restored image .
- Periodic noise is a type of noise that has a regular pattern in the spatial or frequency domain, such as interference lines, moiré patterns, or screen flicker.
- Optimum notch filtering consists of three steps :
  - Identifying the regions of noise frequencies by analyzing the spectrum of the noisy image.
  - Extracting the repetitive pattern of the periodic noise by applying a notch-pass filter on every noise frequency and then applying an inverse 2-D Fourier transform.
  - Restoring the output image by subtracting a variable weighted portion of the repetitive pattern from the contaminated image.
- A notch-pass filter is a type of filter that passes a very narrow set of frequencies around a center frequency, while rejecting all other frequencies.
- A notch-pass filter can be designed by multiplying a low-pass filter and a high-pass filter, both with the same center frequency and bandwidth.
- A notch-pass filter can also be designed by using a Gaussian function with a negative amplitude and a specified center frequency and standard deviation.
- The optimum weight for subtracting the repetitive pattern from the noisy image can be determined by minimizing the mean square error between the original image and the restored image .
- Optimum notch filtering can effectively remove periodic noise from images without affecting the image details or introducing artifacts .