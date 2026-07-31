# Unit 2 - Pin diagram and internal architecture of 8085 microprocessor

## Pin diagram of 8085 microprocessor

The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has 40 pins and requires a +5V power supply. The pin diagram of 8085 microprocessor is shown below:

![Pin diagram of 8085 microprocessor](https://electronicsdesk.com/wp-content/uploads/2019/08/Pin-Diagram-of-8085-Microprocessor.png)

The pins of 8085 microprocessor can be classified into six groups:

- Address and data bus: These are 16 address lines (A0-A15) and 8 data lines (D0-D7) that are used to transfer the address and data between the microprocessor and the external devices. The address bus is unidirectional, while the data bus is bidirectional.
- Control and status signals: These are 6 signals that are used to control and monitor the operations of the microprocessor and the external devices. They are:
  - RD (Read): This is an active low signal that indicates that the microprocessor is reading data from the memory or an input device.
  - WR (Write): This is an active low signal that indicates that the microprocessor is writing data to the memory or an output device.
  - IO/M (Input/Output or Memory): This is a signal that distinguishes between an input/output operation and a memory operation. It is high for input/output and low for memory.
  - ALE (Address Latch Enable): This is a signal that enables the lower order address bus (A0-A7) to be latched by an external latch. This allows the multiplexed address and data bus to be separated.
  - S0 and S1 (Status): These are two signals that indicate the status of the current operation. They can have four possible values:
    - 00: Halt
    - 01: Write
    - 10: Read
    - 11: Fetch
- Power supply and clock signals: These are 3 signals that provide the power and the timing for the microprocessor. They are:
  - Vcc: This is the +5V power supply for the microprocessor.
  - Vss: This is the ground or 0V reference for the microprocessor.
  - X1 and X2: These are the two pins that are connected to an external crystal oscillator or a clock generator circuit. The frequency of the clock signal is 3 MHz or 6 MHz.
- Interrupts: These are 5 signals that are used to request the microprocessor to stop the current operation and execute a subroutine. They are:
  - TRAP: This is a non-maskable interrupt that has the highest priority. It is triggered by a positive edge and cannot be disabled by any instruction.
  - RST 7.5, RST 6.5, and RST 5.5: These are maskable interrupts that have fixed priorities and vector addresses. They are triggered by a high level and can be enabled or disabled by the EI (Enable Interrupt) and DI (Disable Interrupt) instructions.
  - INTR: This is a maskable interrupt that has the lowest priority and a variable vector address. It is triggered by a high level and can be enabled or disabled by the EI and DI instructions. It also requires an acknowledgment signal from the microprocessor, which is the INTA (Interrupt Acknowledge) signal.
- Serial input/output: These are 2 signals that are used to perform serial communication between the microprocessor and the external devices. They are:
  - SID (Serial Input Data): This is a signal that receives serial data from an external device. It is sampled by the microprocessor during the RIM (Read Interrupt Mask) instruction.
  - SOD (Serial Output Data): This is a signal that sends serial data to an external device. It is set or reset by the microprocessor during the SIM (Set Interrupt Mask) instruction.
- Other signals: These are 4 signals that are used for various purposes. They are:
  - RESET IN: This is a signal that resets the microprocessor and initializes the registers and the flags. It is triggered by a high level for at least three clock cycles.
  - RESET OUT: This is a signal that indicates that the microprocessor is being reset. It can be used to reset the external devices as well.
  - HOLD: This is a signal that requests the microprocessor to relinquish the control of the address