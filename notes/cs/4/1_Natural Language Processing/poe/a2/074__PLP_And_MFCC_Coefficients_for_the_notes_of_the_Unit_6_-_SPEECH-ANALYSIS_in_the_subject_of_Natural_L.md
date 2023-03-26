 Here is the content in markdown format without any emojis or external links:

### PLP And MFCC Coefficients for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

#### PLP (Perceptual Linear Prediction) Coefficients

- PLP coefficients are based on the human auditory system.
- They are designed to mimic the perception of loudness and frequency of a human ear.
- PLP analysis performs an auditory-based transformation called the intensity-loudness power law. This transformation models the non-linearity of the human ear.
- The PLP analysis is composed of three steps:

1. Apply a pre-emphasis filter to emphasize high frequency components.
2. Apply an auditory filter bank to emulate frequency analysis by the human ear.
3. Apply a cubic root amplitude compressor to model the intensity-loudness power law.

- The final PLP coefficients contain characteristics of human speech perception making them suitable for speech recognition tasks.

#### MFCC (Mel Frequency Cepstral Coefficients)

- MFCCs are coefficients that represent the short-term power spectrum of a sound, based on a linear cosine transform of a log power spectrum on a nonlinear mel scale of frequency.
- The steps involved in extracting MFCCs are:

1. Frame the speech signal into short segments.
2. Apply a window (like Hamming window) to each frame and calculate the Fast Fourier Transform (FFT).
3. Map the powers of the spectrum obtained above onto the mel scale using triangular overlapping windows.
4. Take the logs of the powers at each of the mel frequencies.
5. Apply the Discrete Cosine Transform (DCT) to the log powers. The result is the MFCCs.

- The MFCCs are generally more robust than the PLP coefficients and are more widely used. They are influenced by both the spectral shape and the total energy of the speech signal.

The content is written in formal tone with points and without any emojis or external links as instructed. Please let me know if you would like me to modify or expand the content in any way.