# Ideal, Butterworth and Gaussian filters for the notes of the Unit 2 - IMAGE ENHANCEMENT in the subject of Image Processing

- Image enhancement is a process of improving the quality and appearance of an image by modifying its features, such as contrast, brightness, sharpness, etc.
- Image enhancement can be done in the spatial domain or the frequency domain. In the spatial domain, the pixel values of an image are directly manipulated. In the frequency domain, the image is transformed into its frequency components, and then filtered and transformed back to the spatial domain.
- Filters are mathematical functions that modify the frequency components of an image. Filters can be classified into low-pass, high-pass, band-pass and band-reject filters, depending on which frequency components they allow or reject.
- Ideal, Butterworth and Gaussian filters are three types of filters that can be used for image enhancement in the frequency domain. They differ in their shape and smoothness of the transition between the passband and the stopband.

## Ideal filter

- An ideal filter is a filter that has a sharp cutoff at a certain frequency. It allows all the frequency components below or above the cutoff frequency, and rejects all the other frequency components. 
- An ideal low-pass filter (ILPF) preserves the low-frequency components of an image, and removes the high-frequency components, such as noise and edges. An ideal high-pass filter (IHPF) preserves the high-frequency components of an image, and removes the low-frequency components, such as background and smooth regions.
- An ideal filter has a rectangular shape in the frequency domain, as shown in the figure below. The cutoff frequency is denoted by D0.

![Ideal filter](https://i.imgur.com/0n1QZ0D.png)

- An ideal filter has a simple mathematical expression, given by:

  - ILPF: H(u,v) = 1, if D(u,v) <= D0; 0, otherwise
  - IHPF: H(u,v) = 0, if D(u,v) <= D0; 1, otherwise

  where D(u,v) is the distance from the origin to the point (u,v) in the frequency domain, and H(u,v) is the filter function.

- An ideal filter has some advantages, such as easy implementation and clear separation of frequency components. However, it also has some disadvantages, such as:

  - It introduces ringing artifacts in the spatial domain, due to the Gibbs phenomenon. This is because the ideal filter has infinite impulse response (IIR) in the spatial domain, which means it has infinite support and oscillations.
  - It is not a realistic filter, because it assumes an infinite resolution and a perfect cutoff frequency, which are not possible in practice.

## Butterworth filter

- A Butterworth filter is a filter that has a smooth transition between the passband and the stopband. It allows some of the frequency components near the cutoff frequency, and rejects some of the frequency components far from the cutoff frequency. The degree of smoothness is controlled by a parameter called the order of the filter.
- A Butterworth low-pass filter (BLPF) preserves the low-frequency components of an image, and attenuates the high-frequency components, depending on their distance from the cutoff frequency. A Butterworth high-pass filter (BHPF) preserves the high-frequency components of an image, and attenuates the low-frequency components, depending on their distance from the cutoff frequency.
- A Butterworth filter has a circular shape in the frequency domain, as shown in the figure below. The cutoff frequency is denoted by D0, and the order of the filter is denoted by n. A higher order means a sharper transition and a closer approximation to the ideal filter.

![Butterworth filter](https://i.imgur.com/9z9aZ4N.png)

- A Butterworth filter has a mathematical expression, given by:

  - BLPF: H(u,v) = 1 / (1 + (D(u,v) / D0)^(2n))
  - BHPF: H(u,v) = 1 / (1 + (D0 / D(u,v))^(2n))

  where D(u,v) is the distance from the origin to the point (u,v) in the frequency domain, and H(u,v) is the filter function.

- A Butterworth filter has some advantages, such as:

  - It does not introduce ringing artifacts in the spatial domain, because it has finite impulse response (FIR) in the spatial domain, which means it has finite support and no oscillations.