### Non-uniform Quantization

Non-uniform quantization is a type of quantization used in data compression where the quantization levels are not equally spaced. This is in contrast to uniform quantization, where the quantization levels are equally spaced.

In non-uniform quantization, the quantization levels are designed to match the statistical distribution of the input signal. This means that the quantization levels are more closely spaced in regions where the input signal is more likely to occur, and more widely spaced in regions where the input signal is less likely to occur.

The advantage of non-uniform quantization is that it can provide a lower distortion for a given number of quantization levels, compared to uniform quantization. This is because the quantization levels are more closely matched to the input signal, which reduces the quantization error.

Non-uniform quantization is commonly used in speech and audio coding, where the input signal has a non-uniform distribution. For example, the human ear is more sensitive to sounds in the mid-frequency range, so the quantization levels in this range are more closely spaced.

There are several methods for designing non-uniform quantizers, including the Lloyd-Max algorithm and the companding method. These methods aim to minimize the distortion by optimizing the placement of the quantization levels.

In summary, non-uniform quantization is a type of quantization used in data compression where the quantization levels are not equally spaced. It is designed to match the statistical distribution of the input signal, which can provide a lower distortion for a given number of quantization levels. Non-uniform quantization is commonly used in speech and audio coding, and there are several methods for designing non-uniform quantizers.