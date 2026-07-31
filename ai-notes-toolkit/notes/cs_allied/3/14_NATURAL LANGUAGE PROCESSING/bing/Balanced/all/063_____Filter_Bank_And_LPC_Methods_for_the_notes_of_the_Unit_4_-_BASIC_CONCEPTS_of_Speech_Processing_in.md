# Filter Bank and LPC Methods for Speech Processing

## Filter Bank Method

- A filter bank is a set of band-pass filters that divide the input signal into different frequency bands.
- Filter bank features are derived from the energy or power spectrum of the signal, which is obtained by applying a Fourier transform to the signal or its windowed segments.
- Filter bank features are often used for speech recognition, as they capture the spectral envelope of the speech signal, which is related to the vocal tract shape and the phonetic content of the speech.
- A common filter bank feature is the mel-frequency cepstrum (MFC), which is based on the mel-scale, a perceptual scale of pitches that is roughly linear below 1 kHz and logarithmic above 1 kHz.
- The MFC feature extraction process consists of the following steps:
  - Pre-emphasis: Apply a high-pass filter to the signal to boost the high-frequency components and reduce the effect of noise.
  - Framing: Divide the signal into short segments or frames, typically 20-40 ms long, with some overlap between adjacent frames.
  - Windowing: Multiply each frame by a window function, such as a Hamming window, to reduce the discontinuities at the edges of the frame.
  - Fourier transform: Compute the magnitude or power spectrum of each frame using a discrete Fourier transform (DFT) or a fast Fourier transform (FFT).
  - Mel filter bank: Apply a set of triangular filters that are spaced according to the mel-scale to the spectrum, and compute the sum of the energy or power within each filter.
  - Logarithm: Take the logarithm of the filter bank outputs to compress the dynamic range and mimic the human perception of loudness.
  - Discrete cosine transform (DCT): Apply a DCT to the log filter bank outputs to decorrelate them and reduce the dimensionality. The resulting coefficients are called the mel-frequency cepstral coefficients (MFCCs).
  - Delta and delta-delta: Optionally, compute the first and second derivatives of the MFCCs to capture the dynamic information of the speech signal.

## LPC Method

- Linear predictive coding (LPC) is a method of speech analysis and synthesis that models the speech signal as a linear combination of past samples, plus a prediction error or residual.
- LPC features are derived from the coefficients of a linear predictor, which is a filter that estimates the current sample based on the previous samples.
- LPC features are also used for speech recognition, as they capture the spectral envelope of the speech signal, which is related to the vocal tract shape and the phonetic content of the speech.
- The LPC feature extraction process consists of the following steps:
  - Pre-emphasis: Apply a high-pass filter to the signal to boost the high-frequency components and reduce the effect of noise.
  - Framing and windowing: Divide the signal into short segments or frames, typically 20-40 ms long, with some overlap between adjacent frames, and multiply each frame by a window function, such as a Hamming window.
  - Autocorrelation: Compute the autocorrelation function of each frame, which is the correlation of the signal with itself at different lags or delays.
  - Linear prediction: Solve the Yule-Walker equations to obtain the coefficients of the linear predictor, which minimize the mean squared error between the actual and predicted samples. The resulting coefficients are called the linear predictive coefficients (LPCs).
  - LPC to cepstrum: Optionally, convert the LPCs to cepstral coefficients by applying a recursion formula or a DCT. The resulting coefficients are called the LPC cepstral coefficients (LPCCs).
  - Delta and delta-delta: Optionally, compute the first and second derivatives of the LPCs or LPCCs to capture the dynamic information of the speech signal.