### Weighted Cepstral Distances And Filtering for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance can be used for speech recognition, speaker recognition, speech enhancement, and speech synthesis applications.
- A simple cepstral distance measure is the Euclidean distance between the cepstral coefficients of two speech frames, but this may not be optimal for capturing the perceptual differences between speech signals.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to the cepstral coefficients according to their importance or variability.
- One way to obtain the weights is to use the inverse of the variance of the cepstral coefficients, which reflects the degree of variation of each coefficient across different speech frames or speakers   .
- Another way to obtain the weights is to use the logarithm of the index of the cepstral coefficient, which reflects the frequency resolution of the cepstral coefficients .
- A weighted cepstral distance measure can improve the performance of speech recognition or speaker recognition systems by reducing the mismatch between the training and testing conditions or between different speakers.
- Filtering is a process of modifying the speech signal by applying a filter function to its spectrum or cepstrum, which can enhance or suppress certain frequency components or features of the signal.
- Filtering can be used for speech analysis to reduce the noise, improve the signal-to-noise ratio, or extract the vocal tract or excitation information from the speech signal.
- Filtering can be performed in the spectral domain or in the cepstral domain, depending on the type of filter function and the desired effect.
- Some examples of filtering techniques are:

  - Spectral subtraction: a method of noise reduction that subtracts an estimate of the noise spectrum from the noisy speech spectrum, resulting in a cleaner speech spectrum.
  - Cepstral liftering: a method of feature extraction that applies a window function to the cepstrum, resulting in a modified cepstrum that emphasizes or de-emphasizes certain cepstral coefficients.
  - Homomorphic filtering: a method of speech decomposition that applies a high-pass filter to the cepstrum, resulting in a separation of the vocal tract and excitation components of the speech signal.