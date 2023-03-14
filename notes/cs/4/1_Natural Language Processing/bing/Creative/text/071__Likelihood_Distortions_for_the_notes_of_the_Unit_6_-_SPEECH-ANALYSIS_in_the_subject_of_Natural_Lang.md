### Likelihood Distortions

- Likelihood distortions are measures of the spectral distance or similarity between two short-time spectra, usually derived from linear predictive coding (LPC) analysis of speech signals.
- Likelihood distortions are commonly used in speech recognition systems to compare the input speech signal with a set of reference templates or models, and to find the best match using dynamic time warping (DTW) or hidden Markov models (HMMs).
- Some of the likelihood distortions that have been proposed and studied are:

  - Itakura-Saito (IS) distortion: This is the maximum likelihood distortion measure, which is based on the ratio of the input spectral density and the model spectral density. It is asymmetrical and sensitive to the spectral shape, but not to the spectral level. It is given by:

    $$d_{IS}(S,f) = \int_{-\pi}^{\pi} \left[ \frac{S(\omega)}{f(\omega)} - \log \frac{S(\omega)}{f(\omega)} - 1 \right] d\omega$$

    where $S(\omega)$ is the input spectral density and $f(\omega)$ is the model spectral density.

  - Log likelihood ratio (LLR) distortion: This is a symmetrical distortion measure, which is based on the logarithm of the ratio of the input spectral density and the model spectral density. It is sensitive to both the spectral shape and level. It is given by:

    $$d_{LLR}(S,f) = \int_{-\pi}^{\pi} \left[ \log S(\omega) - \log f(\omega) \right]^2 d\omega$$

  - Likelihood ratio (LR) distortion: This is a symmetrical distortion measure, which is based on the ratio of the input spectral density and the model spectral density. It is sensitive to both the spectral shape and level. It is given by:

    $$d_{LR}(S,f) = \int_{-\pi}^{\pi} \left[ \frac{S(\omega)}{f(\omega)} - 1 \right]^2 d\omega$$

  - Cepstral (CEP) distortion: This is a symmetrical distortion measure, which is based on the difference of the input cepstrum and the model cepstrum. It is sensitive to both the spectral shape and level. It is given by:

    $$d_{CEP}(S,f) = \sum_{n=0}^{N-1} \left[ c_n(S) - c_n(f) \right]^2$$

    where $c_n(S)$ and $c_n(f)$ are the cepstral coefficients of the input and the model spectra, respectively.

  - Weighted likelihood ratio (WLR) distortion: This is a perceptually based distortion measure, which is based on the weighted ratio of the input spectral density and the model spectral density. It is sensitive to both the spectral shape and level, but it gives more weight to the spectral regions that are more important for speech perception. It is given by:

    $$d_{WLR}(S,f) = \int_{-\pi}^{\pi} W(\omega) \left[ \frac{S(\omega)}{f(\omega)} - 1 \right]^2 d\omega$$

    where $W(\omega)$ is a weighting function that reflects the perceptual importance of different frequency bands.

  - Weighted slope metric (WSM) distortion: This is another perceptually based distortion measure, which is based on the difference of the input spectral slope and the model spectral slope. It is sensitive to the spectral shape, but not to the spectral level. It is given by:

    $$d_{WSM}(S,f) = \int_{-\pi}^{\pi} W(\omega) \left[ \frac{d\log S(\omega)}{d\omega} - \frac{d\log f(\omega)}{d\omega} \right]^2 d\omega$$

    where $W(\omega)$ is the same weighting function as in the WLR distortion.

- The performance of different likelihood distortions in speech recognition depends on various factors, such as the vocabulary size, the number of speakers, the speech quality, the noise level, the speech features, the recognition algorithm, etc.
- Some general observations from previous studies are:

  - All LPC-based distortion measures performed reasonably well, but the LLR and WSM distortion measures gave the highest recognition accuracy