### Filter Bank and LPC Methods for Speech Processing

- Filter bank and LPC methods are two common techniques for feature extraction in speech processing, especially for speech recognition.
- Feature extraction is the process of transforming the speech signal into a compact and meaningful representation that captures the relevant information for the task.
- Filter bank methods are based on dividing the frequency spectrum of the speech signal into a number of sub-bands, and computing the energy or power of each sub-band. The resulting features are called filter bank coefficients or spectral coefficients.
- LPC methods are based on modeling the speech signal as the output of a linear system with a source and a filter. The source represents the excitation of the vocal tract, and the filter represents the shape and resonance of the vocal tract. The resulting features are called LPC coefficients or cepstral coefficients.
- Filter bank methods and LPC methods have different advantages and disadvantages for speech processing. Filter bank methods are more robust to noise and channel distortion, but less efficient in capturing the spectral envelope of the speech signal. LPC methods are more efficient in capturing the spectral envelope, but more sensitive to noise and channel distortion.
- Some examples of filter bank methods are mel-frequency cepstral coefficients (MFCC), perceptual linear prediction (PLP), and filter bank energies (FBE). Some examples of LPC methods are linear predictive coding (LPC), LPC cepstrum, and LPC residual.
- The following table summarizes the main steps and differences between filter bank methods and LPC methods for feature extraction:

| Filter Bank Methods | LPC Methods |
|---------------------|-------------|
| 1. Pre-emphasize the speech signal to boost the high frequencies. | 1. Pre-emphasize the speech signal to boost the high frequencies. |
| 2. Divide the speech signal into frames of fixed length, typically 20-30 ms, with some overlap. | 2. Divide the speech signal into frames of fixed length, typically 20-30 ms, with some overlap. |
| 3. Apply a window function, such as Hamming or Hanning, to each frame to reduce the discontinuities at the edges. | 3. Apply a window function, such as Hamming or Hanning, to each frame to reduce the discontinuities at the edges. |
| 4. Compute the discrete Fourier transform (DFT) of each frame to obtain the frequency spectrum. | 4. Compute the autocorrelation function of each frame to obtain the correlation coefficients. |
| 5. Apply a filter bank, such as triangular or mel-scaled, to the frequency spectrum to obtain the filter bank coefficients. | 5. Apply the Levinson-Durbin algorithm to the correlation coefficients to obtain the LPC coefficients. |
| 6. Optionally, apply a logarithm or a discrete cosine transform (DCT) to the filter bank coefficients to obtain the cepstral coefficients. | 6. Optionally, apply a logarithm or a DCT to the LPC coefficients to obtain the LPC cepstral coefficients. |
| 7. Optionally, apply a liftering or a cepstral mean normalization (CMN) to the cepstral coefficients to enhance or normalize the features. | 7. Optionally, apply a liftering or a CMN to the LPC cepstral coefficients to enhance or normalize the features. |
| 8. Optionally, compute the first and second derivatives of the features to capture the dynamic information. | 8. Optionally, compute the first and second derivatives of the features to capture the dynamic information. |
| 9. Optionally, compute the LPC residual by inverse filtering the speech signal with the LPC filter. | 9. Optionally, compute the LPC residual by inverse filtering the speech signal with the LPC filter. |