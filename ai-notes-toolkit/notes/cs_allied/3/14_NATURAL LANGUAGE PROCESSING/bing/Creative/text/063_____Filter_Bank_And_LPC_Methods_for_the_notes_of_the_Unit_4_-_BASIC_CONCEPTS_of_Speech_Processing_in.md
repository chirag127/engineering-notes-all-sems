### Filter Bank and LPC Methods for Speech Processing

- Filter bank and LPC methods are two common techniques for extracting features from speech signals for speech recognition or synthesis applications.
- Filter bank methods divide the speech signal into frequency bands and compute the energy or power spectrum of each band. The most popular filter bank method is the mel-frequency cepstral coefficients (MFCC) method, which uses a set of triangular filters that are spaced according to the mel scale, which approximates the human perception of frequency. The MFCC method consists of the following steps:
  - Pre-emphasize the speech signal by applying a high-pass filter to reduce the effect of the vocal tract and enhance the high-frequency components.
  - Divide the speech signal into overlapping frames of 20-40 ms duration, and apply a window function (such as Hamming) to each frame to reduce the discontinuities at the edges.
  - Compute the discrete Fourier transform (DFT) of each frame and obtain the magnitude spectrum.
  - Apply the mel filter bank to the magnitude spectrum and sum the energy in each filter.
  - Take the logarithm of the filter bank energies to mimic the human perception of loudness.
  - Apply the discrete cosine transform (DCT) to the log filter bank energies and retain the first few coefficients (typically 12-20) as the MFCC features. Optionally, append the energy of the frame and the first and second derivatives of the MFCC features to form a feature vector.
- LPC methods model the speech signal as the output of a linear filter driven by an excitation signal. The linear filter represents the vocal tract, and the excitation signal represents the glottal source or the noise source. The LPC method consists of the following steps:
  - Divide the speech signal into frames of 10-30 ms duration, and apply a window function to each frame.
  - Estimate the LPC coefficients of each frame by minimizing the mean squared error between the original signal and the predicted signal. This can be done by solving the Yule-Walker equations or using the Levinson-Durbin algorithm.
  - Use the LPC coefficients to obtain the frequency response of the filter, which corresponds to the formant frequencies of the speech signal.
  - Inverse filter the speech signal by passing it through the inverse of the LPC filter, and obtain the residual signal, which corresponds to the excitation signal.
  - Quantize the LPC coefficients and the residual signal using appropriate coding schemes, such as vector quantization or adaptive differential pulse code modulation (ADPCM).
  - To synthesize the speech signal, reverse the process by using the quantized LPC coefficients and the residual signal to generate the filter and the excitation signal, and pass the excitation signal through the filter.

- Filter bank and LPC methods have different advantages and disadvantages for speech processing. Some of the comparisons are :
  - Filter bank methods are more robust to noise and channel distortions, while LPC methods are more sensitive to these factors.
  - Filter bank methods require more computation and storage than LPC methods, especially for high-dimensional feature vectors.
  - Filter bank methods capture the spectral envelope of the speech signal, while LPC methods capture the spectral peaks of the speech signal.
  - Filter bank methods are more suitable for speaker-independent recognition, while LPC methods are more suitable for speaker-dependent recognition.
  - Filter bank methods are more compatible with hidden Markov models (HMMs), which are widely used for speech recognition, while LPC methods are more compatible with dynamic time warping (DTW), which is an older technique for speech recognition.