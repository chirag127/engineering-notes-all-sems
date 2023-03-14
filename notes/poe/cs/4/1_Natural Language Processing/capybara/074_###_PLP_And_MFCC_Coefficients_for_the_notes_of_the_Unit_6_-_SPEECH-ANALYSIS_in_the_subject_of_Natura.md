### PLP And MFCC Coefficients for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

In the field of speech analysis, PLP (Perceptual Linear Prediction) and MFCC (Mel Frequency Cepstral Coefficients) are two commonly used features extraction techniques. Both of these techniques are used to extract the features of speech signals that can be used for speech recognition, speaker identification, and other related tasks. In this unit, we will learn about these techniques in detail. 

#### PLP (Perceptual Linear Prediction)

Perceptual Linear Prediction is a technique that is used to extract the features of speech signals. It is based on the theory of human auditory perception. This technique involves the following steps:

1. Pre-emphasis: The first step in PLP is to apply pre-emphasis to the speech signal. This is done to amplify the high-frequency components of the signal.

2. Windowing: In this step, the speech signal is divided into frames of equal length using a windowing function.

3. Fourier Transform: The Fourier transform is applied to each frame to obtain the power spectrum.

4. Mel Filtering: In this step, the power spectrum is filtered through a set of triangular filters that are spaced according to the Mel scale.

5. Non-linear Transformation: The filtered power spectrum is then subjected to a non-linear transformation that is similar to the logarithm.

6. Perceptual Weighting: The non-linearly transformed spectrum is then weighted according to the perceived sensitivity of the human ear to different frequencies.

7. Linear Prediction: Finally, linear prediction is applied to the weighted spectrum to obtain the PLP coefficients.

#### MFCC (Mel Frequency Cepstral Coefficients)

Mel Frequency Cepstral Coefficients is another technique that is used to extract the features of speech signals. This technique is based on the Mel scale and the cepstral analysis. The following steps are involved in MFCC:

1. Pre-emphasis: Similar to PLP, the first step in MFCC is to apply pre-emphasis to the speech signal.

2. Windowing: The speech signal is divided into frames of equal length using a windowing function.

3. Fourier Transform: The Fourier transform is applied to each frame to obtain the power spectrum.

4. Mel Filtering: The power spectrum is then filtered through a set of triangular filters that are spaced according to the Mel scale.

5. Logarithm: The filtered power spectrum is then subjected to a logarithmic transformation.

6. Discrete Cosine Transform: The resulting spectrum is then transformed using the Discrete Cosine Transform (DCT) to obtain the MFCC coefficients.

#### Learning Tricks and Mnemonics

While there are no specific learning tricks or mnemonics for PLP and MFCC coefficients, it is important to understand the underlying principles behind these techniques. For instance, understanding the Mel scale and the concept of cepstral analysis can help in understanding MFCC. Similarly, understanding the theory of human auditory perception can aid in understanding PLP. Practice and repetition can also help in mastering these techniques.