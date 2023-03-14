The following diagram illustrates the basic architecture of a weighted cepstral distance and filtering system for speech analysis:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Speech input  +---->+  Cepstral      +---->+  Weighted      |
|                |     |  analysis      |     |  cepstral      |
+----------------+     +----------------+     |  distance      |
                                             |  measure       |
+----------------+     +----------------+     |                |
|                |     |                |     |                |
|  Reference     +---->+  Cepstral      +---->+                |
|  speech        |     |  analysis      |     +----------------+
|                |     |                |
+----------------+     +----------------+
```

The system consists of the following steps:

- The speech input and the reference speech are both analyzed using cepstral analysis, which is a technique that transforms the speech signal into a set of cepstral coefficients that represent the spectral envelope of the signal.
- The cepstral coefficients of the speech input and the reference speech are then compared using a weighted cepstral distance measure, which is a metric that assigns different weights to different cepstral coefficients according to their importance or variance. The weighted cepstral distance measure can be used to quantify the similarity or dissimilarity between two speech signals.
- The weighted cepstral distance measure can be used for various applications, such as speech recognition, speaker identification, or speech enhancement. Depending on the application, the system may also include a filtering step, which is a process that modifies the speech signal based on the weighted cepstral distance measure. For example, a perceptual weighting filter can be used to compensate for the spectral tilt of the speech signal, or a homomorphic filter can be used to separate the source and filter components of the speech signal.