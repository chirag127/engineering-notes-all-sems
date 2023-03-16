# Short-Time Fourier Transform

The Short-Time Fourier Transform (STFT) is a Fourier-related transform used to determine the sinusoidal frequency and phase content of local sections of a signal as it changes over time. It is a powerful general-purpose tool for audio signal processing.

- STFT is a sequence of Fourier transforms of a windowed signal.
- STFT provides the time-localized frequency information for situations in which frequency components of a signal vary over time.
- The standard Fourier transform provides the frequency information averaged over the entire signal time interval.
- In practice, the procedure for computing STFTs is to divide a longer time signal into shorter segments of equal length and then compute the Fourier transform separately for each shorter segment.
- The magnitude squared of the STFT is known as the spectrogram time-frequency representation of the signal.