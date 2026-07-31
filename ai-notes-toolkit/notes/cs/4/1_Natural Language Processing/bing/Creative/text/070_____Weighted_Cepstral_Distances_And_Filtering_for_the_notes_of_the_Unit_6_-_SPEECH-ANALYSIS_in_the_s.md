### Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform (DCT) to the log-magnitude spectrum of the signal.
- Cepstral distance is often used in speech recognition and speaker recognition systems to compare the input speech with the stored templates or models.
- Cepstral distance can be computed as the Euclidean distance, the Mahalanobis distance, or the cosine distance between the cepstral vectors of two speech frames.
- Weighted cepstral distance is a variant of cepstral distance that assigns different weights to the cepstral coefficients according to their importance or variability.
- One way to obtain the weights is to use the inverse of the variance of the cepstral coefficients, which reflects the degree of variation of each coefficient within a speaker or a word class .
- Another way to obtain the weights is to use the logarithm of the index of the cepstral coefficient, which reflects the degree of correlation between the cepstral coefficients and the spectral envelope of the speech signal.
- Weighted cepstral distance can improve the performance of speech recognition and speaker recognition systems by emphasizing the more discriminative or informative features and reducing the influence of noise or irrelevant features.
- Filtering is a process of modifying the speech signal or its spectrum to enhance its quality or extract some features.
- Filtering can be applied in the time domain or the frequency domain, using different types of filters such as low-pass, high-pass, band-pass, band-stop, or notch filters.
- Filtering can be used for various purposes in speech analysis, such as removing noise, smoothing the spectrum, emphasizing certain frequency bands, or extracting the fundamental frequency or the formants of the speech signal.