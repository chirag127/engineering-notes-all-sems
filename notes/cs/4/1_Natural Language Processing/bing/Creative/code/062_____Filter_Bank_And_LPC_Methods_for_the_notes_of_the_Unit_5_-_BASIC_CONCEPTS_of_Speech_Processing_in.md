### Filter Bank and LPC Methods for Speech Processing

Filter bank and LPC methods are two common techniques for extracting features from speech signals for speech recognition, synthesis, and analysis. They are based on different models of how speech is produced and perceived by humans.

#### Filter Bank Methods

- Filter bank methods are based on the idea that the human auditory system analyzes speech signals by decomposing them into frequency bands using a bank of filters.
- The most widely used filter bank method is the mel-frequency cepstral coefficients (MFCC) technique, which mimics the non-linear frequency resolution of the human ear by using a set of triangular filters spaced according to the mel scale, which is a perceptual scale of pitches.
- The MFCC technique consists of the following steps:
  - Pre-emphasize the speech signal by applying a high-pass filter to reduce the effect of low-frequency noise and enhance the high-frequency components.
  - Divide the speech signal into overlapping frames of 20-40 ms, and apply a window function (such as Hamming) to each frame to reduce the discontinuities at the edges.
  - Compute the discrete Fourier transform (DFT) of each frame and obtain the magnitude spectrum.
  - Apply the mel filter bank to the magnitude spectrum and sum the energy in each filter.
  - Take the logarithm of the filter bank energies to approximate the human perception of loudness.
  - Apply the discrete cosine transform (DCT) to the log filter bank energies and retain the first 12-13 coefficients as the MFCC features. Optionally, append the energy of the frame and the first and second derivatives of the MFCC features to form a feature vector.
- The MFCC features capture the spectral envelope of the speech signal, which reflects the vocal tract shape and the phonetic information. They are robust to noise and speaker variations, and have low computational cost.

#### LPC Methods

- LPC methods are based on the idea that speech is produced by a source-filter model, where the source is the vocal cords (which produce a periodic signal for voiced sounds or a random signal for unvoiced sounds) and the filter is the vocal tract (which shapes the source signal by resonating at certain frequencies called formants).
- The LPC technique estimates the coefficients of an all-pole filter that approximates the vocal tract filter, and the residual signal that represents the source signal. The LPC technique consists of the following steps:
  - Pre-emphasize the speech signal by applying a high-pass filter to reduce the effect of low-frequency noise and enhance the high-frequency components.
  - Divide the speech signal into overlapping frames of 20-40 ms, and apply a window function (such as Hamming) to each frame to reduce the discontinuities at the edges.
  - Compute the autocorrelation function of each frame and solve the Yule-Walker equations to obtain the LPC coefficients, which are the parameters of the all-pole filter.
  - Apply the inverse filter to the speech signal and obtain the residual signal, which is the output of the source signal.
  - Quantize the LPC coefficients and the residual signal using appropriate coding schemes, such as linear predictive coding (LPC) or code-excited linear prediction (CELP).
- The LPC features capture the spectral envelope of the speech signal, which reflects the vocal tract shape and the phonetic information. They are efficient for speech coding and synthesis, but less robust to noise and speaker variations than MFCC features .