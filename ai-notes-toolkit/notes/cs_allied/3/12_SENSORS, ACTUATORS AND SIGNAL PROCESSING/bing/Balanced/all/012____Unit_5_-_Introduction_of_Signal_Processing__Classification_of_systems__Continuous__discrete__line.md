## Unit 5 - Introduction of Signal Processing

- Signal processing is the analysis, manipulation, and synthesis of signals, such as sound, images, and biological measurements.
- Signals can be classified into different types based on their properties and characteristics.
- Systems are the devices or processes that perform signal processing operations on signals.

### Classification of systems

- Systems can be classified into different types based on their properties and characteristics.
- Some of the common types of systems are:

  - Continuous systems: Systems that operate on continuous signals, which are defined for all values of time.
  - Discrete systems: Systems that operate on discrete signals, which are defined only for discrete values of time.
  - Linear systems: Systems that satisfy the principle of superposition, which means that the output of the system for a linear combination of inputs is equal to the linear combination of the outputs for each input.
  - Causal systems: Systems that depend only on the present and past values of the input, not on the future values.
  - Stable systems: Systems that produce bounded outputs for bounded inputs, which means that the output does not grow indefinitely as the input varies.
  - Dynamic systems: Systems that have memory, which means that the output depends not only on the current input but also on the previous inputs and outputs.
  - Recursive systems: Systems that use feedback, which means that the output is fed back to the input through a delay or a filter.
  - Time-invariant systems: Systems that do not change with time, which means that the output does not depend on when the input is applied.

### Classification of signals

- Signals can be classified into different types based on their properties and characteristics.
- Some of the common types of signals are:

  - Continuous signals: Signals that are defined for all values of time, such as analog signals.
  - Discrete signals: Signals that are defined only for discrete values of time, such as digital signals.
  - Energy signals: Signals that have finite energy, which means that the integral of the square of the signal over all time is finite.
  - Power signals: Signals that have finite power, which means that the average of the square of the signal over a finite time interval is finite.
  - Periodic signals: Signals that repeat themselves after a fixed interval of time, such as sinusoidal signals.
  - Aperiodic signals: Signals that do not repeat themselves after a fixed interval of time, such as random signals.

### Mathematical representation of signals

- Signals can be represented mathematically using different functions, such as:

  - Impulse function: A function that is zero everywhere except at a single point, where it is infinite, and has a unit area under the curve.
  - Step function: A function that is zero for negative values of time and one for positive values of time.
  - Ramp function: A function that is zero for negative values of time and increases linearly with time for positive values of time.
  - Exponential function: A function that has the form $a^t$, where $a$ is a constant.
  - Sinusoidal function: A function that has the form $A \sin(\omega t + \phi)$, where $A$ is the amplitude, $\omega$ is the angular frequency, and $\phi$ is the phase.

### Spectral density

- Spectral density is a measure of how the energy or power of a signal is distributed over different frequencies.
- Spectral density can be computed using the Fourier transform, which converts a signal from the time domain to the frequency domain.
- The Fourier transform of a continuous signal $x(t)$ is given by:

  $$X(f) = \int_{-\infty}^{\infty} x(t) e^{-j 2 \pi f t} dt$$

- The Fourier transform of a discrete signal $x[n]$ is given by:

  $$X(e^{j \omega}) = \sum_{n = -\infty}^{\infty} x[n] e^{-j \omega n}$$

- The spectral density of a signal can be obtained by taking the magnitude squared of the Fourier transform, which is also called the power spectrum.
- The spectral density of a signal can be used to analyze the frequency content of the signal, such as the bandwidth, the dominant frequency, and the noise level.

### Sampling techniques

- Sampling is the process of converting a continuous signal into a discrete signal by taking samples of the signal at regular intervals of time.
- Sampling can be done using different techniques, such as:

  - Ideal sampling: A technique that uses an ideal impulse train to multiply the continuous signal and obtain the discrete signal.
  - Natural sampling: A technique that uses a natural pulse train to multiply the continuous signal