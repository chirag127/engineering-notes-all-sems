### Advanced I/O

- Advanced I/O refers to the techniques and devices that enable a microcontroller to communicate with external peripherals, such as sensors, actuators, displays, keyboards, etc.
- Advanced I/O can be classified into two categories: parallel and serial.
- Parallel I/O uses multiple data lines to transfer data between the microcontroller and the peripheral in parallel, i.e., one bit per line. Parallel I/O is faster than serial I/O, but requires more pins and wires.
- Serial I/O uses one or a few data lines to transfer data between the microcontroller and the peripheral in serial, i.e., one bit after another. Serial I/O is slower than parallel I/O, but requires fewer pins and wires.
- Some of the common parallel I/O devices are:
  - LED: A light-emitting diode that can be turned on or off by applying a voltage to its anode and cathode terminals.
  - LCD: A liquid crystal display that can show alphanumeric or graphical information by controlling the polarization of liquid crystals in each pixel.
  - Keypad: A matrix of switches that can detect the user's input by scanning the rows and columns of the matrix.
  - ADC: An analog-to-digital converter that can convert an analog voltage signal into a digital value that can be read by the microcontroller.
  - DAC: A digital-to-analog converter that can convert a digital value from the microcontroller into an analog voltage signal that can be sent to an external device.
- Some of the common serial I/O devices are:
  - UART: A universal asynchronous receiver/transmitter that can send and receive data using a start bit, a stop bit, and an optional parity bit to synchronize the communication.
  - SPI: A serial peripheral interface that can send and receive data using a clock line, a data in line, a data out line, and a chip select line to select the peripheral.
  - I2C: An inter-integrated circuit that can send and receive data using a clock line and a data line, and can support multiple peripherals on the same bus using an address scheme.
  - USB: A universal serial bus that can send and receive data using a differential pair of data lines, and can support multiple peripherals on the same bus using a host-controller protocol.