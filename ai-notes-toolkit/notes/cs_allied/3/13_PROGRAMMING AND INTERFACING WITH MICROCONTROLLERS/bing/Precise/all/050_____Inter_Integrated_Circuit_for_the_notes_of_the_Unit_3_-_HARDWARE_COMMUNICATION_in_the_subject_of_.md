### Inter-Integrated Circuit

Inter-Integrated Circuit (I2C) is a multi-master, multi-slave, packet-switched, single-ended, serial computer bus invented in 1982 by Philips Semiconductor (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication.

Some key features of I2C include:
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- Typical voltages used are +5 V or +3.3 V, although systems with other voltages are permitted.
- The I2C reference design specifies 100 kbit/s in standard mode (SM) or 10 kbit/s in low-speed mode (LSM), but devices can communicate at several other speeds.
- The maximum number of nodes is limited by the address space, and also by the total bus capacitance of 400 pF, which restricts practical communication distances to a few meters.

I2C is appropriate for peripherals where simplicity and low manufacturing cost are more important than speed. Common applications of the I2C bus include:
- Reading configuration data from SPD EEPROMs on DIMMs.
- Reading temperature, voltage, and fan speed sensors.
- Controlling OLED or LCD displays, including setting contrast and brightness.
- Accessing real-time clocks, digital potentiometers, and analog-to-digital converters.
- Changing volume or tone controls in digital audio equipment.
