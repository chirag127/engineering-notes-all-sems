### Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log spectrum of the signal.
- Cepstral distance is often used in speech recognition and speaker verification systems to compare the input speech with the reference templates or models.
- A simple cepstral distance measure is the Euclidean distance between the cepstral vectors of two speech frames, which can be computed as:

```
d(x,y) = sqrt(sum((x_i - y_i)^2))
```

where x and y are the cepstral vectors of the two frames, and i is the index of the cepstral coefficient.

- However, a simple cepstral distance measure may not be optimal for speech recognition and speaker verification, because it does not take into account the different importance and variability of the cepstral coefficients.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to the cepstral coefficients according to some criteria, such as the inverse variance, the log-index, or the perceptual relevance of the coefficients.
- A weighted cepstral distance measure can be computed as:

```
d_w(x,y) = sqrt(sum(w_i * (x_i - y_i)^2))
```

where w_i is the weight for the i-th cepstral coefficient.

- A weighted cepstral distance measure can improve the performance of speech recognition and speaker verification systems by reducing the influence of noise, channel distortion, and speaker variability on the cepstral distance.
- Some examples of weighted cepstral distance measures are:

  - Furui's weighted cepstral distance measure, which uses the inverse of the intratalker variance of the cepstral coefficients as the weights .
  - Zheng and Wu's log-index weighted cepstral distance measure, which uses the logarithm of the index of the cepstral coefficients as the weights.
  - Perceptually weighted cepstral distance measure, which uses the weights derived from the human auditory system or the mel-frequency scale.

- Filtering is a process of modifying the speech signal or its spectrum to enhance or suppress some features or components, such as noise, pitch, formants, or harmonics.
- Filtering can be applied to the speech signal in the time domain or the frequency domain, using various techniques, such as low-pass, high-pass, band-pass, or band-stop filters, linear prediction, cepstral smoothing, or spectral subtraction.
- Filtering can improve the quality and intelligibility of the speech signal, as well as the accuracy and robustness of the speech recognition and speaker verification systems, by removing or reducing the unwanted or irrelevant components of the speech signal.