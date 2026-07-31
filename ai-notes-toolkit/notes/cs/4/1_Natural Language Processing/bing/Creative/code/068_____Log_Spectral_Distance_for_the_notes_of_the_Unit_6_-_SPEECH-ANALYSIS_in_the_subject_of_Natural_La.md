### Log–Spectral Distance

- The log-spectral distance (LSD), also referred to as log-spectral distortion or root mean square log-spectral distance, is a distance measure (expressed in dB) between two spectra .
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as:

`D_LS = (1/(2π)) ∫_(−π)^π [10 log_(10) (P(ω)/P^(ω))]^2 dω`

- Unlike the Itakura–Saito distance, the log-spectral distance is symmetric.
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum .
- The log-spectral distance can be used to measure the quality of speech synthesis or speech recognition systems, by comparing the spectra of the original and the synthesized or recognized speech signals.
- The log-spectral distance can also be used to measure the similarity of two speech signals, by computing the average log-spectral distance over all frames.