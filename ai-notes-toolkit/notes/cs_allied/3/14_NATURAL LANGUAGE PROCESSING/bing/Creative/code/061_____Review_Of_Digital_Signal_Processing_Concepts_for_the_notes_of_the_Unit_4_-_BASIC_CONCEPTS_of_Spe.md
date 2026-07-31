# Review Of Digital Signal Processing Concepts for the notes of the Unit 4 - BASIC CONCEPTS of Speech Processing in the subject of NATURAL LANGUAGE PROCESSING

- Speech processing is the study of how speech signals are acquired, manipulated, stored, transferred and output.
- Speech signals are usually processed in a digital representation, so speech processing can be regarded as a special case of digital signal processing (DSP), applied to speech signals.
- DSP is the theory, design and implementation of numerical procedures for processing discrete representation of signals.
- DSP techniques can be used to help solve various speech communication problems, such as speech enhancement, speech coding, speech synthesis and speech recognition.
- Some basic concepts and algorithms of DSP that are relevant for speech processing are:

  - Sampling and quantization: the process of converting a continuous-time signal into a discrete-time signal by taking samples at regular intervals and assigning them numerical values.
  - Fourier transform: a mathematical tool that decomposes a signal into its frequency components, revealing the spectral characteristics of the signal.
  - Z-transform: a generalization of the Fourier transform that allows the analysis and design of discrete-time systems, such as filters and linear prediction models.
  - Discrete Fourier transform (DFT) and fast Fourier transform (FFT): numerical algorithms that compute the Fourier transform of a finite-length discrete-time signal, enabling efficient spectral analysis and manipulation of signals.
  - Filter design: the process of designing a system that modifies the frequency response of a signal, such as removing noise, enhancing certain features, or compressing the signal.
  - Windowing: the technique of multiplying a signal by a window function, such as a rectangular, Hamming, or Hanning window, to reduce the spectral leakage and improve the resolution of the DFT.
  - Short-time Fourier transform (STFT): a method of computing the Fourier transform of a signal over short segments, resulting in a time-frequency representation of the signal that captures its local spectral variations.
  - Linear prediction: a method of modeling a signal as a linear combination of its past samples, using an autoregressive (AR) model, which can be used for speech analysis and synthesis.
  - Cepstral analysis: a technique of transforming a signal into its cepstrum, which is the inverse Fourier transform of the logarithm of the magnitude spectrum of the signal, which can be used for speech feature extraction and recognition.