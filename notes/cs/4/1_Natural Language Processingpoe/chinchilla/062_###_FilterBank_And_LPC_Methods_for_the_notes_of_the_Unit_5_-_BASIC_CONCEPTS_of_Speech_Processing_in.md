### Filter Bank and LPC Methods for the Notes of Unit 5 - Basic Concepts of Speech Processing in the Subject of Natural Language Processing

Speech processing is a subfield of natural language processing that deals with the analysis, synthesis, and recognition of human speech. In this unit, we will cover two important methods for speech processing: Filter Bank and Linear Predictive Coding (LPC).

#### Filter Bank Method

The Filter Bank method is a technique used to analyze the spectral content of speech signals. It involves dividing the speech signal into several frequency bands using a bank of filters. Each filter in the bank is designed to pass a specific range of frequencies and reject all others. The output of each filter is then analyzed to obtain the spectral content of the signal.

##### Steps involved in the Filter Bank Method:

1. Pre-emphasis: The speech signal is pre-emphasized to boost the high-frequency components.

2. Windowing: The speech signal is divided into frames of fixed duration and a window function is applied to each frame to reduce spectral leakage.

3. Fourier Transform: The Fourier Transform is applied to each frame to convert the signal from the time domain to the frequency domain.

4. Filter Bank: The signal is passed through a bank of filters to obtain the spectral content of each frame.

5. Logarithmic Compression: The spectral content is compressed using a logarithmic function to improve the dynamic range.

6. Inverse Fourier Transform: The Inverse Fourier Transform is applied to each frame to convert the signal back to the time domain.

7. Overlapping and Add: The frames are then overlapped and added together to obtain the final output signal.

##### Advantages and Disadvantages of Filter Bank Method:

Advantages:
- Effective in analyzing the spectral content of speech signals
- Can be used for speech recognition and speaker identification

Disadvantages:
- Requires a large number of filters to be effective
- Computationally intensive

#### Linear Predictive Coding (LPC) Method

The Linear Predictive Coding (LPC) method is a technique used to model the spectral envelope of speech signals. It involves using a linear predictive model to estimate the coefficients of a filter that can approximate the spectral envelope of the signal.

##### Steps involved in the LPC Method:

1. Pre-emphasis: The speech signal is pre-emphasized to boost the high-frequency components.

2. Windowing: The speech signal is divided into frames of fixed duration and a window function is applied to each frame to reduce spectral leakage.

3. Autocorrelation: The autocorrelation function of each frame is computed.

4. Levinson-Durbin Algorithm: The Levinson-Durbin algorithm is used to estimate the coefficients of a filter that can approximate the spectral envelope of the signal.

5. Inverse Filter: The inverse filter is used to obtain the excitation signal.

6. Overlapping and Add: The frames are then overlapped and added together to obtain the final output signal.

##### Advantages and Disadvantages of LPC Method:

Advantages:
- Effective in modeling the spectral envelope of speech signals
- Can be used for speech compression, speech synthesis, and speaker identification

Disadvantages:
- Sensitive to noise
- Requires accurate estimation of the coefficients of the filter

### Mnemonics and Learning Tricks

For the Filter Bank Method, a useful mnemonic to remember the steps involved is "PWFILIO":
- P: Pre-emphasis
- W: Windowing
- F: Fourier Transform
- IL: Filter Bank
- I: Inverse Fourier Transform
- O: Overlapping and Add

For the LPC Method, a useful mnemonic to remember the steps involved is "PWALEO":
- P: Pre-emphasis
- W: Windowing
- A: Autocorrelation
- LE: Levinson-Durbin Algorithm
- O: Overlapping and Add