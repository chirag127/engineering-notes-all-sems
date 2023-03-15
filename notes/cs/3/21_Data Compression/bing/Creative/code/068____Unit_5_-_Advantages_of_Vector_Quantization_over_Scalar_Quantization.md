```
## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Scalar quantization is a process of mapping a continuous-valued signal to a discrete set of output levels, called quantization levels or code words.
- Vector quantization is a process of mapping a vector of continuous-valued components, such as a block of pixels or a segment of speech, to a discrete set of output vectors, called code vectors or code books.
- Vector quantization has some advantages over scalar quantization, such as:

  - Higher compression ratio: Vector quantization can achieve higher compression ratio than scalar quantization by exploiting the correlation among the components of the input vector. For example, in image compression, vector quantization can reduce the number of bits needed to represent a block of pixels by using a code book that captures the common patterns or features of the image.
  - Lower distortion: Vector quantization can achieve lower distortion than scalar quantization by minimizing the mean squared error between the input vector and the output code vector. For example, in speech compression, vector quantization can preserve the perceptual quality of the speech signal by using a code book that matches the characteristics of the human auditory system.
  - Higher robustness: Vector quantization can achieve higher robustness than scalar quantization by reducing the sensitivity to noise or channel errors. For example, in wireless communication, vector quantization can improve the performance of the system by using a code book that is designed to cope with the channel conditions or the interference.
```