### Sub Cycles in Control Unit

The Control Unit (CU) is an essential component of the Central Processing Unit (CPU) responsible for managing the execution of instructions in a computer system. The CU uses a set of sub-cycles to perform the necessary tasks for processing instructions. This section describes the various sub-cycles in the Control Unit.

1. Fetch Cycle:
The first sub-cycle in the Control Unit is the Fetch Cycle, where the CU retrieves the instruction to be executed from the memory. The CU sends the address of the instruction to the Memory Unit (MU), which then returns the instruction to the CU.

2. Decode Cycle:
After fetching the instruction, the CU needs to decode it to understand what operation needs to be performed. The Decode Cycle is responsible for decoding the instruction and determining the type of operation to be performed.

3. Execute Cycle:
The Execute Cycle performs the actual operation specified by the instruction. This sub-cycle can involve multiple steps, depending on the complexity of the operation. For example, if the instruction is to add two numbers, the Execute Cycle will perform the necessary arithmetic operation to produce the sum.

4. Memory Cycle:
If the instruction involves accessing or modifying data in memory, the Memory Cycle is used to interact with the Memory Unit. This sub-cycle includes the address of the memory location to be accessed and the data to be read or written.

5. Write Back Cycle:
The final sub-cycle in the Control Unit is the Write Back Cycle, which updates the register or memory location with the result of the operation performed in the Execute Cycle.

In summary, the Control Unit uses a set of sub-cycles to execute instructions in a computer system. These sub-cycles include Fetch, Decode, Execute, Memory, and Write Back. Understanding these sub-cycles is essential for designing efficient computer systems and optimizing their performance.