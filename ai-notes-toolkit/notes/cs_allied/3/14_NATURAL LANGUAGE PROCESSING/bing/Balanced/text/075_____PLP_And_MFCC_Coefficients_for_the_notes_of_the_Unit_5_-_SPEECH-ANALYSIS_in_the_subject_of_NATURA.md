### PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction, which is the computation of a set of parameters that represent the characteristics of the speech signal.
- Feature extraction methods aim to reduce the dimensionality of the speech signal, remove the irrelevant or redundant information, and enhance the discriminative power of the features.
- Some of the most widely used feature extraction methods for speech analysis are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC).

#### Perceptual Linear Prediction (PLP)

- PLP is a feature extraction method that mimics the human auditory system, by applying a series of transformations to the speech signal that simulate the perceptual effects of the ear.
- PLP consists of the following steps :
  - Pre-emphasis: a high-pass filtering that enhances the high-frequency components of the speech signal and reduces the effect of noise.
  - Framing and windowing: dividing the speech signal into short segments (frames) of 20-30 ms, and applying a window function (such as Hamming) to each frame to smooth the edges and reduce spectral leakage.
  - Critical-band analysis: applying a filter bank that divides the frequency spectrum into a number of bands that correspond to the critical bands of the human ear. The critical bands are non-uniformly spaced, with higher resolution at lower frequencies and lower resolution at higher frequencies.
  - Intensity-loudness conversion: applying a non-linear transformation that converts the intensity (power) of each critical band into loudness (perceived sound level). The loudness is proportional to the logarithm of the intensity, and is scaled by a factor that depends on the frequency.
  - Equal-loudness pre-emphasis: applying a weighting function that compensates for the variation of the loudness sensitivity of the human ear across different frequencies. The weighting function boosts the low-frequency components and attenuates the high-frequency components of the loudness spectrum.
  - Autoregressive modeling: fitting an autoregressive (AR) model to the loudness spectrum, which estimates the spectral envelope of the speech signal. The AR model is a linear predictor that expresses the current value of the signal as a linear combination of its past values. The coefficients of the AR model are the PLP features, which capture the spectral shape of the speech signal.
  - Cepstral analysis: applying a discrete cosine transform (DCT) to the PLP features, which decorrelates them and reduces their dimensionality. The DCT coefficients are called the PLP cepstrum, which are the final features used for speech analysis.

#### Mel Frequency Cepstral Coefficients (MFCC)

- MFCC is another feature extraction method that mimics the human auditory system, by applying a similar series of transformations to the speech signal as PLP, but with some differences.
- MFCC consists of the following steps  :
  - Pre-emphasis: same as PLP.
  - Framing and windowing: same as PLP.
  - Mel-filter bank analysis: applying a filter bank that divides the frequency spectrum into a number of bands that correspond to the mel scale. The mel scale is a perceptual scale that relates the frequency to the pitch of the sound, and is linear at low frequencies and logarithmic at high frequencies. The filter bank has triangular filters that are uniformly spaced on the mel scale, and overlap with each other.
  - Logarithmic compression: applying a logarithmic function to the output of the filter bank, which converts the power of each band into a measure of loudness. The logarithmic function also enhances the dynamic range of the features and reduces the effect of noise.
  - Cepstral analysis: applying a discrete cosine transform (DCT) to the log filter bank output, which decorrelates the features and reduces their dimensionality. The DCT coefficients are called the MFCC, which are the final features used for speech analysis.

#### Comparison of PLP and MFCC

- Both PLP and MFCC are based on the principle of cepstral analysis, which is the extraction of the spectral envelope of the speech signal by applying a logarithmic function and a DCT.
- Both PLP and MFCC aim to model the human auditory system, by applying a filter bank that mimics the frequency resolution of the ear, and a non-linear transformation that mimics the loudness