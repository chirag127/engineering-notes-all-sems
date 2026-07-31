## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

### Pin diagram of 8085 microprocessor

The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has a 16-bit address bus that can address up to 64 KB of memory. It is a 40-pin IC that operates with a +5V power supply. The pin diagram of 8085 microprocessor is shown below:

![Pin diagram of 8085 microprocessor](https://electronicsdesk.com/wp-content/uploads/2019/06/Pin-Diagram-of-8085-Microprocessor.png)

The pins of the 8085 microprocessor can be classified into six groups:

- **Address and data bus**: These are 16 address lines (A0-A15) and 8 data lines (D0-D7) that are multiplexed, i.e., they share the same pins. The address bus is unidirectional and the data bus is bidirectional. The address and data bus are used to communicate with the memory and I/O devices.
- **Control and status signals**: These are 6 signals that are used to control the operation of the microprocessor and indicate its status. They are:
  - **ALE (Address Latch Enable)**: This is an output signal that indicates when the address is available on the address/data bus. It is used to latch the address from the multiplexed bus using an external latch.
  - **RD (Read)**: This is an active low output signal that indicates when the microprocessor is reading data from the memory or I/O device.
  - **WR (Write)**: This is an active low output signal that indicates when the microprocessor is writing data to the memory or I/O device.
  - **IO/M (Input/Output or Memory)**: This is an output signal that indicates whether the address on the bus is for an I/O device or a memory location. It is high for I/O and low for memory.
  - **S0 and S1 (Status)**: These are two output signals that indicate the status of the microprocessor. They can have four possible values:
    - 00: Halt state
    - 01: Write state
    - 10: Read state
    - 11: Fetch state
- **Power supply and clock signals**: These are 3 signals that are used to provide power and timing to the microprocessor. They are:
  - **Vcc**: This is the +5V power supply pin.
  - **Vss**: This is the ground pin.
  - **X1 and X2**: These are the two pins that are connected to an external crystal oscillator or clock generator circuit that provides the clock pulses to the microprocessor. The frequency of the clock is typically 3 MHz or 6 MHz.
- **Interrupt signals**: These are 5 signals that are used to request the microprocessor to stop its current operation and execute a subroutine. They are:
  - **TRAP**: This is a non-maskable interrupt that has the highest priority. It is an edge-triggered interrupt that cannot be disabled by any instruction. It is used for critical events such as power failure or emergency stop.
  - **RST 7.5, RST 6.5, and RST 5.5**: These are maskable interrupts that have fixed priorities and vector addresses. They are level-triggered interrupts that can be enabled or disabled by the EI (Enable Interrupt) and DI (Disable Interrupt) instructions. They are used for general-purpose applications such as keyboard input or printer output.
  - **INTR**: This is a maskable interrupt that has the lowest priority. It is an edge-triggered interrupt that can be enabled or disabled by the EI and DI instructions. It is used for external devices that can generate variable vector addresses using an external device called an interrupt controller.
- **Serial I/O signals**: These are 2 signals that are used to perform serial data communication with external devices. They are:
  - **SID (Serial Input Data)**: This is an input signal that is used to read serial data from an external device such as a keyboard or a modem.
  - **SOD (Serial Output Data)**: This is an output signal that is used to send serial data to an external device