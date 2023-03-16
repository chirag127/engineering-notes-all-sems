# DAC

DAC stands for Digital-to-Analog Converter. It is an integrated analog peripheral that provides a variable voltage reference that is ratio metric with an input source. DACs are defined by their bit resolution, which indicates how many selectable voltage levels are possible between the positive and negative voltage sources.

## DAC Applications

DACs can be used to generate custom analog signals, such as precision voltages, as well as custom waveforms including sine waves and triangle waves. DACs can also be used for voice synthesis. Some applications that require DACs are:

- Frequency or voltage generation
- Audio and video processing
- Data acquisition and signal processing
- Instrumentation and control
- Communication and networking

## DAC Types

There are different types of DACs based on their architecture, performance, and features. Some common types are:

- High-speed DACs: These are DACs that operate at sampling rates greater than 10 MSPS (mega samples per second). They are used for high-frequency applications such as wireless communication, radar, and digital imaging.
- Precision DACs: These are DACs that operate at sampling rates less than or equal to 10 MSPS. They are used for high-accuracy applications such as industrial automation, medical devices, and test and measurement.
- Smart DACs: These are DACs that have additional features such as programmable output ranges, internal references, calibration, and fault detection. They are used for applications that require flexibility, reliability, and ease of use.

## DACs on Microcontrollers

Some microcontrollers have DAC peripherals on-chip for convenience and integration. These can be used to generate analog signals without the need for external components. However, not all microcontrollers have on-chip DACs, because:

- DACs consume more power and area than other peripherals
- DACs require a stable and isolated reference voltage, which may not be available on the microcontroller
- DACs have limited resolution and speed compared to external DACs
- DACs are not needed for many applications that use PWM (pulse width modulation) to control devices such as motors, solenoids, and switching power supplies

Therefore, designers need to consider the trade-offs between using on-chip or external DACs for their applications. External DACs can offer higher performance and functionality, but they also require more board space and interfacing. On-chip DACs can offer simplicity and integration, but they also have limitations and constraints.