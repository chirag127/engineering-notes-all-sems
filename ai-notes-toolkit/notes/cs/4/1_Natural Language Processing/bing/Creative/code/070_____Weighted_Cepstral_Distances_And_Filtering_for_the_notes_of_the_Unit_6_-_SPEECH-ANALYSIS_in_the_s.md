# Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform (DCT) to the log-magnitude spectrum of the signal.
- Cepstral distance can be used for speech recognition, speaker recognition, speech enhancement, and speech synthesis applications.
- A simple cepstral distance measure is the Euclidean distance between the cepstral coefficients of two signals, but this may not be optimal for speech processing because it does not account for the different importance and variability of different cepstral coefficients.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to different cepstral coefficients according to some criterion, such as the inverse variance of the coefficients, the logarithm of the indices, or the perceptual relevance of the coefficients.
- A weighted cepstral distance measure can improve the performance of speech recognition and speaker recognition systems by reducing the effects of noise, channel distortion, and speaker variability on the cepstral coefficients.
- A weighted cepstral distance measure can also be used for speech enhancement and speech synthesis by filtering the cepstral coefficients of a noisy or synthetic signal with the weights derived from a clean or natural signal, respectively.
- Some examples of weighted cepstral distance measures are:

  - Furui's weighted cepstral distance measure, which uses the inverse of the intratalker variance of the cepstral coefficients as the weights .
  - Zheng and Wu's log-index weighted cepstral distance measure, which uses the logarithm of the corresponding indices as the weights .
  - Perceptually weighted cepstral distance measure, which uses the weights derived from a perceptual model of human hearing, such as the Bark scale or the mel scale .