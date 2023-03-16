### Cepstral Distances

Cepstral analysis is a tool for investigating periodic structures in frequency spectra. It is the result of computing the inverse Fourier transform (IFT) of the logarithm of the estimated signal spectrum.

Cepstral analysis can be applied to detect local periodicity. For example, the Short-Time Fourier Transform (STFT) and corresponding spectra for a sequence of analysis windows in a speech signal can show a clear difference in harmonic structure. Frames 1-5 correspond to unvoiced speech.

In speech coding, basic vocoders were based mainly on the model description mentioned earlier, focused on efficient extraction from real speech of the best set of model parameters (also including voicing, fundamental frequency, and intensity) that better fit the actual speech in each analysis frame.

Cepstral analysis includes the calculation of the cepstral coefficients and the vector of quefrencies.

The present study of cepstral analysis of speech comes under this category. Speech is composed of excitation source and vocal tract system components. In order to analyze and model the excitation and system components of the speech independently and also use that in various speech processing applications, these two components have to be separated.