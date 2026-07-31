# LPC for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- LPC stands for Linear Predictive Coding, a method for signal source modelling in speech signal processing .
- LPC is used to represent the spectral envelope of a speech signal in a compressed form, using the information of a linear predictive model.
- LPC is based on the assumption that a speech signal can be approximated by a linear combination of past samples, plus a prediction error.
- LPC can be divided into two steps: analysis and synthesis.
  - In the analysis step, the speech signal is divided into frames and the reflection coefficients are extracted from each frame using an algorithm such as autocorrelation or Levinson-Durbin.
  - The reflection coefficients are used to compute the LPC coefficients, which represent the filter that models the vocal tract.
  - The LPC coefficients are then used to inverse filter the speech signal, removing the effects of the vocal tract and leaving the residual signal, which represents the glottal source .
  - The residual signal can be further quantized and encoded for transmission or storage.
  - In the synthesis step, the residual signal is decoded and filtered by the LPC filter, reconstructing the speech signal with the original spectral envelope.
- LPC is often used by linguists as a formant extraction tool, since the LPC filter can capture the resonant frequencies of the vocal tract .
- LPC has wide applications in other areas, such as speech coding, speech synthesis, speech recognition, speaker identification, and voice conversion.