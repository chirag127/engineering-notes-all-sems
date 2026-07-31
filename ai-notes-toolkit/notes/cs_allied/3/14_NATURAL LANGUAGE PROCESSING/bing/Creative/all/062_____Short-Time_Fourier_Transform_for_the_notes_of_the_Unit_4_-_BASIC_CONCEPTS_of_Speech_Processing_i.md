# Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time.
- It is based on dividing the signal into overlapping segments, applying a window function to each segment, and computing the discrete Fourier transform (DFT) of the windowed segments.
- The STFT produces a two-dimensional representation of the signal, where the horizontal axis is time and the vertical axis is frequency.
- The STFT is useful for speech and audio processing because it captures the local variations of the spectrum, which reflect the changes in the sound source and the acoustic environment.
- The STFT can be used for various applications, such as filtering, enhancement, compression, recognition, synthesis, and modification of speech and audio signals.

## Algorithm

- The STFT algorithm can be summarized as follows :

  1. Choose a window function \(w[n]\) of length \(N\), such as a Hamming window or a Hann window.
  2. Choose a hop size \(H\), which is the number of samples between adjacent segments. A typical value is \(H = N/2\), which gives 50% overlap between segments.
  3. For each segment \(x[n]\) of the signal, multiply it with the window function \(w[n]\) to obtain the windowed segment \(x_w[n] = x[n]w[n]\).
  4. Compute the DFT of the windowed segment \(X_w[k] = \sum_{n=0}^{N-1} x_w[n] e^{-j2\pi kn/N}\), where \(k = 0, 1, ..., N-1\) is the frequency index.
  5. Store the magnitude \(|X_w[k]|\) and/or the phase \(\angle X_w[k]\) of the DFT as a column in a matrix \(S\), where the column index corresponds to the time index.
  6. Repeat steps 3-5 for all segments of the signal, shifting the window by \(H\) samples each time.
  7. Plot the matrix \(S\) as a spectrogram, where the color or intensity of each pixel represents the magnitude or the power of the DFT at a given time and frequency.

## Properties

- The STFT has some important properties that affect its performance and interpretation :

  - The window function \(w[n]\) determines the trade-off between the time resolution and the frequency resolution of the STFT. A longer window gives better frequency resolution but worse time resolution, and vice versa. A shorter window can capture fast changes in the spectrum, but it also introduces more spectral leakage and reduces the signal-to-noise ratio. A longer window can reduce the leakage and noise, but it also smears the spectral features over time.
  - The hop size \(H\) determines the amount of overlap between segments and the redundancy of the STFT. A larger hop size reduces the computational cost and the storage requirement of the STFT, but it also reduces the time resolution and the smoothness of the spectrogram. A smaller hop size increases the time resolution and the smoothness, but it also increases the computation and the storage.
  - The DFT size \(N\) determines the frequency resolution and the frequency range of the STFT. A larger DFT size gives finer frequency resolution and more frequency bins, but it also increases the computation and the storage. A smaller DFT size gives coarser frequency resolution and fewer frequency bins, but it also reduces the computation and the storage. The DFT size can be different from the window size, in which case zero-padding or truncation is applied to the windowed segments before computing the DFT. Zero-padding can improve the frequency resolution without affecting the time resolution, but it does not increase the information content of the signal. Truncation can reduce the computation and the storage without affecting the time resolution, but it can introduce aliasing and distortion in the frequency domain.