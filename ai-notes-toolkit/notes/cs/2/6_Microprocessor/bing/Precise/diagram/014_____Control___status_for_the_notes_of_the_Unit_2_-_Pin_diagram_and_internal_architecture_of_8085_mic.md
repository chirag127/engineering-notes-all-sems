### Control & Status

Control and status are important components of the 8085 microprocessor. The control unit is responsible for managing the flow of data and instructions within the microprocessor, while the status register provides information about the current state of the microprocessor.

- The control unit manages the flow of data and instructions within the microprocessor by generating control signals that direct the operation of the other components of the microprocessor.
- The status register is a register that provides information about the current state of the microprocessor. It contains flags that indicate the results of arithmetic and logical operations, as well as other conditions such as the presence of an interrupt request.
- The 8085 microprocessor has five flags in the status register: Sign, Zero, Auxiliary Carry, Parity, and Carry.
- The Sign flag is set if the result of an operation is negative.
- The Zero flag is set if the result of an operation is zero.
- The Auxiliary Carry flag is set if there is a carry from the lower half of the result to the upper half during an arithmetic operation.
- The Parity flag is set if the result of an operation has an even number of 1s in its binary representation.
- The Carry flag is set if there is a carry out of the most significant bit during an arithmetic operation.
- The status register can be accessed by certain instructions, allowing the programmer to make decisions based on the current state of the microprocessor.