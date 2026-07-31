### Log–Spectral Distance

- The log-spectral distance (LSD) is a distance measure between two spectra, expressed in decibels (dB).
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as:

$$
D_{LS} = \frac{1}{2\pi} \int_{-\pi}^{\pi} \left[ 10 \log_{10} \frac{P(\omega)}{P^(\omega)} \right]^2 d\omega
$$

- The log-spectral distance is symmetric, unlike the Itakura–Saito distance, which is another distance measure between spectra.
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum.
- The log-spectral distance can be used to evaluate the quality of speech synthesis or speech enhancement methods, by comparing the spectra of the original and the processed speech signals.
- The log-spectral distance can also be used to measure the similarity of speech signals from different speakers or languages, by comparing the average spectra of the speech signals.