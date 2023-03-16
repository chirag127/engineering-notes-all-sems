# Analog to Digital Conversion

- Analog to digital conversion (ADC) is the process of converting a continuous analog signal into a discrete digital signal.
- ADC is useful for interfacing analog sensors, such as temperature, light, sound, etc., to a microcontroller that can process digital data.
- ADC can also be used for signal processing, such as filtering, compression, modulation, etc., by applying digital algorithms to the converted data.
- ADC involves two main steps: sampling and quantization.
- Sampling is the process of taking periodic snapshots of the analog signal at a fixed rate, called the sampling frequency or sampling rate.
- Sampling frequency must be at least twice the highest frequency component of the analog signal, according to the Nyquist-Shannon sampling theorem, to avoid aliasing.
- Aliasing is the phenomenon of losing or distorting high-frequency information in the analog signal due to insufficient sampling frequency.
- Quantization is the process of assigning a discrete value, called a digital code or a digital word, to each sampled value of the analog signal.
- Quantization involves rounding or truncating the sampled values to the nearest discrete value, which introduces quantization error or quantization noise.
- Quantization error is the difference between the actual sampled value and the assigned discrete value, and it is inversely proportional to the resolution of the ADC.
- Resolution of the ADC is the number of bits used to represent each discrete value, and it determines the number of discrete values or levels that the ADC can produce.
- Resolution of the ADC can be expressed as:

  - Resolution (bits) = log2 (number of levels)
  - Resolution (volts) = (reference voltage) / (number of levels - 1)

- Reference voltage is the maximum voltage that the ADC can convert, and it is usually equal to the supply voltage of the microcontroller or the ADC module.
- ADC can be classified into different types based on the method of conversion, such as:

  - Successive approximation ADC: uses a binary search algorithm to find the closest discrete value to the sampled value in a fixed number of steps, equal to the resolution of the ADC.
  - Flash ADC: uses a parallel array of comparators to compare the sampled value with all the discrete values simultaneously, and produces the digital code in one step, but requires a large number of comparators, equal to the number of levels minus one.
  - Delta-sigma ADC: uses an oversampling technique to sample the analog signal at a much higher frequency than the Nyquist rate, and then applies a digital filter and a decimator to reduce the sampling frequency and the quantization noise, and produce a high-resolution digital code.
  - Dual-slope ADC: uses an integrator to measure the time required for the sampled value to reach zero, and then compares that time with the time required for a known reference voltage to reach zero, and produces the digital code based on the ratio of the two times.

- ADC can be interfaced with a microcontroller using different communication protocols, such as:

  - Parallel interface: uses a parallel bus of wires to transfer the digital code from the ADC to the microcontroller, and requires a control signal to indicate when the conversion is complete and the data is ready.
  - Serial interface: uses a serial bus of wires to transfer the digital code from the ADC to the microcontroller, bit by bit, and requires a clock signal to synchronize the data transfer.
  - Serial peripheral interface (SPI): uses a serial bus of four wires: master out slave in (MOSI), master in slave out (MISO), serial clock (SCK), and slave select (SS), to transfer the digital code from the ADC (slave) to the microcontroller (master), and allows multiple slaves to be connected to the same bus using different SS signals.
  - Inter-integrated circuit (I2C): uses a serial bus of two wires: serial data (SDA) and serial clock (SCL), to transfer the digital code from the ADC (slave) to the microcontroller (master), and allows multiple slaves to be connected to the same bus using different addresses.