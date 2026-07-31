### Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique to analyze the frequency content of a signal that varies over time  .
- The STFT divides the signal into overlapping segments, applies a window function to each segment, and computes the discrete Fourier transform (DFT) of the windowed segments  .
- The STFT produces a complex-valued matrix that represents the magnitude and phase of the signal in the time-frequency domain  .
- The STFT is widely used for speech and audio processing, such as speech enhancement, speech recognition, source separation, and audio coding  .
- The STFT has some limitations, such as the trade-off between time and frequency resolution, and the assumption of stationarity within each segment .

#### Algorithm

- Given a signal x(n) of length N, choose a window function w(n) of length M, and a hop size H.
- For each segment index k, compute the windowed segment x_k(n) = x(n + kH)w(n) for n = 0, 1, ..., M-1.
- For each segment index k, compute the DFT of the windowed segment X_k(m) = sum_{n=0}^{M-1} x_k(n) exp(-j2pi nm/M) for m = 0, 1, ..., M-1.
- Store the DFT coefficients X_k(m) in a matrix X, such that X(k, m) = X_k(m).
- The matrix X is the STFT of the signal x(n). The rows of X correspond to different segments (time indices), and the columns of X correspond to different frequency bins (frequency indices).
- To reconstruct the signal from the STFT, apply the inverse DFT to each segment, and overlap-add the windowed segments with the same hop size H.