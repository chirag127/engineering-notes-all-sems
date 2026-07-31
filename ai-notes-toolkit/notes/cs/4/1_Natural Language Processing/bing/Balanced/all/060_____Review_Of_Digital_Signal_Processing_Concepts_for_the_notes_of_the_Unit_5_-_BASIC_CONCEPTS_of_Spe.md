# Review Of Digital Signal Processing Concepts for the notes of the Unit 5 - BASIC CONCEPTS of Speech Processing in the subject of Natural Language Processing

- Speech processing is the study of how speech signals are acquired, manipulated, stored, transferred and output.
- Speech signals are usually processed in a digital representation, so speech processing can be regarded as a special case of digital signal processing (DSP), applied to speech signals.
- DSP is concerned with both a discrete signal representation, and with the theory, design and implementation of numerical procedures for processing discrete representation.
- Some of the basic concepts and algorithms of DSP that are relevant for speech processing are:

  - Sampling and quantization: the process of converting a continuous-time signal into a discrete-time signal by taking samples at regular intervals and assigning them numerical values.
  - Fourier transform and spectrum: the process of decomposing a signal into its frequency components and representing them as a function of frequency.
  - Z-transform and filter: the process of transforming a discrete-time signal into a complex function of a complex variable and applying linear operations to modify its frequency response.
  - Discrete cosine transform and cepstrum: the process of transforming a signal into a sum of cosine functions and applying a logarithm and an inverse Fourier transform to obtain a representation of its spectral envelope.
  - Linear prediction and LPC coefficients: the process of estimating the current sample of a signal as a linear combination of its past samples and obtaining a set of parameters that characterize its spectral shape.
  - Windowing and framing: the process of dividing a signal into short segments and applying a weighting function to reduce the discontinuities at the edges.
  - Short-time Fourier transform and spectrogram: the process of applying the Fourier transform to each frame of a signal and obtaining a time-frequency representation of its energy distribution.
  - Mel-frequency cepstral coefficients and MFCCs: the process of applying a filter bank that mimics the human auditory system to the spectrum of a signal and obtaining a set of features that are widely used for speech recognition and synthesis.

- Some of the applications of DSP in speech processing are:

  - Speech synthesis: the process of generating artificial speech signals from text or other symbolic inputs.
  - Speech recognition: the process of converting speech signals into text or other symbolic outputs.
  - Speech enhancement: the process of improving the quality of speech signals by reducing noise, reverberation, distortion or other degradations.
  - Speech coding: the process of compressing speech signals for efficient transmission or storage.
  - Speech analysis: the process of extracting information from speech signals such as speaker identity, emotion, language, accent, etc..