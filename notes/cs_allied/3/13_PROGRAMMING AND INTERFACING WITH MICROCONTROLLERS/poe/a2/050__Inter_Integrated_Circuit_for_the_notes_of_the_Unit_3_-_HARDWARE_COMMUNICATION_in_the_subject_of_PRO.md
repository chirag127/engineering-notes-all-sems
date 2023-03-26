 Here is the formal notes on Inter-Integrated Circuit (I2C) for Unit 3 - Hardware Communication in the subject of Programming and Interfacing with Microcontrollers:

### Inter-Integrated Circuit (I2C)

- I2C is a serial communication protocol for connecting low-speed peripherals to a microcontroller.
- It uses only two wires: SCL (serial clock) and SDA (serial data).
- Devices are addressed using a 7-bit or 10-bit address scheme.
- Data is transmitted in bytes, MSB first.
- Lines are open-drain and require pull-up resistors.
- Data rates can be up to 400 Kbps according to I2C specifications.
- Common uses include connecting RTC modules, EEPROM memories, sensors, and other peripherals.
- I2C requires using specific functions provided by the microcontroller to initialize, send, and receive data.

To implement I2C:

1. Set the desired data rate using the microcontroller's I2C functions.
2. Choose and assign a unique address to each device connected to the I2C bus.
3. Connect the SCL and SDA lines to all devices. Add pull-up resistors.
4. In the microcontroller, send a START condition.
5. Send the 7-bit or 10-bit address of the device you want to communicate with.
6. Send and receive data bytes with the microcontroller's read and write functions.
7. Send a STOP condition to end the data transfer.

[No external links or emojis included as requested.]