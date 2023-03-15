# Unit 2 - IMAGE ENHANCEMENT

### Ideal, Butterworth and Gaussian filters

- **Ideal filter**: An ideal filter is a filter that completely removes unwanted frequencies while preserving the desired frequencies. In the frequency domain, an ideal low-pass filter has a rectangular shape, with a value of 1 for frequencies below the cutoff frequency and a value of 0 for frequencies above the cutoff frequency. An ideal high-pass filter is the opposite, with a value of 0 for frequencies below the cutoff frequency and a value of 1 for frequencies above the cutoff frequency.

- **Butterworth filter**: A Butterworth filter is a type of signal processing filter designed to have a frequency response as flat as possible in the passband. It is also referred to as a maximally flat magnitude filter. The Butterworth filter is a good compromise between the ideal filter and a more practical filter, as it has a smooth transition between the passband and the stopband, with no ripples in the passband.

- **Gaussian filter**: A Gaussian filter is a filter whose impulse response is a Gaussian function. Gaussian filters are widely used in image processing to smooth images, reduce noise, and perform other image enhancement operations. The Gaussian filter has the property that it is separable, meaning that it can be applied to an image in two separate passes, one horizontal and one vertical, which can significantly reduce the computational cost.
