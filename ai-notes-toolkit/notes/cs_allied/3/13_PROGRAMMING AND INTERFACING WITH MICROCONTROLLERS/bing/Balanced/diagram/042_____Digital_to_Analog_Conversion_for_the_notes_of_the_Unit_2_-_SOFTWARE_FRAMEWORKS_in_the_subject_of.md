### Digital to Analog Conversion

- Digital to analog conversion (DAC) is the process by which digital signals (which have a binary state) are converted to analog signals (which theoretically have an infinite number of states).
- DAC is necessary when we communicate information from one system to another across a public access phone line or when we want to reproduce high-quality sound from digital data .
- There are several DAC architectures; the suitability of a DAC for a particular application is determined by figures of merit including resolution, maximum sampling frequency, accuracy, linearity, speed, power consumption, and cost.
- The following techniques can be used for DAC:
  - Amplitude Shift Keying (ASK): The amplitude of analog carrier signal is modified to reflect binary data.
  - Frequency Shift Keying (FSK): The frequency of analog carrier signal is modified to reflect binary data.
  - Phase Shift Keying (PSK): The phase of analog carrier signal is modified to reflect binary data.
  - Quadrature Amplitude Modulation (QAM): The amplitude and phase of analog carrier signal are modified to reflect binary data.
- A typical DAC consists of the following components:
  - A reference voltage source that provides a fixed reference voltage for the conversion process.
  - A digital input that receives the digital signal to be converted.
  - A switching network that selects the appropriate reference voltage level for each bit of the digital input.
  - A summing amplifier that adds up the selected reference voltage levels and produces the analog output.
  - A low-pass filter that removes the high-frequency components from the analog output and smooths the signal.

![DAC block diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/DAC_block_diagram.svg/1200px-DAC_block_diagram.svg.png)