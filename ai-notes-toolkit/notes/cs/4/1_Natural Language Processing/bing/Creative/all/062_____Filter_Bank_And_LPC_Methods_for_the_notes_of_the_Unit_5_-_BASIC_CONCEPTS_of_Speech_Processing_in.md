# Filter Bank And LPC Methods

## Filter Bank Methods

- Filter bank methods are based on the idea of dividing the frequency spectrum of a speech signal into several sub-bands and computing the energy or power of each sub-band.
- Filter bank methods are motivated by the fact that the human auditory system is more sensitive to some frequency regions than others, and that speech information is not uniformly distributed across the spectrum.
- Filter bank methods can be implemented using different types of filters, such as rectangular, triangular, or mel-scaled filters. The most common filter bank method is the mel-frequency cepstral coefficients (MFCC) method, which uses a mel-scaled filter bank and a discrete cosine transform (DCT) to obtain cepstral coefficients.
- Filter bank methods are widely used for feature extraction in speech recognition, speaker recognition, and speech enhancement applications.

## LPC Methods

- LPC methods are based on the idea of modeling the speech signal as the output of a linear system driven by an excitation source. The linear system is represented by a set of coefficients that capture the spectral envelope of the speech signal, and the excitation source is either a periodic pulse train (for voiced speech) or a white noise (for unvoiced speech).
- LPC methods are motivated by the fact that the speech signal can be approximated by a source-filter model, where the source is the vocal cords and the filter is the vocal tract. The LPC coefficients can be interpreted as the parameters of the vocal tract filter, and the excitation source can be interpreted as the glottal waveform or the airflow.
- LPC methods can be implemented using different techniques, such as autocorrelation, covariance, lattice, inverse filtering, or maximum likelihood methods. The most common LPC method is the autocorrelation method, which uses the Levinson-Durbin algorithm to obtain the LPC coefficients from the autocorrelation function of the speech signal.
- LPC methods are widely used for speech analysis, synthesis, coding, and enhancement applications.