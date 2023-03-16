### I2C/IIC

I2C (Inter-Integrated Circuit), also known as IIC, is a multi-master, multi-slave, packet-switched, single-ended, serial computer bus invented by Philips Semiconductor (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication.

Some key features of I2C include:
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- It is capable of operating at speeds up to 5 Mbit/s in Ultra-Fast mode.
- It supports multiple masters and slaves on the same bus.
- It uses 7-bit or 10-bit addressing, allowing up to 112 or 1024 devices on the same bus.
- It supports clock stretching, where a slave device can hold the clock line low to slow down or pause communication.

I2C is commonly used in applications such as:
- Reading data from sensors, such as temperature, humidity, and pressure sensors.
- Controlling OLED or LCD displays.
- Reading and writing to EEPROM or flash memory.
- Communicating with real-time clocks, digital-to-analog converters, and analog-to-digital converters.

I2C is a popular protocol for communication between microcontrollers and peripherals due to its simplicity, low pin count, and flexibility. It is widely used in embedded systems and is supported by many microcontroller manufacturers.