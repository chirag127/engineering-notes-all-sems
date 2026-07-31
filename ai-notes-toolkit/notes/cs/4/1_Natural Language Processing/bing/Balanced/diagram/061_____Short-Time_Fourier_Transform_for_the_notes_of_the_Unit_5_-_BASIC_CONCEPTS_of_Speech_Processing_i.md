### Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time.
- It involves dividing the signal into overlapping segments, applying a window function to each segment, and computing the discrete Fourier transform (DFT) of the windowed segment.
- The result is a matrix of complex numbers that represent the magnitude and phase of the signal at each time and frequency bin.
- The STFT can be used for various applications in speech and audio processing, such as spectral analysis, filtering, enhancement, compression, recognition, and synthesis.
- The STFT has some limitations, such as the trade-off between time and frequency resolution, and the assumption of stationarity within each segment.
- The STFT can be visualized as a spectrogram, which is a plot of the magnitude or power of the STFT as a function of time and frequency.
- The STFT can be inverted to reconstruct the original signal by applying the inverse DFT to each segment and adding them with appropriate overlap.

#### Algorithm

- Given a signal x[n] of length N, and a window function w[n] of length M, the STFT is computed as follows:

1. Choose a hop size H, which is the number of samples between adjacent segments. Typically, H < M to ensure overlap.
2. For each segment index k = 0, 1, ..., K-1, where K = ceil((N-M)/H) + 1, extract the segment x_k[n] = x[n + kH] for n = 0, 1, ..., M-1.
3. Multiply the segment x_k[n] with the window function w[n] to obtain the windowed segment x_kw[n] = x_k[n]w[n].
4. Compute the DFT of the windowed segment X_k[m] = DFT{x_kw[n]} for m = 0, 1, ..., M-1.
5. Store the complex values X_k[m] in a matrix X[m, k] of size M x K.

- The inverse STFT is computed as follows:

1. For each segment index k = 0, 1, ..., K-1, compute the inverse DFT of the segment X_k[m] to obtain the windowed segment x_kw[n] = IDFT{X_k[m]} for n = 0, 1, ..., M-1.
2. Divide the windowed segment x_kw[n] by the window function w[n] to obtain the segment x_k[n] = x_kw[n]/w[n].
3. Add the segment x_k[n] to the reconstructed signal y[n] at the position n + kH, with appropriate overlap and normalization.
4. The reconstructed signal y[n] should be identical to the original signal x[n] up to numerical errors.