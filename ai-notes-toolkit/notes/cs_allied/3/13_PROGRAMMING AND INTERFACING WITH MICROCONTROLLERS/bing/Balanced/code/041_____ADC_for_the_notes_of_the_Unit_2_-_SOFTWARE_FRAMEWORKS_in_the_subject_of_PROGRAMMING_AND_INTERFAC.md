### ADC for the notes of the Unit 2 - SOFTWARE FRAMEWORKS in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- ADC stands for Analog to Digital Converter, which is a device that converts an analog voltage to a digital value that can be used by a microcontroller.
- ADCs are useful for interfacing with analog sensors, such as temperature, light, distance, position, and force sensors.
- ADCs have a resolution, which is the number of discrete levels that they can detect. For example, a 10-bit ADC can detect 1024 levels, while a 16-bit ADC can detect 65536 levels.
- ADCs also have a sampling rate, which is the speed at which they can digitize the analog signal. The sampling rate depends on the type and architecture of the ADC. Some common types of ADCs are:
  - Successive Approximation Register (SAR) ADCs, which use a binary search algorithm to find the closest digital value to the analog input. They are fast and accurate, but consume more power and have a limited resolution.
  - Sigma-Delta ADCs, which use a feedback loop and a low-pass filter to oversample and average the analog input. They are low-power and high-resolution, but have a slower sampling rate and require more processing.
  - Pipeline ADCs, which use a series of stages to convert the analog input in parallel. They are very fast and can achieve high sampling rates, but have a high power consumption and a latency.
- ADCs are integrated into many microcontrollers, FPGAs, processors, or systems on chips (SoCs). Some examples of microcontrollers with built-in ADCs are:
  - Arduino, which has a 10-bit ADC with a maximum sampling rate of 15 ksps.
  - Analog Devices microcontrollers, which have 12-bit or 16-bit ADCs with sampling rates up to 1 Msps.
  - Microcontrollers with fast ADCs, which can achieve sampling rates above 1 Msps, such as the STM32H7, the Teensy 4.0, or the RP2040.
- To use an ADC in a microcontroller, one needs to prepare the analog signal, configure the ADC settings, and read the digital output. Some steps to prepare the analog signal are:
  - Scaling the signal to match the ADC input range, which is usually 0 to Vref, where Vref is the reference voltage of the ADC.
  - Filtering the signal to remove noise and aliasing, which can affect the accuracy and quality of the digitization.
  - Buffering the signal to isolate it from the ADC input impedance, which can load the signal and cause errors.
- To configure the ADC settings, one needs to select the ADC channel, resolution, sampling rate, reference voltage, and conversion mode. These settings depend on the microcontroller and the ADC type, and are usually done by writing to the ADC registers or using a software library.
- To read the digital output, one needs to wait for the ADC to finish the conversion, which can be indicated by a flag or an interrupt, and then read the ADC data register or buffer. The digital output can be further processed, displayed, stored, or transmitted by the microcontroller.