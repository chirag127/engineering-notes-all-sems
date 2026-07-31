# Weighted Cepstral Distances And Filtering for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- Cepstral distance is a measure of similarity between two speech signals based on their cepstral coefficients, which are obtained by applying a discrete cosine transform to the log magnitude spectrum of the signal.
- Cepstral distance can be used for speech recognition, speaker recognition, speech enhancement, and speech synthesis applications.
- A simple cepstral distance measure is the Euclidean distance between the cepstral coefficients of two speech frames, but this may not be optimal for capturing the perceptual differences between speech signals.
- A weighted cepstral distance measure is a variant of the cepstral distance measure that assigns different weights to the cepstral coefficients according to their importance or variability.
- One way to obtain the weights is to use the inverse of the variance of the cepstral coefficients, which reflects the degree of variation of each coefficient across different speech frames or speakers  .
- Another way to obtain the weights is to use the logarithm of the index of the cepstral coefficient, which reflects the frequency resolution of the cepstral coefficients .
- A weighted cepstral distance measure can improve the performance of speech recognition or speaker recognition systems by reducing the mismatch between the training and testing conditions or between different speakers.
- Filtering is a process of modifying the speech signal by applying a filter function to its spectrum or cepstrum. Filtering can be used for speech enhancement, speech synthesis, or speech modification applications.
- One example of filtering is cepstral mean subtraction (CMS), which is a technique of removing the channel or speaker effects from the speech signal by subtracting the mean of the cepstral coefficients from each speech frame.
- Another example of filtering is spectral subtraction, which is a technique of reducing the background noise from the speech signal by subtracting an estimate of the noise spectrum from the speech spectrum.
- Filtering can improve the quality or intelligibility of the speech signal by removing the unwanted components or enhancing the desired components.