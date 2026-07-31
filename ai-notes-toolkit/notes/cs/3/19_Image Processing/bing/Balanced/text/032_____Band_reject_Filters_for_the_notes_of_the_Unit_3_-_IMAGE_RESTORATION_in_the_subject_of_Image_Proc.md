### Band reject Filters

- A band reject filter is a type of frequency domain filter that blocks or attenuates a range of frequencies in an image and lets the other frequencies pass through .
- A band reject filter is useful when the general location of the noise in the frequency domain is known .
- A band reject filter can be implemented by adding a low-pass filter and a high-pass filter with different cutoff frequencies.
- A band reject filter can have different shapes, such as circular, elliptical, or rectangular, depending on the desired frequency range and transition width.
- A band reject filter can be applied to an image by multiplying its Fourier transform with the filter function in the frequency domain, and then taking the inverse Fourier transform to obtain the filtered image .
- A band reject filter can reduce the effects of periodic noise, such as interference patterns or moiré effects, in an image .
- A band reject filter can also be used for image enhancement, such as edge detection or contrast enhancement, by subtracting the filtered image from the original image.