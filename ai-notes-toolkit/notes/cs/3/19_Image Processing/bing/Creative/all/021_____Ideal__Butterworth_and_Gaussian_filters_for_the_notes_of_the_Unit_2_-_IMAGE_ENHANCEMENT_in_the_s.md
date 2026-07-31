# Ideal, Butterworth and Gaussian filters

- Ideal, Butterworth and Gaussian filters are types of frequency domain filters that are used for image enhancement in digital image processing.
- Frequency domain filters operate on the Fourier transform of an image and modify its magnitude and/or phase to achieve the desired effect.
- Frequency domain filters can be classified into low-pass, high-pass, band-pass and band-reject filters depending on the range of frequencies they allow or block.
- Ideal, Butterworth and Gaussian filters can be applied as any of these types of filters by changing their parameters.

## Ideal filter

- An ideal filter is a filter that has a sharp cutoff at a certain frequency, meaning that it passes all frequencies below or above that frequency without any attenuation, and blocks all frequencies above or below that frequency with complete attenuation.
- An ideal filter has a rectangular shape in the frequency domain, and a sinc function shape in the spatial domain.
- An ideal filter is not physically realizable, as it requires infinite impulse response and infinite delay.
- An ideal filter can cause ringing artifacts and Gibbs phenomenon in the filtered image due to the abrupt transition and the sinc function oscillations.

## Butterworth filter

- A Butterworth filter is a filter that has a smooth transition at a certain frequency, meaning that it passes frequencies below or above that frequency with decreasing or increasing attenuation, and blocks frequencies above or below that frequency with increasing or decreasing attenuation.
- A Butterworth filter has a circular or elliptical shape in the frequency domain, and a Gaussian-like shape in the spatial domain.
- A Butterworth filter is physically realizable, as it has a finite impulse response and a finite delay.
- A Butterworth filter can reduce ringing artifacts and Gibbs phenomenon in the filtered image due to the smooth transition and the Gaussian-like shape.

## Gaussian filter

- A Gaussian filter is a filter that has a Gaussian distribution at a certain frequency, meaning that it passes frequencies around that frequency with the highest attenuation, and blocks frequencies far from that frequency with the lowest attenuation.
- A Gaussian filter has a bell-shaped curve in the frequency domain, and a Gaussian shape in the spatial domain.
- A Gaussian filter is physically realizable, as it has a finite impulse response and a finite delay.
- A Gaussian filter can eliminate ringing artifacts and Gibbs phenomenon in the filtered image due to the Gaussian distribution and the Gaussian shape.