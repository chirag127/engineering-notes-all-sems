### Review Of Digital Signal Processing Concepts for Speech Processing

- Speech processing is the study of how speech signals are acquired, manipulated, stored, transferred and outputted.
- Speech signals are usually processed in a digital representation, so speech processing can be regarded as a special case of digital signal processing (DSP), applied to speech signals.
- DSP is the theory, design and implementation of numerical procedures for processing discrete representation of signals.
- DSP techniques can be used to help solve various speech communication problems, such as speech enhancement, speech coding, speech synthesis, speech recognition, speaker recognition, speech translation, etc.
- Some basic concepts and algorithms of DSP for speech processing are:

  - Sampling and quantization: converting continuous-time analog signals to discrete-time digital signals by taking samples at regular intervals and assigning discrete values to each sample.
  - Discrete Fourier transform (DFT) and fast Fourier transform (FFT): transforming discrete-time signals from time domain to frequency domain or vice versa, by decomposing them into a sum of sinusoids of different frequencies.
  - Z-transform and inverse Z-transform: generalizing the DFT to handle signals of infinite length or with complex coefficients, by using complex variables in the frequency domain.
  - Linear time-invariant (LTI) systems: systems that process signals without changing their shape, frequency or phase, and that have the same response to the same input at any time.
  - Convolution and correlation: operations that measure the similarity or overlap between two signals, by sliding one signal over another and computing the sum of their products.
  - Impulse response and frequency response: characterizing the behavior of LTI systems by their response to a unit impulse or a sinusoid of a given frequency, respectively.
  - Filter design and implementation: designing and realizing LTI systems that modify the frequency spectrum of a signal, by attenuating or amplifying certain frequency components.
  - Windowing and spectral analysis: applying a finite-length window function to a signal to reduce spectral leakage and improve frequency resolution, and using the DFT or FFT to estimate the power spectrum or the spectrogram of the signal.
  - Short-time Fourier transform (STFT) and wavelet transform: extending the DFT or FFT to handle non-stationary signals, by dividing them into short segments and applying a window function and a frequency transform to each segment.
  - Linear prediction and cepstral analysis: modeling the speech signal as the output of a linear filter driven by a source signal, and using the coefficients of the filter or the logarithm of its frequency response to represent the spectral envelope of the speech signal.