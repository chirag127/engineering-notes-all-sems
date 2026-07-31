# Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components and preserve low frequency components  .
- Smoothing filters are used for noise reduction, contrast enhancement, and blurring of images  .
- Commonly seen smoothing filters include ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components and preserve high frequency components  .
- Sharpening filters are used for edge detection, enhancement of details, and sharpening of images  .
- Commonly seen sharpening filters include ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter .
- The choice of filter function depends on the characteristics of the image and the desired output .
- The filter function can be designed in the frequency domain or in the spatial domain and then converted to the frequency domain using Fourier transform .
- The filter function can be applied to the frequency domain image by multiplying it with the image or by convolving it with the image .
- The filter function can be modified by adding or subtracting a constant term to adjust the brightness of the output image .
- The filter function can be combined with other filter functions to achieve different effects, such as band pass filter, band reject filter, notch filter, etc .