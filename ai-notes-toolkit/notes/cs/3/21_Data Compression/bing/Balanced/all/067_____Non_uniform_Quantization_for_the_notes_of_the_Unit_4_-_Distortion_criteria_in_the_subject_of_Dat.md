# Non uniform Quantization

- Non uniform quantization is a technique of data compression that assigns different step sizes to different input ranges.
- Non uniform quantization can reduce the distortion and improve the signal-to-noise ratio (SNR) for signals that have non-uniform probability distributions or non-linear characteristics.
- Non uniform quantization can be achieved by using companding, adaptive quantization, or non-linear mapping functions.
- Companding is a process of compressing the input signal before applying uniform quantization and expanding the output signal after decoding. Companding can be implemented by using logarithmic or power-law functions, such as the μ-law or A-law algorithms .
- Adaptive quantization is a process of adjusting the step size of the quantizer according to the local characteristics of the input signal, such as the variance or the amplitude. Adaptive quantization can be implemented by using feedback or feedforward mechanisms, such as the Lloyd-Max algorithm or the Jayant algorithm.
- Non-linear mapping functions are functions that map the input signal to a discrete set of output levels that are not equally spaced. Non-linear mapping functions can be designed by using optimization methods, such as the K-means algorithm or the gradient descent algorithm .