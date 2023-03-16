## Unit 5 - Introduction of Signal Processing

Signal processing is the science of analyzing, modifying, and synthesizing signals, such as sound, images, and biological measurements. Signal processing can be performed in analog or digital domains, using different techniques and tools.

### Classification of systems

A system is a mathematical model that describes how an input signal is transformed into an output signal. Systems can be classified according to different properties, such as:

- **Continuous** or **discrete**: A continuous system operates on continuous-time signals, while a discrete system operates on discrete-time signals.
- **Linear** or **nonlinear**: A linear system satisfies the superposition principle, which means that the output of the system for a linear combination of inputs is the same linear combination of the outputs for each input. A nonlinear system does not satisfy this property.
- **Causal** or **noncausal**: A causal system depends only on the present and past values of the input signal, while a noncausal system can also depend on the future values of the input signal.
- **Stable** or **unstable**: A stable system produces bounded outputs for bounded inputs, while an unstable system can produce unbounded outputs for bounded inputs.
- **Dynamic** or **static**: A dynamic system has memory, which means that the output of the system depends not only on the current input, but also on the previous inputs. A static system has no memory, which means that the output of the system depends only on the current input.
- **Recursive** or **nonrecursive**: A recursive system uses feedback, which means that the output of the system is fed back to the input through a delay element. A nonrecursive system does not use feedback.
- **Time-invariant** or **time-variant**: A time-invariant system does not change its behavior over time, which means that the output of the system for a given input is the same regardless of when the input is applied. A time-variant system changes its behavior over time, which means that the output of the system for a given input depends on when the input is applied.

### Classification of signals

A signal is a function that conveys information about a phenomenon. Signals can be classified according to different properties, such as:

- **Continuous** or **discrete**: A continuous signal is defined for all values of time, while a discrete signal is defined only for discrete values of time.
- **Energy** or **power**: An energy signal has finite energy, which means that the integral of the square of the signal over all time is finite. A power signal has finite power, which means that the average of the square of the signal over a finite interval of time is finite.
- **Mathematical representation of signals**: Signals can be represented in different ways, such as:

  - **Time domain**: The signal is expressed as a function of time, such as $x(t)$ for a continuous signal or $x[n]$ for a discrete signal.
  - **Frequency domain**: The signal is expressed as a function of frequency, such as $X(f)$ for a continuous signal or $X(e^{j\omega})$ for a discrete signal. The frequency domain representation can be obtained by applying a transform, such as the Fourier transform, to the time domain representation.
  - **Spectral density**: The spectral density is a measure of how the energy or power of a signal is distributed over different frequencies. The spectral density can be obtained by taking the magnitude squared of the frequency domain representation of the signal.

### Sampling techniques

Sampling is the process of converting a continuous signal into a discrete signal by taking samples of the signal at regular intervals of time. Sampling can be performed in different ways, such as:

- **Ideal sampling**: Ideal sampling is a theoretical model that assumes that the samples are taken instantaneously and without any distortion. Ideal sampling can be represented by multiplying the continuous signal by a train of impulses, such as $x_s(t) = x(t) \cdot \sum_{n=-\infty}^{\infty} \delta(t-nT_s)$, where $T_s$ is the sampling period.
- **Practical sampling**: Practical sampling is a realistic model that takes into account the limitations of real devices, such as the finite duration and shape of the sampling pulses, the noise and distortion introduced by the sampling circuit, and the aliasing effect caused by undersampling. Practical sampling can be modeled by