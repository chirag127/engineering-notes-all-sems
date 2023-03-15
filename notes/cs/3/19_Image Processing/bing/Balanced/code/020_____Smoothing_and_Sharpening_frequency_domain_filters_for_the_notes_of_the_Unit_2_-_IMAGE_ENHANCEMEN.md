### Smoothing and Sharpening Frequency Domain Filters

- Frequency domain filters are used for smoothing and sharpening of images by removal of high or low frequency components .
- Frequency domain filters are different from spatial domain filters as they mainly focus on the frequency of the images .
- Frequency domain filtering involves the following steps:
  - Convert the image from spatial domain to frequency domain using Fourier transform.
  - Apply a filter function to the frequency domain image.
  - Convert the filtered image back to spatial domain using inverse Fourier transform.
- Smoothing filters are used to reduce and suppress image noises by attenuating high frequency components.
- Sharpening filters are used to enhance image details by amplifying high frequency components.
- Common types of frequency domain filters are :
  - Ideal filter: A filter that has a sharp cutoff at a certain frequency.
  - Butterworth filter: A filter that has a smooth transition at a certain frequency.
  - Gaussian filter: A filter that has a Gaussian shape in the frequency domain.
- The cutoff frequency of a filter determines the amount of smoothing or sharpening applied to the image .
- The order of a filter determines the steepness of the filter function in the frequency domain .
- The filter function can be either low pass or high pass :
  - Low pass filter: A filter that passes low frequency components and attenuates high frequency components.
  - High pass filter: A filter that passes high frequency components and attenuates low frequency components.
- Smoothing can be achieved by applying a low pass filter to the frequency domain image .
- Sharpening can be achieved by applying a high pass filter to the frequency domain image .
- Some examples of smoothing and sharpening frequency domain filters are  :

```markdown
| Smoothing filter | Sharpening filter |
| ---------------- | ----------------- |
| Ideal low pass filter | Ideal high pass filter |
| Butterworth low pass filter | Butterworth high pass filter |
| Gaussian low pass filter | Gaussian high pass filter |
| Homomorphic filter | Laplacian filter |
| Wiener filter | Unsharp masking filter |
```