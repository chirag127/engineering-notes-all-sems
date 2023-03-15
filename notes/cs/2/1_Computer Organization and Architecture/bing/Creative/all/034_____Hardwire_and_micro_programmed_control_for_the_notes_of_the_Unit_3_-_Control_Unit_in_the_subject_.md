# Hardwired and Microprogrammed Control Unit

A control unit is a component of a CPU that generates control signals to execute instructions. There are two main types of control units: hardwired and microprogrammed.

## Hardwired Control Unit

- A hardwired control unit is a sequential circuit that generates control signals based on the current state, the instruction register, the condition codes, and the external inputs  .
- A hardwired control unit is designed for a specific instruction set, usually RISC style.
- A hardwired control unit is faster and more efficient than a microprogrammed control unit, but it is more complex and difficult to design and modify  .

## Microprogrammed Control Unit

- A microprogrammed control unit is a unit that executes a program of microinstructions stored in a control memory to generate control signals   .
- A microinstruction is a small instruction that specifies one or more micro-operations, such as fetching, decoding, executing, and storing .
- A microprogrammed control unit is designed for a general instruction set, usually CISC style.
- A microprogrammed control unit is slower and less efficient than a hardwired control unit, but it is more flexible and easier to design and modify  .

## Comparison

| Hardwired Control Unit | Microprogrammed Control Unit |
| ---------------------- | ---------------------------- |
| Circuit-based approach | Programming-based approach |
| RISC style instruction set | CISC style instruction set |
| Faster and more efficient | Slower and less efficient |
| More complex and difficult to design and modify | More flexible and easier to design and modify |