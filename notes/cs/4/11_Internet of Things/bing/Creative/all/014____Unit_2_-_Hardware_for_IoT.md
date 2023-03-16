# Unit 2 - Hardware for IoT

Hardware for IoT refers to the physical devices and components that enable the connectivity, communication, and functionality of IoT applications. Hardware for IoT can be classified into four main categories: sensors, microcontrollers, communication modules, and power sources.

## Sensors
Sensors are the most critical hardware in IoT applications and are used to gather information from the surroundings. Sensors can measure various physical phenomena, such as temperature, humidity, light, sound, motion, pressure, etc. Sensors can be analog or digital, passive or active, wired or wireless, depending on their design and purpose. Sensors usually consist of four modules: power management, RF, energy, and sensing . 

- Power management module: This module provides the necessary voltage and current to the sensor and regulates the power consumption.
- RF module: This module manages the communication between the sensor and other devices or networks. It can use different wireless protocols, such as WiFi, Bluetooth, ZigBee, LoRa, etc. It can also include components such as transceiver, duplexer, and BAW.
- Energy module: This module harvests energy from the environment or converts it from other sources, such as solar, thermal, kinetic, etc. It can also store energy in batteries or capacitors for later use.
- Sensing module: This module contains the actual sensor element that converts the physical stimulus into an electrical signal. It can also include components such as amplifier, filter, ADC, etc.

## Microcontrollers
Microcontrollers are small computers that can execute a single task or application. They are usually embedded in IoT devices and control their logic and behavior. Microcontrollers can process the data collected by the sensors, perform calculations, make decisions, and communicate with other devices or networks. Microcontrollers can be programmed using different languages, such as C, Python, Arduino, etc. Microcontrollers usually consist of four modules: CPU, memory, peripherals, and interface .

- CPU module: This module contains the processor that executes the instructions and performs the computations. It can have different architectures, such as ARM, AVR, PIC, etc.
- Memory module: This module contains the memory that stores the data and the program. It can be volatile (RAM) or non-volatile (ROM, EEPROM, flash, etc.).
- Peripherals module: This module contains the components that provide additional functionality to the microcontroller, such as timers, counters, ADC, DAC, PWM, etc.
- Interface module: This module contains the components that enable the communication between the microcontroller and other devices or networks, such as UART, SPI, I2C, USB, Ethernet, etc.

## Communication modules
Communication modules are hardware devices that enable the connectivity and data transmission between IoT devices and networks. Communication modules can use different wireless or wired technologies, such as WiFi, Bluetooth, ZigBee, LoRa, GSM, LTE, Ethernet, etc. Communication modules can be integrated into the sensor or microcontroller modules, or they can be separate devices that connect to them via interfaces. Communication modules usually consist of four modules: antenna, transceiver, modem, and protocol .

- Antenna module: This module contains the antenna that radiates or receives the electromagnetic waves. It can have different shapes, sizes, and frequencies, depending on the communication technology and the application.
- Transceiver module: This module contains the components that modulate and demodulate the signals, such as mixer, oscillator, filter, amplifier, etc. It can also perform functions such as frequency conversion, channel selection, and signal processing.
- Modem module: This module contains the components that encode and decode the data, such as encoder, decoder, multiplexer, demultiplexer, etc. It can also perform functions such as error correction, encryption, and compression.
- Protocol module: This module contains the components that implement the communication protocol, such as controller, processor, memory, etc. It can also perform functions such as addressing, routing, framing, and synchronization.

## Power sources
Power sources are hardware devices that provide the electrical energy to the IoT devices. Power sources can be classified into two types: primary and secondary .

- Primary power sources: These are power sources that cannot be recharged or reused, such as batteries, fuel cells, etc. They have a limited lifespan and capacity, and they need to be replaced when they are depleted.
- Secondary power sources: These are power sources that can be recharged or reused, such as solar panels, thermoelectric