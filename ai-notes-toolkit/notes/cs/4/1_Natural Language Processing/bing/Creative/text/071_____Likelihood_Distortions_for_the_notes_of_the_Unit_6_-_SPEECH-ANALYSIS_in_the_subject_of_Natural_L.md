### Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the spectral distance or similarity between two short-time spectra, usually derived from the log-likelihood function of a statistical model of speech.
- Likelihood distortions are often used to compare speech signals in speech recognition, speech synthesis, speech enhancement, and speech coding applications.
- Some common likelihood distortion measures are:
  - Itakura-Saito (IS) distortion: based on the Kullback-Leibler divergence between two autoregressive models of speech, which assumes Gaussian white noise and minimum phase spectra.
  - Log likelihood ratio (LLR) distortion: based on the log-likelihood ratio test between two Gaussian models of speech, which assumes equal covariance matrices and arbitrary phase spectra.
  - Likelihood ratio (LR) distortion: based on the likelihood ratio test between two Gaussian models of speech, which assumes unequal covariance matrices and arbitrary phase spectra.
  - Cepstral (CEP) distortion: based on the Euclidean distance between the cepstral coefficients of two speech signals, which assumes a linear relationship between the log-spectra and the cepstra.
  - Weighted likelihood ratio (WLR) distortion: based on the LLR distortion with a perceptual weighting function applied to the spectra, which accounts for the human auditory system's sensitivity to different frequency bands.
  - Weighted slope metric (WSM) distortion: based on the slope difference between the spectra of two speech signals, with a perceptual weighting function applied to the slope values, which accounts for the human auditory system's sensitivity to spectral shape and formant transitions.
- The performance of different likelihood distortion measures depends on various factors, such as the speech database, the speech task, the speech model, the feature extraction, the frequency warping, the energy normalization, and the dynamic time warping algorithm.
- According to a comparative study by Lee and Rose , some general observations are:
  - The LLR and WSM distortions gave the highest recognition accuracy, while the IS distortion gave the lowest score.
  - The addition of suprasegmental energy information helped the recognition performance, while the use of gain and absolute loudness degraded the performance.
  - Bark-scale frequency warping did not perform as well as its unwarped counterpart for the highly bandlimited telephone data base they tested.
  - The WLR distortion did not perform as well as its unweighted counterpart.