

# KCS

KCS stands for Knowledge-Centered Service, which is a methodology for creating and maintaining documentation as part of the service delivery process. KCS aims to improve service quality, productivity, and customer satisfaction by capturing and reusing the knowledge of service teams. Some of the main features of KCS are:

- KCS is based on the principle of "capture in the workflow", which means that service agents create and update knowledge articles while solving customer issues, rather than as a separate task.
- KCS uses a "demand-driven" approach, which means that knowledge articles are created and refined based on the actual needs and feedback of customers, rather than based on assumptions or predictions.
- KCS follows a "double-loop" process, which means that knowledge articles are continuously improved through two feedback loops: the "reuse" loop, which measures how often and how effectively an article is used to solve an issue, and the "improve" loop, which measures how often and how significantly an article is modified or enhanced.
- KCS adopts a "shared ownership" model, which means that knowledge articles are owned by the collective service organization, rather than by individual authors or teams. This enables faster and easier access, collaboration, and quality control of knowledge.
- KCS leverages a "structured problem-solving" technique, which means that service agents use a consistent and logical framework to diagnose and resolve customer issues, and to document the problem, cause, and resolution in knowledge articles.
- KCS supports a "self-service" strategy, which means that knowledge articles are made available and searchable for customers, enabling them to find answers to their own questions and issues, reducing the need for service interactions.



## Unit 1 - Microprocessor evolution and types, microprocessor architecture and operation of its components, addressing modes, interrupts, data transfer schemes, instruction and data flow, timer and timing diagram, Interfacing devices.

- A microprocessor is an electronic device that performs arithmetic and logic operations on digital data. It is the brain of a computer system that controls the execution of instructions and the processing of data.
- The evolution of microprocessor can be divided into five generations based on the technology, architecture, and performance of the devices. The characteristics of these generations are:

  - First generation (1971-1972): These were the first commercial microprocessors that used 4-bit or 8-bit data bus and had a simple instruction set. They were mainly used for embedded applications such as calculators, terminals, and printers. Examples are Intel 4004 and Intel 8008.
  - Second generation (1973-1978): These were 8-bit microprocessors that used larger and faster memory and had more complex instruction sets. They were capable of addressing up to 64 KB of memory and supported external devices such as keyboards, displays, and disk drives. Examples are Intel 8080, Motorola 6800, and Zilog Z80.
  - Third generation (1979-1985): These were 16-bit microprocessors that used advanced fabrication techniques and had more powerful instruction sets. They were able to perform multitasking and multiprocessing and supported high-level languages and operating systems. Examples are Intel 8086, Motorola 68000, and Zilog Z8000.
  - Fourth generation (1986-1995): These were 32-bit microprocessors that used very large scale integration (VLSI) technology and had more sophisticated architectures. They were able to perform pipelining, parallel processing, and floating-point operations and supported graphical user interfaces and multimedia applications. Examples are Intel 80386, Motorola 68020, and ARM.
  - Fifth generation (1996-present): These are 64-bit microprocessors that use ultra large scale integration (ULSI) technology and have more advanced features. They are able to perform superscalar, vector, and parallel processing and support virtualization, encryption, and artificial intelligence. Examples are Intel Pentium, AMD Athlon, and IBM Power.

- The microprocessor architecture consists of three main components: the central processing unit (CPU), the memory, and the input/output (I/O) devices. The CPU is further divided into two subunits: the arithmetic logic unit (ALU) and the control unit (CU). The operation of these components are:

  - The ALU performs arithmetic and logic operations on the data provided by the memory or the I/O devices. It also sets the flags and status bits based on the result of the operations.
  - The CU controls the sequence and timing of the instructions and the data flow. It generates the control signals and the addresses for the memory and the I/O devices. It also decodes the instructions and executes them by sending the appropriate signals to the ALU and other components.
  - The memory stores the instructions and the data that are needed by the CPU. It is divided into two types: the primary memory and the secondary memory. The primary memory is the main memory that is directly accessible by the CPU. It is further divided into two types: the random access memory (RAM) and the read only memory (ROM). The RAM is a volatile memory that can be read and written by the CPU. It stores the temporary data and the variables that are used by the programs. The ROM is a non-volatile memory that can only be read by the CPU. It stores the permanent data and the programs that are essential for the system. The secondary memory is the auxiliary memory that is not directly accessible by the CPU. It is used to store large amounts of data and programs that are not frequently used by the system. Examples are hard disks, floppy disks, and optical disks.
  - The I/O devices are the peripherals that allow the communication between the microprocessor and the external world. They are used to input data and instructions to the system and to output the results and information from the system. Examples are keyboards, mice, monitors, printers, and speakers.

- The addressing modes are the ways of specifying the location of the operands that are used by the instructions. The operands can be stored in the registers, the memory, or the I/O devices. The



### Microprocessor Evolution and Types

- A microprocessor is an electronic device that performs arithmetic and logic operations on digital data.
- A microprocessor consists of a central processing unit (CPU), which executes instructions, and a memory unit, which stores data and instructions.
- A microprocessor can be classified according to its generation, bit size, instruction set, and architecture.

#### Generation of Microprocessors

- The generation of a microprocessor refers to the technological advancement and innovation that occurred during its development.
- The first generation of microprocessors was introduced in the early 1970s and used 4-bit or 8-bit data buses. They had low processing speed and memory capacity. Examples are Intel 4004 and Intel 8008 .
- The second generation of microprocessors was introduced in the mid-1970s and used 8-bit or 16-bit data buses. They had higher processing speed and memory capacity. They also supported more complex instructions and addressing modes. Examples are Intel 8080 and Zilog Z80 .
- The third generation of microprocessors was introduced in the early 1980s and used 16-bit or 32-bit data buses. They had even higher processing speed and memory capacity. They also supported pipelining, cache memory, and multitasking. Examples are Intel 8086 and Motorola 68000 .
- The fourth generation of microprocessors was introduced in the late 1980s and used 32-bit or 64-bit data buses. They had very high processing speed and memory capacity. They also supported parallel processing, floating-point arithmetic, and graphical user interface. Examples are Intel 80386 and Intel Pentium .
- The fifth generation of microprocessors was introduced in the late 1990s and used 64-bit data buses. They had extremely high processing speed and memory capacity. They also supported multiprocessing, multimedia, and artificial intelligence. Examples are Intel Core and AMD Ryzen .

#### Bit Size of Microprocessors

- The bit size of a microprocessor refers to the number of bits that it can process in one cycle.
- The bit size determines the range of values that a microprocessor can represent and manipulate.
- The bit size also affects the performance and complexity of a microprocessor.
- A higher bit size means a larger data bus, a larger address bus, a larger register size, and a larger instruction set.
- A higher bit size also means a higher processing speed, a higher memory capacity, and a higher accuracy.
- The bit size of microprocessors has increased from 4 bits to 64 bits over the generations.

#### Instruction Set of Microprocessors

- The instruction set of a microprocessor refers to the set of commands that it can execute.
- The instruction set determines the functionality and versatility of a microprocessor.
- The instruction set also affects the efficiency and compatibility of a microprocessor.
- A larger instruction set means more operations and modes that a microprocessor can perform and support.
- A larger instruction set also means more memory and time required to store and execute the instructions.
- The instruction set of microprocessors can be classified into two types: complex instruction set computing (CISC) and reduced instruction set computing (RISC).

- CISC microprocessors have a large and complex instruction set that can perform multiple operations in one instruction. They are designed to minimize the number of instructions per program and ignore the number of cycles per instruction. They are suitable for high-level languages and general-purpose applications. Examples are Intel 8086 and Intel Pentium.
- RISC microprocessors have a small and simple instruction set that can perform one operation in one instruction. They are designed to minimize the number of cycles per instruction and ignore the number of instructions per program. They are suitable for low-level languages and specific-purpose applications. Examples are ARM and MIPS.

#### Architecture of Microprocessors

- The architecture of a microprocessor refers to the design and organization of its components and subsystems.
- The architecture determines the performance and functionality of a microprocessor.
- The architecture also affects the cost and complexity of a microprocessor.
- The architecture of microprocessors can be classified into two types: von Neumann and Harvard.

- Von Neumann microprocessors have a single memory unit that stores both data and instructions. They have a single data bus and a single address bus that connect the CPU and the memory. They use a sequential fetch-execute cycle to process the instructions. They are simple and



### Microprocessor Architecture and Operation of its Components

A microprocessor is a single integrated circuit (IC) that contains the data processing logic and control of a computer's central processing unit (CPU). It performs arithmetic, logic, and control operations on the data received from an input device or memory. It also communicates with other devices through a system bus. A microprocessor can be classified into different generations based on its features, performance, and technology.

The basic components of a microprocessor architecture are:

- Arithmetic Logic Unit (ALU): It performs arithmetic and logic operations on the data, such as addition, subtraction, multiplication, division, and comparison. It also sets the flags according to the result of the operation.
- Accumulator: It is a special register that holds one of the operands as well as the result of the operation performed by the ALU. It is also used for temporary storage of data.
- Program Counter (PC): It is a register that holds the address of the next instruction to be executed. It is incremented by one after each instruction execution.
- Control Unit: It is the part of the microprocessor that controls the flow of instructions and data within the microprocessor and between the microprocessor and other devices. It generates the control signals for the ALU, registers, and the system bus. It also decodes the instructions and executes them according to the instruction cycle.
- Register Array: It is a set of registers that are used for storing data and addresses. Some of the registers are general-purpose, while some are special-purpose, such as the stack pointer, the index register, the status register, etc. The number and size of the registers vary depending on the microprocessor.



### Addressing Modes

Addressing modes are the ways in which a microprocessor can access the operands or data for an instruction. Different addressing modes provide different levels of flexibility and efficiency for accessing memory or registers. The 8085 and 8086 microprocessors have different sets of addressing modes, but some of them are common. Here are some of the common addressing modes with examples:

- **Immediate addressing mode**: In this mode, the operand or data is specified in the instruction itself. For example, `MVI A, 05H` is an instruction that loads the value 05H into the accumulator register A. This mode is fast and simple, but it can only handle 8-bit or 16-bit data.  

- **Register addressing mode**: In this mode, the operand or data is stored in one of the registers of the microprocessor. For example, `MOV B, A` is an instruction that copies the value of the accumulator register A into the register B. This mode is also fast and simple, but it has limited number of registers available.  

- **Register indirect addressing mode**: In this mode, the operand or data is stored in a memory location whose address is stored in a register pair. For example, `MOV A, M` is an instruction that loads the value of the memory location pointed by the register pair HL into the accumulator register A. This mode allows accessing any memory location, but it requires an extra register pair to store the address.  

- **Direct addressing mode**: In this mode, the operand or data is stored in a memory location whose address is specified in the instruction. For example, `LDA 2000H` is an instruction that loads the value of the memory location 2000H into the accumulator register A. This mode also allows accessing any memory location, but it requires 16 bits to specify the address.  

- **Implicit addressing mode**: In this mode, the operand or data is implied by the instruction itself. For example, `CMA` is an instruction that complements the value of the accumulator register A. This mode does not require any operand or address, but it can only perform certain predefined operations.  

The 8086 microprocessor has some additional addressing modes, such as:

- **Base addressing mode**: In this mode, the operand or data is stored in a memory location whose address is calculated by adding a base register and a displacement value. For example, `MOV AL, [BX+10H]` is an instruction that loads the value of the memory location whose address is BX+10H into the register AL. This mode allows accessing memory locations relative to a base register, but it requires an extra byte to specify the displacement.  

- **Indexed addressing mode**: In this mode, the operand or data is stored in a memory location whose address is calculated by adding an index register and a displacement value. For example, `MOV AL, [SI+10H]` is an instruction that loads the value of the memory location whose address is SI+10H into the register AL. This mode allows accessing memory locations relative to an index register, but it also requires an extra byte to specify the displacement.  

- **Based indexed addressing mode**: In this mode, the operand or data is stored in a memory location whose address is calculated by adding a base register, an index register and a displacement value. For example, `MOV AL, [BX+SI+10H]` is an instruction that loads the value of the memory location whose address is BX+SI+10H into the register AL. This mode allows accessing memory locations relative to both a base register and an index register, but it requires two extra bytes to specify the displacement and the index register.  

- **Relative addressing mode**: In this mode, the operand or data is stored in a memory location whose address is calculated by adding the program counter and a displacement value. For example, `JMP 10H` is an instruction that jumps to the memory location whose address is PC+10H. This mode allows accessing memory locations relative to the current instruction, but it requires an extra byte to specify the displacement.  

- **Port addressing mode**: In this mode, the operand or data is stored in an



### Interrupts

- An interrupt is a condition that causes the microprocessor to temporarily work on a different task, and then later return to its previous task.
- Interrupts can be internal or external. Internal interrupts, or "software interrupts," are triggered by a software instruction and operate similarly to a jump or branch instruction. External interrupts, or "hardware interrupts," are triggered by an external device, such as a keyboard, a mouse, a timer, or another microprocessor.
- Interrupts are used for data transfer between the peripheral and the microprocessor, or for handling errors or exceptional situations  .
- When an interrupt occurs, the microprocessor saves the current state of the program counter and the flags register, and then jumps to a predefined memory location, called the interrupt vector, where the interrupt handler routine is stored .
- The interrupt handler routine completes the required work or handles any errors before handing back control to the interrupted application. The microprocessor restores the saved state of the program counter and the flags register, and resumes the execution of the original program.
- Interrupts can be classified into various categories based on different parameters, such as:
  - Hardware and software interrupts: Hardware interrupts are generated by external devices, while software interrupts are generated by software instructions .
  - Maskable and non-maskable interrupts: Maskable interrupts are those that can be enabled or disabled by the microprocessor, while non-maskable interrupts are those that cannot be ignored by the microprocessor .
  - Vectored and non-vectored interrupts: Vectored interrupts are those that have a predefined interrupt vector, while non-vectored interrupts are those that require the microprocessor to fetch the interrupt vector from the external device .
  - Priority interrupts: Priority interrupts are those that have a predefined order of importance, and can be serviced according to their priority level .



### Data Transfer Schemes

- Data transfer schemes are the methods through which data can be transferred between the units of a microprocessor system, such as the CPU, memory, and I/O devices.
- Data transfer schemes are important for the efficient and smooth operation of the system, as they affect the speed, performance, and complexity of the system.
- There are three main types of data transfer schemes: programmed I/O, interrupt-driven I/O, and direct memory access (DMA).

#### Programmed I/O

- Programmed I/O is a simple and basic data transfer scheme, where the CPU executes a program that controls the data transfer between the memory and the I/O device.
- The program consists of a series of instructions that read or write data from or to the I/O device, using the CPU registers as temporary storage.
- The CPU polls the status of the I/O device to check whether it is ready for data transfer or not, and waits until the device is ready.
- Programmed I/O is suitable for transferring small amounts of data, where speed is not critical, and the CPU can afford to wait for the I/O device.
- The advantages of programmed I/O are that it is simple, easy to implement, and does not require any additional hardware.
- The disadvantages of programmed I/O are that it is slow, inefficient, and wastes the CPU time and resources.

#### Interrupt-Driven I/O

- Interrupt-driven I/O is a data transfer scheme that uses interrupts to notify the CPU when the I/O device is ready for data transfer.
- An interrupt is a signal that causes the CPU to temporarily suspend its current program and execute a special routine called an interrupt service routine (ISR), which handles the data transfer with the I/O device.
- The ISR saves the current state of the CPU, performs the data transfer, and restores the CPU state, before returning to the original program.
- Interrupt-driven I/O is suitable for transferring moderate amounts of data, where speed is important, but not critical, and the CPU can perform other tasks while waiting for the I/O device.
- The advantages of interrupt-driven I/O are that it is faster, more efficient, and does not waste the CPU time and resources as much as programmed I/O.
- The disadvantages of interrupt-driven I/O are that it is more complex, requires additional hardware and software, and may cause conflicts or delays if multiple devices request interrupts at the same time.

#### Direct Memory Access (DMA)

- Direct memory access (DMA) is a data transfer scheme that allows the I/O device to directly access the memory, without involving the CPU.
- A special hardware device called a DMA controller (DMAC) is used to control the data transfer between the memory and the I/O device, using a dedicated bus.
- The CPU initiates the DMA transfer by sending the parameters, such as the source and destination addresses, the amount of data, and the mode of transfer, to the DMAC, and then resumes its normal operation.
- The DMAC takes over the control of the bus, and transfers the data between the memory and the I/O device, using the parameters provided by the CPU.
- The DMAC notifies the CPU when the DMA transfer is complete, by sending an interrupt signal.
- DMA is suitable for transferring large amounts of data, where speed is critical, and the CPU cannot afford to wait for the I/O device.
- The advantages of DMA are that it is the fastest, most efficient, and does not waste the CPU time and resources at all.
- The disadvantages of DMA are that it is the most complex, requires additional hardware and software, and may cause conflicts or delays if multiple devices request DMA at the same time.



### Instruction and Data Flow

- Instruction and data flow are the processes of fetching and executing instructions and transferring data between the microprocessor and other devices.
- Instruction flow involves the following steps:
  - The microprocessor sends the address of the instruction to be fetched to the memory via the address bus.
  - The microprocessor sends a control signal to the memory to indicate that it wants to read the instruction from the memory.
  - The memory sends the instruction to the microprocessor via the data bus.
  - The microprocessor stores the instruction in the instruction register and increments the program counter to point to the next instruction.
  - The microprocessor decodes the instruction and executes it by performing the appropriate operations on the data or registers.
- Data flow involves the following steps:
  - The microprocessor sends the address of the data to be read or written to the memory or I/O device via the address bus.
  - The microprocessor sends a control signal to the memory or I/O device to indicate whether it wants to read or write the data.
  - If the microprocessor wants to read the data, the memory or I/O device sends the data to the microprocessor via the data bus. If the microprocessor wants to write the data, the microprocessor sends the data to the memory or I/O device via the data bus.
  - The microprocessor stores or updates the data in the memory or I/O device and proceeds to the next instruction.



### Timer and Timing Diagram

- A timer is a device that generates a periodic signal that can be used to control the timing of various operations in a microprocessor system.
- A timing diagram is a graphical representation of the sequence of events that occur during the execution of an instruction or a program in a microprocessor system.
- A timing diagram shows the changes in the signals of various components, such as the address bus, the data bus, the control signals, the clock signal, etc., as a function of time.
- A timing diagram can help to understand the working of an instruction or a program, to analyze the performance of a microprocessor system, to debug errors, and to design interfacing devices.
- A timing diagram can be divided into two parts: the operation part and the state part.
- The operation part shows the name of the instruction or the program being executed, and the state part shows the changes in the signals of various components during each clock cycle.
- A timing diagram can be drawn for different types of instructions, such as data transfer instructions, arithmetic and logical instructions, branch instructions, etc.
- A timing diagram can also be drawn for different types of data transfer schemes, such as memory-mapped I/O, port-mapped I/O, interrupt-driven I/O, DMA, etc.
- A timing diagram can vary depending on the microprocessor architecture, the instruction set, the clock frequency, the memory access time, the interfacing devices, etc.
- A timing diagram can be drawn using different notations, such as high and low levels, rising and falling edges, pulses, etc.



### Interfacing devices

- Interfacing devices are circuits that connect the microprocessor with other internal or external devices, such as memory, input/output, timers, etc.
- Interfacing devices can be classified into two types: I/O interfacing and memory interfacing.
- I/O interfacing is the process of connecting input devices (such as keyboard, mouse, etc.) and output devices (such as screen, printer, etc.) with the microprocessor. I/O interfacing devices include latches, buffers, decoders, encoders, multiplexers, etc.
- Memory interfacing is the process of connecting memory devices (such as RAM, ROM, etc.) with the microprocessor. Memory interfacing devices include address latches, address decoders, memory chips, etc.
- Interfacing devices are designed to match the signal requirements of the microprocessor and the devices. For example, the interfacing devices should provide the appropriate voltage levels, timing, control signals, data format, etc. for the microprocessor and the devices to communicate.



## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram of 8085 microprocessor:

  - The 8085 microprocessor is a 40-pin IC with 8-bit data bus and 16-bit address bus.
  - The pins can be classified into six groups: address bus, data bus, control and status signals, power supply and frequency, externally initiated signals, and serial I/O ports.
  - The address bus consists of 8 pins (A8-A15) that are multiplexed with the data bus and 8 pins (A0-A7) that are dedicated for addressing.
  - The data bus consists of 8 pins (AD0-AD7) that are bidirectional and multiplexed with the lower order address bus.
  - The control and status signals consist of 6 pins that are used to synchronize the data transfer between the microprocessor and the peripherals. These are: RD (read), WR (write), ALE (address latch enable), IO/M (input/output or memory), S0 and S1 (status signals).
  - The power supply and frequency pins consist of 2 pins that provide the operating voltage (+5V) and the clock signal (CLK) to the microprocessor.
  - The externally initiated signals consist of 5 pins that are used to communicate with external devices and handle interrupts. These are: RESET IN, RESET OUT, HOLD, HLDA (hold acknowledge), and INTR (interrupt request).
  - The serial I/O ports consist of 2 pins that are used for serial data communication. These are: SID (serial input data) and SOD (serial output data).

- Internal architecture of 8085 microprocessor:

  - The 8085 microprocessor consists of three main units: the arithmetic and logic unit (ALU), the timing and control unit, and the register array.
  - The ALU performs the arithmetic and logical operations on the data. It has an accumulator (A) register, a temporary (T) register, and a flag (F) register. The flag register contains five flags: sign (S), zero (Z), auxiliary carry (AC), parity (P), and carry (CY).
  - The timing and control unit generates the control and status signals for the data transfer and the execution of instructions. It also generates the clock signal for the microprocessor and the peripherals.
  - The register array contains six general purpose registers: B, C, D, E, H, and L. These registers can be used as 8-bit registers or as 16-bit register pairs (BC, DE, HL). The register array also contains two special purpose registers: the program counter (PC) and the stack pointer (SP). The PC holds the address of the next instruction to be executed. The SP holds the address of the top of the stack in the memory.

- Registers, ALU, Control & status, interrupt and machine cycle:

  - Registers are the internal memory locations that store the data and the addresses for the microprocessor operations. They are faster than the external memory and can be accessed directly by the microprocessor.
  - ALU is the unit that performs the arithmetic and logical operations on the data. It can perform operations such as addition, subtraction, increment, decrement, logical AND, OR, XOR, NOT, compare, rotate, etc.
  - Control and status signals are the signals that control the data transfer and the execution of instructions. They are generated by the timing and control unit and are sent to the peripherals and the internal units of the microprocessor. Some of the control signals are: RD, WR, ALE, IO/M, S0, S1, etc. Some of the status signals are: HLDA, INTR, INTA (interrupt acknowledge), etc.
  - Interrupt is a signal that requests the microprocessor to stop the current execution and service a higher priority task. The 8085 microprocessor has five interrupt sources: TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR. The interrupt sources have different priorities and can be enabled or disabled by the software or the hardware.
  - Machine cycle is the time required to complete one operation of accessing memory, I/O, or acknowledging an interrupt. A machine cycle consists of 3 to 6 T-states, where T-state is the time period of one clock cycle. The 8085 microprocessor has four types of machine cycles: opcode fetch, memory read, memory



### Pin diagram and internal architecture of 8085 microprocessor

- The 8085 microprocessor is a 8-bit microprocessor that can perform arithmetic and logical operations on 8-bit data at a time.
- It has 40 pins that can be categorized into six groups: address and data bus, control signals, status signals, power supply, and serial input/output ports  .
- The pin diagram of 8085 microprocessor is shown below:

8085 pin diagram

- The address bus is a group of 16 lines (A0-A15) that are used to transfer the memory address of the data that needs to be read or written. The address bus is unidirectional, i.e., bits flow in one direction from the microprocessor unit to the peripheral devices .
- The data bus is a group of 8 lines (D0-D7) that are used to transfer the data between the microprocessor and the memory or I/O devices. The data bus is bidirectional, i.e., bits can flow in both directions .
- The control signals are used to control the timing and operation of the microprocessor and the peripheral devices. The control signals are:
  - ALE (Address Latch Enable): It is an active high signal that indicates whether the address bus contains a valid address or data. It is used to latch the lower order address from the multiplexed address/data bus .
  - RD (Read): It is an active low signal that indicates that the microprocessor is ready to read data from the memory or I/O device addressed by the address bus .
  - WR (Write): It is an active low signal that indicates that the microprocessor is ready to write data to the memory or I/O device addressed by the address bus .
- The status signals are used to indicate the status of the microprocessor and the peripheral devices. The status signals are:
  - IO/M (Input/Output or Memory): It is an active high signal that indicates whether the address on the address bus is for an I/O device or a memory location .
  - S0 and S1 (Status 0 and Status 1): These are two active high signals that indicate the type of operation being performed by the microprocessor. The possible values of S0 and S1 are :

    | S0 | S1 | Operation |
    | -- | -- | --------- |
    | 0  | 0  | HALT      |
    | 0  | 1  | WRITE     |
    | 1  | 0  | READ      |
    | 1  | 1  | FETCH     |

- The power supply and clock signals are used to provide the necessary power and timing for the microprocessor. The power supply and clock signals are:
  - Vcc and Vss: These are the positive and negative power supply pins that provide +5V and ground respectively to the microprocessor .
  - X1 and X2: These are the crystal oscillator pins that are connected to an external crystal or clock circuit to generate the clock signal for the microprocessor  .
  - CLK (OUT): This is the clock output pin that provides the clock signal to other devices connected to the microprocessor .
- The serial input/output ports are used to transfer data serially between the microprocessor and other devices. The serial input/output ports are:
  - SID (Serial Input Data): This is the serial input pin that receives the serial data from an external device .
  - SOD (Serial Output Data): This is the serial output pin that sends the serial data to an external device .
- The interrupts and externally generated signals are used to handle the external events that require the attention of the microprocessor. The interrupts and externally generated signals are:
  - INTR (Interrupt Request): This is an active low signal that indicates that an external device has requested an interrupt service from the microprocessor. The microprocessor acknowledges the interrupt request by sending an INTA (



### Registers of 8085 microprocessor

- A 8085 microprocessor is a second generation 8-bit microprocessor that is widely used for learning and programming microprocessors.
- It has eight addressable 8-bit registers: A, B, C, D, E, H, L, F, and two 16-bit registers PC and SP.
- These registers can be classified as:

  - General Purpose Registers (GPRs): These are B, C, D, E, H, and L. They can store 8-bit data and can be used for various operations. They are less important than the accumulator.
  - Accumulator: This is the most important register, also known as A. It is used to store the result of arithmetic and logical operations. It can also perform I/O operations.
  - Flag Register: This is also known as F. It is used to store the status of the microprocessor after an operation. It has five flags: Sign (S), Zero (Z), Auxiliary Carry (AC), Parity (P), and Carry (CY).
  - Program Counter (PC): This is a 16-bit register that stores the address of the next instruction to be executed. It is incremented automatically after each instruction.
  - Stack Pointer (SP): This is a 16-bit register that stores the address of the top of the stack. The stack is a section of memory used to store data temporarily.
  - Temporary Registers: These are not directly accessible by the programmer. They are used by the microprocessor internally for various purposes. They are:

    - Temporary Data Register (TDR): This is an 8-bit register that holds the data during data transfer between the microprocessor and the memory or I/O devices.
    - W and Z Registers: These are two 8-bit registers that are used to form a 16-bit address during indirect addressing mode.
    - Serial Control Register (SC) and Serial Shift Register (SS): These are two 8-bit registers that are used to control and monitor the serial communication.

- The flow of an instruction cycle in 8085 architecture is as follows:

  - Fetch: The microprocessor fetches the instruction from the memory pointed by the PC and stores it in the TDR. The PC is incremented by one.
  - Decode: The microprocessor decodes the instruction in the TDR and identifies the operation code and the operands.
  - Execute: The microprocessor executes the instruction according to the operation code and the operands. The result is stored in the accumulator or the memory, and the flags are updated accordingly.
  - Interrupt: The microprocessor checks for any interrupt request from the external devices. If there is any, it saves the current state of the microprocessor and jumps to the interrupt service routine. Otherwise, it continues with the next instruction.



### ALU

- ALU stands for Arithmetic Logic Unit, and it is a major component of the central processing unit of a computer system .
- ALU performs arithmetic and logical operations on integer binary numbers .
- ALU can perform operations such as addition, subtraction, multiplication, division, AND, OR, XOR, NOT, etc  .
- ALU receives operands and control codes from the registers and the control unit, and outputs the results to the registers or the memory .
- ALU can also set or clear status flags, such as zero, carry, overflow, sign, etc, to indicate the outcome of the operations  .
- ALU is typically designed first in a microprocessor, and then the rest of the microprocessor is implemented to feed data and instructions to the ALU.
- ALU is different from a floating-point unit (FPU), which operates on floating point numbers .
- ALU is also different from a logic unit (LU), which only performs logical operations and not arithmetic operations. Some microprocessors have separate AU and LU units.



### Control and Status for the Notes of the Unit 2

- Control and status signals are used to identify the nature of operation, such as memory read, memory write, I/O read, I/O write, etc.
- The 8085 microprocessor provides two control signals: RD (read) and WR (write) to initiate read or write cycle. These signals are used both for reading/writing memory and for reading/writing an input device.
- The 8085 microprocessor also provides a signal called IO/M (input/output or memory) to indicate whether the initiated cycle is for an I/O device or for a memory device. IO/M is high for I/O operations and low for memory operations.
- The 8085 microprocessor has a 16-bit address bus, which can address up to 64KB of memory. The address bus is divided into two parts: the high-order address bus (A15-A8) and the low-order address bus (A7-A0).
- The 8085 microprocessor has an 8-bit data bus, which can transfer 8 bits of data at a time. The data bus is multiplexed with the low-order address bus, and is denoted as AD7-AD0. A multiplexer is used to separate the data bus from the address bus during a read or write operation.
- The 8085 microprocessor has a 16-bit program counter (PC), which holds the address of the next instruction to be executed. The PC is incremented automatically after each instruction fetch.
- The 8085 microprocessor has a 16-bit stack pointer (SP), which points to the top of the stack in the memory. The stack is used to store the return addresses of subroutines, interrupt service routines, and data temporarily.
- The 8085 microprocessor has six 8-bit registers, which are arranged in pairs: BC, DE, and HL. These registers can be used as 16-bit registers by combining them in pairs. For example, BC can be used as B (high-order byte) and C (low-order byte).
- The 8085 microprocessor has an 8-bit accumulator (A), which is used to store the result of arithmetic and logical operations. The accumulator is also called the register A.
- The 8085 microprocessor has an 8-bit flag register (F), which indicates the status of the accumulator after an operation. The flag register has five flags: sign (S), zero (Z), auxiliary carry (AC), parity (P), and carry (CY).
- The 8085 microprocessor has an arithmetic and logic unit (ALU), which performs arithmetic and logical operations on the data in the accumulator and the registers.
- The 8085 microprocessor has a control unit, which generates the control signals for the internal and external devices. The control unit also coordinates the timing and sequencing of the operations.
- The 8085 microprocessor has a serial communication unit, which allows the data transfer between the microprocessor and the external devices in serial mode. The serial communication unit has two pins: SID (serial input data) and SOD (serial output data).
- The 8085 microprocessor has an interrupt unit, which handles the external interrupts from the peripheral devices. The interrupt unit has five interrupt pins: TRAP, RST 7.5, RST 6.5, RST 5.5, and INTR. The interrupt unit also has an interrupt enable flip-flop, which can be set or reset by the EI (enable interrupt) and DI (disable interrupt) instructions.
- The 8085 microprocessor has a machine cycle unit, which defines the basic operations performed by the microprocessor. A machine cycle is the time required to complete one operation of accessing memory, I/O, or acknowledging an external request. A machine cycle consists of three or more T-states, which are the subdivisions of a machine cycle.
- The 8085 microprocessor has an instruction set, which is a collection of instructions that the microprocessor can execute. The instruction set of 8085 microprocessor has 74 instructions, which are classified into five categories: data transfer, arithmetic, logical, branching, and machine control.
- The 8085 microprocessor has three addressing modes, which specify how the operands of an instruction are accessed. The addressing modes are: immediate, direct, and register.
- The 8085 microprocessor has three instruction formats, which define the structure of an instruction. The instruction formats are: one-byte, two-byte, and three-byte.
- The 8085 microprocessor has some assembler directives, which



### Interrupt and Machine Cycle

- An interrupt is a signal that causes the microprocessor to temporarily stop its current program execution and switch to a predefined subroutine called an interrupt service routine (ISR).
- The ISR performs the necessary task related to the interrupt source and then returns to the main program.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are initiated by external devices that are connected to the microprocessor through the interrupt pins.
- Software interrupts are instructions that are embedded in the program code and are executed by the microprocessor.
- The 8085 microprocessor has five hardware interrupt pins: INTR, RST 7.5, RST 6.5, RST 5.5, and TRAP.
- The 8085 microprocessor has eight software interrupt instructions: RST 0, RST 1, RST 2, RST 3, RST 4, RST 5, RST 6, and RST 7.
- The RST instructions cause the microprocessor to jump to a fixed memory location, which is 8 times the value of the RST number. For example, RST 5 causes the microprocessor to jump to 40H (8 x 5).
- The INTR pin is a maskable interrupt, which means it can be enabled or disabled by the software using the EI (enable interrupt) and DI (disable interrupt) instructions.
- The RST 7.5, RST 6.5, and RST 5.5 pins are also maskable interrupts, but they have a priority order. RST 7.5 has the highest priority, followed by RST 6.5, and then RST 5.5.
- The TRAP pin is a non-maskable interrupt, which means it cannot be disabled by the software. It has the highest priority among all the interrupts and is used for critical situations such as power failure or emergency stop.
- When an interrupt is accepted by the microprocessor, it generates an interrupt acknowledge signal (INTA) to inform the interrupt source.
- The interrupt source then sends an instruction to the microprocessor, which is usually a CALL or a RST instruction, to execute the ISR.
- The microprocessor then saves the address of the next instruction on the stack and jumps to the ISR.
- After completing the ISR, the microprocessor returns to the main program by popping the address from the stack and executing a RET (return) instruction.

- A machine cycle is the basic operation performed by the microprocessor to access the memory or the I/O devices.
- A machine cycle consists of one or more clock cycles, where each clock cycle is the time taken by the microprocessor to complete one full pulse of the clock signal.
- The 8085 microprocessor has six types of machine cycles: opcode fetch, memory read, memory write, I/O read, I/O write, and interrupt acknowledge.
- The opcode fetch machine cycle is used to fetch the opcode of an instruction from the memory. It consists of four clock cycles (T1, T2, T3, T4).
- The memory read machine cycle is used to read data from the memory. It consists of three clock cycles (T1, T2, T3).
- The memory write machine cycle is used to write data to the memory. It also consists of three clock cycles (T1, T2, T3).
- The I/O read machine cycle is used to read data from an I/O device. It consists of four clock cycles (T1, T2, T3, T4).
- The I/O write machine cycle is used to write data to an I/O device. It also consists of four clock cycles (T1, T2, T3, T4).
- The interrupt acknowledge machine cycle is used to acknowledge an interrupt request from an external device. It consists of three or more clock cycles (T1, T2, T3, ...).
- The number of clock cycles in an interrupt acknowledge machine cycle depends on the type of interrupt and the instruction sent by the interrupt source.
- For example, if the interrupt source sends a RST instruction, the interrupt acknowledge machine cycle consists of six clock cycles (T1, T2, T3, T4, T5, T6).
- If the interrupt source sends a CALL instruction, the interrupt acknowledge machine cycle consists of nine clock cycles (T1, T2, T3, T4, T5, T6, T7, T8, T9).
- The timing diagram of a



### Instruction sets for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram and internal architecture of 8085 microprocessor
  - The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has a 16-bit address bus that can address up to 64 KB of memory. It has 40 pins and operates with +5V power supply.
  - The pin diagram of 8085 microprocessor is shown below   :

  ```
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | A15 | A14 | A13 | A12 | A11 | A10 | A9  | A8  | A7  | A6  | A5  | A4  | A3  | A2  | A1  | A0  |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10 |  11 |  12 |  13 |  14 |  15 |  16 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | AD7 | AD6 | AD5 | AD4 | AD3 | AD2 | AD1 | AD0 | ALE | IO/M| S0  | S1  | RD  | WR  | READY| HOLD|
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  17 |  18 |  19 |  20 |  21 |  22 |  23 |  24 |  25 |  26 |  27 |  28 |  29 |  30 |  31 |  32 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  | HLDA| RESET IN| RESET OUT| CLK OUT| X2 | X1 | VSS | SID | SOD | TRAP| RST 7.5| RST 6.5| RST 5.5| INTR| INTA| VCC |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  |  33 |   34    |    35    |   36   | 37 | 38 | 39  | 40  | 39  | 38  |   37   |   36   |   35   |  34 |  33 |  32 |
  +-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+-----+
  ```
  - The internal architecture of 8085 microprocessor consists of various units such as registers, ALU, control and status, interrupt and machine cycle. The CPU acts as the core of the microprocessor and it has instruction register and decoder, timing control, various registers, and serial I/O control. The internal architecture of 8085 microprocessor is shown below:

  ```
  +-----------------+     +-----------------+     +-----------------+     +-----------------+
  |                 |     |                 |     |                 |     |                 |
  |    Address      |     |    Data Bus     |     |    Control      |     |    Power        |

```




### Addressing modes for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Addressing modes are the ways of specifying data to be operated by an instruction.
- The 8085 microprocessor supports five addressing modes: immediate, register, register indirect, direct, and implied.
- Immediate addressing mode: the operand is given in the instruction itself. For example, MVI A, 07H means load the accumulator with the value 07H .
- Register addressing mode: the operand is stored in one of the registers. For example, MOV A, B means copy the contents of register B to the accumulator .
- Register indirect addressing mode: the operand is stored in a memory location whose address is given by a register pair. For example, MOV A, M means copy the contents of the memory location pointed by the HL register pair to the accumulator .
- Direct addressing mode: the operand is stored in a memory location whose address is given in the instruction. For example, LDA 2000H means load the accumulator with the contents of the memory location 2000H .
- Implied addressing mode: the operand is implied by the instruction. For example, RLC means rotate the bits of the accumulator left in a circular manner .

: A Short Note on Addressing Modes in 8085 Microprocessor - Unacademy
: Addressing modes in 8085 microprocessor - GeeksforGeeks
: Addressing Modes in 8085 Microprocessor - Technobyte



### Instruction formats and classification

- An instruction is a binary pattern that specifies a specific operation to be performed by the microprocessor.
- The instruction format of 8085 microprocessor consists of one, two or three bytes, depending on the type of instruction.
- The first byte is always the opcode, which specifies the operation code or the type of instruction.
- The second byte (if present) is usually the operand, which specifies the data or the address involved in the operation.
- The third byte (if present) is usually the higher-order byte of the 16-bit address or data.
- The instruction set of 8085 microprocessor is classified into the following five groups according to the function they perform:

  - Data transfer instructions: These instructions are used to transfer data between registers, memory and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations such as addition, subtraction, increment, decrement, etc. Examples are ADD, SUB, INR, DCR, DAD, etc.
  - Logical instructions: These instructions are used to perform logical operations such as AND, OR, XOR, complement, rotate, etc. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branching instructions: These instructions are used to change the sequence of execution of the program based on certain conditions. Examples are JMP, JNZ, JC, CALL, RET, etc.
  - Machine control instructions: These instructions are used to control the operation of the microprocessor such as halt, interrupt enable, interrupt disable, etc. Examples are HLT, EI, DI, NOP, etc.

- The instruction set of 8085 microprocessor is also classified into the following three groups according to the size they occupy in memory:

  - One-byte instructions: These instructions have only one byte, which is the opcode. Examples are CMA, DAA, EI, DI, etc.
  - Two-byte instructions: These instructions have two bytes, the first byte is the opcode and the second byte is the operand. Examples are MVI, IN, OUT, ADI, SUI, etc.
  - Three-byte instructions: These instructions have three bytes, the first byte is the opcode and the last two bytes are the operand. Examples are LDA, STA, LHLD, SHLD, LXI, etc.



### Data Transfer for the Notes of the Unit 2

- Data transfer is the process of moving data from one location to another in the microprocessor system.
- Data transfer can occur between registers, memory, and I/O devices.
- Data transfer instructions are the instructions that perform data transfer operations in the 8085 microprocessor.
- Data transfer instructions are classified into the following types:

  - **MOV**: This instruction copies data from the source register to the destination register. The source and destination registers can be any of the general-purpose registers (B, C, D, E, H, L, or A) or the accumulator. The syntax is `MOV destination, source`. For example, `MOV A, B` copies the contents of register B to the accumulator.
  - **MVI**: This instruction loads an 8-bit immediate data into a register. The register can be any of the general-purpose registers or the accumulator. The syntax is `MVI register, data`. For example, `MVI A, 05H` loads the hexadecimal value 05 into the accumulator.
  - **LDA**: This instruction loads an 8-bit data from a memory location into the accumulator. The memory location is specified by a 16-bit address. The syntax is `LDA address`. For example, `LDA 2000H` loads the data stored at the memory location 2000H into the accumulator.
  - **STA**: This instruction stores an 8-bit data from the accumulator into a memory location. The memory location is specified by a 16-bit address. The syntax is `STA address`. For example, `STA 3000H` stores the data in the accumulator into the memory location 3000H.
  - **LHLD**: This instruction loads a 16-bit data from a memory location into the register pair HL. The memory location is specified by a 16-bit address. The lower byte of the data is stored in register L and the higher byte is stored in register H. The syntax is `LHLD address`. For example, `LHLD 4000H` loads the data stored at the memory locations 4000H and 4001H into the register pair HL.
  - **SHLD**: This instruction stores a 16-bit data from the register pair HL into a memory location. The memory location is specified by a 16-bit address. The lower byte of the data is stored in the lower memory location and the higher byte is stored in the higher memory location. The syntax is `SHLD address`. For example, `SHLD 5000H` stores the data in the register pair HL into the memory locations 5000H and 5001H.
  - **LXI**: This instruction loads a 16-bit immediate data into a register pair. The register pair can be BC, DE, HL, or SP. The lower byte of the data is stored in the lower register and the higher byte is stored in the higher register. The syntax is `LXI register pair, data`. For example, `LXI B, 1234H` loads the hexadecimal value 1234 into the register pair BC.
  - **LDAX**: This instruction loads an 8-bit data from a memory location into the accumulator. The memory location is specified by the contents of a register pair. The register pair can be BC or DE. The syntax is `LDAX register pair`. For example, `LDAX B` loads the data stored at the memory location pointed by the register pair BC into the accumulator.
  - **STAX**: This instruction stores an 8-bit data from the accumulator into a memory location. The memory location is specified by the contents of a register pair. The register pair can be BC or DE. The syntax is `STAX register pair`. For example, `STAX D` stores the data in the accumulator into the memory location pointed by the register pair DE.
  - **XCHG**: This instruction exchanges the contents of the register pairs DE and HL. The syntax is `XCHG`. For example, `XCHG` swaps the data in the register pairs DE and HL.



### Arithmetic Operations

- The 8085 microprocessor performs various arithmetic operations, such as addition, subtraction, increment, and decrement .
- These arithmetic operations have the following mnemonics :

| Mnemonic | Operand | Explanation |
| --- | --- | --- |
| ADD | r/M/data | Add register, memory or data to accumulator |
| ADC | r/M/data | Add register, memory or data to accumulator with carry |
| SUB | r/M/data | Subtract register, memory or data from accumulator |
| SBB | r/M/data | Subtract register, memory or data from accumulator with borrow |
| INR | r/M | Increment register or memory by 1 |
| DCR | r/M | Decrement register or memory by 1 |
| INX | rp | Increment register pair by 1 |
| DCX | rp | Decrement register pair by 1 |
| DAD | rp | Add register pair to HL register pair |
| DAA | - | Decimal adjust accumulator |

- The 8085 microprocessor also performs multiplication and division operations by using repeated addition and subtraction instructions.
- The arithmetic operations affect the flags in the flag register, such as the zero flag, the sign flag, the parity flag, the carry flag, and the auxiliary carry flag .
- The arithmetic operations are performed by the arithmetic and logic unit (ALU) of the 8085 microprocessor, which is a part of the internal architecture.
- The arithmetic operations are classified as data transfer instructions, as they transfer data between the accumulator and other registers, memory or data .



### Logical Operations in 8085 Microprocessor

- Logical operations are the instructions that perform basic logical operations such as AND, OR, XOR, NOT, etc. on the bits of the operands.
- In the 8085 microprocessor, the destination operand for the logical instructions is always the accumulator register (A).
- The logical operations work on a bitwise level, meaning that each bit of the accumulator is logically operated with the corresponding bit of the source operand.
- The source operand can be either a register, a memory location, or an immediate data.
- The result of the logical operation is stored in the accumulator register and the flags are affected accordingly.
- The logical instructions in 8085 microprocessor are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| ANA | Logical AND with accumulator | ANA B (A <- A AND B) |
| ANI | Logical AND with immediate data | ANI 0F (A <- A AND 0F) |
| ORA | Logical OR with accumulator | ORA C (A <- A OR C) |
| ORI | Logical OR with immediate data | ORI 0A (A <- A OR 0A) |
| XRA | Logical XOR with accumulator | XRA D (A <- A XOR D) |
| XRI | Logical XOR with immediate data | XRI 55 (A <- A XOR 55) |
| CMA | Complement accumulator | CMA (A <- NOT A) |
| RLC | Rotate accumulator left | RLC (A <- A << 1) |
| RRC | Rotate accumulator right | RRC (A <- A >> 1) |
| RAL | Rotate accumulator left through carry | RAL (A <- A << 1 + CY) |
| RAR | Rotate accumulator right through carry | RAR (A <- A >> 1 + CY) |

- The flags affected by the logical instructions are:

| Flag | Condition |
| --- | --- |
| S | Set if the result is negative |
| Z | Set if the result is zero |
| P | Set if the result has even parity |
| C | Set or reset depending on the instruction |
| AC | Set if there is a carry from bit 3 to bit 4 |



### Branching Operations

- Branching operations are instructions that allow the microprocessor to change the sequence of the program, either unconditionally or under certain conditions  .
- Branching operations can be classified into three types: unconditional branching, conditional branching, and subroutine branching .
- Unconditional branching instructions are those that always cause a jump to a specified address, regardless of the status of the flags or the contents of the registers. The only unconditional branching instruction in 8085 microprocessor is JMP (Jump) which has the format JMP 16-bit address  .
- Conditional branching instructions are those that cause a jump to a specified address only if a certain condition is met, otherwise the program continues with the next instruction. The condition is usually based on the status of the flags or the contents of the accumulator. The conditional branching instructions in 8085 microprocessor are JC (Jump if Carry), JNC (Jump if No Carry), JZ (Jump if Zero), JNZ (Jump if Not Zero), JP (Jump if Positive), JM (Jump if Minus), JPE (Jump if Parity Even), and JPO (Jump if Parity Odd). They all have the format JXX 16-bit address, where XX is the condition  .
- Subroutine branching instructions are those that cause a jump to a specified address and save the return address in the stack. A subroutine is a section of code that performs a specific task and can be called from different parts of the program. The subroutine branching instructions in 8085 microprocessor are CALL (Call Subroutine), RET (Return from Subroutine), and RST (Restart). They all have the format XXX 16-bit address, except RST which has the format RST n, where n is a number from 0 to 7  .
- Branching operations are useful for implementing loops, decision making, and modular programming in 8085 microprocessor. They can alter the flow of control and make the program more efficient and flexible .



### Machine Control and Assembler Directives

- Machine control instructions are used to control the operation of the 8085 microprocessor, such as enabling or disabling interrupts, halting the processor, or sending or receiving serial data.
- Assembler directives are commands to the assembler that do not generate machine codes, but help in the assembly process, such as defining data, allocating memory, or specifying the starting address of the program.
- Some of the machine control instructions are:
  - EI: Enable Interrupts. This instruction sets the interrupt enable flip-flop, which allows the processor to accept maskable interrupts. Opcode: 11111011, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: FB.
  - DI: Disable Interrupts. This instruction resets the interrupt enable flip-flop, which prevents the processor from accepting maskable interrupts. Opcode: 11110011, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: F3.
  - HLT: Halt. This instruction stops the execution of the program and puts the processor in the idle state. The processor can be restarted by a reset or an interrupt. Opcode: 01110110, Length: 1 byte, M-Cycles: 1, T-States: 7, Hex code: 76.
  - SIM: Set Interrupt Mask. This instruction is used to implement different interrupts of 8085 microprocessor like RST 7.5, 6.5 and 5.5 and also serial data output. It does not affect TRAP interrupt. Opcode: 00110000, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: 30.
  - RIM: Reset Interrupt Mask. This instruction is used to read the status of the interrupts and the serial data input. It does not affect TRAP interrupt. Opcode: 00100000, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex code: 20.
- Some of the assembler directives are:
  - DB: Define Byte. This directive is used for the purpose of allocating and initializing single or multiple data bytes. For example, AREA DB 30H, 52H, 35H allocates three consecutive locations where 30H, 52H and 35H are to be stored .
  - DW: Define Word. This directive is used for the purpose of allocating and initializing single or multiple data words. For example, DATA DW 1234H, 5678H allocates two consecutive words where 1234H and 5678H are to be stored .
  - DS: Define Storage. This directive is used for the purpose of reserving a specified number of bytes or words without initializing them. For example, TEMP DS 10 reserves 10 bytes of memory with the label TEMP .
  - EQU: Equate. This directive is used for the purpose of assigning a value or an expression to a symbol. For example, COUNT EQU 10 assigns the value 10 to the symbol COUNT .
  - ORG: Origin. This directive is used for the purpose of specifying the starting address of the program or a segment. For example, ORG 2000H sets the program counter to 2000H .
  - END: End. This directive is used for the purpose of indicating the end of the source program. For example, END marks the end of the program and optionally specifies the starting address of the program .



## Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The 8086 microprocessor is a 16-bit microprocessor with a 16-bit internal and external data bus. It can access up to 1 MB of memory using 20 address lines .
- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)  .
- The Bus Interface Unit (BIU) interfaces 8086 with the external world. It handles all the data transfer functions. It consists of the following components  :
  - Segment registers: These are four 16-bit registers that store the starting addresses of four memory segments: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES).
  - Instruction pointer: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
  - Address adder: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O device.
  - Instruction queue: This is a 6-byte FIFO buffer that prefetches and stores the instructions from the memory for faster execution by the EU.
- The Execution Unit (EU) executes the instructions fetched by the BIU. It consists of the following components  :
  - General purpose registers: These are eight 16-bit registers that can be used for various arithmetic and logical operations. They are: accumulator (AX), base (BX), counter (CX), data (DX), source index (SI), destination index (DI), stack pointer (SP), and base pointer (BP).
  - Arithmetic and logic unit (ALU): This is a circuit that performs various arithmetic and logical operations on the data stored in the registers or memory.
  - Flag register: This is a 16-bit register that stores the status of the ALU operations and some control bits. It has nine active flags: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF), trap (TF), interrupt enable (IF), direction (DF), and overflow (OF).
  - Control unit: This is a circuit that decodes the instructions fetched by the BIU and generates the appropriate control signals to execute them.
- The memory addressing of the 8086 microprocessor is based on the concept of memory segmentation. The memory is divided into segments of 64 KB each, and each segment has a 16-bit address. The physical address of a memory location is calculated by adding the segment address (multiplied by 16) and the offset address. For example, if the segment address is 1000H and the offset address is 2000H, the physical address is 1000H * 16 + 2000H = 12000H  .
- The operating modes of the 8086 microprocessor are two: minimum mode and maximum mode. In minimum mode, the 8086 operates as a single processor in a system. In maximum mode, the 8086 operates as a master processor in a multiprocessor system  .
- The instruction set of the 8086 microprocessor is a collection of instructions that the 8086 can execute. The instructions are classified into five types: data transfer instructions, arithmetic instructions, logical instructions, control transfer instructions, and string instructions  .
- The instruction format of the 8086 microprocessor is the way the instructions are encoded in binary form. The instruction format consists of one or more bytes, each byte having eight bits. The instruction format has three fields: opcode, operand, and prefix  .
  - Opcode: This is the field that specifies the operation to be performed by the instruction. It can be one or two bytes long.
  - Operand: This is the field that specifies the source and/or destination of the data for the instruction. It can be one, two, or four bytes long



### Architecture of 8086 Microprocessor

- The 8086 is a 16-bit microprocessor with a 16-bit internal and external data bus. It can access up to 1 MB of memory with 20 address lines.
- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and the Execution Unit (EU)  .
- The Bus Interface Unit (BIU) provides the interface of 8086 to external memory and I/O devices via the System Bus. It handles all the data transfer functions  .
- The BIU consists of the following components :
  - Segment registers: These are four 16-bit registers that store the starting addresses of four memory segments: code, data, stack, and extra. Each segment can be up to 64 KB in size.
  - Instruction pointer: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
  - Address adder: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O device.
  - Prefetch unit: This is a circuit that fetches up to six bytes of instructions from the memory and stores them in a queue. It helps to speed up the execution by providing the EU with a continuous stream of instructions.
- The Execution Unit (EU) performs the arithmetic and logical operations on the data. It also controls the flow of the program by executing the instructions  .
- The EU consists of the following components :
  - General purpose registers: These are eight 16-bit registers that can be used for various purposes such as data manipulation, addressing, and temporary storage. They are: AX, BX, CX, DX, SI, DI, BP, and SP. They can also be accessed as 8-bit registers by using their lower or higher halves: AL, AH, BL, BH, CL, CH, DL, and DH.
  - Flag register: This is a 16-bit register that stores the status of the EU after an operation. It has nine flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow. Some of these flags can be set or cleared by the programmer using instructions.
  - Arithmetic and logic unit (ALU): This is a circuit that performs the arithmetic and logical operations on the data. It can operate on 8-bit or 16-bit operands and produce 8-bit or 16-bit results. It also sets or clears the flags according to the outcome of the operation.
  - Control unit: This is a circuit that decodes the instructions fetched by the BIU and generates the control signals to execute them. It also handles the interrupts and exceptions that may occur during the execution.
- The 8086 microprocessor has three operating modes: minimum mode, maximum mode, and halt mode.
  - Minimum mode: This is the mode in which the 8086 operates as a single processor in a system. It uses the MN/MX pin to select this mode. In this mode, the 8086 generates all the control signals for the memory and I/O devices. It also uses the BHE/S7 pin to indicate whether the data bus is accessing the lower or higher byte of a word.
  - Maximum mode: This is the mode in which the 8086 operates as a master processor in a multiprocessor system. It uses the MN/MX pin to select this mode. In this mode, the 8086 relinquishes some of the control signals to an external coprocessor such as the 8087 or the 8089. It also uses the S0, S1, and S2 pins to indicate the status of the current bus cycle.
  - Halt mode: This is the mode in which the 8086 stops executing instructions and enters a low-power state. It uses the HLT instruction to enter this mode. In this mode, the 8086 can only be restarted by a reset or an interrupt signal.
- The 8086 microprocessor has a rich instruction set that can be classified into the following types:
  - Data transfer instructions: These are the instructions that move data between registers, memory, and I/O devices.



### Register Organization for the Notes of the Unit 3 - Architecture of 8086 Microprocessor

- The 8086 microprocessor has 14 internal registers that are accessible to the programmer .
- The registers are divided into four groups: general-purpose registers, segment registers, pointer and index registers, and instruction pointer and flags register.
- Each register is 16 bits wide and can store one word (two bytes) of data .
- Some registers can be further divided into two 8-bit registers to perform byte operations .
- The register organization of the 8086 microprocessor is also known as the programmer's model.

#### General-Purpose Registers

- The general-purpose registers are AX, BX, CX, and DX  .
- They can be used to store temporary data, operands, and results of arithmetic and logical operations.
- They can also be used as base or index registers for memory addressing.
- Each general-purpose register can be split into two 8-bit registers: AH and AL for AX, BH and BL for BX, CH and CL for CX, and DH and DL for DX .
- AX is the accumulator register and is used for input/output operations, multiplication, division, and some string operations.
- BX is the base register and is used as a base pointer for memory access.
- CX is the count register and is used as a loop counter and for shift and rotate operations.
- DX is the data register and is used for input/output operations, multiplication, division, and some string operations.

#### Segment Registers

- The segment registers are CS, DS, SS, and ES  .
- They are used to define the memory segments for code, data, stack, and extra data respectively.
- They store the 16-bit segment addresses of the memory segments.
- Each segment address is multiplied by 16 (shifted left by 4 bits) to form the 20-bit physical address of the memory location.
- The segment registers cannot be used for arithmetic or logical operations.

#### Pointer and Index Registers

- The pointer and index registers are SP, BP, SI, and DI  .
- They are used to store the offsets of memory locations within the segments defined by the segment registers.
- They can also be used for arithmetic and logical operations.
- SP is the stack pointer and points to the top of the stack segment.
- BP is the base pointer and is used as a base pointer for memory access in the stack segment.
- SI is the source index and is used as a source pointer for string operations.
- DI is the destination index and is used as a destination pointer for string operations.

#### Instruction Pointer and Flags Register

- The instruction pointer (IP) and the flags register are two special registers that are not directly accessible to the programmer .
- IP is a 16-bit register that stores the offset of the next instruction to be executed within the code segment.
- The flags register is a 16-bit register that stores the status and control flags of the microprocessor.
- The flags register has 9 implemented bits: carry flag (CF), parity flag (PF), auxiliary carry flag (AF), zero flag (ZF), sign flag (SF), trap flag (TF), interrupt enable flag (IF), direction flag (DF), and overflow flag (OF).
- The flags register can be manipulated by some instructions such as CLC, STC, CLI, STI, CLD, STD, etc.

: https://www.electronicsmind.com/registers-in-8086-microprocessor/
: https://benchpartner.com/register-organization-of-8086
: https://8086up.wordpress.com/2014/03/05/register-organization-of-8086/
: https://www.geeksforgeeks.org/general-purpose-registers-8086-microprocessor/
: https://www.geeksforgeeks.org/architecture-of-8086/



### Bus Interface Unit

- The bus interface unit (BIU) is one of the two sections of the 8086 microprocessor architecture. The other section is the execution unit (EU).
- The BIU provides the interface of 8086 to external memory and I/O devices via the system bus. It handles all the data transfer functions.
- The BIU performs read and write operations on data in the memory and on the external devices connected to the ports of the microprocessor, and it also sends out addresses.
- The BIU contains four 16-bit special purpose registers called as segment registers. They are code segment register (CS), data segment register (DS), stack segment register (SS), and extra segment register (ES).
- The segment registers are used for memory segmentation, which is a technique to divide the memory into logical segments of 64 KB each. Each segment register holds the base address of one of the segments.
- The BIU also contains a 16-bit instruction pointer (IP) register, which holds the offset address of the next instruction to be executed within the code segment.
- The BIU also contains a 6-byte instruction queue, which prefetches and stores the instructions from the memory before they are executed by the EU. This increases the speed of execution and allows pipelining.
- The BIU uses three different buses to transfer data and instructions between the microprocessor and other components in a computer system. They are address bus, data bus, and control bus.
- The address bus is used to send the memory address of the instruction or data being read or written. It is 20-bit wide and can address up to 1 MB of memory.
- The data bus is used to transfer the actual data or instructions between the microprocessor and the memory or I/O devices. It is 16-bit wide and can transfer one word (16 bits) at a time.
- The control bus is used to send the control signals that synchronize the operations of the microprocessor and the external devices. It consists of various signals such as read, write, interrupt, etc.



### Execution Unit (EU) of 8086 Microprocessor

- The execution unit (EU) is responsible for decoding and executing the instructions fetched by the bus interface unit (BIU) from the memory or I/O devices  .
- The EU consists of the following components :
  - Arithmetic and Logic Unit (ALU): It performs arithmetic and logical operations on 8-bit or 16-bit data. It also updates the status flags according to the result of the operation.
  - General Purpose Registers: There are eight 16-bit registers that can be used for storing data, addresses, or operands. They are AX, BX, CX, DX, SI, DI, BP, and SP. Some of them can be accessed as two 8-bit registers, such as AH and AL for AX, BH and BL for BX, etc.
  - Segment Registers: There are four 16-bit registers that store the segment addresses of the memory. They are CS (code segment), DS (data segment), SS (stack segment), and ES (extra segment).
  - Instruction Pointer (IP): It holds the offset address of the next instruction to be executed within the current code segment.
  - Flag Register: It is a 16-bit register that contains nine status flags that indicate the status of the result of the last operation. They are CF (carry flag), PF (parity flag), AF (auxiliary carry flag), ZF (zero flag), SF (sign flag), TF (trap flag), IF (interrupt flag), DF (direction flag), and OF (overflow flag).
- The EU communicates with the BIU through an internal 16-bit bus called the EU-BIU interface . The EU sends requests to the BIU to fetch instructions or data from the memory or I/O devices, and the BIU transfers them to the EU when they are available. The EU also sends the results of the operations to the BIU to store them in the memory or I/O devices.
- The EU operates independently of the BIU, which means that it can execute instructions while the BIU is fetching the next instruction or data . This is called pipelining and it increases the speed and efficiency of the microprocessor. However, the EU has to wait for the BIU if the required instruction or data is not available in the queue.



### Memory Addressing for the Notes of the Unit 3 - Architecture of 8086 Microprocessor

- The 8086 microprocessor is a 16-bit processor that can address up to 1 MB of memory using 20 address lines .
- The memory is divided into segments of 64 KB each, and each segment has a starting address called the segment base address.
- The 8086 microprocessor has four segment registers: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES). These registers store the upper 16 bits of the segment base addresses.
- The lower 16 bits of the memory address are called the offset or displacement, and they are specified by an instruction operand or an index register .
- The memory address is calculated by adding the segment base address and the offset, and shifting the result left by four bits. This is called the physical address or the effective address .
- The 8086 microprocessor has seven addressing modes: register, immediate, direct, register indirect, based, indexed, and based indexed .
- In register addressing mode, the operands are stored in the registers, and no memory access is required.
- In immediate addressing mode, the operand is specified as a constant value in the instruction, and no memory access is required.
- In direct addressing mode, the offset of the operand is specified in the instruction, and the segment base address is taken from the default segment register (DS for data, CS for code, SS for stack).
- In register indirect addressing mode, the offset of the operand is stored in an index register (BX, SI, DI, or BP), and the segment base address is taken from the default segment register.
- In based addressing mode, the offset of the operand is stored in a base register (BX or BP), and the segment base address is taken from the corresponding segment register (DS for BX, SS for BP).
- In indexed addressing mode, the offset of the operand is stored in an index register (SI or DI), and the segment base address is taken from the default segment register.
- In based indexed addressing mode, the offset of the operand is the sum of a base register (BX or BP) and an index register (SI or DI), and the segment base address is taken from the corresponding segment register (DS for BX, SS for BP).
- The 8086 microprocessor can operate in two modes: minimum mode and maximum mode. In minimum mode, the 8086 is the only processor in the system, and it generates all the control signals. In maximum mode, the 8086 is part of a multiprocessor system, and it uses an external bus controller to generate the control signals.
- The 8086 microprocessor has three types of instruction sets: data transfer, arithmetic and logic, and control transfer.
- The 8086 microprocessor has three types of instruction formats: one-byte, two-byte, and three-byte. The one-byte format consists of an opcode only. The two-byte format consists of an opcode and a single operand. The three-byte format consists of an opcode and two operands.
- The 8086 microprocessor has four types of instructions: register to/from register, register to/from memory, immediate to register/memory, and memory to memory.
- The 8086 microprocessor has two types of interrupts: hardware and software. Hardware interrupts are generated by external devices, and they are handled by an interrupt controller. Software interrupts are generated by the program, and they are handled by an interrupt vector table.



### Memory Segmentation

- Memory segmentation is a technique that allows the 8086 microprocessor to access more than 64 KB of memory by dividing the memory into segments of 64 KB each.
- The 8086 microprocessor has a 20-bit address bus, which means it can address 1 MB (2^20) of memory. However, its internal registers are only 16-bit, which means they can only hold values up to 65,536 (2^16).
- To overcome this limitation, the 8086 microprocessor uses four segment registers: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES). These registers store the upper 16 bits of the starting addresses of the four memory segments that the 8086 microprocessor is currently working with.
- The lower 16 bits of the memory address are stored in the offset registers: instruction pointer (IP), base pointer (BP), source index (SI), and destination index (DI). These registers are used to specify the location of the instruction, data, or stack within the segment.
- The physical address (also called the effective address) of a memory location is calculated by adding the segment address and the offset address. For example, if CS = 1000H and IP = 2000H, then the physical address of the next instruction is 1000H * 10H + 2000H = 12000H.
- The 8086 microprocessor can access four types of memory segments: code segment, data segment, stack segment, and extra segment. The code segment contains the instructions to be executed. The data segment contains the data to be manipulated. The stack segment contains the stack data structure for storing temporary data and return addresses. The extra segment is used for additional data storage or for accessing memory outside the current data segment.
- The 8086 microprocessor can switch between different memory segments by changing the values of the segment registers. However, it can only work with four segments at a time, and each segment can be up to 64 KB in size. This limits the amount of memory that can be accessed by a single program.



### Operating modes for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The 8086 microprocessor is a 16-bit, N-channel, HMOS microprocessor that can operate in two modes: minimum mode and maximum mode.
- In minimum mode, the 8086 is the only processor in the system and provides all the control signals for memory and I/O interfacing. This mode is suitable for single-processor systems with simple hardware and software requirements.
- In maximum mode, the 8086 can coexist with other processors such as 8087, 8089, or 8088 and uses a bus controller chip (8288) to generate the control signals. This mode is suitable for multiprocessor systems with complex hardware and software requirements.
- The 8086 has a register organization that consists of four 16-bit general-purpose registers (AX, BX, CX, DX), four 16-bit segment registers (CS, DS, SS, ES), four 16-bit pointer and index registers (SP, BP, SI, DI), a 16-bit instruction pointer (IP), and a 16-bit flag register (FLAGS).
- The bus interface unit (BIU) of the 8086 is responsible for fetching instructions from memory, generating physical addresses, and interfacing with external devices. The BIU contains a 6-byte instruction queue that prefetches instructions from memory and stores them for execution by the execution unit (EU).
- The execution unit (EU) of the 8086 is responsible for decoding and executing instructions, performing arithmetic and logical operations, and manipulating data and flags. The EU communicates with the BIU through an internal bus and uses the registers for temporary storage of data and operands.
- The 8086 has a 20-bit address bus that can address up to 1 MB of memory. The memory is divided into segments of 64 KB each, and each segment has a base address and an offset address. The base address is stored in one of the segment registers, and the offset address is specified by the instruction or the pointer and index registers.
- The memory addressing modes of the 8086 are: direct, register indirect, based, indexed, based indexed, and relative. These modes allow the 8086 to access data from different locations in memory using different combinations of registers and operands.
- The memory segmentation of the 8086 allows the 8086 to access different types of data and code in different segments of memory. The four segment registers are used to access four types of segments: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES). The CS register holds the base address of the code segment, where the instructions are stored. The IP register holds the offset address of the next instruction to be executed. The DS register holds the base address of the data segment, where the data variables are stored. The SS register holds the base address of the stack segment, where the stack data are stored. The SP register holds the offset address of the top of the stack. The ES register holds the base address of the extra segment, where additional data can be stored.
- The 8086 has two types of operating modes: real mode and virtual 8086 mode. In real mode, the 8086 operates as a 16-bit processor with a 20-bit address bus and can access up to 1 MB of memory. In real mode, the segment registers are used to generate the physical address by shifting the segment register value by 4 bits to the left and adding the offset value. In virtual 8086 mode, the 8086 operates as a virtual 8086 processor within a protected mode operating system. In virtual 8086 mode, the 8086 can execute real mode applications that are incompatible with protected mode, while the operating system provides protection and isolation for the virtual 8086 processor.
- The instruction set of the 8086 consists of various types of instructions that can perform different operations on data and control the flow of execution. The types of instructions are: data transfer instructions, arithmetic instructions, logical instructions, shift and rotate instructions, string instructions, branch



### Instruction sets for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)   .
- The BIU interfaces the 8086 with the external world and handles all the data transfer functions. It consists of the following components   :
  - A 16-bit data bus that can transfer 16 bits of data at a time.
  - A 20-bit address bus that can access up to 1 MB of memory.
  - Four 16-bit segment registers: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES) that store the base addresses of the four memory segments.
  - An instruction pointer (IP) that points to the next instruction to be executed in the code segment.
  - A 6-byte instruction queue that prefetches and stores the instructions from the code segment.
- The EU executes the instructions fetched by the BIU and performs the arithmetic and logical operations. It consists of the following components   :
  - An arithmetic and logic unit (ALU) that performs 8-bit and 16-bit arithmetic and logical operations.
  - A flag register that contains 9 flags that indicate the status of the ALU operations and control the program flow.
  - Four 16-bit general purpose registers: accumulator (AX), base (BX), counter (CX), and data (DX) that can be used as 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL) or as 16-bit registers (AX, BX, CX, DX).
  - Two 16-bit index registers: source index (SI) and destination index (DI) that are used for string operations and memory addressing.
  - A 16-bit stack pointer (SP) that points to the top of the stack in the stack segment.
  - A 16-bit base pointer (BP) that is used for accessing parameters and local variables in the stack segment.
- The memory addressing of the 8086 microprocessor is based on the concept of memory segmentation. The memory is divided into four segments: code, data, stack, and extra. Each segment has a base address stored in the corresponding segment register and a maximum size of 64 KB. The physical address of a memory location is calculated by adding the base address of the segment and the offset address of the location. The offset address can be specified by using one of the following addressing modes   :
  - Immediate addressing mode: the operand is a constant value that is part of the instruction.
  - Register addressing mode: the operand is stored in one of the registers.
  - Direct addressing mode: the operand is stored in a memory location whose offset address is given in the instruction.
  - Register indirect addressing mode: the operand is stored in a memory location whose offset address is stored in one of the index registers (SI or DI).
  - Based addressing mode: the operand is stored in a memory location whose offset address is the sum of the contents of one of the base registers (BX or BP) and a displacement value given in the instruction.
  - Indexed addressing mode: the operand is stored in a memory location whose offset address is the sum of the contents of one of the index registers (SI or DI) and a displacement value given in the instruction.
  - Based indexed addressing mode: the operand is stored in a memory location whose offset address is the sum of the contents of one of the base registers (BX or BP), one of the index registers (SI or DI), and a displacement value given in the instruction.
- The operating modes of the 8086 microprocessor are the minimum mode and the maximum mode. In the minimum mode, the 8086 operates as a single processor in a system and uses the control signals generated by itself. In the maximum mode, the 8086 operates as a master processor in a multiprocessor system and uses the control signals generated by an external coprocessor   .
- The instruction set of the



### Instruction format for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts. in the subject of Microprocessor KCS

- Register organization: The 8086 microprocessor has 14 registers, each of 16 bits. They are divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register.
  - General-purpose registers: These are AX, BX, CX, and DX. They can be used for arithmetic, logic, data transfer, and other operations. They can also be accessed as 8-bit registers by using their high (H) and low (L) bytes. For example, AX can be accessed as AH and AL.
  - Segment registers: These are CS, DS, SS, and ES. They are used to hold the segment addresses of the code, data, stack, and extra segments, respectively. Each segment register can store a 16-bit value, which is multiplied by 16 to form a 20-bit physical address of the segment.
  - Pointer and index registers: These are SP, BP, SI, and DI. They are used to hold the offsets of the stack, base, source, and destination, respectively. They can be used for addressing data in the memory or for performing arithmetic operations.
  - Flag register: This is a 16-bit register that holds the status of the 8086 microprocessor. It has 9 flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow. Each flag is a single bit that indicates the result of the last operation or the state of the microprocessor.
- Bus interface unit (BIU): This is the part of the 8086 microprocessor that handles the communication with the external devices, such as memory and I/O ports. It has four main functions: fetching instructions from the memory, generating physical addresses for memory access, performing bus arbitration, and providing a prefetch queue for storing the fetched instructions.
  - Instruction fetch: The BIU fetches the instructions from the memory using the CS and IP registers. The CS register holds the segment address of the code, and the IP register holds the offset of the instruction. The BIU combines them to form a 20-bit physical address, which is sent to the memory. The BIU then reads the instruction from the memory and stores it in the prefetch queue.
  - Address generation: The BIU generates the physical addresses for memory access using the segment and offset registers. The segment register can be one of the four segment registers (CS, DS, SS, or ES), depending on the type of memory access. The offset register can be one of the pointer or index registers (SP, BP, SI, or DI), or an immediate or displacement value, depending on the addressing mode. The BIU combines them to form a 20-bit physical address, which is sent to the memory.
  - Bus arbitration: The BIU performs the bus arbitration to ensure that only one device can access the bus at a time. The BIU has two signals: BREQ (bus request) and HLDA (hold acknowledge). The BREQ signal is used by the external devices to request the bus from the BIU. The HLDA signal is used by the BIU to acknowledge the bus request and to release the bus to the external device. The BIU can also request the bus from the external device by using the BREQ signal.
  - Prefetch queue: The BIU has a prefetch queue that can store up to six bytes of instructions. The BIU fetches the instructions from the memory and stores them in the prefetch queue in advance, before they are executed by the execution unit. This improves the performance of the 8086 microprocessor by reducing the wait states and increasing the instruction throughput.
- Execution unit (EU): This is the part of the 8086 microprocessor that executes the instructions fetched by the BIU. It has four main functions: decoding the instructions, accessing the registers, performing the arithmetic and logic operations, and updating the flags and the IP register.
  - Instruction decode: The EU decodes the instructions from the prefetch queue and determines the operation code, the operands, and the addressing mode. The EU then sends the appropriate control signals to the BIU, the registers, and the ALU to execute the instruction.
  - Register access: The EU accesses the registers to read or write the operands for the instruction. The EU can access the general-purpose registers, the segment registers, the pointer and index registers, and the flag register. The EU can also access the



### Types of instructions for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The 8086 microprocessor supports **8 types** of instructions:
  - Data Transfer Instructions: These instructions are used to transfer the data from the source operand to the destination operand. Examples are MOV, PUSH, POP, XCHG, etc.
  - Arithmetic Instructions: These instructions are used to perform arithmetic operations like addition, subtraction, multiplication, division, increment or decrement. Examples are ADD, SUB, MUL, DIV, INC, DEC, etc.
  - Bit Manipulation Instructions: These instructions are used to manipulate the individual bits of the operands. Examples are AND, OR, XOR, NOT, TEST, etc.
  - String Manipulation Instructions: These instructions are used to perform operations on strings of data. Examples are REP, MOVS, CMPS, SCAS, LODS, STOS, etc.
  - Program Execution Transfer Instructions: These instructions are used to change the sequence of execution of the program. Examples are JMP, CALL, RET, JZ, JNZ, JC, JNC, etc.
  - Processor Control Instructions: These instructions are used to control the operation of the processor. Examples are HLT, NOP, WAIT, LOCK, etc.
  - Shift and Rotate Instructions: These instructions are used to shift or rotate the bits of the operands. Examples are SHL, SHR, SAL, SAR, ROL, ROR, RCL, RCR, etc.
  - Loop Instructions: These instructions are used to repeat a block of code for a specified number of times or until a condition is met. Examples are LOOP, LOOPE, LOOPNE, LOOPZ, LOOPNZ, etc.

- The instruction set of 8086 microprocessor can be classified into **5 groups** based on the function they perform:
  - Data Transfer Instruction: This group includes the instructions used for moving the data from one place to another. The data can be transferred between registers, memory, and I/O ports. The data can be 8-bit or 16-bit depending on the operands. The format of the data transfer instruction is:

    ```
    Mnemonic    Destination, Source
    ```

    The destination can be a register or a memory location, and the source can be a register, a memory location, an immediate data, or an I/O port. The data transfer instruction does not affect any flag.

  - Arithmetic Instructions: This group includes the instructions used for executing arithmetic operations like addition, subtraction, multiplication, division, increment or decrement. The arithmetic instructions can operate on 8-bit or 16-bit operands depending on the operands. The format of the arithmetic instruction is:

    ```
    Mnemonic    Destination, Source
    ```

    The destination can be a register or a memory location, and the source can be a register, a memory location, or an immediate data. The arithmetic instructions affect the flags of the 8086 microprocessor, which reflect the status of the result of the operations.

  - Logical Instructions: This group includes the instructions used for performing logical operations on the operands. The logical operations are AND, OR, XOR, and NOT. The logical instructions can operate on 8-bit or 16-bit operands depending on the operands. The format of the logical instruction is:

    ```
    Mnemonic    Destination, Source
    ```

    The destination can be a register or a memory location, and the source can be a register, a memory location, or an immediate data. The logical instructions affect the flags of the 8086 microprocessor, which reflect the status of the result of the operations.

  - String Manipulation Instruction: This group includes the instructions used for performing operations on strings of data. The string manipulation instructions use the following registers to access the strings:

    - SI: Source Index register, which points to the source string in the memory.
    - DI: Destination Index register, which points to the destination string in the memory.
    - CX: Count register, which stores the number of bytes or words to be processed.
    - DF: Direction flag, which determines the direction of the string processing. If DF = 0, the string is processed from lower address to higher address. If DF = 1, the string is processed from higher address to lower address.

    The string manipulation instructions can operate on byte strings or word strings depending on the



### Interrupts

- Interrupts are signals that cause the microprocessor to suspend its current operation and execute a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are caused by external devices that send a signal to the microprocessor through a dedicated pin. Software interrupts are caused by instructions executed by the microprocessor.
- The 8086 microprocessor has two hardware interrupt pins: NMI (Non-Maskable Interrupt) and INTR (Interrupt Request).
  - NMI is a high-priority interrupt that cannot be disabled or ignored by the microprocessor. It is used for critical events that require immediate attention, such as power failure or parity error.
  - INTR is a low-priority interrupt that can be enabled or disabled by the microprocessor using the interrupt enable (IF) flag in the flags register. It is used for normal events that can be handled at a convenient time, such as keyboard input or disk access.
- The 8086 microprocessor has 256 types of software interrupts, numbered from 0 to 255. Each type of interrupt has a corresponding ISR that is stored in a table called the Interrupt Vector Table (IVT).
  - The IVT is located in the memory address range from 0x0000 to 0x03FF. Each entry in the IVT is 4 bytes long and contains the segment and offset address of the ISR for that interrupt type.
  - The interrupt type number is multiplied by 4 to get the offset of the IVT entry for that interrupt. For example, the IVT entry for interrupt type 10h is at offset 40h in the IVT.
  - When a software interrupt is executed, the microprocessor pushes the flags register, the code segment register, and the instruction pointer register onto the stack, and then jumps to the ISR address stored in the IVT entry for that interrupt type.
  - When the ISR is completed, the microprocessor executes an IRET (Interrupt Return) instruction, which pops the instruction pointer, the code segment, and the flags register from the stack, and resumes the interrupted program.
- Some of the software interrupts are predefined by Intel and have specific functions. For example, interrupt type 21h is used for DOS services, such as file operations, input/output operations, memory allocation, etc.



### Hardware and Software Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current task and execute a special subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are caused by external devices that send a signal to the microprocessor through a dedicated pin. Software interrupts are caused by instructions in the program that generate a software interrupt request to the microprocessor.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR. NMI stands for non-maskable interrupt and INTR stands for maskable interrupt.
- NMI has a higher priority than INTR and cannot be disabled by the microprocessor. It is used for critical events such as power failure or memory parity error.
- INTR can be enabled or disabled by the microprocessor using the EI (enable interrupt) and DI (disable interrupt) instructions. It is used for normal events such as keyboard input or timer output.
- The 8086 microprocessor has 256 software interrupts, numbered from 0 to 255. Each software interrupt has a corresponding interrupt vector, which is a 4-byte address that points to the ISR in memory.
- The software interrupts are invoked by the INT instruction, which takes an 8-bit operand that specifies the interrupt number. For example, INT 21H invokes the software interrupt 21H, which is used for DOS services.
- When an interrupt occurs, the microprocessor performs the following steps:
  - It saves the current flags register and the current code segment (CS) and instruction pointer (IP) registers on the stack.
  - It disables further interrupts by clearing the interrupt enable (IF) flag in the flags register.
  - It calculates the interrupt vector address by multiplying the interrupt number by 4. For example, the interrupt vector address for interrupt 21H is 21H x 4 = 84H.
  - It fetches the ISR address from the interrupt vector address and loads it into the CS and IP registers.
  - It executes the ISR until it encounters an IRET (interrupt return) instruction, which returns the control to the interrupted program.
  - It restores the flags register and the CS and IP registers from the stack.
  - It enables further interrupts by setting the IF flag in the flags register.



## Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that a microprocessor can execute.
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that has 74 instructions and 246 opcodes. It has a 16-bit address bus and an 8-bit data bus.
- 8086 is a 16-bit microprocessor that has 133 instructions and 255 opcodes. It has a 20-bit address bus and a 16-bit data bus.
- The instructions in assembly language can be classified into the following categories :
  - Data transfer instructions: These are used to move data between registers, memory and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These are used to perform arithmetic operations on data. Examples are ADD, SUB, INR, DCR, ADC, SBB, etc.
  - Logic instructions: These are used to perform logical operations on data. Examples are AND, OR, XOR, NOT, CMP, etc.
  - Branch instructions: These are used to alter the sequence of execution based on certain conditions. Examples are JMP, JC, JNC, JZ, JNZ, etc.
  - Looping instructions: These are used to repeat a block of instructions until a condition is met. Examples are LOOP, LOOPE, LOOPNE, etc.
  - Counting instructions: These are used to increment or decrement a register or a memory location by one. Examples are INC, DEC, etc.
  - Indexing instructions: These are used to access data in memory using an index register. Examples are LEA, LDS, LES, etc.
  - Programming techniques: These are used to implement various algorithms and data structures using assembly language. Examples are sorting, searching, stack, queue, etc.
  - Counters and time delays: These are used to generate a specific number of clock cycles or a specific duration of time using assembly language. Examples are NOP, HLT, DELAY, etc.
  - Stacks and subroutines: These are used to implement the concept of stack and subroutine in assembly language. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are used to call or return from a subroutine based on certain conditions. Examples are CC, CNC, CZ, CNZ, etc.



### Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that a microprocessor can execute  .
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that has 74 instructions, 246 opcodes, 5 addressing modes, and a 16-bit address bus  .
- 8086 is a 16-bit microprocessor that has 133 instructions, 255 opcodes, 12 addressing modes, and a 20-bit address bus .
- The instructions of 8085 and 8086 can be classified into the following categories   :
  - Data transfer instructions: These are used to move data between registers, memory, and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These are used to perform arithmetic operations on data such as addition, subtraction, multiplication, division, increment, and decrement. Examples are ADD, SUB, MUL, DIV, INR, DCR, etc.
  - Logic instructions: These are used to perform logical operations on data such as AND, OR, XOR, NOT, complement, shift, and rotate. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branch instructions: These are used to alter the sequence of execution of the program based on certain conditions such as flags, registers, or memory contents. Examples are JMP, JZ, JNZ, JC, JNC, CALL, RET, etc.
  - Looping instructions: These are used to repeat a block of instructions for a specified number of times or until a condition is met. Examples are LOOP, LOOPE, LOOPNE, etc.
  - Counting instructions: These are used to increment or decrement a register or a memory location by a constant value. Examples are INX, DCX, etc.
  - Indexing instructions: These are used to access data from an array or a table using an index register. Examples are LXI, LDAX, STAX, etc.
  - Programming techniques: These are used to implement various algorithms and data structures using the instructions of the microprocessor. Examples are sorting, searching, string manipulation, stack implementation, etc.
  - Counters and time delays: These are used to generate a specific duration of time by executing a loop of instructions for a calculated number of times. Examples are using register pairs as counters, using timer/counter devices, etc.
  - Stacks and subroutines: These are used to store and retrieve data or return addresses from a memory area called stack using push and pop operations. Subroutines are blocks of instructions that can be called from the main program using call and return instructions. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are used to call or return from a subroutine based on certain conditions such as flags, registers, or memory contents. Examples are CC, CNC, CZ, CNZ, etc.



### Instructions for the notes of the Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level programming language that is specific to a given processor. It uses mnemonics to represent the binary instructions that the microprocessor can execute. 
- The intel 8085 and 8086 are popular 8-bit and 16-bit microprocessors respectively, that are used widely across the world to introduce students to microprocessor concepts and assembly language programming. 
- The intel 8085 and 8086 have different architectures, registers, instruction sets, addressing modes, and memory models. Therefore, the assembly language programs written for one microprocessor may not work on the other.
- The intel 8085 and 8086 assembly language programs consist of the following components:
  - A label, which is an optional identifier for a memory location or a program segment. It is followed by a colon (:).
  - An instruction, which is a mnemonic that represents an operation code (opcode) and one or more operands. The operands can be registers, memory addresses, data values, or labels. The instruction is followed by a semicolon (;).
  - A comment, which is an optional explanation or remark for the program. It is preceded by a semicolon (;).
  - A directive, which is a command to the assembler that controls the assembly process, such as defining constants, variables, macros, segments, etc. It is preceded by a dot (.).
- The intel 8085 and 8086 assembly language programs can be classified into the following categories based on the type of instructions they use:
  - Data transfer instructions, which are used to move data between registers, memory, and input/output devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions, which are used to perform arithmetic operations on data, such as addition, subtraction, multiplication, division, increment, decrement, etc. Examples are ADD, SUB, MUL, DIV, INR, DCR, etc.
  - Logic instructions, which are used to perform logical operations on data, such as AND, OR, XOR, NOT, complement, shift, rotate, etc. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branch instructions, which are used to alter the sequence of execution of the program based on certain conditions, such as jump, call, return, etc. Examples are JMP, JC, JNC, JZ, JNZ, CALL, RET, etc.
  - Looping instructions, which are used to repeat a block of code for a specified number of times or until a condition is met. Examples are LOOP, LOOPE, LOOPNE, etc.
  - Counting instructions, which are used to manipulate the contents of a register or a memory location as a counter. Examples are INX, DCX, LXI, etc.
  - Indexing instructions, which are used to access data in memory using an index register. Examples are LDAX, STAX, etc.
  - Programming techniques, which are used to improve the efficiency, readability, and maintainability of the program, such as using subroutines, macros, comments, labels, directives, etc.
  - Counters and time delays, which are used to generate a specific duration of time or a specific number of pulses using a loop or a counter. Examples are DELAY, COUNT, etc.
  - Stacks and subroutines, which are used to store and retrieve data or return addresses using a special memory area called the stack. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions, which are used to call or return from a subroutine based on certain conditions, such as CC, CNC, CZ, CNZ, etc.



### Data Transfer Instructions in 8085 Microprocessor

- Data transfer instructions are the instructions that are used to transfer data between registers, memory and I/O devices in the 8085 microprocessor.
- Data transfer instructions can be classified into four categories: register to register, register to memory, memory to register and I/O to register or register to I/O.
- Data transfer instructions do not affect the flags in the 8085 microprocessor, except for the IN and OUT instructions, which affect the parity flag.
- Data transfer instructions have different formats and opcodes depending on the source and destination operands. The following table shows some examples of data transfer instructions and their formats :

| Instruction | Opcode | Format | Description |
| --- | --- | --- | --- |
| MOV r1, r2 | 01DDDSSS | MOV destination, source | Copies the contents of the source register to the destination register |
| MVI r, data | 00DDD110 | MVI destination, data | Loads the 8-bit data into the destination register |
| LDA addr | 00111010 | LDA address | Loads the accumulator with the contents of the memory location specified by the 16-bit address |
| STA addr | 00110010 | STA address | Stores the contents of the accumulator into the memory location specified by the 16-bit address |
| LHLD addr | 00101010 | LHLD address | Loads the H and L registers with the contents of the memory locations specified by the 16-bit address and the next address |
| SHLD addr | 00100010 | SHLD address | Stores the contents of the H and L registers into the memory locations specified by the 16-bit address and the next address |
| LXI rp, data | 00RP0001 | LXI register pair, data | Loads the register pair with the 16-bit data |
| LDAX rp | 00RP1010 | LDAX register pair | Loads the accumulator with the contents of the memory location pointed by the register pair |
| STAX rp | 00RP0010 | STAX register pair | Stores the contents of the accumulator into the memory location pointed by the register pair |
| XCHG | 11101011 | XCHG | Exchanges the contents of the H and L registers with the contents of the D and E registers |
| IN port | 11011011 | IN port | Reads the data from the input port specified by the 8-bit port address and loads it into the accumulator |
| OUT port | 11010011 | OUT port | Writes the data from the accumulator to the output port specified by the 8-bit port address |

- Data transfer instructions are essential for performing various operations on data, such as arithmetic, logic, branch and looping operations, in the 8085 microprocessor.



### Arithmetic Instructions in 8085 Microprocessor

- Arithmetic instructions are the instructions that perform basic arithmetic operations such as addition, subtraction, increment, and decrement on the data stored in the registers or memory locations.
- The destination operand of these instructions is generally the accumulator, which holds the result of the operation.
- The source operand can be a register, a memory location, or an immediate data.
- The arithmetic instructions affect the flags according to the result of the operation. The flags that are affected are sign, zero, auxiliary carry, parity, and carry flags.
- The arithmetic instructions can be classified into four categories: addition, subtraction, increment, and decrement.

#### Addition Instructions

- The addition instructions perform the addition of two 8-bit or 16-bit operands and store the result in the accumulator or a register pair.
- The addition instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| ADD r | Add the contents of register r to the accumulator | ADD B |
| ADD M | Add the contents of memory location pointed by HL pair to the accumulator | ADD M |
| ADI data | Add the 8-bit immediate data to the accumulator | ADI 25H |
| ADC r | Add the contents of register r and the carry flag to the accumulator | ADC C |
| ADC M | Add the contents of memory location pointed by HL pair and the carry flag to the accumulator | ADC M |
| ACI data | Add the 8-bit immediate data and the carry flag to the accumulator | ACI 12H |
| DAD rp | Add the contents of register pair rp to the HL pair | DAD BC |

#### Subtraction Instructions

- The subtraction instructions perform the subtraction of two 8-bit or 16-bit operands and store the result in the accumulator or a register pair.
- The subtraction instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| SUB r | Subtract the contents of register r from the accumulator | SUB D |
| SUB M | Subtract the contents of memory location pointed by HL pair from the accumulator | SUB M |
| SUI data | Subtract the 8-bit immediate data from the accumulator | SUI 34H |
| SBB r | Subtract the contents of register r and the borrow (complement of carry) from the accumulator | SBB E |
| SBB M | Subtract the contents of memory location pointed by HL pair and the borrow from the accumulator | SBB M |
| SBI data | Subtract the 8-bit immediate data and the borrow from the accumulator | SBI 16H |

#### Increment Instructions

- The increment instructions perform the increment of an 8-bit or a 16-bit operand by one and store the result in the same operand.
- The increment instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| INR r | Increment the contents of register r by one | INR A |
| INR M | Increment the contents of memory location pointed by HL pair by one | INR M |
| INX rp | Increment the contents of register pair rp by one | INX SP |

#### Decrement Instructions

- The decrement instructions perform the decrement of an 8-bit or a 16-bit operand by one and store the result in the same operand.
- The decrement instructions are:

| Mnemonic | Description | Example |
| --- | --- | --- |
| DCR r | Decrement the contents of register r by one | DCR H |
| DCR M | Decrement the contents of memory location pointed by HL pair by one | DCR M |
| DCX rp | Decrement the contents of register pair rp by one | DCX DE |



### Logic for the notes of the Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level programming language that uses mnemonics to represent machine instructions .
- Assembly language is specific to a given processor, so the assembly language of 8085 is different from that of 8086 or Motorola 6800 .
- The microprocessor cannot understand a program written in assembly language, so a program known as assembler is used to convert an assembly language program to machine code .
- Assembly language programming of 8085/8086 involves the following steps:
  - Writing the source code in a text editor
  - Saving the source code with an extension .asm
  - Assembling the source code using an assembler
  - Linking the object code with any libraries or modules
  - Loading the executable code into the memory
  - Running the program and debugging if necessary
- Assembly language programming of 8085/8086 requires the knowledge of the following concepts:
  - Instructions: The basic commands that the microprocessor can execute, such as data transfer, arithmetic, logic, branch, loop, etc.
  - Operands: The data or addresses that the instructions operate on, such as registers, memory locations, immediate values, etc.
  - Labels: The symbolic names that represent the addresses of instructions or data, such as START, LOOP, DATA, etc.
  - Directives: The commands that tell the assembler how to process the source code, such as ORG, EQU, DB, DW, END, etc.
  - Macros: The sequences of instructions that can be defined and invoked by a single name, such as SUM, MAX, MIN, etc.
- Data transfer instructions are used to move data between registers, memory, and I/O devices . Some examples are:
  - MOV: Move data from source to destination
  - MVI: Move immediate data to register or memory
  - LDA: Load accumulator from memory
  - STA: Store accumulator to memory
  - IN: Input data from I/O device to accumulator
  - OUT: Output data from accumulator to I/O device
- Arithmetic instructions are used to perform addition, subtraction, increment, and decrement operations on data . Some examples are:
  - ADD: Add register or memory to accumulator
  - ADI: Add immediate data to accumulator
  - SUB: Subtract register or memory from accumulator
  - SUI: Subtract immediate data from accumulator
  - INR: Increment register or memory by one
  - DCR: Decrement register or memory by one
- Logic instructions are used to perform bitwise logical operations on data, such as AND, OR, XOR, NOT, etc . Some examples are:
  - ANA: And register or memory with accumulator
  - ANI: And immediate data with accumulator
  - ORA: Or register or memory with accumulator
  - ORI: Or immediate data with accumulator
  - XRA: Xor register or memory with accumulator
  - XRI: Xor immediate data with accumulator
  - CMA: Complement accumulator
- Branch instructions are used to alter the sequence of execution of the program based on certain conditions, such as flags, registers, or memory values . Some examples are:
  - JMP: Jump unconditionally to a specified address
  - JC: Jump if carry flag is set
  - JNC: Jump if carry flag is reset
  - JZ: Jump if zero flag is set
  - JNZ: Jump if zero flag is reset
  - JPE: Jump if parity flag is even
  - JPO: Jump if parity flag is odd
- Loop instructions are used to repeat a block of code for a specified number of times or until a condition is met . Some examples are:
  - LOOP: Decrement CX register and jump if not zero
  - LOOPE: Decrement CX register and jump if zero flag is set
  - LOOPNE: Decrement CX register and jump if zero flag is reset
- Counting instructions are used to manipulate the values of registers or memory locations for counting purposes . Some examples are:
  - INC: Increment register or



### Branch Operations

Branch operations are instructions that change the normal sequential flow of execution in a program. They are used to implement control structures such as loops, conditionals, subroutines, etc. Branch operations can be classified into three types:

- **Jump instructions**: These instructions transfer the program control to a specified memory address unconditionally or based on a flag condition. The operand of a jump instruction can be an immediate value, a register, or a memory location. The syntax of a jump instruction is:

  ```
  JMP label
  ```

  or

  ```
  Jcc label
  ```

  where `label` is the destination address and `cc` is a flag condition such as `Z` (zero), `NZ` (not zero), `C` (carry), `NC` (no carry), etc. For example:

  ```
  JMP LOOP ; unconditional jump to LOOP
  JZ DONE ; jump to DONE if zero flag is set
  ```

- **Call instructions**: These instructions transfer the program control to a subroutine, which is a block of code that performs a specific task and returns to the caller. The return address of the caller is pushed onto the stack before the call instruction is executed. The syntax of a call instruction is:

  ```
  CALL label
  ```

  or

  ```
  Ccc label
  ```

  where `label` is the address of the subroutine and `cc` is a flag condition. For example:

  ```
  CALL SUM ; call the subroutine SUM
  CNZ ERROR ; call the subroutine ERROR if not zero flag is set
  ```

- **Return instructions**: These instructions return the program control to the caller of a subroutine. The return address is popped from the stack and loaded into the program counter. The syntax of a return instruction is:

  ```
  RET
  ```

  or

  ```
  Rcc
  ```

  where `cc` is a flag condition. For example:

  ```
  RET ; return to the caller
  RC ; return if carry flag is set
  ```



### Looping

- Looping is a technique of repeating a block of statements until a condition is satisfied.
- Looping is useful for performing tasks that require iteration, such as counting, indexing, programming techniques, counters and time delays.
- Looping can be implemented in assembly language using the JMP instruction or the LOOP instruction.
- The JMP instruction is a conditional or unconditional jump to a specified label. The label identifies the target instruction to be executed next.
- The LOOP instruction is a special instruction that decrements the ECX register and jumps to a specified label if the ECX register is not zero. The ECX register acts as the loop counter.
- The syntax of the JMP instruction is:

  ```
  JMP condition label
  ```

  where condition is an optional flag that specifies the condition for the jump, and label is the target label.

- The syntax of the LOOP instruction is:

  ```
  LOOP label
  ```

  where label is the target label.

- An example of a loop using the JMP instruction is:

  ```
  MOV CX, 10 ; initialize the loop counter to 10
  L1:        ; loop label
  ; loop body
  DEC CX     ; decrement the loop counter
  JNZ L1     ; jump to L1 if the loop counter is not zero
  ```

- An example of a loop using the LOOP instruction is:

  ```
  MOV ECX, 10 ; initialize the loop counter to 10
  L1:         ; loop label
  ; loop body
  LOOP L1     ; decrement the loop counter and jump to L1 if not zero
  ```

