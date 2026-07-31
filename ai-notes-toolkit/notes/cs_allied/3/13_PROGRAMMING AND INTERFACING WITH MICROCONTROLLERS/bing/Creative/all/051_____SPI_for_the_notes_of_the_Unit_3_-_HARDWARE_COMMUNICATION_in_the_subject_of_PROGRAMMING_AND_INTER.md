# SPI

SPI stands for Serial Peripheral Interface. It is a synchronous serial communication protocol that allows one master device to communicate with multiple slave devices using a shared bus. It is commonly used for short-distance communication between microcontrollers and their peripherals, such as sensors, memory cards, displays, etc.

## SPI Communication Basics

- SPI uses four wires to transmit data: MOSI (Master Out Slave In), MISO (Master In Slave Out), SCK (Serial Clock), and SS (Slave Select).
- The master device initiates and controls the data transfer by generating the clock signal and selecting the slave device using the SS line.
- The master and the slave exchange data simultaneously by shifting bits in and out on the MOSI and MISO lines, respectively, on each clock cycle.
- The data transfer rate depends on the clock frequency, which can be set by the master device according to the specifications of the slave device.
- The data transfer can be in full-duplex (both directions at the same time) or half-duplex (one direction at a time) mode.
- The data transfer can be in different modes, depending on the polarity and phase of the clock signal. There are four possible modes, numbered from 0 to 3, as shown in the table below.

| Mode | Clock Polarity | Clock Phase | Data Capture | Data Output |
|------|----------------|-------------|--------------|-------------|
| 0    | 0 (Low)        | 0 (Leading) | Rising Edge  | Falling Edge|
| 1    | 0 (Low)        | 1 (Trailing)| Falling Edge | Rising Edge |
| 2    | 1 (High)       | 0 (Leading) | Falling Edge | Rising Edge |
| 3    | 1 (High)       | 1 (Trailing)| Rising Edge  | Falling Edge|

- The master and the slave must agree on the mode, the data length (typically 8 bits), and the bit order (MSB first or LSB first) before the data transfer.

## SPI Communication Types

- There are different types of SPI communication, depending on the number and configuration of the master and slave devices.
- The simplest type is single master-single slave, where only one master and one slave are connected using four wires. The SS line is optional in this case, as there is no need to select the slave device.
- Another type is single master-multiple slaves, where one master can communicate with multiple slaves using a separate SS line for each slave. The master can select only one slave at a time by pulling its SS line low, while keeping the other SS lines high. The MOSI, MISO, and SCK lines are shared by all the devices.
- A third type is multiple masters-multiple slaves, where more than one master can communicate with multiple slaves using a common bus. This type requires additional hardware and software to arbitrate the access to the bus and avoid collisions. A common method is to use a priority encoder to assign a unique priority to each master and select the one with the highest priority when more than one master requests the bus.

## SPI Communication Applications

- SPI is widely used for communication between microcontrollers and various peripherals, such as sensors, memory cards, displays, etc. Some examples are:
  - SD cards use SPI to transfer data to and from the host device.
  - RFID readers use SPI to read data from RFID tags and send it to the host device.
  - LCD displays use SPI to receive commands and data from the host device and display them on the screen.
  - Accelerometers use SPI to measure the acceleration and orientation of the device and send it to the host device.
  - Temperature sensors use SPI to measure the temperature and send it to the host device.