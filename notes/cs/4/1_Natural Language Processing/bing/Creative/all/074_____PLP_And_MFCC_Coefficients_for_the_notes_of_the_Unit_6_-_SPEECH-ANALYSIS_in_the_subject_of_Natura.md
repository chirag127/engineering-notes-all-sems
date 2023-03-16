# PLP and MFCC Coefficients for Speech Analysis

Speech analysis is the process of extracting meaningful information from speech signals, such as the speaker's identity, emotion, language, accent, etc. Speech analysis is an important task in natural language processing, speech recognition, speaker verification, speech synthesis, and other applications.

One of the main challenges in speech analysis is to find a suitable representation of the speech signal that captures the relevant information and discards the irrelevant variations. Speech signals are complex and noisy, and they depend on many factors, such as the speaker's vocal tract, the microphone, the environment, etc. Therefore, speech analysis requires feature extraction methods that can reduce the dimensionality and complexity of the speech signal, and enhance the discriminative and robust aspects of the speech information.

Two of the most widely used feature extraction methods for speech analysis are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC). These methods are based on the idea of modeling the speech signal as a source-filter system, where the source is the vocal cords and the filter is the vocal tract. The source produces a periodic or aperiodic excitation signal, and the filter shapes the spectrum of the excitation signal according to the position and shape of the articulators (tongue, lips, jaw, etc.). The resulting speech signal is the output of the filter.

PLP and MFCC methods aim to extract features that are related to the filter characteristics, which are assumed to be more informative and invariant than the source characteristics. PLP and MFCC methods also try to mimic the human auditory system, which is known to be sensitive to certain frequency bands and to perform nonlinear transformations of the speech signal.

The main steps of PLP and MFCC methods are:

- Preprocessing: The speech signal is divided into short frames (typically 20-30 ms) with some overlap (typically 50%). Each frame is multiplied by a window function (typically Hamming) to reduce the discontinuities at the edges.
- Spectrum estimation: The spectrum of each frame is estimated by applying the Discrete Fourier Transform (DFT) or the Fast Fourier Transform (FFT) to the windowed frame. The spectrum is usually represented by its magnitude or power, and sometimes by its phase.
- Frequency warping: The spectrum is warped to a perceptual frequency scale, such as the Bark scale for PLP or the Mel scale for MFCC. The warping is done by applying a filter bank that consists of overlapping triangular filters that cover the entire frequency range. The filter bank has more filters at lower frequencies and fewer filters at higher frequencies, reflecting the human auditory system's resolution. The output of the filter bank is the average power or energy of the spectrum within each filter.
- Cepstral analysis: The cepstral coefficients are obtained by applying the inverse DFT or the discrete cosine transform (DCT) to the log of the filter bank output. The cepstral coefficients are a compact representation of the spectrum that decorrelates the spectral features and reduces the dimensionality. The lower-order cepstral coefficients are more related to the filter characteristics, while the higher-order cepstral coefficients are more related to the source characteristics. Typically, only the lower-order cepstral coefficients are retained as features, and the higher-order cepstral coefficients are discarded or reduced by applying a liftering window.
- Postprocessing: The cepstral coefficients are further processed to enhance their robustness and discriminability. Some common postprocessing techniques are:

  - Mean normalization: The mean of the cepstral coefficients is subtracted from each frame to reduce the effect of the channel and the background noise.
  - Delta and delta-delta features: The first and second derivatives of the cepstral coefficients are computed and appended to the cepstral coefficients to capture the dynamic information of the speech signal.
  - Cepstral mean and variance normalization (CMVN): The mean and variance of the cepstral coefficients are normalized to a predefined value (typically zero and one) to reduce the effect of the speaker and the environment variability.
  - Feature selection: The most relevant and informative features are selected by applying some criterion, such as the Fisher score, the mutual information, or the principal component analysis (PCA).

The main differences between PLP and MFCC methods are:

- PLP uses the Bark scale as the perceptual frequency scale, while MFCC uses the Mel scale. The Bark scale is based on the critical bandwidths of the human auditory system, while the Mel scale is based on the perceived pitch of the human ear. The Bark scale has a finer resolution at lower frequencies and a coarser resolution at higher frequencies than the