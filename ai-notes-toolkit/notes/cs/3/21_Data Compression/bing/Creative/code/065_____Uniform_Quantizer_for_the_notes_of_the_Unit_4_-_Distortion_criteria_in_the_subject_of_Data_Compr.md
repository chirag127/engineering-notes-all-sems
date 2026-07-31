# Uniform Quantizer for the notes of the Unit 4 - Distortion criteria in the subject of Data Compression

- A uniform quantizer is a type of scalar quantizer that maps a continuous range of input values into a finite set of output levels with equal spacing .
- A uniform quantizer can be characterized by its step size Δ, which is the distance between two adjacent output levels .
- A uniform quantizer can be classified into two types: mid-tread and mid-rise.
  - A mid-tread quantizer has a zero output level and the output levels are symmetric around zero. It is also called a symmetric uniform quantizer.
  - A mid-rise quantizer does not have a zero output level and the output levels are asymmetric around zero. It is also called an asymmetric uniform quantizer.
- A uniform quantizer can be used for data compression by reducing the number of bits required to represent the input values  .
  - A uniform quantizer can be combined with an entropy encoder to further compress the output levels by exploiting their statistical properties .
  - A uniform quantizer can also be incorporated into a deep learning based image compression framework, where the quantizer is applied to the feature maps between the encoder and decoder .
- A uniform quantizer has some advantages and disadvantages for data compression .
  - Advantages:
    - It is simple to implement and analyze .
    - It has a constant signal-to-quantization-noise ratio (SQNR) for any input distribution .
    - It performs well at high bit rates, where the quantization error is small compared to the input signal .
  - Disadvantages:
    - It is not optimal for non-uniform input distributions, where some input values are more likely than others .
    - It suffers from granular noise at low bit rates, where the quantization error is large compared to the input signal .
    - It introduces distortion that is independent of the input signal, which may be perceptually annoying for some applications .