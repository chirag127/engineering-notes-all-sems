### Control and Status for the Notes of the Unit 2

- Control and status signals are used to identify the nature of operation, such as memory read, memory write, I/O read, I/O write, etc.
- The 8085 microprocessor provides two control signals: RD (read) and WR (write) to initiate read or write cycle.
- The 8085 microprocessor also provides a signal IO/M (input/output or memory) to indicate whether the initiated cycle is for I/O device or for memory device.
- The truth table for the control and status signals is as follows:

| IO/M | RD | WR | Operation |
|------|----|----|-----------|
| 0    | 0  | 1  | Memory read |
| 0    | 1  | 0  | Memory write |
| 1    | 0  | 1  | I/O read |
| 1    | 1  | 0  | I/O write |

- The 8085 microprocessor also provides some status signals, such as S0 and S1, to indicate the type of current machine cycle.
- The truth table for the status signals is as follows:

| S1 | S0 | Machine cycle |
|----|----|---------------|
| 0  | 0  | Halt |
| 0  | 1  | Write |
| 1  | 0  | Read |
| 1  | 1  | Fetch |

- The 8085 microprocessor also provides some other signals, such as ALE (address latch enable), which is used to separate the address and data from the multiplexed address/data bus.
- The 8085 microprocessor also provides some serial communication signals, such as SID (serial input data) and SOD (serial output data), which are used to transmit and receive one bit of data at a time.
- The timing and control of serial communication is managed by the 8085’s internal circuitry. The 8085 also has two special purpose registers, the Serial Control Register (SC) and the Serial Shift Register (SS), which are used to control and monitor the serial communication.