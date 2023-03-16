# Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance is often used in speech recognition and speaker recognition systems to compare the input speech with the stored templates or models.
- However, cepstral distance is not optimal for speech recognition because it does not account for the different importance of different cepstral coefficients for speech perception and discrimination.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to different cepstral coefficients according to some criteria, such as the inverse variance of the coefficients, the logarithm of the indices, or the perceptual relevance of the coefficients.
- A weighted cepstral distance measure can improve the performance of speech recognition and speaker recognition systems by reducing the mismatch between the acoustic and perceptual features of speech.
- One example of a weighted cepstral distance measure is the log-index weighted cepstral distance measure, which is defined as follows:

$$
d_{LW}(\mathbf{c}_1,\mathbf{c}_2) = \sqrt{\sum_{k=1}^K \log(k) (c_{1k}-c_{2k})^2}
$$

where $\mathbf{c}_1$ and $\mathbf{c}_2$ are the cepstral vectors of two speech frames, and $K$ is the number of cepstral coefficients.

- Another example of a weighted cepstral distance measure is the inverse variance weighted cepstral distance measure, which is defined as follows:

$$
d_{IV}(\mathbf{c}_1,\mathbf{c}_2) = \sqrt{\sum_{k=1}^K \frac{1}{\sigma_k^2} (c_{1k}-c_{2k})^2}
$$

where $\sigma_k^2$ is the variance of the $k$-th cepstral coefficient across the training data.

- Filtering is a process of modifying the speech signal or its features to enhance or suppress certain aspects of the signal, such as noise, pitch, or formants.
- Filtering can be applied in the time domain, the frequency domain, or the cepstral domain, depending on the type and purpose of the filter.
- Some examples of filtering techniques for speech analysis are:

  - Pre-emphasis filter: a high-pass filter that boosts the high-frequency components of the speech signal to compensate for the attenuation caused by the vocal tract and the microphone. Pre-emphasis filter can improve the signal-to-noise ratio and the spectral resolution of the speech signal.
  - Mel-scale filter bank: a set of triangular filters that are spaced according to the mel scale, which is a perceptual scale of pitch. Mel-scale filter bank can reduce the dimensionality and redundancy of the speech spectrum and capture the salient features of speech perception.
  - Cepstral mean subtraction: a technique that subtracts the mean of the cepstral coefficients from each cepstral vector to remove the channel effects and the speaker-dependent characteristics of the speech signal. Cepstral mean subtraction can improve the robustness and the speaker-independence of the speech recognition system.
  - Cepstral liftering: a technique that applies a weighting function to the cepstral coefficients to emphasize or de-emphasize certain cepstral components. Cepstral liftering can enhance the spectral resolution and the perceptual relevance of the cepstral features.