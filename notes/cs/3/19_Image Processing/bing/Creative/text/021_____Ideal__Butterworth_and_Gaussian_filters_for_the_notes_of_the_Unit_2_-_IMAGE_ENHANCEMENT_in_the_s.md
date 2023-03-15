### Ideal, Butterworth and Gaussian filters

- Ideal, Butterworth and Gaussian filters are types of frequency domain filters that are used for image enhancement in digital image processing.
- Frequency domain filters operate on the Fourier transform of an image and modify its magnitude and/or phase to produce a filtered image.
- Ideal, Butterworth and Gaussian filters can be either low-pass or high-pass filters, depending on whether they attenuate or preserve the low-frequency or high-frequency components of an image.
- Low-pass filters are used to smooth an image and remove noise, while high-pass filters are used to sharpen an image and enhance edges.

#### Ideal filter

- An ideal filter is a filter that has a sharp cutoff frequency and a constant magnitude response. It is also called a brick-wall filter because of its rectangular shape in the frequency domain.
- An ideal low-pass filter (ILPF) has a magnitude response of 1 for frequencies below the cutoff frequency and 0 for frequencies above it. An ideal high-pass filter (IHPF) has a magnitude response of 0 for frequencies below the cutoff frequency and 1 for frequencies above it.
- An ideal filter can be implemented by multiplying the Fourier transform of an image by a circular mask that has a radius equal to the cutoff frequency.
- An ideal filter has the advantage of being simple and easy to design, but it has the disadvantage of producing ringing artifacts in the spatial domain due to the Gibbs phenomenon. Ringing artifacts are oscillations that occur near the edges of an image due to the abrupt changes in the frequency domain.

#### Butterworth filter

- A Butterworth filter is a filter that has a smooth cutoff frequency and a magnitude response that decreases monotonically as the frequency increases or decreases from the cutoff frequency. It is also called a maximally flat filter because it has no ripples in the passband or the stopband.
- A Butterworth low-pass filter (BLPF) has a magnitude response that is given by the formula:

$$
H(u,v) = \frac{1}{1 + \left(\frac{D(u,v)}{D_0}\right)^{2n}}
$$

where $D(u,v)$ is the distance from the origin to the point $(u,v)$ in the frequency domain, $D_0$ is the cutoff frequency, and $n$ is the order of the filter. A Butterworth high-pass filter (BHPF) has a magnitude response that is given by the formula:

$$
H(u,v) = \frac{1}{1 + \left(\frac{D_0}{D(u,v)}\right)^{2n}}
$$

- A Butterworth filter can be implemented by multiplying the Fourier transform of an image by the magnitude response function.
- A Butterworth filter has the advantage of being smooth and having no ringing artifacts, but it has the disadvantage of having a gradual transition from the passband to the stopband, which may result in some loss of image details.

#### Gaussian filter

- A Gaussian filter is a filter that has a Gaussian-shaped magnitude response in the frequency domain. It is also called a bell-shaped filter because of its curved shape.
- A Gaussian low-pass filter (GLPF) has a magnitude response that is given by the formula:

$$
H(u,v) = e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

where $D(u,v)$ is the distance from the origin to the point $(u,v)$ in the frequency domain, and $D_0$ is the cutoff frequency. A Gaussian high-pass filter (GHPF) has a magnitude response that is given by the formula:

$$
H(u,v) = 1 - e^{-\frac{D^2(u,v)}{2D_0^2}}
$$

- A Gaussian filter can be implemented by multiplying the Fourier transform of an image by the magnitude response function.
- A Gaussian filter has the advantage of being smooth and having no ringing artifacts, but it has the disadvantage of having a very gradual transition from the passband to the stopband, which may result in more loss of image details than a Butterworth filter.