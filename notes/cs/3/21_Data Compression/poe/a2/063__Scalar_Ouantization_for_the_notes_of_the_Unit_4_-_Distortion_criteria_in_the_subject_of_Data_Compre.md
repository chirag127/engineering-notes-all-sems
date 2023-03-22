 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Scalar Quantization for the notes of the Unit 4 - Distortion criteria

1.  Scalar quantization is the simplest form of quantization where the quantization regions are intervals on the real line and each interval is assigned a reconstruction level.
2.  The input to the quantizer is a scalar variable and the output is also a scalar.
3.  The quantization error is the difference between the original input and the quantizer output. The mean-squared error (MSE) is a common distortion measure to evaluate the performance of a quantizer.
4.  The goal is to choose the reconstruction levels and interval boundaries to minimize the MSE subject to a constraint on the number of intervals (and hence Reconstruction levels). This leads to the process of optimizing the Lloyd-Max quantizer.
5.  The steps to obtain the Lloyd-Max quantizer are:
    1.  Initialize the Reconstruction levels and interval boundaries arbitrarily
    2.  Determine the centroid (expected value) of the input probability density function over each interval. The centroids become the new reconstruction levels.
    3.  Determine the new interval boundaries as the midpoints between consecutive reconstruction levels.
    4.  Repeat steps 2 and 3 until the reconstruction levels and interval boundaries converge.
6.  The Lloyd-Max quantizer is an optimal quantizer that minimizes the MSE for a given number of intervals (and reconstruction levels). It forms the basis for the design of more complex quantizers.

How's this? I have written the points in a formal tone without any emojis or external links as you requested. Please let me know if you would like me to modify or add anything.