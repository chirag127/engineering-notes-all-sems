### Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are low pass filters that attenuate (suppress) high frequency components without disturbing low frequency components  .
- Smoothing filters are used for noise reduction, contrast enhancement, and blurring of images  .
- Commonly seen smoothing filters include ideal low pass filter, Butterworth low pass filter, and Gaussian low pass filter  .
- Sharpening filters are high pass filters that attenuate (suppress) low frequency components without disturbing high frequency components  .
- Sharpening filters are used for edge detection, enhancement of fine details, and sharpening of images  .
- Commonly seen sharpening filters include ideal high pass filter, Butterworth high pass filter, and Gaussian high pass filter  .
- Sometimes, it is possible to remove very high and very low frequency components using band pass filters or band reject filters .
- The choice of filter function depends on the characteristics of the image and the desired output .
- The following diagram illustrates the frequency domain filtering process:

![Frequency domain filtering process](https://miro.medium.com/max/1400/1*0yZ4tQ0Z2wYwY6lZ8QbZ1w.png)

: https://www.geeksforgeeks.org/frequency-domain-filters-and-its-types/
: https://medium.com/@devangdayal/frequency-domain-filtering-on-an-image-using-opencv-26bfcc97e23b
: https://www.dynamsoft.com/blog/insights/image-processing/image-processing-101-spatial-filters-convolution/
: https://www.researchgate.net/publication/321849631_Image_Smoothening_and_Sharpening_using_Frequency_Domain_Filtering_Technique