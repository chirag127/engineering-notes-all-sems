# Ideal, Butterworth and Gaussian filters

- Ideal, Butterworth and Gaussian filters are types of frequency domain filters that are used for image enhancement in image processing.
- Frequency domain filters modify the Fourier transform of an image to achieve a desired effect, such as sharpening, smoothing, or removing noise.
- Ideal, Butterworth and Gaussian filters differ in the shape and smoothness of their transfer functions, which affect the quality and performance of the filtering.

## Ideal filter

- An ideal filter is a filter that has a sharp cutoff frequency and a constant magnitude response. It is also called a brick-wall filter or a rectangular filter.
- An ideal filter can be either a low-pass filter (ILPF) or a high-pass filter (IHPF), depending on whether it passes or blocks low-frequency components of the image.
- An ideal filter has the advantage of being simple and easy to implement, but it has the disadvantage of introducing ringing artifacts and aliasing in the filtered image, due to the abrupt changes in the frequency domain.

## Butterworth filter

- A Butterworth filter is a filter that has a smooth and monotonic magnitude response that approaches the ideal filter as the order of the filter increases. It is also called a maximally flat filter or a smooth filter.
- A Butterworth filter can be either a low-pass filter (BLPF) or a high-pass filter (BHPF), depending on whether it passes or blocks low-frequency components of the image.
- A Butterworth filter has the advantage of being more realistic and natural than the ideal filter, but it has the disadvantage of having a slower rolloff and a larger transition band, which may result in some unwanted frequencies being passed or blocked.

## Gaussian filter

- A Gaussian filter is a filter that has a bell-shaped magnitude response that follows the Gaussian distribution. It is also called a normal filter or a Gaussian bell filter.
- A Gaussian filter can be either a low-pass filter (GLPF) or a high-pass filter (GHPF), depending on whether it passes or blocks low-frequency components of the image.
- A Gaussian filter has the advantage of being smooth and continuous in both the spatial and frequency domains, which reduces the ringing artifacts and aliasing in the filtered image, but it has the disadvantage of having a wider bandwidth and a lower cutoff frequency than the ideal filter, which may result in some loss of image details.