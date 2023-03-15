## Unit 5 - Advantages of Vector Quantization over Scalar Quantization

Vector Quantization (VQ) is a technique used in signal processing that allows the modeling of probability density functions by the distribution of prototype vectors. It has several advantages over Scalar Quantization (SQ), which is a simpler technique that quantizes a scalar value into a single value.

1. For a given rate, VQ results in a lower distortion than SQ.
2. If the source output is correlated, vectors of source output values will tend to fall in clusters.
3. Even if there is no dependency, VQ offers greater flexibility.
4. VQ can lower the average distortion with the number of reconstruction levels held constant, while SQ cannot.
5. VQ can reduce the number of reconstruction levels when distortion is held constant, while SQ cannot.
6. The most significant way VQ can improve performance over SQ is by exploiting the statistical dependence among scalars in the block.
7. VQ is also more effective than SQ when the source output values are not correlated.

However, like all things in life, quality comes with a price. For VQ, that price comes in the form of increased encoder complexity and codebook memory.