# Filter Bank And LPC Methods

Filter bank and LPC methods are two techniques for analyzing and synthesizing speech signals. They are based on different models of how speech is produced and perceived.

## Filter Bank Methods

Filter bank methods are based on the idea that speech is composed of different frequency components that can be separated by a set of filters. Each filter passes a narrow band of frequencies and attenuates the others. The output of each filter is called a subband signal, and the set of subband signals is called a filter bank.

Filter bank methods can be used for both speech analysis and synthesis. For speech analysis, the filter bank is applied to the input speech signal and the subband signals are extracted. The subband signals can be further processed to obtain features such as the mel-frequency cepstral coefficients (MFCCs), which are widely used for speech recognition. MFCCs are obtained by applying a discrete cosine transform (DCT) to the logarithm of the subband energies.

For speech synthesis, the filter bank is applied in reverse. The subband signals are generated from the features and then combined to form the output speech signal. This can be done by using a simple filter that equalizes the variance of the cepstral coefficients, as proposed by Ravindran and Demiroglu.

## LPC Methods

LPC methods are based on the idea that speech is produced by a source-filter model. The source is the vocal cords, which produce a periodic signal (buzz) for voiced sounds or a random signal (hiss) for unvoiced sounds. The filter is the vocal tract, which shapes the source signal by resonating at certain frequencies called formants.

LPC methods can also be used for both speech analysis and synthesis. For speech analysis, the LPC method estimates the formants and the source signal from the input speech signal. This can be done by using various algorithms, such as the autocorrelation method, the covariance method, the lattice method, or the inverse filter formulation. The output of the LPC analysis is a set of coefficients that represent the filter and a residual signal that represents the source.

For speech synthesis, the LPC method reverses the process. The source signal is generated from the residual signal and the filter is generated from the coefficients. The source signal is then passed through the filter to produce the output speech signal.