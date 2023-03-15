# Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Pin diagram of 8085 microprocessor

- The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has 40 pins and requires a +5V power supply. The pin diagram of 8085 microprocessor is shown below:

![Pin diagram of 8085 microprocessor](https://electronicsdesk.com/wp-content/uploads/2019/04/Pin-Diagram-of-8085-Microprocessor.png)

- The pins of the 8085 microprocessor can be classified into six groups:

  - Address and data bus: These are 16 address lines (A0-A15) and 8 data lines (D0-D7) that are used to communicate with the memory and I/O devices. The address bus is unidirectional, while the data bus is bidirectional. The address bus can address up to 64 KB of memory. The data bus can transfer 8 bits of data at a time.
  - Control and status signals: These are 6 pins that are used to control the operation of the microprocessor and indicate its status. They are:

    - ALE (Address Latch Enable): This is an output signal that indicates when the address bus contains a valid address. It is used to latch the address from the address bus into an external latch.
    - RD (Read): This is an active low output signal that indicates when the microprocessor is reading data from the memory or I/O device.
    - WR (Write): This is an active low output signal that indicates when the microprocessor is writing data to the memory or I/O device.
    - IO/M (Input/Output or Memory): This is an output signal that indicates whether the address on the address bus is for an I/O device or a memory location. It is high for I/O and low for memory.
    - S0 and S1 (Status): These are two output signals that indicate the status of the microprocessor. They can have four possible values:

      - 00: Halt state
      - 01: Write state
      - 10: Read state
      - 11: Fetch state

  - Power supply and clock signals: These are 3 pins that are used to provide power and timing to the microprocessor. They are:

    - Vcc: This is the +5V power supply pin.
    - Vss: This is the ground pin.
    - X1 and X2: These are two pins that are connected to an external crystal oscillator or a clock generator circuit. They provide the clock pulses to the microprocessor.

  - Externally initiated signals: These are 4 pins that are used to receive signals from external devices that can affect the operation of the microprocessor. They are:

    - RESET IN: This is an active high input signal that is used to reset the microprocessor and initialize its registers and flags. It also clears the interrupt enable and halt flags.
    - RESET OUT: This is an active low output signal that is used to reset the external devices connected to the microprocessor. It is activated after the RESET IN signal is deactivated.
    - READY: This is an active high input signal that is used to synchronize the microprocessor with the slower memory or I/O devices. It indicates when the device is ready to send or receive data. If the READY signal is low, the microprocessor waits until it becomes high before completing the data transfer.
    - HOLD: This is an active high input signal that is used to request the microprocessor to relinquish the control of the address, data and control buses. It is used by external devices that want to access the memory or I/O devices directly. The microprocessor acknowledges the request by activating the HLDA (Hold Acknowledge) signal and releasing the buses.
    - HLDA: This is an active high output signal that is used to acknowledge the HOLD request. It indicates that the microprocessor has released the buses and entered the hold state. It remains high until the HOLD signal is deactivated.

  - Serial I/O ports: These are 2 pins that are used to perform serial data communication with external devices. They are:

    - SID (Serial Input Data): This is an input pin that is used to receive serial data from an external device. The data