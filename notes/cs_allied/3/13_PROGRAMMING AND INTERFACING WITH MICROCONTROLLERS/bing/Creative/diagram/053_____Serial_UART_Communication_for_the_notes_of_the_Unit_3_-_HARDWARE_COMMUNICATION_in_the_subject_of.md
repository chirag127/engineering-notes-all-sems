### Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter**  .
- It is a **serial communication device** that performs parallel-to-serial and serial-to-parallel data conversion .
- It is **universal** because the parameters like transfer speed, data speed, etc. are configurable .
- It is **asynchronous** because there is no clock signal to synchronize the output bits from the transmitting device to the receiving device.
- A UART is usually an individual or part of an integrated circuit (IC) used for serial communications over a computer or peripheral device serial port.
- One or more UART peripherals are commonly integrated in microcontroller chips.
- Specialised UARTs are used for automobiles, smart cards and SIMs.
- A UART consists of a **transmitter** and a **receiver**  .
- The transmitter and receiver have a **data register** and a **shift register** each  .
- The data register is used to store the parallel data to be transmitted or received  .
- The shift register is used to shift the data bits serially in or out of the UART  .
- The transmitter and receiver also have a **baud rate generator** that determines the speed of data transmission or reception  .
- The baud rate is the number of bits transferred per second  .
- The baud rate can be set by the user or by the system  .
- The transmitter and receiver also have a **control unit** that controls the operation of the UART  .
- The control unit can enable or disable the UART, select the data format, set the parity bit, etc  .
- The data format of a UART consists of a **start bit**, a **data word**, an optional **parity bit**, and a **stop bit**  .
- The start bit is a logic low signal that indicates the beginning of a data transmission  .
- The data word is the actual data to be transmitted or received, usually 7 or 8 bits long  .
- The parity bit is an optional bit that is used for error detection, it can be even or odd  .
- The stop bit is a logic high signal that indicates the end of a data transmission  .
- The UART communication protocol can be summarized as follows  :

  - The transmitter sends a start bit, followed by the data word, followed by the optional parity bit, followed by the stop bit.
  - The receiver detects the start bit, then reads the data word, then checks the parity bit if present, then acknowledges the stop bit.
  - The transmitter and receiver must have the same baud rate, data format, and parity settings for successful communication.

- A UART can communicate with another UART directly or through a communication channel like RS-232   .
- RS-232 is a standard that defines the electrical characteristics and timing of signals, the meaning of signals, and the physical size and pinout of connectors.
- RS-232 uses a voltage level of -12V to +12V to represent logic levels, while UART uses 0V to 5V or 3.3V.
- RS-232 also uses inverted logic, where a logic low is represented by a positive voltage and a logic high is represented by a negative voltage.
- Therefore, a UART needs a level converter or a driver to communicate with RS-232 devices.
- A UART can also communicate with other serial communication protocols like SPI, I2C, USB, etc. with