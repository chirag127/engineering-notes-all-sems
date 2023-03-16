### Log–Spectral Distance

- Log–Spectral Distance (LSD) is a measure of similarity or dissimilarity between two spectra, usually expressed in decibels (dB).
- It is calculated as the root mean square (RMS) of the difference between the logarithms of the power spectra of the two signals.
- Mathematically, the LSD between spectra P(ω) and P̂(ω) is defined as:

  D<sub>LS</sub> = (1/2π) ∫<sub>−π</sub><sup>π</sup> [10 log<sub>10</sub> P(ω)/P̂(ω)]<sup>2</sup> dω

- LSD is symmetric, meaning that D<sub>LS</sub>(P, P̂) = D<sub>LS</sub>(P̂, P).
- LSD is often used in speech coding to evaluate the quality of the reconstructed speech signal after compression or quantization.
- LSD can also be used to compare different spectral representations of speech, such as linear predictive coding (LPC), mel-frequency cepstral coefficients (MFCC), or perceptual linear prediction (PLP).
- LSD is related to other spectral distance measures, such as the Itakura–Saito distance, the cepstral distance, and the spectral distortion. However, LSD has some advantages over these measures, such as being more robust to noise and more consistent with human perception.