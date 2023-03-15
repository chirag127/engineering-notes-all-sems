# Control and Status for 8085 Microprocessor

- The 8085 microprocessor provides two control signals, **RD** and **WR**, to initiate read or write cycle.
- These signals are used both for reading/writing memory and for reading/writing an input/output device.
- The 8085 microprocessor also provides a signal, **IO/M**, to indicate whether the initiated cycle is for an I/O device or for a memory device.
- The **IO/M** signal is high for I/O operations and low for memory operations.
- The control signals are synchronized with the system clock by the timing and control unit of the 8085 microprocessor.
- The timing and control unit also generates other signals, such as **ALE**, **S0**, **S1**, and **READY**, to coordinate the data transfer between the microprocessor and the external devices.
- The **ALE** (Address Latch Enable) signal is used to separate the address and data lines of the multiplexed bus AD7-AD0.
- The **ALE** signal is high during the first clock cycle of every machine cycle and low during the remaining clock cycles.
- The **ALE** signal enables the external latch to store the address bits from AD7-AD0 and make them available on the address bus A7-A0.
- The **S0** and **S1** (Status) signals are used to indicate the type of the current machine cycle.
- The **S0** and **S1** signals can have four possible combinations: 00 for halt, 01 for write, 10 for read, and 11 for fetch.
- The **READY** signal is used to indicate whether the external device is ready for data transfer or not.
- The **READY** signal is high when the device is ready and low when the device is not ready.
- The **READY** signal can be used to insert wait states in the machine cycle to synchronize the microprocessor with slower devices.
- The 8085 microprocessor also supports serial communication through two pins, **SID** (Serial Input Data) and **SOD** (Serial Output Data).
- The timing and control of serial communication is managed by the 8085’s internal circuitry.
- The 8085 microprocessor also has two special purpose registers, the **Serial Control Register (SC)** and the **Serial Shift Register (SS)**, which are used to control and monitor the serial communication.

: https://www.eeeguide.com/control-signals-of-8085/
: https://www.tutorialspoint.com/microprocessor/microprocessor_8085_pin_configuration.htm
: https://www.geeksforgeeks.org/pin-diagram-8085-microprocessor/
: https://www.geeksforgeeks.org/architecture-of-8085-microprocessor/
: https://www.tutorialspoint.com/microprocessor/microprocessor_8085_architecture.htm