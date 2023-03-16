# PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting meaningful information from speech signals, such as the speaker identity, the spoken language, the emotion, the content, etc.
- Speech analysis requires feature extraction methods that can represent the speech signals in a compact and discriminative way, while capturing the relevant aspects of the speech production and perception.
- PLP and MFCC are two popular feature extraction methods for speech analysis, based on different models of the human auditory system.
- PLP stands for Perceptual Linear Prediction, and MFCC stands for Mel-Frequency Cepstral Coefficients.

## PLP

- PLP is a feature extraction method that mimics the human auditory system by applying a series of transformations to the speech signal, such as:

  - Pre-emphasis: a high-pass filtering that enhances the high-frequency components of the speech signal.
  - Windowing: a segmentation of the speech signal into short frames (typically 20-30 ms) with some overlap (typically 50%).
  - Critical-band analysis: a spectral analysis that divides the frequency spectrum into a number of bands (typically 15-20) that correspond to the frequency resolution of the human ear.
  - Equal-loudness pre-emphasis: a weighting of the spectral bands according to the human perception of loudness, which is more sensitive to mid-frequency sounds than to low- or high-frequency sounds.
  - Intensity-loudness power law: a compression of the spectral bands according to the human perception of intensity, which is logarithmic rather than linear.
  - Autoregressive modeling: a parametric modeling of the spectral envelope using linear prediction, which results in a set of coefficients (typically 10-14) that capture the main features of the speech signal.

- PLP features are obtained by applying a discrete cosine transform (DCT) to the autoregressive coefficients, which reduces the dimensionality and decorrelates the features.

## MFCC

- MFCC is another feature extraction method that mimics the human auditory system by applying a similar series of transformations to the speech signal, such as:

  - Pre-emphasis: same as PLP.
  - Windowing: same as PLP.
  - Mel-frequency analysis: a spectral analysis that divides the frequency spectrum into a number of bands (typically 20-40) that correspond to the mel scale, which is a perceptual scale of pitches that is linear at low frequencies and logarithmic at high frequencies.
  - Logarithmic compression: a compression of the spectral bands using the logarithm function, which approximates the human perception of intensity.
  - Cepstral analysis: a parametric modeling of the spectral envelope using the cepstrum, which is the inverse Fourier transform of the logarithm of the spectrum, and results in a set of coefficients (typically 10-20) that capture the main features of the speech signal.

- MFCC features are obtained by applying a discrete cosine transform (DCT) to the cepstral coefficients, which reduces the dimensionality and decorrelates the features.

## Comparison

- PLP and MFCC are both widely used feature extraction methods for speech analysis, and have similar performance in many applications, such as speech recognition, speaker recognition, language identification, etc.
- PLP and MFCC have some differences in the way they model the human auditory system, such as:

  - PLP uses critical-band analysis, while MFCC uses mel-frequency analysis, which have different frequency resolutions and scales.
  - PLP uses equal-loudness pre-emphasis, while MFCC does not, which affects the weighting of the spectral bands.
  - PLP uses intensity-loudness power law, while MFCC uses logarithmic compression, which have different nonlinearities and dynamic ranges.
  - PLP uses autoregressive modeling, while MFCC uses cepstral analysis, which have different mathematical formulations and interpretations.

- PLP and MFCC can be combined or modified to improve their performance or suitability for specific tasks, such as:

  - PLP-RASTA: a variant of PLP that applies a band-pass filtering to the spectral bands to remove the effects of noise and channel variations.
  - MFCC-Delta: a variant of MFCC that appends the first- and second-order derivatives of the MFCC features to capture the dynamic information of the speech signal.
  - PLP-MFCC: a hybrid method that combines the PLP and MFCC features to obtain a more robust and comprehensive representation of the speech signal.