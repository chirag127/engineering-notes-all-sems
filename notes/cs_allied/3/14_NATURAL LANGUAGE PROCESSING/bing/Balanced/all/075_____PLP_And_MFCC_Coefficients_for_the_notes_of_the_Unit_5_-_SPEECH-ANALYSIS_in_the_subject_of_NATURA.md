# PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting meaningful information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction methods that can represent the speech signals in a compact and discriminative way, while capturing the relevant aspects of speech production and perception.
- PLP and MFCC are two popular feature extraction methods for speech analysis, based on different models of the human auditory system.
- PLP stands for Perceptual Linear Prediction, and MFCC stands for Mel Frequency Cepstral Coefficients.

## PLP

- PLP is a feature extraction method that mimics the human auditory system by applying a series of transformations to the speech signal, such as:

  - Pre-emphasis: a high-pass filtering that enhances the high-frequency components of the speech signal.
  - Windowing: a segmentation of the speech signal into short frames, usually 20-30 ms long, with some overlap between adjacent frames.
  - Critical band analysis: a spectral analysis that divides the frequency spectrum into a number of bands that correspond to the frequency resolution of the human ear.
  - Equal-loudness pre-emphasis: a weighting of the spectral components according to the human perception of loudness, which depends on the frequency and the sound level.
  - Intensity-loudness power law: a compression of the dynamic range of the spectral components according to the human perception of intensity, which is proportional to the logarithm of the sound power.
  - Autoregressive modeling: a parametric modeling of the spectral envelope using a linear prediction filter, which captures the resonant frequencies of the vocal tract.
  - Cepstral analysis: a conversion of the linear prediction coefficients into cepstral coefficients, which are more compact and robust to noise.

- PLP features are usually 10-15 cepstral coefficients, along with the energy and the first and second derivatives of the cepstral coefficients, which capture the temporal dynamics of the speech signal.

## MFCC

- MFCC is another feature extraction method that mimics the human auditory system by applying a similar series of transformations to the speech signal, such as:

  - Pre-emphasis: same as PLP.
  - Windowing: same as PLP.
  - Mel filter bank analysis: a spectral analysis that divides the frequency spectrum into a number of triangular filters that are spaced according to the mel scale, which approximates the human perception of pitch.
  - Logarithmic compression: a compression of the filter bank outputs using the logarithm function, which reduces the dynamic range and enhances the contrast between spectral peaks and valleys.
  - Discrete cosine transform: a conversion of the log filter bank outputs into cepstral coefficients, which decorrelate the spectral components and reduce the dimensionality.

- MFCC features are usually 12-20 cepstral coefficients, along with the energy and the first and second derivatives of the cepstral coefficients, which capture the temporal dynamics of the speech signal.

## Comparison

- PLP and MFCC are both widely used feature extraction methods for speech analysis, and they have some similarities and differences, such as:

  - Similarities: both methods are based on the human auditory system, and both methods use cepstral analysis to obtain compact and robust features.
  - Differences: PLP uses critical band analysis, equal-loudness pre-emphasis, intensity-loudness power law, and autoregressive modeling, while MFCC uses mel filter bank analysis, logarithmic compression, and discrete cosine transform.
  - Advantages and disadvantages: PLP is more accurate in modeling the spectral envelope and the human perception of loudness and intensity, while MFCC is more efficient in reducing the dimensionality and the correlation of the spectral components. PLP is more sensitive to noise and speaker variability, while MFCC is more robust to noise and speaker variability.

- The choice of the feature extraction method depends on the application and the data, and sometimes a combination of PLP and MFCC can be used to improve the performance of speech analysis.