# PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting meaningful information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction, which is the computation of a set of parameters that represent the characteristics of the speech signal in a compact and robust way.
- Feature extraction methods can be classified into two categories: spectral and cepstral.
- Spectral methods use the frequency domain representation of the speech signal, such as the Fourier transform, to compute features that capture the energy distribution across different frequency bands.
- Cepstral methods use the logarithm of the spectrum, followed by an inverse Fourier transform, to compute features that capture the shape of the vocal tract, which is related to the phonetic content of the speech.
- Two popular cepstral methods are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC).

## PLP

- PLP is a feature extraction method that mimics the human auditory system, by applying a series of transformations to the speech signal that account for the perceptual aspects of hearing.
- PLP consists of the following steps :
  - Pre-emphasis: a high-pass filtering that enhances the high-frequency components of the speech signal, which are usually attenuated by the vocal tract.
  - Windowing: a segmentation of the speech signal into short frames (typically 20-30 ms) with some overlap (typically 50%), and applying a window function (such as Hamming) to each frame to reduce the discontinuities at the edges.
  - Critical band analysis: a spectral analysis that divides the frequency spectrum into a number of bands (typically 18) that correspond to the critical bands of the human ear, which are the frequency regions where two tones can be perceived as distinct. The energy in each band is computed by applying a triangular filter bank to the spectrum.
  - Equal-loudness pre-emphasis: a weighting of the critical band energies according to the equal-loudness curve of the human ear, which reflects the sensitivity of the ear to different frequencies. The curve is usually approximated by a cubic spline function.
  - Intensity-loudness power law: a compression of the critical band energies according to the power law of the human ear, which reflects the nonlinear relationship between the physical intensity and the perceived loudness of a sound. The power law is usually approximated by taking the cube root of the energies.
  - Autoregressive modeling: a parametric modeling of the compressed critical band energies using an autoregressive (AR) model, which assumes that each energy value can be predicted as a linear combination of the previous values, plus some error term. The AR model coefficients are computed using the Levinson-Durbin algorithm, and are called the PLP coefficients.
  - Cepstral analysis: a conversion of the PLP coefficients into cepstral coefficients, which are the coefficients of the inverse Fourier transform of the logarithm of the AR model spectrum. The cepstral coefficients are more compact and robust than the PLP coefficients, and are usually truncated to a lower dimension (typically 12-14).

## MFCC

- MFCC is another feature extraction method that mimics the human auditory system, by applying a similar series of transformations to the speech signal as PLP, but with some differences.
- MFCC consists of the following steps :
  - Pre-emphasis: same as PLP.
  - Windowing: same as PLP.
  - Mel-frequency analysis: a spectral analysis that divides the frequency spectrum into a number of bands (typically 20-40) that correspond to the mel scale, which is a perceptual scale of pitches that is linear at low frequencies and logarithmic at high frequencies. The mel scale is designed to approximate the frequency resolution of the human ear. The energy in each band is computed by applying a triangular filter bank to the spectrum.
  - Logarithmic compression: a compression of the mel-frequency energies by taking the logarithm, which reduces the dynamic range and enhances the contrast between high and low energies.
  - Discrete cosine transform (DCT): a conversion of the log mel-frequency energies into cepstral coefficients, which are the coefficients of the DCT of the energies. The DCT is a linear transformation that decorrelates the energies and reduces the dimensionality. The cepstral coefficients are called the MFCCs, and are usually truncated to a lower dimension (typically 12-14).

## Comparison

- PLP and MFCC are