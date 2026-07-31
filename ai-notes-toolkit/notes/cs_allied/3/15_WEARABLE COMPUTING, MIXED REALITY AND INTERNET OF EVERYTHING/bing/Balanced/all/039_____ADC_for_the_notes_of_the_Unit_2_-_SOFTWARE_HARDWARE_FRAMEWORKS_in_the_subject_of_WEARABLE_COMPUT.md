# ADC

ADC stands for Analog to Digital Converter. It is a device that converts analog signals, such as sound, light, temperature, etc., into digital signals that can be processed by a computer or a microcontroller.

## ADC in Software Hardware Frameworks

- ADC is an essential component of software hardware frameworks for wearable computing, mixed reality and internet of everything applications, as it enables the interaction between the physical world and the digital world.
- ADC can be used to capture sensor data, such as heart rate, motion, orientation, etc., from wearable devices and send them to a processing unit, such as a smartphone, a laptop, or a cloud server, for analysis, visualization, or feedback.
- ADC can also be used to generate output signals, such as sound, light, vibration, etc., from a processing unit and deliver them to a wearable device or a mixed reality device, such as a speaker, a LED, a motor, or a display, for user interaction, notification, or immersion.
- ADC can be integrated into a single chip, such as a microcontroller, a system on chip (SoC), or a field programmable gate array (FPGA), or can be connected as a separate module, such as a breakout board, a shield, or a hat, depending on the design and performance requirements of the application.

## ADC Characteristics and Parameters

- ADC has several characteristics and parameters that affect its performance and suitability for different applications, such as:

  - Resolution: The number of bits used to represent the digital output of the ADC. Higher resolution means more accuracy and precision, but also more power consumption and data transfer rate.
  - Sampling rate: The frequency at which the ADC samples the analog input signal. Higher sampling rate means more information and fidelity, but also more power consumption and data transfer rate.
  - Input range: The minimum and maximum voltage levels that the ADC can accept as analog input. The input range should match the output range of the sensor or the signal source.
  - Reference voltage: The voltage level that the ADC uses to compare the analog input signal and determine the digital output value. The reference voltage can be fixed or adjustable, internal or external, depending on the ADC design and configuration.
  - Conversion time: The time required for the ADC to complete one conversion cycle, from sampling the analog input to producing the digital output. Lower conversion time means faster response and throughput, but also more power consumption and noise.
  - Power consumption: The amount of electrical energy that the ADC consumes during operation. Lower power consumption means longer battery life and less heat generation, but also lower performance and quality.
  - Noise: The unwanted variation or distortion of the digital output of the ADC due to external or internal factors, such as interference, temperature, quantization, etc. Lower noise means higher signal to noise ratio (SNR) and better quality, but also more complexity and cost.

## ADC Types and Techniques

- ADC can be classified into different types and techniques based on the method or principle that they use to convert the analog input signal into the digital output signal, such as:

  - Successive approximation register (SAR) ADC: A type of ADC that uses a binary search algorithm to find the closest digital output value to the analog input value. It consists of a comparator, a successive approximation register (SAR), and a digital to analog converter (DAC). It has high resolution, low power consumption, and moderate speed and noise.
  - Sigma-delta (ΣΔ) ADC: A type of ADC that uses an oversampling technique to reduce the noise and increase the resolution of the digital output signal. It consists of a modulator, a decimator, and a filter. It has very high resolution, low noise, and low power consumption, but low speed and high complexity.
  - Flash ADC: A type of ADC that uses a parallel array of comparators to compare the analog input signal with a set of reference voltages and produce the digital output signal in one step. It has very high speed, low conversion time, and low complexity, but low resolution, high power consumption, and high noise.
  - Dual-slope ADC: A type of ADC that uses a counter and a capacitor to measure the time required for the analog input signal to charge or discharge the capacitor and produce the digital output signal proportional to the time. It has high resolution, low noise, and low power consumption, but low speed and high conversion time.