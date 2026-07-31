# Unit 5 - Introduction of Signal Processing

## Classification of systems

- A system is a set of components that interact to perform a function or achieve a goal.
- A system can be classified according to different criteria, such as:

  - **Continuous or discrete**: A system is continuous if it operates on continuous signals, which are defined for all values of time. A system is discrete if it operates on discrete signals, which are defined only for discrete values of time.
  - **Linear or nonlinear**: A system is linear if it satisfies the principle of superposition, which means that the output of the system for a linear combination of inputs is equal to the same linear combination of the outputs for each input. A system is nonlinear if it does not satisfy this property.
  - **Causal or noncausal**: A system is causal if the output of the system at any time depends only on the input of the system up to that time. A system is noncausal if the output of the system at any time depends on the input of the system in the future.
  - **Stable or unstable**: A system is stable if the output of the system remains bounded for any bounded input. A system is unstable if the output of the system becomes unbounded for some bounded input.
  - **Dynamic or static**: A system is dynamic if the output of the system at any time depends on the input of the system and the state of the system at that time. A system is static if the output of the system at any time depends only on the input of the system at that time.
  - **Recursive or nonrecursive**: A system is recursive if the output of the system at any time depends on the input of the system and the output of the system at previous times. A system is nonrecursive if the output of the system at any time depends only on the input of the system at that time.
  - **Time-invariant or time-varying**: A system is time-invariant if the output of the system for a given input does not change when the input is shifted in time. A system is time-varying if the output of the system for a given input changes when the input is shifted in time.

## Classification of signals

- A signal is a function that conveys information about a phenomenon or a system.
- A signal can be classified according to different criteria, such as:

  - **Continuous or discrete**: A signal is continuous if it is defined for all values of time. A signal is discrete if it is defined only for discrete values of time.
  - **Energy or power**: A signal is energy if it has a finite amount of energy, which is the integral of the square of the signal over all time. A signal is power if it has a finite average power, which is the limit of the average of the square of the signal over a finite interval as the interval tends to infinity.
  - **Periodic or aperiodic**: A signal is periodic if it repeats itself after a fixed interval of time, called the period. A signal is aperiodic if it does not repeat itself after any interval of time.
  - **Even or odd**: A signal is even if it is symmetric about the origin, which means that the signal is equal to its mirror image. A signal is odd if it is antisymmetric about the origin, which means that the signal is equal to the negative of its mirror image.
  - **Deterministic or random**: A signal is deterministic if it can be predicted exactly for any time. A signal is random if it cannot be predicted exactly for any time, but it can be described by a probability distribution.

## Mathematical representation of signals

- A signal can be represented mathematically by different methods, such as:

  - **Time-domain representation**: A signal is represented by a function of time, which shows the variation of the signal with respect to time.
  - **Frequency-domain representation**: A signal is represented by a function of frequency, which shows the distribution of the signal energy or power over different frequencies.
  - **Spectral density**: A signal is represented by a function of frequency, which shows the density of the signal energy or power per unit frequency.
  - **Transform-domain representation**: A signal is represented by a function of a complex variable, which is obtained by applying a mathematical transform to the signal, such as the Fourier transform, the Laplace transform, or the Z-transform.

## Sampling techniques

- Sampling is the process of converting a continuous signal into a discrete signal by taking samples of the signal at regular intervals of time, called the sampling period or the sampling interval.
- Sampling techniques are methods of choosing the sampling period or the sampling interval to preserve the information of the signal as much as possible, such as:

  - **