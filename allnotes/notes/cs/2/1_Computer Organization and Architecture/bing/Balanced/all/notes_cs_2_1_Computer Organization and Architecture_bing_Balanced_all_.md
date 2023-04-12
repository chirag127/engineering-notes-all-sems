

## Unit 1 - Introduction

- In this unit, you will learn about the basic concepts and principles of artificial intelligence (AI).
- AI is the study of how to create machines and systems that can perform tasks that normally require human intelligence, such as reasoning, learning, perception, decision making, and natural language processing.
- AI can be divided into two main branches: symbolic AI and sub-symbolic AI.
  - Symbolic AI uses symbols and rules to represent and manipulate knowledge, such as logic, search, planning, and expert systems.
  - Sub-symbolic AI uses numerical and statistical methods to model and learn from data, such as neural networks, evolutionary algorithms, and reinforcement learning.
- AI can also be classified into different types based on the level of intelligence and the scope of the task:
  - Artificial narrow intelligence (ANI) or weak AI is the ability to perform a specific task or domain at or above human level, such as playing chess, recognizing faces, or translating languages.
  - Artificial general intelligence (AGI) or strong AI is the ability to perform any intellectual task that a human can do, such as understanding natural language, reasoning, and common sense.
  - Artificial superintelligence (ASI) is the ability to surpass human intelligence in all aspects, such as creativity, wisdom, and social skills.
- AI has many applications and benefits for various fields and domains, such as medicine, education, entertainment, business, and security.
- AI also poses many challenges and risks, such as ethical, social, legal, and technical issues, such as bias, privacy, accountability, and safety.



# Functional units of digital system and their interconnections

A digital system is a system that processes and stores data in binary form, using electronic devices such as transistors, logic gates, and memory cells. A digital system can perform various functions, such as arithmetic, logic, control, input, output, and communication. To perform these functions, a digital system consists of several functional units that are interconnected by buses. A bus is a set of wires or lines that carry data, address, or control signals between the functional units.

The main functional units of a digital system are:

- Input unit: This unit takes the input from the user or an external device and converts it into binary code that can be processed by the digital system. The input unit may include devices such as keyboards, mouse, scanners, microphones, cameras, etc. The input unit sends the binary data to the central processing unit (CPU) through the input bus.

- Central processing unit (CPU): This unit is the brain of the digital system, as it performs all the processing and control operations. The CPU consists of two subunits: the arithmetic and logic unit (ALU) and the control unit (CU). The ALU performs arithmetic and logic operations on the data, such as addition, subtraction, multiplication, division, comparison, etc. The CU controls the sequence and timing of the operations, and generates the control signals for the other functional units. The CPU also contains several registers, which are small memory units that store data temporarily. The CPU communicates with the other functional units through the data bus, the address bus, and the control bus.

- Memory unit: This unit stores the data and instructions that are needed by the CPU and the other functional units. The memory unit may include different types of memory devices, such as random access memory (RAM), read-only memory (ROM), cache memory, hard disk, etc. The memory unit receives and sends the data and the address from and to the CPU through the data bus and the address bus.

- Output unit: This unit converts the binary data from the CPU into a form that can be displayed or transmitted to the user or an external device. The output unit may include devices such as monitors, printers, speakers, modems, etc. The output unit receives the data from the CPU through the output bus.

The following diagram shows the functional units of a digital system and their interconnections:

Functional units of a digital system and their interconnections



# Buses

- A bus is a set of electrical wires that connects major components of a computer system, such as CPU, memory and I/O devices   .
- A bus can be used to transmit data, address and control signals among the components   .
- A bus can be classified into three functional groups: data bus, address bus and control bus   .
  - Data bus: used to carry data between CPU, memory and I/O devices. Bidirectional. The width of the data bus determines the amount of data that can be transferred at a time   .
  - Address bus: used to carry the address of the memory location or I/O device that the CPU wants to access. Unidirectional. The width of the address bus determines the maximum memory capacity of the system   .
  - Control bus: used to carry control signals that indicate the type and direction of the data transfer, such as read, write, interrupt, etc. Bidirectional. The number of control lines determines the variety of operations that can be performed by the system   .
- A bus can be designed in different ways, such as single bus, multiple bus, crossbar switch, etc., depending on the performance and cost requirements of the system  .
- A bus can have different speeds, measured in MHz or Mbps, depending on the frequency and throughput of the data transfer.



# Bus Architecture

- A bus is a set of electrical wires that connects major components of a computer system, such as CPU, memory and I/O devices.
- A bus can be classified into three functional groups: data lines, address lines and control lines  .
- Data lines are used to transfer data between components. The number of data lines determines the data transfer rate and the data size  .
- Address lines are used to specify the source or destination of data. The number of address lines determines the address space and the memory capacity  .
- Control lines are used to coordinate the operations of components. They carry signals such as read, write, enable, interrupt, etc  .
- A system bus is a bus that connects the CPU, memory and I/O devices to the motherboard. It can be further divided into internal bus and external bus.
- An internal bus, also known as memory bus or front-side bus, connects the CPU and memory to the motherboard. It operates at high speed and has a fixed data width.
- An external bus, also known as I/O bus or expansion bus, connects the I/O devices to the motherboard. It operates at lower speed and has a variable data width.
- A common bus system is a bus design that uses a single bus for data, address and control lines. It reduces the cost and complexity of the system, but also increases the bus contention and latency.
- A multiple bus system is a bus design that uses separate buses for data, address and control lines. It increases the performance and reliability of the system, but also increases the cost and complexity of the system.



# Types of Buses

A bus is a set of wires or lines that carry data, addresses, and control signals between different components of a computer system. Buses can be classified into different types based on their functions, locations, and architectures. Here are some of the common types of buses in computer architecture:

- **System bus**: This is the bus that connects the CPU to the main memory on the motherboard. The system bus is also called the front-side bus, memory bus, local bus, or host bus. The system bus consists of three sub-buses: address bus, data bus, and control bus.
  - **Address bus**: This is a unidirectional bus that carries the address of the memory location or the I/O device that the CPU wants to access. The width of the address bus determines the maximum amount of memory that the CPU can address. For example, a 32-bit address bus can address up to 2^32 bytes of memory, which is 4 GB.
  - **Data bus**: This is a bidirectional bus that transfers the data between the CPU and the memory or the I/O devices. The width of the data bus determines the amount of data that can be transferred in one cycle. For example, a 16-bit data bus can transfer 16 bits or 2 bytes of data at a time.
  - **Control bus**: This is a bidirectional bus that carries the control signals that synchronize the operations of the CPU, memory, and I/O devices. The control signals include read, write, interrupt, reset, clock, and others.

- **Expansion bus**: This is the bus that connects the expansion cards or peripheral devices to the system bus. The expansion bus is also called the I/O bus, peripheral bus, or external bus. The expansion bus allows the system to be customized and upgraded with different devices, such as graphics cards, sound cards, network cards, and others. There are different standards and protocols for the expansion bus, such as ISA, EISA, MCA, VESA, PCI, PCI Express, and others. The expansion bus typically has a lower speed and bandwidth than the system bus.

- **Internal bus**: This is the bus that connects the internal components of the CPU, such as the arithmetic logic unit (ALU), the registers, the cache, and the instruction decoder. The internal bus is also called the local bus, processor bus, or CPU bus. The internal bus operates at the same speed as the CPU and has a high bandwidth. The internal bus is usually not visible to the external system and is specific to the CPU architecture.



# Bus Arbitration

- Bus arbitration is the process by which the current bus master accesses and then leaves the control of the bus and passes it to another bus requesting processor unit    .
- A bus master is a controller that can access the bus for a given instance.
- Bus arbitration is necessary to avoid conflicts and ensure proper communication among the devices connected to the bus.
- There are two types of bus arbitration: centralized arbitration and distributed arbitration.

## Centralized Arbitration

- In centralized arbitration, there is a single bus arbiter that decides which device gets the bus access.
- The bus arbiter can be a part of the processor, the memory controller, or a separate chip.
- The devices send their bus requests to the bus arbiter, which grants the bus access to one of them based on some priority scheme.
- The advantages of centralized arbitration are simplicity and efficiency.
- The disadvantages of centralized arbitration are single point of failure, bottleneck, and scalability issues.

## Distributed Arbitration

- In distributed arbitration, there is no central bus arbiter, and the devices communicate with each other to decide which device gets the bus access.
- The devices use a common bus line or a set of bus lines to send and receive signals indicating their bus requests and grants.
- The devices follow some protocol or algorithm to resolve conflicts and determine the bus access order.
- The advantages of distributed arbitration are fault tolerance, parallelism, and scalability.
- The disadvantages of distributed arbitration are complexity and overhead.



# Register for the notes of the Unit 1 - Introduction in the subject of Computer Organization and Architecture

- To register for the notes of the Unit 1 - Introduction in the subject of Computer Organization and Architecture, you need to follow these steps:
  - Visit the official website of the course provider and log in with your credentials.
  - Navigate to the course page of Computer Organization and Architecture and click on the Unit 1 - Introduction link.
  - You will see a button that says "Register for notes" or something similar. Click on it and confirm your registration.
  - You will receive an email with a link to access the notes of the Unit 1 - Introduction. You can also find the notes on the course page under the "Resources" section.
  - The notes of the Unit 1 - Introduction will cover the following topics:
    - The basic concepts and terminology of computer organization and architecture.
    - The historical evolution and trends of computer systems and their components.
    - The performance metrics and evaluation methods of computer systems.
    - The instruction set architecture and its design principles and trade-offs.
    - The basic components and organization of a computer system, such as the processor, memory, input/output, and bus.
    - The overview of the main topics and concepts that will be covered in the subsequent units of the course.
- You can use the notes of the Unit 1 - Introduction as a reference and a supplement to the lectures and the textbook. You can also test your understanding and knowledge by answering the questions and exercises at the end of each topic.
- If you have any questions or doubts about the notes of the Unit 1 - Introduction, you can contact the instructor or the teaching assistants of the course through the online forum or the email. They will be happy to assist you and clarify your queries.



# Bus

- A bus is a set of wires or lines that carry data, address, and control signals between different components of a computer system.
- A bus can be classified into three types: data bus, address bus, and control bus.
- Data bus: It carries data between the processor, memory, and input/output devices. It is bidirectional, meaning that data can flow in both directions. The width of the data bus determines the amount of data that can be transferred at a time. For example, a 32-bit data bus can transfer 32 bits or 4 bytes of data at a time.
- Address bus: It carries the address of the memory location or input/output device that the processor wants to access. It is unidirectional, meaning that data can only flow from the processor to the memory or input/output devices. The width of the address bus determines the maximum amount of memory or input/output devices that can be addressed by the processor. For example, a 16-bit address bus can address up to 2^16 or 65,536 memory locations or input/output devices.
- Control bus: It carries control signals that synchronize the operations of the processor, memory, and input/output devices. It can be bidirectional or unidirectional, depending on the design of the computer system. Control signals include read, write, enable, reset, interrupt, etc.



# Memory Transfer

- Memory transfer is the process of moving data from one location to another in a computer system.
- Memory transfer can be performed by different components, such as the CPU, the memory controller, the input/output devices, or the direct memory access (DMA) controller.
- Memory transfer can be classified into two types: synchronous and asynchronous.
  - Synchronous memory transfer means that the data transfer is synchronized with a clock signal, and the sender and the receiver agree on the timing and the speed of the transfer.
  - Asynchronous memory transfer means that the data transfer is not synchronized with a clock signal, and the sender and the receiver use handshaking signals to coordinate the transfer.
- Memory transfer can also be classified into two modes: block transfer and stream transfer.
  - Block transfer means that the data is transferred in fixed-size units, called blocks or words, and each block is transferred as a whole.
  - Stream transfer means that the data is transferred in variable-size units, called bytes or bits, and each byte or bit is transferred individually.
- Memory transfer can involve different types of memory, such as primary memory, secondary memory, cache memory, or register memory.
  - Primary memory, also known as main memory or RAM, is the memory that the CPU can access directly and quickly. It is usually volatile, meaning that it loses its data when the power is off.
  - Secondary memory, also known as auxiliary memory or disk memory, is the memory that the CPU cannot access directly and has to use input/output devices to transfer data to and from it. It is usually non-volatile, meaning that it retains its data when the power is off.
  - Cache memory, also known as buffer memory, is a small and fast memory that is used to store frequently accessed data from the primary memory or the secondary memory. It is usually volatile and has a lower capacity than the primary memory or the secondary memory.
  - Register memory, also known as CPU registers, is the smallest and fastest memory that is used to store temporary data or instructions for the CPU. It is usually volatile and has a very limited capacity.



# Processor Organization

- Processor organization is the study of how the components of a processor are designed and interconnected to perform various tasks.
- Processor organization is a part of computer organization and architecture, which deals with the structure and behavior of a computer system as seen by the programmer or user.
- Processor organization affects the performance, cost, and complexity of a computer system.

## Components of a Processor

- A processor, also known as a central processing unit (CPU), is the main component of a computer system that executes instructions and performs calculations.
- A processor consists of the following components:

  - Arithmetic and Logic Unit (ALU): The ALU performs arithmetic and logical operations on data, such as addition, subtraction, multiplication, division, and comparison.
  - Control Unit (CU): The CU controls the operation of the processor by fetching, decoding, and executing instructions, and by generating control signals for other components.
  - Registers: Registers are small, fast memory units that store data and instructions temporarily. Registers can be classified into general-purpose registers, which can be used for any data or address, and special-purpose registers, which have specific functions, such as program counter, instruction register, status register, etc.
  - Buses: Buses are sets of wires that transfer data, addresses, and control signals between the processor and other components, such as memory and input/output devices.

## Processor Design

- Processor design is the process of choosing and implementing the components and interconnections of a processor to achieve a desired functionality and performance.
- Processor design involves the following aspects:

  - Instruction Set Design: The instruction set is the set of instructions that a processor can execute. The instruction set defines the format, operands, and operation of each instruction. The instruction set affects the complexity, performance, and compatibility of a processor.
  - Basic Processor Implementation Techniques: The basic processor implementation techniques are the methods of designing the datapath and the control unit of a processor. The datapath is the part of the processor that performs data operations, such as ALU and registers. The control unit is the part of the processor that controls the datapath and the buses. The basic processor implementation techniques include hardwired control, microprogrammed control, single-cycle, multi-cycle, and pipelined execution.
  - Performance Measurement: Performance measurement is the evaluation of the speed and efficiency of a processor. Performance measurement involves the use of metrics, such as clock rate, instruction count, CPI (cycles per instruction), MIPS (million instructions per second), and execution time. Performance measurement also involves the use of benchmarks, which are standard programs or tasks that are used to compare the performance of different processors or systems.
  - Caches and Virtual Memory: Caches and virtual memory are techniques that improve the performance of a processor by reducing the access time to memory. Caches are small, fast memory units that store frequently used data or instructions. Virtual memory is a technique that allows a processor to access a larger memory space than the physical memory by using disk space as an extension of memory.
  - Pipelined Processor Design: Pipelined processor design is a technique that improves the performance of a processor by dividing the execution of an instruction into several stages and executing multiple instructions in parallel. Pipelined processor design involves the use of registers, called pipeline registers, to store the intermediate results of each stage. Pipelined processor design also involves the handling of hazards, which are situations that prevent the correct execution of instructions in a pipeline, such as data dependencies, control dependencies, and resource conflicts.
  - Design Trade-offs among Cost, Performance, and Complexity: Design trade-offs are the choices and compromises that a processor designer has to make among different factors, such as cost, performance, and complexity. Cost is the amount of money or resources required to design, manufacture, and operate a processor. Performance is the speed and efficiency of a processor. Complexity is the difficulty and effort required to design, implement, and verify a processor. Design trade-offs involve the use of techniques, such as parallelism, pipelining, superscalar, VLIW, RISC, CISC, etc., to achieve a balance among cost, performance, and complexity.



# General Registers Organization

- General registers organization is a type of CPU organization that uses multiple general-purpose registers for storing and manipulating data, instead of a single accumulator register.
- General-purpose registers are registers that can be used for various purposes, such as holding operands, addresses, intermediate results, flags, or control information.
- General registers organization can have two or three address fields in the instruction format, depending on the number of operands required for an operation.
- General registers organization can be further classified into two types: register-memory reference architecture and register-register reference architecture.

## Register-memory reference architecture

- In this architecture, the CPU has a small number of registers, usually one or two.
- The source operands can be either in a register or in memory, but the destination operand must be in a register.
- The advantage of this architecture is that it reduces the instruction length and the number of memory accesses.
- The disadvantage of this architecture is that it increases the register contention and the number of register transfers.

## Register-register reference architecture

- In this architecture, the CPU has a large number of registers, usually 16 or more.
- The source and destination operands must be in registers, and memory operands are accessed only by load and store instructions.
- The advantage of this architecture is that it increases the speed of execution and reduces the memory traffic.
- The disadvantage of this architecture is that it increases the instruction length and the complexity of register allocation.

: https://www.geeksforgeeks.org/introduction-of-general-register-based-cpu-organization/
: https://www.ques10.com/p/18407/describe-the-register-organization-within-the-cp-1/



# Stack Organization

- Stack is a storage structure that stores information in such a way that the last item stored is the first item retrieved.
- It is based on the principle of LIFO (Last-in-first-out).
- The stack in digital computers is a group of memory locations with a register that holds the address of top of element.
- The register that holds the top of stack address is called the stack pointer (SP).
- The stack pointer is incremented or decremented as data is pushed or popped from the stack.
- The stack can be used for various purposes, such as:
  - Storing return addresses of subroutines.
  - Passing parameters to subroutines.
  - Saving and restoring the state of the CPU.
  - Evaluating arithmetic and logical expressions.
  - Implementing recursion.
- The computers that use stack-based CPU organization are based on a data structure called a stack machine.
- A stack machine is a computer that uses a stack to hold operands and results of arithmetic and logical operations.
- A stack machine has no general-purpose registers, only a stack pointer.
- The stack acts as a source and destination, push and pop instructions are used to access instructions and data from the stack.
- There is no need to pass the source and destination address because the default address is top of the stack.
- In a stack machine, there is no need to pass explicit addresses in the instruction.
- The advantages of stack organization are:
  - Simplicity of instruction format and decoding.
  - Reduced memory access and bandwidth requirements.
  - Ease of implementation of subroutines and recursion.
- The disadvantages of stack organization are:
  - Limited parallelism and pipelining.
  - Dependence on the stack pointer.
  - Increased number of instructions.



# Addressing Modes

- Addressing modes are the different ways of specifying the location of an operand in an instruction .
- Operand is the data on which the operation specified by the instruction is performed.
- The choice of addressing mode affects the instruction format, the instruction size, the instruction execution time, and the memory access time.
- Different types of addressing modes are:

  - **Implied / Implicit Addressing Mode**: In this mode, the operand is specified in the instruction itself or implied by the instruction . For example, `CLC` (clear carry flag) instruction does not need any operand, as the operand is the carry flag itself.
  - **Immediate Addressing Mode**: In this mode, the operand is a constant value that is directly given in the instruction . For example, `MOV AX, 10` instruction moves the value 10 to the AX register.
  - **Direct Addressing Mode**: In this mode, the operand is the effective address (EA) of the memory location where the data is stored . The EA is given as a part of the instruction. For example, `MOV AX, [1000]` instruction moves the data stored at memory location 1000 to the AX register.
  - **Register Addressing Mode**: In this mode, the operand is a register that holds the data . The register name is given as a part of the instruction. For example, `MOV AX, BX` instruction moves the data stored in the BX register to the AX register.
  - **Register Indirect Addressing Mode**: In this mode, the operand is the EA of the memory location where the data is stored . The EA is stored in a register, whose name is given as a part of the instruction. For example, `MOV AX, [BX]` instruction moves the data stored at the memory location pointed by the BX register to the AX register.
  - **Indexed Addressing Mode**: In this mode, the operand is the EA of the memory location where the data is stored . The EA is calculated by adding a constant value (called displacement or offset) to the content of an index register, whose name is given as a part of the instruction. For example, `MOV AX, [1000 + SI]` instruction moves the data stored at the memory location obtained by adding 1000 to the content of the SI register to the AX register.
  - **Base Register Addressing Mode**: In this mode, the operand is the EA of the memory location where the data is stored . The EA is calculated by adding a constant value (called displacement or offset) to the content of a base register, whose name is given as a part of the instruction. For example, `MOV AX, [1000 + BP]` instruction moves the data stored at the memory location obtained by adding 1000 to the content of the BP register to the AX register.
  - **Relative Addressing Mode**: In this mode, the operand is the EA of the memory location where the next instruction is stored . The EA is calculated by adding a constant value (called displacement or offset) to the content of the program counter (PC) register, which holds the address of the current instruction. This mode is used for branching instructions. For example, `JMP 100` instruction jumps to the instruction located at 100 bytes ahead of the current instruction.
  - **Stack Addressing Mode**: In this mode, the operand is the top of the stack . The stack is a special memory area that follows the last-in first-out (LIFO) principle. The stack pointer (SP) register holds the address of the top of the stack. This mode is used for pushing and popping data to and from the stack. For example, `PUSH AX` instruction pushes the data stored in the AX register to the top of the stack.



## Unit 2 - Arithmetic and logic unit

- An arithmetic and logic unit (ALU) is a digital circuit that performs arithmetic and logical operations on binary numbers.
- The ALU is one of the core components of the central processing unit (CPU) of a computer system.
- The ALU can perform basic operations such as addition, subtraction, multiplication, division, and bitwise operations such as AND, OR, XOR, and NOT.
- The ALU can also perform more complex operations such as shifting, rotating, comparing, and counting.
- The ALU receives two input operands (A and B) and a set of control signals from the control unit (CU) of the CPU.
- The control signals determine which operation the ALU will perform on the input operands and how the output will be stored or transferred.
- The ALU produces an output result (R) and a set of status flags (such as zero, carry, overflow, and sign) that indicate the outcome of the operation.
- The ALU can be designed using combinational logic circuits (such as multiplexers, adders, and comparators) or sequential logic circuits (such as registers, counters, and shifters).
- The ALU can be implemented using various technologies such as transistors, integrated circuits, or microprocessors.
- The ALU can be optimized for speed, power, size, or functionality depending on the requirements of the computer system.



# Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware.
- Propagation delay is the time taken for the carry to propagate from one stage to the next in a ripple carry adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- A look ahead carry adder uses the concepts of carry generate and carry propagate to compute the carry out of a block.
- Carry generate (Cg) occurs when an output carry is generated internally by the full adder, regardless of the carry in. Cg = A.B
- Carry propagate (Cp) occurs when an output carry is equal to the carry in, meaning that the full adder propagates the carry to the next stage. Cp = A ⊕ B
- The carry out of a block can be expressed as a function of Cg, Cp and the carry in (Cin) of the block. Cout = Cg + Cp.Cin
- The carry out of a block can be computed in parallel with the sum outputs of the block, thus reducing the delay.
- A look ahead carry adder can be implemented using a 4-bit carry look ahead adder (CLA) module, which has four inputs (A0, A1, A2, A3), four outputs (S0, S1, S2, S3), a carry in (Cin) and a carry out (Cout).
- A 4-bit CLA module consists of four full adders, a carry look ahead generator (CLG) and a carry look ahead propagator (CLP).
- The CLG computes the Cg and Cp signals for each bit of the block.
- The CLP computes the Cout signal using the Cg and Cp signals and the Cin signal.
- The sum outputs are computed by the full adders using the A, B and Cp signals.
- A 4-bit CLA module can be extended to a 16-bit CLA adder by using four 4-bit CLA modules and a 4-bit CLA module as a carry look ahead unit (CLU).
- The CLU computes the carry out signals for each 4-bit block using the Cg and Cp signals of the blocks and the Cin signal of the adder.
- The carry out signals of the CLU are connected to the carry in signals of the corresponding 4-bit blocks.
- The sum outputs of the 16-bit CLA adder are the sum outputs of the four 4-bit blocks.
- A 16-bit CLA adder can be further extended to a 64-bit CLA adder by using four 16-bit CLA adders and a 4-bit CLA module as a CLU.



# Multiplication

- Multiplication is an arithmetic operation that computes the product of two numbers.
- Multiplication can be performed by repeated addition, but this is inefficient for large numbers.
- Multiplication can also be performed by using a binary multiplier, which is a combinational circuit that takes two binary numbers as inputs and produces their product as output.
- A binary multiplier can be implemented by using a series of half-adders and full-adders, which are basic logic gates that can perform binary addition.
- A binary multiplier can be classified into two types: serial multiplier and parallel multiplier.
- A serial multiplier performs multiplication by shifting and adding one bit at a time, starting from the least significant bit (LSB) of the multiplier and the multiplicand.
- A parallel multiplier performs multiplication by generating partial products for each bit of the multiplier and the multiplicand, and then adding them together in parallel.
- A parallel multiplier is faster than a serial multiplier, but requires more hardware resources and complexity.
- A parallel multiplier can be further optimized by using various techniques, such as Booth's algorithm, Wallace tree, Dadda multiplier, etc.



# Signed operand multiplication

- Signed operand multiplication is the process of multiplying two binary numbers that have a sign bit, usually in two's complement representation.
- The sign bit is the most significant bit of the number, and it indicates whether the number is positive (0) or negative (1).
- There are different algorithms for performing signed operand multiplication, such as the paper-and-pencil method, the Booth's algorithm, and the modified Booth's algorithm.
- The paper-and-pencil method is similar to the decimal multiplication, but it uses binary arithmetic and shifting operations. It consists of the following steps:
  - Convert the multiplier and the multiplicand to positive numbers and remember their original signs.
  - Align the multiplier and the multiplicand according to their least significant bits.
  - For each bit of the multiplier, starting from the least significant bit, perform the following:
    - If the bit is 1, add the multiplicand to the partial product and write the result below the previous partial product.
    - If the bit is 0, write the previous partial product without any change.
    - Shift the partial product and the multiplier one bit to the right, discarding the rightmost bit of the partial product and inserting a 0 at the leftmost bit of the multiplier.
  - Repeat the above steps until the multiplier becomes 0.
  - The final partial product is the result of the multiplication. If the signs of the multiplier and the multiplicand were different, complement the result to get the negative value.
- The Booth's algorithm is a more efficient algorithm that reduces the number of additions by encoding the multiplier bits in pairs. It consists of the following steps:
  - Initialize a register A to 0, a register Q to the multiplier, and a register Qn+1 to 0. Also, initialize a counter to the number of bits in the multiplier.
  - For each iteration, perform the following:
    - Examine the pair of bits Q0 and Qn+1, and perform the following actions based on their values:
      - If Q0Qn+1 = 00 or 11, do nothing.
      - If Q0Qn+1 = 01, subtract the multiplicand from A and write the result in A.
      - If Q0Qn+1 = 10, add the multiplicand to A and write the result in A.
    - Shift the registers A, Q, and Qn+1 one bit to the right, preserving the sign bit of A. This is an arithmetic shift right operation.
    - Decrement the counter by 1.
  - Repeat the above steps until the counter becomes 0.
  - The final value of AQ is the result of the multiplication.
- The modified Booth's algorithm is a further improvement that encodes the multiplier bits in groups of three, reducing the number of additions by half. It consists of the following steps:
  - Initialize a register A to 0, a register Q to the multiplier, and a register Qn+1 to 0. Also, initialize a counter to half the number of bits in the multiplier.
  - For each iteration, perform the following:
    - Examine the group of bits Q1Q0Qn+1, and perform the following actions based on their values:
      - If Q1Q0Qn+1 = 000 or 111, do nothing.
      - If Q1Q0Qn+1 = 001, add 2 times the multiplicand to A and write the result in A.
      - If Q1Q0Qn+1 = 010 or 110, add the multiplicand to A and write the result in A.
      - If Q1Q0Qn+1 = 011, subtract the multiplicand from A and write the result in A.
      - If Q1Q0Qn+1 = 100 or 101, subtract 2 times the multiplicand from A and write the result in A.
    - Shift the registers A, Q, and Qn+1 two bits to the right, preserving the sign bit of A. This is an arithmetic shift right operation.
    - Decrement the counter by 1.
  - Repeat the above steps until the counter becomes 0.
  - The final value of AQ is the result of the multiplication.



# Booth's Algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in two's complement notation. It was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in London.

The main features of Booth's algorithm are:

- It examines adjacent pairs of bits of the multiplier and performs different operations based on the bit pair.
- It reduces the number of additions and subtractions required for multiplication, compared to the conventional method of shifting and adding.
- It can handle both positive and negative operands, as well as overflow and underflow conditions.

The steps of Booth's algorithm are:

1. Initialize the accumulator (A) and the quotient (Q) registers to zero. The A register has the same number of bits as the multiplicand (M), and the Q register has the same number of bits as the multiplier (Y). Also, initialize a single-bit register (Q-1) to zero. This register holds the previous bit of the multiplier.
2. Perform a right arithmetic shift on the combined register AQ and Q-1. This means that the sign bit of A is copied to the leftmost bit of Q, and the rightmost bit of Q is copied to Q-1. The rightmost bit of A is discarded.
3. Examine the two rightmost bits of AQ and Q-1. Depending on the bit pair, perform one of the following operations:
    - If the bit pair is 00 or 11, do nothing.
    - If the bit pair is 01, add the multiplicand M to the accumulator A and store the result in A.
    - If the bit pair is 10, subtract the multiplicand M from the accumulator A and store the result in A.
4. Repeat steps 2 and 3 for n times, where n is the number of bits in the multiplier Y.
5. The final product is obtained by concatenating the accumulator A and the quotient Q. If the product is negative, it is in two's complement form.

The following example illustrates the Booth's algorithm for multiplying 3 and -4 in binary:

| Step | A  | Q  | Q-1 | Operation |
| ---- | -- | -- | --- | --------- |
| 0    | 0  | 0011 | 0   | Initial values |
| 1    | 0  | 0001 | 1   | Right shift |
| 2    | 1100 | 0001 | 1   | A = A - M |
| 3    | 1110 | 0000 | 1   | Right shift |
| 4    | 1110 | 0000 | 1   | Do nothing |
| 5    | 1111 | 0000 | 0   | Right shift |
| 6    | 0011 | 1000 | 0   | A = A + M |
| 7    | 0001 | 1100 | 0   | Right shift |
| 8    | 0001 | 1100 | 0   | Do nothing |
| 9    | 0000 | 1110 | 0   | Right shift |
| 10   | 0000 | 1110 | 0   | Do nothing |
| 11   | 0000 | 0111 | 0   | Right shift |
| 12   | 0000 | 0111 | 0   | Do nothing |

The final product is 000001110000, which is -12 in decimal. This is the correct answer, since 3 x -4 = -12.



# Array Multiplier

- An array multiplier is a digital combinational circuit used for multiplying two binary numbers by employing an array of full adders and half adders .
- The array multiplier is based on the add-shift algorithm, which generates the partial products by using an array of AND gates and then adds them by using an array of adders.
- The main advantage of the array multiplier is its simple and regular design, which makes it easy to implement and scale .
- The main disadvantage of the array multiplier is its high delay and high power consumption, which limits its performance and efficiency .
- The delay of the array multiplier is proportional to the number of bits in the operands, and the power consumption is proportional to the number of gates in the circuit .
- The array multiplier can be improved by using different techniques, such as using radix-4 partial-product generation, using carry-save adders, using Wallace trees, or using field-programmable gate arrays (FPGAs).
- The array multiplier is widely used for applications that require high throughput and accuracy, such as digital signal processing, image processing, cryptography, and machine learning.



# Division and logic operations for the notes of the Unit 2 - Arithmetic and logic unit in the subject of Computer Organization and Architecture

- Division is the process of finding the quotient and the remainder of two numbers.
- Division can be performed by repeated subtraction, shift and subtract, or restoring and non-restoring methods.
- Logic operations are the basic operations that manipulate binary data, such as AND, OR, NOT, XOR, etc.
- Logic operations can be used to implement Boolean functions, which are the expressions of truth values based on logical variables and operators.
- Logic operations can also be used to perform bitwise operations, which are the operations that manipulate individual bits of a binary number, such as shifting, rotating, masking, etc.
- Logic operations can be implemented by using logic gates, which are the electronic circuits that perform the basic logic functions.
- Logic gates can be combined to form more complex circuits, such as adders, multiplexers, decoders, etc.



# Floating point arithmetic operation

- A floating point (FP) number is a kind of fraction where the radix point is allowed to move.
- A floating point number consists of three parts: a sign bit, a significand, and an exponent.
- The sign bit indicates whether the number is positive or negative.
- The significand is the fractional part of the number, normalized to have a leading 1 in binary representation.
- The exponent is the power of two by which the significand is multiplied.
- The IEEE 754 standard defines a binary floating point format, with different sizes and precisions for single-precision (32-bit) and double-precision (64-bit) numbers.
- Floating point arithmetic operations include addition, subtraction, multiplication, and division.
- Floating point arithmetic operations are done with algorithms similar to those used on sign magnitude integers, but with some additional steps to handle the exponents and normalize the results .
- Floating point arithmetic operations are subject to rounding errors, overflow, and underflow, which can affect the accuracy and reliability of the computations.



# Arithmetic and Logic Unit Design

- An arithmetic and logic unit (ALU) is a component of a central processing unit (CPU) that performs arithmetic and logic operations on the operands in computer instruction words.
- An ALU can perform three kinds of operations: arithmetic operations, such as addition, subtraction, multiplication and division; logical operations, such as AND, OR, NOT, XOR and NAND; and data movement operations, such as load and store.
- An ALU can be divided into two subunits: an arithmetic unit (AU) and a logic unit (LU). The AU performs arithmetic operations, while the LU performs logical operations.
- An ALU can be designed using various logic gates, such as AND, OR, NOT, XOR and NAND. The logic gates can be combined to form more complex circuits, such as adders, subtracters, multipliers, dividers, shifters and comparators.
- An ALU can also be designed using reversible logic, which is a logic that preserves the information and does not produce any garbage outputs or consume any power. Reversible logic can be implemented using quantum-dot cellular automata (QCA), which are nanoscale devices that use the quantum mechanical behavior of electrons to perform logic operations.
- An ALU can be evaluated based on various parameters, such as quantum cost, garbage outputs, constant inputs, area, number of cells and simulation time. These parameters can be used to measure the performance, efficiency and complexity of the ALU design.



# IEEE Standard for Floating Point Numbers

- Floating point numbers are a way to represent real numbers in hardware, using a fixed number of bits.
- IEEE 754 is the most widely used standard for floating point arithmetic, which specifies the formats, methods, and exception handling for binary and decimal floating point numbers  .
- IEEE 754 defines two precisions for binary floating point numbers: single precision and double precision.
  - Single precision numbers have 32 bits: 1 for the sign, 8 for the exponent, and 23 for the significand.
  - Double precision numbers have 64 bits: 1 for the sign, 11 for the exponent, and 52 for the significand.
- IEEE 754 also defines two precisions for decimal floating point numbers: decimal32 and decimal64.
  - Decimal32 numbers have 32 bits: 1 for the sign, 6 for the exponent, and 25 for the significand.
  - Decimal64 numbers have 64 bits: 1 for the sign, 8 for the exponent, and 55 for the significand.
- IEEE 754 uses a biased representation for the exponent, which means that a fixed value is added to the actual exponent to get a positive value.
  - For single precision, the bias is 127, so the exponent range is -126 to 127.
  - For double precision, the bias is 1023, so the exponent range is -1022 to 1023.
  - For decimal32, the bias is 101, so the exponent range is -95 to 96.
  - For decimal64, the bias is 398, so the exponent range is -383 to 384.
- IEEE 754 uses a normalized representation for the significand, which means that the most significant bit is always 1 and is not stored.
  - For single precision, the significand has 24 bits, but only 23 are stored.
  - For double precision, the significand has 53 bits, but only 52 are stored.
  - For decimal32, the significand has 26 bits, but only 25 are stored.
  - For decimal64, the significand has 56 bits, but only 55 are stored.
- IEEE 754 defines some special values for floating point numbers, such as zero, infinity, NaN (not a number), and subnormal numbers .
  - Zero is represented by setting all the bits to zero.
  - Infinity is represented by setting the exponent bits to all ones and the significand bits to all zeros.
  - NaN is represented by setting the exponent bits to all ones and the significand bits to any non-zero value.
  - Subnormal numbers are represented by setting the exponent bits to all zeros and the significand bits to any non-zero value.
- IEEE 754 defines four rounding modes for floating point arithmetic: round to nearest, round to zero, round to positive infinity, and round to negative infinity.
  - Round to nearest is the default mode, which rounds the result to the nearest representable value, and breaks ties by rounding to the even value.
  - Round to zero is the mode that rounds the result toward zero, which means truncating the fractional part.
  - Round to positive infinity is the mode that rounds the result toward positive infinity, which means rounding up.
  - Round to negative infinity is the mode that rounds the result toward negative infinity, which means rounding down.
- IEEE 754 defines five exception conditions for floating point arithmetic: invalid operation, division by zero, overflow, underflow, and inexact.
  - Invalid operation is the condition that occurs when the result is undefined, such as NaN, or when an invalid operation is performed, such as adding infinity to negative infinity.
  - Division by zero is the condition that occurs when a finite non-zero number is divided by zero, which results in either positive or negative infinity.
  - Overflow is the condition that occurs when the result is too large to be represented by the format, which results in either positive or negative infinity.
  - Underflow is the



## Unit 3 - Control Unit

- The control unit (CU) is a component of the central processing unit (CPU) that directs the operation of the processor.
- The control unit generates control signals that instruct the arithmetic logic unit (ALU), the memory, and the input/output devices on how to respond to the instructions fetched from the memory.
- The control unit can be classified into two types: hardwired control unit and microprogrammed control unit.
- A hardwired control unit is a circuit that implements a fixed set of control signals based on the current instruction and the state of the processor. A hardwired control unit is fast, but inflexible and difficult to modify.
- A microprogrammed control unit is a circuit that executes a small program stored in a control memory, called a microprogram. A microprogram consists of a sequence of microinstructions, each of which generates a set of control signals for one or more micro-operations. A microprogrammed control unit is flexible, easy to modify, and can implement complex instructions, but slower than a hardwired control unit.
- The control unit can also be classified into two modes: single-cycle mode and multi-cycle mode.
- In single-cycle mode, the control unit executes one instruction in one clock cycle. This means that all the instruction phases (fetch, decode, execute, memory access, and write back) are performed in one cycle. This mode is simple, but inefficient, as different instructions may require different amounts of time to complete.
- In multi-cycle mode, the control unit executes one instruction in multiple clock cycles. This means that each instruction phase is performed in a separate cycle, and the control unit can vary the number of cycles depending on the instruction type. This mode is more efficient, but complex, as the control unit needs to keep track of the current instruction phase and the next instruction phase.



# Instruction types for the notes of the Unit 3 - Control Unit in the subject of Computer Organization and Architecture

- An instruction is a binary code that specifies an operation to be performed by the processor and the operands to be used in the operation.
- Instructions can be classified into different types based on the number and type of operands, the complexity of the operation, and the control flow of the program.
- Some common instruction types are:

  - **Register instructions**: These instructions use only registers as operands. They are fast and simple to execute, but they have limited address space and require more bits to encode the register numbers. For example, `ADD R1, R2, R3` adds the contents of registers R2 and R3 and stores the result in register R1.
  - **Immediate instructions**: These instructions use a constant value as one of the operands. They are useful for initializing registers, performing arithmetic operations with small constants, and loading addresses. For example, `ADDI R1, R2, 5` adds the constant 5 to the contents of register R2 and stores the result in register R1.
  - **Memory instructions**: These instructions use memory locations as operands. They are necessary for accessing data that cannot fit in registers, such as arrays, strings, and structures. They are slower than register instructions, as they require memory access cycles. For example, `LW R1, 100(R2)` loads the word from the memory address obtained by adding 100 to the contents of register R2 and stores it in register R1.
  - **Branch instructions**: These instructions alter the control flow of the program based on a condition. They are essential for implementing loops, conditional statements, and function calls. They usually compare the contents of two registers or a register and a constant, and then jump to a specified address if the condition is true. For example, `BEQ R1, R2, L1` compares the contents of registers R1 and R2, and jumps to the label L1 if they are equal.
  - **Jump instructions**: These instructions unconditionally alter the control flow of the program by jumping to a specified address. They are used for implementing function calls and returns, and for transferring control to different parts of the program. For example, `J L2` jumps to the label L2.
  - **Complex instructions**: These instructions perform complex operations that may require multiple simple instructions. They are designed to improve the performance and functionality of the processor, but they may also increase the complexity and cost of the hardware. For example, `MUL R1, R2, R3` multiplies the contents of registers R2 and R3 and stores the result in register R1.



# Unit 3 - Control Unit

The control unit is the component of the computer that directs the operation of the processor, memory, and input/output devices. It generates the control signals that determine the sequence of instructions executed by the processor and the flow of data among the components.

The control unit can be designed using two different approaches: hardwired control and microprogrammed control.

## Hardwired Control

- Hardwired control is a method of implementing the control unit using combinational logic circuits.
- The control signals are generated by decoding the instruction opcode and the current state of the processor.
- The logic circuits are designed using Boolean algebra, Karnaugh maps, or other techniques.
- Hardwired control is fast, but inflexible and complex to design and modify.

## Microprogrammed Control

- Microprogrammed control is a method of implementing the control unit using a special memory called the control store.
- The control signals are generated by executing a sequence of microinstructions stored in the control store.
- Each microinstruction specifies the control signals for one or more micro-operations, such as fetching, decoding, or executing an instruction.
- The microinstructions are executed by a microprogram sequencer, which determines the next microinstruction to be executed based on the instruction opcode, the processor state, and the microinstruction fields.
- Microprogrammed control is flexible, but slower and less efficient than hardwired control.



# Instruction Cycles

- Instruction cycles are the basic operations of the CPU that consist of three steps: fetch, decode, and execute  .
- Fetch: The CPU retrieves the instruction from the memory unit and stores it in the instruction register . The program counter is incremented to point to the next instruction .
- Decode: The CPU analyzes the instruction and determines what actions are required . The instruction may specify the operands (data) and the operation (function) to be performed on them .
- Execute: The CPU performs the operation on the operands, which may involve transferring data between registers, memory, and input/output devices, or performing arithmetic or logical operations . The result may be stored in a register or memory location .
- The instruction cycle is repeated until the program is completed or an interrupt occurs . An interrupt is a signal that causes the CPU to stop the current instruction cycle and switch to another task .
- The instruction cycle may vary depending on the type and complexity of the instruction, the CPU architecture, and the presence of pipelining or parallelism  . Pipelining is a technique that allows the CPU to fetch the next instruction while executing the current one, thus increasing the speed and efficiency of the CPU  . Parallelism is a technique that allows the CPU to execute multiple instructions simultaneously, thus increasing the throughput and performance of the CPU  .



# Sub Cycles for the Notes of the Unit 3 - Control Unit in the Subject of Computer Organization and Architecture

- The control unit is the part of the processor that coordinates the sequence of data movements into, out of, and between the processor's many sub-units.
- The control unit also interprets the instructions fetched from the memory and generates the appropriate control signals to execute them.
- The execution of an instruction involves the execution of a sequence of substeps, generally called cycles.
- For example, an instruction may consist of fetch, indirect, execute, and interrupt cycles.
- Each cycle is in turn made up of a sequence of more fundamental operations, called micro-operations.
- A micro-operation is a basic operation performed on data stored in one or more registers, or on data transferred between a register and an external bus.
- A micro-operation generally involves a transfer between registers, a transfer between a register and an external bus, or a simple ALU operation.
- The control unit generates the control signals that cause each micro-operation to be executed.
- The control signals also cause the opening and closing of logic gates, resulting in the transfer of data to and from registers and the operation of the ALU.
- One technique for implementing a control unit is referred to as hardwired, which means that the control signals are generated by using combinational logic circuits.
- Another technique is to use a microprogrammed control unit, which means that the control signals are stored in a special memory called the control memory.
- The control memory contains a sequence of microinstructions, each of which specifies one or more micro-operations to be performed in a single cycle.
- The control unit fetches and executes the microinstructions from the control memory, similar to how the processor fetches and executes the instructions from the main memory.
- The advantage of using a microprogrammed control unit is that it is easier to modify and update the control logic by changing the microinstructions in the control memory.
- The disadvantage is that it may be slower and less efficient than a hardwired control unit.
- The sub cycles of the control unit depend on the type and structure of the instruction set of the processor.
- Each instruction is executed during an instruction cycle made up of shorter sub cycles.
- The instruction cycle can be divided into four main sub cycles: fetch, decode, execute, and store.
- The fetch sub cycle is the first sub cycle of the instruction cycle, in which the control unit fetches the instruction from the memory and stores it in the instruction register .
- The decode sub cycle is the second sub cycle of the instruction cycle, in which the control unit decodes the instruction and determines the operation code and the operands .
- The execute sub cycle is the third sub cycle of the instruction cycle, in which the control unit executes the instruction by performing the specified micro-operations .
- The store sub cycle is the fourth sub cycle of the instruction cycle, in which the control unit stores the result of the execution in the memory or a register .
- Some instructions may require additional sub cycles, such as indirect, interrupt, or branch sub cycles.
- The indirect sub cycle is used when the instruction contains an indirect address, which means that the actual address of the operand is stored in another memory location.
- The interrupt sub cycle is used when the processor receives an interrupt signal from an external device, which means that the current instruction execution is suspended and a special interrupt service routine is executed.
- The branch sub cycle is used when the instruction is a conditional or unconditional branch, which means that the next instruction to be executed is not the sequential one, but the one specified by the branch target address.
- The number and order of the sub cycles may vary depending on the processor design and the instruction format.
- The control unit is responsible for controlling the timing and synchronization of the sub cycles by using a clock signal and a state counter.
- The clock signal is a periodic pulse that determines the speed of the processor.
- The state counter is a register that keeps track of the current sub cycle and generates the corresponding control signals.



# Fetch and Execute Cycle

- The fetch and execute cycle is the basic operation or instruction cycle of a computer  .
- It is the process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions.
- The cycle consists of several stages, which are usually divided into two phases: fetch and execute  .
- The fetch phase involves the following steps:
  - The address of the next instruction to be executed is stored in the program counter (PC) register.
  - The address in the PC is moved to the memory address register (MAR), which is connected to the address lines of the system bus.
  - The PC is incremented by one to point to the next instruction.
  - The instruction stored at the address in the MAR is fetched from the memory and placed in the memory data register (MDR), which is connected to the data lines of the system bus.
  - The instruction in the MDR is moved to the instruction register (IR), where it is decoded and interpreted by the control unit.
- The execute phase involves the following steps:
  - The control unit generates the appropriate control signals to direct the data movement and processing required by the instruction.
  - The operands (data) needed by the instruction are fetched from the registers or memory and placed in the arithmetic logic unit (ALU) or other functional units.
  - The ALU or other functional units perform the operation specified by the instruction and store the result in a register or memory.
  - The cycle repeats for the next instruction until the program is completed or interrupted.
- The fetch and execute cycle is also known as the fetch-decode-execute cycle or FDX.



# Micro-operations

- Micro-operations are the basic or atomic operations of a processor .
- They are used to implement complex machine instructions.
- They usually perform operations on data stored in one or more registers .
- They can be classified into four categories:
  - Register transfer micro-operations: They transfer data between registers or between registers and external buses.
  - Arithmetic micro-operations: They perform arithmetic operations on numeric data stored in registers.
  - Logic micro-operations: They perform bit-wise logical operations on non-numeric data stored in registers.
  - Shift micro-operations: They perform serial transfer of data and support arithmetic, logic, and data-processing operations .
- Micro-operations can be expressed using symbols and notations :
  - R1 ← R2: Transfer the content of register R2 to register R1.
  - R3 ← R1 + R2: Add the content of registers R1 and R2 and store the result in register R3.
  - R1 ← R1 ^ R2: Perform bitwise XOR operation on the content of registers R1 and R2 and store the result in register R1.
  - R1 ← shl R1: Shift the content of register R1 one bit position to the left.
- Micro-operations are executed by the control unit of the processor.
- Micro-operations are synchronized by a common clock.
- Micro-operations can be performed in parallel or in sequence.
- Micro-operations are the building blocks of instruction execution.



# Execution of a Complete Instruction

- A complete instruction is a sequence of bits that specifies an operation to be performed by the processor and the operands to be used in the operation.
- The execution of a complete instruction involves the following steps:
  - **Instruction fetch**: The processor fetches the instruction from the memory using the program counter (PC) register, which holds the address of the next instruction to be executed. The instruction is loaded into the instruction register (IR) and the PC is incremented by the instruction length.
  - **Instruction decode**: The processor decodes the instruction by examining the opcode field, which indicates the type and format of the instruction. The processor also determines the operands to be used in the operation, which may be specified in the instruction itself (immediate operands), in registers (register operands), or in memory (memory operands).
  - **Operand fetch**: The processor fetches the operands from the sources specified in the instruction. For register operands, the processor accesses the register file, which is a set of registers that store data values. For memory operands, the processor accesses the memory using the address specified in the instruction or computed from the instruction (effective address). For immediate operands, the processor uses the value embedded in the instruction.
  - **Execute**: The processor performs the operation specified by the opcode using the operands fetched in the previous step. The operation may be an arithmetic, logical, or bitwise operation, a data transfer, a control transfer, or a system call. The result of the operation may be stored in a register or in memory, depending on the instruction.
  - **Write back**: The processor writes the result of the operation to the destination specified in the instruction. For register operands, the processor writes the result to the register file. For memory operands, the processor writes the result to the memory using the address specified in the instruction or computed from the instruction.
  - **Update PC**: The processor updates the PC to point to the next instruction to be executed. For most instructions, the PC is simply incremented by the instruction length. For branch instructions, the PC is changed to the target address of the branch, which may be specified in the instruction or computed from the instruction. For jump instructions, the PC is changed to the address specified in the instruction or in a register. For subroutine instructions, the PC is changed to the address of the subroutine and the return address is saved in a register or in memory.

- The execution of a complete instruction may vary depending on the instruction set architecture (ISA) and the processor design. Some ISAs have fixed-length instructions, while others have variable-length instructions. Some ISAs have simple and uniform instruction formats, while others have complex and irregular instruction formats. Some processors have single-cycle execution, while others have multi-cycle or pipelined execution. Some processors have hardwired control, while others have microprogrammed control.



# Program Control

Program control is the process of directing the execution of instructions in a computer program. Program control can be achieved by using different types of instructions, such as:

- **Arithmetic and logic instructions**: These instructions perform operations on data, such as addition, subtraction, multiplication, division, and, or, not, etc. These instructions can also set or test some flags in the processor, such as zero, carry, overflow, etc. These flags can be used to control the flow of the program based on some conditions.
- **Data transfer instructions**: These instructions move data between registers, memory, and input/output devices. These instructions can also load or store data from or to memory, or transfer data between different addressing modes, such as immediate, direct, indirect, register, etc.
- **Input/output instructions**: These instructions communicate with external devices, such as keyboards, monitors, printers, disks, etc. These instructions can read or write data from or to the devices, or check their status or control signals.
- **Program control instructions**: These instructions change the sequence of execution of the program, such as branching, jumping, calling, returning, etc. These instructions can be conditional or unconditional, depending on whether they depend on some flags or not. These instructions can also be relative or absolute, depending on whether they use an offset or an address to specify the destination of the control transfer.

Program control instructions are essential for implementing various programming constructs, such as loops, if-else statements, switch-case statements, functions, procedures, etc. Program control instructions can also be used to implement interrupts, exceptions, and traps, which are mechanisms to handle abnormal or unexpected events during the execution of the program.

Program control can be implemented by using different types of control units in the processor, such as:

- **Hardwired control unit**: This type of control unit uses a fixed logic circuit to generate the control signals for each instruction. The logic circuit is designed based on the instruction format, the operation code, and the micro-operations. The advantage of this type of control unit is that it is fast and simple. The disadvantage is that it is inflexible and difficult to modify or expand.
- **Microprogrammed control unit**: This type of control unit uses a memory to store the control signals for each instruction as words, called micro-instructions. The micro-instructions are executed by a microprogram, which is a sequence of micro-instructions that perform a specific instruction. The advantage of this type of control unit is that it is flexible and easy to modify or expand. The disadvantage is that it is slower and more complex than the hardwired control unit.



# Reduced Instruction Set Computer

- A reduced instruction set computer (RISC) is a computer that uses a central processing unit (CPU) that implements the processor design principle of simplified instructions.
- RISC is the opposite of complex instruction set computer (CISC), which uses more complex and varied instructions to perform tasks.
- The main idea behind RISC is to make hardware simpler and faster by using a smaller number of types of instructions that can operate at a higher speed .
- Some of the characteristics of RISC are:
  - Fixed-length and simple instruction format
  - Single-cycle instruction execution
  - Large number of general-purpose registers
  - Load/store architecture for memory access
  - Hardwired control unit for instruction decoding
  - Pipelining for instruction-level parallelism
- Some of the advantages of RISC are :
  - Higher performance due to faster instruction execution
  - Easier compiler design and optimization
  - Lower power consumption and heat dissipation
  - Smaller chip size and lower cost
- Some of the disadvantages of RISC are :
  - Larger code size due to more instructions
  - More memory bandwidth and cache required
  - Less support for complex operations and addressing modes
  - Less compatibility with existing software and standards



# Pipelining

- Pipelining is a technique for breaking down a sequential process into various sub-operations and executing each sub-operation in its own dedicated segment that runs in parallel with all other segments.
- Pipelining defines the temporal overlapping of processing. Pipelines are emptiness greater than assembly lines in computing that can be used either for instruction processing or, in a more general method, for executing any complex operations.
- Pipelining is the process of accumulating instruction from the processor through a pipeline. It allows storing and executing instructions in an orderly process. It is also known as pipeline processing.
- A pipeline has two ends, the input end and the output end. Between these ends, there are several stages that perform different operations on the data or instructions.
- Interface registers are used to hold the intermediate output between two stages. These interface registers are also known as pipeline registers or pipeline latches.
- All the stages in the pipeline along with the interface registers are connected in a linear fashion. The output of one stage is fed as the input to the next stage.
- The stages in the pipeline are synchronized by a common clock. Each stage performs its operation in one clock cycle and passes the result to the next stage in the next clock cycle.
- The main advantage of pipelining is that it increases the throughput of the processor, i.e., the number of instructions executed per unit time. This is because multiple instructions are processed simultaneously at different stages of the pipeline .
- The main disadvantage of pipelining is that it introduces some overheads and complexities, such as pipeline hazards, stalls, and bubbles. These are the situations that prevent the pipeline from operating at its full capacity and cause delays or inefficiencies .
- There are different types of pipelining, such as instruction pipelining, data pipelining, arithmetic pipelining, and superscalar pipelining. Each type has its own characteristics and applications .



# Hardwired and Microprogrammed Control Unit

- A control unit is a component of a computer system that controls the execution of instructions by the processor.
- There are two main types of control units: hardwired and microprogrammed.
- A hardwired control unit is implemented using a hardware circuit that generates control signals based on the current instruction and the state of the processor  .
- A microprogrammed control unit is implemented by storing a sequence of microinstructions in a control memory that specify the control signals for each instruction    .
- The main differences between hardwired and microprogrammed control units are:

  - A hardwired control unit is faster, simpler, and more efficient than a microprogrammed control unit, but it is more difficult to design, modify, and decode     .
  - A hardwired control unit is suitable for RISC (Reduced Instruction Set Computer) architectures that have a small and fixed set of instructions, while a microprogrammed control unit is suitable for CISC (Complex Instruction Set Computer) architectures that have a large and variable set of instructions    .
  - A hardwired control unit is implemented as a finite state machine that changes its state according to the input signals, while a microprogrammed control unit is implemented as a microprogram sequencer that fetches and executes microinstructions from the control memory  .
  - A hardwired control unit has a fixed logic circuit that cannot be changed, while a microprogrammed control unit has a programmable control memory that can be updated or replaced  .



# Microprogram Sequencing

- Microprogram sequencing is the process of generating the addresses of the microinstructions stored in the control memory of a microprogrammed control unit .
- The microinstructions contain the control signals that determine the operation of the data path components of the CPU .
- The microprogram sequencer is the component that performs the microprogram sequencing. It can be designed with different techniques and features to suit the requirements of the CPU  .
- Some of the factors that affect the design of the microprogram sequencer are:
  - The size of the microinstruction: The larger the microinstruction, the more control signals it can encode, but the more control memory space it requires.
  - The time of the microinstruction: The faster the microinstruction, the shorter the CPU cycle time, but the more complex the control logic and the data path.
  - The format of the microinstruction: The format determines how the microinstruction specifies the next microinstruction address and the conditional branching logic.
  - The organization of the control memory: The control memory can be organized as a linear array, a matrix, or a tree, depending on the access time and the flexibility of the microprogram.
- Some of the common techniques for microprogram sequencing are:
  - Horizontal microprogramming: The microinstruction contains all the control signals in parallel, and the next microinstruction address is calculated by incrementing the current address or by using a field in the microinstruction.
  - Vertical microprogramming: The microinstruction contains a subset of the control signals in serial, and the next microinstruction address is calculated by using a field in the microinstruction or by using a separate address register.
  - Hybrid microprogramming: The microinstruction contains a combination of horizontal and vertical fields, and the next microinstruction address is calculated by using different methods depending on the field type.
  - Conditional microprogramming: The microinstruction contains a condition field that specifies a condition to be tested by the data path, and the next microinstruction address is calculated by using a branch field or a branch register.
  - Subroutine microprogramming: The microinstruction contains a subroutine field that specifies a subroutine to be executed by the microprogram sequencer, and the next microinstruction address is calculated by using a stack or a queue.
- Some of the advanced features for microprogram sequencing are:
  - Microprogram counter: A register that holds the current microinstruction address and can be modified by the microprogram sequencer or the data path.
  - Microprogram register: A register that holds the current microinstruction and can be modified by the microprogram sequencer or the data path.
  - Microprogram cache: A small and fast memory that holds a subset of the microinstructions and can be accessed by the microprogram sequencer faster than the control memory.
  - Microprogram ROM: A read-only memory that holds a fixed set of microinstructions and can be accessed by the microprogram sequencer without modification.
  - Microprogram RAM: A read-write memory that holds a variable set of microinstructions and can be accessed and modified by the microprogram sequencer or the data path.



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



## Unit 4 - Memory

Memory is the mental process of encoding, storing and retrieving information. Memory can be divided into three main types: sensory memory, short-term memory and long-term memory.

- Sensory memory is the brief and transient storage of sensory information, such as visual, auditory or tactile stimuli. Sensory memory lasts for less than a second and has a large capacity. Sensory memory can be further divided into iconic memory (visual), echoic memory (auditory) and haptic memory (touch).
- Short-term memory (STM) is the temporary storage of information that can be consciously accessed and manipulated. STM has a limited capacity of about 7 +/- 2 items and a duration of about 15-30 seconds. STM can be improved by chunking, rehearsal and mnemonics. STM can be further divided into phonological loop (verbal), visuospatial sketchpad (visual) and central executive (control).
- Long-term memory (LTM) is the permanent and relatively unlimited storage of information that can be retrieved and used later. LTM has a large capacity and a long duration. LTM can be divided into declarative memory (explicit) and procedural memory (implicit).
  - Declarative memory is the memory of facts and events that can be consciously recalled and verbally expressed. Declarative memory can be further divided into semantic memory (general knowledge) and episodic memory (personal experiences).
  - Procedural memory is the memory of skills and habits that can be performed automatically and unconsciously. Procedural memory includes motor skills, cognitive skills and classical conditioning.

Memory can be affected by various factors, such as attention, encoding, retrieval, interference, forgetting and distortion. Memory can also be improved by various strategies, such as elaboration, organization, imagery, testing and spacing. Memory is an essential cognitive function that enables us to learn, remember and use information in our daily lives.



# Basic concept and hierarchy of memory in computer organization and architecture

- Memory is the component of a computer system that stores data and instructions for processing.
- Memory can be classified into different types based on their speed, capacity, cost, and volatility (whether they retain data when power is off or not).
- Memory hierarchy is the arrangement of different types of memory in a computer system according to their response time, complexity, and capacity.
- The memory hierarchy aims to achieve a balance between performance and cost by using faster and smaller memory near the processor and slower and larger memory farther from the processor.
- The memory hierarchy consists of the following levels:

  - **Register**: The fastest and smallest type of memory, located inside the processor, used to store temporary data and control information.
  - **Cache memory**: A small and fast type of memory, located between the processor and the main memory, used to store frequently accessed data and instructions.
  - **Main memory**: The primary memory of the computer system, located on the motherboard, used to store data and instructions that are currently in use by the processor.
  - **Auxiliary memory**: The secondary or external memory of the computer system, located outside the motherboard, used to store large amounts of data and instructions that are not frequently accessed by the processor.
  - **Associative memory**: A special type of memory, located either inside or outside the processor, used to store data and instructions based on their content rather than their address.

- The memory hierarchy can be represented by the following diagram:

  ```
  +-----------------+
  |    Register     |
  +-----------------+
         |
         |
         V
  +-----------------+
  |   Cache memory  |
  +-----------------+
         |
         |
         V
  +-----------------+
  |   Main memory   |
  +-----------------+
         |
         |
         V
  +-----------------+
  | Auxiliary memory|
  +-----------------+
         |
         |
         V
  +-----------------+
  |Associative memory|
  +-----------------+
  ```

- The memory hierarchy follows the principle of locality of reference, which states that a program tends to access the same or nearby memory locations repeatedly over a short period of time.
- The memory hierarchy exploits this principle by keeping the most frequently accessed data and instructions in the faster and smaller memory levels and the less frequently accessed data and instructions in the slower and larger memory levels.
- The memory hierarchy improves the performance and efficiency of the computer system by reducing the average memory access time and the memory bandwidth requirement.



# Semiconductor RAM Memories

Semiconductor RAM memories are a type of volatile memory that store data in integrated circuits using metal-oxide-semiconductor (MOS) technology. They allow random access to data, meaning that any location can be read or written in any order. They are used for temporary storage of data and instructions in computers and other devices.

Some of the main characteristics of semiconductor RAM memories are:

- They have fast access time, ranging from 10 ns to 100 ns.
- They have high density, meaning that they can store more bits per unit area.
- They have low power consumption, compared to other types of memory.
- They have high cost per bit, due to the complexity of fabrication and packaging.
- They have limited storage capacity, due to the physical limitations of the technology.
- They lose data when the power supply is turned off, unless they have a backup battery or capacitor.

There are two basic types of semiconductor RAM memories: static RAM (SRAM) and dynamic RAM (DRAM).

- SRAM uses bistable latches to store each bit of data. It does not need to be refreshed periodically, as the data is maintained as long as the power is on. It has faster access time, lower power consumption, and higher reliability than DRAM. However, it also has lower density, higher cost, and larger size than DRAM. It is mainly used for cache memory, registers, and buffers.
- DRAM uses capacitors to store each bit of data. It needs to be refreshed periodically, as the charge on the capacitors leaks over time. It has slower access time, higher power consumption, and lower reliability than SRAM. However, it also has higher density, lower cost, and smaller size than SRAM. It is mainly used for main memory, video memory, and mobile devices.

There are also various subtypes of SRAM and DRAM, such as:

- Synchronous SRAM (SSRAM), which uses a clock signal to synchronize the data transfer with the processor.
- Asynchronous SRAM (ASRAM), which does not use a clock signal and operates independently of the processor.
- Synchronous DRAM (SDRAM), which uses a clock signal to synchronize the data transfer with the processor and can operate at higher speeds than conventional DRAM.
- Double Data Rate SDRAM (DDR SDRAM), which transfers data on both the rising and falling edges of the clock signal, effectively doubling the data rate.
- Magnetoresistive RAM (MRAM), which uses magnetic tunnel junctions to store data and does not need to be refreshed. It has the advantages of both SRAM and DRAM, such as fast access time, high density, low power consumption, and non-volatility. However, it also has high cost and technical challenges.

These are some of the basic concepts of semiconductor RAM memories. For more details, you can refer to the following sources:

: RAM: Semiconductor Memories, RAM Definition, Basic Types - Testbook Learn
: What are Semiconductor Memory Types? RAM & ROM - Binary Terms
: Semiconductor memory | Types (RAM, ROM, DRAM, SROM, SDRAM, MRAM, PROM ...
: Memories - Infineon Technologies
: Semiconductor memory - Wikipedia
: Semiconductor Memories and Systems | ScienceDirect



# 2D & 2 1/2D Memory Organization

- 2D memory organization is a way of arranging memory cells in a matrix of rows and columns, where each row contains a word of data  .
- A word is a fixed-sized unit of data that can be accessed or manipulated by the processor.
- A decoder is a combinational circuit that converts a binary code into a corresponding output signal.
- A decoder is used to select a row or a column of the memory matrix by decoding the address bits  .
- The advantages of 2D memory organization are:
  - It is simple and easy to implement .
  - It can store large amounts of data in a compact space .
- The disadvantages of 2D memory organization are:
  - It requires more hardware components, such as decoders and gates, which increase the cost and complexity .
  - It does not support error correction or detection, which can lead to data corruption or loss .
  - It has a long access time, as it needs to select both a row and a column for each memory access .

- 2 1/2D memory organization is a modification of 2D memory organization, where each row of the memory matrix is divided into smaller segments, called blocks  .
- A block is a group of consecutive words that can be accessed together by the processor.
- A block decoder is used to select a block within a row by decoding the block address bits  .
- The advantages of 2 1/2D memory organization are:
  - It reduces the hardware complexity, as it requires fewer gates and decoders than 2D memory organization .
  - It supports error correction or detection, as each block can have a parity bit or a checksum to verify the data integrity .
  - It improves the access time, as it can transfer multiple words in a single memory access .
- The disadvantages of 2 1/2D memory organization are:
  - It increases the memory wastage, as some blocks may not be fully utilized by the processor .
  - It requires more address bits, as it needs to specify both the row, the column, and the block within the row .



# ROM Memories

- ROM stands for Read Only Memory. It is a type of non-volatile memory that stores data permanently and cannot be modified or erased by the user.
- ROM is used to store fixed programs that are not to be altered and for tables of constants that are not subject to change. For example, ROM is used to store the computer’s BIOS (basic input/output system), which contains the instructions for booting the computer, as well as firmware for other hardware devices.
- ROM is also used to implement any combinational circuit with k inputs and n outputs. For example, ROM can be used to implement a decoder, a multiplexer, or a look-up table.
- ROM is based on semiconductor technology. There are different types of ROM, such as mask-programmed ROM, programmable ROM (PROM), erasable programmable ROM (EPROM), electrically erasable programmable ROM (EEPROM), and flash memory .
- The main characteristics of ROM are:
  - It is non-volatile, which means it retains data even when the power is turned off.
  - It is read-only, which means it can only be read and not written or modified by the user.
  - It is random access, which means it can access any location in the memory in the same amount of time.
  - It is static, which means it does not require refreshing to maintain the data.
  - It is relatively slow, which means it has a longer access time than RAM.
  - It is relatively expensive, which means it has a higher cost per bit than RAM.
  - It is relatively small, which means it has a lower storage capacity than RAM.



# Cache Memories

Cache memory is a special type of memory that is used to improve the performance of the CPU by reducing the access time to the main memory. Cache memory is faster than main memory, but smaller in size and more expensive. Cache memory is located between the CPU and the main memory, and acts as a buffer that stores frequently used data and instructions.

Some of the topics that are covered in the notes of Unit 4 - Memory in the subject of Computer Organization and Architecture are:

- Cache memory organization and operation
- Cache memory mapping techniques
- Cache memory performance and optimization
- Cache memory hierarchy and levels
- Cache memory coherence and consistency

## Cache Memory Organization and Operation

- Cache memory consists of two components: a cache controller and a cache store.
- The cache controller is responsible for managing the data transfer between the CPU and the cache store, and between the cache store and the main memory.
- The cache store is divided into equal-sized blocks, each of which can store a fixed number of bytes of data.
- The main memory is also divided into blocks of the same size as the cache store blocks, and each block has a unique address.
- The cache controller maintains a tag for each block in the cache store, which indicates the address of the corresponding block in the main memory.
- When the CPU requests data or instructions from a memory address, the cache controller checks if the block containing that address is present in the cache store, by comparing the tag with the address.
- If the block is present, the cache controller returns the data or instructions to the CPU from the cache store. This is called a cache hit.
- If the block is not present, the cache controller fetches the block from the main memory and stores it in the cache store, replacing an existing block if necessary. This is called a cache miss.
- The cache controller uses a replacement policy to decide which block to replace in the cache store when a cache miss occurs. Some common replacement policies are FIFO, LRU, LFU, and Random.
- The cache controller also uses a write policy to decide how to handle write operations from the CPU to the cache store. Some common write policies are write-through, write-back, write-allocate, and write-no-allocate.

## Cache Memory Mapping Techniques

- Cache memory mapping techniques are the methods used by the cache controller to determine the location of a block in the cache store, given its address in the main memory.
- There are three main types of cache memory mapping techniques: direct mapping, associative mapping, and set-associative mapping.
- Direct mapping: In this technique, each block in the main memory is mapped to exactly one block in the cache store, based on a simple modulo function. For example, if the cache store has 16 blocks, then the block with address A in the main memory is mapped to the block with index A mod 16 in the cache store. This technique is simple and fast, but it may cause high conflict misses, which occur when two or more blocks in the main memory map to the same block in the cache store.
- Associative mapping: In this technique, each block in the main memory can be mapped to any block in the cache store, based on the availability of free blocks. The cache controller uses a tag comparator to search for the block in the cache store, by comparing the tag with the address of the block in the main memory. This technique is flexible and reduces conflict misses, but it is complex and slow, as it requires a full search of the cache store.
- Set-associative mapping: In this technique, each block in the main memory is mapped to a specific set of blocks in the cache store, based on a partial modulo function. For example, if the cache store has 16 blocks, and each set has 4 blocks, then the block with address A in the main memory is mapped to the set with index A mod 4 in the cache store. Within the set, the block can be mapped to any of the 4 blocks, based on the availability of free blocks. The cache controller uses a tag comparator to search for the block in the set, by comparing the tag with the address of the block in the main memory. This technique is a compromise between direct mapping and associative mapping, as it balances the trade-off between simplicity and flexibility.

## Cache Memory Performance and Optimization

- Cache memory performance is measured by two main metrics: hit rate and miss penalty.
- Hit rate is the ratio of the number of cache hits to the total number of memory requests from the CPU. Hit rate indicates how often the cache memory can satisfy the CPU requests without accessing the main



# Concept and Design Issues & Performance for the Notes of the Unit 4 - Memory in the Subject of Computer Organization and Architecture

- Memory is a crucial component of a computer system that stores data and instructions for processing.
- Memory can be classified into different types and levels based on various factors such as capacity, access time, cost, and performance.
- Memory hierarchy is a concept that organizes memory into different levels, such that the higher levels have smaller capacity, faster access time, higher cost, and better performance than the lower levels.
- The main types of memory in a computer system are:

  - Register: The fastest and most expensive type of memory that is located inside the CPU and holds data and instructions that are currently being executed.
  - Cache: A small and fast type of memory that is located between the CPU and the main memory and holds frequently accessed data and instructions to reduce the average access time.
  - Main memory: A large and relatively slow type of memory that is directly accessible by the CPU and holds data and instructions that are currently in use by the programs.
  - Auxiliary memory: The largest and slowest type of memory that is external to the CPU and holds data and instructions that are not currently in use by the programs.

- Some of the design issues and performance factors that affect memory are:

  - Addressing: The method of identifying and locating data and instructions in memory. There are different types of addressing schemes such as direct, indirect, indexed, relative, etc.
  - Mapping: The method of assigning addresses to the physical locations of data and instructions in memory. There are different types of mapping techniques such as direct, associative, set-associative, etc.
  - Replacement: The method of choosing which data and instructions to remove from memory when there is no space available for new ones. There are different types of replacement policies such as least recently used (LRU), first in first out (FIFO), random, etc.
  - Write policy: The method of updating data and instructions in memory when they are modified by the CPU. There are two main types of write policies: write-through and write-back.
  - Locality: The principle that states that data and instructions that are accessed once are likely to be accessed again soon. There are two types of locality: temporal and spatial.
  - Hit ratio: The ratio of the number of successful accesses to memory to the total number of accesses. A higher hit ratio indicates better performance of memory.
  - Miss penalty: The additional time required to access memory when the requested data or instruction is not found in the desired level. A lower miss penalty indicates better performance of memory.



# Address Mapping and Replacement

- Address mapping is the process of translating a logical address (also called a virtual address) into a physical address (also called a real address) that corresponds to a location in the main memory or the cache memory.
- Address mapping is necessary because the logical address space of a process may be different from the physical address space of the memory, and the cache memory may not contain all the blocks of the main memory.
- Address mapping is performed by a hardware device called the memory management unit (MMU), which uses a mapping function to map a logical address to a physical address.
- Address mapping can be done using different techniques, such as paging, segmentation, or a combination of both.
- Paging is a technique that divides the logical address space and the physical address space into fixed-size units called pages and frames, respectively. Each page has a unique page number and each frame has a unique frame number. The MMU uses a page table to store the mapping between page numbers and frame numbers. The page table is stored in the main memory and has an entry for each page of the logical address space. The MMU uses the page number of the logical address as an index to the page table and obtains the corresponding frame number. The frame number and the offset of the logical address are then concatenated to form the physical address.
- Segmentation is a technique that divides the logical address space and the physical address space into variable-size units called segments. Each segment has a unique segment number and a base address that indicates the starting location of the segment in the physical address space. The MMU uses a segment table to store the mapping between segment numbers and base addresses. The segment table is stored in the main memory and has an entry for each segment of the logical address space. The MMU uses the segment number of the logical address as an index to the segment table and obtains the corresponding base address. The base address and the offset of the logical address are then added to form the physical address.
- Paging and segmentation can be combined to provide a two-level address mapping scheme. In this scheme, the logical address space is divided into segments, and each segment is further divided into pages. The MMU uses a segment table and a page table for each segment to map a logical address to a physical address. The MMU first uses the segment number of the logical address as an index to the segment table and obtains the base address of the page table for that segment. The MMU then uses the page number of the logical address as an index to the page table and obtains the frame number of the page. The frame number and the offset of the logical address are then concatenated to form the physical address.

- Address replacement is the process of selecting a block of the cache memory to be replaced by a new block of the main memory when the cache is full and a cache miss occurs.
- Address replacement is necessary because the cache memory has a limited size and cannot store all the blocks of the main memory. Therefore, some blocks of the cache memory have to be replaced by new blocks of the main memory when they are needed by the processor.
- Address replacement is performed by a hardware device called the cache controller, which uses a replacement algorithm to select a block of the cache memory to be replaced.
- Address replacement can be done using different techniques, such as direct mapping, associative mapping, or set-associative mapping.
- Direct mapping is a technique that maps each block of the main memory to exactly one block of the cache memory. The cache memory is divided into lines, and each line has a unique line number. The cache controller uses a mapping function to map a block number of the main memory to a line number of the cache memory. The mapping function is usually a modulo operation that takes the lower bits of the block number and divides them by the number of lines in the cache. The cache controller then compares the tag of the block number with the tag of the line number to determine if there is a cache hit or a cache miss. If there is a cache miss, the cache controller replaces the entire line of the cache memory with the new block of the main memory.
- Associative mapping is a technique that maps each block of the main memory to any block of the cache memory. The cache memory is divided into lines, and each line has a valid bit and a tag. The cache controller uses a comparison function to compare the tag of the block number of the main memory with the tags of all the lines of the cache memory simultaneously. The cache controller then determines if there is a cache hit or a cache miss. If there is a cache miss, the cache controller uses a replacement algorithm to select a



# Auxiliary memories

- Auxiliary memories are the lowest-cost, highest-capacity and slowest-access storage devices in a computer system .
- They are used to store programs and data for long-term storage or when not in immediate use .
- They are nonvolatile, which means they retain the data even when the power is off.
- Some examples of auxiliary memories are magnetic tapes, magnetic disks, optical disks, flash drives, etc .




# Magnetic Disk

- A magnetic disk is a type of secondary memory that consists of a flat disc with a magnetic coating that stores data .
- It is used to store various programs and files that are not needed by the computer when it is running .
- The magnetic coating can be polarized in one direction or the opposite direction to represent binary data (1 or 0) .
- The disk is divided into circular tracks and sectors, which are the smallest units of data that can be accessed.
- A read/write head moves over the disk surface to read or write data on the sectors .
- The disk rotates at a high speed to allow fast access to the data .
- The access time of a magnetic disk depends on the seek time (the time to move the head to the desired track), the rotational latency (the time to wait for the desired sector to come under the head), and the transfer rate (the speed of reading or writing data).
- Magnetic disks can be classified into hard disks, floppy disks, and optical disks based on their size, capacity, and technology .
- Hard disks have a large capacity and a fast access time, but they are expensive and sensitive to physical damage .
- Floppy disks have a small capacity and a slow access time, but they are cheap and portable .
- Optical disks use a laser beam to read or write data on a reflective surface, and they have a higher capacity and a longer lifespan than magnetic disks, but they are slower and more expensive .
- Magnetic disks are one of the oldest forms of computer memory, dating back to the 1950s when they were used as magnetic drum memory.



# Magnetic Tape Memory

- Magnetic tape is a system for storing digital information on a thin plastic ribbon that is coated with magnetic material.
- Magnetic tape was developed in Germany in 1928 for audio storage and was first used for computer data storage in 1951 in the UNIVAC I computer.
- Magnetic tape is a sequential memory, which means that data can only be accessed in a linear order by moving the tape past a read/write head .
- Magnetic tape has a low data read/write speed compared to other memory devices, but it has a high storage capacity and reliability.
- Magnetic tape is mainly used for backup, archival, and long-term data preservation purposes, as well as for some specialized applications such as video recording and scientific data collection.



# Optical Disks

- Optical disks are a type of secondary storage device that use a laser beam to read and write data on a rotating disk coated with a reflective material  .
- Optical disks offer high capacity, portability, durability, and low cost compared to magnetic disks .
- Optical disks come in various formats, such as CD-ROM, CD-R, CD-RW, DVD-ROM, DVD-R, DVD-RW, Blu-ray, and Ultra HD Blu-ray .
- Optical disks can be classified into three categories based on their write capability  :
  - Read-only optical disks (ROM): These disks are pre-recorded with data that cannot be modified by the user. Examples are CD-ROM and DVD-ROM.
  - Write-once optical disks (WORM): These disks allow the user to write data once, but not erase or modify it. Examples are CD-R and DVD-R.
  - Rewritable optical disks (RW): These disks allow the user to write, erase, and rewrite data multiple times. Examples are CD-RW, DVD-RW, and Blu-ray.
- Optical disks use a laser beam to read and write data on the disk surface. The laser beam is focused by a lens on a small spot on the disk, where it can either reflect or be absorbed by the disk material  .
- The disk surface is divided into concentric tracks, which are further divided into sectors. Each sector can store a fixed amount of data, such as 2 KB for CD-ROM and 32 KB for DVD-ROM .
- The data on the disk is encoded using a technique called eight-to-fourteen modulation (EFM), which converts each 8-bit byte into a 14-bit code that avoids long sequences of zeros or ones. This reduces the possibility of errors and improves the reliability of the disk .
- The data on the disk is also protected by error detection and correction codes, such as cyclic redundancy check (CRC) and Reed-Solomon codes, which can detect and correct errors caused by scratches, dust, or defects on the disk surface .
- The data transfer rate of optical disks depends on the rotational speed of the disk, the number of tracks, the density of data, and the type of interface. The rotational speed of optical disks is usually expressed in terms of multiples of a base speed, such as 1x, 2x, 4x, etc. For example, a CD-ROM with a 1x speed rotates at 200 rpm and has a data transfer rate of 150 KB/s, while a CD-ROM with a 52x speed rotates at 10,400 rpm and has a data transfer rate of 7.8 MB/s .
- The access time of optical disks consists of three components: seek time, latency, and transfer time. Seek time is the time required to move the read/write head to the desired track. Latency is the time required to wait for the desired sector to rotate under the read/write head. Transfer time is the time required to read or write the data from or to the disk. The access time of optical disks is usually higher than that of magnetic disks, due to the slower rotational speed and the longer seek time .
- Optical disks have several advantages and disadvantages over other types of storage devices. Some of the advantages are  :
  - High capacity: Optical disks can store large amounts of data, ranging from 700 MB for CD-ROM to 128 GB for Ultra HD Blu-ray.
  - Portability: Optical disks are easy to carry and transport, due to their small size and light weight.
  - Durability: Optical disks are resistant to magnetic fields, heat, humidity, and dust, which can damage magnetic disks.
  - Low cost: Optical disks are relatively cheap to produce and purchase, compared to magnetic disks and solid-state drives.
- Some of the disadvantages are  :
  - Low speed: Optical disks have lower data transfer rates and higher access times than magnetic disks and solid-state drives, due to the slower rotational speed and the longer seek time.
  - Fragility: Optical disks are prone to physical damage,



# Virtual Memory

- Virtual memory is a **technique** that allows the execution of programs that are not completely in physical memory.
- Virtual memory creates an **illusion** of a large main memory for the programmer, when in reality the physical memory is limited.
- Virtual memory uses some of the space from **secondary storage** (such as hard disk) and maps it to the **address space** of the process.
- Virtual memory allows **multiple processes** to share the physical memory and run concurrently, without interfering with each other.
- Virtual memory also enables **memory protection**, **relocation**, and **swapping** of processes.

## Characteristics of Virtual Memory

- Virtual memory is **transparent** to the programmer, meaning that the programmer does not need to know how the virtual memory is implemented or managed by the operating system.
- Virtual memory is **dynamic**, meaning that the mapping between the virtual and physical addresses can change during the execution of a process, depending on the availability of physical memory and the demand of the process.
- Virtual memory is **hierarchical**, meaning that the virtual address space is divided into **pages** of fixed size, and the physical memory is divided into **frames** of the same size. A page can be mapped to any frame in the physical memory, or to a location in the secondary storage if the page is not in the physical memory.
- Virtual memory is **associative**, meaning that the mapping between the pages and the frames is not fixed, but can be changed by the operating system using a **page table**. A page table is a data structure that stores the mapping information for each page of a process.
- Virtual memory is **demand-paged**, meaning that a page is only brought into the physical memory when it is needed by the process, not when the process is loaded. This reduces the amount of physical memory required and allows the execution of larger programs than the physical memory can accommodate.
- Virtual memory is **paged-replacement**, meaning that when the physical memory is full and a new page is needed, the operating system must choose a page to **replace** or **evict** from the physical memory and write it back to the secondary storage. The choice of the page to replace is based on a **replacement algorithm** that tries to minimize the number of **page faults**. A page fault occurs when a process tries to access a page that is not in the physical memory.



# Concept Implementation for the Notes of the Unit 4 - Memory in the Subject of Computer Organization and Architecture

- Memory is an essential component of a computer system that stores and retrieves data and instructions. It is organized in the form of cells, each with a unique address.
- Memory can be classified into different types based on various criteria, such as capacity, access time, cost, volatility, etc. Some common types of memory are:
  - Random Access Memory (RAM): It is a volatile memory that can be read and written by the CPU. It is used to store temporary data and instructions during program execution. RAM can be further divided into Static RAM (SRAM) and Dynamic RAM (DRAM).
  - Read Only Memory (ROM): It is a non-volatile memory that can only be read by the CPU. It is used to store permanent data and instructions that do not change frequently. ROM can be further divided into Programmable ROM (PROM), Erasable PROM (EPROM), Electrically Erasable PROM (EEPROM), etc.
  - Cache Memory: It is a small and fast memory that is used to store frequently accessed data and instructions from the main memory. It reduces the average access time and improves the performance of the CPU. Cache memory can be implemented using SRAM or DRAM. Cache memory can be classified into different levels, such as L1, L2, L3, etc., based on their proximity to the CPU.
  - Auxiliary Memory: It is a large and slow memory that is used to store data and instructions that are not currently needed by the CPU. It is also known as secondary memory or external memory. Some examples of auxiliary memory are magnetic disk, magnetic tape, optical disk, flash memory, etc.
  - Virtual Memory: It is a technique that allows the CPU to access more memory than the physical memory available in the system. It is implemented by using a part of the auxiliary memory as an extension of the main memory. Virtual memory creates an illusion of a large and contiguous memory space for the CPU.
- Memory organization in a computer system can be influenced by various factors, such as the instruction set architecture, the memory hierarchy, the memory address mode, the memory mapping and replacement, etc. Some common concepts and design issues related to memory organization are:
  - Instruction Set Architecture (ISA): It is the interface between the hardware and the software of a computer system. It defines the set of instructions, registers, data types, addressing modes, etc., that the CPU can execute. ISA can be classified into two types: Reduced Instruction Set Computer (RISC) and Complex Instruction Set Computer (CISC).
  - Memory Hierarchy: It is the arrangement of different types of memory in a computer system based on their capacity, access time, cost, etc. The memory hierarchy follows the principle of locality, which states that the CPU tends to access the same or nearby memory locations repeatedly. The memory hierarchy aims to provide the CPU with the required data and instructions at the lowest possible cost and time.
  - Memory Address Mode: It is the method of specifying the location of an operand in an instruction. It determines how the CPU calculates the effective address of the operand from the instruction. Some common memory address modes are: immediate, register, direct, indirect, indexed, relative, etc.
  - Memory Mapping: It is the process of assigning a logical address to a physical address in the memory. It determines how the CPU accesses the data and instructions stored in the memory. Memory mapping can be done using different techniques, such as direct mapping, associative mapping, set-associative mapping, etc.
  - Memory Replacement: It is the process of selecting a block of memory to be replaced by a new block of memory when the memory is full. It is used to manage the cache memory and the virtual memory. Memory replacement can be done using different algorithms, such as least recently used (LRU), first in first out (FIFO), least frequently used (LFU), etc.



## Unit 5 - Input / Output

- Input/output (I/O) is the process of transferring data between a computer system and its external devices, such as keyboards, mice, printers, monitors, disks, networks, etc.
- I/O devices can be classified into two categories: character devices and block devices. Character devices transfer data one character at a time, such as keyboards and terminals. Block devices transfer data in fixed-size blocks, such as disks and tapes.
- I/O operations can be performed in different modes: synchronous, asynchronous, buffered, unbuffered, direct, and indirect. Synchronous I/O waits for the completion of the operation before returning control to the program. Asynchronous I/O returns control to the program immediately after issuing the operation, and notifies the program when the operation is completed. Buffered I/O uses an intermediate memory area to store data temporarily before transferring it to or from the device. Unbuffered I/O transfers data directly between the program and the device. Direct I/O bypasses the operating system and accesses the device directly. Indirect I/O uses the operating system to mediate the data transfer between the program and the device.
- I/O operations can be performed using different methods: polling, interrupt-driven, direct memory access (DMA), and I/O channels. Polling is a method where the program repeatedly checks the status of the device until it is ready for data transfer. Interrupt-driven is a method where the device sends a signal to the processor when it is ready for data transfer, and the processor executes a special routine to handle the I/O operation. DMA is a method where a special hardware controller transfers data between the device and the memory without involving the processor. I/O channels are special processors dedicated to handling I/O operations, and they communicate with the main processor using commands and status signals.
- I/O operations can be performed using different interfaces: device registers, device drivers, system calls, libraries, and application programming interfaces (APIs). Device registers are special memory locations that store the status and control information of the device. Device drivers are software modules that manage the communication between the device and the operating system. System calls are functions provided by the operating system that allow programs to request I/O services. Libraries are collections of functions that provide higher-level abstractions and convenience for I/O operations. APIs are sets of rules and conventions that define how programs can interact with the I/O devices and services.



# Peripheral devices for the notes of the Unit 5 - Input / Output in the subject of Computer Organization and Architecture

- Peripheral devices are those devices that are linked either internally or externally to a computer.
- Peripheral devices are used to transfer data, provide auxiliary storage, or perform other functions that are not part of the core computer system architecture.
- Peripheral devices are commonly divided into three kinds: input devices, output devices, and storage devices.
- Input devices are used to convert incoming data and instructions into a pattern of electrical signals in binary code that are comprehensible to a digital computer. Examples of input devices are keyboards, mouse, scanners, microphones, and webcams .
- Output devices are used to convert the binary information stored in the computer memory into a form that can be perceived by human senses. Examples of output devices are display units, printers, loudspeakers, and digital cameras .
- Storage devices are used to store data and instructions for later use or retrieval. Storage devices can be internal or external to the computer case. Examples of storage devices are magnetic disks, tapes, optical disks, and flash drives .



# I/O Interface

- The I/O interface is the method that is used to transfer information between internal storage (memory) and external I/O devices (peripherals)  .
- The I/O devices provide input and output for the computer system, such as keyboard, mouse, monitor, printer, disk, etc. .
- The I/O interface supports a systematic means of controlling interaction with the outside world and providing the operating system with the information it needs to manage I/O activity effectively  .
- The I/O interface consists of the following components   :
  - I/O bus: The communication link between the CPU, memory and I/O modules.
  - I/O module: The device that interfaces the I/O device to the I/O bus. It performs the following functions:
    - Control and timing: It synchronizes the data transfer between the I/O device and the I/O bus.
    - Communication with the CPU: It receives commands and status information from the CPU and sends status and error signals to the CPU.
    - Data buffering: It temporarily stores the data that is being transferred between the I/O device and the I/O bus.
    - Error detection: It checks for any errors that may occur during the data transfer and reports them to the CPU.
  - I/O device: The physical device that performs the input or output operation. It has a mechanical component and an electronic component. The electronic component is called the device controller, which communicates with the I/O module.
- The I/O interface can operate in different modes, such as programmed I/O, interrupt-driven I/O and direct memory access (DMA)   .
  - Programmed I/O: The CPU initiates and controls the data transfer between the I/O device and the memory. The CPU polls the status of the I/O device and waits for it to be ready before transferring the data. This mode is simple but inefficient, as it wastes CPU time and resources.
  - Interrupt-driven I/O: The CPU initiates the data transfer between the I/O device and the memory, but does not wait for it to complete. Instead, the CPU resumes its normal operation and lets the I/O device interrupt it when the data transfer is done. This mode is more efficient than programmed I/O, as it frees the CPU from polling and waiting.
  - Direct memory access (DMA): The CPU delegates the data transfer between the I/O device and the memory to a special hardware device called the DMA controller. The CPU only initiates and terminates the data transfer, but does not control it. The DMA controller takes over the I/O bus and transfers the data directly from the I/O device to the memory, without involving the CPU. This mode is the most efficient, as it reduces the CPU involvement and overhead.



# I/O Ports

- I/O ports are the interfaces between the CPU and the external devices, such as keyboards, mice, printers, scanners, modems, etc.
- I/O ports allow data to be transferred between the internal storage and the external I/O devices.
- I/O ports are controlled by special hardware components called I/O modules, which coordinate the timing and control of the data flow.
- I/O ports can be classified into two types: serial ports and parallel ports.
- Serial ports transmit data one bit at a time, using a single wire or a pair of wires. Serial ports are used for devices that require low data rates, such as modems and older mice. Serial ports have two versions: 9-pin and 25-pin. Data travels at 115 kilobits per second on serial ports.
- Parallel ports transmit data multiple bits at a time, using multiple wires. Parallel ports are used for devices that require high data rates, such as printers and scanners. Parallel ports have a 25-pin model. Data travels at 8 megabytes per second on parallel ports.
- Universal Serial Bus (USB) ports are a special type of serial ports that can support multiple devices using a single port. USB ports can provide power to the connected devices and allow hot swapping, which means devices can be plugged and unplugged without turning off the computer. USB ports have different versions, such as USB 1.1, USB 2.0, USB 3.0, and USB 3.1, which have different data rates and features.
- FireWire ports and Infiniband ports are examples of external I/O interfaces that can support high-speed data transfer and direct memory access (DMA), which means a specialized I/O processor can move a large block of data without involving the CPU. FireWire ports can transfer data at 400 megabits per second or 800 megabits per second, depending on the version. Infiniband ports can transfer data at 2.5 gigabits per second or 10 gigabits per second, depending on the version.

: https://www.tutorialspoint.com/discuss-the-i-o-interface-in-computer-architecture
: https://examradar.com/io-system-organisation/
: https://www.ioenotes.edu.np/media/notes/computer-organization-and-architecture-coa/Chapter7-Input-Output-Organization.pdf
: https://www.geeksforgeeks.org/input-output-ports/
: https://www.ecs.csun.edu/~cputnam/Comp546/Input-Output-Web.pdf



# Interrupts

- An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention.
- Interrupts allow the processor to handle asynchronous events without wasting cycles in polling or busy waiting.
- Interrupts can be classified into hardware interrupts and software interrupts.
  - Hardware interrupts are generated by external devices, such as keyboards, mice, printers, disks, etc., that request the processor to perform some I/O operation .
  - Software interrupts are generated by programs, such as system calls, exceptions, traps, etc., that request the processor to perform some service or handle some error .
- When an interrupt occurs, the processor saves the current state of the program (such as the program counter and the status register) and jumps to a predefined address that contains the interrupt service routine (ISR) .
  - The ISR is a special program that performs the required actions to service the interrupt, such as reading or writing data, sending or receiving signals, etc .
  - After the ISR is completed, the processor restores the saved state of the program and resumes its normal execution .
- Interrupts can be masked or unmasked, depending on whether the processor can ignore or respond to them .
  - Maskable interrupts are those that can be disabled or enabled by the processor, such as I/O interrupts .
  - Non-maskable interrupts are those that cannot be disabled by the processor, such as power failure or system error interrupts .
- Interrupts can be prioritized, depending on the urgency or importance of the event that caused them .
  - Higher priority interrupts can preempt lower priority interrupts, meaning that the processor will service the higher priority interrupt first and then resume the lower priority interrupt .
  - Lower priority interrupts can be deferred or queued, meaning that the processor will service them after the higher priority interrupt or after the current program is finished .
- Interrupts can be handled in different ways, depending on the architecture or design of the system .
  - Vectored interrupts are those that have a fixed address for each ISR, meaning that the processor can directly jump to the ISR without consulting a table or a device .
  - Non-vectored interrupts are those that have a common address for all ISRs, meaning that the processor has to consult a table or a device to find the ISR for the interrupt .
  - Daisy-chained interrupts are those that use a single interrupt request line for multiple devices, meaning that the processor has to poll each device to find the source of the interrupt.
  - Multiple interrupt request lines are those that use separate interrupt request lines for each device, meaning that the processor can identify the source of the interrupt by the line number.



# Interrupt Hardware

- Interrupt hardware is the circuitry that allows a device or a software program to send a signal to the processor to request its attention.
- Interrupts are useful for handling asynchronous events, such as input/output operations, timers, exceptions, or user interactions.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are generated by external devices, such as keyboards, mice, disks, printers, or network cards, that are connected to the interrupt request line (IRQ) of the processor.
- Software interrupts are generated by instructions executed by the processor, such as system calls, traps, or exceptions, that invoke a predefined interrupt service routine (ISR).
- An interrupt service routine is a special program that handles the interrupt and performs the necessary actions, such as reading or writing data, updating registers, or sending signals.
- Interrupts can be enabled or disabled by the processor, depending on the current state of execution. When interrupts are enabled, the processor can respond to interrupt requests. When interrupts are disabled, the processor ignores interrupt requests and continues with the current instruction stream.
- Interrupts can have different priorities, depending on the urgency or importance of the event. Higher priority interrupts can preempt lower priority interrupts, and lower priority interrupts can be deferred or masked until higher priority interrupts are serviced.
- Interrupts can be vectored or non-vectored, depending on the way the processor identifies the source and the address of the ISR. In vectored interrupts, the interrupt request carries a unique identifier or a vector that points to the ISR. In non-vectored interrupts, the processor uses a fixed address or a table to locate the ISR.



# Types of Interrupts and Exceptions

Interrupts and exceptions are events that disrupt the normal flow of execution of a program by the processor. They are handled by changing the control flow to a predefined handler routine that performs the appropriate actions and then returns to the original program.

There are different types of interrupts and exceptions, depending on the source, cause, and nature of the event. Some of the common types are:

- **Normal Interrupts**: These are interrupts that are caused by software instructions, such as system calls, I/O requests, or breakpoints. They are usually expected and planned by the programmer, and they can be masked or disabled by the processor. For example, a program may issue a system call to read data from a file, which triggers a normal interrupt to the operating system.
- **Exceptions**: These are unplanned interrupts that arise within the processor, due to some error or abnormal condition during the execution of an instruction. They can be classified into four subtypes: trap, fault, abort, and reset. 
  - **Trap**: A trap is an exception that is reported immediately after the execution of the instruction that caused it. It is usually used for debugging purposes, such as setting breakpoints or tracing the execution of a program. A trap can also be used to implement system calls or user-defined functions. For example, a program may use a trap instruction to invoke a service routine that prints a message on the screen. 
  - **Fault**: A fault is an exception that is reported before the execution of the instruction that caused it. It is usually caused by an error that can be corrected by the handler routine, such as a page fault, a divide-by-zero error, or an invalid opcode. The handler routine can resume the execution of the instruction after correcting the error, or terminate the program if the error is fatal. For example, a program may cause a page fault when it tries to access a memory location that is not mapped in the virtual address space. The handler routine can then allocate a physical page for the virtual address and resume the execution of the instruction. 
  - **Abort**: An abort is an exception that is reported during the execution of the instruction that caused it. It is usually caused by a severe error that cannot be corrected by the handler routine, such as a parity error, a machine check, or a bus error. The handler routine can only terminate the program or perform some recovery actions, but it cannot resume the execution of the instruction. For example, a program may cause a machine check when it tries to execute an instruction that is not supported by the processor. The handler routine can then display an error message and halt the system. 
  - **Reset**: A reset is an exception that is caused by an external signal, such as a power failure, a hardware reset button, or a watchdog timer. It is the most severe type of exception, as it resets the entire processor and restarts the execution from a predefined address. The handler routine can only perform some initialization tasks, such as setting up the registers, the stack, and the memory. For example, a system may perform a reset when it detects a power failure, to prevent data corruption and ensure a safe restart. 
- **External Interrupts**: These are interrupts that are caused by external devices or controllers, such as keyboards, mice, timers, disks, or network cards. They are usually asynchronous and unpredictable, and they can be prioritized or vectored by the processor. They are used to signal the processor that some event has occurred or some service is required by the device. For example, a keyboard may generate an external interrupt when a key is pressed, to notify the processor that a character is available for input.



# Modes of Data Transfer

Data transfer is the process of moving data from one device or component to another in a computer system. Data transfer can occur between the CPU and the memory, between the CPU and the input/output devices, or between the memory and the input/output devices. Data transfer can be handled in one of three possible modes:

- **Programmed I/O**: In this mode, the CPU executes a program that contains instructions to transfer data to or from an I/O device. Each data item transfer is initiated by an instruction in the program. The CPU monitors the status of the I/O device to determine when the next data item can be transferred. This mode is also called polling or busy-waiting, as the CPU wastes time checking the I/O device repeatedly until it is ready.
- **Interrupt-initiated I/O**: In this mode, the CPU executes a program that contains instructions to transfer data to or from an I/O device. However, instead of waiting for the I/O device to be ready, the CPU issues a command to the I/O device and then proceeds to execute other tasks. When the I/O device completes the data transfer, it sends an interrupt signal to the CPU, which then suspends the current program and executes an interrupt handler routine to process the data. This mode is also called interrupt-driven or asynchronous I/O, as the CPU does not need to synchronize with the I/O device.
- **Direct memory access (DMA)**: In this mode, the CPU delegates the data transfer to a special hardware unit called the DMA controller, which can access the memory and the I/O device independently of the CPU. The CPU initiates the data transfer by supplying the DMA controller with the starting address and the number of words to be transferred, and then proceeds to execute other tasks. The DMA controller transfers the data directly between the memory and the I/O device, without involving the CPU. When the data transfer is completed, the DMA controller sends an interrupt signal to the CPU, which then resumes the current program. This mode is also called block transfer or cycle-stealing, as the DMA controller temporarily takes over the memory bus from the CPU.

The choice of the mode of data transfer depends on several factors, such as the speed of the I/O device, the amount of data to be transferred, the priority of the I/O operation, and the availability of the CPU and the memory resources. Each mode has its own advantages and disadvantages, such as performance, complexity, overhead, and reliability.



# Programmed I/O

- Programmed I/O is a method of transferring data between the CPU and a peripheral device, such as a keyboard, a mouse, a disk, or a network adapter   .
- Programmed I/O operations are the result of I/O instructions written in the computer program .
- In programmed I/O, each data transfer is initiated by the CPU, and the CPU is in continuous monitoring of the interface  .
- Programmed I/O is very cheap and easy to implement, but it has some disadvantages:
  - It consumes a lot of CPU time and resources, as the CPU has to wait for the I/O device to be ready and to perform the data transfer   .
  - It is not suitable for high-speed devices, as the CPU may not be able to keep up with the data rate of the device   .
  - It is not scalable, as the number of I/O devices increases, the CPU will have to handle more I/O instructions and polling loops  .
- Programmed I/O can be implemented in two ways: synchronous and asynchronous:
  - In synchronous programmed I/O, the CPU executes an I/O instruction and then waits for the I/O operation to complete before resuming the execution of the program.
  - In asynchronous programmed I/O, the CPU executes an I/O instruction and then continues to execute the program, until it checks the status of the I/O device periodically or receives a signal from the device indicating the completion of the I/O operation.
- Programmed I/O can be improved by using buffering techniques, such as double buffering or circular buffering, which allow the CPU to transfer data to or from a buffer in memory, while the I/O device transfers data to or from another buffer in memory.



# Interrupt Initiated I/O

- Interrupt initiated I/O is a method of data transfer between the CPU and the I/O devices that does not require the CPU to constantly check the status of the I/O devices.
- In this method, the CPU issues a command to the I/O device and then resumes its normal execution of other tasks.
- When the I/O device is ready for data transfer, it sends an interrupt signal to the CPU, which temporarily suspends its current task and transfers the control to an interrupt handler routine.
- The interrupt handler routine performs the necessary data transfer between the CPU and the I/O device and then returns the control to the CPU, which resumes its previous task.
- Interrupt initiated I/O improves the efficiency of the CPU by reducing the idle time and allowing the CPU to perform other tasks while the I/O device is busy.
- Interrupt initiated I/O also allows multiple I/O devices to communicate with the CPU in a priority-based manner, such that the interrupt from a higher priority device is serviced before the interrupt from a lower priority device.
- Interrupt initiated I/O requires an interrupt mechanism that consists of the following components:
  - An interrupt request line that connects the I/O device to the CPU and carries the interrupt signal.
  - An interrupt controller that receives the interrupt signals from multiple I/O devices and determines the priority and the source of the interrupt.
  - An interrupt vector that identifies the address of the interrupt handler routine for each I/O device.
  - An interrupt enable flag that allows the CPU to enable or disable the interrupt mechanism.
  - An interrupt service routine that performs the data transfer and other operations related to the interrupting I/O device.



# Direct Memory Access for the notes of the Unit 5 - Input / Output in the subject of Computer Organization and Architecture

- Direct Memory Access (DMA) is a feature of computer systems that allows certain hardware subsystems to access main system memory independently of the central processing unit (CPU).
- DMA can improve the performance and efficiency of data transfer between I/O devices and memory, as well as between different memory locations, by freeing the CPU from involvement with the data transfer.
- DMA can be used for "memory to memory" copying or moving data in memory, or for "peripheral to memory" data transfer from an I/O device to memory or vice versa.
- DMA requires a hardware device called a DMA controller (DMAC) that can communicate with the CPU and the I/O devices, and can control the data transfer on the bus.
- The DMA controller can operate in different modes, such as single transfer mode, block transfer mode, demand transfer mode, or cascade mode, depending on the amount and type of data to be transferred.
- The DMA controller can also support different types of DMA, such as single-channel DMA, multi-channel DMA, or bus mastering DMA, depending on the number and capability of the devices involved in the data transfer.
- The DMA controller can initiate a DMA transfer by sending a DMA request signal to the CPU, which can grant the request by sending a DMA acknowledge signal to the DMA controller.
- The DMA controller can then take control of the bus and transfer the data between the source and the destination, either directly or through an intermediate buffer.
- The DMA controller can notify the CPU of the completion of the data transfer by sending an interrupt signal to the CPU, which can then resume its normal operation.
- The advantages of DMA are that it can reduce the CPU overhead, increase the data transfer rate, and allow parallel processing of data.
- The disadvantages of DMA are that it can increase the hardware complexity, cause bus contention, and introduce security risks.



# I/O Channels and Processors

- I/O channels are extensions of the DMA concept that have the ability to execute I/O instructions using special-purpose processors on I/O channels and complete control over I/O operations.
- The processor does not execute I/O instructions itself, but initiates I/O transfer by instructing the I/O channel to execute a program in memory.
- I/O channels can be classified into different types based on their functionality and speed, such as byte multiplexer, block multiplexer, selector, and priority .
- Byte multiplexer channels are used for low-speed devices and transmit or accept characters, interleaving bytes from several devices.
- Block multiplexer channels are used for high-speed devices and transmit or accept blocks of characters, interleaving blocks of bytes from several devices.
- Selector channels are used for very high-speed devices and can transfer data to or from one device at a time, without interleaving.
- Priority channels are similar to selector channels, but can assign different priorities to different devices and handle them accordingly.
- I/O processors are simple, but contain sufficient memory to handle all I/O tasks.
- I/O processors are also called I/O controllers, I/O synchronizers, or DMA controllers.
- I/O processors can fetch and execute their own instructions, communicate with the CPU using interrupts, and support one or more controllers or devices .
- I/O processors are more equipped with facilities than those available in typical DMA controllers, such as buffering, error detection, and formatting.



# Serial Communication

Serial communication is the process of sequentially transferring the information/bits on the same channel. Due to this, the cost of wire will be reduced, but it slows the transmission speed. Serial communication is used for all long-haul communication and most computer networks, where the cost of cable and synchronization difficulties make parallel communication impractical.

Some of the main points to note about serial communication are:

- Serial communication can either be asynchronous or synchronous. Asynchronous communication does not require a common clock signal between the sender and the receiver, but it uses start and stop bits to indicate the beginning and the end of a data frame. Synchronous communication requires a common clock signal between the sender and the receiver, and it does not use start and stop bits, but it may use other synchronization methods .
- Serial communication can use different methods to encode the data in the form of serial digital binary. Some of the well-known interfaces used for the data exchange are RS-232, RS-485, I2C, SPI, etc. These interfaces differ in the number of wires, the voltage levels, the data rates, the error detection and correction mechanisms, and the protocols they follow.
- Serial communication can also be classified into simplex, half-duplex, and full-duplex modes. Simplex mode allows data transmission in one direction only, such as from a keyboard to a computer. Half-duplex mode allows data transmission in both directions, but not at the same time, such as in a walkie-talkie. Full-duplex mode allows data transmission in both directions simultaneously, such as in a telephone.
- A data communication processor is an I/O processor that distributes and collects data from numerous remote terminals connected through telephone and other communication lines to the computer. It is a specialized I/O processor designed to communicate with data communication networks.



# Synchronous and Asynchronous Communication

- Synchronous communication is a type of communication where the sender and the receiver exchange messages in real time, without any delay. Examples of synchronous communication are phone calls, video calls, face-to-face meetings, and live chats.
- Asynchronous communication is a type of communication where the sender and the receiver do not need to be available at the same time to communicate. The messages are sent and received at different times, with some delay. Examples of asynchronous communication are emails, text messages, voice messages, and online forums.
- The main advantages of synchronous communication are:
  - It allows for immediate feedback and clarification of messages.
  - It fosters a sense of connection and collaboration among the participants.
  - It can convey emotions and tone more effectively than written communication.
- The main disadvantages of synchronous communication are:
  - It can be disruptive and distracting for the participants, especially if they have other tasks to do.
  - It can be difficult to schedule and coordinate across different time zones and availability.
  - It can be affected by technical issues such as poor network connection, background noise, and low-quality audio or video.
- The main advantages of asynchronous communication are:
  - It allows for more flexibility and convenience for the participants, who can communicate at their own pace and time.
  - It enables more thoughtful and detailed responses, as the participants have more time to process and compose their messages.
  - It reduces the risk of spreading failures across services, as the messages are independent and do not rely on the availability of the receiver.
- The main disadvantages of asynchronous communication are:
  - It can cause delays and misunderstandings, as the messages may not be received or interpreted in a timely manner.
  - It can reduce the sense of engagement and rapport among the participants, as the messages may lack context and emotion.
  - It can compromise the data consistency and integrity, as the messages may be outdated or conflicting with each other.



# Standard Communication Interfaces

- A communication interface is a device or system that allows data to be exchanged between different components of a computer system or a network.
- A standard communication interface is a communication interface that follows a predefined set of rules or protocols to ensure compatibility and interoperability among different devices and systems.
- Some examples of standard communication interfaces are SCSI, USB, Ethernet, Bluetooth, HDMI, etc.
- A standard communication interface can be classified into two types: parallel and serial.
  - A parallel communication interface transfers multiple bits of data simultaneously over multiple wires or channels.
  - A serial communication interface transfers one bit of data at a time over a single wire or channel.
- A standard communication interface can also be classified into two modes: synchronous and asynchronous .
  - A synchronous communication interface transfers data at a fixed rate and uses a common clock signal to synchronize the sender and the receiver .
  - An asynchronous communication interface transfers data at a variable rate and uses start and stop bits to indicate the beginning and the end of a data unit .
- A standard communication interface can also be classified into two levels: physical and logical.
  - A physical communication interface defines the electrical and mechanical characteristics of the connection, such as voltage levels, connectors, cables, etc.
  - A logical communication interface defines the format and meaning of the data, such as encoding, framing, error detection, etc.
- A standard communication interface can also be classified into two roles: master and slave.
  - A master communication interface initiates and controls the data transfer and can communicate with multiple slaves.
  - A slave communication interface responds to the requests from the master and can communicate with only one master.
- A standard communication interface can also be classified into two directions: input and output.
  - An input communication interface receives data from an external device and sends it to the CPU or the memory.
  - An output communication interface receives data from the CPU or the memory and sends it to an external device.
- A standard communication interface consists of the following components:
  - A data bus buffer that connects the communication interface to the data bus of the CPU or the memory and allows bidirectional data transfer.
  - A read/write control logic that controls the direction and timing of the data transfer and generates the necessary signals for the communication interface and the external device.
  - A port register that holds the data to be transferred or received by the communication interface.
  - A control and status register that stores the configuration and mode of the communication interface and indicates the status and errors of the data transfer.

