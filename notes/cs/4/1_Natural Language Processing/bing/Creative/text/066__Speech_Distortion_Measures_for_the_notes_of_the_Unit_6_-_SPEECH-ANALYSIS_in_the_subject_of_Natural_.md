### Speech Distortion Measures

- Speech distortion measures are quantitative methods to evaluate the quality or similarity of speech signals, especially in speech processing applications such as coding, enhancement, recognition, synthesis, etc.
- Speech distortion measures can be classified into two categories: waveform-based and spectral-based.
  - Waveform-based measures compare the original and processed speech signals in the time domain, such as mean squared error (MSE), signal-to-noise ratio (SNR), segmental SNR (SSNR), etc.
  - Spectral-based measures compare the original and processed speech signals in the frequency domain, such as log spectral distance (LSD), cepstral distance (CD), Itakura-Saito (IS) distance, etc.
- Spectral-based measures are more suitable for speech signals, as they can capture the perceptual and statistical properties of speech better than waveform-based measures.
- Spectral-based measures can be further divided into two types: linear and nonlinear.
  - Linear measures assume that the spectral distortion is additive and independent of the signal, such as LSD and CD.
  - Nonlinear measures assume that the spectral distortion is multiplicative and dependent on the signal, such as IS and normalized model distortion (NMD).
- Nonlinear measures have some advantages over linear measures, such as being more robust to noise, having a property similar to the triangle inequality, and yielding efficient computation algorithms for generalized centroids or minimum distortion points of speech frames.
- Speech distortion measures can be used for various purposes, such as evaluating the performance of speech processing systems, designing optimal quantizers or codebooks, clustering or classifying speech frames, etc.