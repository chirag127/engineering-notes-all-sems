### Filter Bank and LPC Methods

Filter bank and LPC methods are two techniques for extracting features from speech signals for speech processing applications such as speech recognition, speech synthesis, and speech coding.

#### Filter Bank Method

- A filter bank method divides the speech signal into several frequency bands using a set of bandpass filters, and computes the energy or power of each band as a feature.
- A common filter bank method is the mel-frequency cepstral coefficients (MFCC) method, which uses a set of triangular filters that are spaced according to the mel-scale, which approximates the human perception of frequency.
- The MFCC method consists of the following steps:
  - Pre-emphasize the speech signal to boost the high-frequency components and reduce the effect of noise.
  - Divide the speech signal into overlapping frames of fixed length, typically 20-30 ms.
  - Apply a window function, such as a Hamming window, to each frame to reduce the discontinuities at the edges.
  - Compute the discrete Fourier transform (DFT) of each frame to obtain the frequency spectrum.
  - Apply the mel-filter bank to the spectrum and sum the energy of each filter.
  - Take the logarithm of the filter bank energies to mimic the human perception of loudness.
  - Apply the discrete cosine transform (DCT) to the log filter bank energies to obtain the cepstral coefficients, which are the features for speech recognition.
  - Optionally, append the delta and delta-delta coefficients, which are the first and second derivatives of the cepstral coefficients, to capture the dynamic information of speech.
- The filter bank method has the advantages of being simple, robust, and efficient, and can capture the spectral envelope of speech, which is important for speech recognition.
- The filter bank method has the disadvantages of being sensitive to noise, speaker variability, and channel distortion, and may not capture the fine details of speech, such as the pitch and formants.

#### LPC Method

- A linear predictive coding (LPC) method models the speech signal as the output of a linear filter driven by an excitation signal, which can be either a periodic pulse train (for voiced speech) or a white noise (for unvoiced speech).
- The LPC method consists of the following steps:
  - Divide the speech signal into overlapping frames of fixed length, typically 10-20 ms.
  - Estimate the coefficients of the linear filter, which are called the LPC coefficients, using an autocorrelation method or a covariance method, which minimize the prediction error between the actual speech signal and the predicted signal.
  - Compute the LPC spectrum, which is the frequency response of the linear filter, and the LPC cepstrum, which is the inverse Fourier transform of the logarithm of the LPC spectrum.
  - Use the LPC coefficients, the LPC spectrum, or the LPC cepstrum as the features for speech processing.
  - Optionally, estimate the pitch and the gain of the excitation signal using a pitch detection algorithm and a normalization method, and use them as additional features.
- The LPC method has the advantages of being able to model the speech production mechanism, capture the formants and the pitch of speech, and compress the speech signal efficiently.
- The LPC method has the disadvantages of being complex, computationally intensive, and sensitive to noise and pitch variations.