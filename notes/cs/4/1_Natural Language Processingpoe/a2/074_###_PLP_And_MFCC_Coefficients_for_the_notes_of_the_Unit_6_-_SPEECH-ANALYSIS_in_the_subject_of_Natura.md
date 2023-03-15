 Here is the content in markdown format:

### PLP And MFCC Coefficients for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

PLP (Perceptual Linear Predictive) coefficients -

- PLP is a speech analysis technique that mimics the human auditory system.
- It applies a filter that equals the frequency sensitivity of the human ear.
- It performs a log compression on the filterbank energies similar to the human ear's nonlinearity.
- The log compressed energies are then used to extract PLP cepstral coefficients.
- PLP coefficients are more robust to noise and channel variations compared to LPCCs.

MFCC (Mel Frequency Cepstral Coefficients) -

- MFCC is a speech analysis technique that models the human ear's response to frequencies.
- It applies a filterbank that mimics the frequency resolution of the human ear. The filters are spaced linearly at low frequencies and logarithmically at high frequencies.
- The log compressed filterbank energies are then used to extract MFCC cepstral coefficients.
- MFCCs are the most popular speech features used in speech recognition systems.
- Some key advantages are - they capture the phonetic content of speech, reduce the effect of noise, and are easy to compute.

Mnemonics and Learning Tricks -

- PLP - Think of PLP as mimicking the human Perceptual system and applying a Log compression similar to the human ear.
- MFCC - Think of MFCC as using a Mel scale Frequency filterbank that Compresses the energies and then extracts Cepstral coefficients. The Mel scale and log compression mimic the human ear's response.

Applications - Both PLP and MFCC coefficients are widely used as speech features to train models for speech recognition, speaker recognition and other speech processing tasks. MFCCs are more popular but PLP coefficients can be more robust to noise. The choice of coefficients depends on the exact application and how sensitive it is to noise/channel variations.