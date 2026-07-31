# PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction, which is the computation of a set of parameters that represent the characteristics of the speech signal.
- Feature extraction methods should be robust, efficient, and capture the relevant information from the speech signal.
- Some of the popular feature extraction methods for speech analysis are PLP and MFCC.

## PLP (Perceptual Linear Prediction)

- PLP is a feature extraction method that mimics the human auditory system, by applying a psychoacoustic model to the speech signal.
- PLP consists of the following steps :
  - Pre-emphasis: a high-pass filter that enhances the high-frequency components of the speech signal.
  - Windowing: dividing the speech signal into short frames (typically 20-30 ms) and applying a window function (such as Hamming) to each frame.
  - FFT (Fast Fourier Transform): computing the spectrum of each frame, which represents the frequency-domain information of the speech signal.
  - Critical-band analysis: applying a filter bank that divides the spectrum into frequency bands that correspond to the human auditory system. The filter bank is based on the Bark scale, which is a psychoacoustic scale that measures the perceived pitch of a sound.
  - Equal-loudness pre-emphasis: applying a weighting function that emphasizes the frequency bands that are more sensitive to the human ear, and attenuates the ones that are less sensitive.
  - Intensity-loudness power law: applying a non-linear transformation that converts the intensity (energy) of each frequency band into loudness (perceived sound level).
  - Autoregressive modeling: fitting a linear prediction model to the loudness spectrum, which captures the spectral envelope of the speech signal. The model coefficients are called the PLP coefficients, and they are the final features extracted by PLP.
- PLP features are usually augmented with the energy of each frame, and the first and second derivatives of the PLP coefficients, to capture the temporal dynamics of the speech signal.
- PLP features are suitable for speech recognition, speaker recognition, and speech synthesis applications.

## MFCC (Mel Frequency Cepstral Coefficients)

- MFCC is another feature extraction method that mimics the human auditory system, by applying a different psychoacoustic model to the speech signal.
- MFCC consists of the following steps :
  - Pre-emphasis: same as PLP.
  - Windowing: same as PLP.
  - FFT: same as PLP.
  - Mel-filter bank: applying a filter bank that divides the spectrum into frequency bands that correspond to the human auditory system. The filter bank is based on the Mel scale, which is another psychoacoustic scale that measures the perceived pitch of a sound. The Mel scale is more linear than the Bark scale at low frequencies, and more logarithmic at high frequencies.
  - Logarithmic compression: applying a logarithmic function to the energy of each frequency band, which reduces the dynamic range of the speech signal and approximates the human perception of loudness.
  - DCT (Discrete Cosine Transform): computing the cepstrum of the log-energy spectrum, which represents the frequency-domain information of the spectral envelope. The cepstrum is the spectrum of the log-spectrum, and it can be interpreted as the rate of change of the spectrum. The DCT coefficients are called the MFCC coefficients, and they are the final features extracted by MFCC.
- MFCC features are usually augmented with the energy of each frame, and the first and second derivatives of the MFCC coefficients, to capture the temporal dynamics of the speech signal.
- MFCC features are widely used for speech recognition, speaker recognition, speech synthesis, and speech emotion recognition applications.

## Comparison of PLP and MFCC

- PLP and MFCC are both feature extraction methods that mimic the human auditory system, but they differ in the psychoacoustic models and the transformations they apply to the speech signal.
- PLP uses the Bark scale, the equal-loudness pre-emphasis, the intensity-loudness power law, and the autoregressive modeling, while MFCC uses the Mel scale, the logarithmic compression, and the DCT.
- PLP and MFCC have different properties and advantages, depending on the application and the speech signal characteristics.
- Some studies have compared the performance of PLP and MFCC for different speech analysis tasks,