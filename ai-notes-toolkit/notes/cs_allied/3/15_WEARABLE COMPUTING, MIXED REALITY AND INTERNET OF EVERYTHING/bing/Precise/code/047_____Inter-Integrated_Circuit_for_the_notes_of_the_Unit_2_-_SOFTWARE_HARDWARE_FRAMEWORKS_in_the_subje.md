### Inter-Integrated Circuit

Inter-Integrated Circuit (I2C) is a multi-master, multi-slave, packet-switched, single-ended, serial computer bus invented in 1982 by Philips Semiconductor (now NXP Semiconductors). It is widely used for attaching lower-speed peripheral ICs to processors and microcontrollers in short-distance, intra-board communication.

Some key features of I2C include:
- It uses only two bidirectional open-drain lines, Serial Data Line (SDA) and Serial Clock Line (SCL), pulled up with resistors.
- Typical voltages used are +5 V or +3.3 V, although systems with other voltages are permitted.
- The I2C reference design has a 7-bit or a 10-bit (depending on the device used) address space.
- Data is transferred in sequences of 8 bits.
- The maximum data rate is specified at 3.4 Mbit/s in High-Speed Mode (Hs-mode), although faster unofficial rates have been reported.

I2C is appropriate for peripherals where simplicity and low manufacturing cost are more important than speed. Common applications of the I2C bus include EEPROMs, thermal sensors, and real-time clocks. I2C is also used in microcontroller-based projects and other electronic projects. It is a popular protocol for inter-chip communication in embedded systems.