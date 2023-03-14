Filter Bank and LPC Methods are two techniques for feature extraction in speech processing. They both aim to represent the spectral envelope of a speech signal in a compressed form, using the information of a linear predictive model. However, they differ in the way they compute the linear prediction coefficients and the cepstral coefficients.

Filter Bank Method:

The Filter Bank Method is based on the idea of dividing the frequency spectrum of a speech signal into several sub-bands, and computing the energy in each sub-band. The sub-bands are usually spaced according to the mel scale, which is a perceptual scale of pitches that is roughly linear below 1 kHz and logarithmic above 1 kHz. The energy in each sub-band is then converted to a logarithmic scale, and a discrete cosine transform (DCT) is applied to obtain the cepstral coefficients. The cepstral coefficients are a compact representation of the spectral envelope, and they are also decorrelated, which means they have low redundancy and are suitable for statistical modeling. The Filter Bank Method is also known as the Mel-Frequency Cepstral Coefficients (MFCC) Method, and it is the most widely used technique in speech recognition and synthesis.

The following diagram illustrates the basic architecture of the Filter Bank Method:

```
Speech Signal --> Pre-emphasis --> Framing --> Windowing --> FFT --> Mel Filter Bank --> Log --> DCT --> Cepstral Coefficients
```

LPC Method:

The LPC Method is based on the idea of modeling the speech signal as the output of a linear filter driven by a source signal. The source signal can be either a periodic pulse train (for voiced sounds) or a white noise (for unvoiced sounds). The linear filter represents the vocal tract, which shapes the source signal into speech sounds. The LPC Method estimates the coefficients of the linear filter by minimizing the prediction error, which is the difference between the actual speech signal and the predicted speech signal. The prediction error is also known as the residual signal, and it contains information about the source signal. The LPC coefficients are then converted to the cepstral coefficients by applying a logarithm and an inverse Fourier transform (IFT). The cepstral coefficients are a compact representation of the spectral envelope, and they are also decorrelated, but they are less robust to noise and channel distortion than the Filter Bank Method.

The following diagram illustrates the basic architecture of the LPC Method:

```
Speech Signal --> Pre-emphasis --> Framing --> Windowing --> LPC Analysis --> LPC Coefficients --> Log --> IFT --> Cepstral Coefficients
```