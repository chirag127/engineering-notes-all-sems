# Filter Bank and LPC Methods for Speech Processing

## Filter Bank Method

- A filter bank is a set of band-pass filters that divide the frequency spectrum of a signal into sub-bands.
- Filter bank features are derived from the energy or power spectrum of the signal, which is obtained by applying a Fourier transform to the signal frames.
- Filter bank features are often used as an alternative to cepstral features, such as mel-frequency cepstral coefficients (MFCC) or linear predictive cepstral coefficients (LPCC), for speech recognition.
- Filter bank features have some advantages over cepstral features, such as being more robust to noise and channel distortion, and being more computationally efficient.
- Filter bank features can be further processed by applying a discrete cosine transform (DCT) or a linear discriminant analysis (LDA) to reduce the dimensionality and enhance the discriminative power of the features.
- One example of filter bank features is the perceptual linear prediction (PLP) features, which are based on a psychoacoustic model of human hearing and use a critical-band filter bank to mimic the frequency resolution of the auditory system .

## LPC Method

- Linear predictive coding (LPC) is a method of speech analysis and synthesis that models the speech signal as a linear combination of past samples.
- LPC estimates the coefficients of an all-pole filter that represents the vocal tract, which are called the LPC coefficients or the linear prediction coefficients.
- LPC coefficients can be used to synthesize speech by applying the inverse filter to a source signal, which can be either a periodic pulse train (for voiced speech) or a white noise (for unvoiced speech).
- LPC coefficients can also be used to extract features for speech recognition, such as the LPC cepstral coefficients (LPCC) or the line spectral frequencies (LSF).
- LPC features have some advantages over filter bank features, such as being more compact and having a better representation of the spectral envelope of the speech signal.
- LPC features can also be combined with filter bank features to obtain hybrid features, such as the mel-frequency linear prediction (MFLP) features or the perceptual linear prediction cepstral coefficients (PLPCC)  .