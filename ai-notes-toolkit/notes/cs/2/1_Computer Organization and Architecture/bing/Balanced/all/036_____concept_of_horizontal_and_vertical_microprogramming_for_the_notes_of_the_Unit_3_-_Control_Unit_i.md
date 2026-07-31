# Concept of Horizontal and Vertical Microprogramming

- Microprogramming is a technique to implement the control unit of a processor using a small memory that stores microinstructions.
- Microinstructions are low-level instructions that specify the control signals for each step of the instruction cycle.
- There are two main types of microprogramming: horizontal and vertical.

## Horizontal Microprogramming

- In horizontal microprogramming, each microinstruction has one bit for each control signal in the data-path.
- The microinstruction is directly decoded by the control unit and sent to the data-path components.
- Horizontal microprogramming has the following advantages:
  - It allows a high degree of parallelism and flexibility in the data-path operations.
  - It reduces the number of microinstructions needed to implement a given instruction set.
- Horizontal microprogramming has the following disadvantages:
  - It requires a large and wide memory to store the microinstructions.
  - It increases the complexity and cost of the control unit circuitry.

## Vertical Microprogramming

- In vertical microprogramming, each microinstruction has a smaller number of bits than the control signals in the data-path.
- The microinstruction is encoded using a function code that represents a group of control signals.
- The microinstruction is decoded by an instruction decoder that generates the control signals for the data-path components.
- Vertical microprogramming has the following advantages:
  - It reduces the size and width of the memory needed to store the microinstructions.
  - It simplifies the control unit circuitry and reduces the cost.
- Vertical microprogramming has the following disadvantages:
  - It limits the parallelism and flexibility in the data-path operations.
  - It increases the number of microinstructions needed to implement a given instruction set.