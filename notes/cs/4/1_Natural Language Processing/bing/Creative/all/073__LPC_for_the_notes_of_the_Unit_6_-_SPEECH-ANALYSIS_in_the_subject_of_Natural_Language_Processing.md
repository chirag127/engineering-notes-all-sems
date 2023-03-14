### LPC for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- LPC stands for Linear Predictive Coding, which is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model.
- LPC is the most widely used method in speech coding and speech synthesis. It is generally used for speech analysis and resynthesis. It is used as a form of voice compression by phone companies, such as in the GSM standard, for example.
- LPC starts with the assumption that a speech signal is produced by a buzzer at the end of a tube (for voiced sounds), with occasional added hissing and popping sounds (for voiceless sounds such as sibilants and plosives). This is called the source-filter model of speech production.
- LPC analyzes the speech signal by estimating the formants, removing their effects from the speech signal, and estimating the intensity and frequency of the remaining buzz. The process of removing the formants is called inverse filtering, and the remaining signal after the subtraction of the filtered modeled signal is called the residue.
- LPC synthesizes the speech signal by reversing the process: use the buzz parameters and the residue to create a source signal, use the formants to create a filter (which represents the tube), and run the source through the filter, resulting in speech.
- Because speech signals vary with time, this process is done on short chunks of the speech signal, which are called frames; generally, 30 to 50 frames per second give an intelligible speech with good compression.
- The main steps involved in LPC analysis and synthesis are:

  - Pre-emphasis: This is a process of applying a high-pass filter to the speech signal to boost the high-frequency components and reduce the dynamic range of the signal. This helps to improve the accuracy of the LPC model and reduce the effects of noise.
  - Framing and windowing: This is a process of dividing the speech signal into overlapping frames of fixed length (usually 10 to 30 ms) and applying a window function (such as Hamming or Hanning) to each frame to reduce the discontinuities at the edges of the frame.
  - Autocorrelation: This is a process of computing the correlation of the signal with itself at different time lags. This helps to find the periodicity and the spectral peaks of the signal, which are related to the pitch and the formants, respectively.
  - Linear prediction: This is a process of finding a set of coefficients that can be used to predict the current sample of the signal based on the previous samples. This is done by minimizing the mean squared error between the actual signal and the predicted signal. The prediction error is also called the residual or the excitation signal.
  - Levinson-Durbin recursion: This is a process of converting the autocorrelation coefficients into a set of reflection coefficients, which are used to construct the LPC filter. The reflection coefficients are also related to the formants and the bandwidths of the signal. The LPC filter is an all-pole filter that models the spectral envelope of the signal.
  - Analysis filter: This is a process of passing the speech signal through the LPC filter to obtain the residual signal. The LPC filter is also called the inverse filter, because it removes the effects of the vocal tract from the speech signal.
  - Synthesis filter: This is a process of passing the residual signal through the inverse of the LPC filter to obtain the reconstructed speech signal. The inverse of the LPC filter is an all-zero filter that models the vocal tract of the speaker.
  - De-emphasis: This is a process of applying a low-pass filter to the reconstructed speech signal to undo the effects of the pre-emphasis filter and restore the original dynamic range of the signal.

- The block diagram below shows the system of LPC analysis and synthesis.

```
+----------------+     +----------------+     +----------------+     +----------------+
|                |     |                |     |                |     |                |
|  Pre-emphasis  +---->+  Framing and   +---->+  Autocorrelation  +---->+  Linear       |
|                |     |  windowing     |     |                |     |  prediction    |
|                |     |                |     |                |     |                |