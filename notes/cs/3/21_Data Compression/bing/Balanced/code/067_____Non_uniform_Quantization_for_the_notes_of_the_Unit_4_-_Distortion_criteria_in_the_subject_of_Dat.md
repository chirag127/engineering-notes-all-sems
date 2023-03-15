### Non uniform Quantization

- Non uniform quantization is a technique of mapping input values from a large set (often a continuous set) to output values in a smaller set (often a discrete set) with unequal spacing between the output values.
- Non uniform quantization is more suitable for signals that have non-uniform distributions, such as speech or image signals, where some values are more likely to occur than others.
- Non uniform quantization can achieve lower distortion than uniform quantization with the same number of bits, by allocating more bits to the regions of high probability and less bits to the regions of low probability.
- Non uniform quantization can be implemented in different ways, such as:
  - Using a non-linear function to map the input values to the output values, such as the logarithmic function or the companding function.
  - Using an adaptive quantizer that adjusts the output levels according to the statistics of the input signal.
  - Using a trainable quantizer that optimizes the output levels using the back-propagation of the network gradients, such as in neural network compression .
- Non uniform quantization can reduce the quantization noise and improve the signal-to-noise ratio (SNR) of the quantized signal, but it also introduces some challenges, such as:
  - The complexity and cost of the quantizer and the dequantizer, which may require non-linear operations or feedback mechanisms.
  - The compatibility and interoperability of the quantizer and the dequantizer, which may require a common standard or a shared codebook.
  - The accuracy and efficiency of the quantizer and the dequantizer, which may depend on the quality of the non-linear function or the optimization algorithm .