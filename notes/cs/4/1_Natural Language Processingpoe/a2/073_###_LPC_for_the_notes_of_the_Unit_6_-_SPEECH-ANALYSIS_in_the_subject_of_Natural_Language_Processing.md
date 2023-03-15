 Here is the content in markdown format:

### LPC for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

1. Linear Prediction Coding (LPC) - LPC is a tool used to compress speech signals. It works on the principle of estimating the current sample as a linear combination of the previous samples. The coefficients of the linear combination are called the LPC coefficients or LPC parameters.
2. Steps involved in LPC -
    1. Divide the speech signal into frames of N samples each.
    2. Calculate the autocorrelation of each frame.
    3. Solve the autocorrelation values using the Burg method to get the LPC coefficients.
    4. The LPC coefficients contain the resonance information of the vocal tract and hence can be used to synthesize speech.
3. Applications of LPC -
    1. Speech compression - LPC is widely used for low bit rate speech coding as the LPC parameters can be quantized and transmitted instead of the speech samples. This leads to compression.
    2. Speech synthesis - The LPC coefficients can be used to synthesize speech. The synthesizer produces an output by filtering white noise through an all-pole filter whose coefficients are the LPC coefficients.

Mnemonics -
LPC - Linear predictor coding
Burg method - Solves the autocorrelation to get LPC coefficients

Advantages -
1. Compresses speech effectively leading to low bit rates.
2. The resonant information of the vocal tract is captured in the LPC coefficients which can be used to synthesize natural sounding speech.

Disadvantages -
1. The speech quality degrades with high compression.
2. Presence of noise affects the LPC analysis and coefficients significantly leading to reduction in speech quality.

References -
[1] http://www.speech.cs.cmu.edu/15-492/lectures/lec15_lpc.html
[2] https://en.wikipedia.org/wiki/Linear_predictive_coding