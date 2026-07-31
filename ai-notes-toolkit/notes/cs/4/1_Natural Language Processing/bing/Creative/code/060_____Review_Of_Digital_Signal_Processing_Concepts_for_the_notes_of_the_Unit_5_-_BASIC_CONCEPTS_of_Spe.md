# Review Of Digital Signal Processing Concepts for the notes of the Unit 5 - BASIC CONCEPTS of Speech Processing in the subject of Natural Language Processing

- Speech processing is the study of how speech signals are acquired, manipulated, stored, transferred and output.
- Speech signals are usually processed in a digital representation, so speech processing can be regarded as a special case of digital signal processing (DSP), applied to speech signals.
- DSP is concerned with both a discrete signal representation, and with the theory, design and implementation of numerical procedures for processing discrete representation.
- Some of the basic concepts and algorithms of DSP that are relevant for speech processing are:

  - Sampling and quantization: the process of converting a continuous-time signal into a discrete-time signal by taking samples at regular intervals and assigning them numerical values.
  - Fourier transform: a mathematical tool that decomposes a signal into its frequency components, revealing the spectral characteristics of the signal.
  - Z-transform: a generalization of the Fourier transform that allows the analysis and design of discrete-time systems in the frequency domain.
  - Linear systems: systems that satisfy the properties of superposition and homogeneity, meaning that the output of the system is a linear combination of the inputs.
  - Convolution: a mathematical operation that describes the output of a linear system in terms of the input and the impulse response of the system.
  - Filters: devices or algorithms that modify the frequency content of a signal, either by attenuating or enhancing certain frequency components.
  - Discrete Fourier transform (DFT): a discrete version of the Fourier transform that computes the frequency spectrum of a finite-length signal.
  - Fast Fourier transform (FFT): an efficient algorithm for computing the DFT of a signal, reducing the computational complexity from O(N^2) to O(N log N), where N is the length of the signal.
  - Windowing: a technique that involves multiplying a signal by a window function, such as a rectangular, Hamming, or Hanning window, to reduce the spectral leakage and improve the frequency resolution of the DFT.
  - Short-time Fourier transform (STFT): a method of analyzing the frequency content of a signal as a function of time, by dividing the signal into short segments and applying the DFT to each segment.
  - Spectrogram: a graphical representation of the STFT, showing the magnitude or power of the frequency components as a function of time and frequency.
  - Linear prediction: a method of estimating the future values of a signal based on a linear combination of its past values, using an autoregressive model.
  - Cepstrum: a measure of the periodicity of a signal, obtained by applying the inverse Fourier transform to the logarithm of the magnitude spectrum of the signal.
  - Mel-frequency cepstrum (MFC): a representation of the spectral envelope of a signal, obtained by applying a mel-scale filter bank to the magnitude spectrum, taking the logarithm, and applying the discrete cosine transform (DCT).
  - Mel-frequency cepstral coefficients (MFCC): the coefficients of the MFC, which are widely used as features for speech recognition and speaker identification.