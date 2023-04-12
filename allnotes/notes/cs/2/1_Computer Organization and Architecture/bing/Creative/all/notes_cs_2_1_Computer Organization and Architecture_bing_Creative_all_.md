

## Unit 1 - Introduction

- This unit provides an overview of the course, its objectives, and its scope.
- The course is about artificial intelligence (AI), which is the study of how to create machines and software that can perform tasks that require human intelligence, such as reasoning, learning, planning, decision making, natural language processing, computer vision, and robotics.
- The course will cover the following topics:
  - The history and foundations of AI, including its goals, challenges, and ethical issues.
  - The methods and techniques of AI, such as search, knowledge representation, inference, logic, machine learning, neural networks, and deep learning.
  - The applications and domains of AI, such as natural language processing, computer vision, speech recognition, natural language generation, recommender systems, game playing, and autonomous agents.
- The course will also introduce some of the tools and frameworks that are used to develop and implement AI systems, such as Python, TensorFlow, PyTorch, and OpenAI.
- The course will require the students to have some background in mathematics, statistics, and programming, as well as a basic understanding of data structures and algorithms.
- The course will consist of lectures, readings, assignments, quizzes, and a final project. The students will be evaluated based on their performance on these components. The course will also encourage the students to participate in online discussions and peer feedback.



# Functional units of digital system and their interconnections

A digital system is a system that processes and stores data in binary form, using electronic devices such as transistors, logic gates, and memory cells. A digital system can perform various functions, such as arithmetic, logic, control, input, output, and communication. To perform these functions, a digital system consists of several functional units that are interconnected by buses. A bus is a set of wires or lines that carry data, address, or control signals between different components of the system. The main functional units of a digital system and their interconnections are:

- **Input unit**: This unit is responsible for taking the input from the user or an external device and converting it into binary code that can be processed by the system. The input unit consists of input devices, such as keyboards, mouse, scanners, microphones, etc. The input unit is connected to the central processing unit (CPU) by an input bus.
- **Central processing unit (CPU)**: This unit is the brain of the system, as it performs all the processing and computation tasks required by the system. The CPU consists of three subunits: the arithmetic and logic unit (ALU), the control unit (CU), and the registers. The ALU performs arithmetic and logic operations on the data, such as addition, subtraction, multiplication, division, and comparison. The CU controls the sequence and timing of the operations performed by the ALU and other units, by generating and sending control signals. The registers are small and fast memory units that store data and instructions temporarily during the execution of a program. The CPU is connected to the memory unit and the input/output unit by the system bus, which consists of three sub-buses: the data bus, the address bus, and the control bus. The data bus carries the data between the CPU and the memory or the input/output unit. The address bus carries the address of the memory location or the input/output device that is to be accessed by the CPU. The control bus carries the control signals that indicate the type and direction of the data transfer or the operation to be performed.
- **Memory unit**: This unit is responsible for storing data and instructions permanently or temporarily, depending on the type of memory. The memory unit consists of various types of memory devices, such as random access memory (RAM), read-only memory (ROM), cache memory, hard disk, flash memory, etc. The memory unit is connected to the CPU by the system bus, and it can be accessed by the CPU using the address and data buses. The memory unit can also be connected to the input/output unit by a memory bus, which allows direct data transfer between the memory and the input/output devices, without involving the CPU. This is called direct memory access (DMA).
- **Output unit**: This unit is responsible for displaying or sending the output of the system to the user or an external device. The output unit consists of output devices, such as monitors, printers, speakers, etc. The output unit is connected to the CPU by an output bus, and it can receive data from the CPU using the data bus. The output unit can also be connected to the memory unit by a memory bus, which allows direct data transfer between the memory and the output devices, without involving the CPU. This is also called direct memory access (DMA).

The following diagram shows the functional units of a digital system and their interconnections:

Functional units of a digital system and their interconnections

Source:



# Buses

- A bus is a set of electrical wires that connects major components (CPU, memory and I/O devices) of a computer system   .
- A bus allows data, address and control signals to be transmitted between different devices   .
- A bus can be classified into three functional groups: data bus, address bus and control bus   .
- Data bus: It carries the data between the CPU, memory and I/O devices. It is bidirectional, meaning that data can flow in both directions   .
- Address bus: It carries the address of the memory location or I/O device that the CPU wants to access. It is unidirectional, meaning that data can flow only from the CPU to the memory or I/O devices   .
- Control bus: It carries the control signals that indicate the type and direction of data transfer, such as read, write, interrupt, etc. It can be bidirectional or unidirectional, depending on the design of the system   .
- The width of a bus is the number of wires or bits that it can carry at a time. The wider the bus, the more data can be transferred in parallel   .
- The speed of a bus is the frequency at which it operates, measured in MHz or GHz. The higher the speed, the faster the data can be transferred   .
- The throughput of a bus is the amount of data that can be transferred per unit time, measured in bits per second or megabytes per second. It depends on both the width and the speed of the bus   .
- A system bus can have different architectures, such as single bus, multiple bus, crossbar switch, etc. The architecture affects the performance, cost and complexity of the system   .



# Bus Architecture

- A bus is a set of electrical wires that connects major components of a computer system, such as CPU, memory and I/O devices.
- A bus can be classified into three functional groups: data lines, address lines and control lines .
- Data lines are used to transfer data between components. The number of data lines determines the data transfer rate and the word size of the system.
- Address lines are used to specify the source or destination of data. The number of address lines determines the address space and the memory capacity of the system.
- Control lines are used to coordinate the activities of components and to signal the type and direction of data transfer. The control lines include read/write, memory request, interrupt request, etc.
- A bus can be designed in different ways, depending on the number of components, the speed of data transfer, and the cost of implementation.
- A common bus system is a simple and economical design, where all the components share a single bus. However, this design has low performance and high contention, as only one component can use the bus at a time.
- A multiple bus system is a more complex and expensive design, where different components have their own dedicated buses. This design has high performance and low contention, as multiple components can use the buses simultaneously.



# Types of Buses

A bus is a set of wires or lines that carry data, addresses, and control signals between different components of a computer system. Buses can be classified into different types based on their functions, locations, and architectures.

## System Bus

The system bus is the main bus that connects the CPU to the main memory and other components on the motherboard. It consists of three sub-buses: the address bus, the data bus, and the control bus .

- The address bus is a unidirectional bus that carries the memory or I/O address from the CPU to the memory or I/O device. The width of the address bus determines the maximum amount of memory that can be addressed by the CPU.
- The data bus is a bidirectional bus that transfers data between the CPU and the memory or I/O device. The width of the data bus determines the amount of data that can be transferred in one cycle.
- The control bus is a bidirectional bus that carries control signals from the CPU to the memory or I/O device, and vice versa. The control signals indicate the type, direction, and timing of the data transfer.

## Expansion Bus

The expansion bus is a secondary bus that connects the peripheral devices to the system bus through expansion slots on the motherboard. It allows the system to be expanded with additional devices, such as graphics cards, sound cards, network cards, etc. There are different types of expansion buses, such as ISA, EISA, MCA, VESA, PCI, PCI Express, etc., each with different specifications and performance.

- ISA (Industry Standard Architecture) is an old and slow expansion bus that was widely used in the 1980s and early 1990s. It has a 16-bit data bus and a 24-bit address bus, and operates at 8 MHz.
- EISA (Extended Industry Standard Architecture) is an extension of ISA that supports 32-bit data and address buses, and operates at 8.33 MHz. It is backward compatible with ISA devices.
- MCA (Micro Channel Architecture) is a proprietary expansion bus developed by IBM that supports 16-bit and 32-bit data and address buses, and operates at 10 MHz. It is not compatible with ISA or EISA devices.
- VESA (Video Electronics Standards Association) is an expansion bus designed for high-performance graphics cards. It has a 32-bit data bus and a 32-bit address bus, and operates at 33 MHz.
- PCI (Peripheral Component Interconnect) is a common and fast expansion bus that supports 32-bit and 64-bit data and address buses, and operates at 33 MHz or 66 MHz. It is compatible with ISA and EISA devices through a bridge.
- PCI Express (PCIe) is a newer and faster expansion bus that uses serial point-to-point connections instead of parallel shared buses. It supports multiple lanes of data transfer, each with a bandwidth of 250 MB/s or 500 MB/s, depending on the direction. It is backward compatible with PCI devices through a bridge.

## Other Types of Buses

There are also other types of buses that are used for specific purposes or applications, such as:

- USB (Universal Serial Bus) is a serial bus that connects external devices, such as keyboards, mice, printers, scanners, cameras, etc., to the computer. It supports hot plugging, plug and play, and power management. It has different versions, such as USB 1.1, USB 2.0, USB 3.0, etc., each with different speeds and features.
- FireWire (IEEE 1394) is a serial bus that connects high-speed devices, such as digital cameras, camcorders, external hard drives, etc., to the computer. It supports hot plugging, plug and play, and peer-to-peer communication. It has different versions, such as FireWire 400, FireWire 800, etc., each with different speeds and features.
- SCSI (Small Computer System Interface) is a parallel bus that connects high-performance devices, such as hard disks, CD-ROMs, scanners, etc., to the computer. It supports multiple devices on a single bus, and has different standards, such as SCSI-1, SCSI-2, SCSI-3, etc., each with different speeds and features.
- I2C (Inter-Integrated Circuit) is a serial bus that connects low-speed devices, such as sensors, EEPROMs, LCDs, etc., to the computer. It uses only two wires, one for data and one for clock,



# Bus Arbitration in Computer Organization

- Bus arbitration is the process by which the next device becomes the bus controller by transferring bus mastership to another bus   .
- A bus master is a device that initiates data transfers on the bus at any given time, such as a processor or a DMA controller  .
- Bus arbitration is necessary to avoid conflicts and ensure proper communication among multiple bus masters that may want to access the bus simultaneously .
- There are two types of bus arbitration: centralized and distributed   .
- In centralized arbitration, there is a single bus arbiter that performs the required arbitration and grants the bus access to one of the requesting devices. The bus arbiter can be either a processor or a separate hardware unit   .
- In distributed arbitration, there is no central arbiter, but each device has its own arbitration logic and communicates with other devices to decide the bus access. This can be done using daisy chaining or independent request lines   .
- Centralized arbitration is simpler and faster, but it creates a single point of failure and a bottleneck for the bus access. Distributed arbitration is more reliable and scalable, but it requires more hardware and communication overhead .



# Register for the notes of the Unit 1 - Introduction in the subject of Computer Organization and Architecture

To register for the notes of the Unit 1 - Introduction in the subject of Computer Organization and Architecture, please follow these steps:

- Visit the official website of the course provider and log in with your credentials.
- Navigate to the course page of Computer Organization and Architecture and click on the Unit 1 - Introduction link.
- You will see a list of topics covered in the unit, such as basic concepts, performance measures, instruction set architecture, etc.
- Click on the Register button at the top of the page to enroll in the unit and access the notes.
- You will receive a confirmation email with a link to download the notes in PDF format.
- You can also view the notes online or print them for your convenience.
- You can also access the notes from the course dashboard or the unit page at any time.
- You can also register for the notes of other units in the same way.



# Bus

- A bus is a communication system that transfers data between components inside a computer, or between computers.
- A bus consists of a set of electrical wires that can carry one bit of data each.
- A bus can be classified into three types: data bus, address bus, and control bus .
- Data bus: It carries the data between the CPU, memory, and I/O devices. It is bidirectional, meaning that data can flow in both directions. The width of the data bus determines how many bits of data can be transferred at a time .
- Address bus: It carries the address of the memory location or I/O device that the CPU wants to access. It is unidirectional, meaning that data can flow only from the CPU to the memory or I/O devices. The width of the address bus determines how many memory locations or I/O devices can be addressed by the CPU .
- Control bus: It carries the control signals that synchronize the operations of the CPU, memory, and I/O devices. It can be bidirectional or unidirectional, depending on the design of the system. The control signals include read, write, interrupt, reset, etc .
- A common bus system is a system where all the components of the computer share the same bus. This reduces the cost and complexity of the system, but also limits the performance and scalability of the system.
- A common bus system can be further divided into two types: single-bus system and multiple-bus system.
- Single-bus system: It is a system where there is only one bus for data, address, and control. This simplifies the design of the system, but also increases the contention and congestion on the bus. The speed of the system depends on the speed of the slowest component on the bus.
- Multiple-bus system: It is a system where there are separate buses for data, address, and control. This improves the performance and reliability of the system, but also increases the cost and complexity of the system. The speed of the system depends on the speed of the fastest component on the bus.



# Memory Transfer

Memory transfer is the process of moving data between different types of storage devices in a computer system. Memory transfer can be performed for various purposes, such as fetching instructions, reading or writing data, or implementing virtual memory.

## Types of Memory Transfer

There are two main types of memory transfer operations:

- **Read operation**: The transfer of data from a memory word to the external environment, such as a register or a bus. The read operation is represented as the transfer of data from the address register (AR) with the selected word M for the memory into the memory buffer register (MBR). [AR]M MBR=Read Operation
- **Write operation**: The transfer of data from the external environment to a memory word. The write operation is represented as the transfer of data from the memory buffer register (MBR) to the address register (AR) with the chosen word M for the memory. MBR M [AR] =Write Operation

The control signals of the read and write operations initiate the memory transfer operations.

## Memory Transfer Cycle

A memory transfer cycle is the sequence of steps that are required to perform a memory transfer operation. A memory transfer cycle consists of the following phases:

- **Address phase**: The CPU sends the address of the memory word to be accessed to the memory unit through the address bus. The CPU also sends the control signal to indicate whether the operation is a read or a write.
- **Data phase**: Depending on the type of operation, the data is transferred between the memory unit and the CPU through the data bus. For a read operation, the data is transferred from the memory word to the CPU. For a write operation, the data is transferred from the CPU to the memory word.
- **Termination phase**: The CPU and the memory unit signal the completion of the memory transfer operation and release the buses.

## Memory Transfer and Virtual Memory

Virtual memory is a technique that allows the computer to use secondary storage devices, such as hard disks or solid-state drives, as an extension of the main memory, such as RAM. Virtual memory enables the computer to run larger programs or multiple programs simultaneously by swapping the data between the main memory and the secondary storage.

Memory transfer is an essential part of implementing virtual memory. The operating system divides the virtual memory space into fixed-size units called pages. The pages are mapped to the physical memory space in units called frames. The operating system maintains a data structure called the page table that records the mapping between the pages and the frames.

When a program accesses a memory address, the operating system checks the page table to see if the corresponding page is present in the main memory. If the page is present, the operating system performs a memory transfer operation to read or write the data from or to the main memory. If the page is not present, the operating system performs a page fault handling routine, which involves the following steps:

- The operating system selects a frame in the main memory to replace with the required page. The operating system may use some replacement algorithm, such as least recently used (LRU) or first in first out (FIFO), to choose the frame.
- The operating system performs a memory transfer operation to write the data from the selected frame to the secondary storage device. The operating system updates the page table to mark the frame as free.
- The operating system performs a memory transfer operation to read the data from the required page in the secondary storage device to the free frame in the main memory. The operating system updates the page table to mark the frame as occupied and record the mapping between the page and the frame.
- The operating system resumes the program execution and performs the memory transfer operation to read or write the data from or to the main memory.

## References

: https://www.tutorialspoint.com/what-is-memory-transfer-in-computer-architecture
: https://www.indeed.com/career-advice/career-development/virtual-memory
: https://www.geeksforgeeks.org/memory-organisation-in-computer-architecture/
: https://www.javatpoint.com/coa-bus-and-memory-transfers



# Processor Organization

- Processor organization is the study of how the components of a processor are designed and interconnected to perform various tasks.
- Processor organization is a part of computer organization and architecture, which deals with the design and implementation of computer systems at various levels of abstraction.
- Processor organization affects the performance, cost, and complexity of a computer system.

## Components of a Processor

- A processor consists of the following major components:

  - Arithmetic Logic Unit (ALU): The ALU performs arithmetic and logical operations on data.
  - Control Unit (CU): The CU controls the execution of instructions by fetching, decoding, and issuing them to the ALU and other components.
  - Registers: Registers are small, fast memory units that store data and instructions temporarily.
  - Buses: Buses are wires that transfer data and signals between the processor and other components.

## Processor Design

- Processor design involves choosing the following aspects of a processor:

  - Instruction Set: The instruction set is the set of operations that the processor can perform. It defines the format, operands, and addressing modes of instructions.
  - Data Path: The data path is the circuitry that connects the ALU, registers, and buses. It determines how data flows within the processor and how it interacts with external components.
  - Control Unit: The control unit is the circuitry that generates the control signals that coordinate the activities of the data path and other components. It can be implemented using hardwired logic or microprogramming.
  - Performance: The performance of a processor is measured by the speed and efficiency of executing instructions. It depends on factors such as clock rate, instruction cycle, pipeline, cache, and parallelism.



# General Registers Organization

- General registers organization is a type of CPU organization that uses multiple general-purpose registers instead of a single accumulator register.
- General-purpose registers can store operands, intermediate results, addresses, or any other data that is needed for the execution of instructions.
- General registers organization can have two or three address fields in the instruction format, depending on the number of operands required for each operation.
- General registers organization can be further classified into two types: register-memory reference architecture and register-register reference architecture.

## Register-memory reference architecture

- In this architecture, source 1 is always required in the register, source 2 can be present either in the register or in memory, and the destination can be either in the register or in memory.
- This architecture has the advantage of allowing direct access to memory operands without loading them into registers first, which reduces the number of instructions and memory cycles.
- However, this architecture also has some disadvantages, such as the need for a large instruction word to specify the address modes and the register numbers, and the limited number of registers available for fast data manipulation.

## Register-register reference architecture

- In this architecture, all the operands and the destination are required to be in the registers, and memory access is only allowed through load and store instructions.
- This architecture has the advantage of having a smaller instruction word, which reduces the instruction fetch time and the memory bandwidth requirement.
- Moreover, this architecture allows more registers to be used for data processing, which increases the performance and the flexibility of the instruction set.
- However, this architecture also has some disadvantages, such as the need for more instructions and memory cycles to load and store operands from and to memory, and the increased complexity of the register file and the register addressing logic.

: https://www.geeksforgeeks.org/introduction-of-general-register-based-cpu-organization/
: https://www.geeksforgeeks.org/different-classes-of-cpu-registers/



# Stack Organization

- A stack is a data structure that stores information in a last-in, first-out (LIFO) order.
- A stack is implemented as a logical part of the main memory or as a set of registers in the CPU.
- A stack pointer (SP) register is used to store the address of the topmost element of the stack.
- A stack can be used for various purposes in computer architecture, such as:
  - Evaluating arithmetic expressions in postfix notation.
  - Implementing subroutine calls and returns.
  - Passing parameters and local variables in procedures.
  - Supporting recursion and dynamic memory allocation.
  - Implementing exception handling and interrupt mechanisms.
- A stack-based CPU organization is one that uses a stack as the primary data structure for operand storage and manipulation.
- A stack-based CPU organization has the following advantages:
  - It simplifies the instruction set and the instruction format, as most instructions do not need to specify the operands explicitly, but implicitly refer to the top of the stack.
  - It reduces the number of registers and the register file size, as only one register (SP) is needed to access the stack.
  - It facilitates the compiler design and code generation, as the stack can be used to implement high-level language constructs easily.
- A stack-based CPU organization has the following disadvantages:
  - It increases the memory access and the memory bandwidth requirements, as most operations involve pushing and popping data from the stack.
  - It limits the parallelism and the pipelining potential, as the stack operations are sequential and dependent on the previous ones.
  - It reduces the flexibility and the performance optimization, as the stack order may not match the optimal order of execution.



# Addressing Modes

- Addressing modes are the different ways of specifying the location of an operand in an instruction .
- The operand can be a data value, a memory address, or a register.
- The choice of addressing mode affects the instruction format, the instruction size, the instruction execution time, and the memory access time.
- Different types of addressing modes are:

  - **Implied / Implicit Addressing Mode**: The operand is specified in the instruction itself or implied by the instruction opcode  . For example, `CLC` (clear carry flag) instruction does not need any operand.
  - **Immediate Addressing Mode**: The operand is a constant value that is given in the instruction itself   . For example, `MOV AX, 10` (move 10 to AX register) instruction has an immediate operand of 10.
  - **Direct Addressing Mode**: The operand is a memory address that is given in the instruction itself   . For example, `MOV AX, [1000]` (move the content of memory location 1000 to AX register) instruction has a direct operand of 1000.
  - **Register Addressing Mode**: The operand is a register that is specified in the instruction itself or implied by the instruction opcode   . For example, `MOV AX, BX` (move the content of BX register to AX register) instruction has two register operands of AX and BX.
  - **Register Indirect Addressing Mode**: The operand is a memory address that is stored in a register   . For example, `MOV AX, [BX]` (move the content of memory location pointed by BX register to AX register) instruction has a register indirect operand of BX.
  - **Displacement Addressing Mode**: The operand is a memory address that is calculated by adding a displacement value to a base address   . For example, `MOV AX, [BX+10]` (move the content of memory location pointed by BX register plus 10 to AX register) instruction has a displacement operand of BX+10.
  - **Relative Addressing Mode**: The operand is a memory address that is calculated by adding a displacement value to the current program counter  . For example, `JMP 20` (jump to the instruction 20 bytes ahead of the current instruction) instruction has a relative operand of 20.
  - **Indexed Addressing Mode**: The operand is a memory address that is calculated by adding an index value to a base address  . For example, `MOV AX, [1000+SI]` (move the content of memory location 1000 plus the content of SI register to AX register) instruction has an indexed operand of 1000+SI.
  - **Base Register Addressing Mode**: The operand is a memory address that is calculated by adding a displacement value to a base address that is stored in a register  . For example, `MOV AX, [BP+10]` (move the content of memory location pointed by BP register plus 10 to AX register) instruction has a base register operand of BP+10.
  - **Stack Addressing Mode**: The operand is a memory address that is at the top of the stack  . For example, `POP AX` (pop the top of the stack to AX register) instruction has a stack operand of the top of the stack.



## Unit 2 - Arithmetic and logic unit

- An arithmetic and logic unit (ALU) is a digital circuit that performs arithmetic and logical operations on binary data.
- The ALU is one of the core components of the central processing unit (CPU) of a computer system.
- The ALU can perform basic operations such as addition, subtraction, multiplication, division, and bitwise operations such as AND, OR, XOR, NOT, and shift.
- The ALU can also perform comparison operations such as equal, less than, and greater than, and generate flags or status bits based on the result of the operation.
- The ALU receives two input operands (A and B) and a set of control signals from the control unit (CU) of the CPU.
- The control signals determine which operation the ALU will perform on the input operands and how the output will be stored or transferred to other components of the CPU.
- The ALU has an output register (R) that stores the result of the operation and a flag register (F) that stores the status bits.
- The ALU can also have additional registers such as an accumulator (ACC) that stores the intermediate results of a sequence of operations, and a carry register (C) that stores the carry or borrow bit of an arithmetic operation.
- The ALU can be designed using combinational logic circuits such as adders, subtractors, multipliers, dividers, and multiplexers, or using sequential logic circuits such as registers, counters, and shift registers.
- The ALU can be implemented using various technologies such as transistors, integrated circuits, microprocessors, or field-programmable gate arrays (FPGAs).
- The ALU can be classified into different types based on the number of input operands, the number of output registers, the number of operations, and the complexity of the operations.
- Some examples of ALU types are:

  - Single-operand ALU: An ALU that performs operations on one input operand and one output register, such as increment, decrement, complement, and rotate.
  - Two-operand ALU: An ALU that performs operations on two input operands and one output register, such as addition, subtraction, and bitwise operations.
  - Three-operand ALU: An ALU that performs operations on three input operands and one output register, such as multiply-accumulate, fused multiply-add, and ternary logic operations.
  - Multi-operand ALU: An ALU that performs operations on more than three input operands and one output register, such as vector operations, matrix operations, and polynomial operations.
  - Single-output ALU: An ALU that has one output register that stores the result of the operation, such as R = A + B.
  - Multi-output ALU: An ALU that has more than one output register that store different parts of the result of the operation, such as R = A + B, C = A - B, and F = A < B.
  - Fixed-function ALU: An ALU that performs a fixed set of operations that are predefined and hardwired, such as addition, subtraction, and comparison.
  - Programmable ALU: An ALU that performs a variable set of operations that are selected by the control signals, such as arithmetic, logical, and shift operations.
  - Simple ALU: An ALU that performs basic and low-complexity operations, such as addition, subtraction, and bitwise operations.
  - Complex ALU: An ALU that performs advanced and high-complexity operations, such as multiplication, division, and floating-point operations.



# Look ahead carries adders

- A look ahead carry adder is a type of adder that reduces the propagation delay by using more complex hardware.
- Propagation delay is the time taken for the carry to propagate from one stage to the next in a ripple carry adder.
- A look ahead carry adder divides the adder into blocks and provides circuitry to quickly determine the carry out of a block as soon as the carry in is known.
- A look ahead carry adder uses the concepts of carry generate and carry propagate to calculate the carry out of a block.
- Carry generate (Cg) occurs when an output carry is generated internally by the full adder, regardless of the carry in. Cg = A.B
- Carry propagate (Cp) occurs when an output carry is propagated from the carry in, regardless of the input bits. Cp = A ⊕ B
- The carry out of a block can be expressed as a function of Cg, Cp and the carry in (Cin). Cout = Cg + Cp.Cin
- A look ahead carry adder can be implemented using a carry look ahead generator (CLG) and a group of full adders.
- A CLG takes the Cg and Cp signals from each full adder and generates the carry out signals for each block using logic gates.
- A full adder takes the input bits (A and B) and the carry in (Cin) and generates the sum bit (S) and the carry out (Cout) using logic gates.
- The sum bit can be expressed as a function of A, B and Cin. S = A ⊕ B ⊕ Cin
- A look ahead carry adder can be designed for any number of bits by cascading the CLG and the full adders.
- A look ahead carry adder can improve the speed of addition by reducing the carry propagation delay, but it requires more hardware and power than a ripple carry adder.



# Multiplication

- Multiplication is a binary operation that takes two operands and produces a single result.
- Multiplication can be performed by repeated addition, shifting and adding, or using a multiplication algorithm.
- Multiplication can be done in different number systems, such as binary, decimal, hexadecimal, etc.
- Multiplication can be done on different types of operands, such as integers, fractions, fixed-point numbers, floating-point numbers, etc.
- Multiplication can be done using different hardware components, such as adders, shifters, multipliers, etc.
- Multiplication can be done using different methods, such as booth's algorithm, array multiplier, Wallace tree, etc.
- Multiplication can be done in parallel or serial, depending on the speed and complexity of the hardware.
- Multiplication can be done with or without overflow detection, depending on the size and range of the operands and the result.
- Multiplication can be done with or without rounding, depending on the accuracy and precision of the result.



# Signed operand multiplication

- Signed operand multiplication is the process of multiplying two binary numbers that have a sign bit, usually in 2's complement or signed-magnitude representation.
- The sign bit is the most significant bit of the binary number, and it indicates whether the number is positive (0) or negative (1).
- The sign bit can be extended to the left to represent larger numbers, or truncated to the right to represent smaller numbers, without changing the value of the number.
- The sign bit can also be used to determine the sign of the product of two signed operands, by using the following rule: the sign of the product is the exclusive OR of the signs of the operands.
- For example, if we multiply two 4-bit signed operands, -3 (1101) and 5 (0101), the sign of the product is 1 (negative), because 1 XOR 0 = 1.
- The magnitude of the product is obtained by multiplying the magnitudes of the operands, ignoring the sign bits, and then adjusting the result to fit the desired number of bits.
- There are different algorithms for multiplying signed operands, such as the shift-and-add algorithm, the Booth's algorithm, and the Wallace tree algorithm.
- The shift-and-add algorithm is a simple and general method that works for both unsigned and signed operands, by shifting the multiplier to the right and adding the multiplicand to the partial product if the multiplier bit is 1.
- The Booth's algorithm is an optimization of the shift-and-add algorithm that reduces the number of additions and subtractions by encoding the multiplier into groups of 0s and 1s, and then performing conditional operations based on the encoded bits.
- The Wallace tree algorithm is a parallel method that reduces the number of partial products by using a tree of carry-save adders, and then adding the final sum and carry bits using a fast adder.



# Booth's Algorithm

Booth's algorithm is a multiplication algorithm that multiplies two signed binary numbers in 2's complement notation. It was invented by Andrew Donald Booth in 1950 while doing research on crystallography at Birkbeck College in London.

The algorithm is based on the following observations:

- A string of 0's in the multiplier requires no addition but just shifting.
- A string of 1's in the multiplier from bit weight 2^k to 2^m can be treated as 2^(m+1) - 2^k.
- A 0-to-1 transition in the multiplier at bit weight 2^k can be treated as -2^k.

The algorithm works as follows:

- Let X and Y be the multiplicand and multiplier of N bits each, and A, S, and P be N+1 bit registers.
- Initialize A and S to 0, and P to Y appended with a 0 bit.
- Initialize S to 2's complement of X, i.e., -X.
- Repeat the following steps N times:
  - If the rightmost two bits of P are 00 or 11, do an arithmetic right shift of P by 1 bit.
  - If the rightmost two bits of P are 01, do P = P + A and then an arithmetic right shift of P by 1 bit.
  - If the rightmost two bits of P are 10, do P = P + S and then an arithmetic right shift of P by 1 bit.
- After N iterations, the product is in P.

The following example illustrates the algorithm for multiplying 3 and -4 in binary:

- X = 0011, Y = 1100
- A = 00000, S = 11101, P = 11000
- Step 1: P = 01100 (right shift)
- Step 2: P = 10001 (P + S, right shift)
- Step 3: P = 11000 (right shift)
- Step 4: P = 01100 (right shift)
- Final product: P = 01100, which is -12 in decimal.



# Array Multiplier

- An array multiplier is a digital combinational circuit used for multiplying two binary numbers by employing an array of full adders and half adders .
- This array is used for the nearly simultaneous addition of the various product terms involved.
- To form the various product terms, an array of AND gates is used before the Adder array.
- The array multiplier is based on the add shift algorithm, which states that the partial product is equal to the multiplicand multiplied by the multiplier bit.
- The main advantage of the array multiplier is its simple and regular design structure, which makes it easy to implement and scale.
- The main disadvantage of the array multiplier is its high propagation delay, which depends on the number of bits in the operands.
- The propagation delay can be calculated as follows:

  - Let n be the number of bits in the operands.
  - Let t<sub>AND</sub> be the delay of an AND gate.
  - Let t<sub>HA</sub> be the delay of a half adder.
  - Let t<sub>FA</sub> be the delay of a full adder.
  - Then, the propagation delay of the array multiplier is given by:

    - t<sub>delay</sub> = t<sub>AND</sub> + (n-1)t<sub>HA</sub> + (n-1)t<sub>FA</sub>

- The following diagram shows an example of a 4x4 array multiplier :

4x4 array multiplier

- The inputs are A<sub>3</sub>A<sub>2</sub>A<sub>1</sub>A<sub>0</sub> and B<sub>3</sub>B<sub>2</sub>B<sub>1</sub>B<sub>0</sub>, and the outputs are P<sub>7</sub>P<sub>6</sub>P<sub>5</sub>P<sub>4</sub>P<sub>3</sub>P<sub>2</sub>P<sub>1</sub>P<sub>0</sub>.
- The product terms are generated by ANDing each bit of the multiplicand with each bit of the multiplier.
- The product terms are then added by using half adders and full adders in a diagonal fashion.
- The carry outputs of the adders are connected to the next higher-order adder.
- The final product is obtained by concatenating the sum outputs of the adders.



# Division and logic operations

- Division and logic operations are some of the functions performed by the arithmetic logic unit (ALU) of a computer.
- The ALU is a part of the computer that executes arithmetic and logic operations on data, such as addition, subtraction, multiplication, division, and bitwise operations, such as OR, AND, NOT, XOR, etc.
- Division is the operation of finding the quotient and the remainder of two numbers, such as 12 / 4 = 3 (quotient) and 12 % 4 = 0 (remainder).
- Logic operations are the operations that manipulate the bits of a number, such as 1010 OR 0110 = 1110, 1010 AND 0110 = 0010, NOT 1010 = 0101, etc.
- Division and logic operations can be performed on different types of numbers, such as unsigned, signed, fixed-point, floating-point, etc.
- Division and logic operations can be implemented in different ways, such as using hardware circuits, software algorithms, or a combination of both.
- Some of the algorithms for division are:
  - Restoring division: a method that uses repeated shifts and additions to find the quotient and the remainder.
  - Non-restoring division: a method that uses repeated shifts and subtractions to find the quotient and the remainder.
  - Signed-magnitude division: a method that uses the sign of the operands to determine the sign of the result, and then performs unsigned division on the magnitudes of the operands.
  - Booth's algorithm: a method that uses a modified form of binary representation to reduce the number of shifts and subtractions.
- Some of the algorithms for logic operations are:
  - Bitwise operations: a method that performs logic operations on each pair of corresponding bits of the operands, such as 1010 OR 0110 = 1110.
  - Boolean algebra: a method that uses the rules of logic to simplify and manipulate logic expressions, such as A OR (B AND C) = (A OR B) AND (A OR C).
  - Karnaugh maps: a method that uses a graphical representation of logic expressions to minimize the number of terms and variables, such as A OR (B AND C) = A OR C.



# Floating point arithmetic operation

- A floating point (FP) number is a kind of fraction where the radix point is allowed to move.
- A floating point number consists of three parts: a sign bit, a significand, and an exponent.
- The sign bit indicates whether the number is positive or negative.
- The significand is the fractional part of the number, normalized to have a leading 1 in binary representation.
- The exponent is the power of two by which the significand is multiplied.
- The floating point representation can implement operations for high range values, such as scientific and engineering calculations.
- The IEEE 754 standard defines a binary floating point format, with different precisions: single (32-bit), double (64-bit), and extended (80-bit or more).
- The architecture details of the floating point format are left to the hardware manufacturers.
- The storage order of individual bytes in binary floating point numbers varies from architecture to architecture.
- The floating point arithmetic operations include addition, subtraction, multiplication, and division.
- The floating point arithmetic operations are done with algorithms similar to those used on sign magnitude integers, but with some additional steps.
- The additional steps include aligning the significands by shifting them according to the exponents, normalizing the result by adjusting the exponent and the significand, and handling special cases such as overflow, underflow, zero, infinity, and NaN (not a number).
- The floating point arithmetic operations are quite often included in the internal hardware, such as a floating point unit (FPU) or a coprocessor.
- If no hardware is available for the floating point arithmetic operations, the compiler can generate software routines to perform them, but this may be slower and less accurate.



# Arithmetic & Logic Unit Design

The arithmetic and logic unit (ALU) is the part of a central processing unit (CPU) that performs arithmetic and logic operations on the operands in computer instruction words. The ALU can be divided into two units: an arithmetic unit (AU) and a logic unit (LU).

The AU performs arithmetic operations such as addition, subtraction, multiplication and division. The LU performs logic operations such as AND, OR, NOT, XOR, etc. The ALU also performs data movement operations such as load and store.

The ALU design depends on the instruction set architecture (ISA) of the CPU, the number of bits, the data types, the performance requirements and the technology used. The ALU can be implemented using combinational logic circuits, sequential logic circuits, reversible logic circuits or quantum logic circuits .

Some of the common components of an ALU are:

- Adder: A circuit that performs binary addition of two operands. There are different types of adders, such as half adder, full adder, ripple-carry adder, carry-lookahead adder, etc.
- Subtractor: A circuit that performs binary subtraction of two operands. It can be implemented using an adder and a complementer.
- Multiplier: A circuit that performs binary multiplication of two operands. There are different types of multipliers, such as array multiplier, booth multiplier, Wallace tree multiplier, etc.
- Divider: A circuit that performs binary division of two operands. There are different types of dividers, such as restoring divider, non-restoring divider, SRT divider, etc.
- Shifter: A circuit that performs bit shifting of an operand. There are different types of shifters, such as logical shifter, arithmetic shifter, barrel shifter, etc.
- Comparator: A circuit that compares two operands and produces a result based on their equality, inequality, or magnitude.
- Logic gates: Basic circuits that perform logic operations on one or more bits. There are different types of logic gates, such as AND, OR, NOT, NAND, NOR, XOR, XNOR, etc.

The ALU design also involves setting the control inputs for each unit, generating the output and the status flags, and optimizing the parameters such as quantum cost, garbage outputs, constant inputs, area, number of cells and simulation time. The ALU design can be verified using simulation tools, testing methods and formal methods.



# IEEE Standard for Floating Point Numbers

- Floating point numbers are a way to represent real numbers in hardware, such as computers, using a fixed number of bits.
- IEEE 754 is the most widely used standard for floating point arithmetic, which specifies the formats, methods, and exception handling for binary and decimal floating point numbers  .
- IEEE 754 defines two precisions for binary floating point numbers: single precision and double precision .
  - Single precision numbers have 32 bits: 1 bit for the sign, 8 bits for the exponent, and 23 bits for the significand .
  - Double precision numbers have 64 bits: 1 bit for the sign, 11 bits for the exponent, and 52 bits for the significand .
- The sign bit indicates whether the number is positive or negative: 0 for positive, 1 for negative .
- The exponent bits represent the exponent of the number in base 2, using a biased representation .
  - The bias is 127 for single precision and 1023 for double precision .
  - The exponent value is obtained by subtracting the bias from the exponent bits .
  - For example, if the exponent bits are 10000001 for single precision, the exponent value is 10000001 - 127 = -126 .
- The significand bits represent the fraction part of the number, using a normalized representation .
  - The normalized representation assumes that there is an implied 1 to the left of the radix point .
  - For example, if the significand bits are 01000000000000000000000 for single precision, the significand value is 1.01 .
- The floating point number is obtained by multiplying the sign, the significand, and the base 2 raised to the exponent .
  - For example, if the sign bit is 1, the exponent bits are 10000001, and the significand bits are 01000000000000000000000 for single precision, the floating point number is -1 x 1.01 x 2^-126 .
- IEEE 754 also defines special values for some combinations of exponent and significand bits, such as zero, infinity, and NaN (not a number) .
  - Zero is represented by all zero bits in the exponent and significand .
  - Infinity is represented by all one bits in the exponent and all zero bits in the significand .
  - NaN is represented by all one bits in the exponent and any non-zero bits in the significand .
- IEEE 754 also specifies how to perform arithmetic operations on floating point numbers, such as addition, subtraction, multiplication, division, and square root .
  - The operations are performed by aligning the exponents, adding or subtracting the significands, normalizing the result, and rounding to the nearest representable value .
  - The operations may also generate exception conditions, such as overflow, underflow, inexact, invalid, and division by zero .
  - The standard defines default handling for these exceptions, such as returning a special value, signaling an error, or using a user-defined handler .



## Unit 3 - Control Unit

- The control unit (CU) is a component of the central processing unit (CPU) that directs the operation of the processor.
- The control unit generates control signals that enable the execution of instructions by the arithmetic logic unit (ALU), the memory, and the input/output devices.
- The control unit can be classified into two types: hardwired and microprogrammed.
- A hardwired control unit is implemented using logic gates and flip-flops. It is fast, but inflexible and difficult to modify.
- A microprogrammed control unit is implemented using a read-only memory (ROM) that stores a sequence of microinstructions. Each microinstruction specifies a set of control signals for one or more micro-operations. It is flexible and easy to modify, but slower than a hardwired control unit.
- The control unit performs the following steps to execute an instruction:
  - Fetch: The control unit fetches the instruction from the memory and stores it in the instruction register (IR).
  - Decode: The control unit decodes the instruction and determines the operation code (opcode) and the operands.
  - Execute: The control unit generates the appropriate control signals to perform the operation specified by the instruction. This may involve transferring data between registers, performing arithmetic or logical operations, accessing the memory, or interacting with the input/output devices.
  - Store: The control unit stores the result of the operation in the designated register or memory location. It also updates the program counter (PC) to point to the next instruction.



# Instruction types for the notes of the Unit 3 - Control Unit in the subject of Computer Organization and Architecture

- An instruction is a binary code that specifies an operation to be performed by the processor and the operands to be used in the operation.
- Instructions can be classified into different types based on their format, functionality, and complexity.
- Some common instruction types are:

  - **Register instructions**: These instructions use only registers as operands. They are fast and simple to execute, but they have limited address space and require more bits to encode the register numbers. Example: `ADD R1, R2, R3` (add the contents of registers R2 and R3 and store the result in register R1).
  - **Immediate instructions**: These instructions use a constant value as one of the operands. They are useful for initializing registers, performing arithmetic operations with small constants, and loading addresses. They have less bits for the opcode, but they have limited range and precision for the constant value. Example: `ADDI R1, R2, 5` (add 5 to the contents of register R2 and store the result in register R1).
  - **Memory instructions**: These instructions use memory locations as operands. They are necessary for accessing data that cannot fit in registers, such as arrays, strings, and structures. They have more bits for the opcode, but they have larger address space and can access any data type. Example: `LW R1, 100(R2)` (load the word from the memory address obtained by adding 100 to the contents of register R2 and store it in register R1).
  - **Branch instructions**: These instructions alter the normal sequential flow of execution by changing the value of the program counter (PC). They are used for implementing conditional and unconditional jumps, loops, and subroutines. They have less bits for the opcode, but they have limited range for the target address and require additional hardware for calculating the new PC value. Example: `BEQ R1, R2, L1` (branch to label L1 if the contents of registers R1 and R2 are equal).
  - **Control instructions**: These instructions affect the operation of the control unit or the processor. They are used for enabling or disabling interrupts, setting or clearing flags, changing the processor mode, and halting the execution. They have more bits for the opcode, but they have special functions and require more hardware for implementing them. Example: `HALT` (stop the execution of the program).



# Unit 3 - Control Unit

The control unit is a component of the central processing unit (CPU) that controls and directs the operations of the computer system. It generates the necessary control signals to execute the program instructions and to coordinate the activities of the other functional units of the CPU, such as the arithmetic logic unit (ALU) and the memory unit (MU).

The control unit can be designed using two methods:

- **Hardwired control unit**: The control signals are generated by using combinational logic circuits. The logic circuits are designed based on the instruction set architecture of the processor. The hardwired control unit is fast, but inflexible and difficult to modify.
- **Microprogrammed control unit**: The control signals are generated by using a sequence of microinstructions stored in a special memory called the control store. The microinstructions are executed by a microsequencer, which can be implemented using a finite state machine. The microprogrammed control unit is flexible and easy to modify, but slower than the hardwired control unit.

The control unit can be classified into two types based on the level of instruction execution:

- **Instruction-level control unit**: The control unit that generates the control signals for the execution of one instruction at a time. It is also called the main control unit or the global control unit. It is responsible for fetching, decoding, and executing the instructions from the memory.
- **Micro-operation-level control unit**: The control unit that generates the control signals for the execution of one micro-operation at a time. It is also called the local control unit or the detailed control unit. It is responsible for performing the micro-operations within an instruction, such as fetching operands, performing arithmetic or logic operations, and storing results.

The control unit can be further divided into two subunits based on the function:

- **Instruction register and decoder**: The subunit that holds the current instruction and decodes it into its opcode and operands. It also generates the signals to select the appropriate functional unit and register for the instruction execution.
- **Timing and control unit**: The subunit that generates the timing signals to synchronize the operations of the CPU and the control signals to activate the required components and data paths for the instruction execution. It also generates the signals to handle the interrupts and exceptions that may occur during the instruction execution.



# Instruction Cycles

- Instruction cycles are the steps that a CPU performs to execute a single instruction.
- Instruction cycles are the basic operation of the CPU and consist of three main phases: fetch, decode, and execute.
- The CPU repetitively performs instruction cycles to execute a program that is stored in the memory unit.
- The instruction cycle can be decomposed into a sequence of elementary micro-operations that are performed by the CPU components.
- The instruction cycle can be affected by the presence of indirect addressing, interrupts, and pipelining.

## Fetch Phase

- The fetch phase is the first phase of the instruction cycle, where the CPU fetches the next instruction from the memory unit.
- The fetch phase involves the following micro-operations:
  - The CPU copies the content of the program counter (PC) to the memory address register (MAR), which holds the address of the next instruction to be fetched.
  - The CPU sends a read signal to the memory unit, which reads the instruction from the address specified by the MAR and places it on the data bus.
  - The CPU copies the content of the data bus to the instruction register (IR), which holds the last instruction fetched.
  - The CPU increments the PC by one, so that it points to the next instruction in the program.

## Decode Phase

- The decode phase is the second phase of the instruction cycle, where the CPU decodes the instruction in the IR and determines the operation and the operands involved.
- The decode phase involves the following micro-operations:
  - The CPU examines the opcode (operation code) field of the instruction in the IR and identifies the type and format of the instruction.
  - The CPU extracts the operand field(s) of the instruction in the IR and determines the address and value of the operand(s).
  - The CPU may need to perform an indirect cycle if the instruction uses indirect addressing, which means that the operand field contains the address of another memory location that holds the actual operand.
  - The CPU may need to perform an interrupt cycle if an interrupt request is detected, which means that the CPU has to suspend the current instruction and execute a service routine for the interrupt.

## Execute Phase

- The execute phase is the third phase of the instruction cycle, where the CPU executes the instruction and performs the required operation on the operand(s).
- The execute phase involves the following micro-operations:
  - The CPU transfers the operand(s) from the memory unit or the registers to the arithmetic logic unit (ALU), which performs the arithmetic or logical operation specified by the opcode.
  - The CPU transfers the result of the operation from the ALU to the memory unit or the registers, depending on the instruction format.
  - The CPU may need to update the condition code register (CCR), which holds the status flags that indicate the outcome of the operation, such as zero, negative, overflow, or carry.
  - The CPU may need to update the PC or the stack pointer (SP) if the instruction is a branch or a call, which means that the CPU has to change the sequence of execution or store the return address on the stack.

## Pipelining

- Pipelining is a technique that improves the performance of the CPU by overlapping the execution of multiple instructions.
- Pipelining divides the instruction cycle into smaller stages, such as instruction fetch, instruction decode, operand fetch, execute, and result store.
- Pipelining allows the CPU to fetch the next instruction while decoding the current instruction, and execute the current instruction while fetching the operand(s) for the next instruction, and so on.
- Pipelining increases the throughput (the number of instructions executed per unit time) of the CPU, but it also introduces some challenges, such as data hazards, control hazards, and structural hazards.



# Sub Cycles for the Notes of the Unit 3 - Control Unit in the Subject of Computer Organization and Architecture

- The control unit is the part of the processor that coordinates the sequence of data movements into, out of, and between the processor's many sub-units.
- The control unit also interprets the instructions fetched from the memory and generates the appropriate control signals to execute them.
- The execution of an instruction involves the execution of a sequence of substeps, generally called cycles.
- For example, an instruction may consist of fetch, indirect, execute, and interrupt cycles.
- Each cycle is in turn made up of a sequence of more fundamental operations, called micro-operations.
- A micro-operation is a basic operation performed on the data stored in one or more registers, or on the data transferred between a register and an external bus.
- A micro-operation generally involves a transfer between registers, a transfer between a register and an external bus, or a simple ALU operation.
- The control unit generates the control signals that cause each micro-operation to be executed.
- The control signals also control the opening and closing of logic gates, resulting in the transfer of data to and from registers and the operation of the ALU.
- One technique for implementing a control unit is referred to as hardwired, which means that the control signals are generated by using combinational logic circuits.
- Another technique is to use a microprogrammed control unit, which means that the control signals are stored in a control memory and executed by a microprogram sequencer.
- The advantage of a microprogrammed control unit is that it is easier to modify and debug than a hardwired one.
- The disadvantage is that it may be slower and less efficient than a hardwired one.
- The sub cycles of an instruction cycle depend on the type and format of the instruction, as well as the addressing mode and the processor architecture .
- A typical instruction cycle may have the following sub cycles :
  - Fetch cycle: The control unit fetches the instruction from the memory and stores it in the instruction register. The program counter is incremented to point to the next instruction.
  - Decode cycle: The control unit decodes the instruction and determines the operation code, the operands, and the addressing mode. The control unit may also fetch the operands from the memory or the registers, depending on the addressing mode.
  - Execute cycle: The control unit executes the instruction by performing the specified operation on the operands. The result may be stored in a register or in the memory, depending on the instruction.
  - Interrupt cycle: The control unit checks for any interrupts that may have occurred during the execution of the instruction. If an interrupt is detected, the control unit saves the current state of the processor and transfers the control to the interrupt handler routine. After the interrupt is serviced, the control unit restores the state of the processor and resumes the execution of the instruction cycle.



# Fetch and Execute Cycle

- The fetch and execute cycle is the basic operation cycle of a computer (also known as the fetch decode execute cycle or FDX)  .
- It is the process by which a computer retrieves a program instruction from its memory, determines what actions the instruction requires, and carries out those actions .
- The fetch and execute cycle was first proposed by John von Neumann who is famous for the Von Neumann architecture, the framework which is being followed by most computers today .
- The fetch and execute cycle consists of several stages, which are:

  - **Fetch**: The CPU fetches the instruction from the memory address that is stored in the program counter (PC) and places it in the instruction register (IR). The PC is then incremented to point to the next instruction   .
  - **Decode**: The CPU decodes the instruction in the IR and determines the operation code (opcode) and the operands. The opcode specifies what operation to perform, and the operands specify the data or the memory locations involved in the operation   .
  - **Execute**: The CPU executes the instruction by performing the operation specified by the opcode using the operands. The result of the operation may be stored in a register, a memory location, or sent to an output device   .
- The fetch and execute cycle is repeated until the program is completed or an error occurs   .
- The fetch and execute cycle is the basic operation of a computer, but it can be modified or enhanced by using techniques such as pipelining, parallel processing, caching, and branch prediction to improve the performance and efficiency of the CPU .



# Micro-operations

- Micro-operations are the basic or atomic operations of a processor .
- They are used to implement complex machine instructions.
- They usually perform operations on data stored in one or more registers .
- They can be classified into four categories:
  - Register transfer micro-operations: They transfer data between registers or between registers and external buses of the CPU .
  - Arithmetic micro-operations: They perform arithmetic operations on numeric data stored in registers.
  - Logic micro-operations: They perform bit-wise logical operations on non-numeric data stored in registers.
  - Shift micro-operations: They perform serial transfer of data and support arithmetic, logic, and data-processing operations . They can shift the contents of a register to the left or the right.
- Micro-operations can be expressed using symbolic notation . For example:
  - R1 ← R2: This means transfer the contents of register R2 to register R1.
  - R3 ← R1 + R2: This means add the contents of registers R1 and R2 and store the result in register R3.
  - R4 ← R4 OR R5: This means perform bit-wise OR operation on the contents of registers R4 and R5 and store the result in register R4.
  - R6 ← shl R6: This means shift the contents of register R6 one bit position to the left.



# Execution of a Complete Instruction

- The execution of a complete instruction involves the following steps :
  - **Fetch**: The processor fetches the instruction from the memory using the address stored in the program counter (PC) register. The PC is then incremented by the size of the instruction.
  - **Decode**: The processor decodes the instruction opcode and operands and determines the type and format of the instruction. The processor also checks if the instruction is valid and supported by the architecture.
  - **Execute**: The processor executes the instruction by performing the required operation on the operands. The operation may involve arithmetic, logic, data transfer, control transfer, or I/O. The processor may also update the condition codes or flags based on the result of the operation.
  - **Store**: The processor stores the result of the operation in the destination operand, which may be a register or a memory location. The processor may also update the PC if the instruction is a branch or a jump.
- The execution of a complete instruction may take one or more clock cycles depending on the complexity and length of the instruction.
- The execution of a complete instruction may also involve the use of a datapath, which is a collection of functional units, registers, and buses that perform the operations required by the instruction.
- The execution of a complete instruction may also involve the use of a control unit, which is a circuit that generates the control signals that coordinate the activities of the datapath.
- The execution of a complete instruction may follow different instruction sequencing methods, such as straight-line sequencing, conditional branching, unconditional branching, subroutine call and return, or interrupt and exception handling .



# Program Control

Program control is the process of directing the execution of instructions in a computer program. Program control can be achieved by using different types of instructions, such as:

- **Arithmetic and logic instructions**: These instructions perform operations on data, such as addition, subtraction, multiplication, division, and, or, not, etc. These instructions can also affect the status flags, such as zero, carry, overflow, etc., which can be used for conditional branching.
- **Data transfer instructions**: These instructions move data between registers, memory, and input/output devices. These instructions can also load or store immediate values, addresses, or offsets.
- **Branching instructions**: These instructions alter the normal sequential flow of execution by changing the program counter (PC) to a different value. Branching instructions can be unconditional or conditional, depending on the status flags or the result of a comparison. Branching instructions can also be direct or indirect, depending on whether the target address is specified explicitly or stored in a register or memory location.
- **Subroutine instructions**: These instructions allow the program to call a subprogram or a function, which can perform a specific task and return to the caller. Subroutine instructions involve saving the return address (usually in a stack) and jumping to the subprogram entry point. The subprogram can also pass parameters and return values using registers, memory, or stack.
- **Interrupt instructions**: These instructions allow the program to request the attention of the operating system or the hardware, which can handle an exceptional event or a service request. Interrupt instructions involve saving the current state of the program (usually in a stack) and jumping to an interrupt handler, which can perform the required action and resume the program execution.

Program control can also be influenced by the design of the control unit, which is the part of the processor that generates the control signals for the execution of instructions. The control unit can be implemented in two ways:

- **Hardwired control**: In this method, the control unit is designed using combinational logic circuits, which generate the control signals based on the opcode and the current state of the processor. Hardwired control is faster and simpler, but less flexible and more difficult to modify.
- **Microprogrammed control**: In this method, the control unit is designed using a microprogram, which is a sequence of microinstructions stored in a special memory called the control store. Each microinstruction specifies the control signals for one or more micro-operations, which are the elementary operations performed by the processor. Microprogrammed control is slower and more complex, but more flexible and easier to modify.



# Reduced Instruction Set Computer

- A reduced instruction set computer (RISC) is a computer architecture that uses a small, highly optimized set of instructions, rather than the more specialized set often found in other types of architecture, such as in a complex instruction set computer (CISC) .
- RISC is designed to simplify the individual instructions given to the computer to accomplish tasks, and to make them execute very fast .
- RISC is the most efficient CPU architecture technology, and it is an evolution and alternative to CISC.
- RISC has the following characteristics :
  - Each instruction performs a single, well-defined operation, such as load, store, add, or branch.
  - Each instruction has a fixed length and format, which makes decoding and pipelining easier and faster.
  - Most instructions use the register-to-register (or load/store) model, where operands are either registers or memory locations, and results are stored in registers.
  - The number of registers is large, typically 32 or more, to reduce the need for accessing memory.
  - The instruction set is orthogonal, meaning that any instruction can use any register or addressing mode, without restrictions or penalties.
  - The addressing modes are simple and few, usually limited to immediate, displacement, and indexing.
  - The memory access is aligned, meaning that data must be stored and retrieved on natural boundaries (such as word or byte boundaries).
  - The control flow is based on conditional branch instructions, rather than on flags or condition codes.
- Some examples of RISC architectures are MIPS, ARM, SPARC, PowerPC, and RISC-V.



# Pipelining

Pipelining is a technique for improving the performance of a computer system by overlapping the execution of multiple instructions in different stages of a processor. Pipelining can be used for instruction processing or for any complex operation that can be divided into sub-operations.

## Basic Concepts of Pipelining

- A pipeline is a sequence of stages that process data or instructions in parallel. Each stage performs a specific function and passes the output to the next stage. The input and output of each stage are stored in registers called interface registers or pipeline registers.
- The number of stages in a pipeline is called the pipeline depth. The time required for a stage to complete its operation is called the stage delay. The time interval between the initiation of two successive instructions in a pipeline is called the pipeline cycle time or clock cycle.
- The performance of a pipeline is measured by its throughput, which is the number of instructions or operations completed per unit time. The ideal throughput of a pipeline is equal to the inverse of the pipeline cycle time. The speedup of a pipeline is the ratio of the throughput of a pipeline to the throughput of a single-stage processor.
- The efficiency of a pipeline is the ratio of the actual throughput to the ideal throughput. The efficiency of a pipeline depends on the balance of the stage delays, the frequency of hazards, and the degree of parallelism in the instruction stream.

## Types of Pipelining

- Instruction pipelining is a technique for processing multiple instructions in different stages of a processor. The stages of an instruction pipeline typically include fetch, decode, execute, memory access, and writeback. Instruction pipelining increases the instruction level parallelism (ILP) in a program by overlapping the execution of independent instructions.
- Data pipelining is a technique for processing multiple data elements in different stages of a processor. The stages of a data pipeline typically include load, operate, store, and repeat. Data pipelining increases the data level parallelism (DLP) in a program by overlapping the execution of independent data elements.
- Arithmetic pipelining is a technique for processing multiple arithmetic operations in different stages of a processor. The stages of an arithmetic pipeline typically include fetch operands, perform operation, normalize result, and round result. Arithmetic pipelining increases the arithmetic level parallelism (ALP) in a program by overlapping the execution of independent arithmetic operations.

## Advantages and Disadvantages of Pipelining

- The main advantage of pipelining is that it improves the performance of a computer system by increasing the throughput and reducing the latency of the processor. Pipelining also reduces the cost and power consumption of the processor by using simpler and smaller components for each stage.
- The main disadvantage of pipelining is that it introduces complexity and overhead in the design and implementation of the processor. Pipelining also increases the possibility of hazards, which are situations that prevent the smooth execution of instructions or operations in a pipeline. Hazards can be classified into three types: structural, data, and control hazards.
- Structural hazards occur when two or more instructions or operations require the same resource at the same time. For example, a structural hazard can occur when two instructions try to access the same memory unit or register file in the same cycle. Structural hazards can be resolved by increasing the number of resources, using buffers or queues, or stalling the pipeline.
- Data hazards occur when an instruction or operation depends on the result of a previous instruction or operation that has not yet completed. For example, a data hazard can occur when an instruction tries to read a register that is being written by a previous instruction in the pipeline. Data hazards can be resolved by using forwarding or bypassing, reordering or scheduling, or stalling the pipeline.
- Control hazards occur when the flow of instructions or operations is altered by a branch or a jump instruction. For example, a control hazard can occur when the target address of a branch or a jump instruction is not known until the execute stage of the pipeline. Control hazards can be resolved by using branch prediction, branch target buffering, or delaying the branch.



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



# Microprogram Sequencing

- Microprogram sequencing is the process of generating the addresses of the microinstructions stored in the control memory of a microprogrammed control unit .
- The microinstructions contain the control signals that determine the operation of the data path components of the CPU .
- The microprogram sequencer is the component that performs the microprogram sequencing. It can be designed with different techniques and features to suit the requirements of the CPU  .
- Some of the factors that affect the design of the microprogram sequencer are:
  - The size of the microinstruction: The number of bits needed to encode the control signals and the address fields.
  - The time of execution: The number of clock cycles needed to fetch and execute a microinstruction.
  - The branching capability: The ability to alter the normal sequential order of microinstructions based on some conditions or inputs.
  - The encoding scheme: The way of representing the control signals and the address fields in the microinstruction.
- Some of the common techniques for microprogram sequencing are:
  - Horizontal microprogramming: The microinstruction contains all the control signals in a single word, and the next microinstruction address is calculated by incrementing the current address or using a branch field.
  - Vertical microprogramming: The microinstruction contains a subset of the control signals in a compressed format, and the next microinstruction address is calculated by using a next-address field or a branch field.
  - Hybrid microprogramming: The microinstruction contains a combination of horizontal and vertical formats, and the next microinstruction address is calculated by using different methods depending on the format.
- Some of the common features for microprogram sequencing are:
  - Conditional branching: The ability to branch to a different microinstruction based on the outcome of a test or a flag.
  - Subroutine call and return: The ability to call a sequence of microinstructions stored in a different location and return to the original sequence after execution.
  - Looping and counting: The ability to repeat a sequence of microinstructions for a specified number of times or until a condition is met.
  - Interrupt handling: The ability to suspend the current microprogram and execute a different microprogram in response to an external signal or event.



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



## Unit 4 - Memory

Memory is the mental process of encoding, storing and retrieving information. Memory can be divided into three main types: sensory memory, short-term memory and long-term memory.

- Sensory memory is the brief and transient storage of sensory information, such as visual, auditory or tactile stimuli. Sensory memory lasts for a fraction of a second and has a large capacity, but is prone to decay and interference.
- Short-term memory is the active and conscious manipulation of information, such as rehearsing a phone number or solving a math problem. Short-term memory lasts for about 15 to 30 seconds and has a limited capacity, but can be extended by chunking or mnemonics.
- Long-term memory is the relatively permanent and stable storage of information, such as facts, skills or personal experiences. Long-term memory has a potentially unlimited capacity and duration, but is subject to forgetting and distortion.

Memory can also be classified into two main categories: declarative memory and procedural memory.

- Declarative memory is the memory of facts and events that can be consciously recalled and verbally expressed, such as the name of the capital of France or the date of your birthday. Declarative memory can be further divided into two subtypes: semantic memory and episodic memory.
  - Semantic memory is the memory of general knowledge and concepts that are independent of time and context, such as the meaning of words or the rules of grammar.
  - Episodic memory is the memory of personal experiences and events that are tied to a specific time and place, such as your first day of school or your last vacation.
- Procedural memory is the memory of skills and habits that can be performed automatically and unconsciously, such as riding a bike or playing a musical instrument. Procedural memory is often resistant to forgetting and difficult to verbalize.

Memory is influenced by many factors, such as attention, encoding, retrieval, interference, consolidation, forgetting and distortion.

- Attention is the selective focus on a stimulus or a task that enhances the encoding and retrieval of information. Attention can be divided into two types: selective attention and divided attention.
  - Selective attention is the ability to focus on one stimulus or task while ignoring irrelevant or distracting stimuli or tasks, such as listening to a lecture while ignoring background noise.
  - Divided attention is the ability to perform two or more stimuli or tasks simultaneously, such as talking on the phone while driving. Divided attention often reduces the quality and quantity of information that can be encoded and retrieved.
- Encoding is the process of transforming information into a form that can be stored in memory, such as visual, acoustic or semantic codes. Encoding can be enhanced by elaboration, organization, imagery and mnemonics.
  - Elaboration is the process of adding meaning and detail to information, such as relating it to prior knowledge or personal experience.
  - Organization is the process of grouping and categorizing information into meaningful units, such as hierarchies, schemas or networks.
  - Imagery is the process of creating mental pictures or visual representations of information, such as drawing a map or forming a mental image of a word.
  - Mnemonics are memory aids or techniques that facilitate the encoding and retrieval of information, such as acronyms, rhymes or the method of loci.
- Retrieval is the process of accessing and bringing information from memory into conscious awareness, such as recalling a fact or recognizing a face. Retrieval can be influenced by cues, context and mood.
  - Cues are stimuli or hints that help trigger the retrieval of information, such as the first letter of a word or the smell of a place.
  - Context is the physical or mental environment in which information was encoded or retrieved, such as the location or the state of mind. Context can facilitate the retrieval of information if it matches the encoding context, a phenomenon known as context-dependent memory.
  - Mood is the emotional state or feeling in which information was encoded or retrieved, such as happy or sad. Mood can facilitate the retrieval of information if it matches the encoding mood, a phenomenon known as mood-congruent memory.
- Interference is the process of losing or impairing the retrieval of information due to the presence of other information, such as similar or conflicting information. Interference can be divided into two types: retroactive interference and proactive interference.
  - Retroactive interference is the process of losing or impairing the retrieval of old information due to the encoding or retrieval of new information, such as forgetting your old phone number after learning a new one.
  - Proactive interference is the process of losing or impairing the retrieval of new information due to the encoding or retrieval of old information, such as calling your new partner by your ex's name.
- Consolidation is the process of strengthening and stabilizing



# Basic concept and hierarchy for the notes of the Unit 4 - Memory in the subject of Computer Organization and Architecture

- Memory is the component of a computer system that stores data and instructions for processing.
- Memory hierarchy is the arrangement of memory and storage devices in a computer system according to their speed, capacity, and cost.
- The purpose of memory hierarchy is to minimize the average access time of the entire memory system by exploiting the principle of locality of reference, which states that a program tends to access a small subset of its address space frequently and repeatedly.
- The memory hierarchy consists of several levels of memory, each with different characteristics and functions. The levels are:

  - **Register**: The fastest and smallest level of memory, located inside the CPU. It holds the data and instructions that are currently being executed by the CPU.
  - **Cache memory**: A small and fast level of memory, located close to the CPU. It acts as a buffer between the CPU and the main memory, and stores frequently accessed data and instructions.
  - **Main memory**: Also known as primary memory or random access memory (RAM), it is the largest and most commonly used level of memory. It holds the data and instructions that are currently needed by the CPU and the programs running on the computer.
  - **Secondary memory**: Also known as auxiliary memory or external memory, it is the slowest and cheapest level of memory. It provides permanent and large storage for data and instructions that are not currently needed by the CPU or the programs. Examples of secondary memory are hard disk, optical disk, flash memory, etc.

- The figure below shows a diagram of the memory hierarchy:

Memory hierarchy diagram

- The memory hierarchy design is based on the following trade-offs:

  - **Speed**: The higher the level of memory, the faster it is, but also the smaller and more expensive it is.
  - **Capacity**: The lower the level of memory, the larger and cheaper it is, but also the slower it is.
  - **Locality**: The higher the level of memory, the more likely it is to contain the data and instructions that are needed by the CPU, but also the more complex and costly it is to manage.

- The memory hierarchy works by using the following techniques:

  - **Temporal locality**: If a data or instruction is accessed once, it is likely to be accessed again soon. Therefore, it is copied from a lower level of memory to a higher level of memory, where it can be accessed faster.
  - **Spatial locality**: If a data or instruction is accessed once, it is likely that the nearby data or instructions will be accessed soon. Therefore, a block or a group of data or instructions is copied from a lower level of memory to a higher level of memory, where it can be accessed faster.
  - **Mapping**: A mechanism that determines how a data or instruction is located and transferred between different levels of memory. There are different types of mapping, such as direct, associative, or set-associative.
  - **Replacement**: A policy that decides which data or instruction to remove from a higher level of memory when it is full and a new data or instruction needs to be copied from a lower level of memory. There are different types of replacement, such as least recently used (LRU), first in first out (FIFO), or random.
  - **Write**: A strategy that determines how a data or instruction is updated in different levels of memory when it is modified by the CPU. There are different types of write, such as write-through, write-back, or write-allocate.



# Semiconductor RAM Memories

Semiconductor RAM memories are a type of volatile memory that store data in integrated circuits using metal-oxide-semiconductor (MOS) transistors. They allow random access to data, meaning that any location can be read or written in any order. They are used for temporary storage of data and instructions in computers and other devices.

Some of the main characteristics of semiconductor RAM memories are:

- They have fast access time, ranging from 10 ns to 100 ns.
- They have high density, meaning that they can store a large amount of data in a small area.
- They have low power consumption, compared to other types of memory.
- They have high cost per bit, meaning that they are more expensive than other types of memory.
- They have limited lifetime, meaning that they can lose data over time or due to external factors.

There are two basic types of semiconductor RAM memories: static RAM (SRAM) and dynamic RAM (DRAM).

## Static RAM (SRAM)

Static RAM (SRAM) is a type of semiconductor RAM memory that uses bistable latches to store each bit of data. A bistable latch is a circuit that can hold one of two states (0 or 1) and does not need to be refreshed to maintain its state. SRAM is faster and more reliable than DRAM, but it is also more complex and consumes more power.

Some of the main features of SRAM are:

- It has access time of 10 ns to 30 ns.
- It has low density, meaning that it can store a small amount of data in a large area.
- It has high power consumption, compared to DRAM.
- It has high cost per bit, meaning that it is very expensive.
- It has unlimited lifetime, meaning that it does not lose data unless the power is turned off.

SRAM is used for cache memory, registers, and other applications that require high speed and low latency.

## Dynamic RAM (DRAM)

Dynamic RAM (DRAM) is a type of semiconductor RAM memory that uses capacitors to store each bit of data. A capacitor is a device that can store electric charge and can be charged or discharged by applying a voltage. DRAM is slower and less reliable than SRAM, but it is also simpler and consumes less power.

Some of the main features of DRAM are:

- It has access time of 50 ns to 100 ns.
- It has high density, meaning that it can store a large amount of data in a small area.
- It has low power consumption, compared to SRAM.
- It has low cost per bit, meaning that it is relatively cheap.
- It has limited lifetime, meaning that it can lose data over time or due to external factors.

DRAM is used for main memory, video memory, and other applications that require large capacity and low cost.

DRAM requires periodic refreshing to maintain its data, meaning that the capacitors need to be recharged by applying a voltage. The refreshing process reduces the effective access time and bandwidth of DRAM. To overcome this limitation, various types of DRAM have been developed, such as:

- Synchronous DRAM (SDRAM): DRAM that operates in sync with the system clock, allowing faster and more efficient data transfer.
- Double Data Rate SDRAM (DDR SDRAM): SDRAM that transfers data on both the rising and falling edges of the clock signal, doubling the data rate.
- Rambus DRAM (RDRAM): DRAM that uses a high-speed serial bus to communicate with the memory controller, allowing higher bandwidth and lower latency.
- Graphics DRAM (GDRAM): DRAM that is optimized for graphics applications, such as 3D rendering and video processing.
- Magnetoresistive RAM (MRAM): DRAM that uses magnetic elements to store data, allowing non-volatility and high speed.



# 2D & 2 1/2D memory organization

- 2D memory organization is a way of arranging memory cells in a matrix of rows and columns, where each row contains a word of data  .
- A word is a fixed-sized unit of data that can be transferred or processed by the computer system.
- A decoder is a combinational circuit that converts a binary code into a corresponding output signal.
- A decoder is used to select a row of the memory matrix by decoding the row address bits  .
- A multiplexer is a combinational circuit that selects one of the inputs and forwards it to the output.
- A multiplexer is used to select a column of the memory matrix by multiplexing the column address bits  .
- The selected memory cell is accessed by the intersection of the row and column lines  .
- The advantages of 2D memory organization are:
  - It reduces the number of address lines and pins required for the memory chip  .
  - It allows for higher memory density and capacity  .
- The disadvantages of 2D memory organization are:
  - It increases the complexity and cost of the decoder and multiplexer circuits  .
  - It increases the access time and power consumption of the memory chip  .
  - It does not allow for error correction or detection.

- 2 1/2D memory organization is a modification of 2D memory organization that adds an extra dimension of memory banks  .
- A memory bank is a group of memory cells that share the same row and column address lines, but have separate data and control lines  .
- A bank selector is a circuit that selects one of the memory banks based on the bank address bits  .
- The advantages of 2 1/2D memory organization are:
  - It allows for parallel access to multiple memory banks, which increases the bandwidth and performance of the memory system  .
  - It allows for error correction or detection by using redundant memory banks or parity bits .
- The disadvantages of 2 1/2D memory organization are:
  - It increases the number of data and control lines and pins required for the memory chip  .
  - It increases the complexity and cost of the bank selector circuit  .

- A schematic diagram of 2D and 2 1/2D memory organization is shown below:

2D and 2 1/2D memory organization

: https://citizenchoice.in/course/Lx7dMUDDQFIZ4LQuX1mJ/Chapter%204/2D-2.5-D-Memory-Organization
: https://www.studocu.com/in/document/dr-apj-abdul-kalam-technical-university/computer-organization-architecture/2d-and-2-2d-and-25-d/39625128
: https://www.geeksforgeeks.org/2d-and-2-5d-memory-organization/
: https://study.com/academy/lesson/two-dimensional-memory-models-benefits-limitations.html



# ROM Memories

- ROM stands for Read Only Memory, which means that the data stored in it can only be read and not modified.
- ROM is non-volatile memory, which means that the data stored in it is retained even when the power is turned off.
- ROM is typically used to store the computer’s BIOS (basic input/output system), which contains the instructions for booting the computer, as well as firmware for other hardware devices.
- ROM is also employed in the design of control units for digital computers, as it can implement any combinational circuit with k inputs and n outputs.
- ROM is a type of semiconductor-based memory, which is fabricated by joining circuits that physically encode the data to be stored.
- There are different types of ROM, such as:
  - Mask ROM: The data is programmed during the manufacturing process and cannot be changed later.
  - Programmable ROM (PROM): The data can be programmed once by the user using a special device called a programmer.
  - Erasable PROM (EPROM): The data can be erased and reprogrammed by exposing the chip to ultraviolet light.
  - Electrically Erasable PROM (EEPROM): The data can be erased and reprogrammed electrically, without removing the chip from the circuit.
  - Flash ROM: The data can be erased and reprogrammed in blocks, rather than byte by byte, which makes it faster and more convenient.
- ROM has some advantages and disadvantages, such as:
  - Advantages:
    - It is non-volatile, which means that it does not lose data when the power is off.
    - It is reliable and durable, as it does not have any moving parts or wear out.
    - It is secure, as it cannot be easily modified or corrupted by viruses or hackers.
  - Disadvantages:
    - It is read-only, which means that it cannot be updated or modified.
    - It is expensive and slow, compared to other types of memory.
    - It has limited storage capacity, as it depends on the physical size of the chip.



# Cache memories for the notes of the Unit 4 - Memory in the subject of Computer Organization and Architecture

- Cache memory is a special type of memory that is faster than main memory and is used to store frequently accessed data and instructions .
- Cache memory is located on the path between the CPU and the main memory, so that the CPU can access it without going through the slower main memory .
- The purpose of cache memory is to reduce the average time to access data from the main memory, which improves the performance and efficiency of the CPU .
- Cache memory works on the principle of locality of reference, which states that a program tends to access the same or nearby memory locations repeatedly.
- Cache memory consists of a small number of blocks, each of which can store a fixed number of words from the main memory .
- Each block in the cache memory has a tag, which is a part of the address of the corresponding block in the main memory .
- The cache memory also has a control unit, which is responsible for managing the transfer of data between the cache and the main memory .
- The cache memory can be classified into different types based on the mapping technique, the write policy, the cache level, and the cache organization.
- The mapping technique determines how a block of main memory is mapped to a block of cache memory. There are three main types of mapping techniques: direct mapping, associative mapping, and set-associative mapping.
- The write policy determines how the cache memory is updated when the CPU writes data to a memory location. There are two main types of write policies: write-through and write-back.
- The cache level refers to the hierarchy of cache memories in a system. There can be multiple levels of cache memories, such as L1, L2, and L3, which have different sizes, speeds, and distances from the CPU.
- The cache organization refers to the structure and design of the cache memory. There are two main types of cache organizations: unified and split.
- Cache memory has several advantages, such as faster access time, reduced bandwidth consumption, reduced power consumption, and improved CPU utilization.
- Cache memory also has some disadvantages, such as increased cost, increased complexity, increased heat generation, and cache coherence issues.
- Cache memory is an important component of computer architecture that enhances the performance and efficiency of the CPU by reducing the average time to access data from the main memory .



# Concept and Design Issues & Performance for the Notes of the Unit 4 - Memory in the Subject of Computer Organization and Architecture

- Memory is a crucial component of a computer system that stores data and instructions for processing. Memory can be classified into different types and levels based on various factors, such as capacity, access time, cost, and performance.
- Memory hierarchy is a concept that organizes memory into different levels, such as registers, cache, main memory, and secondary memory, to achieve a balance between speed and cost. The higher the level, the faster and more expensive the memory is. The lower the level, the slower and cheaper the memory is.
- Memory hierarchy also exploits the principle of locality, which states that programs tend to access data and instructions that are close to each other in space (spatial locality) or time (temporal locality). By keeping frequently accessed data and instructions in the higher levels of memory, the average access time can be reduced.
- Cache memory is a small and fast memory that acts as a buffer between the processor and the main memory. Cache memory stores copies of data and instructions that are likely to be accessed by the processor in the near future. Cache memory improves the performance of the computer system by reducing the number of memory accesses to the main memory, which is slower and farther away from the processor.
- Cache memory has several design issues, such as cache size, cache organization, cache mapping, cache replacement, and cache write policies. These issues affect the performance of the cache memory and the overall system.
- Cache size determines how much data and instructions can be stored in the cache memory. A larger cache size can reduce the cache miss rate, which is the ratio of cache misses to cache accesses. A cache miss occurs when the processor requests data or instructions that are not present in the cache memory, and has to access the main memory instead. However, a larger cache size also increases the cache access time, which is the time required to access the cache memory. A trade-off between cache size and cache access time has to be made to optimize the performance of the cache memory.
- Cache organization determines how the cache memory is divided into blocks or lines, which are the units of data transfer between the cache and the main memory. A cache block can have one or more words, which are the units of data transfer between the processor and the cache. A cache block can also have a tag, which is a part of the address that identifies the block in the cache. A cache organization can be direct-mapped, fully associative, or set associative, depending on how the cache blocks are mapped to the main memory addresses.
- Cache mapping determines how the main memory addresses are mapped to the cache blocks. There are three main types of cache mapping: direct mapping, associative mapping, and set associative mapping. Direct mapping maps each main memory address to exactly one cache block, using a simple modulo function. Associative mapping maps each main memory address to any cache block, using a comparison function. Set associative mapping maps each main memory address to a set of cache blocks, using a combination of modulo and comparison functions. Each type of cache mapping has its own advantages and disadvantages in terms of complexity, speed, and conflict misses. A conflict miss occurs when two or more main memory addresses map to the same cache block, and one of them has to be replaced by the other.
- Cache replacement determines which cache block to replace when a new block has to be brought into the cache memory. There are several cache replacement algorithms, such as least recently used (LRU), first in first out (FIFO), random, and least frequently used (LFU). Each algorithm has its own criteria for selecting the cache block to be replaced, based on the recency or frequency of access. The cache replacement algorithm affects the cache miss rate and the performance of the cache memory.
- Cache write policies determine how the cache memory handles write operations by the processor. There are two main types of cache write policies: write through and write back. Write through updates both the cache and the main memory whenever the processor writes to the cache. Write back updates only the cache whenever the processor writes to the cache, and updates the main memory only when the cache block is replaced. Each type of cache write policy has its own advantages and disadvantages in terms of consistency, bandwidth, and write misses. A write miss occurs when the processor writes to a main memory address that is not present in the cache memory, and has to bring the block into the cache first.
- Auxiliary memory is a large and slow memory that acts as a backup for the main memory. Auxiliary memory stores data and instructions that are not frequently accessed by the processor



# Address Mapping and Replacement

Address mapping is the process of translating a logical address (generated by the CPU) into a physical address (used to access the main memory or the cache memory). Address mapping is necessary because the CPU and the memory have different address spaces and different ways of organizing data.

There are different types of address mapping techniques, depending on how the logical address is divided and how the physical address is determined. Some of the common types are:

- **Direct mapping**: In this technique, the logical address is divided into three parts: the tag, the block number, and the word number. The block number is used to determine the cache block where the data is stored, and the tag is used to check if the data is valid. The word number is used to access the specific word within the block. This technique is simple and fast, but it may cause conflicts if two different logical addresses map to the same cache block.

- **Associative mapping**: In this technique, the logical address is divided into two parts: the tag and the word number. The tag is used to search the entire cache for a matching entry, and the word number is used to access the specific word within the block. This technique is flexible and avoids conflicts, but it is slow and expensive, as it requires a large amount of hardware to perform the search.

- **Set-associative mapping**: In this technique, the logical address is divided into three parts: the tag, the set number, and the word number. The set number is used to determine the cache set where the data is stored, and the tag is used to search within the set for a matching entry. The word number is used to access the specific word within the block. This technique is a compromise between direct and associative mapping, as it reduces the search time and the conflict rate, but it also increases the hardware complexity and the cost.

Address replacement is the process of selecting a cache block to be replaced when a new block needs to be brought into the cache. Address replacement is necessary because the cache has a limited size and cannot store all the blocks from the main memory. There are different types of address replacement algorithms, depending on how the cache block is chosen. Some of the common algorithms are:

- **FIFO (First-In First-Out)**: In this algorithm, the cache block that was brought into the cache first is replaced by the new block. This algorithm is simple and fair, but it may replace a frequently used block by a less used block.

- **LRU (Least Recently Used)**: In this algorithm, the cache block that was least recently accessed is replaced by the new block. This algorithm is based on the assumption that the block that was used recently is likely to be used again, and the block that was not used for a long time is unlikely to be used again. This algorithm is more efficient than FIFO, but it requires more hardware and time to keep track of the access history.

- **LFU (Least Frequently Used)**: In this algorithm, the cache block that was accessed the least number of times is replaced by the new block. This algorithm is based on the assumption that the block that was used frequently is likely to be used again, and the block that was used rarely is unlikely to be used again. This algorithm is more accurate than LRU, but it requires more hardware and time to keep track of the access frequency.

- **Random**: In this algorithm, the cache block to be replaced is chosen randomly. This algorithm is simple and fast, but it may replace a useful block by a useless block.



# Auxiliary memories

- Auxiliary memories are also known as secondary memories or external memories.
- They are non-volatile storage devices that can store large amounts of data and programs for long-term or permanent use.
- They have lower cost per bit, higher capacity, and longer data retention than primary memories, but they also have slower access time and lower bandwidth.
- They are connected to the computer system through input/output interfaces and require special software to manage the data transfer between them and the main memory.
- Some common examples of auxiliary memories are magnetic disks, optical disks, flash drives, and magnetic tapes.

## Magnetic disks

- Magnetic disks are circular platters coated with a thin layer of magnetic material that can store binary data as tiny magnetized regions on the surface.
- They are divided into concentric tracks and sectors, and each sector can store a fixed number of bytes.
- They are accessed by a read/write head that moves radially over the disk surface and rotates with the disk at a high speed.
- They can be classified into two types: hard disks and floppy disks.

### Hard disks

- Hard disks are rigid magnetic disks that are sealed inside a protective casing and mounted on a spindle.
- They have higher capacity, faster speed, and longer durability than floppy disks, but they are also more expensive and prone to mechanical failure.
- They are the most widely used auxiliary memory devices for storing operating systems, applications, and user data.

### Floppy disks

- Floppy disks are flexible magnetic disks that are enclosed in a plastic jacket and inserted into a disk drive.
- They have lower capacity, slower speed, and shorter lifespan than hard disks, but they are also cheaper and more portable.
- They are mostly obsolete now, but they were once popular for transferring small files and booting systems.

## Optical disks

- Optical disks are circular platters made of plastic or metal that can store binary data as tiny pits or marks on the surface.
- They are divided into concentric tracks and sectors, and each sector can store a fixed number of bytes.
- They are accessed by a laser beam that reflects off the disk surface and is detected by a photodiode.
- They can be classified into three types: read-only, write-once, and rewritable.

### Read-only optical disks

- Read-only optical disks are optical disks that are pre-recorded with data and cannot be modified by the user.
- They have high capacity, long durability, and low cost, but they are also inflexible and prone to physical damage.
- They are mainly used for distributing software, music, movies, and games.
- Some examples are CD-ROM, DVD-ROM, and Blu-ray Disc.

### Write-once optical disks

- Write-once optical disks are optical disks that can be recorded with data once by the user and cannot be erased or overwritten.
- They have high capacity, long durability, and moderate cost, but they are also inflexible and prone to physical damage.
- They are mainly used for archiving data, backup, and distribution.
- Some examples are CD-R, DVD-R, and BD-R.

### Rewritable optical disks

- Rewritable optical disks are optical disks that can be recorded with data multiple times by the user and can be erased or overwritten.
- They have high capacity, moderate durability, and high cost, but they are also flexible and reusable.
- They are mainly used for storing data, backup, and transfer.
- Some examples are CD-RW, DVD-RW, and BD-RE.

## Flash drives

- Flash drives are small and portable devices that can store binary data as electric charges in flash memory cells.
- They have no moving parts and are accessed by a controller that interfaces with a USB port or a memory card slot.
- They have high capacity, fast speed, and long durability, but they are also expensive and prone to wear and tear.
- They are mainly used for storing data, backup, and transfer.
- Some examples are USB flash drives, memory cards, and solid state drives.

## Magnetic tapes

- Magnetic tapes are long and narrow strips of plastic coated with a thin layer of magnetic material that can store binary data as tiny magnetized regions on the surface.
- They are wound on spools and are accessed by a read/write head that moves linearly over the tape surface and rotates with the tape at a constant speed.
- They have low cost, high capacity, and long durability, but they also have slow speed, low bandwidth, and sequential access.
- They are mainly used for archiving data, backup, and distribution.
- Some examples are cassette tapes, reel tapes, and tape cartridges.



# Magnetic Disk

- A magnetic disk is a storage device that is used to write, rewrite and access data. It uses a magnetization process to store binary data on a circular disk. 
- A magnetic disk consists of one or more platters, which are flat, circular disks coated with a thin film of magnetic material. Each platter has two recordable surfaces, one on each side.  
- Each platter is divided into concentric circles called tracks, which are further divided into sectors. A sector is the smallest unit of data that can be read or written on a disk. A sector typically stores 512 bytes of data.  
- A magnetic disk also has a moveable read/write head, which is attached to an arm that can move across the surface of the platter. The read/write head can read or write data on a specific track and sector by changing the magnetic polarity of the disk surface.  
- A magnetic disk rotates at a high speed, ranging from 5,400 to 15,000 revolutions per minute (RPM). The rotational speed determines how fast the read/write head can access the data on the disk.  
- A magnetic disk has several advantages over other storage devices, such as high capacity, low cost, durability, and random access. However, it also has some disadvantages, such as mechanical failure, fragmentation, and sensitivity to magnetic fields.



# Magnetic Tape Memory

- Magnetic tape memory is a system for storing digital information on magnetic tape using digital recording.
- Magnetic tape is the oldest memory media for computers, still in use today.
- Magnetic tape consists of a thin plastic ribbon coated by magnetic oxide, which can store data as binary patterns of magnetic polarity .
- Magnetic tape is a sequential memory, which means that data can only be accessed in a linear order, not randomly .
- Magnetic tape requires a magnetic tape drive, which is a device that writes and reads data from the tape using a read/write head .
- Magnetic tape has some advantages, such as high reliability, low cost, high capacity, and long-term storage .
- Magnetic tape also has some disadvantages, such as slow read/write speed, sequential access, wear and tear, and vulnerability to magnetic fields .



# Optical Disks

- Optical disks are a type of secondary storage device that use laser beams to read and write data on a rotating disk coated with a reflective material   .
- Optical disks have several advantages over magnetic disks, such as higher storage capacity, longer durability, lower cost per bit, and resistance to environmental factors .
- Optical disks also have some disadvantages, such as slower access time, higher power consumption, lower reliability, and higher sensitivity to scratches and dust .
- There are different types of optical disks, such as CD-ROM, CD-R, CD-RW, DVD-ROM, DVD-R, DVD-RW, Blu-ray, and HD DVD  .
- CD-ROM stands for compact disc read-only memory, and it can store up to 700 MB of data. CD-ROMs are pre-recorded and cannot be erased or modified .
- CD-R stands for compact disc recordable, and it can store up to 700 MB of data. CD-Rs can be written once by the user using a special device called a CD burner, but they cannot be erased or modified .
- CD-RW stands for compact disc rewritable, and it can store up to 700 MB of data. CD-RWs can be written, erased, and rewritten multiple times by the user using a CD burner, but they have lower compatibility and durability than CD-Rs .
- DVD-ROM stands for digital versatile disc read-only memory, and it can store up to 4.7 GB of data on a single layer or 8.5 GB on a dual layer. DVD-ROMs are pre-recorded and cannot be erased or modified .
- DVD-R stands for digital versatile disc recordable, and it can store up to 4.7 GB of data on a single layer or 8.5 GB on a dual layer. DVD-Rs can be written once by the user using a special device called a DVD burner, but they cannot be erased or modified .
- DVD-RW stands for digital versatile disc rewritable, and it can store up to 4.7 GB of data on a single layer or 8.5 GB on a dual layer. DVD-RWs can be written, erased, and rewritten multiple times by the user using a DVD burner, but they have lower compatibility and durability than DVD-Rs .
- Blu-ray is a newer type of optical disk that can store up to 25 GB of data on a single layer or 50 GB on a dual layer. Blu-ray uses a blue-violet laser with a shorter wavelength than the red laser used by CD and DVD, which allows for higher density and capacity .
- HD DVD stands for high-definition digital versatile disc, and it can store up to 15 GB of data on a single layer or 30 GB on a dual layer. HD DVD uses a blue laser with a slightly longer wavelength than Blu-ray, which allows for lower cost and higher compatibility, but lower capacity .
- Optical disks are used for various purposes, such as storing audio, video, software, games, documents, and backup data .



# Virtual Memory

- Virtual memory is a **technique** that allows the execution of programs that are not completely in physical memory.
- Virtual memory creates an **illusion** of a large main memory for the programmer, when in reality the physical memory is limited.
- Virtual memory uses some of the space from **secondary storage** (such as hard disk) and maps it to the **address space** of the process.
- Virtual memory allows **multiple processes** to share the physical memory and run concurrently, without interfering with each other.
- Virtual memory also enables **memory protection**, **relocation**, and **swapping** of processes.

## Characteristics of Virtual Memory

- Virtual memory is **transparent** to the programmer, meaning that the programmer does not need to know how the virtual memory is implemented or managed by the operating system.
- Virtual memory is **dynamic**, meaning that the mapping between the virtual addresses and the physical addresses can change during the execution of a process.
- Virtual memory is **hierarchical**, meaning that the virtual address space is divided into **pages** and the physical memory is divided into **frames**. A page is a fixed-size block of contiguous virtual addresses, and a frame is a fixed-size block of contiguous physical addresses. A page can be mapped to any frame in the physical memory, or to a location in the secondary storage if the page is not currently in use.
- Virtual memory is **demand-paged**, meaning that a page is only brought into the physical memory when it is needed by the process. This reduces the amount of physical memory required and allows the execution of programs that are larger than the physical memory.
- Virtual memory is **paged-replacement**, meaning that when the physical memory is full and a new page needs to be brought in, an existing page has to be **evicted** from the physical memory and written back to the secondary storage. The operating system uses a **replacement policy** to decide which page to evict, such as **least recently used (LRU)**, **first in first out (FIFO)**, or **random**.
- Virtual memory is **managed** by the operating system, with the help of the **hardware**. The hardware provides a **memory management unit (MMU)**, which is responsible for translating the virtual addresses to the physical addresses and checking the validity and protection of the pages. The MMU uses a **page table**, which is a data structure that stores the mapping information for each page. The page table is maintained by the operating system and updated whenever a page is brought in or evicted from the physical memory.



# Concept Implementation for the Notes of the Unit 4 - Memory in the Subject of Computer Organization and Architecture

- Memory is an essential component of a computer system that stores and retrieves data and instructions.
- Memory can be classified into two types: primary memory and secondary memory.
- Primary memory is the main memory of the computer that is directly accessible by the CPU. It is also known as RAM (Random Access Memory).
- Secondary memory is the auxiliary memory of the computer that is not directly accessible by the CPU. It is also known as ROM (Read Only Memory), cache memory, magnetic disk, magnetic tape, optical disk, etc.
- Memory organization refers to the way how the memory cells are arranged and accessed by the CPU.
- Memory organization can be divided into three levels: instruction set architecture, memory hierarchy, and virtual memory.

## Instruction Set Architecture

- Instruction set architecture (ISA) is the interface between the hardware and the software of a computer system. It defines the format, encoding, and semantics of the instructions that the CPU can execute.
- ISA also specifies the registers, addressing modes, data types, and interrupt mechanisms of the CPU.
- ISA can be classified into two types: RISC (Reduced Instruction Set Computer) and CISC (Complex Instruction Set Computer).
- RISC is a type of ISA that uses simple and uniform instructions that can be executed in one clock cycle. RISC has fewer and smaller registers, fewer addressing modes, and simpler instruction formats than CISC.
- CISC is a type of ISA that uses complex and variable-length instructions that can perform multiple operations in one instruction. CISC has more and larger registers, more addressing modes, and more instruction formats than RISC.
- RISC and CISC have different advantages and disadvantages in terms of performance, power consumption, code size, and compatibility.

## Memory Hierarchy

- Memory hierarchy is the arrangement of different types of memory in a computer system according to their speed, size, and cost.
- Memory hierarchy consists of several levels of memory, such as registers, cache, main memory, and secondary memory.
- The higher levels of memory are faster, smaller, and more expensive than the lower levels of memory.
- The lower levels of memory are slower, larger, and cheaper than the higher levels of memory.
- The CPU accesses the memory from the highest level to the lowest level, depending on the availability and locality of the data and instructions.
- Memory hierarchy aims to optimize the performance and cost of the computer system by using the principle of locality and the technique of caching.

## Virtual Memory

- Virtual memory is a technique that allows the computer system to use more memory than the physical memory available.
- Virtual memory creates an illusion of a large and contiguous memory space for the programs and the CPU by using the secondary memory as an extension of the main memory.
- Virtual memory divides the logical address space of a program into fixed-size units called pages, and the physical address space of the main memory into fixed-size units called frames.
- Virtual memory maps the pages to the frames using a data structure called page table, which is stored in the main memory or a special cache called translation lookaside buffer (TLB).
- Virtual memory uses two techniques to manage the pages and frames: page replacement and page allocation.
- Page replacement is the technique of selecting a victim page from the main memory to be replaced by a new page from the secondary memory when the main memory is full.
- Page allocation is the technique of assigning a free frame to a new page when the page is brought from the secondary memory to the main memory.
- Virtual memory improves the utilization and protection of the main memory, and allows the execution of large and multiple programs simultaneously.



## Unit 5 - Input / Output

- Input/output (I/O) is the process of transferring data between a computer system and its external devices, such as keyboards, mice, printers, monitors, disks, networks, etc.
- I/O devices can be classified into two categories: character devices and block devices.
  - Character devices transfer data one character (or byte) at a time, such as keyboards and terminals.
  - Block devices transfer data in fixed-size blocks, such as disks and tapes.
- I/O operations can be performed in different modes, such as synchronous, asynchronous, buffered, unbuffered, direct, and indirect.
  - Synchronous I/O means that the process that initiates the I/O operation waits until it is completed before resuming execution.
  - Asynchronous I/O means that the process that initiates the I/O operation can continue execution while the I/O operation is in progress.
  - Buffered I/O means that the data transferred between the process and the device is temporarily stored in a buffer (or cache) in memory to improve performance and reduce device access.
  - Unbuffered I/O means that the data transferred between the process and the device is not stored in a buffer, but directly transferred to or from the device.
  - Direct I/O means that the data transferred between the process and the device bypasses the operating system and is handled by the device driver or the hardware controller.
  - Indirect I/O means that the data transferred between the process and the device goes through the operating system, which provides services such as security, protection, and abstraction.
- I/O operations can be performed using different methods, such as polling, interrupt-driven, and direct memory access (DMA).
  - Polling is a method where the CPU repeatedly checks the status of the device to determine when it is ready to perform an I/O operation.
  - Interrupt-driven is a method where the device signals the CPU when it is ready to perform an I/O operation, and the CPU executes an interrupt handler to service the device.
  - DMA is a method where a special hardware controller transfers data between the device and the memory without involving the CPU, and notifies the CPU when the transfer is completed.



# Peripheral devices for the notes of the Unit 5 - Input / Output in the subject of Computer Organization and Architecture

- Peripheral devices are those devices that are linked either internally or externally to a computer.
- Peripheral devices are used to transfer data, provide input or output, or store information for the computer system .
- Peripheral devices are commonly divided into three kinds: input devices, output devices, and storage devices.
- Input devices are used to enter data and instructions into the computer, such as keyboards, mice, scanners, microphones, etc .
- Output devices are used to display or produce the results of the computer processing, such as monitors, printers, speakers, webcams, etc .
- Storage devices are used to store data and information for later use, such as hard disks, flash drives, optical disks, tapes, etc .
- Peripheral devices communicate with the computer system through various interfaces, such as serial ports, parallel ports, USB ports, wireless connections, etc .
- Peripheral devices may have different characteristics, such as speed, capacity, reliability, cost, etc, that affect their performance and suitability for different applications .
- Peripheral devices are an essential part of the computer system, as they enable the user to interact with the computer and extend its functionality and capabilities  .



# I/O Interface

- The I/O interface is the method that is used to transfer information between internal storage and external I/O devices.
- The I/O interface supports the communication between the CPU and the peripherals connected to the computer system.
- The I/O interface is part of the computer system's I/O architecture, which is its interface to the outside world .
- The I/O interface is designed to provide a systematic means of controlling interaction with the outside world and to provide the operating system with the information it needs to manage I/O activity effectively.
- The I/O interface consists of the following components:
  - I/O bus: The communication link between the CPU, memory and I/O devices.
  - I/O module: The device that controls the data transfer between the I/O bus and the I/O device.
  - I/O device: The external device that provides input or output for the computer system.
- The I/O interface can operate in different modes, such as programmed I/O, interrupt-driven I/O and direct memory access (DMA) I/O.
  - Programmed I/O: The CPU initiates and monitors the data transfer between the memory and the I/O device. The CPU is busy during the entire I/O operation and cannot perform other tasks.
  - Interrupt-driven I/O: The CPU initiates the data transfer between the memory and the I/O device and then resumes other tasks. The I/O device interrupts the CPU when the data transfer is complete or when an error occurs. The CPU then handles the interrupt and completes the I/O operation.
  - Direct memory access (DMA) I/O: The CPU initiates the data transfer between the memory and the I/O device and then resumes other tasks. The I/O device transfers the data directly to or from the memory without involving the CPU. The I/O device interrupts the CPU only when the data transfer is complete or when an error occurs. The CPU then handles the interrupt and completes the I/O operation.



# I/O Ports

- I/O ports are the interfaces between the CPU and the external devices, such as keyboards, monitors, printers, scanners, etc.
- I/O ports allow data to be transferred between the internal storage and the external I/O devices.
- I/O ports are controlled by I/O modules, which are special hardware components that supervise and synchronize all I/O operations.
- I/O modules perform the following functions:
  - Control and timing: coordinate the flow of traffic between internal resources and external devices.
  - Communication with the CPU: receive commands and report status.
  - Communication with the device: send commands and receive status.
  - Data buffering: store data temporarily to compensate for the speed difference between the CPU and the device.
  - Error detection: check for errors in the data or the device.
- There are different types of I/O ports, such as serial ports, parallel ports, USB ports, etc.
  - Serial ports: used for external modems and older computer mouse. Data travels one bit at a time. Two versions: 9-pin and 25-pin. Data rate: 115 kilobits per second.
  - Parallel ports: used for scanners and printers. Data travels eight bits at a time. One version: 25-pin. Data rate: 150 kilobytes per second.
  - USB ports: used for various devices, such as keyboards, mice, cameras, flash drives, etc. Data travels in packets. Two versions: USB 2.0 and USB 3.0. Data rate: up to 480 megabits per second for USB 2.0 and up to 5 gigabits per second for USB 3.0.
- There are different methods of I/O operations, such as programmed I/O, interrupt-driven I/O, and direct memory access (DMA).
  - Programmed I/O: the CPU executes a program that instructs the I/O module to perform an I/O operation. The CPU waits for the I/O module to complete the operation and then resumes the program.
  - Interrupt-driven I/O: the CPU executes a program that instructs the I/O module to perform an I/O operation and then continues with another program. The I/O module interrupts the CPU when the operation is completed and then the CPU resumes the original program.
  - DMA: the CPU instructs a specialized I/O processor to perform an I/O operation and then continues with another program. The I/O processor transfers a large block of data directly between the memory and the device without involving the CPU. The I/O processor interrupts the CPU when the operation is completed and then the CPU resumes the original program.



# Interrupts

- An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention.
- Interrupts allow the processor to suspend its current execution and service the occurred interrupt by executing the corresponding interrupt service routine (ISR).
- Interrupts are essential for efficient and responsive interaction between the processor and the external devices such as I/O or memory.
- Interrupts can be classified into two main types: hardware interrupts and software interrupts.
  - Hardware interrupts are generated by external devices such as keyboards, mice, printers, etc. that are connected to the interrupt request line of the processor.
  - Software interrupts are generated by instructions executed by the processor such as system calls, exceptions, or traps.
- Interrupts can also be classified based on their priority, masking, and handling.
  - Priority determines the order in which interrupts are serviced by the processor. Higher priority interrupts can preempt lower priority interrupts.
  - Masking is the ability to disable or enable interrupts based on certain conditions. Maskable interrupts can be ignored by the processor, while non-maskable interrupts cannot.
  - Handling is the method of processing interrupts by the processor. Vectored interrupts have a predefined address for the ISR, while non-vectored interrupts require the processor to fetch the address from a memory location.
- Interrupts require the processor to perform the following steps:
  - Save the current state of the processor, such as the program counter, registers, flags, etc.
  - Identify the source and type of the interrupt and determine the appropriate ISR to execute.
  - Transfer the control to the ISR and execute it until completion or until another interrupt occurs.
  - Restore the saved state of the processor and resume the interrupted execution.



# Interrupt Hardware

- An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention.
- Interrupts are commonly used by hardware devices to indicate electronic or physical state changes that require time-sensitive attention, such as clicking a mouse, pressing a keyboard key, or printing a document  .
- Interrupts are also commonly used to implement computer multitasking, especially in real-time computing. Systems that use interrupts in these ways are said to be interrupt-driven.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
  - Hardware interrupts are generated by external devices that are connected to the interrupt request line of the processor. A single request line is used for all the devices, and each device has a unique priority level. The processor checks the priority of the interrupt request and decides whether to accept it or not.
  - Software interrupts are generated by programs that execute special instructions, such as system calls or exceptions. Software interrupts are also called traps or faults. They are used to request services from the operating system or to handle errors or exceptions.
- When an interrupt occurs, the processor saves the current state of the program and transfers the control to an interrupt handler routine, which is a special program that performs the required work or handles any errors before handing back control to the interrupted program . The interrupt handler routine is also called an interrupt service routine (ISR) or an interrupt handler.
- Interrupts can be enabled or disabled by the processor or the operating system. Enabling interrupts allows the processor to respond to interrupt requests, while disabling interrupts prevents the processor from being interrupted. Disabling interrupts is usually done temporarily to ensure the atomicity or consistency of certain operations .



# Types of Interrupts and Exceptions

## Interrupts
- Interrupts are signals that cause the CPU to temporarily stop its current execution and switch to a predefined handler routine.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are generated by external devices, such as keyboards, mice, timers, disk drives, etc. They are asynchronous, meaning they can occur at any time during the execution of a program.
- Software interrupts are generated by the program itself, such as system calls, breakpoints, illegal instructions, etc. They are synchronous, meaning they occur at a specific point in the program execution.

## Exceptions
- Exceptions are also signals that cause the CPU to temporarily stop its current execution and switch to a predefined handler routine.
- Exceptions are generated by the CPU itself, when it encounters an abnormal or erroneous condition during the execution of an instruction.
- Exceptions can be classified into four types: traps, faults, aborts and resets.
- Traps are intentional exceptions that are used for debugging, testing, or implementing system services. They are also synchronous and occur at a specific point in the program execution.
- Faults are unintentional exceptions that are caused by errors or invalid conditions in the program or data. They are also synchronous and can be corrected by the handler routine. For example, division by zero, page fault, etc.
- Aborts are severe exceptions that are caused by unrecoverable errors or system failures. They are also synchronous but cannot be corrected by the handler routine. For example, parity error, machine check, etc.
- Resets are special exceptions that are caused by power-on or hardware reset. They are asynchronous and cause the CPU to restart from a known state. For example, system reboot, watchdog timer, etc.



# Modes of Data Transfer

Data transfer is the process of moving data from one device or component to another in a computer system. Data transfer can occur between the CPU and the memory, between the CPU and the input/output devices, or between the memory and the input/output devices. There are three main modes of data transfer in computer organization and architecture:

- **Programmed I/O**: In this mode, the CPU executes a program that contains instructions to transfer data to or from an I/O device. The CPU initiates and controls the data transfer by issuing commands to the I/O device and checking its status. The CPU is busy during the entire data transfer and cannot perform other tasks. This mode is simple but inefficient, as it wastes CPU time and resources.
- **Interrupt-initiated I/O**: In this mode, the CPU executes a program that contains instructions to transfer data to or from an I/O device, but the data transfer is performed by the I/O device itself. The CPU only initiates the data transfer by issuing a command to the I/O device and then resumes its normal operation. When the data transfer is completed, the I/O device interrupts the CPU to notify it. The CPU then handles the interrupt by executing a service routine that processes the data. This mode is more efficient than programmed I/O, as it allows the CPU to perform other tasks while the data transfer is in progress.
- **Direct memory access (DMA)**: In this mode, the data transfer between the I/O device and the memory is performed by a special hardware unit called the DMA controller, without involving the CPU. The CPU initiates the data transfer by supplying the DMA controller with the starting address and the number of words to be transferred, and then proceeds to execute other tasks. The DMA controller accesses the memory and the I/O device directly through the memory bus and transfers the data. When the data transfer is completed, the DMA controller interrupts the CPU to notify it. This mode is the most efficient of all, as it frees the CPU from the data transfer and reduces the number of interrupts.



# Programmed I/O

- Programmed I/O is a method of transferring data between the CPU and a peripheral device, such as a keyboard, a mouse, a disk, or a network adapter   .
- Programmed I/O operations are the result of I/O instructions written in the computer program .
- In programmed I/O, each data transfer is initiated by the CPU, and the CPU is in continuous monitoring of the interface  .
- Programmed I/O is usually used for transferring data from a CPU register and memory.
- Programmed I/O is very cheap and easy to implement, but it has some disadvantages:
  - It consumes a lot of CPU time and resources, as the CPU has to wait for the I/O device to be ready and check the status of the device repeatedly   .
  - It reduces the performance and throughput of the system, as the CPU cannot execute other tasks while performing I/O operations   .
  - It is not suitable for high-speed devices or large amounts of data, as the CPU may not be able to keep up with the data rate or the data size   .
- Programmed I/O can be improved by using techniques such as buffering, handshaking, and polling.



# Interrupt Initiated I/O

- Interrupt initiated I/O is a mode of data transfer between the CPU and the I/O devices that uses an interrupt facility and special commands.
- In this mode, the CPU issues an I/O command to the I/O module and then resumes its normal execution of other tasks.
- The I/O module performs the data transfer independently of the CPU and raises an interrupt signal when the data is ready or the transfer is complete.
- The CPU responds to the interrupt by saving its current state and executing an interrupt service routine (ISR) that handles the I/O operation.
- The ISR may read or write the data from or to the I/O module, acknowledge the interrupt, and restore the CPU state to resume the normal execution.
- Interrupt initiated I/O has the following advantages over programmed I/O:
  - It reduces the CPU involvement and overhead in the I/O process.
  - It allows the CPU to perform other tasks while the I/O module is busy with the data transfer.
  - It improves the performance and efficiency of the system by avoiding the wastage of CPU cycles in polling or looping.
- Interrupt initiated I/O has the following challenges and limitations:
  - It requires a mechanism to identify the source and type of the interrupt, which may be done by using interrupt vectors or priority levels.
  - It requires a mechanism to handle multiple or simultaneous interrupts, which may be done by using interrupt masking or nesting.
  - It may cause latency or delay in the CPU response to the interrupt, which may affect the real-time or critical applications.
  - It may still involve the CPU in the data transfer if the I/O module does not have a direct memory access (DMA) capability.



# Direct Memory Access for the notes of the Unit 5 - Input / Output in the subject of Computer Organization and Architecture

- Direct Memory Access (DMA) is a feature of computer systems that allows certain hardware subsystems to access main system memory independently of the central processing unit (CPU).
- DMA is used to improve the performance and efficiency of data transfer between I/O devices and memory, or between memory and memory, without involving the CPU in each operation .
- DMA can reduce the CPU's workload and latency, as well as increase the bandwidth and throughput of the system.
- DMA can be implemented using a dedicated hardware device called a DMA controller (DMAC), which communicates with the CPU, the memory, and the I/O devices using control signals and buses.
- The DMA controller can operate in different modes, such as single transfer, block transfer, demand transfer, and burst transfer, depending on the amount and frequency of data to be transferred.
- The DMA controller can also support different types of DMA, such as cycle stealing, transparent, and fly-by, depending on the priority and timing of the data transfer.
- The DMA controller can also perform memory-to-memory operations, such as copying or moving data in memory, or scatter-gather operations, which involve transferring data from or to non-contiguous memory locations.
- The DMA controller can also be integrated with other hardware components, such as network-on-chip or memory computing architectures, to enable faster and more parallel data processing.



# I/O Channels and Processors

- I/O channels are extensions of the DMA concept that have the ability to execute I/O instructions using special-purpose processors on I/O channels and complete control over I/O operations.
- The processor does not execute I/O instructions itself, but initiates I/O transfer by instructing the I/O channel to execute a program in memory.
- I/O channels can be classified into different types based on their functionality and performance :
  - Byte multiplexer: It is used for low-speed devices. It transmits or accepts characters and interleaves bytes from several devices.
  - Block multiplexer: It accepts or transmits blocks of characters and interleaves blocks of bytes from several devices. It is used for high-speed devices.
  - Selector channel: It can handle one high-speed device at a time and transfers data directly to or from the main memory.
  - Multiplexor channel: It can handle multiple devices simultaneously and transfers data to or from a buffer in the channel processor.
- I/O processors are simple, independent and low-cost processors that handle all I/O tasks for the channels .
- I/O processors have their own memory and instruction set and can fetch and execute their own programs .
- I/O processors communicate with the CPU using interrupts and inform the CPU about the completion or error of I/O operations .
- I/O processors can improve the performance and efficiency of I/O operations by offloading the CPU from I/O tasks.



# Serial Communication

Serial communication is the process of sequentially transferring the information/bits on the same channel. Due to this, the cost of wire will be reduced, but it slows the transmission speed. Serial communication is used for all long-haul communication and most computer networks, where the parallel communication is impractical. Serial communication can either be asynchronous or synchronous.

## Asynchronous Serial Communication

Asynchronous serial communication is a method of transmitting data without a common clock signal between the sender and the receiver. The sender and the receiver agree on a baud rate, which is the number of bits per second, and use start and stop bits to mark the beginning and the end of each data frame. The advantage of asynchronous serial communication is that it does not require a dedicated clock line, and it can tolerate some variations in the baud rate. The disadvantage is that it requires more bits for framing and error detection, and it is more susceptible to noise and interference.

## Synchronous Serial Communication

Synchronous serial communication is a method of transmitting data with a common clock signal between the sender and the receiver. The sender and the receiver synchronize their clocks using a separate clock line or by embedding the clock signal in the data stream. The advantage of synchronous serial communication is that it can achieve higher data rates and lower overhead, as it does not need start and stop bits. The disadvantage is that it requires a dedicated clock line or a more complex encoding scheme, and it is more sensitive to clock skew and jitter.

## Serial Communication Interfaces

Some of the well-known interfaces used for serial communication are:

- RS-232: A standard for serial communication between a computer and a peripheral device, such as a modem or a printer. It uses a single-ended signaling, which means that each signal is referenced to a common ground. It can support data rates up to 20 kbps over a distance of 15 meters.
- RS-485: A standard for serial communication between multiple devices on a bus network, such as industrial control systems or security cameras. It uses a differential signaling, which means that each signal is represented by the difference between two wires. It can support data rates up to 10 Mbps over a distance of 1.2 kilometers.
- I2C: A standard for serial communication between multiple devices on a two-wire bus, such as sensors or microcontrollers. It uses a synchronous serial communication, where the clock signal is provided by the master device. It can support data rates up to 3.4 Mbps over a distance of 1 meter.
- SPI: A standard for serial communication between multiple devices on a four-wire bus, such as memory chips or LCD displays. It uses a synchronous serial communication, where the clock signal is provided by the master device. It can support data rates up to 50 Mbps over a distance of 10 centimeters.

## Data Communication Processor

A data communication processor is an I/O processor that distributes and collects data from numerous remote terminals connected through telephone and other communication lines to the computer. It is a specialized I/O processor designed to communicate with data communication networks. It performs the following functions:

- Modulation and demodulation: It converts the digital signals from the computer to analog signals for the communication lines, and vice versa.
- Error detection and correction: It checks the integrity of the data and corrects any errors that may occur during transmission.
- Protocol conversion: It converts the data format and protocol of the computer to the data format and protocol of the network, and vice versa.
- Buffering and multiplexing: It stores the data temporarily and combines multiple data streams into one, or splits one data stream into multiple.



# Synchronous and Asynchronous Communication

Synchronous and asynchronous communication are two modes of communication that are used in computer organization and architecture. They differ in the timing and coordination of the data transfer between the sender and the receiver.

## Synchronous Communication

- Synchronous communication is a mode of communication where the sender and the receiver are synchronized in time and exchange data at a fixed rate.
- Synchronous communication requires a common clock signal between the sender and the receiver to coordinate the data transfer.
- Synchronous communication is simpler in design but carries the risk of spreading failures across services. To mitigate that risk, the architect must implement sophisticated service discovery and application load balancing among microservices.
- Synchronous communication is suitable for real-time applications that require low latency and high reliability, such as video conferencing, online gaming, and live streaming.
- Examples of synchronous communication are phone calls, video calls, face-to-face meetings, and synchronous serial communication protocols such as SPI and I2C.

## Asynchronous Communication

- Asynchronous communication is a mode of communication where the sender and the receiver are not synchronized in time and exchange data at variable rates.
- Asynchronous communication does not require a common clock signal between the sender and the receiver, but uses start and stop bits to indicate the beginning and the end of a data frame.
- Asynchronous communication trades architectural simplicity and data consistency for scalability, resilience, and flexibility. It allows the sender and the receiver to operate independently and handle data at their own pace.
- Asynchronous communication is suitable for non-real-time applications that require high throughput and low coupling, such as email, chat, and asynchronous serial communication protocols such as UART and USB.
- Examples of asynchronous communication are email, text messages, social media posts, and blog comments.



# Standard Communication Interfaces

- A communication interface is a device or system that allows data to be exchanged between different components of a computer system or a network.
- A standard communication interface is a communication interface that follows a predefined set of rules or protocols for data transfer, such as SCSI, USB, Ethernet, etc.
- A standard communication interface decouples the design and introduction of computing hardware, such as I/O devices, from the design and introduction of other components of a computing system, thereby allowing users and manufacturers great flexibility in the implementation of computing systems.
- A standard communication interface consists of two main parts: the physical layer and the logical layer.
  - The physical layer defines the electrical and mechanical characteristics of the interface, such as the connectors, cables, voltages, signals, etc.
  - The logical layer defines the format and meaning of the data that is transferred over the interface, such as the commands, responses, error detection, etc.
- A standard communication interface supports a method by which data is transferred between internal storage and external I/O devices.
  - The data transfer can be synchronous or asynchronous.
    - Synchronous data transfer means that the data is transferred at a fixed rate and with a fixed timing between the sender and the receiver.
    - Asynchronous data transfer means that the data is transferred without a fixed rate or timing between the sender and the receiver, and the sender and the receiver use some signals or codes to indicate the start and the end of the data .
  - The data transfer can be serial or parallel.
    - Serial data transfer means that the data is transferred one bit at a time over a single wire or channel.
    - Parallel data transfer means that the data is transferred multiple bits at a time over multiple wires or channels.
- A standard communication interface provides a set of primitive operations or services that each layer in a network layered architecture can use to communicate with each other.
  - The services can be connection-oriented or connectionless.
    - Connection-oriented services mean that the sender and the receiver establish a logical connection before exchanging data, and maintain the connection until the data transfer is complete.
    - Connectionless services mean that the sender and the receiver do not establish a logical connection before exchanging data, and each data unit is treated independently.
  - The services can be reliable or unreliable.
    - Reliable services mean that the sender and the receiver ensure that the data is delivered correctly and in order, and use some mechanisms to handle errors, losses, or duplicates.
    - Unreliable services mean that the sender and the receiver do not guarantee that the data is delivered correctly and in order, and do not use any mechanisms to handle errors, losses, or duplicates.
- A standard communication interface uses an interface data unit (IDU) to have an agreed way of communication among two layers in a network layered architecture.
  - An IDU is a data unit that contains the information that is exchanged between two layers, such as the header, the payload, and the trailer.
  - An IDU is passed from the higher layer to the lower layer, and from the lower layer to the higher layer, through a service access point (SAP).
  - A SAP is an identifier label for the endpoints of a network in a layered model, and it specifies which service or protocol is used by the layer.
- A standard communication interface uses a control and status register to communicate with the CPU.
  - A control and status register is a register that contains the information that is used to control or monitor the operation of the interface, such as the mode, the direction, the status, the interrupt, etc.
  - A control and status register is accessed by the CPU through a data bus buffer, which is a bi-directional data bus that connects the interface to the CPU.
  - A control and status register is also connected to the read/write control logic, which is a circuit that determines whether the CPU is reading from or writing to the interface.
- A standard communication interface uses a port register to communicate with the I/O device.
  - A port register is a register that contains the data that is transferred between the interface and the I/O device, such as the input data, the output data, the address

