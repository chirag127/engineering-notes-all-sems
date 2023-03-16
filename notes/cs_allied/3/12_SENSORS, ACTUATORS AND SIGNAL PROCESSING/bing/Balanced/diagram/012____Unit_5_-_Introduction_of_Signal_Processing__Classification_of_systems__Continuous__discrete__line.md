## Unit 5 - Introduction of Signal Processing

Signal processing is the analysis, manipulation, and synthesis of signals, such as sound, images, and biological measurements.

### Classification of systems

A system is a set of components that interact to perform a function or achieve a goal. A system can be classified according to various criteria, such as:

- **Continuous** or **discrete**: A continuous system operates on continuous signals, which are defined for all values of time or space. A discrete system operates on discrete signals, which are defined only for certain values of time or space.
- **Linear** or **nonlinear**: A linear system satisfies the principle of superposition, which means that the output of the system for a sum of inputs is equal to the sum of outputs for each input. A nonlinear system does not satisfy this property.
- **Causal** or **noncausal**: A causal system depends only on the present and past values of the input, not on the future values. A noncausal system can depend on the future values of the input.
- **Stable** or **unstable**: A stable system produces bounded outputs for bounded inputs, meaning that the output does not grow indefinitely or oscillate wildly. An unstable system does not have this property.
- **Dynamic** or **static**: A dynamic system has memory, meaning that the output depends not only on the current input, but also on the previous inputs and outputs. A static system has no memory, meaning that the output depends only on the current input.
- **Recursive** or **nonrecursive**: A recursive system uses feedback, meaning that the output or a part of it is fed back to the input. A nonrecursive system does not use feedback.
- **Time-invariant** or **time-variant**: A time-invariant system does not change its behavior over time, meaning that the output for a given input is the same regardless of when the input is applied. A time-variant system changes its behavior over time, meaning that the output for a given input depends on when the input is applied.

### Classification of signals

A signal is a function that conveys information about a phenomenon. A signal can be classified according to various criteria, such as:

- **Continuous** or **discrete**: A continuous signal is defined for all values of time or space. A discrete signal is defined only for certain values of time or space.
- **Energy** or **power**: An energy signal has finite energy, meaning that the integral or sum of the square of the signal over time or space is finite. A power signal has finite power, meaning that the average of the square of the signal over time or space is finite.
- **Mathematical representation**: A signal can be represented in different ways, such as in the time domain, frequency domain, or other domains. The time domain representation shows how the signal varies over time or space. The frequency domain representation shows how the signal is composed of different frequency components. Other domains, such as the Laplace domain or the z-domain, are useful for analyzing certain types of systems or signals.

### Spectral density

The spectral density of a signal is a measure of how the power or energy of the signal is distributed over different frequency bands. The spectral density can be computed using the Fourier transform or other methods. The spectral density can be used to characterize the frequency content of a signal, to filter out unwanted noise or interference, or to perform spectral analysis.

### Sampling techniques

Sampling is the process of converting a continuous signal into a discrete signal by taking samples of the signal at regular intervals. Sampling can be done in different ways, such as:

- **Ideal sampling**: Ideal sampling involves multiplying the continuous signal by a train of impulses, which are very narrow and high pulses that occur at the sampling rate. Ideal sampling preserves all the information of the original signal, but it is not practical to implement in reality.
- **Natural sampling**: Natural sampling involves multiplying the continuous signal by a train of pulses, which are finite in width and height and occur at the sampling rate. Natural sampling approximates ideal sampling, but it introduces some distortion in the signal due to the finite width of the pulses.
- **Flat-top sampling**: Flat-top sampling involves holding the value of the continuous signal constant for the duration of each pulse. Flat-top sampling simplifies the implementation of natural sampling, but it introduces more distortion in the signal due to the discontinuities at the edges of the pulses.

### Quantization

Quantization is the process of converting a continuous signal or a discrete signal with infinite precision into a discrete signal with finite precision by assigning each sample to one of a finite number of levels. Quantization can be done in different ways, such as:

- **Uniform quantization**: Uniform quantization involves dividing the range of the signal