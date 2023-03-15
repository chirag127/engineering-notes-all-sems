# Band reject Filters

- A band reject filter is a type of frequency domain filter that blocks or attenuates a range of frequencies in an image and lets the other frequencies pass through .
- A band reject filter is useful when the general location of the noise in the frequency domain is known.
- A band reject filter can be implemented by adding a low-pass filter and a high-pass filter with different cutoff frequencies.
- A band reject filter can be either ideal, Gaussian, or Butterworth, depending on the shape and smoothness of the filter function.
- A band reject filter can be applied to an image by multiplying its Fourier transform with the filter function and then taking the inverse Fourier transform of the result.

## Example

- Here is an example of applying a band reject filter to an image with periodic noise.

- Original image:

![Original image](https://blog.minhazav.dev/images/zone-plate.png)

- Fourier transform of the image:

![Fourier transform of the image](https://blog.minhazav.dev/images/zone-plate-fft.png)

- Band reject filter function:

![Band reject filter function](https://blog.minhazav.dev/images/zone-plate-bandreject-filter.png)

- Filtered image:

![Filtered image](https://blog.minhazav.dev/images/zone-plate-bandreject.png)

## References

: BANDREJECT_FILTER - L3Harris Geospatial. https://www.l3harrisgeospatial.com/docs/BANDREJECT_FILTER.html

: Lowpass, Highpass, Bandreject and Bandpass filters in image processing using Zone plate. https://blog.minhazav.dev/lowpass-highpass-band-reject-and-band-pass-filter/