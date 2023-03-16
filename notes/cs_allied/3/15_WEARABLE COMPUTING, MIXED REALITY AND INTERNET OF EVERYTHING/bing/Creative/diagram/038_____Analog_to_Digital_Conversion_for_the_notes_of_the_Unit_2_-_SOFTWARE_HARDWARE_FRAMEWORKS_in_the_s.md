### Analog to Digital Conversion

- Analog to digital conversion (ADC) is an electronic process that converts a continuous analog signal, such as a sound, light, or voltage, into a discrete digital signal, such as a binary code .
- ADC is a useful feature that allows digital devices, such as microcontrollers, computers, or sensors, to interface with the analog world around us.
- ADC is essential for applications such as digital imaging, radar, signal processing, data acquisition, and communication .
- ADC involves two main steps: sampling and quantization .
  - Sampling is the process of taking periodic snapshots of the analog signal at a fixed rate, called the sampling frequency. The sampling frequency must be at least twice the highest frequency component of the analog signal, according to the Nyquist-Shannon sampling theorem, to avoid aliasing .
  - Quantization is the process of assigning a discrete value, usually a binary number, to each sample, based on its amplitude. The number of bits used to represent each sample is called the resolution of the ADC. The resolution determines the accuracy and dynamic range of the ADC. The quantization process introduces some error, called quantization noise, which can be reduced by increasing the resolution .
- There are different types of ADCs, such as successive approximation, flash, sigma-delta, and dual-slope, that differ in their speed, accuracy, complexity, and cost .
- ADCs are usually integrated into microcontrollers or other digital devices, or can be standalone chips that communicate with digital devices via serial or parallel interfaces .