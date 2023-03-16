### DAC

- DAC stands for Digital-to-Analog Converter. It is an integrated analog peripheral that provides a variable voltage reference that is ratio metric with an input source.
- DACs are defined by their bit resolution, which indicates how many selectable voltage levels are possible between the positive and negative voltage sources.
- DACs can be used to generate custom analog signals, such as precision voltages, waveforms, voice synthesis, etc .
- Some microcontrollers have DACs on-chip for frequency or voltage generation, which provides additional functionality while saving board space.
- However, some applications might require specialized DAC functionality not found in microcontrollers, such as high speed, high precision, or multiple channels .
- In such cases, external DACs can be used to extend the microcontroller functionality. External DACs can be interfaced with microcontrollers using serial or parallel communication protocols, such as SPI, I2C, UART, etc.
- External DACs can also offer better isolation from the internal digital logic of the microcontroller, which can minimize power supply ripple and noise.
- Some examples of external DACs are MCP4725, MCP4921, MCP4922, DAC0808, etc .
- Some examples of microcontrollers with on-chip DACs are STM32F4, PIC16F178x, PIC18FxxQ10, etc .