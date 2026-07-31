# Optimum Notch Filtering

- Optimum notch filtering is a technique for reducing periodic noise in images .
- Periodic noise is a type of noise that has a regular pattern in the spatial or frequency domain, such as interference lines, stripes, or grids.
- Optimum notch filtering consists of two stages :
  - The first stage is to extract the principal contribution of the periodic noise from the noisy image. This is done by applying a notch-pass filter in the frequency domain to isolate the noise frequencies, and then applying an inverse 2-D Fourier transform to obtain the noise pattern in the spatial domain .
  - The second stage is to restore the output image by subtracting a variable weighted portion of the noise pattern from the contaminated image. The weight is determined by minimizing the local variance of the restored image .
- Optimum notch filtering can effectively remove periodic noise without blurring the image or introducing artifacts .
- The main challenge of optimum notch filtering is to determine the regions of noise frequencies in the frequency domain. This can be done by analyzing the spectrum of the noisy image, or by using adaptive methods that adjust the notch-pass filter according to the noise characteristics .
- An example of optimum notch filtering is shown below:

![Noisy image](https://i.stack.imgur.com/4y7zW.png)

![Spectrum of noisy image](https://i.stack.imgur.com/8z0yS.png)

![Notch-pass filter](https://i.stack.imgur.com/7wZ0T.png)

![Noise pattern](https://i.stack.imgur.com/9X3Yy.png)

![Restored image](https://i.stack.imgur.com/0w0Zo.png)