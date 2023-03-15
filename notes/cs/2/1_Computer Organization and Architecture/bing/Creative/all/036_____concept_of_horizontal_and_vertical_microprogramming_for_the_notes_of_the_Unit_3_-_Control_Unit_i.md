# Concept of Horizontal and Vertical Microprogramming

- Microprogramming is a technique to implement the control unit of a processor using a small memory that stores microinstructions.
- Microinstructions are low-level instructions that specify the control signals for each step of the instruction cycle.
- There are two main types of microprogramming: horizontal and vertical.

## Horizontal Microprogramming

- In horizontal microprogramming, the microinstructions are wide and have one bit for each control signal in the data-path.
- The microinstructions are written in a linear fashion, with each bit corresponding to a specific action to be performed by the processor.
- The advantages of horizontal microprogramming are:
  - It allows more flexibility and parallelism in the control unit design.
  - It reduces the number of microinstructions needed to implement a given instruction set.
  - It eliminates the need for an instruction decoder in the control unit.
- The disadvantages of horizontal microprogramming are:
  - It requires a large memory to store the microinstructions, which increases the cost and complexity of the control unit.
  - It requires a large number of wires to connect the memory to the data-path, which increases the delay and power consumption of the control unit.

## Vertical Microprogramming

- In vertical microprogramming, the microinstructions are narrow and have a few bits for each control signal in the data-path.
- The microinstructions are written in a hierarchical fashion, with each bit representing a code that is decoded into multiple control signals by an instruction decoder.
- The advantages of vertical microprogramming are:
  - It reduces the memory size and the number of wires needed to store and transmit the microinstructions, which decreases the cost and complexity of the control unit.
  - It allows more compact and efficient encoding of the microinstructions, which reduces the memory access time and power consumption of the control unit.
- The disadvantages of vertical microprogramming are:
  - It reduces the flexibility and parallelism in the control unit design.
  - It increases the number of microinstructions needed to implement a given instruction set.
  - It requires an instruction decoder in the control unit, which adds to the delay and complexity of the control unit.