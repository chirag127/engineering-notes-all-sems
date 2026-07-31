## Design the control unit of a computer using either hardwiring or microprogramming based on its register transfer language description

- The control unit is the part of the CPU that generates the control signals to coordinate the execution of instructions.
- The control signals are based on the instruction code and the current state of the CPU.
- The control unit can be designed using either hardwiring or microprogramming techniques.
- Hardwiring is the method of implementing the control logic using combinational circuits, such as multiplexers, decoders, and gates.
- Microprogramming is the method of implementing the control logic using a small program stored in a read-only memory (ROM) or a writable control store (WCS).
- The program consists of a sequence of microinstructions, each of which specifies a set of control signals for one or more clock cycles.
- The register transfer language (RTL) is a notation for describing the operations and data transfers of an instruction at the register level.
- The RTL can be used to specify the behavior of the control unit for each instruction in the instruction set architecture (ISA).
- The RTL can be translated into a state diagram, which shows the sequence of states and transitions for each instruction cycle.
- The state diagram can be used to design the control unit using either hardwiring or microprogramming.

### Hardwired Control Unit Design Steps

- The logic designer is expected to have written the RTL description of each instruction execution in the ISA.
- Then the design is a three-step activity:
  - Step 1: Transform RTL into a state diagram for each machine cycle of the ISA instruction set. This helps in determining which output signals should be asserted in each timing state.
  - Step 2: Encode the states using a state register and a state decoder. The state register holds the current state of the control unit, and the state decoder generates the state signals for the combinational logic.
  - Step 3: Design the combinational logic that generates the control signals based on the state signals, the instruction code, and the status flags. The control signals are fed back to the state register to update the next state.

### Microprogrammed Control Unit Design Steps

- As in the case of hardwired control unit, transform RTL into a state diagram for each machine cycle of the ISA instruction set. This helps in determining which output signals should be asserted in each timing state.
- Then the design is a two-step activity:
  - Step 1: Encode the state diagram into a microprogram, which is a sequence of microinstructions stored in a ROM or a WCS. Each microinstruction specifies a set of control signals and a next address field, which can be conditional or unconditional.
  - Step 2: Design the microprogram control unit, which consists of a microprogram counter (MPC), a microinstruction register (MIR), and a next address logic. The MPC holds the address of the current microinstruction, the MIR holds the contents of the current microinstruction, and the next address logic determines the address of the next microinstruction based on the next address field and the status flags. The control signals are generated from the MIR and fed back to the MPC to update the next address.