# Data persistence for the notes of the Unit 4 - ADVANCED I/O INTERFACING in the subject of PROGRAMMING AND INTERFACING WITH MICROCONTROLLERS

- Data persistence is the longevity of data after the application that created it has been closed.
- Data persistence is important in programming because it means that data can be accessed from different applications, devices, and operating systems.
- Data persistence requires the data to be written to non-volatile storage, such as flash or EEPROM, which can retain the information long-term, even if the power is removed  .
- Data persistence in microcontrollers involves using driver code that manipulates the control registers as necessary to write data to flash or EEPROM.
- Data persistence in microcontrollers also involves ensuring that the startup code does not initialize the portion of RAM where the persistent data is located.
- Data persistence in microcontrollers may also involve using external devices, such as FRAM, that can store data using the I2C interface.
- Data persistence in microcontrollers should also include data integrity checks, such as CRC-16 or CRC-32, to verify the data when reading or writing.