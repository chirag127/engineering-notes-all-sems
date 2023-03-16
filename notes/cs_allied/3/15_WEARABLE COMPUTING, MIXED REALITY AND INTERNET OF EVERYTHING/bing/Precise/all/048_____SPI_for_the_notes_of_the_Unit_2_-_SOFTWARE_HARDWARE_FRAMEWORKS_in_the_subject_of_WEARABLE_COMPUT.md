# Unit 2 - SOFTWARE HARDWARE FRAMEWORKS

### SPI

- SPI stands for Serial Peripheral Interface.
- It is a synchronous serial communication interface specification used for short-distance communication.
- It is primarily used in embedded systems for communication between microcontrollers and peripheral devices such as sensors, shift registers, and SD cards.
- SPI operates in full-duplex mode, meaning data can be transmitted and received simultaneously.
- It uses a master-slave architecture, where the master device controls the communication and the slave devices respond to the master's commands.
- The communication is initiated by the master device, which generates the clock signal and selects the slave device it wants to communicate with.
- The data is transmitted using a shift register, where the data is shifted out bit by bit on each clock pulse.
- The clock polarity and clock phase can be configured to control the timing of the data transmission.
- SPI is a simple and efficient communication protocol, but it has some limitations, such as the need for a separate chip select line for each slave device and the lack of error checking.