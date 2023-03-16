### Serial UART Communication

- UART stands for **Universal Asynchronous Receiver Transmitter**  , which is a serial communication device that performs parallel-to-serial and serial-to-parallel data conversion.
- UART is universal because the parameters like transfer speed, data speed, etc. are configurable.
- UART is asynchronous because there is no clock signal to synchronize the output bits from the transmitting device going to the receiving end.
- UART is a single LSI (large-scale integration) chip designed to perform asynchronous communication. It can be integrated in microcontroller chips or used as a standalone device.
- UART uses two wires for communication: RX (receive) and TX (transmit). The RX of one device is connected to the TX of another device, and vice versa.
- UART communication follows a protocol that defines the format and timing of the data bits. The protocol consists of the following elements:
  - **Baud rate**: the number of bits per second that are transmitted or received. The baud rate of the transmitter and receiver must match for successful communication.
  - **Start bit**: a logic low (0) bit that indicates the beginning of a data frame.
  - **Data bits**: the actual information that is transmitted or received. The number of data bits can vary from 5 to 9, depending on the device configuration.
  - **Parity bit**: an optional bit that is used for error detection. The parity bit can be even, odd, or none, depending on the device configuration.
  - **Stop bit**: a logic high (1) bit that indicates the end of a data frame. The number of stop bits can be 1, 1.5, or 2, depending on the device configuration.
- UART communication can be full-duplex or half-duplex, depending on the device configuration. Full-duplex means that both devices can transmit and receive data simultaneously, while half-duplex means that only one device can transmit or receive data at a time.
- UART communication can be used for various applications, such as connecting microcontrollers to sensors, modules, computers, or other devices. UART is also compatible with other serial communication standards, such as RS-232, RS-485, or USB, with the help of level converters or adapters.