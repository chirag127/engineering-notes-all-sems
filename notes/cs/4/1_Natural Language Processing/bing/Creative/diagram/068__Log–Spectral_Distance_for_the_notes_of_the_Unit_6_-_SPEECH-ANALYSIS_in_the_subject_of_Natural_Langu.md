The log-spectral distance (LSD) is a measure of the difference between two power spectra, usually in the context of speech coding or enhancement. It is defined as the root mean square of the logarithmic difference between the spectra, and can be expressed in decibels (dB). The LSD is symmetric and can be seen as a special case of the p-norm distance with p=2 and a logarithmic scale. The LSD can also be related to the cepstral distance by Parseval's theorem.

The following diagram illustrates the basic steps of computing the LSD between two spectra P and Q:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  P(w)         |     |  Q(w)         |     |  P(w)/Q(w)    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  log(P(w))    |     |  log(Q(w))    |     |  log(P(w)/Q(w))|
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  log(P(w))    |     |  log(Q(w))    |     |  log(P(w)) -   |
|                |     |                |     |  log(Q(w))     |
+----------------+     +----------------+     +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  log(P(w))    |     |  log(Q(w))    |     |  [log(P(w)) -  |
|                |     |                |     |  log(Q(w))]^2  |
+----------------+     +----------------+     +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  10*log(P(w)) |     |  10*log(Q(w)) |     |  10*[log(P(w)) -|
|                |     |                |     |  log(Q(w))]^2  |
+----------------+     +----------------+     +----------------+
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         |                     |                     |
         v                     v                     v
+----------------+     +----------------+     +----------------+
|                |     |                |     |