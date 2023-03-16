# Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance is often used in speech recognition and speaker recognition systems to compare the input speech with the reference templates or models.
- A simple cepstral distance measure is the Euclidean distance between the cepstral vectors of two speech frames, but this may not be optimal for speech recognition because it does not account for the different importance and variability of the cepstral coefficients.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to the cepstral coefficients according to some criteria, such as the inverse variance, the log-index, or the perceptual relevance of the coefficients.
- A weighted cepstral distance measure can improve the performance of speech recognition systems by reducing the mismatch between the input speech and the reference templates or models, and by enhancing the discriminative power of the cepstral features.
- A weighted cepstral distance measure can be computed as follows:

  - Let x and y be two cepstral vectors of dimension N, and w be a weight vector of dimension N.
  - The weighted cepstral distance between x and y is given by:

    - d(x, y) = sqrt(sum(w_i * (x_i - y_i)^2) for i = 1 to N)

  - The weight vector w can be determined by different methods, such as:

    - Inverse variance weighting: w_i = 1 / var(x_i) or w_i = 1 / var(y_i), where var(x_i) or var(y_i) is the variance of the i-th cepstral coefficient across the training data or the reference data.
    - Log-index weighting: w_i = log(i), where i is the index of the cepstral coefficient, assuming that the lower-index coefficients are more important and less variable than the higher-index coefficients.
    - Perceptual weighting: w_i = a * e^(-b * i), where a and b are constants that control the shape of the exponential decay function, assuming that the lower-index coefficients are more perceptually relevant and less affected by noise than the higher-index coefficients.

- Filtering is a process of modifying the speech signal or the cepstral coefficients to reduce the effects of noise, channel distortion, or speaker variability, and to enhance the features that are relevant for speech recognition or speaker recognition.
- Filtering can be applied in different domains, such as the time domain, the frequency domain, or the cepstral domain, and can use different techniques, such as linear filtering, nonlinear filtering, or adaptive filtering.
- Some examples of filtering methods for speech analysis are:

  - Pre-emphasis: a high-pass filtering of the speech signal in the time domain to boost the high-frequency components and to compensate for the spectral tilt caused by the vocal tract.
  - Mel-frequency cepstral coefficients (MFCCs): a nonlinear filtering of the speech signal in the frequency domain to convert the linear spectrum into a mel-scale spectrum that mimics the human auditory system, and then applying a discrete cosine transform to obtain the cepstral coefficients.
  - Cepstral mean normalization (CMN): a linear filtering of the cepstral coefficients in the cepstral domain to subtract the mean of the cepstral coefficients from each cepstral vector, to reduce the effects of channel distortion or speaker variability.
  - Cepstral mean and variance normalization (CMVN): a linear filtering of the cepstral coefficients in the cepstral domain to subtract the mean and divide by the standard deviation of the cepstral coefficients from each cepstral vector, to reduce the effects of channel distortion or speaker variability and to normalize the dynamic range of the cepstral features.
  - Cepstral liftering: a nonlinear filtering of the cepstral coefficients in the cepstral domain to multiply each cepstral coefficient by a lifter function, such as a cosine function or a Hamming window, to emphasize or de-emphasize certain cepstral coefficients according to their importance or variability.