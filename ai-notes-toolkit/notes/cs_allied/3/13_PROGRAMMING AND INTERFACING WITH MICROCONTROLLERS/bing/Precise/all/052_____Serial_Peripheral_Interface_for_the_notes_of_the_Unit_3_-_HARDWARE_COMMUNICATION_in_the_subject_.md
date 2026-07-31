# Unit 3 - HARDWARE COMMUNICATION: Serial Peripheral Interface

- The Serial Peripheral Interface (SPI) is a synchronous serial communication interface specification used for short-distance communication, primarily in embedded systems.
- The interface was developed by Motorola in the mid-1980s and has become a de facto standard.
- Typical applications include Secure Digital cards and liquid crystal displays.
- SPI is a four-wire bus. It consists of a serial clock, master output/slave input, master input/slave output, and a device select pin.
- The speed of the bus range is much higher than that found in I2C or SMBus; speeds up to 80 MHz are not uncommon.
- SPI is commonly used to send data between microcontrollers and small peripherals such as shift registers, sensors, and SD cards.
- It uses separate clock and data lines, along with a select line to choose the device you wish to talk to.
