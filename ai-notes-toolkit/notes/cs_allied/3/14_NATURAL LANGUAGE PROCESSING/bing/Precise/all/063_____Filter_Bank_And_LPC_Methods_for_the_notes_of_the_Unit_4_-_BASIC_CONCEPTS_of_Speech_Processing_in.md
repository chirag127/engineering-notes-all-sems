# Filter Bank and LPC Methods

Filter bank and LPC methods are two techniques used in speech processing, specifically in the analysis of speech signals. These methods are commonly used in the field of natural language processing.

## Filter Bank Methods

Filter bank methods involve dividing the speech signal into different frequency bands using a set of bandpass filters. Each filter in the filter bank is designed to pass a specific range of frequencies while attenuating others. The output of each filter is then analyzed to extract information about the speech signal.

Some common filter bank methods used in speech processing include:
- Mel-Frequency Cepstral Coefficients (MFCCs): This method uses a filter bank based on the Mel scale, which is a perceptual scale of pitches judged by listeners to be equal in distance from one another.
- Perceptual Linear Prediction (PLP): This method uses a filter bank based on the Bark scale, which is another perceptual scale of pitches.

## LPC Methods

Linear Predictive Coding (LPC) is a method used to represent the spectral envelope of a speech signal. It involves analyzing the speech signal to determine a set of coefficients that can be used to predict future samples of the signal based on past samples.

LPC analysis is commonly used in speech coding, where the goal is to compress the speech signal for transmission or storage. It is also used in speech synthesis, where the goal is to generate synthetic speech that sounds natural.

In summary, filter bank and LPC methods are two important techniques used in speech processing. They are commonly used in natural language processing to analyze and extract information from speech signals. These methods can be used for various applications, including speech coding, speech synthesis, and speech recognition.