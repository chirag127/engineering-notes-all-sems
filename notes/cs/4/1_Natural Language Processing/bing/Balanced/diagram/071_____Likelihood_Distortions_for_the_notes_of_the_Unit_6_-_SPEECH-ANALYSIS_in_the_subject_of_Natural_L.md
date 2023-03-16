### Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the spectral distance or similarity between two short-time spectra, usually derived from the log-likelihood function of a statistical model of speech.
- Likelihood distortions are often used to compare speech signals or features for speech recognition, enhancement, or synthesis applications.
- Some common likelihood distortion measures are:
  - Itakura-Saito (IS) distortion: based on the Kullback-Leibler divergence between two autoregressive models of speech spectra.
  - Log likelihood ratio (LLR) distortion: based on the log-likelihood ratio test between two Gaussian models of speech spectra.
  - Likelihood ratio (LR) distortion: based on the likelihood ratio test between two Gaussian models of speech spectra.
  - Cepstral (CEP) distortion: based on the Euclidean distance between two cepstral vectors derived from speech spectra.
  - Weighted likelihood ratio (WLR) distortion: based on the likelihood ratio test between two Gaussian models of speech spectra, weighted by a perceptual frequency scale (such as Bark or Mel scale).
  - Weighted slope metric (WSM) distortion: based on the slope difference between two speech spectra, weighted by a perceptual frequency scale.
- The performance of different likelihood distortion measures depends on the speech data, the feature extraction method, the frequency warping technique, and the suprasegmental information (such as energy or loudness) used.
- According to a comparative study by Lee and Rose , some general observations are:
  - The LLR and WSM distortion measures gave the highest recognition accuracy, while the IS distortion measure gave the lowest score.
  - The addition of suprasegmental energy information helped the recognition performance, while the use of gain and absolute loudness degraded the performance.
  - Bark-scale frequency warping did not perform as well as its unwarped counterpart for the highly bandlimited telephone data base tested.
  - The WLR distortion measure did not perform as well as its unweighted counterpart.