# Microprogram Sequencing

- Microprogram sequencing is the process of generating the addresses of the microinstructions stored in the control memory of a microprogrammed control unit .
- The microinstructions contain the control signals that specify the operations of the data path components of the CPU .
- The microprogram sequencer is the component that performs the microprogram sequencing. It can be designed with different techniques and features to suit the requirements of the CPU  .
- Some of the factors that affect the design of the microprogram sequencer are:
  - The size of the microinstruction: The number of bits needed to encode the control signals and the address fields.
  - The time of execution: The number of clock cycles needed to fetch and execute a microinstruction.
  - The branching capability: The ability to alter the normal sequential order of microinstructions based on some conditions or inputs.
  - The addressing mode: The way of specifying the next microinstruction address in the current microinstruction.
- Some of the common techniques for microprogram sequencing are:
  - Horizontal microprogramming: The microinstruction contains all the control signals in parallel, and the next address is calculated by incrementing the current address by one.
  - Vertical microprogramming: The microinstruction contains a subset of the control signals in serial, and the next address is specified by an address field in the microinstruction.
  - Hybrid microprogramming: A combination of horizontal and vertical microprogramming, where the microinstruction contains some control signals in parallel and some in serial, and the next address can be calculated or specified by an address field.
  - Conditional microprogramming: The microinstruction contains a condition field that determines whether the next address is calculated or specified by an address field, based on the outcome of some test or input.
  - Subroutine microprogramming: The microinstruction contains a subroutine field that allows the microprogram to call another microprogram and return to the original microprogram after completion.