LPC is a technique for representing the spectral envelope of a speech signal in a compressed form, using a linear predictive model . LPC analyzes the speech signal by estimating the formants, removing their effects from the speech signal, and estimating the intensity and frequency of the remaining buzz. The process of removing the formants is called inverse filtering, and the remaining signal after the subtraction of the filtered modeled signal is called the residue.

The following diagram illustrates the basic architecture of a LPC system for speech analysis and synthesis:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Speech Input  +---->+  LPC Analysis  +---->+  LPC Synthesis +---->+  Speech Output  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
                          |       |
                          |       |
                          |       v
                          |  +---------+
                          |  |         |
                          +->+ Residue |
                             |         |
                             +---------+
```

The LPC analysis block takes the speech input and computes the reflection coefficients, which are used to model the spectral envelope of the speech signal. The LPC synthesis block takes the reflection coefficients and the residue and reconstructs the speech signal by applying the inverse filter. The residue is the difference between the original speech signal and the filtered modeled signal, and it contains the information about the pitch and the intensity of the speech signal.