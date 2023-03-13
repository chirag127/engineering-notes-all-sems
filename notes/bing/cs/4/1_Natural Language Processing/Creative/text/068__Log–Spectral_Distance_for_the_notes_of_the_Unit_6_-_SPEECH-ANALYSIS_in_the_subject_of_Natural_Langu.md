### Log–Spectral Distance

- The log-spectral distance (LSD), also referred to as log-spectral distortion or root mean square log-spectral distance, is a distance measure between two spectra .
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as :

  D<sub>LS</sub> = (1/2π) ∫<sub>−π</sub><sup>π</sup> [10 log<sub>10</sub> P(ω)/P^(ω)]<sup>2</sup> dω

- Unlike the Itakura–Saito distance, the log-spectral distance is symmetric .
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum .
- The log-spectral distance can be used to measure the quality of speech signals, such as the effects of noise, filtering, or compression.
- The log-spectral distance can also be used to compare different speech coding methods, such as linear predictive coding (LPC), code-excited linear prediction (CELP), or vector quantization (VQ).
- The log-spectral distance can be computed efficiently using the fast Fourier transform (FFT) or the discrete cosine transform (DCT).