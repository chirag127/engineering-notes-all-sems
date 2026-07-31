# PLP And MFCC Coefficients

Perceptual Linear Prediction (PLP) and Mel-Frequency Cepstral Coefficients (MFCC) are two popular techniques used in speech analysis for feature extraction.

## PLP Coefficients
- PLP is a technique that applies a linear predictive model to the power spectrum of a speech signal.
- It is based on the idea that the human auditory system does not perceive sounds in a linear manner.
- PLP attempts to model the human auditory system by applying a series of transformations to the power spectrum of the speech signal.
- These transformations include critical-band filtering, equal-loudness pre-emphasis, and intensity-loudness conversion.
- The resulting spectrum is then used to compute the PLP coefficients using linear prediction.

## MFCC Coefficients
- MFCC is a technique that applies a non-linear transformation to the power spectrum of a speech signal.
- It is based on the idea that the human auditory system perceives sounds in a non-linear manner, with greater sensitivity to lower frequencies.
- MFCC attempts to model the human auditory system by applying a series of transformations to the power spectrum of the speech signal.
- These transformations include Mel-scale filtering and logarithmic compression.
- The resulting spectrum is then used to compute the MFCC coefficients using the Discrete Cosine Transform (DCT).

Both PLP and MFCC coefficients are commonly used in speech recognition and speaker identification systems. They provide a compact representation of the speech signal that is robust to variations in the recording environment and the speaker's voice. However, the choice of technique depends on the specific application and the desired trade-off between computational complexity and performance.