# SPI

SPI stands for Serial Peripheral Interface. It is a synchronous serial communication protocol that provides full-duplex communication at very high speeds. SPI is a master-slave type protocol that provides a simple and low-cost interface between a microcontroller and its peripherals  .

## SPI Communication Basics

- SPI uses four wires to communicate: SCLK (Serial Clock), MOSI (Master Out Slave In), MISO (Master In Slave Out), and SS (Slave Select).
- The master device generates the clock signal and selects the slave device by pulling the SS line low.
- The master and the slave exchange data by shifting bits out and in simultaneously on the MOSI and MISO lines, respectively.
- The data transfer rate is determined by the clock frequency, which can be up to several MHz.
- The data can be transferred in different modes, depending on the clock polarity and phase. There are four possible modes, numbered from 0 to 3, as shown in the table below .

| Mode | Clock Polarity (CPOL) | Clock Phase (CPHA) | Data Capture Edge | Data Shift Edge |
|------|-----------------------|--------------------|-------------------|-----------------|
| 0    | 0                     | 0                  | Rising            | Falling         |
| 1    | 0                     | 1                  | Falling           | Rising          |
| 2    | 1                     | 0                  | Falling           | Rising          |
| 3    | 1                     | 1                  | Rising            | Falling         |

## SPI Communication Types

- In typical SPI bus mode, only one master device can control multiple independent slave devices. Each slave device has its own SS line, and only one SS line can be low at a time. This mode is also called single-master mode .
- In multi-master mode, more than one master device can share the same SPI bus. However, only one master device can initiate a data transfer at a time, and the other master devices must act as slaves. This mode requires additional hardware or software to arbitrate the bus access and avoid collisions.
- In daisy-chain mode, multiple slave devices are connected in series, and the MISO line of one slave is connected to the MOSI line of the next slave. The master device can communicate with all the slaves by sending and receiving data through a single SS line. However, this mode requires more clock cycles to transfer the same amount of data as in the typical SPI bus mode.

## SPI Communication Applications

- SPI is widely used for interfacing various devices, such as sensors, memory cards, LCD displays, RFID readers, wireless modules, etc. Some examples are :
  - SD card reader modules use SPI to read and write data to and from the SD card.
  - RFID card reader modules use SPI to send and receive data from the RFID tags.
  - 2.4 GHz wireless transmitter/receivers use SPI to configure the wireless parameters and exchange data with the microcontroller.