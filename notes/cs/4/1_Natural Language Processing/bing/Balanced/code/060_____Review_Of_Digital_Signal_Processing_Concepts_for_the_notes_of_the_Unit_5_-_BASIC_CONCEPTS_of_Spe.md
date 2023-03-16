### Review Of Digital Signal Processing Concepts for the notes of the Unit 5 - BASIC CONCEPTS of Speech Processing in the subject of Natural Language Processing

- Speech processing is the study of how speech signals are acquired, manipulated, stored, transferred and output.
- Speech signals are usually processed in a digital representation, so speech processing can be regarded as a special case of digital signal processing (DSP), applied to speech signals.
- DSP is concerned with both a discrete signal representation, and with the theory, design and implementation of numerical procedures for processing discrete representation.
- DSP techniques can be applied to help solve various speech communication problems, such as speech enhancement, speech coding, speech synthesis, speech recognition, speaker recognition, speech translation, etc.
- Some basic concepts and algorithms of DSP that are relevant for speech processing are:

  - Sampling and quantization: the process of converting a continuous-time analog signal into a discrete-time digital signal by taking samples at regular intervals and assigning them numerical values.
  - Fourier transform: a mathematical tool that decomposes a signal into its frequency components, revealing the spectral characteristics of the signal.
  - Z-transform: a generalization of the Fourier transform that allows the analysis of discrete-time signals and systems in the complex domain.
  - Linear systems: systems that satisfy the properties of superposition and homogeneity, meaning that the output of the system is a linear combination of the inputs.
  - Convolution: a mathematical operation that describes the output of a linear system in terms of the input and the impulse response of the system.
  - Filters: devices or algorithms that modify the frequency content of a signal, such as low-pass, high-pass, band-pass, band-stop, etc.
  - Discrete Fourier transform (DFT): a numerical approximation of the Fourier transform that operates on a finite number of samples of a signal.
  - Fast Fourier transform (FFT): a fast algorithm for computing the DFT of a signal, reducing the computational complexity from O(N^2) to O(N log N), where N is the number of samples.
  - Windowing: a technique that applies a weighting function to a signal before performing the DFT, in order to reduce the spectral leakage and improve the frequency resolution.
  - Short-time Fourier transform (STFT): a technique that divides a long signal into short segments and performs the DFT on each segment, resulting in a time-frequency representation of the signal.
  - Linear prediction: a technique that models a signal as a linear combination of its past samples, and estimates the coefficients of the linear predictor using the autocorrelation or the covariance method.
  - Cepstrum: a transform that applies the logarithm and the inverse Fourier transform to the spectrum of a signal, revealing the periodicity and the envelope of the signal.
  - Mel-frequency cepstrum (MFC): a feature extraction technique that applies the cepstrum to a spectrum that is warped according to the mel-scale, which mimics the human perception of frequency.
  - Hidden Markov models (HMMs): a statistical model that represents a signal as a sequence of states, each with a probability distribution over the observations, and a transition matrix that governs the state changes.
  - Dynamic time warping (DTW): a technique that aligns two signals by finding the optimal path that minimizes the distance between them, allowing for non-linear time distortions.
  - Vector quantization (VQ): a technique that compresses a signal by dividing the feature space into regions, each with a representative vector, and assigning each feature vector to the closest region.
  - Artificial neural networks (ANNs): a computational model that consists of a network of interconnected nodes, each with a nonlinear activation function, that can learn to approximate complex functions from data.
  - Deep learning: a branch of machine learning that uses multiple layers of ANNs to learn hierarchical representations of data, achieving state-of-the-art results in various speech processing tasks.