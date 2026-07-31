### Inter-Integrated Circuit

Inter-Integrated Circuit (I2C) is a multi-master, multi-slave, packet switched, single-ended, serial computer bus invented in 1982 by Philips Semiconductor (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication.

Some key features of I2C include:
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- Typical voltages used are +5 V or +3.3 V, although systems with other voltages are permitted.
- The I2C specification defines the low-speed mode (10 kbit/s), the standard mode (100 kbit/s), the fast mode (400 kbit/s) and the high-speed mode (3.4 Mbit/s).
- Many devices can be connected to the same bus and each one can act as a master by initiating a data transfer.
- I2C is appropriate for peripherals where simplicity and low manufacturing cost are more important than speed.
