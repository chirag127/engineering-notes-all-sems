# Unit 3 - Control Unit: Concept of Horizontal and Vertical Microprogramming

Microprogramming is a technique used to implement the control unit of a computer's central processing unit (CPU). It involves storing a sequence of microinstructions in a control memory, which define the behavior of the control unit. There are two types of microprogramming: horizontal and vertical.

1. **Horizontal microprogramming**: In horizontal microprogramming, each microinstruction specifies one or more micro-operations to be performed in parallel. This is achieved by having a wide microinstruction word, where each bit or group of bits corresponds to a specific control signal or group of control signals. Horizontal microprogramming allows for a high degree of parallelism, but requires a large control memory to store the wide microinstructions.

2. **Vertical microprogramming**: In vertical microprogramming, each microinstruction specifies a single micro-operation to be performed. This is achieved by having a narrow microinstruction word, where each microinstruction is encoded using a small number of bits. Vertical microprogramming requires less control memory than horizontal microprogramming, but allows for less parallelism.

The choice between horizontal and vertical microprogramming depends on the specific design goals and constraints of the CPU. Some CPUs use a combination of both horizontal and vertical microprogramming to balance the trade-offs between control memory size and parallelism.