### Band reject Filters

- A band reject filter is a type of frequency domain filter that blocks or attenuates a range of frequencies in an image and lets the other frequencies pass through .
- A band reject filter is useful when the general location of the noise in the frequency domain is known .
- A band reject filter can be implemented by adding a low-pass filter and a high-pass filter with different cutoff frequencies.
- A band reject filter can be either ideal, Gaussian, or Butterworth, depending on the shape and smoothness of the filter function.
- A band reject filter can be applied to a one-channel image by using the BANDREJECT_FILTER function in IDL.
- A band reject filter can be used to remove periodic noise or interference patterns from an image .