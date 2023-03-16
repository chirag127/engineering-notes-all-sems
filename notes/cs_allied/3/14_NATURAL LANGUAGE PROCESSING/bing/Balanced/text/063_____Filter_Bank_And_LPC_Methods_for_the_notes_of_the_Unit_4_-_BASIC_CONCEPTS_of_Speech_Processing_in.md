### Filter Bank and LPC Methods

- Filter bank and LPC methods are two techniques for extracting features from speech signals for speech processing applications such as speech recognition, speech synthesis, and speech coding.
- Filter bank methods divide the speech signal into frequency bands and compute the energy or power spectrum of each band. The most common filter bank method is the mel-frequency cepstral coefficients (MFCC) method, which uses a set of triangular filters spaced according to the mel scale, which approximates the human perception of frequency. The MFCC method consists of the following steps:
  - Pre-emphasize the speech signal to boost the high-frequency components and reduce the effect of noise.
  - Apply a Hamming window to the speech signal to reduce the spectral leakage and smooth the edges of the signal.
  - Perform a fast Fourier transform (FFT) on the windowed signal to obtain the magnitude spectrum.
  - Apply the mel filter bank to the magnitude spectrum and sum the energy in each filter.
  - Take the logarithm of the filter bank energies to mimic the human perception of loudness.
  - Perform a discrete cosine transform (DCT) on the log filter bank energies to obtain the cepstral coefficients, which are the features used for speech processing.
- LPC methods model the speech signal as the output of a linear filter driven by an excitation signal. The linear filter represents the vocal tract, which shapes the speech signal by resonating at certain frequencies called formants. The excitation signal represents the source of the speech, which can be either a periodic pulse train for voiced sounds or a random noise for unvoiced sounds. The LPC method consists of the following steps:
  - Estimate the coefficients of the linear filter by minimizing the prediction error, which is the difference between the actual speech signal and the predicted speech signal based on the past samples. This can be done by solving the Yule-Walker equations or using the Levinson-Durbin algorithm.
  - Apply the inverse of the linear filter to the speech signal to obtain the residual signal, which is the excitation signal.
  - Quantize the filter coefficients and the residual signal to reduce the bit rate for speech coding or transmission.
  - Synthesize the speech signal by reversing the process: use the residual signal as the source signal, use the filter coefficients to create a filter that represents the vocal tract, and run the source signal through the filter to obtain the speech signal.