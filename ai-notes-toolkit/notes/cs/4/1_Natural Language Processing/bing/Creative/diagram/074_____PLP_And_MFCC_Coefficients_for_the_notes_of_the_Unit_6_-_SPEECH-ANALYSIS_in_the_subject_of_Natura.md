### PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting useful information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction, which is the computation of a compact and informative representation of the speech signal, usually in the form of a vector of numerical values.
- Feature extraction methods aim to capture the salient characteristics of speech, such as the spectral envelope, the pitch, the energy, the formants, etc., while discarding the irrelevant or redundant information, such as the background noise, the channel distortion, the speaker's anatomy, etc.
- Feature extraction methods also try to mimic the human auditory system, which is the most efficient and robust speech analyzer, by applying perceptual weighting and scaling to the speech signal.
- Two of the most widely used feature extraction methods for speech analysis are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC).

#### Perceptual Linear Prediction (PLP)

- PLP is a feature extraction method that was proposed by Hermansky in 1990.
- PLP is based on the linear prediction (LP) analysis, which models the speech signal as the output of an all-pole filter driven by a source signal.
- PLP applies several perceptual transformations to the speech signal before performing the LP analysis, such as:

  - Pre-emphasis: a high-pass filtering that enhances the high-frequency components of the speech signal and compensates for the spectral tilt caused by the glottal source.
  - Critical-band analysis: a frequency analysis that divides the speech spectrum into several bands that correspond to the frequency resolution of the human ear.
  - Equal-loudness curve: a weighting function that adjusts the amplitude of each critical band according to the human perception of loudness at different frequencies.
  - Intensity-loudness power law: a non-linear compression that reduces the dynamic range of the speech signal and simulates the human perception of loudness as a power function of intensity.
  - Autocorrelation: a time-domain analysis that computes the correlation of the speech signal with itself at different lags, which reflects the periodicity and the spectral envelope of the signal.

- PLP then performs the LP analysis on the autocorrelation coefficients and obtains the LP coefficients, which are a set of parameters that describe the spectral envelope of the speech signal.
- PLP finally converts the LP coefficients into cepstral coefficients, which are a more compact and orthogonal representation of the spectral envelope, by applying a discrete cosine transform (DCT).
- PLP typically produces 10 to 14 cepstral coefficients per speech frame, which are used as the feature vector for speech analysis.

#### Mel Frequency Cepstral Coefficients (MFCC)

- MFCC is a feature extraction method that was proposed by Davis and Mermelstein in 1980.
- MFCC is based on the cepstral analysis, which is a technique that transforms the speech spectrum into the cepstrum domain, where the spectral envelope and the spectral details are separated.
- MFCC applies several perceptual transformations to the speech signal before performing the cepstral analysis, such as:

  - Pre-emphasis: same as in PLP.
  - Windowing: a segmentation of the speech signal into short frames of 20 to 40 ms, each multiplied by a window function, such as a Hamming window, to reduce the discontinuities at the frame boundaries.
  - Fast Fourier Transform (FFT): a frequency analysis that converts each speech frame into a spectrum of complex values, which represent the magnitude and the phase of each frequency component.
  - Mel filter bank: a frequency analysis that divides the speech spectrum into several triangular filters that are spaced according to the mel scale, which is a perceptual scale of pitches that approximates the human perception of frequency.
  - Logarithm: a non-linear compression that reduces the dynamic range of the speech signal and simulates the human perception of loudness as a logarithmic function of intensity.

- MFCC then performs the cepstral analysis on the log filter bank energies and obtains the cepstral coefficients, which are a set of parameters that describe the spectral envelope of the speech signal.
- MFCC typically produces 12 to 20 cepstral coefficients per speech frame, which are used as the feature vector for speech analysis.

#### Comparison of PLP and MFCC

- PLP and MFCC are both feature extraction methods that apply perceptual transformations to the speech signal and produce cepstral coefficients as the feature vector.
- PLP and MF