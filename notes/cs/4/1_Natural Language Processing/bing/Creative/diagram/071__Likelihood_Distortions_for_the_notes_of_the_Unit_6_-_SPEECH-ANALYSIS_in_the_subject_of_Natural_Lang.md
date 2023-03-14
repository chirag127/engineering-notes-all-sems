Likelihood distortions are measures of the spectral distance or similarity between two short-time spectra, usually derived from the log-likelihood ratio of two probability density functions. They are commonly used in speech recognition to compare the input speech signal with the stored templates or models of the words or phonemes. Different likelihood distortions have different properties and effects on the performance of speech recognition systems.

One of the most widely used likelihood distortions is the Itakura-Saito (IS) distortion measure, which is based on the assumption that the speech spectra are modeled by autoregressive (AR) processes. The IS distortion measure is defined as:

D_IS(X,Y) = log (P_X(Y) / P_Y(Y)) - 1

where X and Y are the AR coefficients of the two spectra, and P_X(Y) and P_Y(Y) are the AR spectral densities.

Another likelihood distortion is the log likelihood ratio (LLR) distortion measure, which is based on the assumption that the speech spectra are modeled by Gaussian processes. The LLR distortion measure is defined as:

D_LLR(X,Y) = log (P_X(Y) / P_Y(Y))

where X and Y are the mean vectors and covariance matrices of the two spectra, and P_X(Y) and P_Y(Y) are the Gaussian spectral densities.

Other likelihood distortions include the likelihood ratio (LR) distortion measure, which is the exponential of the LLR distortion measure, the cepstral (CEP) distortion measure, which is based on the Euclidean distance between the cepstral coefficients of the two spectra, and the weighted likelihood ratio (WLR) and the weighted slope metric (WSM) distortion measures, which are perceptually based distortions that incorporate the human auditory system characteristics.

The following diagram illustrates the basic architecture of a speech recognition system using likelihood distortions:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|  Input Speech  +----->+  Feature       +----->+  Template or   |
|                |      |  Extraction    |      |  Model         |
+----------------+      +----------------+      +----------------+
                                    |                   |
                                    |                   |
                                    |                   |
                                    v                   v
                               +----------------+      +----------------+
                               |                |      |                |
                               |  Spectral      |      |  Spectral      |
                               |  Representation|      |  Representation|
                               |                |      |                |
                               +----------------+      +----------------+
                                    |                   |
                                    |                   |
                                    |                   |
                                    v                   v
                               +----------------+
                               |                |
                               |  Likelihood    |
                               |  Distortion    |
                               |                |
                               +----------------+
                                    |
                                    |
                                    |
                                    v
                               +----------------+
                               |                |
                               |  Recognition   |
                               |  Decision      |
                               |                |
                               +----------------+
```