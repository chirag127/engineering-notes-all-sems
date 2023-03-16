### PLP and MFCC Coefficients for Speech Analysis

- Speech analysis is the process of extracting useful information from speech signals, such as the speaker identity, emotion, language, accent, etc.
- Speech analysis requires feature extraction methods that can represent the speech signals in a compact and discriminative way, while capturing the relevant characteristics of the speech production and perception.
- PLP and MFCC are two popular feature extraction methods for speech analysis, based on different models of the human auditory system.
- PLP stands for Perceptual Linear Prediction, and it is a method that applies a linear predictive analysis to the frequency spectrum of the speech signal, after applying a psychoacoustic model that mimics the human hearing sensitivity and frequency resolution .
- MFCC stands for Mel Frequency Cepstral Coefficients, and it is a method that computes the cepstral coefficients of the speech signal, after applying a filter bank that approximates the human auditory system's nonlinear frequency scaling, known as the mel scale .
- Both PLP and MFCC aim to reduce the dimensionality of the speech signal and to enhance the features that are relevant for speech recognition and speaker identification.
- PLP and MFCC differ in the way they model the human auditory system, and in the way they compute the cepstral coefficients.
- PLP uses an all-pole model to represent the spectrum of the speech signal, while MFCC uses a discrete cosine transform (DCT) to obtain the cepstral coefficients .
- PLP also applies an equal-loudness curve and an intensity-loudness power law to the spectrum, to account for the human perception of loudness at different frequencies .
- MFCC applies a logarithmic function to the filter bank outputs, to account for the human perception of loudness as a logarithmic function of intensity .
- PLP and MFCC have different advantages and disadvantages for speech analysis, depending on the application and the data.
- PLP is more robust to noise and channel distortion, as it models the spectrum more accurately and smoothly .
- MFCC is more sensitive to fine spectral details, as it preserves the high-frequency information better than PLP .
- PLP and MFCC can be combined or modified to improve their performance, such as using PLP-RASTA, which applies a temporal filtering to the PLP coefficients to reduce the effects of noise and channel variation , or using delta and delta-delta features, which capture the dynamic information of the speech signal by computing the first and second derivatives of the cepstral coefficients .