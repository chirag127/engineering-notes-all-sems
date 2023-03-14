### Weighted Cepstral Distances And Filtering for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Weighted cepstral distances and filtering are techniques to measure the similarity or dissimilarity between speech signals based on their cepstral features.
- Cepstral features are derived from the spectrum of a speech signal by applying a logarithmic function and an inverse Fourier transform. They capture the information about the vocal tract shape and the excitation source of speech.
- Weighted cepstral distances and filtering are useful for speech recognition, speaker identification, speech enhancement, and speech synthesis applications.
- Some of the advantages of weighted cepstral distances and filtering are:
  - They are robust to noise and channel variations.
  - They can handle different speaking rates and styles.
  - They can reduce the dimensionality of the feature space and improve the computational efficiency.
- Some of the disadvantages of weighted cepstral distances and filtering are:
  - They may lose some information about the fine structure of the spectrum and the phase of the speech signal.
  - They may be sensitive to the choice of the weighting function and the filter parameters.
  - They may not capture the dynamic and contextual information of speech.

- The basic steps of weighted cepstral distances and filtering are:

  1. Compute the cepstral coefficients of the speech signals using a discrete Fourier transform (DFT), a logarithmic function, and an inverse DFT.
  2. Apply a weighting function to the cepstral coefficients to emphasize or de-emphasize certain frequency bands. The weighting function can be based on the human auditory system, the signal-to-noise ratio, or the spectral shape of the speech signal.
  3. Apply a filtering operation to the weighted cepstral coefficients to smooth or sharpen the cepstral features. The filtering operation can be a low-pass filter, a high-pass filter, a band-pass filter, or a liftering operation.
  4. Compute the distance between the filtered cepstral coefficients of the speech signals using a suitable metric, such as the Euclidean distance, the Mahalanobis distance, or the Kullback-Leibler divergence.
  5. Compare the distance with a threshold or a reference value to determine the similarity or dissimilarity between the speech signals.

- An example of weighted cepstral distances and filtering is the mel-frequency cepstral coefficients (MFCCs), which are widely used for speech recognition and speaker identification. The steps of MFCCs are:

  1. Compute the cepstral coefficients of the speech signals using a DFT, a logarithmic function, and an inverse DFT.
  2. Apply a mel-scale weighting function to the cepstral coefficients to mimic the human auditory system. The mel-scale is a perceptual scale of pitches that is linear at low frequencies and logarithmic at high frequencies.
  3. Apply a liftering operation to the weighted cepstral coefficients to enhance the lower-order cepstral features, which contain more information about the vocal tract shape. The liftering operation is a multiplication of the cepstral coefficients by a sine or a cosine function.
  4. Compute the distance between the liftered cepstral coefficients of the speech signals using a suitable metric, such as the Euclidean distance, the Mahalanobis distance, or the Kullback-Leibler divergence.
  5. Compare the distance with a threshold or a reference value to determine the similarity or dissimilarity between the speech signals.

- A possible mnemonic to remember the steps of MFCCs is:

  - DFT, Log, IDFT: Do Logarithms Invert DFT?
  - Mel-scale weighting: Melody is weighted by frequency.
  - Liftering: Lift the lower-order coefficients.
  - Distance metric: Distance measures dissimilarity.