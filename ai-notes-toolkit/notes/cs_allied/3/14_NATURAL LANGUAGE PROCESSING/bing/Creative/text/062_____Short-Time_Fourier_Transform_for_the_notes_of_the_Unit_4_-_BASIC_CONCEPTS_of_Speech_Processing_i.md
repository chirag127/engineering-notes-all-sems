### Short-Time Fourier Transform

- The short-time Fourier transform (STFT) is a technique for analyzing the frequency content of a signal over time.
- It involves dividing the signal into overlapping segments, applying a window function to each segment, and computing the discrete Fourier transform (DFT) of the windowed segments.
- The result is a two-dimensional representation of the signal, where each point in the time-frequency plane corresponds to the complex amplitude of a particular frequency component at a particular time instant.
- The STFT is useful for speech and audio processing because it can capture the non-stationary and time-varying characteristics of these signals, such as pitch, formants, harmonics, and noise.
- The STFT can also be used as a basis for various signal processing operations, such as filtering, enhancement, compression, recognition, and synthesis.
- The STFT has some limitations, such as the trade-off between time and frequency resolution, the leakage effect due to windowing, and the redundancy of the representation.

Some key concepts and formulas related to the STFT are:

- The window function $w[n]$ is a sequence of length $N$ that is multiplied with each segment of the signal. It should have desirable properties such as being symmetric, smooth, and having a narrow main lobe and low side lobes in the frequency domain. Some common window functions are rectangular, Hamming, Hanning, and Blackman.
- The hop size $H$ is the number of samples between the start of two consecutive segments. It determines the degree of overlap between the segments. A smaller hop size gives a finer time resolution but a larger computational cost. A larger hop size gives a coarser time resolution but a smaller computational cost. A typical choice is $H = N/2$, where $N$ is the window length.
- The analysis frame $x_m[n]$ is the $m$-th segment of the signal $x[n]$, obtained by multiplying the signal with the window function shifted by $mH$ samples, i.e., $x_m[n] = x[n+mH]w[n]$ for $n = 0, 1, \dots, N-1$.
- The STFT $X[m, k]$ is the DFT of the analysis frame $x_m[n]$, i.e., $X[m, k] = \sum_{n=0}^{N-1} x_m[n] e^{-j2\pi nk/N}$ for $k = 0, 1, \dots, N-1$. It can be interpreted as the complex amplitude of the $k$-th frequency bin at the $m$-th time frame.
- The magnitude spectrum $|X[m, k]|$ is the absolute value of the STFT, which indicates the strength of the $k$-th frequency component at the $m$-th time frame. It can be used to visualize the spectral content of the signal over time.
- The phase spectrum $\angle X[m, k]$ is the argument of the STFT, which indicates the phase of the $k$-th frequency component at the $m$-th time frame. It can be used to reconstruct the signal from the STFT using the inverse DFT (IDFT).
- The inverse STFT $x[n]$ is the signal reconstructed from the STFT using the IDFT and the overlap-add method, i.e., $x[n] = \sum_{m=-\infty}^{\infty} x_m[n-mH] = \frac{1}{N} \sum_{m=-\infty}^{\infty} \sum_{k=0}^{N-1} X[m, k] e^{j2\pi nk/N}$ for $n = 0, 1, \dots, L-1$, where $L$ is the length of the signal. The inverse STFT is exact if the window function satisfies the constant overlap-add (COLA) condition, i.e., $\sum_{m=-\infty}^{\infty} w[n-mH] = 1$ for all $n$.