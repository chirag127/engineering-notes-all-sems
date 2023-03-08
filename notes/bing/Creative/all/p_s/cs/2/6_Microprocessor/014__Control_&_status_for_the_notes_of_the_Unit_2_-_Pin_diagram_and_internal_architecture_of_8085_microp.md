### Control & Status

- The 8085 microprocessor has several control and status signals that are used to communicate with external devices, such as memory, I/O, and peripherals.
- The control signals are used to initiate read or write cycles, to select memory or I/O devices, and to enable or disable interrupts.
- The status signals are used to indicate the current state of the microprocessor, such as the type of operation, the status of the flags, and the status of the serial communication.
- The control and status signals of the 8085 microprocessor are as follows:

| Signal | Type | Description |
| ------ | ---- | ----------- |
| ALE | Output | Address Latch Enable. It is a pulse signal that goes high during the first clock cycle of every machine cycle. It is used to latch the lower 8 bits of the address from the multiplexed address/data bus (AD7-AD0) into an external latch. |
| RD | Output | Read. It is an active low signal that goes low when the microprocessor wants to read data from memory or I/O devices. |
| WR | Output | Write. It is an active low signal that goes low when the microprocessor wants to write data to memory or I/O devices. |
| IO/M | Output | I/O or Memory. It is a signal that indicates whether the microprocessor is accessing memory or I/O devices. It is high for I/O operations and low for memory operations. |
| S1 and S0 | Output | Status. These are two signals that indicate the type of current operation. They can have four possible values: 00 for Halt, 01 for Write, 10 for Read, and 11 for Fetch. |
| INTA | Output | Interrupt Acknowledge. It is an active low signal that goes low when the microprocessor acknowledges an interrupt request from an external device. |
| INTR | Input | Interrupt Request. It is a maskable interrupt signal that can be enabled or disabled by software. It is sampled during the last clock cycle of the instruction and if it is high, the microprocessor executes an interrupt service routine after completing the current instruction. |
| RST 7.5, RST 6.5, RST 5.5 | Input | Restart. These are three maskable interrupt signals that have a fixed priority and vector address. They are edge-triggered and can be enabled or disabled by software. They are sampled during the T3 and T4 states of the instruction cycle and if any of them is high, the microprocessor executes an interrupt service routine after completing the current instruction. The vector addresses are 003CH, 0034H, and 002CH respectively. |
| TRAP | Input | Trap. It is a non-maskable interrupt signal that has the highest priority among all interrupts. It is edge and level triggered and cannot be disabled by software. It is sampled during the T4 state of the instruction cycle and if it is high, the microprocessor executes an interrupt service routine after completing the current instruction. The vector address is 0024H. |
| HOLD | Input | Hold. It is a signal that requests the microprocessor to relinquish the control of the address, data, and control buses to another device, such as a DMA controller. It is sampled at the end of each machine cycle and if it is high, the microprocessor completes the current machine cycle and then goes to the hold state. |
| HLDA | Output | Hold Acknowledge. It is a signal that indicates that the microprocessor has entered the hold state and has released the buses. It remains high as long as the hold signal is high. |
| READY | Input | Ready. It is a signal that indicates whether the memory or I/O device is ready to send or receive data. It is sampled at the end of T2 state and if it is low, the microprocessor inserts wait states until it goes high. |
| SID | Input | Serial Input Data. It is a signal that is used to input serial data into the microprocessor. It is controlled by the Serial Control Register (SC) and the Serial Shift Register (SS). |
| SOD | Output | Serial Output Data. It is a signal that is used to output serial data from the microprocessor. It is controlled by the Serial Control Register (SC) and the Serial Shift Register (SS). |
| RESET IN | Input | Reset. It is a signal that is used to reset the microprocessor and initialize its registers. It must be high for at least three clock cycles to reset the microprocessor. |
| RESET

Some possible mnemonics and learning tricks for the topic are:

- To remember the order of the three maskable interrupts, you can use the acronym **RST** which stands for **R**estart, **S**top, and **T**rap. The numbers 7.5, 6.5, and 5.5 are in descending order of priority and vector address.
- To remember the four possible values of the status signals S1 and S0, you can use the acronym **HAWRF** which stands for **H**alt, **A**ddress, **W**rite, **R**ead, and **F**etch. The binary values are 00, 01, 10, and 11 respectively.
- To remember the difference between IO/M and RD/WR signals, you can use the following trick: IO/M is high for I/O and low for memory, while RD is low for read and WR is low for write. So, the signals are opposite to their names.