LPC is a method used mostly in audio signal processing and speech processing for representing the spectral envelope of a digital signal of speech in compressed form, using the information of a linear predictive model. LPC analyzes the speech signal by estimating the formants, removing their effects from the speech signal, and estimating the intensity and frequency of the remaining buzz. The process of removing the formants is called inverse filtering, and the remaining signal after the subtraction of the filtered modeled signal is called the residue.

The following diagram illustrates the basic architecture of a LPC system for speech analysis and synthesis using ASCII characters:

```
+----------------+     +----------------+     +----------------+
| Speech signal  |---->| Pre-emphasis   |---->| Windowing      |
+----------------+     +----------------+     +----------------+
                                                   |
                                                   V
+----------------+     +----------------+     +----------------+
| Residual       |<----| Synthesis      |<----| LPC            |
| signal         |     | filter         |     | coefficients   |
+----------------+     +----------------+     +----------------+
                                                   |
                                                   V
+----------------+     +----------------+     +----------------+
| Reconstructed  |<----| De-emphasis    |<----| Analysis       |
| speech signal  |     | filter         |     | filter         |
+----------------+     +----------------+     +----------------+
```