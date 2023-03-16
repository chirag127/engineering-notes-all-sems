### LPC for the notes of the Unit 5 - SPEECH-ANALYSIS in the subject of NATURAL LANGUAGE PROCESSING

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model .
- LPC analyzes the speech signal by estimating the formants, which are the resonant frequencies of the vocal tract, and removing their effects from the speech signal, leaving behind the residual signal, which contains the pitch and the noise components.
- The process of removing the formants is called inverse filtering, and the residual signal is obtained by subtracting the filtered modeled signal from the original speech signal.
- The linear predictive model assumes that the current sample of the speech signal can be approximated as a linear combination of the previous samples, plus some error term .
- The coefficients of the linear combination are called the LPC coefficients, or the prediction coefficients, and they can be obtained by minimizing the mean squared error between the original signal and the predicted signal .
- The LPC coefficients can be used to reconstruct the spectral envelope of the speech signal, which is a smooth curve that approximates the peaks and valleys of the frequency spectrum .
- The LPC coefficients can also be converted to the reflection coefficients, which are the ratios of the backward and forward traveling waves in a lossless transmission line model of the vocal tract .
- The reflection coefficients have some advantages over the LPC coefficients, such as being more stable, having a smaller dynamic range, and being more suitable for quantization and transmission .
- The residual signal can be further processed to extract the pitch and the noise components, which can be used to synthesize the speech signal by adding them to the filtered modeled signal .
- The synthesis of the speech signal from the LPC coefficients, the pitch, and the noise is called LPC synthesis, and it can produce intelligible speech with a low bit rate .
- LPC is the most widely used method in speech coding and speech synthesis, and it has many applications, such as voice over IP, speech recognition, speech enhancement, and speech modification .