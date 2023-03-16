### ADC

ADC stands for Analog to Digital Converter. It is a device that converts an analog signal, such as a voltage or a current, into a digital signal, which is a sequence of binary bits. ADCs are widely used in microcontrollers, sensors, data acquisition systems, and other applications that require interfacing between the analog and digital domains.

Some of the topics that are covered in this unit are:

- ADC types and architectures
- ADC specifications and parameters
- ADC interfacing and programming
- ADC applications and examples

#### ADC types and architectures

There are different types and architectures of ADCs, each with its own advantages and disadvantages. Some of the common types are:

- Successive approximation register (SAR) ADC: This type of ADC uses a binary search algorithm to find the digital output that matches the analog input. It consists of a comparator, a DAC, and a register. It is fast, accurate, and simple to implement, but it requires a high-resolution DAC and a stable reference voltage.
- Sigma-delta (ΣΔ) ADC: This type of ADC uses a feedback loop to oversample and filter the analog input, and then decimate the output to obtain the desired resolution. It consists of a modulator, a filter, and a decimator. It is very accurate, low-noise, and suitable for high-resolution applications, but it is slow, complex, and power-hungry.
- Pipeline ADC: This type of ADC uses a series of stages, each consisting of a sample-and-hold circuit, a sub-ADC, and a sub-DAC, to convert the analog input in parallel. It is very fast, high-bandwidth, and scalable, but it is also expensive, power-hungry, and prone to errors.

#### ADC specifications and parameters

There are various specifications and parameters that describe the performance and characteristics of an ADC, such as:

- Resolution: The number of bits in the digital output, which determines the number of discrete levels that the ADC can distinguish. For example, a 10-bit ADC can detect 1024 levels, while a 16-bit ADC can detect 65536 levels.
- Sampling rate: The frequency at which the ADC samples the analog input, which determines the maximum bandwidth that the ADC can capture. For example, a 1 MSPS ADC can sample up to 500 kHz of analog signal, according to the Nyquist theorem.
- Accuracy: The degree of closeness between the digital output and the true value of the analog input, which depends on various factors such as offset, gain, linearity, and noise. Accuracy is usually expressed as an absolute or relative error, or as a percentage of full scale.
- Dynamic range: The ratio between the maximum and minimum signal levels that the ADC can handle without distortion, which depends on the resolution, the reference voltage, and the noise. Dynamic range is usually expressed in decibels (dB).
- Power consumption: The amount of power that the ADC consumes during operation, which depends on the type, the architecture, the sampling rate, and the resolution. Power consumption is usually expressed in milliwatts (mW) or microwatts (µW).

#### ADC interfacing and programming

ADC interfacing and programming refers to the process of connecting an ADC to a microcontroller and writing code to control and read the ADC. There are different ways of interfacing an ADC to a microcontroller, such as:

- Parallel interface: The ADC and the microcontroller share a common data bus, and the ADC sends the digital output to the microcontroller in parallel. This interface is fast, simple, and synchronous, but it requires a lot of pins and wires.
- Serial interface: The ADC and the microcontroller communicate using a serial protocol, such as SPI, I2C, or UART, and the ADC sends the digital output to the microcontroller in serial. This interface is slow, complex, and asynchronous, but it requires fewer pins and wires.
- Integrated interface: The ADC is built-in to the microcontroller, and the ADC and the microcontroller share the same power supply, clock, and memory. This interface is convenient, efficient, and cost-effective, but it limits the choice and flexibility of the ADC.

The programming of an ADC involves configuring the ADC settings, such as the resolution, the sampling rate, the reference voltage, and the channel selection, and initiating and reading the ADC conversion, either by polling, interrupt, or DMA methods. The programming of an ADC also depends on the type of microcontroller, the type of ADC, and the type of interface.

#### ADC applications and examples

ADCs are used