 Here is the content in markdown format for the topic - ### Wiener filtering for the notes of the Unit 3 - IMAGE RESTORATION in the subject of Image Processing:

### Wiener Filtering

- Wiener filtering is a statistical technique for filtering noisy images/signals.
- It is a minimum mean square error (MMSE) estimator i.e. it produces an estimate that minimizes the mean square error (MSE) between the desired noise-free signal and the estimated signal.
- The Wiener filter is a linear filter whose impulse response is inversely proportional to the power spectral density of the additive noise and proportional to the power spectral density of the original signal.
- The Wiener filter produces optimal estimates of a signal in the mean square sense but requires full knowledge of the power spectral densities of the signal and noise.
- The Wiener filter equation is given as:

$$H(u,v) = \frac{S_x(u,v)}{S_x(u,v) + S_n(u,v)} $$

Where $S_x(u,v)$ and $S_n(u,v)$ are the power spectral densities of the signal and noise respectively.
- The Wiener filter is a fast and memory efficient filter as it uses the FFT to implement the filtering in the frequency domain.
- However, it needs the knowledge of noise and signal power which can be difficult to obtain in practice. Hence, suboptimal filters like least mean squares are preferred in cases where sufficient a priori knowledge is not available.
- Advantages: Produces optimal estimate in mean square sense. Can remove noise and blurring simultaneously.
- Disadvantages: Requires knowledge of noise and signal power spectra which may not be readily available.
- Applications: Image deblurring, noise removal, speech processing, etc.