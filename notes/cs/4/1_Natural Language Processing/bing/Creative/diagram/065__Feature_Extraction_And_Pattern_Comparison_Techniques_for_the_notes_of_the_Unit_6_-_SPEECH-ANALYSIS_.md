The following diagram illustrates the basic architecture of a feature extraction and pattern comparison technique for speech analysis:

```
+----------------+     +-----------------+     +-----------------+
| Speech signal  | --> | Feature         | --> | Pattern         |
|                |     | extraction      |     | comparison      |
|                |     | (e.g. MFCC, LPC)|     | (e.g. DTW, HMM) |
+----------------+     +-----------------+     +-----------------+
```

The feature extraction stage transforms the speech signal into a sequence of feature vectors that represent the acoustic characteristics of the speech. The feature extraction methods can be classified into temporal or spectral analysis, depending on whether they use the speech waveform or its spectral representation. Some of the common feature extraction methods are MFCC, LPC, RASTA, PLP, etc.  

The pattern comparison stage compares the feature vectors with a set of reference patterns that correspond to different speech units, such as phonemes, words, or sentences. The pattern comparison methods can be classified into template-based or model-based, depending on whether they use a direct or a probabilistic representation of the reference patterns. Some of the common pattern comparison methods are DTW, HMM, SVM, etc.  

The output of the pattern comparison stage is a measure of similarity or a score that indicates how well the feature vectors match the reference patterns. The score can be used to perform speech recognition, speaker identification, or other speech-related tasks.