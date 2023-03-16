### I2C/IIC

- I2C or IIC stands for Inter-Integrated Circuit, a serial communication protocol invented by Philips Semiconductor (now NXP Semiconductor) in 1982.
- It is designed for communication between chips on the same Printed Circuit Board (PCB) or within a short distance .
- It is a synchronous, multi-master/multi-slave, packet-switched, single-ended bus that uses two wires: Serial Data Line (SDA) and Serial Clock Line (SCL) .
- The SCL is controlled by the master device, which generates clock pulses at a regular interval. The SDA is used to transfer data bits between the master and the slave devices .
- The data transfer is synchronized to the rising edge of the clock pulse, meaning that a single bit of data is sent or received when the SCL changes from low to high.
- The I2C protocol supports multiple masters and slaves on the same bus, which can communicate with each other by using unique addresses .
- The I2C protocol also supports arbitration and collision detection, which means that if two or more masters try to access the bus at the same time, only one of them will be able to do so, and the others will wait until the bus is free .
- The I2C protocol has several advantages, such as simplicity, flexibility, low cost, low power consumption, and high speed .
- The I2C protocol has some limitations, such as limited bus length, limited number of devices, limited data rate, and susceptibility to noise .
- The I2C protocol is widely used in various applications, such as sensors, EEPROMs, LCDs, RTCs, and microcontrollers  .