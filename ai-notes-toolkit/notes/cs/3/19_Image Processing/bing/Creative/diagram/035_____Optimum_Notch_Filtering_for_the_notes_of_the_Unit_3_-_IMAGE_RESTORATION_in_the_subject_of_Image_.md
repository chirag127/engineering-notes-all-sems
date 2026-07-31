### Optimum Notch Filtering

- Optimum notch filtering is a technique for reducing periodic noise in images by minimizing the local variance of the restored image .
- Periodic noise is a type of noise that has a regular pattern in the spatial or frequency domain, such as interference lines, moiré patterns, or screen flicker.
- Optimum notch filtering consists of three steps:
  - Identifying the regions of noise frequencies by analyzing the spectrum of the noisy image.
  - Extracting the repetitive pattern of the periodic noise by applying a notch-pass filter on every noise frequency and then performing an inverse Fourier transform.
  - Restoring the output image by subtracting a variable weighted portion of the repetitive pattern from the noisy image.
- A notch-pass filter is a type of filter that passes a very narrow set of frequencies around a center frequency, while rejecting all other frequencies.
- A notch-pass filter can be designed by multiplying a low-pass filter and a high-pass filter, both with the same center frequency and bandwidth.
- A notch-pass filter can be implemented in the frequency domain by multiplying the Fourier transform of the noisy image with the filter mask.
- A notch-pass filter can be either Gaussian or Butterworth, depending on the shape of the filter mask.
- The variable weighted portion of the repetitive pattern is determined by the optimum notch filter method, which tries to minimize the local variance of the restored image .
- The optimum notch filter method can be formulated as an optimization problem, where the objective function is the local variance of the restored image and the constraint is the energy conservation of the image .
- The optimum notch filter method can be solved by using the Lagrange multiplier technique or the gradient descent method .
- Optimum notch filtering can effectively remove periodic noise from images, while preserving the image details and edges.