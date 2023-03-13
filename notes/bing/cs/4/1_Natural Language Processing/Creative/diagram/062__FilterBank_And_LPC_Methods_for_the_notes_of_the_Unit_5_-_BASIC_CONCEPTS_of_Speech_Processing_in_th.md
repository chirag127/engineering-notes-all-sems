Filter Bank and LPC methods are two different techniques for feature extraction in speech processing. Filter Bank methods divide the speech signal into frequency bands and compute the energy or power spectrum of each band. LPC methods model the speech signal as a linear combination of past samples and estimate the coefficients of the linear predictor.

The following diagram illustrates the basic architecture of a Filter Bank method:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Pre-emphasis   |     |  Framing and    |     |  Windowing      |
|                 |     |  Overlapping    |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  FFT            |     |  Filter Bank    |     |  Logarithm      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  DCT            |     |  Cepstral       |     |  Delta and      |
|                 |     |  Liftering      |     |  Delta-Delta    |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +---------------------->|                       |
                                |                       |
                                |                       |
                                |                       |
                                |                       |
                                |                       |
                                |                       |
                                v                       v
+-----------------+     +-----------------+
|                 |     |                 |
|  Feature        |     |  Recognition    |
|  Vector         |     |  System         |
|                 |     |                 |
+-----------------+     +-----------------+
```

The following diagram illustrates the basic architecture of a LPC method:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Pre-emphasis   |     |  Framing and    |     |  Windowing      |
|                 |     |  Overlapping    |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        v                       v                       v
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  LPC Analysis   |     |  LPC Synthesis  |     |  LPC Error      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        |                       |                       |
        +---------------------->|                       |
                                |                       |
                                |                       |
                                |                       |
                                |                       |
                                |                       |
                                |                       |
                                v                       v
+-----------------+     +-----------------+
|                 |     |                 |
|  Feature        |