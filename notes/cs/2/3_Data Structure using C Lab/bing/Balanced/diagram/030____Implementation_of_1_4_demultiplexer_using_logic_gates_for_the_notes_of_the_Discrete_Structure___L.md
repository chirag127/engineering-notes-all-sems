## Implementation of 1:4 demultiplexer using logic gates

- A demultiplexer is a device that takes a single input and distributes it to one of several outputs depending on the values of some control signals.
- A 1:4 demultiplexer has one input, four outputs, and two control signals.
- The input is called D, the outputs are called Y0, Y1, Y2, and Y3, and the control signals are called S0 and S1.
- The truth table for a 1:4 demultiplexer is as follows:

| S1 | S0 | Y0 | Y1 | Y2 | Y3 |
|----|----|----|----|----|----|
| 0  | 0  | D  | 0  | 0  | 0  |
| 0  | 1  | 0  | D  | 0  | 0  |
| 1  | 0  | 0  | 0  | D  | 0  |
| 1  | 1  | 0  | 0  | 0  | D  |

- The output equations for a 1:4 demultiplexer are as follows:

  - Y0 = D * S1' * S0'
  - Y1 = D * S1' * S0
  - Y2 = D * S1 * S0'
  - Y3 = D * S1 * S0

- A 1:4 demultiplexer can be implemented using logic gates as shown in the following diagram:

```mermaid
graph LR
D -->|D| AND1
D -->|D| AND2
D -->|D| AND3
D -->|D| AND4
S0 -->|S0| NOT1
S1 -->|S1| NOT2
NOT1 -->|S0'| AND1
NOT1 -->|S0'| AND3
S0 -->|S0| AND2
S0 -->|S0| AND4
NOT2 -->|S1'| AND1
NOT2 -->|S1'| AND2
S1 -->|S1| AND3
S1 -->|S1| AND4
AND1 -->|Y0| Y0
AND2 -->|Y1| Y1
AND3 -->|Y2| Y2
AND4 -->|Y3| Y3
```