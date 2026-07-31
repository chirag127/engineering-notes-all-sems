### Filter Bank and LPC Methods for Speech Processing

- Speech processing is the study of how humans produce, perceive, and understand speech, and how to design machines that can perform these tasks.
- Speech processing involves various stages, such as speech analysis, speech synthesis, speech recognition, speech enhancement, speech coding, and speech translation.
- Speech analysis is the process of extracting features or parameters from the speech signal that represent its characteristics, such as pitch, energy, spectrum, and formants.
- Speech synthesis is the process of generating speech from text or other symbolic representations, such as phonetic symbols, prosodic features, or articulatory gestures.
- Speech recognition is the process of converting speech into text or other symbolic representations, such as commands, keywords, or semantic meanings.
- Speech enhancement is the process of improving the quality of speech by reducing noise, reverberation, or distortion.
- Speech coding is the process of compressing speech for efficient transmission or storage, while preserving its intelligibility and naturalness.
- Speech translation is the process of converting speech from one language to another, while preserving its meaning and style.

- Filter bank and LPC methods are two common techniques for speech analysis and speech coding, which are based on different models of speech production.
- Filter bank methods assume that speech is produced by a source-filter model, where the source is either a periodic pulse train (for voiced sounds) or a random noise (for unvoiced sounds), and the filter is a time-varying vocal tract that shapes the spectrum of the source.
- Filter bank methods use a bank of band-pass filters to divide the speech signal into frequency bands, and compute the energy or amplitude of each band. The filter bank can be designed to mimic the frequency response of the human auditory system, such as the mel-scale or the bark-scale.
- Filter bank methods can also apply a discrete cosine transform (DCT) or a discrete Fourier transform (DFT) to the filter bank outputs, to obtain a compact and decorrelated representation of the speech spectrum, such as the mel-frequency cepstral coefficients (MFCC) or the perceptual linear prediction (PLP) coefficients.
- Filter bank methods are widely used for speech recognition, speech enhancement, and speech synthesis, as they capture the perceptual and acoustic features of speech.
- LPC methods assume that speech is produced by an all-pole model, where the speech signal is approximated as a linear combination of past samples, and the coefficients of the linear combination are called the linear prediction coefficients (LPC).
- LPC methods use an autocorrelation method or a covariance method to estimate the LPC from the speech signal, and use a Levinson-Durbin recursion or a lattice filter to compute the reflection coefficients or the prediction error filter from the LPC.
- LPC methods can also apply a cepstral analysis or a line spectral frequency (LSF) analysis to the LPC, to obtain a compact and robust representation of the speech spectrum, such as the LPC cepstral coefficients or the LSF coefficients.
- LPC methods are widely used for speech coding, speech synthesis, and speech enhancement, as they capture the spectral envelope and the pitch of speech.