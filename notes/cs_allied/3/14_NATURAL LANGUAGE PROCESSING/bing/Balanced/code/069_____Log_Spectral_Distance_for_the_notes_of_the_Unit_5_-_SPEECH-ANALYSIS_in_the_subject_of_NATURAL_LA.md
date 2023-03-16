# Log–Spectral Distance

- The log-spectral distance (LSD), also referred to as log-spectral distortion or root mean square log-spectral distance, is a distance measure (expressed in dB) between two spectra .
- The log-spectral distance between spectra P(ω) and P^(ω) is defined as p-norm:

```
D_LS = (1/2π) ∫[10 log10(P(ω)/P^(ω))]^p dω
```

- The log-spectral distance is symmetric, unlike the Itakura–Saito distance .
- In speech coding, log spectral distortion for a given frame is defined as the root mean square difference between the original LPC log power spectrum and the quantized or interpolated LPC log power spectrum .
- The log-spectral distance can be used to measure the quality of speech synthesis or speech recognition systems, by comparing the spectra of the original and the synthesized or recognized speech signals .
- The log-spectral distance can also be used to measure the similarity of two speech signals, by computing the average log-spectral distance over a set of frames .
- The log-spectral distance is sensitive to the phase difference between the spectra, and may not reflect the perceptual difference between the speech signals .