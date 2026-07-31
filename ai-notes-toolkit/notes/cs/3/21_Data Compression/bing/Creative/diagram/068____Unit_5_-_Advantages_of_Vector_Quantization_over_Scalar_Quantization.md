## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

- Quantization is the process of mapping input values from a large set (often a continuous set) to output values in a (countable) smaller set, often with a finite number of elements.
- Scalar quantization is a type of quantization where each input symbol is treated separately in producing the output.
- Vector quantization is a type of quantization where the input symbols are clubbed together in groups called vectors, and processed to give the output.
- Some of the advantages of vector quantization over scalar quantization are:

  - Vector quantization can remove auto-correlation in the encoded signal and therefore, is more efficient in rate-distortion terms than scalar quantization.
  - Vector quantization can exploit the inter-symbol dependencies and reduce the redundancy in the input data.
  - Vector quantization can achieve higher compression ratios and lower distortion than scalar quantization for the same number of bits per input tuple.
  - Vector quantization can better adapt to the local characteristics of the input data and preserve the perceptual quality of the output.