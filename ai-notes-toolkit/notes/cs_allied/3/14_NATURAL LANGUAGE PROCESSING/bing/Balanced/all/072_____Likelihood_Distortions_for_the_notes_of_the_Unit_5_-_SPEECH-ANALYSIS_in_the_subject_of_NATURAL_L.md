# Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the similarity or dissimilarity between two short-time spectra of speech signals, usually obtained by applying a window function to the speech waveform and taking the Fourier transform.
- Likelihood distortions are used to compare speech frames in speech recognition systems, such as dynamic time warping (DTW) or hidden Markov models (HMMs), to find the best match between a speech input and a reference template or model.
- Likelihood distortions can be derived from different criteria, such as minimizing the mean square error, maximizing the likelihood, or incorporating perceptual factors.
- Some common likelihood distortion measures are:
  - Itakura-Saito (IS) distortion: based on the Kullback-Leibler divergence between two probability density functions, assuming a Gaussian distribution with diagonal covariance matrix. It is invariant to scaling and additive constants, but sensitive to spectral shape.
  - Log likelihood ratio (LLR) distortion: based on the logarithm of the ratio of two probability density functions, assuming a Gaussian distribution with diagonal covariance matrix. It is invariant to scaling, but sensitive to additive constants and spectral shape.
  - Likelihood ratio (LR) distortion: based on the ratio of two probability density functions, assuming a Gaussian distribution with diagonal covariance matrix. It is sensitive to scaling, additive constants, and spectral shape.
  - Cepstral (CEP) distortion: based on the Euclidean distance between two cepstral vectors, obtained by taking the inverse Fourier transform of the log spectrum. It is sensitive to scaling and additive constants, but less sensitive to spectral shape.
  - Weighted likelihood ratio (WLR) distortion: based on the LLR distortion, but with a weighting function applied to the frequency axis to emphasize the perceptually important regions, such as the formants. It is invariant to scaling, but sensitive to additive constants and spectral shape, with a perceptual bias.
  - Weighted slope metric (WSM) distortion: based on the Euclidean distance between two slope vectors, obtained by taking the first derivative of the log spectrum. It is invariant to scaling and additive constants, but sensitive to spectral shape, with a perceptual bias.

- The performance of different likelihood distortion measures depends on various factors, such as the speech database, the recognition task, the feature extraction method, the window size and shape, the frequency warping, the energy normalization, and the loudness scaling.
- According to a comparative study by Lee and Rose , some general observations are:
  - The LLR and WSM distortion measures gave the highest recognition accuracy, while the IS distortion measure gave the lowest score.
  - The addition of suprasegmental energy information helped the recognition performance, while the use of gain and absolute loudness degraded the performance.
  - Bark-scale frequency warping did not perform as well as its unwarped counterpart for the highly bandlimited telephone data base they tested.
  - The WLR distortion measure did not perform as well as its unweighted counterpart.