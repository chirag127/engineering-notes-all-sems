 Here is the content in markdown format:

### Communicating data with H/W units for the notes of the Unit 7 - IoT Applications in the subject of Internet of Things

- IoT devices communicate with each other using various hardware communication interfaces like:
- Serial Communication interfaces: UART, SPI, I2C
- Parallel communication interfaces: GPIO
- Wireless communication interfaces: WiFi, Bluetooth, Zigbee, LoRaWAN, etc.

**UART**: Universal Asynchronous Receiver/Transmitter
- Used for serial data communication between two devices.
- Uses TX and RX pins. Data is sent sequentially one bit at a time.
- Baud rate specifies the speed of data transmission.
- Advantage: Simple and easy to implement.
- Disadvantage: Only suitable for short distance communication.

**SPI**: Serial Peripheral Interface
- Full duplex, synchronous serial data interface with separate transmit and receive lines.
- Uses 4 wires: SCLK, MOSI, MISO, SS.
- Data is transferred in bursts with a master-slave architecture.
- Fast data transfer rate.
- Complex protocol but takes less pins.

**I2C**: Inter-Integrated Circuit
- Synchronous serial protocol for short distance communication.
- Uses 2 wires: SDA and SCL.
- Master-slave architecture with multiple slave devices sharing the same bus.
- Addresses are used to identify each device on the bus.
- Relatively slow but takes less wires.

**GPIO**: General Purpose Input Output
- Used to receive and send digital signals.
- Can be configured as input to read sensors or as output to control actuators.
- Simple to use but not suitable for high speed data communication.

**WiFi, Bluetooth, etc.**: For wireless data communication over longer ranges. Have various network topologies and protocols for establishing connections between devices.

[Diagrams and examples can be added here]