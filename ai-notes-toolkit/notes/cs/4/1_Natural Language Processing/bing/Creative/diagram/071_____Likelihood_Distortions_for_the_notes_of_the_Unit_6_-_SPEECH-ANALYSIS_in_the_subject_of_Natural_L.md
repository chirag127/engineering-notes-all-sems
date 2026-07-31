### Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the spectral distance or dissimilarity between two short-time spectra, usually a reference spectrum and a test spectrum.
- Likelihood distortions are used to compare and align speech signals in speech recognition systems, such as dynamic time warping (DTW) based isolated word recognizers .
- There are several types of likelihood distortions, such as:
  - Itakura-Saito (IS) distortion: based on the Kullback-Leibler divergence between two probability density functions, assuming a Gaussian distribution with a diagonal covariance matrix .
  - Log likelihood ratio (LLR) distortion: based on the logarithm of the ratio of two probability density functions, assuming a Gaussian distribution with a full covariance matrix .
  - Likelihood ratio (LR) distortion: based on the ratio of two probability density functions, assuming a Gaussian distribution with a full covariance matrix .
  - Cepstral (CEP) distortion: based on the Euclidean distance between the cepstral coefficients of two spectra .
  - Weighted likelihood ratio (WLR) distortion: based on the LLR distortion with a perceptual weighting function applied to the frequency axis, to emphasize the importance of lower frequencies .
  - Weighted slope metric (WSM) distortion: based on the slope difference between two spectra, with a perceptual weighting function applied to the frequency axis, to emphasize the importance of lower frequencies .
- The choice of the likelihood distortion measure affects the performance of the speech recognition system. According to a comparative study by Furui and Sondhi , some of the findings are:
  - The LLR and WSM distortions gave the highest recognition accuracy, while the IS distortion gave the lowest score .
  - The addition of suprasegmental energy information helped the recognition performance, while the use of gain and absolute loudness degraded the performance .
  - Bark-scale frequency warping did not perform as well as its unwarped counterpart, at least for the highly bandlimited telephone data base tested .
  - The WLR distortion did not perform as well as its unweighted counterpart .