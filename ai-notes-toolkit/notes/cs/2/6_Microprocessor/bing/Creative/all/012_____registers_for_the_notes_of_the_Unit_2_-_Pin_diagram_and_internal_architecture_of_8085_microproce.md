# Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Pin diagram of 8085 microprocessor

- The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has 40 pins and requires a +5V power supply. The pin diagram of 8085 microprocessor is shown below   :

![Pin diagram of 8085 microprocessor](https://electronicsdesk.com/wp-content/uploads/2019/10/Pin-Diagram-of-8085-Microprocessor.png)

- The pins of the 8085 microprocessor can be classified into six groups:

  - Address and data bus: These are 16 address lines (A0-A15) and 8 data lines (D0-D7) that are used to communicate with the external memory and I/O devices. The address bus is unidirectional, while the data bus is bidirectional. The address and data lines are multiplexed, meaning that they share the same pins. The lower 8 address lines (A0-A7) are multiplexed with the data lines (D0-D7), and the higher 8 address lines (A8-A15) are multiplexed with the status signals (IO/M, S0, S1). To separate the address and data signals, a demultiplexer or a latch is used.

  - Control and status signals: These are 4 signals that indicate the status of the microprocessor and the type of operation being performed. They are:

    - IO/M: This signal specifies whether the operation is a memory operation or an I/O operation. It is low (0) for memory and high (1) for I/O.
    - S0 and S1: These two signals specify the type of operation as follows:

      | S1 | S0 | Operation |
      |----|----|-----------|
      | 0  | 0  | HALT      |
      | 0  | 1  | WRITE     |
      | 1  | 0  | READ      |
      | 1  | 1  | FETCH     |

    - RD: This signal is low (0) when the microprocessor reads data from the memory or an I/O device.
    - WR: This signal is low (0) when the microprocessor writes data to the memory or an I/O device.

  - Power supply and clock signals: These are 3 signals that provide the power and the timing for the microprocessor. They are:

    - Vcc: This is the +5V power supply pin.
    - Vss: This is the ground pin.
    - X1 and X2: These are the input pins for the crystal oscillator that generates the clock signal for the microprocessor. The frequency of the clock signal is 6.144 MHz.

  - Externally initiated signals: These are 5 signals that are initiated by external devices to communicate with the microprocessor. They are:

    - RESET IN: This signal is used to reset the microprocessor and initialize the registers and the program counter. It is an active high signal, meaning that it resets the microprocessor when it is high (1).
    - RESET OUT: This signal is used to reset the external devices connected to the microprocessor. It is an active low signal, meaning that it resets the devices when it is low (0).
    - READY: This signal is used to synchronize the microprocessor with the slower devices. It is an active high signal, meaning that it indicates that the device is ready to send or receive data when it is high (1).
    - HOLD: This signal is used by an external device to request the microprocessor to relinquish the control of the buses. It is an active high signal, meaning that it requests the hold when it is high (1).
    - HLDA: This signal is used by the microprocessor to acknowledge the hold request. It is an active high signal, meaning that it indicates that the microprocessor has granted the hold when it is high (1).

  - Serial I/O ports: These are 2 pins that are used for serial data communication. They are:

    - SID: This is the serial input data pin. It is used to receive serial data from