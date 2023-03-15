### Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image, such as a low pass filter or a high pass filter.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components and preserve low frequency components  .
- Smoothing filters are used for noise reduction, blurring, and smoothing of images .
- Commonly used smoothing filters include ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components and preserve high frequency components  .
- Sharpening filters are used for edge detection, enhancement, and sharpening of images .
- Commonly used sharpening filters include ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter .
- Sometimes, it is possible to remove very high and very low frequency components using band pass filters or band reject filters .
- Band pass filters allow a certain range of frequencies to pass through and reject others .
- Band reject filters allow all frequencies to pass through except a certain range of frequencies .
- Band pass and band reject filters are used for selective filtering of images .