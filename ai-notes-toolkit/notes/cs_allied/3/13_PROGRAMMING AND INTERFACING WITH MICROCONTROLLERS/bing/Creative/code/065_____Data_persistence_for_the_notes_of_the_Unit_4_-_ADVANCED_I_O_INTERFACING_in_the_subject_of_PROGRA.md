### Data persistence for the notes of the Unit 4 - ADVANCED I/O INTERFACING in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- Data persistence is the longevity of data after the application that created it has been closed.
- Data persistence is important in programming because it means that data can be accessed from different applications, devices, and operating systems.
- Data persistence requires writing data to non-volatile storage, which is a type of memory that can retain information long-term, even if the power is removed .
- Non-volatile storage can be flash memory, EEPROM, or external devices such as SD cards or I2C FRAM .
- To write data to non-volatile storage, the microcontroller needs driver code that manipulates the control registers as necessary.
- To read data from non-volatile storage, the microcontroller needs to check the integrity of the data using CRC or checksum.
- To avoid data corruption, the microcontroller should write two copies of the data and compare them before reading.
- To optimize data persistence, the microcontroller should minimize the number of write cycles and use wear leveling techniques.