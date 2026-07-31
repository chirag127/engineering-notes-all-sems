# Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Pin diagram of 8085 microprocessor

- The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time.
- It has 40 pins and requires a +5V power supply.
- The pin diagram of 8085 microprocessor is shown below:

![Pin diagram of 8085 microprocessor](https://electronicsdesk.com/wp-content/uploads/2019/06/Pin-Diagram-of-8085-Microprocessor.png)

- The pins can be classified into six groups:

  - Address and data bus: These are 16 address lines (A0-A15) and 8 data lines (D0-D7) that are used to communicate with the external memory and I/O devices. The address bus is unidirectional and the data bus is bidirectional.
  - Control and status signals: These are 6 signals that are used to control the read and write operations, and to indicate the status of the microprocessor. They are:

    - RD (Read): This is an active low signal that indicates that the microprocessor is reading data from the memory or I/O device.
    - WR (Write): This is an active low signal that indicates that the microprocessor is writing data to the memory or I/O device.
    - IO/M (Input/Output or Memory): This is a signal that distinguishes between memory and I/O operations. It is high for I/O operations and low for memory operations.
    - S0 and S1 (Status): These are two signals that indicate the type of operation being performed by the microprocessor. They can have four possible values:

      - 00: Halt
      - 01: Write
      - 10: Read
      - 11: Fetch

    - READY: This is a signal that indicates whether the memory or I/O device is ready to accept or send data. It is high when ready and low when not ready.

  - Power supply and clock signals: These are 3 signals that are used to provide power and timing to the microprocessor. They are:

    - Vcc: This is the +5V power supply pin.
    - Vss: This is the ground pin.
    - X1 and X2: These are the pins that are connected to an external crystal oscillator that generates the clock signal for the microprocessor. The frequency of the clock signal is 3 MHz.

  - Externally initiated signals: These are 4 signals that are used to interrupt, reset, or hold the microprocessor. They are:

    - INTR (Interrupt Request): This is an active high signal that requests the microprocessor to execute an interrupt service routine. The microprocessor acknowledges this signal by sending an INTA (Interrupt Acknowledge) signal.
    - RST 5.5, RST 6.5, and RST 7.5 (Restart): These are three active high signals that cause the microprocessor to execute a restart service routine. The microprocessor jumps to a predefined memory location depending on the signal:

      - RST 5.5: 002CH
      - RST 6.5: 0034H
      - RST 7.5: 003CH

    - RST (Reset): This is an active high signal that resets the microprocessor and initializes the registers and flags. The microprocessor jumps to the memory location 0000H after reset.
    - HOLD (Hold): This is an active high signal that requests the microprocessor to relinquish the control of the address and data bus. The microprocessor acknowledges this signal by sending an HLDA (Hold Acknowledge) signal and enters the hold state.

  - Serial I/O ports: These are 2 pins that are used to perform serial data communication with other devices. They are:

    - SID (Serial Input Data): This is the pin that receives serial data from an external device.
    - SOD (Serial Output Data): This is the pin that sends serial data to an external device.

  - Other pins: These are 5 pins that have miscellaneous functions. They are:

    - ALE (Address Latch Enable): This is an active high signal that is used to separate the address and data on the multiplexed address and data bus. It