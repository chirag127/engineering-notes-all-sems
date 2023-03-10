 Here is the content in markdown format for the topic -

### Uniform Quantizer

A uniform quantizer divides the input range into equal-sized intervals and maps each interval to a single representative value (reconstruction level).

- The input range is divided into 2^n intervals of equal size where n is the number of bits used to represent the quantized values. For e.g. if n=3, the input range is divided into 8 equal intervals.
- The representative value for each interval is the midpoint of the interval.
- Advantages: Simple to implement and analyze. Minimizes the maximum quantization error.
- Disadvantages: Poor efficiency (large granularity). The quantization error is not uniformly distributed across the input range.

Example:

- Input range: [0, 10]
- n = 2 (2 bits to represent quantized value)
- Division into equal intervals: [0, 5), [5, 10]
- Representative values (Reconstruction levels): 2.5, 7.5

If input is 3.2 -> Quantized value is 2
If input is 7 -> Quantized value is 7

Applications: Used in signal processing and compression of dynamic range when high precision is not required.

This is written in markdown format with points and includes examples and applications. Let me know if you would like me to elaborate on any of the points or add more details.