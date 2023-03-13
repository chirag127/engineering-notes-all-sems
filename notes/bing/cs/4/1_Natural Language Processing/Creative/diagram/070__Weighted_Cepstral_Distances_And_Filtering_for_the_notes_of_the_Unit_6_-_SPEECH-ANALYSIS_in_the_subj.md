The following diagram illustrates the basic architecture of a weighted cepstral distance and filtering system for speech analysis:

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Speech Input  +---->+  Cepstral      +---->+  Weighting     +---->+  Distance      |
|                |     |  Coefficients  |     |  Filter        |     |  Measure       |
|                |     |                |     |                |     |                |
+----------------+     +----------------+     +----------------+     +----------------+

```

The system consists of four main components:

- Speech Input: The input signal that contains the speech to be analyzed.
- Cepstral Coefficients: The representation of the speech signal in the cepstral domain, which is obtained by applying a discrete cosine transform (DCT) to the logarithm of the power spectrum of the signal. The cepstral coefficients capture the spectral envelope of the speech signal, which reflects the vocal tract characteristics of the speaker.
- Weighting Filter: The filter that applies a perceptual or statistical weighting to the cepstral coefficients, in order to emphasize or de-emphasize certain frequency bands or coefficients. The weighting filter can be based on the inverse variance of the coefficients, the auditory masking theory, or the cepstral difference of different models of the speech signal.
- Distance Measure: The measure that computes the similarity or dissimilarity between two sets of cepstral coefficients, usually by using a Euclidean or Mahalanobis distance. The distance measure can be used for speech recognition, speaker identification, or speech quality assessment.