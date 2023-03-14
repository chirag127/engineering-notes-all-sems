### PLP And MFCC Coefficients for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

Speech analysis is an important area in natural language processing that involves understanding the acoustic properties of speech. The analysis of speech signals is essential for many applications, including speech recognition, speaker identification, and emotion recognition. In this context, two important techniques for speech analysis are PLP and MFCC coefficients.

#### PLP Coefficients

Perceptual Linear Prediction (PLP) is a technique used to extract features from speech signals that are based on the human auditory system's perception. PLP coefficients are calculated by taking into account the spectral properties of sound and the way the human ear responds to them. Some of the key features of PLP coefficients are:

- PLP coefficients are calculated by first applying a pre-emphasis filter to the input signal to amplify the high-frequency components of the speech signal.
- The speech signal is then divided into overlapping frames, and a power spectrum is calculated for each frame using the Fourier transform.
- The power spectrum is then transformed using the Mel filter bank, which is a set of filters that are designed to match the human ear's frequency response.
- The Mel-filtered spectrum is then compressed using a non-linear transformation that approximates the logarithm of the power spectrum. This transformation is based on the observation that the human ear responds to loudness on a logarithmic scale.
- Finally, the PLP coefficients are calculated by taking the discrete cosine transform (DCT) of the compressed Mel-filtered spectrum.

#### MFCC Coefficients

Mel Frequency Cepstral Coefficients (MFCC) are another popular technique for speech analysis that is based on the Mel filter bank. MFCC coefficients are calculated in a similar way to PLP coefficients, but with some key differences. Some of the key features of MFCC coefficients are:

- Like PLP coefficients, MFCC coefficients are calculated by first applying a pre-emphasis filter to the input signal and dividing it into overlapping frames.
- The power spectrum of each frame is then calculated using the Fourier transform.
- The Mel-filtered spectrum is then calculated using the Mel filter bank, as in the case of PLP coefficients.
- However, instead of compressing the Mel-filtered spectrum using a non-linear transformation, as in the case of PLP coefficients, the logarithm of the Mel-filtered spectrum is taken and then transformed using the DCT.
- The resulting coefficients are called MFCC coefficients.

#### Mnemonic for Remembering PLP and MFCC Coefficients

To remember the difference between PLP and MFCC coefficients, you can use the following mnemonic:

- "PLP is perceptual, so it uses a non-linear transformation based on loudness perception, while MFCC is cepstral, so it uses the logarithm of the Mel-filtered spectrum."

This mnemonic highlights the key difference between PLP and MFCC coefficients, namely that PLP coefficients are based on the perception of loudness, while MFCC coefficients are based on the cepstral analysis of the spectral envelope.

In conclusion, PLP and MFCC coefficients are two important techniques for speech analysis that are widely used in natural language processing applications. Both techniques are based on the Mel filter bank, but they differ in the way they compress the Mel-filtered spectrum. By understanding the differences between these techniques and the way they are calculated, you can better understand how they can be used in practical applications such as speech recognition and speaker identification.