### Filter Bank And LPC Methods for the Notes of the Unit 5 - Basic Concepts of Speech Processing in the Subject of Natural Language Processing

Filter Bank and Linear Predictive Coding (LPC) are two widely used methods in speech processing for feature extraction and speech analysis. Here are the details of both methods:

#### Filter Bank Method:
The filter bank method is used to extract the spectral envelope of speech signals. The spectral envelope is the energy distribution of speech signals over frequency and is used to identify the formants, which are the resonant frequencies of the vocal tract. The filter bank method consists of the following steps:

1. Pre-emphasis: The purpose of pre-emphasis is to boost the high-frequency components of speech signals and to reduce the effect of low-frequency noise. A high-pass filter is used to perform pre-emphasis.

2. Windowing: The speech signal is divided into frames of fixed duration using a window function. The most commonly used window function is the Hamming window.

3. Discrete Fourier Transform (DFT): The DFT is applied to each frame to obtain the frequency spectrum of the speech signal.

4. Mel Filter Bank: The Mel filter bank is used to extract the spectral envelope of speech signals. The Mel filter bank is a set of triangular filters that are spaced uniformly on the Mel scale, which is a perceptual scale of pitch based on the human ear's response to sound.

5. Logarithmic Compression: The output of the Mel filter bank is compressed logarithmically to match the human perception of loudness.

#### LPC Method:
The LPC method is used to model the vocal tract of speech signals. The vocal tract is the part of the human body that is responsible for producing speech sounds. The LPC method consists of the following steps:

1. Windowing: The speech signal is divided into frames of fixed duration using a window function. The most commonly used window function is the Hamming window.

2. Autocorrelation: The autocorrelation function is calculated for each frame of speech signals.

3. Levinson-Durbin Algorithm: The Levinson-Durbin algorithm is used to compute the LPC coefficients that minimize the prediction error between the original speech signal and the predicted speech signal.

4. Spectral Envelope: The LPC coefficients are used to estimate the spectral envelope of speech signals.

#### Advantages of Filter Bank and LPC Methods:
- Both methods are widely used in speech processing for feature extraction and speech analysis.
- Filter Bank method is useful for identifying the formants, which are critical for speech recognition.
- LPC method is useful for modeling the vocal tract and generating speech signals.

#### Disadvantages of Filter Bank and LPC Methods:
- Both methods are computationally expensive and require a significant amount of memory.
- The accuracy of these methods depends on the quality of the speech signal and the choice of parameters.

### Mnemonic:
A possible mnemonic for remembering the steps of the Filter Bank method is PWDLM (Pre-emphasis, Windowing, DFT, Logarithmic Compression, Mel Filter Bank).