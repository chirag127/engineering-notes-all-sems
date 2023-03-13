According to the search results, likelihood distortions are measures of the spectral distance between two short-time spectra, which are often used in speech recognition systems. One of the most common likelihood distortion measures is the log likelihood ratio (LLR), which is defined as the negative logarithm of the ratio of the probability densities of the two spectra. The LLR can be computed as follows:

LLR = -log(p(x|y)/p(x))

where x and y are the two spectra, and p(x|y) and p(x) are their probability densities.

The following diagram illustrates the basic architecture of a speech recognition system that uses likelihood distortions to compare the input speech signal with a set of reference templates:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Input speech  |---->|  Feature       |---->|  Template      |
|                |     |  extraction    |     |  matching      |
+----------------+     +----------------+     +----------------+
                                         |     |
                                         |     |
                                         |     v
                                         |  +----------------+
                                         |  |                |
                                         +->|  Likelihood    |
                                            |  distortions   |
                                            |                |
                                            +----------------+
                                                  |
                                                  |
                                                  v
                                            +----------------+
                                            |                |
                                            |  Recognition   |
                                            |  output       |
                                            |                |
                                            +----------------+
```