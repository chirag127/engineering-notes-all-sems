# ADC for the notes of the Unit 2 - SOFTWARE FRAMEWORKS in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- ADC stands for Analog to Digital Converter, which is a device that converts an analog voltage to a digital value that can be used by a microcontroller.
- ADCs are useful for interfacing with analog sensors, such as temperature, light, distance, position, and force sensors.
- ADCs have a resolution, which is the number of discrete levels that they can detect. For example, a 10-bit ADC can detect 1024 levels, while a 16-bit ADC can detect 65536 levels.
- ADCs also have a sampling rate, which is the speed at which they can digitize the analog signal. The sampling rate depends on the type and architecture of the ADC. Some common types of ADCs are:
  - Successive Approximation Register (SAR) ADCs, which use a binary search algorithm to find the closest digital value to the analog input. They are fast and accurate, but consume more power and have a limited resolution.
  - Sigma-Delta ADCs, which use a feedback loop and a low-pass filter to oversample the analog input and produce a high-resolution digital output. They are low-power and high-resolution, but have a lower sampling rate and are more susceptible to noise.
  - Pipeline ADCs, which use a series of stages to process the analog input in parallel and produce a high-speed digital output. They are used for applications that require very high sampling rates, such as video and radar.
- ADCs are integrated into many microcontrollers, FPGAs, processors, or systems on chips (SoCs). Some microcontrollers have built-in ADCs, which means they can directly digitize analog signals and manipulate the results using their I/O lines. Some examples of microcontrollers with fast ADCs are:
  - STM32H7 series, which have up to 3 ADCs with 16-bit resolution and up to 3.6 Msps sampling rate.
  - Teensy 4.0, which has a 12-bit ADC with up to 1 Msps sampling rate.
  - Arduino Uno, which has a 10-bit ADC with up to 10 ksps sampling rate.
- To use an ADC, one needs to prepare the analog signal for the ADC input, configure the ADC settings, and read the ADC output. Some steps to prepare the analog signal are:
  - Scaling the signal to match the ADC input range, which is usually 0 to Vref, where Vref is the reference voltage of the ADC.
  - Filtering the signal to remove noise and unwanted frequencies, which can affect the accuracy and resolution of the ADC.
  - Buffering the signal to isolate the ADC input from the signal source, which can have a high impedance or a variable voltage.
- To configure the ADC settings, one needs to select the ADC channel, resolution, sampling rate, reference voltage, and conversion mode. These settings depend on the type and specifications of the ADC and the microcontroller.
- To read the ADC output, one needs to use the ADC registers, interrupts, or DMA (Direct Memory Access) to transfer the digital value from the ADC to the microcontroller memory or peripherals. The ADC output can then be processed, displayed, stored, or transmitted by the microcontroller.