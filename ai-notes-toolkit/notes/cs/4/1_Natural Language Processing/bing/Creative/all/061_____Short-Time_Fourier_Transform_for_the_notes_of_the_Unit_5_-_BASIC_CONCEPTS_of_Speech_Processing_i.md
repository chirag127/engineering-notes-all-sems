# Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time   .
- It is based on dividing the signal into overlapping segments, applying a window function to each segment, and computing the discrete Fourier transform (DFT) of the windowed segments   .
- The STFT produces a complex-valued matrix that represents the magnitude and phase of the signal's spectrum at each time and frequency bin  .
- The STFT is useful for speech and audio processing because it captures the non-stationary and time-varying nature of speech signals   .
- The STFT can be used for various applications, such as spectral analysis, filtering, enhancement, modification, synthesis, and recognition of speech signals   .

## Algorithm

- The STFT algorithm can be summarized as follows   :

  - Given a signal x(n) of length N, choose a window function w(n) of length M, and a hop size H.
  - For each frame index k = 0, 1, ..., K-1, where K = floor((N-M)/H) + 1, do the following:
    - Extract a segment of the signal x(n) from n = kH to n = kH + M - 1, and multiply it with the window function w(n) to obtain x_k(n) = x(n)w(n).
    - Compute the DFT of x_k(n) using a fast Fourier transform (FFT) algorithm, and store the result in a column vector X_k of length L, where L is the DFT size (usually a power of 2 greater than or equal to M). X_k(l) = sum_{n=0}^{M-1} x_k(n) exp(-j2pi ln/L) for l = 0, 1, ..., L-1.
    - Append X_k to the STFT matrix X as the k-th column. X = [X_0, X_1, ..., X_{K-1}].
  - Return the STFT matrix X as the output.

## Example

- The following figure shows an example of the STFT of a speech signal sampled at 16 kHz, using a Hamming window of length 256 samples, a hop size of 128 samples, and a DFT size of 512 samples .

![STFT of a speech signal](https://ccrma.stanford.edu/~jos/sasp/STFT_Speech_Signal.png)

- The horizontal axis represents time in seconds, the vertical axis represents frequency in Hz, and the color represents the magnitude of the STFT in dB.
- The STFT reveals the harmonic structure of the voiced segments, the noise-like characteristics of the unvoiced segments, and the transitions between them. It also shows the variations in the fundamental frequency and the formant frequencies over time.