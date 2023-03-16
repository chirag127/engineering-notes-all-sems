## Unit 5 - Introduction of Signal Processing

- Signal processing is the analysis, manipulation, and synthesis of signals, such as sound, images, and biological measurements.
- Signals can be classified into different types based on their characteristics, such as:

  - Continuous or discrete: A continuous signal is defined for every point in time, while a discrete signal is defined only at discrete points in time.
  - Energy or power: An energy signal has finite energy and zero average power, while a power signal has finite average power and infinite energy.
  - Linear or nonlinear: A linear signal is one that satisfies the superposition principle, which means that the output of a system is the sum of the outputs of the system for each input separately. A nonlinear signal is one that does not satisfy the superposition principle.
  - Causal or noncausal: A causal signal is one that depends only on the present and past values of the input, while a noncausal signal is one that depends on the future values of the input as well.
  - Stable or unstable: A stable signal is one that has bounded output for bounded input, while an unstable signal is one that has unbounded output for bounded input.
  - Dynamic or static: A dynamic signal is one that depends on the current and previous values of the input, while a static signal is one that depends only on the current value of the input.
  - Recursive or nonrecursive: A recursive signal is one that depends on the output of the system as well as the input, while a nonrecursive signal is one that depends only on the input.
  - Time-invariant or time-varying: A time-invariant signal is one that does not change its characteristics over time, while a time-varying signal is one that changes its characteristics over time.

- Mathematical representation of signals: Signals can be represented by mathematical functions, such as:

  - Sinusoidal signals: A sinusoidal signal is one that has the form $x(t) = A \cos(\omega t + \phi)$, where $A$ is the amplitude, $\omega$ is the angular frequency, and $\phi$ is the phase.
  - Exponential signals: An exponential signal is one that has the form $x(t) = Ae^{at}$, where $A$ and $a$ are constants.
  - Impulse signals: An impulse signal is one that has the form $x(t) = \delta(t)$, where $\delta(t)$ is the Dirac delta function, which is zero everywhere except at $t = 0$, where it is infinite.
  - Step signals: A step signal is one that has the form $x(t) = u(t)$, where $u(t)$ is the unit step function, which is zero for $t < 0$ and one for $t \geq 0$.
  - Ramp signals: A ramp signal is one that has the form $x(t) = tu(t)$, where $t$ is the time variable and $u(t)$ is the unit step function.
  - Periodic signals: A periodic signal is one that repeats itself after a fixed interval of time, called the period. The period can be expressed as $T = \frac{2\pi}{\omega}$, where $\omega$ is the angular frequency of the signal.

- Spectral density: The spectral density of a signal is a measure of how the energy or power of the signal is distributed over different frequencies. It can be computed by taking the Fourier transform of the signal, which converts the signal from the time domain to the frequency domain. The Fourier transform of a signal $x(t)$ is given by:

  - $X(\omega) = \int_{-\infty}^{\infty} x(t) e^{-j\omega t} dt$, for continuous signals.
  - $X(k) = \sum_{n = -\infty}^{\infty} x(n) e^{-j\frac{2\pi}{N} kn}$, for discrete signals.

- Sampling techniques: Sampling is the process of converting a continuous signal into a discrete signal by taking samples of the signal at regular intervals of time. The sampling frequency is the number of samples taken per second, and it is denoted by $f_s$. The sampling theorem states that a continuous signal can be perfectly reconstructed from its samples if the sampling frequency is at least twice the highest frequency component of the signal, which is called the Nyquist frequency. The Nyquist frequency is denoted by $f_N$, and it is given by $f_N = \frac{f_s}{2}$.

- Quantization: Quantization is the process of converting a continuous signal into a discrete signal by assigning each sample