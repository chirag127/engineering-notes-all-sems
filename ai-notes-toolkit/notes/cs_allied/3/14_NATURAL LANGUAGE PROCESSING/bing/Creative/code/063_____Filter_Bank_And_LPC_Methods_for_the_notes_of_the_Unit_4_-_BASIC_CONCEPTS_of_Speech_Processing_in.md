# Filter Bank and LPC Methods for Speech Processing

## Filter Bank Method

- A filter bank is a set of band-pass filters that divide the input signal into different frequency bands.
- Filter bank features are derived from the energy or power spectrum of the signal, which is obtained by applying a Fourier transform to the signal or its windowed segments.
- Filter bank features are often used for speech recognition, as they capture the spectral envelope of the signal, which is related to the vocal tract shape and the phonetic content of the speech.
- A common filter bank feature is the mel-frequency cepstrum (MFC), which is based on the mel-scale, a perceptual scale of pitches that is roughly linear below 1 kHz and logarithmic above 1 kHz.
- The MFC feature extraction process consists of the following steps:
  - Pre-emphasis: Apply a high-pass filter to the signal to boost the high-frequency components and reduce the effect of noise.
  - Framing: Divide the signal into overlapping frames of fixed length, typically 20-30 ms.
  - Windowing: Multiply each frame by a window function, such as a Hamming window, to reduce the spectral leakage and discontinuities at the frame boundaries.
  - Fourier transform: Compute the discrete Fourier transform (DFT) of each windowed frame to obtain the magnitude spectrum.
  - Mel filter bank: Apply a set of triangular filters to the magnitude spectrum, where the filters are spaced according to the mel-scale. The number of filters is usually 20-40.
  - Logarithm: Take the logarithm of the filter bank energies to mimic the human perception of loudness and to compress the dynamic range.
  - Discrete cosine transform (DCT): Apply a DCT to the log filter bank energies to obtain the cepstral coefficients, which are the MFC features. The number of coefficients is usually 12-16.
  - Delta and delta-delta: Optionally, compute the first and second derivatives of the MFC features to capture the temporal dynamics of the speech signal.

## LPC Method

- Linear predictive coding (LPC) is a method of speech analysis and synthesis that models the speech signal as a linear combination of past samples, plus a prediction error or residual.
- LPC features are derived from the coefficients of a linear predictor, which is a filter that estimates the current sample based on the previous samples.
- LPC features are also used for speech recognition, as they capture the spectral envelope of the signal, which is related to the vocal tract shape and the phonetic content of the speech.
- The LPC feature extraction process consists of the following steps:
  - Pre-emphasis: Apply a high-pass filter to the signal to boost the high-frequency components and reduce the effect of noise.
  - Framing: Divide the signal into overlapping frames of fixed length, typically 20-30 ms.
  - Windowing: Multiply each frame by a window function, such as a Hamming window, to reduce the spectral leakage and discontinuities at the frame boundaries.
  - Linear prediction: For each frame, find the optimal linear predictor coefficients that minimize the mean squared error between the actual and predicted samples. The number of coefficients is usually 10-14.
  - LPC coefficients: The linear predictor coefficients are the LPC features, which represent the inverse filter that removes the effect of the vocal tract from the speech signal.
  - Cepstrum: Optionally, compute the cepstrum of the LPC coefficients by applying a logarithm and an inverse Fourier transform. The cepstrum coefficients are also called LPC cepstrum features, which are more robust to noise and speaker variability than the LPC coefficients.

## Comparison

- Filter bank and LPC methods are both widely used for speech processing, but they have some advantages and disadvantages over each other.
- Filter bank method is more computationally efficient than LPC method, as it does not require solving a system of linear equations for each frame.
- Filter bank method is more flexible than LPC method, as it can use different filter shapes and scales to match the characteristics of the speech signal.
- LPC method is more compact than filter bank method, as it requires fewer coefficients to represent the spectral envelope of the signal.
- LPC method is more accurate than filter bank method, as it models the speech signal as a linear prediction rather than a Fourier approximation.
- LPC method is more suitable for speech synthesis than filter bank method, as it can generate a natural sounding speech signal by applying the inverse filter to a source signal.