The following diagram illustrates the basic architecture of a PLP and MFCC coefficients extraction for speech analysis. The diagram is drawn using ASCII characters.

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Speech Input  +---->+  Pre-emphasis  +---->+  Framing and   +---->+  Windowing     |
|                |     |                |     |  Overlapping   |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
                                                                 |
                                                                 |
                                                                 v
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  FFT Spectrum  +---->+  Mel Filter    +---->+  Logarithm     +---->+  DCT           |
|                |     |  Bank          |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+
                                                                 |
                                                                 |
                                                                 v
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  MFCC          +---->+  Cepstral      +---->+  Liftering     +---->+  Delta and     |
|                |     |  Mean          |     |                |     |  Delta-Delta   |
+----------------+     |  Normalization |     +----------------+     |  Coefficients  |
                       |                |                           |                |
                       +----------------+                           +----------------+
                                                                 |
                                                                 |
                                                                 v
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  PLP           +---->+  Autocorrelation+---->+  LPC Analysis  +---->+  Cepstral      |
|                |     |                |     |                |     |  Transformation|
+----------------+     +----------------+     +----------------+     +----------------+
```

The diagram shows the following steps:

- Speech input: The raw speech signal is captured by a microphone or other device and converted into a digital waveform.
- Pre-emphasis: A high-pass filter is applied to the speech signal to boost the high-frequency components and reduce the low-frequency components. This helps to balance the spectrum and improve the signal-to-noise ratio.
- Framing and overlapping: The speech signal is divided into short segments or frames, typically 20-40 ms long, with some overlap between adjacent frames. This helps to capture the short-term characteristics of the speech signal and reduce the effects of discontinuities at the frame boundaries.
- Windowing: A window function, such as a Hamming window, is applied to each frame to smooth the edges and reduce spectral leakage. This helps to improve the frequency resolution and reduce the effects of noise and interference.
- FFT spectrum: A fast Fourier transform (FFT) is applied to each windowed frame to obtain the magnitude spectrum of the speech signal. This represents the frequency components and their amplitudes in each frame.
- Mel filter bank: A set of triangular filters, spaced according to the Mel scale, is applied to the FFT spectrum to obtain the Mel spectrum. The Mel scale is a perceptual scale that approximates the human auditory system's response to different frequencies. The Mel spectrum represents the energy in each Mel frequency band.
- Logarithm: A logarithm function is applied to the Mel spectrum to obtain the log Mel spectrum. This helps to compress the dynamic range and mimic the human perception of loudness.
- DCT: A discrete cosine transform (DCT) is applied to the log Mel spectrum to obtain the Mel frequency cepstral coefficients (MFCC). The DCT reduces the correlation between adjacent frequency bands and retains the most important information for speech recognition. The MFCC represent the spectral shape of the speech signal in a compact and robust way.
- Cepstral mean normalization: A normalization technique is applied to the MFCC to reduce the effects of channel and speaker variability. The mean of each MFCC is subtracted from the corresponding MFCC to obtain the normalized MFCC.
- Liftering: A liftering function, such as a sinusoidal function, is applied to the normalized MFCC to enhance the higher-order coefficients and reduce the lower-order coefficients. This helps to emphasize the spectral peaks and valleys that are important for speech recognition.
- Delta and delta-delta coefficients: The first and second derivatives of the normalized and lif