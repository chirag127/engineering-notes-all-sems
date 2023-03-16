### Log–Spectral Distance

- The log-spectral distance (LSD), also referred to as log-spectral distortion or root mean square log-spectral distance, is a distance measure (expressed in dB) between two spectra .
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as p-norm:

`D_LS = (1/2π) ∫[10 log10 P(ω)/P^(ω)]^p dω`

- Unlike the Itakura–Saito distance, the log-spectral distance is symmetric .
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum .
- Log spectral distance is used to measure the quality of speech synthesis and speech recognition systems .
- Log spectral distance can be computed efficiently using the fast Fourier transform (FFT) algorithm .