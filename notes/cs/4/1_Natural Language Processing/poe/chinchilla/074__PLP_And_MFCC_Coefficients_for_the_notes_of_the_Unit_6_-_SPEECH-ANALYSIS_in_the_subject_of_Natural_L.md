### PLP And MFCC Coefficients for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

Speech analysis is a critical aspect of natural language processing. It involves extracting relevant features from speech signals to perform various tasks such as speaker identification, speech recognition, and emotion detection. Two popular techniques used for speech feature extraction are Perceptual Linear Prediction (PLP) and Mel Frequency Cepstral Coefficients (MFCC).

Here are some key points to help you understand PLP and MFCC coefficients for speech analysis:

#### Perceptual Linear Prediction (PLP)

- PLP is a technique used for speech feature extraction that models the human auditory system's perception of sound.
- It involves dividing the speech signal into overlapping frames and applying a filter bank to each frame to extract spectral information.
- The spectral information is then used to estimate the formants of the signal, which are the resonant frequencies of the vocal tract.
- PLP coefficients are obtained by applying a linear prediction analysis to the estimated formants. The result is a set of coefficients that capture the spectral envelope of the speech signal.
- PLP coefficients are often used in speech recognition systems because they are robust to noise and speaker variability.

#### Mel Frequency Cepstral Coefficients (MFCC)

- MFCC is another technique used for speech feature extraction that is based on the human auditory system's perception of sound.
- It involves dividing the speech signal into overlapping frames and applying a filter bank to each frame to extract spectral information.
- The spectral information is then transformed using the Discrete Cosine Transform (DCT) to obtain the cepstral coefficients.
- The cepstral coefficients are then modified using a logarithmic scale called the Mel scale, which models how humans perceive frequency.
- The resulting coefficients are called Mel Frequency Cepstral Coefficients (MFCC).
- MFCC coefficients are commonly used in speech recognition and speaker identification systems because they are robust to noise and speaker variability.

In conclusion, PLP and MFCC are two popular techniques used for speech feature extraction in natural language processing. Both techniques model the human auditory system's perception of sound and are robust to noise and speaker variability. Understanding these techniques is essential for building accurate and reliable speech recognition and speaker identification systems.