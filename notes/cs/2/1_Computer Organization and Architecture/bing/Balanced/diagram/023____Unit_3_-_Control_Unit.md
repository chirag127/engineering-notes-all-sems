## Unit 3 - Control Unit

- The control unit (CU) is a component of the central processing unit (CPU) that directs the operation of the processor.
- The control unit generates control signals that instruct the arithmetic logic unit (ALU), the memory, and the input/output devices on how to respond to the instructions fetched from the memory.
- The control unit can be classified into two types: hardwired control unit and microprogrammed control unit.
- A hardwired control unit is a circuit that implements a fixed set of control signals based on the current instruction and the state of the processor. A hardwired control unit is fast, but inflexible and difficult to modify.
- A microprogrammed control unit is a circuit that executes a microprogram, which is a sequence of microinstructions stored in a control memory. A microinstruction specifies a set of control signals for one or more clock cycles. A microprogrammed control unit is flexible and easy to modify, but slower than a hardwired control unit.
- The control unit can also be classified into two modes: single-cycle mode and multi-cycle mode.
- In single-cycle mode, the control unit executes one instruction in one clock cycle. This means that all the instruction phases (fetch, decode, execute, memory access, and write back) are performed in parallel within one cycle. A single-cycle mode requires a high clock frequency and a complex control unit, but achieves a high instruction throughput.
- In multi-cycle mode, the control unit executes one instruction in multiple clock cycles. This means that the instruction phases are performed sequentially, one per cycle. A multi-cycle mode requires a lower clock frequency and a simpler control unit, but achieves a lower instruction throughput.