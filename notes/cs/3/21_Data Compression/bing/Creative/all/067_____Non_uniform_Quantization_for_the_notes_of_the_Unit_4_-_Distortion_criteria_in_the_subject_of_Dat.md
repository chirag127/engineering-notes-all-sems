# Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal intervals.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely to occur than others.
- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions where the input values are more concentrated and less bits to the regions where the input values are less frequent.
- Non uniform quantization can be implemented in different ways, such as:
  - Using a non-linear function to map the input values to the output values, such as the logarithmic function or the companding function.
  - Using an adaptive quantizer that adjusts the quantization intervals according to the statistics of the input signal, such as the Lloyd-Max quantizer or the delta modulation quantizer.
  - Using a trainable quantizer that learns the optimal quantization points from the data, such as the vector quantizer or the neural network quantizer .
- Non uniform quantization has applications in data compression, signal processing, machine learning, and communication systems    .