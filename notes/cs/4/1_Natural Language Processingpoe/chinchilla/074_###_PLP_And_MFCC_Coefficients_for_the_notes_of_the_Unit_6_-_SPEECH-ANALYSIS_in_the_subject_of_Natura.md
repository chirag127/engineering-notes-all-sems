### PLP And MFCC Coefficients for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

In speech analysis, the goal is to extract useful features from the speech signal that can be used for various tasks such as speech recognition, speaker identification, etc. Two popular feature extraction techniques used in speech analysis are the Perceptual Linear Prediction (PLP) and Mel-Frequency Cepstral Coefficients (MFCC).

#### Perceptual Linear Prediction (PLP)

- PLP is a feature extraction technique that models the human auditory system's perception of sound.
- It is based on the Linear Predictive Coding (LPC) technique, which models the speech signal as a linear combination of its past values.
- The PLP algorithm uses a non-linear frequency warping function to convert the frequency domain of the signal into a perceptually meaningful domain.
- The resulting PLP coefficients are highly correlated with the human auditory system's perception of sound and are hence useful for speech recognition tasks.
- PLP has several advantages over MFCC, such as better noise robustness, reduced sensitivity to spectral tilt, and better speaker normalization.
- However, PLP has higher computational complexity than MFCC.

#### Mel-Frequency Cepstral Coefficients (MFCC)

- MFCC is a widely used feature extraction technique in speech analysis.
- It is based on the Mel scale, which is a perceptual scale of pitches judged by listeners to be equal in distance from one another.
- The MFCC algorithm involves taking the log of the magnitude of the Fourier Transform of short-time frames of the speech signal.
- The resulting log-magnitude spectrum is then transformed using the Discrete Cosine Transform (DCT) to obtain the MFCC coefficients.
- MFCC has several advantages, such as being computationally efficient, having a low-dimensional feature space, and being highly discriminative for speech recognition tasks.
- However, MFCC is sensitive to noise and spectral tilt, and it requires careful normalization to handle speaker variability.

#### Learning Tricks and Mnemonics

- To remember the key differences between PLP and MFCC, remember the phrase "PLP is perceptually linear, while MFCC is Mel-frequency cepstral."
- To remember the MFCC algorithm's steps, remember the phrase "Log, Mel, DCT."