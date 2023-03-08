 Here is the content in markdown format for the topic ### DFT, DCT for the notes of the Unit 1 - DIGITAL IMAGE FUNDAMENTALS in the subject of Image Processing:

### Discrete Fourier Transform (DFT)
- DFT is a technique to analyze the frequency components of a digital signal.
- It converts a signal from its original domain (often time or space) to the frequency domain.
- The frequency domain representation contains the amplitude and phase information of each frequency component in the signal.
- The DFT is denoted by X(k), where k is the frequency index. The DFT of a sequence x(n) is given by:

X(k) = ∑n=0N−1x(n)e−j2πkn/N

Where N is the length of the sequence.
- The inverse DFT can be used to convert back to the original domain and is given by:

x(n) = 1/N ∑k=0N−1X(k)e j2πkn/N

- Some applications of DFT are: filtering, modulation, convolution, spectra analysis, etc.

### Discrete Cosine Transform (DCT)
- DCT is a Fourier-related transform similar to DFT but uses only real numbers.
- It converts a signal from the spatial domain to the frequency domain. The basis functions for DCT are cosine functions oscillating at different frequencies.
- DCT is widely used in image/video compression techniques like JPEG, MPEG, etc. as it has a strong "energy compaction" property. It clusters most of the signal information into a few low-frequency components.
- The DCT transforms a sequence x(n) to X(k) and is given by:

X(k) = 2N∑n=0N−1x(n)cos[π(2n+1)k/2N]

- The inverse DCT can be used to get back the original sequence and is given by:

x(n) = 2N∑k=0N−1X(k)cos[π(2k+1)n/2N]

- Some advantages of DCT over DFT are: it only uses real values, it is faster to compute, and it has greater compression capability.