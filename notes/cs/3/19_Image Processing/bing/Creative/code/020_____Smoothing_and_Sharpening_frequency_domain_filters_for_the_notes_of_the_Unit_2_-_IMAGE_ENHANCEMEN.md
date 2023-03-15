### Smoothing and Sharpening frequency domain filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filters are applied by transforming the image from spatial domain to frequency domain using Fourier transform, applying the filter in the frequency domain, and then transforming the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components without disturbing low frequency components  .
- Smoothing filters are used for noise reduction, contrast enhancement, and blurring of images  .
- Commonly used smoothing filters in frequency domain are ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter  .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components without disturbing high frequency components  .
- Sharpening filters are used for edge detection, enhancement of fine details, and sharpening of images  .
- Commonly used sharpening filters in frequency domain are ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter  .
- The following diagram shows the effect of smoothing and sharpening filters on an image in frequency domain:

![Diagram of smoothing and sharpening filters in frequency domain](https://miro.medium.com/max/1400/1*Q0Q0Z9k0Z1x4Z4Y4f4Y4jw.png)