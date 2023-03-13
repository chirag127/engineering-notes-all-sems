### Features for the notes of the Unit 6 - SPEECH-ANALYSIS in the subject of Natural Language Processing

- Speech analysis is the process of extracting information from speech signals, such as the speaker's identity, emotion, language, accent, etc.
- Speech analysis can be divided into two main tasks: speech recognition and speaker recognition.
- Speech recognition is the task of converting speech signals into text or commands, such as transcribing a voice message or controlling a smart device with voice commands.
- Speaker recognition is the task of identifying or verifying the speaker's identity from speech signals, such as unlocking a phone with voice biometrics or detecting impostors in a call center.
- Speech analysis relies on various features that capture the characteristics of speech signals, such as the frequency, amplitude, duration, pitch, intensity, etc.
- Some of the common features used for speech analysis are:

  - **Spectral features**: These features describe the frequency distribution of speech signals, such as the energy, spectrum, cepstrum, etc. They are often computed using Fourier transform or filter banks.
  - **Temporal features**: These features describe the time variation of speech signals, such as the zero-crossing rate, autocorrelation, etc. They are often computed using windowing or segmentation techniques.
  - **Prosodic features**: These features describe the suprasegmental aspects of speech, such as the pitch, intensity, duration, etc. They are often computed using pitch detection or intensity estimation algorithms.
  - **Formant features**: These features describe the resonant frequencies of the vocal tract, which are related to the vowel quality and the speaker's identity. They are often computed using linear predictive coding or peak picking methods.
  - **Mel-frequency cepstral coefficients (MFCCs)**: These features are derived from the spectral features, but they are more robust to noise and speaker variability. They are computed by applying a mel-scale filter bank, a logarithmic function, and a discrete cosine transform to the spectral features.
  - **Linear prediction coefficients (LPCs)**: These features are derived from the temporal features, but they are more efficient and compact. They are computed by applying a linear prediction model to the speech signal, which estimates the current sample as a linear combination of the previous samples.
  - **Perceptual linear prediction (PLP)**: These features are derived from the spectral features, but they are more perceptually relevant and invariant to speaker and channel differences. They are computed by applying a critical-band filter bank, an equal-loudness curve, an intensity-loudness power law, and a linear prediction model to the spectral features.
  - **Delta and delta-delta features**: These features are derived from the spectral, temporal, or prosodic features, but they capture the dynamic changes of speech signals over time. They are computed by taking the first and second derivatives of the original features.