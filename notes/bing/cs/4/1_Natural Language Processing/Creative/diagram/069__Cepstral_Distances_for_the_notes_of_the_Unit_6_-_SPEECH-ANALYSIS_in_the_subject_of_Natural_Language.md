Cepstral analysis is a technique for extracting information from speech signals by transforming them into the cepstral domain. The cepstrum is the inverse Fourier transform of the logarithm of the magnitude spectrum of a signal. It can be used to separate the excitation source and the vocal tract system components of speech, and to measure the similarity between different speech signals using cepstral distances.

A cepstral distance is a measure of how different two speech signals are in terms of their cepstral coefficients. Cepstral coefficients are the values of the cepstrum at different quefrencies, which are analogous to frequencies in the spectral domain. The lower quefrencies correspond to the vocal tract system, and the higher quefrencies correspond to the excitation source. A cepstral distance can be computed by taking the Euclidean distance, the Mahalanobis distance, or the Kullback-Leibler divergence between the cepstral coefficients of two speech signals.

The following diagram illustrates the basic steps of cepstral analysis and cepstral distance computation for speech signals:

```
+----------------+    +----------------+    +----------------+    +----------------+
| Speech signal  |    | Magnitude      |    | Logarithm      |    | Inverse Fourier|
| x(t)           | -> | spectrum       | -> |                | -> | transform      | -> Cepstrum c(n)
|                |    | |X(f)|         |    | log(|X(f)|)    |    |                |
+----------------+    +----------------+    +----------------+    +----------------+

+----------------+    +----------------+    +----------------+    +----------------+
| Speech signal  |    | Magnitude      |    | Logarithm      |    | Inverse Fourier|
| y(t)           | -> | spectrum       | -> |                | -> | transform      | -> Cepstrum d(n)
|                |    | |Y(f)|         |    | log(|Y(f)|)    |    |                |
+----------------+    +----------------+    +----------------+    +----------------+

+----------------+    +----------------+
| Cepstral       |    | Cepstral       |
| coefficients   |    | distance       |
| c(n) and d(n)  | -> | D(c, d)        |
|                |    |                |
+----------------+    +----------------+
```