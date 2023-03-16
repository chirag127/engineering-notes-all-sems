# LPC for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model .
- LPC is the most widely used method in speech coding and speech synthesis, as it is a powerful speech analysis technique and a low-bit-rate speech encoder.
- LPC analyzes the speech signal by estimating the formants, which are the resonant frequencies of the vocal tract, and removing their effects from the speech signal, resulting in a residual signal that contains the pitch and the unvoiced components .
- The process of removing the formants is called inverse filtering, and the residual signal after the subtraction of the filtered modeled signal is called the residue.
- LPC uses a linear predictive model to approximate the current speech sample as a linear combination of past speech samples, and the coefficients of this linear combination are called the LPC coefficients  .
- The LPC coefficients can be converted to other equivalent representations, such as the reflection coefficients, the line spectral frequencies, or the cepstral coefficients, which have different properties and applications  .
- The LPC coefficients can be used to compute the LPC spectrum, which is the frequency response of the inverse filter, and represents the spectral envelope of the speech signal  .
- The LPC spectrum can be used to extract features for speech recognition, such as the formant frequencies and bandwidths, the pitch frequency, and the voiced/unvoiced decision  .
- The LPC coefficients and the residual signal can be used to synthesize speech by applying the inverse filter to the residual signal, and adding some noise to the unvoiced segments  .
- The LPC coefficients and the residual signal can also be quantized and encoded to achieve a low-bit-rate speech compression, which can be transmitted or stored and decoded to reconstruct the speech signal  .