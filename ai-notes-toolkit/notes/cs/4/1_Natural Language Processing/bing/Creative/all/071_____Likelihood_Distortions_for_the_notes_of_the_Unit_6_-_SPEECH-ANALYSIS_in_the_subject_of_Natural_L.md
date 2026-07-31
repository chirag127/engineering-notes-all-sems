# Likelihood Distortions for Speech Analysis

- Likelihood distortions are measures of the similarity or dissimilarity between two short-time spectra of speech signals, which are often used in speech recognition systems to compare the input speech with the stored templates or models .
- Likelihood distortions can be classified into two categories: linear and nonlinear.
- Linear distortions are based on the Euclidean distance between the spectral vectors, such as the cepstral distortion (CEP) or the log spectral distortion (LSD).
- Nonlinear distortions are based on the ratio of the spectral vectors, such as the likelihood ratio (LR), the log likelihood ratio (LLR), or the Itakura-Saito (IS) distortion.
- Nonlinear distortions are more robust to variations in the signal energy or gain, and can better model the human perception of speech than linear distortions.
- However, nonlinear distortions are also more sensitive to noise and spectral mismatch, and can be computationally more complex than linear distortions.
- Some perceptually based distortions have been proposed to overcome the limitations of the conventional likelihood distortions, such as the weighted likelihood ratio (WLR) or the weighted slope metric (WSM) distortion.
- These distortions incorporate some aspects of the human auditory system, such as the critical band frequency warping, the loudness scaling, or the spectral slope weighting.
- These distortions aim to improve the recognition performance by reducing the mismatch between the speech spectra and the perceptual spectra.
- A comparative study of several likelihood distortions for speech recognition showed that the LLR and WSM distortions gave the highest recognition accuracy, while the IS distortion gave the lowest score .
- The study also showed that the addition of suprasegmental energy information helped the recognition performance, while the use of gain and absolute loudness degraded the performance .
- The study also showed that the bark-scale frequency warping did not perform as well as its unwarped counterpart for the highly bandlimited telephone data base .
- The study also showed that the WLR distortion did not perform as well as its unweighted counterpart .