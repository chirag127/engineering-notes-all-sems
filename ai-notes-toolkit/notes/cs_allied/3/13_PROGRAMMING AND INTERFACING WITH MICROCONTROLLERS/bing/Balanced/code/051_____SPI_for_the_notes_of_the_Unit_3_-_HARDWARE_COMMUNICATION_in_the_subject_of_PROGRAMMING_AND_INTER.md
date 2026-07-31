### SPI

- SPI stands for Serial Peripheral Interface, a synchronous serial communication protocol that allows a master device to communicate with one or more slave devices.
- SPI uses four wires: SCLK (serial clock), MOSI (master out slave in), MISO (master in slave out), and SS (slave select).
- The master device generates the clock signal and selects the slave device by pulling its SS line low. The master and slave devices exchange data by shifting bits out and in on the MOSI and MISO lines, respectively, on each clock edge.
- SPI supports full-duplex communication, meaning that data can be sent and received simultaneously. The data rate is determined by the clock frequency, which can be up to several megahertz.
- SPI has several advantages over other serial protocols, such as simplicity, speed, flexibility, and low overhead. However, SPI also has some limitations, such as lack of error detection, lack of flow control, and limited number of devices that can be connected on a single bus.