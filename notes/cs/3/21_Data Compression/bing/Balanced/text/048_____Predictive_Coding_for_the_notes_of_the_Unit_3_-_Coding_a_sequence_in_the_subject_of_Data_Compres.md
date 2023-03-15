### Predictive Coding

- Predictive coding is a method of lossless data compression that uses a model to predict the next symbol or bit in a sequence, based on the previous symbols or bits.
- The prediction error, or the difference between the actual and predicted symbol or bit, is then encoded using a variable-length code, such as arithmetic coding or Huffman coding.
- Predictive coding can achieve higher compression ratios than fixed-length codes, because the prediction error tends to have a lower entropy than the original data.
- Predictive coding can be applied to different types of data, such as audio, image, video, or text.
- Some examples of predictive coding algorithms are:
  - Linear predictive coding (LPC), which models the spectral envelope of a speech signal using a linear filter and encodes the filter coefficients and the residual signal.
  - Dynamic Markov compression (DMC), which models the probability distribution of the next bit in a binary sequence using a Markov chain and encodes the bits using arithmetic coding.
  - WebP, which is an image format that uses predictive coding to reduce the spatial redundancy in each block of pixels and encodes the residuals using a combination of Huffman coding and arithmetic coding.