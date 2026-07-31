# Concept of Horizontal and Vertical Microprogramming

- Microprogramming is a technique to implement the control unit of a processor using a microprogram, which is a sequence of microinstructions stored in a control memory (ROM or RAM).
- Each microinstruction specifies one or more micro-operations to be performed by the processor, such as fetching an instruction, decoding it, executing it, updating the program counter, etc.
- Microinstructions can be classified into two types: horizontal and vertical, depending on the format and encoding of the control bits.

## Horizontal Microprogramming

- In horizontal microprogramming, each microinstruction has a wide format, with one bit for each control point in the data-path.
- The control bits are not encoded, and each bit directly controls a specific micro-operation, such as enabling a register, selecting an ALU operation, setting a flag, etc.
- Horizontal microinstructions have the following advantages:
  - They allow a high degree of parallelism, as multiple micro-operations can be performed simultaneously in one microinstruction cycle.
  - They are flexible and easy to modify, as new micro-operations can be added by simply adding more control bits.
- Horizontal microinstructions have the following disadvantages:
  - They require a large control memory, as each microinstruction has a large number of bits.
  - They are slow, as the control memory access time and the decoding time are proportional to the width of the microinstruction.

## Vertical Microprogramming

- In vertical microprogramming, each microinstruction has a narrow format, with fewer bits than the number of control points in the data-path.
- The control bits are encoded, and each bit or group of bits represents a function code that specifies a set of micro-operations to be performed by the processor.
- An instruction decoder is used to decode the function code into multiple control signals that control the data-path components.
- Vertical microinstructions have the following advantages:
  - They require a smaller control memory, as each microinstruction has a smaller number of bits.
  - They are fast, as the control memory access time and the decoding time are independent of the width of the microinstruction.
- Vertical microinstructions have the following disadvantages:
  - They allow a lower degree of parallelism, as fewer micro-operations can be performed simultaneously in one microinstruction cycle.
  - They are less flexible and harder to modify, as new micro-operations require changing the encoding scheme and the instruction decoder.