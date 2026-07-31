### Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filters are applied by transforming the image from spatial domain to frequency domain using Fourier transform, applying the filter in the frequency domain, and then transforming the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components and preserve low frequency components  .
- Smoothing filters are used for noise reduction, contrast enhancement, and blurring of images  .
- Commonly used smoothing filters are ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter  .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components and preserve high frequency components  .
- Sharpening filters are used for edge detection, enhancement of fine details, and sharpening of images  .
- Commonly used sharpening filters are ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter  .
- The following diagram shows the basic steps of frequency domain filtering:

![Frequency domain filtering diagram](https://miro.medium.com/max/1400/1*0fZ4YkZ4a4y4l0f0Q9y0jw.png)

- The following diagram shows the frequency response of different types of low pass and high pass filters:

![Frequency response diagram](https://media.geeksforgeeks.org/wp-content/uploads/20191205174032/frequency-domain-filters.png)