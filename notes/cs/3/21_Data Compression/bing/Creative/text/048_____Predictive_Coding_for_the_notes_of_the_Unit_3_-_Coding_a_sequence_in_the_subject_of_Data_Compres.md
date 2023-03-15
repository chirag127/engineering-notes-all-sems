### Predictive Coding

- Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, based on the previous symbols or bits.
- The prediction error, or the difference between the actual and predicted symbol or bit, is then encoded using a variable-length code, such as arithmetic coding, Huffman coding, or Golomb coding.
- Predictive coding can achieve higher compression ratios than fixed-length codes, because the prediction error tends to have a lower entropy than the original data.
- Predictive coding can be applied to different types of data, such as text, audio, image, or video. Depending on the data, different models can be used to make predictions, such as Markov models, linear models, neural networks, or wavelets.
- Some examples of predictive coding algorithms are:
  - Dynamic Markov compression (DMC), which uses a Markov model to predict the next bit in a binary sequence .
  - Linear predictive coding (LPC), which uses a linear model to predict the next sample in an audio signal.
  - WebP, which uses a directional predictor to predict the next pixel in an image.
  - Compressed predictive information coding (CPIC), which uses a neural network to predict the next state in a dynamic system.