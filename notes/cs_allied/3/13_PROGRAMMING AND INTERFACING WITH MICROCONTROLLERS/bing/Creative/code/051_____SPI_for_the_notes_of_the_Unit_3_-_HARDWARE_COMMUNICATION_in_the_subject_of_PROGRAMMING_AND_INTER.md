### SPI

- SPI stands for Serial Peripheral Interface, a synchronous serial communication protocol that allows a master device to communicate with one or more slave devices.
- SPI uses four signals: SCLK (serial clock), MOSI (master out slave in), MISO (master in slave out), and SS (slave select).
- The master device generates the SCLK signal and selects the slave device by pulling the SS signal low. The master and slave devices exchange data by shifting bits on the MOSI and MISO lines simultaneously with each clock pulse.
- SPI is a full-duplex protocol, meaning that data can be sent and received at the same time. SPI is also a byte-oriented protocol, meaning that data is transferred in units of 8 bits (or multiples of 8 bits).
- SPI has several advantages over other serial protocols, such as simplicity, speed, flexibility, and low overhead. However, SPI also has some limitations, such as the need for more pins, the lack of error detection and correction, and the potential for signal interference and crosstalk.