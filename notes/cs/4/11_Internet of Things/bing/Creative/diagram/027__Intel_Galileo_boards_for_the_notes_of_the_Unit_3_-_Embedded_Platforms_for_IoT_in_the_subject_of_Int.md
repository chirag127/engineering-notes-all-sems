The following diagram illustrates the basic architecture of an Intel Galileo board:

```
+---------------------------------------+
|                                       |
|  +------------------+                 |
|  |                  |                 |
|  |  Intel Quark     |                 |
|  |  SoC X1000       |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  DDR3 256 MB     |                 |
|  |  RAM             |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  SPI Flash       |                 |
|  |  8 MB            |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  Ethernet PHY    |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  USB Hub         |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  USB Client      |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  USB Host        |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  RS-232 UART     |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  JTAG Header     |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  Power Jack      |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  Power Switch    |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  Reset Button    |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  Arduino Shield  |                 |
|  |  Interface       |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  GPIO Expander   |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  PWM Controller  |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  ADC             |                 |
|  |                  |                 |
|  +------------------+                 |
|  |                  |                 |
|  |  I2C EEPROM      |                 |
|  |                  |                 |
|  +------------------+                 |
|                                       |
+---------------------------------------+
```

The Intel Galileo board is based on the Intel Quark SoC X1000, a 32-bit Intel Pentium-class system on a chip. It has 256 MB of DDR3 RAM and 8 MB of SPI flash memory. It supports Ethernet, USB, RS-232, and JTAG connectivity. It also has a power jack, a power switch, a reset button, and an Arduino shield interface. The Arduino shield interface allows the board to be compatible with Arduino shields designed for the Uno R3. The board also has a GPIO expander, a PWM controller, an ADC, and an I2C EEPROM to provide additional functionality. The board can run Linux or the Arduino software development environment.