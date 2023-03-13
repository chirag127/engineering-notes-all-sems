### PLP And MFCC Coefficients

- PLP and MFCC are two popular methods for extracting features from speech signals for speech recognition and other applications.
- PLP stands for Perceptual Linear Prediction, and MFCC stands for Mel-Frequency Cepstral Coefficients.
- Both methods are based on the idea of mimicking the human auditory system, which is sensitive to different frequency bands and has a nonlinear perception of loudness and pitch.
- PLP and MFCC both involve the following steps:
  - Pre-emphasis: Applying a high-pass filter to the speech signal to boost the high-frequency components and reduce the effect of noise.
  - Framing: Dividing the speech signal into short segments or frames, typically 20-30 ms long, with some overlap between adjacent frames.
  - Windowing: Multiplying each frame by a window function, such as a Hamming window, to reduce the discontinuities at the frame boundaries and improve the frequency analysis.
  - Fourier transform: Computing the discrete Fourier transform (DFT) of each windowed frame to obtain the frequency spectrum.
  - Filter bank: Applying a set of filters to the frequency spectrum to obtain the energy in different frequency bands. The filters are usually triangular and spaced according to a perceptual scale, such as the Mel scale or the Bark scale.
  - Logarithm: Taking the logarithm of the filter bank energies to approximate the human perception of loudness.
  - Cepstrum: Computing the inverse DFT of the log filter bank energies to obtain the cepstral coefficients, which are a compact representation of the spectral envelope.
- The main difference between PLP and MFCC is in the filter bank and the cepstrum steps.
- PLP uses a filter bank based on the Bark scale, which is a psychoacoustic scale that divides the audible frequency range into 24 critical bands. PLP also applies an equal-loudness curve and a spectral smoothing operation to the filter bank energies to account for the human sensitivity to different frequencies and the masking effect of loud sounds. PLP then computes the cepstral coefficients using an autoregressive model, which is a linear prediction technique that estimates the current value of a signal based on its past values.
- MFCC uses a filter bank based on the Mel scale, which is a perceptual scale that relates the frequency to the pitch of a sound. MFCC does not apply any equal-loudness curve or spectral smoothing to the filter bank energies. MFCC computes the cepstral coefficients using the discrete cosine transform (DCT), which is a fast and efficient way to obtain the real-valued coefficients from the complex-valued DFT.
- PLP and MFCC have different advantages and disadvantages for speech analysis. PLP is more accurate in modeling the human auditory system and capturing the perceptual aspects of speech, but it is more computationally complex and sensitive to noise. MFCC is simpler and faster to compute and more robust to noise, but it may lose some information about the fine structure of the speech spectrum.