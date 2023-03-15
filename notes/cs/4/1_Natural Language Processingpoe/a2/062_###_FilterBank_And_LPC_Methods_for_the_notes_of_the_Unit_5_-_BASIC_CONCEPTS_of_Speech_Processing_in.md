 Here is the content in markdown format for the topic ### FilterBank And LPC Methods for the notes of the Unit 5 - BASIC CONCEPTS of Speech Processing in the subject of Natural Language Processing:

### FilterBank And LPC Methods

Filter bank and Linear Predictive Coding (LPC) are two important analysis techniques for speech processing.

#### Filter Bank Method:

- Speech signal is passed through a bank of bandpass filters to split the signal into multiple frequency bands.
- The output of each bandpass filter is the signal component in that frequency range.
- These filter outputs contain information about the spectral envelope of the speech signal.
- The filter bank method is useful for estimating the spectral envelope of speech.

**Advantages:**

- Simple and intuitive method.
- Insensitive to noise.

**Disadvantages:**

- Requires large number of filters to get good frequency resolution.
- Unable to capture dynamic variations in the spectral envelope.

**Applications:** Speech coding, Speech enhancement

#### LPC Method:

- The speech signal is modeled as the output of an all-pole filter excited by a periodic impulse train (for voiced speech) or white noise (for unvoiced speech).
- LPC estimates the coefficients of the all-pole filter to obtain the spectral envelope of the speech signal.
- LPC provides a parametric representation of the spectral envelope in terms of the filter coefficients.

**Advantages:**

- Requires fewer parameters compared to filter bank method.
- Able to capture dynamic variations in the spectral envelope.

**Disadvantages:**

- More complex and less intuitive.
- Sensitive to noise.

**Applications:** Speech coding, Speech synthesis, Speaker recognition

**Mnemonics:**

- Think of filter bank as a "bank of filters" splitting the signal into frequency bands.
- Think of LPC as "linearly predicting coefficients" to model the speech signal.

**Learning Tricks:**

- Implement both the methods using software and analyze speech signals to understand the key steps and outputs. This will help in remembering the concepts and methods.
- Visualize the block diagrams of the methods and relate the blocks to the steps involved. This makes the methods more memorable.