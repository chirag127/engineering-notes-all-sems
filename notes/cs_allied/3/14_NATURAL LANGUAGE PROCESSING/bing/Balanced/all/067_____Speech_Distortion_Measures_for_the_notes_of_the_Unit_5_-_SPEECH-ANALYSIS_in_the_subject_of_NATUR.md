# Speech Distortion Measures

- Speech distortion measures are quantitative methods to evaluate the quality and intelligibility of speech signals that have been affected by noise, hearing loss, or processing algorithms.
- Speech distortion measures can be classified into two main categories: signal-based and perception-based.
- Signal-based measures compare the original and distorted speech signals in terms of their spectral, temporal, or cepstral features, and compute a numerical score that reflects the degree of similarity or dissimilarity between them.
- Perception-based measures estimate how well a human listener can understand or identify the distorted speech, either by using subjective ratings or by using objective models that simulate the auditory system.
- Some examples of signal-based measures are:
  - Mean squared error (MSE): the average of the squared differences between the original and distorted speech samples.
  - Log spectral distance (LSD): the average of the absolute differences between the logarithms of the original and distorted speech spectra.
  - Itakura-Saito (IS) distance: a measure of the divergence between two probability distributions of speech spectra, based on the Kullback-Leibler divergence.
  - Segmental signal-to-noise ratio (SNRseg): the average of the local SNRs computed over short segments of speech.
  - Cepstral distance (CD): the average of the Euclidean distances between the original and distorted speech cepstra.
- Some examples of perception-based measures are:
  - Mean opinion score (MOS): the average of the subjective ratings given by human listeners on a scale from 1 (bad) to 5 (excellent).
  - Speech intelligibility index (SII): a measure of the proportion of speech information that is audible to a listener with a given hearing loss, based on the audibility of speech bands in different frequency regions.
  - Speech transmission index (STI): a measure of the modulation transfer function of a communication channel, which reflects how well the temporal fluctuations of speech are preserved.
  - Perceptual evaluation of speech quality (PESQ): an objective model that predicts the MOS of distorted speech, based on the comparison of the internal representations of the original and distorted speech in the auditory system.