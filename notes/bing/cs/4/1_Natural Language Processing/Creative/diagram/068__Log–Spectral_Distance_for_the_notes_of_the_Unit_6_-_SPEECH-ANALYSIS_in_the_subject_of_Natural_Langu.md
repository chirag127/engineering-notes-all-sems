The log-spectral distance (LSD) is a distance measure between two spectra, usually expressed in decibels (dB). It is defined as the root mean square difference between the logarithms of the power spectra of two signals. It can be used to measure the distortion or similarity of two signals, such as speech signals.

The following diagram illustrates the basic steps of calculating the log-spectral distance between two speech signals:

```
+-----------------+     +-----------------+     +-----------------+
| Original speech |     | Quantized speech|     | Interpolated    |
| signal x(t)     |     | signal y(t)     |     | speech signal   |
|                 |     |                 |     | z(t)            |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Short-time      |     | Short-time      |     | Short-time      |
| Fourier         |     | Fourier         |     | Fourier         |
| transform       |     | transform       |     | transform       |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Power spectrum  |     | Power spectrum  |     | Power spectrum  |
| P(w)            |     | Q(w)            |     | R(w)            |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Logarithm       |     | Logarithm       |     | Logarithm       |
| 10*log10(P(w))  |     | 10*log10(Q(w))  |     | 10*log10(R(w))  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Difference      |     | Difference      |     | Difference      |
| 10*log10(P(w))  |     | 10*log10(Q(w))  |     | 10*log10(R(w))  |
| - 10*log10(Q(w))|     | - 10*log10(P(w))|     | - 10*log10(P(w))|
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Squaring        |     | Squaring        |     | Squaring        |
| [10*log10(P(w)) |     | [10*log10(Q(w)) |     | [10*log10(R(w)) |
| - 10*log10(Q(w))]^2   | - 10*log10(P(w))]^2   | - 10*log10(P(w))]^2
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                      |                      |
        |                      |                      |
        |                      |                      |
        |                      |                      |
        v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Integration     |     | Integration     |     | Integration     |
| 1/(2*pi) *      |     | 1/(2*pi) *      |     | 1/(2*pi) *      |
| integral of     |     | integral of     |     | integral of     |
| [10*log10(P(w)) |     | [10*log10(Q(w)) |     | [10*log10(R(w))