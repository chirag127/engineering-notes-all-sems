# Speech Distortion Measures

Speech distortion measures are quantitative methods to evaluate the quality and intelligibility of speech signals that have been affected by noise, hearing loss, or processing algorithms. Speech distortion measures can be classified into two main categories: signal-based and perceptual-based.

- Signal-based measures compare the original speech signal with the distorted speech signal using mathematical operations such as correlation, distance, or error. Signal-based measures are easy to compute and do not require human listeners, but they may not reflect the subjective perception of speech quality or intelligibility. Some examples of signal-based measures are:

  - Signal-to-noise ratio (SNR): the ratio of the power of the speech signal to the power of the noise signal. A higher SNR indicates a lower level of noise and a better speech quality.
  - Segmental SNR: the SNR computed for short segments of speech, usually 10-20 ms. This measure can capture the local variations of noise and speech levels and can be weighted by the importance of each segment for speech intelligibility.
  - Log spectral distance (LSD): the average of the squared differences between the log spectra of the original and distorted speech signals. A lower LSD indicates a higher spectral similarity and a better speech quality.
  - Itakura-Saito (IS) distance: a measure of the distortion between two autoregressive models of speech signals, based on the Kullback-Leibler divergence. A lower IS distance indicates a higher model similarity and a better speech quality.
  - Cepstral distance: the average of the squared differences between the cepstra of the original and distorted speech signals. A lower cepstral distance indicates a higher cepstral similarity and a better speech quality.

- Perceptual-based measures use human listeners to rate the quality or intelligibility of speech signals using subjective scales or objective tests. Perceptual-based measures are more reliable and valid than signal-based measures, but they are more time-consuming and expensive to conduct. Some examples of perceptual-based measures are:

  - Mean opinion score (MOS): a subjective rating of the overall quality of speech signals on a scale from 1 (bad) to 5 (excellent). MOS can be obtained by asking listeners to rate speech samples or by using standardized methods such as PESQ or POLQA.
  - Speech intelligibility index (SII): an objective measure of the proportion of speech information that is audible to a listener with a given hearing loss. SII can be computed by estimating the audibility of speech in different frequency bands and weighting them by their importance for speech intelligibility.
  - Speech reception threshold (SRT): an objective measure of the lowest SNR at which a listener can understand 50% of speech signals. SRT can be measured by presenting speech signals with varying levels of noise and asking listeners to repeat or identify them.
  - Word recognition score (WRS): an objective measure of the percentage of speech signals that a listener can correctly identify. WRS can be measured by presenting speech signals with a fixed level of noise and asking listeners to repeat or identify them.