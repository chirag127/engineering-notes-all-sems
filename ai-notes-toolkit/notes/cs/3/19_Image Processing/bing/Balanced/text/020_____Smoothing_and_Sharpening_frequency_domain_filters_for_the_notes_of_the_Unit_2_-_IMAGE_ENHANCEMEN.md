### Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components without disturbing low frequency components  .
- Smoothing filters are used for noise reduction, contrast enhancement, and blurring of images  .
- Commonly used smoothing filters are ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter  .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components without disturbing high frequency components  .
- Sharpening filters are used for edge detection, enhancement of fine details, and sharpening of images  .
- Commonly used sharpening filters are ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter  .
- The choice of filter function depends on the desired characteristics of the output image, such as the cutoff frequency, the transition band, and the amount of ringing .
- The filter function can be designed in either the frequency domain or the spatial domain, and then converted to the other domain using Fourier transform or inverse Fourier transform .
- The filter function can also be modified by using a window function to reduce the side lobes and improve the frequency response .
- The filter function can also be combined with other techniques, such as histogram equalization, to improve the contrast and brightness of the output image.