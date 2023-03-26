 Here is the content in markdown format without any emojis or external links:

### Inter-Integrated Circuit

- I2C (Inter-Integrated Circuit) is a serial bus interface standard that allows low-speed peripherals to communicate with a microprocessor.
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- I2C supports multiple masters and slaves with each slave having a unique address.
- Data is transmitted in messages. A message is initiated by the master, which sends the address of the slave it wants to communicate with.
- This is followed by transmission of one or more bytes to the addressed slave. The slave may send zero or more bytes in reply. A message is ended by a STOP condition initiated by the master.
- I2C is useful for connecting slow peripheral devices that are physically close, such as sensors, real-time clocks, memory, and DACs.
- Advantages: Only two wires (clock and data lines), low speeds (up to 400kHz standard, up to 1MHz in some implementations), multiple slave support (up to 112 devices), has been widely adopted so lots of peripherals support I2C interface.
- Disadvantages: Limited maximum speed and distance (meter-scale on a PCB).

Does this look okay? Let me know if you would like me to modify or add anything.