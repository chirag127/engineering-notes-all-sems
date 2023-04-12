

# KCS

KCS stands for Knowledge-Centered Service, which is a methodology for creating and maintaining documentation as part of the service delivery process. KCS aims to improve the quality and efficiency of service organizations by capturing, structuring, and reusing knowledge from various sources, such as customer interactions, system logs, or employee feedback. Some of the benefits of KCS are:

- It reduces the need for repeated requests and escalations by providing accurate and consistent information to customers and employees.
- It increases the productivity and satisfaction of service agents by enabling them to find and share knowledge easily and quickly.
- It decreases the costs and risks of service delivery by minimizing errors, redundancies, and gaps in knowledge.
- It enhances the service levels and value to customers by providing timely and relevant solutions and insights.

KCS is based on a set of principles and practices that guide the service organization in creating a knowledge culture and a knowledge base. Some of the key elements of KCS are:

- The KCS Loop, which is a cycle of capturing, structuring, reusing, and improving knowledge in the context of solving problems and answering questions.
- The KCS Roles, which are the different levels of participation and responsibility in the knowledge process, such as contributor, publisher, coach, or leader.
- The KCS Measures, which are the metrics and indicators that evaluate the performance and impact of the knowledge process, such as resolution time, reuse rate, or customer satisfaction.
- The KCS Adoption, which is the process of implementing and sustaining KCS in the service organization, involving planning, communication, training, and governance.

KCS is a widely recognized and adopted methodology in the service industry, and it is supported by the Consortium for Service Innovation, a non-profit organization that provides resources and guidance for KCS practitioners. KCS is also compatible with other service frameworks and standards, such as ITIL, ISO, or COBIT.



## Unit 1 - Microprocessor evolution and types, microprocessor architecture and operation of its components, addressing modes, interrupts, data transfer schemes, instruction and data flow, timer and timing diagram, Interfacing devices.

- A microprocessor is an electronic device that performs arithmetic and logic operations on digital data. It is the brain of a computer system that controls the execution of programs and the processing of information.
- The evolution of microprocessors can be divided into five generations based on the number of bits, transistors, clock speed, instruction set, and fabrication technology. The five generations are:

  - First generation (1971-1972): These were the first commercial microprocessors that used 4-bit or 8-bit data buses and had a few thousand transistors. They could perform simple operations such as addition, subtraction, and logical operations. Examples are Intel 4004 and Intel 8008.
  - Second generation (1973-1978): These were 8-bit or 16-bit microprocessors that used more transistors and had higher clock speeds. They could perform more complex operations such as multiplication, division, and floating-point arithmetic. Examples are Intel 8080, Motorola 6800, and Zilog Z80.
  - Third generation (1979-1985): These were 16-bit or 32-bit microprocessors that used very large scale integration (VLSI) technology and had millions of transistors. They could perform multiple operations in parallel and had larger memory and address spaces. Examples are Intel 8086, Motorola 68000, and Zilog Z8000.
  - Fourth generation (1986-1995): These were 32-bit or 64-bit microprocessors that used ultra large scale integration (ULSI) technology and had billions of transistors. They could perform pipelining, superscalar, and vector processing and had advanced features such as cache memory, floating-point unit, and coprocessors. Examples are Intel 80386, Motorola 68020, and Intel Pentium.
  - Fifth generation (1996-present): These are 64-bit or 128-bit microprocessors that use nanotechnology and have trillions of transistors. They can perform parallel, distributed, and quantum computing and have features such as multicore, multithreading, and artificial intelligence. Examples are Intel Core, AMD Ryzen, and IBM Power.

- The microprocessor architecture consists of three main components: the central processing unit (CPU), the memory, and the input/output (I/O) devices. The CPU is further divided into three subcomponents: the arithmetic logic unit (ALU), the control unit (CU), and the registers. The operation of these components is as follows:

  - The ALU performs arithmetic and logic operations on the data provided by the registers or the memory. It also sets the flags that indicate the status of the operation, such as carry, zero, sign, overflow, etc.
  - The CU generates the control signals that coordinate the activities of the ALU, the registers, and the memory. It also fetches the instructions from the memory, decodes them, and executes them according to the instruction cycle.
  - The registers are small and fast memory units that store the data and the instructions temporarily. They include the accumulator, the program counter, the stack pointer, the instruction register, the status register, and the general-purpose registers.
  - The memory is a large and slow memory unit that stores the data and the instructions permanently. It is divided into two types: the random access memory (RAM) and the read-only memory (ROM). The RAM is volatile and can be read and written, while the ROM is non-volatile and can only be read.
  - The I/O devices are the peripherals that allow the communication between the microprocessor and the external world. They include the keyboard, the mouse, the monitor, the printer, etc. They are connected to the microprocessor through the I/O ports or the buses.

- The addressing modes are the ways of specifying the location of the operands in the memory or the registers. They determine how the effective address of the operands is calculated and how the data is accessed. The common addressing modes are:

  - Immediate addressing: The operand is a constant value that is part of the instruction. For example, ADD #10, A means add 10 to the accumulator.
  - Register addressing: The operand is



# Microprocessor Evolution and Types

A microprocessor is an electronic device that performs arithmetic and logic operations on digital data. It is the brain of a computer system that controls the input, output, and processing of data. A microprocessor consists of a central processing unit (CPU) and a memory unit that store data and instructions.

## Evolution of Microprocessors

The evolution of microprocessors can be divided into five generations, based on the technology, architecture, and performance of the devices. The characteristics of these generations are:

- **First Generation (1971-1972)**: These were the first commercial microprocessors, such as the 4-bit Intel 4004 and the 8-bit Intel 8008. They were designed for specific applications, such as calculators, terminals, and printers. They had low speed, low memory, and limited instruction set. 
- **Second Generation (1973-1978)**: These were the 8-bit microprocessors, such as the Intel 8080, the Motorola 6800, and the Zilog Z80. They were used for general-purpose computing, such as personal computers, video games, and embedded systems. They had higher speed, larger memory, and more complex instruction set than the first generation. 
- **Third Generation (1979-1985)**: These were the 16-bit microprocessors, such as the Intel 8086, the Motorola 68000, and the Zilog Z8000. They were used for advanced computing, such as multitasking, graphics, and networking. They had higher speed, larger memory, and more powerful instruction set than the second generation. 
- **Fourth Generation (1986-1995)**: These were the 32-bit microprocessors, such as the Intel 80386, the Motorola 68020, and the ARM. They were used for high-performance computing, such as multimedia, virtual reality, and parallel processing. They had higher speed, larger memory, and more sophisticated instruction set than the third generation. 
- **Fifth Generation (1996-present)**: These are the 64-bit microprocessors, such as the Intel Pentium, the AMD Athlon, and the IBM Power. They are used for supercomputing, artificial intelligence, and cloud computing. They have higher speed, larger memory, and more advanced instruction set than the fourth generation. 

## Types of Microprocessors

Microprocessors can be classified into two types, based on the complexity and functionality of their instruction set. The types of microprocessors are:

- **Complex Instruction Set Microprocessor (CISC)**: These are the microprocessors that have a large and varied instruction set, which can perform complex operations on data. They are designed to minimize the number of instructions per program and ignore the number of cycles per instruction. They are suitable for applications that require high-level languages, such as compilers and interpreters.
- **Reduced Instruction Set Microprocessor (RISC)**: These are the microprocessors that have a small and simple instruction set, which can perform basic operations on data. They are designed to reduce the number of cycles per instruction and ignore the number of instructions per program. They are suitable for applications that require low-level languages, such as assemblers and compilers.



# Microprocessor Architecture and Operation of Its Components

A microprocessor is a single integrated circuit (IC) that contains the data processing logic and control of a computer's central processing unit (CPU). It performs arithmetic, logic, and control operations on the data received from an input device or memory. It also communicates with other devices through a system bus.

The basic components of a microprocessor architecture are:

- Arithmetic Logic Unit (ALU): It performs arithmetic and logic operations on the data, such as addition, subtraction, multiplication, division, and, or, not, etc. It also sets the flags according to the result of the operation.
- Accumulator: It is a special register that holds one of the operands as well as the result of the operation performed by the ALU. It is also used to store intermediate or final results before transferring them to memory or output devices.
- Program Counter (PC): It is a register that holds the address of the next instruction to be executed. It is incremented by one after each instruction fetch, unless it is modified by a jump or branch instruction.
- Control Unit: It is the component that controls the execution of instructions and the flow of data within the microprocessor. It generates the control signals that enable or disable other components, such as the ALU, the registers, the memory, and the input/output devices. It also generates the timing signals that synchronize the operations of the microprocessor.
- Register Array: It is a set of registers that store data temporarily during the execution of instructions. They are used to hold operands, addresses, or intermediate results. Some registers are general-purpose, while others are special-purpose, such as the stack pointer, the index register, the status register, etc.
- System Bus: It is a set of wires that connect the microprocessor to other devices, such as the memory, the input/output devices, and other microprocessors. It consists of three types of lines: data lines, address lines, and control lines. Data lines carry the data to be transferred, address lines carry the address of the device to be accessed, and control lines carry the control signals that indicate the type and direction of the transfer.



# Addressing Modes

Addressing modes are an aspect of the instruction set architecture in most central processing unit (CPU) designs. They define how the machine language instructions in that architecture identify the operand(s) of each instruction.

An operand is the data or the memory location on which the instruction operates. The different addressing modes provide different ways in which the instruction specifies the address of the operand or the operand itself.

There are different types of addressing modes, such as:

- **Immediate addressing mode**: In this mode, the instruction includes the operand along with the operation. For example, `ADD #5` means add 5 to the accumulator. This mode is fast and simple, but it can only operate on constants .
- **Register addressing mode**: In this mode, the operand is stored in a register, which is specified in the instruction. For example, `ADD R1` means add the contents of register R1 to the accumulator. This mode is also fast and simple, but it has a limited number of registers .
- **Register indirect addressing mode**: In this mode, the operand is stored in a memory location, whose address is stored in a register, which is specified in the instruction. For example, `ADD (R1)` means add the contents of the memory location pointed by register R1 to the accumulator. This mode allows accessing a large memory space, but it requires an extra memory access .
- **Direct addressing mode**: In this mode, the operand is stored in a memory location, whose address is directly specified in the instruction. For example, `ADD 1000H` means add the contents of the memory location 1000H to the accumulator. This mode also allows accessing a large memory space, but it requires a large instruction size .
- **Implicit addressing mode**: In this mode, the operand is implied by the instruction itself. For example, `INR A` means increment the accumulator by 1. This mode does not require any operand specification, but it can only perform predefined operations .

Some other addressing modes are:

- **Indexed addressing mode**: In this mode, the operand is stored in a memory location, whose address is obtained by adding an index value to a base address. For example, `ADD 1000H, R1` means add the contents of the memory location 1000H + R1 to the accumulator. This mode is useful for accessing arrays or tables .
- **Relative addressing mode**: In this mode, the operand is a memory location, whose address is obtained by adding an offset value to the current program counter. For example, `JMP 10` means jump to the instruction 10 bytes ahead of the current instruction. This mode is useful for branching or looping .
- **Port addressing mode**: In this mode, the operand is an input/output device, whose address is specified in the instruction. For example, `IN 05H` means read data from the input device 05H and store it in the accumulator. This mode is useful for interfacing with external devices.



# Interrupts

- An interrupt is a condition that causes the microprocessor to temporarily work on a different task, and then later return to its previous task.
- Interrupts can be internal or external. Internal interrupts, or "software interrupts," are triggered by a software instruction and operate similarly to a jump or branch instruction. External interrupts, or "hardware interrupts," are triggered by an external device, such as a keyboard, a mouse, a timer, or another microprocessor.
- Interrupts are used for data transfer between the peripheral and the microprocessor, or for handling errors or events that require immediate attention .
- When an interrupt occurs, the microprocessor saves the current state of the program counter and the flags register, and then jumps to a predefined memory location, called the interrupt vector, where the address of the interrupt service routine (ISR) is stored. The ISR is a subroutine that performs the required task or work related to the interrupt. After the ISR is completed, the microprocessor returns to the previous state and resumes the interrupted program .
- Interrupts can be classified into various categories based on different parameters, such as:

  - Maskable and non-maskable: Maskable interrupts can be disabled or enabled by the microprocessor using special instructions, such as EI (enable interrupts) and DI (disable interrupts). Non-maskable interrupts cannot be disabled and have the highest priority .
  - Vectored and non-vectored: Vectored interrupts have a fixed interrupt vector, where the address of the ISR is stored. Non-vectored interrupts have a single interrupt vector, where the microprocessor has to read the interrupt type and then branch to the corresponding ISR .
  - Edge-triggered and level-triggered: Edge-triggered interrupts are generated by a change in the level of the interrupt signal, such as from low to high or high to low. Level-triggered interrupts are generated by a specific level of the interrupt signal, such as high or low.
  - Software and hardware: Software interrupts are generated by a software instruction, such as INT (interrupt) or TRAP (trap). Hardware interrupts are generated by an external device, such as a keyboard, a mouse, a timer, or another microprocessor .

- Some examples of interrupts in 8085 microprocessor are:

  - TRAP: It is a non-maskable, edge-triggered, and vectored interrupt. It has the highest priority among all interrupts. It is used for power failure or emergency exit.
  - RST 7.5, RST 6.5, RST 5.5: These are maskable, edge-triggered, and vectored interrupts. They have lower priority than TRAP, but higher priority than INTR. They are used for external devices or applications.
  - INTR: It is a maskable, level-triggered, and non-vectored interrupt. It has the lowest priority among all interrupts. It is used for general purpose data transfer or communication.
  - RST 4.5, RST 3.5, RST 2.5, RST 1.5, RST 0.5: These are software interrupts, triggered by the instruction RST n, where n is the interrupt number. They are vectored interrupts, with fixed interrupt vectors. They are used for subroutine calls or program branching.



# Data Transfer Schemes

Data transfer schemes are the methods through which data can be transferred between the units of a microprocessor system, such as the CPU, memory, and I/O devices. Data transfer schemes are important for the efficient and smooth operation of the system. There are three main types of data transfer schemes:

- Programmed I/O Data Transfer
- Interrupt Driven Data Transfer
- Direct Memory Access (DMA) Data Transfer

## Programmed I/O Data Transfer

Programmed I/O Data Transfer is a simple and basic method of data transfer. In this scheme, the data transfer is controlled by a program that resides in the memory and is executed by the CPU. The CPU initiates and monitors the data transfer between the memory and the I/O device by using instructions and registers. This scheme is used when the speed of data transfer is not critical and the amount of data to be transferred is small. The advantages of this scheme are:

- It is easy to implement and understand.
- It does not require any additional hardware or circuitry.

The disadvantages of this scheme are:

- It consumes a lot of CPU time and resources, as the CPU has to constantly check the status of the I/O device and perform the data transfer.
- It reduces the performance of the system, as the CPU cannot perform any other task while the data transfer is in progress.

## Interrupt Driven Data Transfer

Interrupt Driven Data Transfer is an improved method of data transfer that overcomes some of the drawbacks of the programmed I/O data transfer. In this scheme, the data transfer is initiated by the I/O device, which sends an interrupt signal to the CPU when it is ready to send or receive data. The CPU then temporarily suspends its current task and executes an interrupt service routine (ISR) that performs the data transfer between the memory and the I/O device. After the data transfer is completed, the CPU resumes its previous task. This scheme is used when the speed of data transfer is moderate and the amount of data to be transferred is variable. The advantages of this scheme are:

- It reduces the CPU involvement and overhead, as the CPU only performs the data transfer when it is requested by the I/O device.
- It improves the performance of the system, as the CPU can perform other tasks while the I/O device is waiting for data.

The disadvantages of this scheme are:

- It requires additional hardware and software to handle the interrupt signals and the ISR.
- It may cause priority and synchronization issues, as multiple I/O devices may request data transfer at the same time.

## Direct Memory Access (DMA) Data Transfer

Direct Memory Access (DMA) Data Transfer is the most advanced and efficient method of data transfer. In this scheme, the data transfer is performed directly between the memory and the I/O device, without involving the CPU. A special hardware device called the DMA controller (DMAC) is used to control and coordinate the data transfer. The CPU only initiates the data transfer by sending the parameters such as the source and destination addresses, the amount of data, and the mode of transfer to the DMAC. The DMAC then takes over the data transfer and sends an interrupt signal to the CPU when the data transfer is completed. The CPU then resumes its normal operation. This scheme is used when the speed of data transfer is high and the amount of data to be transferred is large. The advantages of this scheme are:

- It frees the CPU from the data transfer task, as the CPU only sets up the data transfer and does not participate in it.
- It maximizes the performance of the system, as the CPU and the I/O device can operate in parallel.

The disadvantages of this scheme are:

- It requires a complex and expensive hardware device (the DMAC) to perform the data transfer.
- It may cause memory contention and bus arbitration issues, as the DMAC and the CPU may access the memory and the bus at the same time.



# Instruction and Data Flow

## Microprocessor Evolution and Types

- A microprocessor is an electronic device that performs arithmetic and logic operations on digital data.
- It consists of a central processing unit (CPU) and a memory unit that store instructions and data.
- The CPU executes the instructions and manipulates the data according to the program logic.
- The evolution of microprocessor can be divided into five generations based on the technology, architecture, and performance of the microprocessors.
- The first generation microprocessors were introduced in 1971-1972. They were 4-bit microprocessors that could process only 4 bits of data at a time. They had low speed, low memory capacity, and limited instruction set. Examples are Intel 4004 and Intel 4040 .
- The second generation microprocessors were introduced in 1973-1978. They were 8-bit microprocessors that could process 8 bits of data at a time. They had higher speed, larger memory capacity, and more complex instruction set. Examples are Intel 8008, Intel 8080, and Zilog Z80 .
- The third generation microprocessors were introduced in 1979-1985. They were 16-bit microprocessors that could process 16 bits of data at a time. They had faster speed, larger memory capacity, and more advanced instruction set. They also supported pipelining, segmentation, and multitasking. Examples are Intel 8086, Intel 8088, and Motorola 68000 .
- The fourth generation microprocessors were introduced in 1986-1995. They were 32-bit microprocessors that could process 32 bits of data at a time. They had very high speed, larger memory capacity, and more powerful instruction set. They also supported virtual memory, cache memory, and parallel processing. Examples are Intel 80386, Intel 80486, and Motorola 68020 .
- The fifth generation microprocessors were introduced in 1996-present. They are 64-bit microprocessors that can process 64 bits of data at a time. They have very high speed, larger memory capacity, and more sophisticated instruction set. They also support multiprocessing, multithreading, and multimedia. Examples are Intel Pentium, Intel Core, and AMD Athlon  .
- The microprocessors can also be categorized according to the instruction set architecture, such as complex instruction set computer (CISC) and reduced instruction set computer (RISC).
- CISC microprocessors have a large and complex instruction set that can perform multiple operations in a single instruction. They are designed to minimize the number of instructions per program and ignore the number of cycles per instruction. Examples are Intel 8086, Intel 80386, and Intel Pentium.
- RISC microprocessors have a small and simple instruction set that can perform only one operation in a single instruction. They are designed to reduce the number of cycles per instruction and ignore the number of instructions per program. Examples are ARM, MIPS, and PowerPC.



# Timer and Timing Diagram

- A timer is a device that generates a periodic signal that can be used to control the timing of various operations in a microprocessor system.
- A timing diagram is a graphical representation of the sequence of events that occur during the execution of an instruction or a program in a microprocessor system.
- A timing diagram shows the changes in the values of various signals, such as the address bus, the data bus, the control signals, the clock signal, etc., as a function of time.
- A timing diagram can help to understand the working of an instruction or a program, to analyze the performance of a microprocessor system, to debug errors, and to design interfacing devices.

## Types of Timers

- There are different types of timers that can be used in microprocessor systems, such as:
  - Periodic timers: These timers generate a periodic interrupt signal that can be used to execute a routine at regular intervals. For example, a periodic timer can be used to update a real-time clock, to sample an analog signal, to generate a PWM signal, etc.
  - PWM timers: These timers generate a pulse-width modulated (PWM) signal that can be used to control the speed or direction of a motor, to dim a LED, to generate a sound, etc. A PWM signal is a digital signal that has a variable duty cycle, which is the ratio of the on time to the total period of the signal.
  - Capture timers: These timers can measure the duration or frequency of an external signal by capturing the value of a counter when the signal changes its state. For example, a capture timer can be used to measure the speed of a rotating wheel, to decode a remote control signal, to measure the pulse width of a PWM signal, etc.
  - Compare timers: These timers can generate an output signal or an interrupt signal when the value of a counter matches a predefined value. For example, a compare timer can be used to generate a one-shot pulse, to toggle an output pin, to trigger an ADC conversion, etc.

## Timing Diagram of an Instruction

- The timing diagram of an instruction shows the sequence of events that occur during the execution of the instruction in a microprocessor system.
- The timing diagram of an instruction can be divided into different phases, such as:
  - Fetch phase: This is the phase where the microprocessor fetches the opcode of the instruction from the memory and stores it in the instruction register. The fetch phase usually requires one or more clock cycles, depending on the size and type of the instruction.
  - Decode phase: This is the phase where the microprocessor decodes the opcode of the instruction and determines the type, size, and operands of the instruction. The decode phase usually requires one clock cycle.
  - Execute phase: This is the phase where the microprocessor performs the operation specified by the instruction and updates the flags and registers accordingly. The execute phase may require one or more clock cycles, depending on the complexity of the operation and the operands involved.
  - Store phase: This is the phase where the microprocessor stores the result of the operation in the memory or a register, if required by the instruction. The store phase may require one or more clock cycles, depending on the size and type of the result and the destination.

- The timing diagram of an instruction can vary depending on the microprocessor architecture, the instruction set, the addressing modes, the data transfer schemes, the interrupts, etc.
- The timing diagram of an instruction can be drawn using different symbols and notations, such as:
  - A horizontal line to represent a signal or a bus, with the name of the signal or the bus written above or below the line.
  - A vertical line to represent a clock cycle, with the clock signal shown as a square wave.
  - A high or low level to represent the logic state of a signal or a bus, with the value of the signal or the bus written above or below the line.
  - A rising or falling edge to represent the transition of a signal or a bus from one logic state to another.
  - A dashed line to represent a signal or a bus that is not used or not relevant for the instruction.
  - A bracket or a label to indicate the start and end of a phase or a sub-phase of the instruction.

- An example of a timing diagram of an instruction is shown below. The instruction is MOV A, B, which copies the contents of register B to register A in an 8085 microprocessor system. The timing diagram shows the fetch, decode, and execute phases of the instruction, along with the changes in the address bus,



# Interfacing devices

- Interfacing devices are the components that connect the microprocessor with other internal and external devices, such as memory, input/output devices, timers, etc.
- Interfacing devices enable the microprocessor to communicate with different types of devices, exchange data, and control their operations.
- Interfacing devices can be classified into two types: I/O interfacing and memory interfacing.

## I/O interfacing

- I/O interfacing is the process of connecting input devices (such as keyboard, mouse, etc.) and output devices (such as screen, printer, etc.) with the microprocessor.
- I/O interfacing allows the microprocessor to receive data from the input devices, process it, and send it to the output devices.
- I/O interfacing can be done in two ways: parallel and serial.
  - Parallel interfacing involves transferring multiple bits of data at the same time through multiple wires or pins. Parallel interfacing is faster but requires more hardware and wiring.
  - Serial interfacing involves transferring one bit of data at a time through a single wire or pin. Serial interfacing is slower but requires less hardware and wiring.
- I/O interfacing requires some additional components, such as latches, buffers, decoders, encoders, etc. to match the signals and data formats of the microprocessor and the I/O devices.

## Memory interfacing

- Memory interfacing is the process of connecting memory devices (such as RAM, ROM, etc.) with the microprocessor.
- Memory interfacing allows the microprocessor to access the memory to read the instructions and data, and store the results of the computation.
- Memory interfacing can be done in two ways: address-mapped and port-mapped.
  - Address-mapped interfacing involves assigning a unique address to each memory location, and using the address bus of the microprocessor to access the memory. Address-mapped interfacing is simpler but consumes more address space.
  - Port-mapped interfacing involves assigning a unique port number to each memory device, and using the data bus of the microprocessor to access the memory. Port-mapped interfacing is more complex but saves address space.
- Memory interfacing requires some additional components, such as address latches, address decoders, memory chips, etc. to match the signals and data formats of the microprocessor and the memory devices.



## Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

- Pin diagram of 8085 microprocessor:

  - The 8085 microprocessor is a 40-pin IC with 8-bit data bus and 16-bit address bus.
  - The pins can be classified into six groups: address bus, data bus, control and status signals, power supply and frequency, externally initiated signals, and serial I/O ports.
  - The address bus consists of 8 pins (A8-A15) that are multiplexed with the data bus (AD0-AD7) and two pins (A16 and A17) that are used to select the memory bank.
  - The data bus consists of 8 pins (AD0-AD7) that are bidirectional and multiplexed with the lower 8 bits of the address bus (A0-A7).
  - The control and status signals consist of 6 pins: RD (read), WR (write), IO/M (input/output or memory), S0 and S1 (status), and ALE (address latch enable).
  - The power supply and frequency pins consist of 2 pins: Vcc (+5V) and Vss (ground), and one pin: X1/X2 (clock input).
  - The externally initiated signals consist of 5 pins: RESET IN (reset input), RESET OUT (reset output), HOLD (hold request), HLDA (hold acknowledge), and READY (ready).
  - The serial I/O ports consist of 2 pins: SID (serial input data) and SOD (serial output data).

- Internal architecture of 8085 microprocessor:

  - The 8085 microprocessor consists of three main units: arithmetic and logic unit (ALU), registers, and control unit.
  - The ALU performs arithmetic and logical operations on 8-bit data. It has an accumulator (A) register, a temporary (T) register, and a flag (F) register. The flag register contains five flags: sign (S), zero (Z), auxiliary carry (AC), parity (P), and carry (C).
  - The registers are used to store data and addresses. They include six general purpose registers: B, C, D, E, H, and L, which can be used as pairs (BC, DE, HL) or individually. They also include two special purpose registers: program counter (PC) and stack pointer (SP), which store 16-bit addresses. The PC points to the next instruction to be executed, and the SP points to the top of the stack in memory.
  - The control unit generates control and timing signals for the internal and external operations of the microprocessor. It has an instruction register (IR), an instruction decoder, and a timing and control unit. The IR holds the current instruction, the instruction decoder decodes the instruction and generates the appropriate signals, and the timing and control unit synchronizes the operations with the clock.

- Instruction sets:

  - The 8085 microprocessor has 246 instructions, which can be classified into five groups: data transfer, arithmetic, logical, branching, and machine control.
  - The data transfer instructions are used to move data between registers, memory, and I/O devices. They include instructions such as MOV, MVI, LXI, LDA, STA, LHLD, SHLD, LDAX, STAX, XCHG, etc.
  - The arithmetic instructions are used to perform arithmetic operations on 8-bit or 16-bit data. They include instructions such as ADD, ADC, SUB, SBB, INR, DCR, INX, DCX, DAD, etc.
  - The logical instructions are used to perform logical operations on 8-bit data. They include instructions such as ANA, ORA, XRA, CMP, RLC, RRC, RAL, RAR, CMA, CMC, STC, etc.
  - The branching instructions are used to alter the sequence of execution of the program based on certain conditions. They include instructions such as JMP, JNZ, JZ, JNC, JC, JPO, JPE, JN, JP, CALL, RET, RST, etc.
  - The machine control instructions are used to control the operation of the microprocessor and the peripheral devices. They include instructions such as HLT, NOP, DI, EI, SIM, RIM, etc.

- Addressing modes:

  - The 8085 microprocessor has five addressing modes



# Pin diagram and internal architecture of 8085 microprocessor

The 8085 microprocessor is a 8-bit microprocessor that can perform various operations on 8-bit data. It has a 16-bit address bus that can access up to 64 KB of memory and a 8-bit data bus that can transfer data between the microprocessor and the external devices. The 8085 microprocessor has 40 pins that can be categorized into six groups:

- Address and data bus: These are the pins that carry the address and data signals between the microprocessor and the memory or I/O devices. The address bus consists of 16 pins (A0-A15) that can provide 16-bit address for memory or I/O devices. The data bus consists of 8 pins (D0-D7) that can transfer 8-bit data to or from the microprocessor. The address and data bus are multiplexed, which means that they share the same pins for different purposes at different times. The address and data bus are separated by using two control signals: ALE (Address Latch Enable) and IO/M (I/O or Memory).

- Control signals: These are the pins that control the timing and direction of data transfer between the microprocessor and the external devices. The control signals include:

  - ALE (Address Latch Enable): This is an active high signal that indicates that the address bus contains a valid address for memory or I/O devices. This signal is used to latch the address from the multiplexed address and data bus into a separate latch, which then provides a stable address to the external devices.
  - IO/M (I/O or Memory): This is an active low signal that indicates whether the address on the address bus is for an I/O device or a memory device. When IO/M is low, the address is for an I/O device, and when IO/M is high, the address is for a memory device.
  - RD (Read): This is an active low signal that indicates that the microprocessor wants to read data from the memory or I/O device addressed by the address bus. When RD is low, the microprocessor reads data from the data bus and stores it in the accumulator or a register.
  - WR (Write): This is an active low signal that indicates that the microprocessor wants to write data to the memory or I/O device addressed by the address bus. When WR is low, the microprocessor writes data from the accumulator or a register to the data bus.
  - S0 and S1 (Status): These are two signals that indicate the status of the microprocessor during various operations. The status signals can have four possible values:

    - S0 = 0 and S1 = 0: This indicates that the microprocessor is performing a halt instruction, which means that it is in an idle state and waiting for an interrupt or a reset.
    - S0 = 0 and S1 = 1: This indicates that the microprocessor is performing a write operation, which means that it is writing data to the memory or I/O device.
    - S0 = 1 and S1 = 0: This indicates that the microprocessor is performing a read operation, which means that it is reading data from the memory or I/O device.
    - S0 = 1 and S1 = 1: This indicates that the microprocessor is performing a fetch operation, which means that it is fetching an instruction from the memory.

- Status signals: These are the pins that provide information about the internal condition of the microprocessor, such as the flags, the interrupts, and the stack pointer. The status signals include:

  - SOD (Serial Output Data): This is a pin that provides serial output data from the microprocessor. The microprocessor can send serial data to an external device by using the SIM (Set Interrupt Mask) instruction, which sets the SOD bit in the accumulator. The serial data is then shifted out from the SOD pin on every positive edge of the clock signal.
  - SID (Serial Input Data): This is a pin that receives serial input data to the microprocessor. The microprocessor can receive serial data from an external device by using the RIM (Read Interrupt Mask) instruction, which reads the SID bit into the accumulator. The serial data is then shifted in from the SID pin on every positive edge of the clock signal.
  - INTR (Interrupt Request): This is an active high signal that indicates that an external device wants to interrupt the microprocessor. The microprocessor can accept or reject the interrupt request by using the EI (Enable Interrupt) or DI (Disable



# Registers for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Registers
- A register is a small storage unit that can hold data or instructions temporarily.
- The 8085 microprocessor has eight addressable 8-bit registers: A, B, C, D, E, H, L, F, and two 16-bit registers PC and SP .
- These registers can be classified as:
  - General Purpose Registers
  - Temporary Registers
  - Special Purpose Registers
  - Stack Pointer and Program Counter

### General Purpose Registers
- The 8085 has six general-purpose registers to store 8-bit data; these are identified as- B, C, D, E, H, and L .
- They are less important than the accumulator.
- They can be used individually or in pairs to store data, address or operands .
- The pairs are BC, DE and HL .
- The HL pair is often used to store the address of a memory location, and hence it is also called the Memory Address Register (MAR) .

### Temporary Registers
- The 8085 has two temporary registers that are not accessible to the programmer.
- They are:
  - Temporary Data Register: It is used to hold the data during arithmetic and logical operations.
  - W and Z Registers: They are used to store the 8-bit data during the execution of some instructions, such as CALL, RET, RST, etc.

### Special Purpose Registers
- The 8085 has two special purpose registers that are accessible to the programmer .
- They are:
  - Accumulator: It is an 8-bit register that is a part of the arithmetic and logic unit (ALU) .
  - It is used to store the result of any operation performed by the ALU .
  - It can also be used to store or transfer data .
  - It is also called the A register .
  - Flag Register: It is an 8-bit register that is used to indicate the status of the microprocessor after an operation .
  - It has five flags that are affected by the arithmetic and logical operations .
  - They are: Sign (S), Zero (Z), Auxiliary Carry (AC), Parity (P) and Carry (CY) .
  - The other three bits of the flag register are not used .
  - The flag register is also called the F register .

### Stack Pointer and Program Counter
- The 8085 has two 16-bit registers that are used to store the address of a memory location .
- They are:
  - Stack Pointer: It is used to point to the top of the stack in the memory .
  - The stack is a section of memory that is used to store the return address and data during the execution of subroutines and interrupts .
  - The stack pointer is decremented by two when a data or address is pushed onto the stack, and incremented by two when a data or address is popped from the stack .
  - The stack pointer is also called the SP register .
  - Program Counter: It is used to point to the address of the next instruction to be executed by the microprocessor .
  - The program counter is incremented by one or more depending on the size of the instruction .
  - The program counter is also called the PC register .

## Pin diagram and internal architecture of 8085 microprocessor
- The 8085 microprocessor is a 40-pin integrated



# ALU

- ALU stands for Arithmetic Logic Unit, and it is a major component of the central processing unit of a computer system .
- ALU performs arithmetic and logical operations on integer binary numbers .
- ALU can also perform bitwise operations, such as AND, OR, XOR, NOT, etc .
- ALU receives operands and control codes from the rest of the microprocessor, and outputs the results and status flags .
- ALU is typically the part of the processor that is designed first, as it determines the performance and functionality of the processor.
- ALU can be divided into two subunits: the arithmetic unit (AU) and the logic unit (LU), depending on the type of operation.
- AU performs addition, subtraction, multiplication, division, and other arithmetic operations.
- LU performs logical operations, such as comparison, testing, and shifting.
- ALU can have different designs and architectures, depending on the instruction set and addressing modes of the processor .
- ALU can be implemented using combinational logic circuits, such as adders, subtractors, comparators, multiplexers, etc .
- ALU can also be implemented using microcode, which is a low-level program that controls the operation of the ALU .
- ALU can be enhanced by adding a floating-point unit (FPU), which can perform arithmetic and logical operations on floating-point numbers .
- ALU can also be enhanced by adding a graphics processing unit (GPU), which can perform parallel and vector operations on large data sets.



# Control and Status for 8085 Microprocessor

- The 8085 microprocessor provides two control signals, RD and WR, to initiate read or write cycle.
- These signals are used both for reading/writing memory and for reading/writing an input/output device.
- The 8085 microprocessor also provides a signal, IO/M, to indicate whether the initiated cycle is for an input/output device or for a memory device.
- The IO/M signal is high for input/output operations and low for memory operations.
- The control signals are synchronized with the clock signal generated by the 8085 microprocessor.
- The control signals are active low, meaning they are asserted when they are at logic 0.
- The 8085 microprocessor also provides some status signals, such as S0 and S1, to indicate the type of operation being performed.
- The status signals are encoded as follows:

| S1 | S0 | Operation |
|----|----|-----------|
| 0  | 0  | HALT      |
| 0  | 1  | WRITE     |
| 1  | 0  | READ      |
| 1  | 1  | FETCH     |

- The 8085 microprocessor also provides some other signals, such as ALE, INTA, READY, HOLD, HLDA, RESET IN, RESET OUT, SID, SOD, etc., to perform various functions  .
- A brief description of these signals is given below  :

| Signal | Description |
|--------|-------------|
| ALE    | Address Latch Enable, used to separate the address and data lines of the multiplexed bus AD0-AD7 |
| INTA   | Interrupt Acknowledge, used to acknowledge an interrupt request from an external device |
| READY  | Ready, used to indicate that the device is ready to send or receive data |
| HOLD   | Hold, used to request the 8085 microprocessor to relinquish the control of the bus |
| HLDA   | Hold Acknowledge, used to indicate that the 8085 microprocessor has granted the hold request |
| RESET IN | Reset In, used to reset the 8085 microprocessor |
| RESET OUT | Reset Out, used to reset the external devices connected to the 8085 microprocessor |
| SID    | Serial Input Data, used to receive serial data from an external device |
| SOD    | Serial Output Data, used to send serial data to an external device |



# Interrupt and Machine Cycle

## Interrupt
- An interrupt is a signal that causes the microprocessor to temporarily stop its current program execution and switch to a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are initiated by external devices that are connected to the microprocessor through the interrupt pins. The 8085 microprocessor has five interrupt pins: INTR, RST 7.5, RST 6.5, RST 5.5, and TRAP .
- Software interrupts are instructions that are inserted in the program to generate an interrupt. The 8085 microprocessor has eight software interrupts: RST 0, RST 1, RST 2, RST 3, RST 4, RST 5, RST 6, and RST 7.
- Interrupts can be enabled or disabled by using the EI (enable interrupt) and DI (disable interrupt) instructions. The microprocessor also has a flip-flop called the interrupt enable flip-flop (IEF) that controls the interrupt acceptance. The EI instruction sets the IEF to 1, while the DI instruction resets it to 0.
- When an interrupt is accepted, the microprocessor performs the following steps :
  - It completes the execution of the current instruction.
  - It saves the address of the next instruction on the stack.
  - It sends an interrupt acknowledge signal (INTA) to the interrupting device.
  - It receives the interrupt vector (a predefined address of the ISR) from the interrupting device or from the instruction itself.
  - It jumps to the ISR and executes it.
  - It returns to the main program by popping the saved address from the stack.

## Machine Cycle
- A machine cycle is the basic operation performed by the microprocessor to execute an instruction. It consists of one or more clock cycles (T-states) during which the microprocessor accesses the memory or the I/O devices.
- The 8085 microprocessor has six types of machine cycles: opcode fetch, memory read, memory write, I/O read, I/O write, and interrupt acknowledge .
- The opcode fetch cycle is the first cycle of every instruction. It is used to fetch the opcode (the binary code of the instruction) from the memory. It consists of four T-states: T1, T2, T3, and T4. During this cycle, the microprocessor performs the following operations :
  - It places the address of the instruction on the address bus (A15-A0) and enables the ALE (address latch enable) signal to latch the address in the external latch.
  - It enables the RD (read) signal to indicate that it is reading from the memory.
  - It receives the opcode from the data bus (D7-D0) and stores it in the instruction register (IR).
  - It increments the program counter (PC) by one to point to the next instruction.
- The memory read cycle is used to read data from the memory. It consists of three T-states: T1, T2, and T3. During this cycle, the microprocessor performs the following operations :
  - It places the address of the data on the address bus (A15-A0) and enables the ALE signal to latch the address in the external latch.
  - It enables the RD signal to indicate that it is reading from the memory.
  - It receives the data from the data bus (D7-D0) and stores it in the accumulator (A) or another register.
- The memory write cycle is used to write data to the memory. It consists of three T-states: T1, T2, and T3. During this cycle, the microprocessor performs the following operations :
  - It places the address of the data on the address bus (A15-A0) and enables the ALE signal to latch the address in the external latch.
  - It enables the WR (write) signal to indicate that it is writing to the memory.
  - It places the data from the accumulator (A) or another register on the data bus (D7-D0) and sends it to the memory.
- The I/O read cycle is used to read data from an I/O device. It consists of three T-states



# Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Pin diagram of 8085 microprocessor

- The 8085 microprocessor is an 8-bit microprocessor that operates on 8 bits of data at a time. It has 40 pins and requires a +5V power supply. The pin diagram of 8085 microprocessor is shown below:

Pin diagram of 8085 microprocessor

- The pins of the 8085 microprocessor can be classified into six groups:

  - Address and data bus: These are 16 address lines (A0-A15) and 8 data lines (D0-D7) that are used to communicate with the memory and I/O devices. The address bus is unidirectional, while the data bus is bidirectional. The address bus can address up to 64 KB of memory. The data bus can transfer 8 bits of data at a time.
  - Control and status signals: These are 6 pins that are used to control the operation of the microprocessor and indicate its status. They are:

    - ALE (Address Latch Enable): This is an output signal that indicates when the address bus contains a valid address. It is used to latch the address from the address bus into an external latch.
    - RD (Read): This is an active low output signal that indicates when the microprocessor is reading data from the memory or I/O device.
    - WR (Write): This is an active low output signal that indicates when the microprocessor is writing data to the memory or I/O device.
    - IO/M (Input/Output or Memory): This is an output signal that indicates whether the address on the address bus is for an I/O device or a memory location. It is high for I/O and low for memory.
    - S0 and S1 (Status): These are two output signals that indicate the status of the microprocessor. They can have four possible values:

      - 00: Halt state
      - 01: Write state
      - 10: Read state
      - 11: Fetch state

  - Power supply and clock signals: These are 3 pins that are used to provide power and timing to the microprocessor. They are:

    - Vcc: This is the +5V power supply pin.
    - Vss: This is the ground pin.
    - X1 and X2: These are two pins that are connected to an external crystal oscillator or a clock generator circuit. They provide the clock pulses to the microprocessor.

  - Externally initiated signals: These are 4 pins that are used to receive signals from external devices that can affect the operation of the microprocessor. They are:

    - RESET IN: This is an active high input signal that is used to reset the microprocessor and initialize its registers and flags. It also clears the interrupt enable and halt flags.
    - RESET OUT: This is an active low output signal that is used to reset the external devices connected to the microprocessor. It is activated after the RESET IN signal is deactivated.
    - READY: This is an active high input signal that is used to synchronize the microprocessor with the slower memory or I/O devices. It indicates when the device is ready to send or receive data. If the READY signal is low, the microprocessor waits until it becomes high before completing the data transfer.
    - HOLD: This is an active high input signal that is used to request the microprocessor to relinquish the control of the address, data and control buses. It is used by external devices that want to access the memory or I/O devices directly. The microprocessor acknowledges the request by activating the HLDA (Hold Acknowledge) signal and releasing the buses.
    - HLDA: This is an active high output signal that is used to acknowledge the HOLD request. It indicates that the microprocessor has released the buses and entered the hold state. It remains high until the HOLD signal is deactivated.

  - Serial I/O ports: These are 2 pins that are used to perform serial data communication with external devices. They are:

    - SID (Serial Input Data): This is an input pin that is used to receive serial data from an external device. The data



# Addressing modes for the notes of the Unit 2 - Pin diagram and internal architecture of 8085 microprocessor, registers, ALU, Control & status, interrupt and machine cycle. Instruction sets. Addressing modes. Instruction formats Instruction Classification: data transfer, arithmetic operations, logical operations, branching operations, machine control and assembler directives.

## Addressing modes

- The way of specifying data to be operated by an instruction is called addressing mode.
- The 8085 microprocessor uses five addressing modes: 
  - Immediate addressing mode
  - Register addressing mode
  - Register indirect addressing mode
  - Direct addressing mode
  - Implicit addressing mode

### Immediate addressing mode

- In this mode, the 8/16-bit data is specified in the instruction itself as one of its operand.
- For example: MVI A, 32H means load the accumulator with the data 32H.
- The advantage of this mode is that it is fast and simple.
- The disadvantage of this mode is that it can only operate on 8/16-bit data and it occupies more memory space.

### Register addressing mode

- In this mode, the data to be operated is available inside the register(s) specified in the instruction.
- For example: MOV B, C means copy the data from register C to register B.
- The advantage of this mode is that it is fast and does not require any memory access.
- The disadvantage of this mode is that it can only operate on the data stored in the registers.

### Register indirect addressing mode

- In this mode, the effective address of the data is stored in a register pair specified in the instruction.
- The data is then accessed from the memory location pointed by the register pair.
- For example: MOV A, M means copy the data from the memory location pointed by the register pair HL to the accumulator.
- The advantage of this mode is that it can access any memory location using a register pair.
- The disadvantage of this mode is that it requires an extra memory access and it can only use the register pairs BC, DE and HL.

### Direct addressing mode

- In this mode, the effective address of the data is specified in the instruction itself as a 16-bit operand.
- The data is then accessed from the memory location pointed by the 16-bit operand.
- For example: LDA 2000H means load the accumulator with the data from the memory location 2000H.
- The advantage of this mode is that it can access any memory location directly.
- The disadvantage of this mode is that it occupies more memory space and it requires an extra memory access.

### Implicit addressing mode

- In this mode, the data to be operated is implied by the instruction itself and is not specified explicitly.
- For example: CMA means complement the accumulator, i.e., change 0 to 1 and 1 to 0 in the accumulator.
- The advantage of this mode is that it is simple and does not require any operand.
- The disadvantage of this mode is that it can only perform some predefined operations.



# Instruction formats and classification

## Instruction formats

- An instruction is a binary pattern that specifies a certain operation to be performed by the microprocessor.
- An instruction consists of two parts: an **opcode** and an **operand**.
- The opcode is the part of the instruction that specifies the type of operation to be performed, such as add, subtract, move, etc.
- The operand is the part of the instruction that specifies the data or the address of the data on which the operation is to be performed.
- The operand can be a register, a memory location, an immediate data, or an I/O port.
- The 8085 microprocessor has three types of instruction formats: **one-byte**, **two-byte**, and **three-byte** instructions.
- The one-byte instructions have only the opcode and no operand. For example, `HLT` is a one-byte instruction that halts the microprocessor.
- The two-byte instructions have the opcode in the first byte and the operand in the second byte. For example, `MVI A, 05H` is a two-byte instruction that moves the immediate data `05H` to the accumulator register `A`.
- The three-byte instructions have the opcode in the first byte and the operand in the second and third bytes. For example, `LDA 2000H` is a three-byte instruction that loads the accumulator with the data from the memory location `2000H`.
- The following table shows the general formats of the three types of instructions:

| Instruction type | Format | Example |
| ---------------- | ------ | ------- |
| One-byte | OPCODE | HLT |
| Two-byte | OPCODE OPERAND | MVI A, 05H |
| Three-byte | OPCODE OPERAND OPERAND | LDA 2000H |

## Instruction classification

- The 8085 microprocessor has a set of 246 instructions, which are classified into five groups according to their functions: **data transfer**, **arithmetic**, **logical**, **branching**, and **machine control**.
- The data transfer instructions are used to move data between registers, memory, and I/O devices. For example, `MOV A, B` is a data transfer instruction that copies the contents of register `B` to register `A`.
- The arithmetic instructions are used to perform arithmetic operations such as addition, subtraction, increment, decrement, etc. on the data in the registers or memory. For example, `ADD B` is an arithmetic instruction that adds the contents of register `B` to the accumulator and stores the result in the accumulator.
- The logical instructions are used to perform logical operations such as AND, OR, XOR, complement, rotate, etc. on the data in the registers or memory. For example, `ANA B` is a logical instruction that performs the bitwise AND operation between the contents of register `B` and the accumulator and stores the result in the accumulator.
- The branching instructions are used to alter the sequence of execution of the program based on certain conditions. For example, `JNZ 1000H` is a branching instruction that jumps to the memory location `1000H` if the zero flag is not set.
- The machine control instructions are used to control the operation of the microprocessor and the peripheral devices. For example, `EI` is a machine control instruction that enables the interrupt system of the microprocessor.
- The assembler directives are not instructions, but commands to the assembler that specify how to assemble the program. For example, `ORG 2000H` is an assembler directive that tells the assembler to start assembling the program from the memory location `2000H`.



# Data Transfer for the Notes of the Unit 2

## Pin Diagram and Internal Architecture of 8085 Microprocessor

- The 8085 microprocessor is an 8-bit processor that has 40 pins and operates on a single +5V power supply.
- The pin diagram of the 8085 microprocessor is shown below:

Pin diagram of 8085 microprocessor

- The internal architecture of the 8085 microprocessor consists of the following components:

  - Registers: The 8085 has six general-purpose registers (B, C, D, E, H, and L) that can store 8-bit data each. It also has one accumulator (A) that can perform arithmetic and logical operations. Additionally, it has two special-purpose registers: the program counter (PC) that holds the address of the next instruction to be executed, and the stack pointer (SP) that points to the top of the stack in memory.
  - ALU: The arithmetic and logic unit (ALU) performs various operations on the data stored in the registers or memory. It can perform addition, subtraction, increment, decrement, logical AND, OR, XOR, complement, and rotate operations. It also sets the flags in the flag register according to the result of the operation.
  - Control and Status: The control and status unit generates the control signals for the internal and external devices. It also monitors the status of the microprocessor and the external devices. It has five flags: sign (S), zero (Z), auxiliary carry (AC), parity (P), and carry (CY) that indicate the outcome of the ALU operations.
  - Interrupt: The interrupt unit handles the external requests for interrupting the normal execution of the program. It has five interrupt pins: INTR, RST 7.5, RST 6.5, RST 5.5, and TRAP. The INTR is a maskable interrupt that can be enabled or disabled by software. The RST 7.5, RST 6.5, and RST 5.5 are also maskable interrupts that have fixed priority and vector addresses. The TRAP is a non-maskable interrupt that has the highest priority and cannot be disabled by software.
  - Machine Cycle: The machine cycle is the basic unit of time for the microprocessor operations. It consists of three or more clock cycles, depending on the type of operation. There are four types of machine cycles: opcode fetch, memory read, memory write, and I/O. The opcode fetch cycle fetches the instruction from the memory and decodes it. The memory read cycle reads the data from the memory and stores it in the register or accumulator. The memory write cycle writes the data from the register or accumulator to the memory. The I/O cycle transfers the data between the microprocessor and the external devices.

## Instruction Sets

- The instruction set of the 8085 microprocessor is a collection of commands that the microprocessor can execute. Each instruction has a mnemonic, an opcode, and an operand. The mnemonic is a symbolic representation of the instruction, such as ADD, MOV, JMP, etc. The opcode is a binary code that identifies the instruction, such as 10000110, 01000110, 11000011, etc. The operand is the data or the address that the instruction operates on, such as A, B, C, 2000H, etc.
- The instruction set of the 8085 microprocessor can be classified into five groups: data transfer, arithmetic, logical, branching, and machine control.

### Data Transfer

- The data transfer instructions are used to transfer data between the registers, memory, and I/O devices. They do not affect the flags or the ALU operations. Some examples of data transfer instructions are:

  - MOV: This instruction copies the data from the source operand to the destination operand. For example, MOV A, B copies the data from register B to register A.
  - MVI: This instruction loads an 8-bit immediate data to the destination operand. For example, MVI A, 05H loads the hexadecimal value 05 to register A.
  - LDA: This instruction loads an 8-bit data from a 16-bit memory address to the accumulator. For example, LDA 2000H loads the data from the memory location 2000H to the accumulator.
  - STA: This instruction stores an 8-bit data from the accumulator to a 16-bit memory address. For



# Arithmetic Operations in 8085 Microprocessor

- The 8085 microprocessor performs various arithmetic operations, such as addition, subtraction, increment, and decrement  .
- These arithmetic operations have the following mnemonics  :

| Mnemonic | Operand | Explanation |
| --- | --- | --- |
| ADD | r/M | Add register or memory to accumulator |
| ADC | r/M | Add register or memory to accumulator with carry |
| ADI | data | Add immediate data to accumulator |
| ACI | data | Add immediate data to accumulator with carry |
| DAD | rp | Add register pair to HL register pair |
| SUB | r/M | Subtract register or memory from accumulator |
| SBB | r/M | Subtract register or memory from accumulator with borrow |
| SUI | data | Subtract immediate data from accumulator |
| SBI | data | Subtract immediate data from accumulator with borrow |
| INR | r/M | Increment register or memory by 1 |
| INX | rp | Increment register pair by 1 |
| DCR | r/M | Decrement register or memory by 1 |
| DCX | rp | Decrement register pair by 1 |

- The arithmetic operations affect the flags of the 8085 microprocessor, such as the sign flag, zero flag, auxiliary carry flag, parity flag, and carry flag .
- The arithmetic operations are performed by the arithmetic and logic unit (ALU) of the 8085 microprocessor, which is a part of the internal architecture.
- The arithmetic operations are classified as data transfer instructions, as they transfer data between the registers, memory, and accumulator .



# Logical Operations in 8085 Microprocessor

- Logical operations are the instructions that perform basic logical operations such as AND, OR, XOR, NOT, etc. on the bits of the operands.
- In the 8085 microprocessor, the destination operand for the logical instructions is always the accumulator register (A).
- The logical operations work on a bitwise level, meaning that each bit of the accumulator is logically operated with the corresponding bit of the source operand.
- The source operand can be either a register, a memory location, or an immediate data.
- The result of the logical operation is stored in the accumulator register and the flags are affected accordingly.
- The logical instructions in 8085 microprocessor are:

  - **ANA** (AND with accumulator): This instruction performs the bitwise AND operation between the accumulator and the source operand and stores the result in the accumulator. The source operand can be a register, a memory location, or an immediate data. The flags affected by this instruction are: S, Z, P, C, and AC.
  - **ORA** (OR with accumulator): This instruction performs the bitwise OR operation between the accumulator and the source operand and stores the result in the accumulator. The source operand can be a register, a memory location, or an immediate data. The flags affected by this instruction are: S, Z, P, C, and AC.
  - **XRA** (XOR with accumulator): This instruction performs the bitwise XOR operation between the accumulator and the source operand and stores the result in the accumulator. The source operand can be a register, a memory location, or an immediate data. The flags affected by this instruction are: S, Z, P, C, and AC.
  - **CMA** (Complement accumulator): This instruction performs the bitwise complement operation on the accumulator, meaning that each bit of the accumulator is inverted. The source operand is not required for this instruction. The flags affected by this instruction are: None.
  - **RLC** (Rotate left through carry): This instruction performs the left circular rotation of the accumulator, meaning that the leftmost bit of the accumulator is shifted to the rightmost position and also to the carry flag. The source operand is not required for this instruction. The flags affected by this instruction are: C.
  - **RRC** (Rotate right through carry): This instruction performs the right circular rotation of the accumulator, meaning that the rightmost bit of the accumulator is shifted to the leftmost position and also to the carry flag. The source operand is not required for this instruction. The flags affected by this instruction are: C.
  - **RAL** (Rotate left through accumulator): This instruction performs the left rotation of the accumulator, meaning that the leftmost bit of the accumulator is shifted to the carry flag and the carry flag is shifted to the rightmost position of the accumulator. The source operand is not required for this instruction. The flags affected by this instruction are: C.
  - **RAR** (Rotate right through accumulator): This instruction performs the right rotation of the accumulator, meaning that the rightmost bit of the accumulator is shifted to the carry flag and the carry flag is shifted to the leftmost position of the accumulator. The source operand is not required for this instruction. The flags affected by this instruction are: C.



# Branching Operations

- Branching operations are instructions that allow the microprocessor to change the sequence of the program, either unconditionally or under certain conditions  .
- Branching operations can be classified into three types: unconditional branching, conditional branching, and subroutine branching.
- Unconditional branching instructions are those that always cause a jump to a specified address, regardless of the status of the flags or the contents of the registers. The only unconditional branching instruction in 8085 microprocessor is JMP (Jump) which takes a 16-bit address as an operand  .
- Conditional branching instructions are those that cause a jump to a specified address only if a certain condition is met, such as the value of a flag or the result of a comparison. The 8085 microprocessor has eight conditional branching instructions: JC (Jump if Carry), JNC (Jump if No Carry), JZ (Jump if Zero), JNZ (Jump if Not Zero), JP (Jump if Positive), JM (Jump if Minus), JPE (Jump if Parity Even), and JPO (Jump if Parity Odd). Each of these instructions takes a 16-bit address as an operand and checks the corresponding flag before jumping  .
- Subroutine branching instructions are those that allow the microprocessor to execute a subroutine, which is a sequence of instructions that performs a specific task and returns to the main program. The 8085 microprocessor has three subroutine branching instructions: CALL (Call Subroutine), RET (Return from Subroutine), and RST (Restart). The CALL instruction takes a 16-bit address as an operand and pushes the return address (the address of the next instruction in the main program) onto the stack before jumping to the subroutine. The RET instruction pops the return address from the stack and jumps back to the main program. The RST instruction takes a 3-bit number (0 to 7) as an operand and jumps to a predefined address (0000H to 0038H) where a subroutine is stored. The RST instruction also pushes the return address onto the stack before jumping  .
- Branching operations are useful for implementing loops, decision making, and modular programming in the 8085 microprocessor.



# Machine Control and Assembler Directives

- Machine control instructions are used to control the operation of the 8085 microprocessor, such as enabling or disabling interrupts, halting the processor, or sending or receiving serial data.
- Assembler directives are commands to the assembler that do not generate machine code, but affect the assembly process, such as defining symbols, allocating memory, or specifying the origin of the program.

## Machine Control Instructions

- The 8085 microprocessor has four machine control instructions: HLT, NOP, SIM, and RIM.
- HLT (Halt) - Opcode: 76, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 7, Hex Code: 76
  - This instruction stops the execution of the program and puts the processor in the halt state until an interrupt or reset occurs.
- NOP (No Operation) - Opcode: 00, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex Code: 00
  - This instruction does nothing and is used to fill the unused memory locations or to introduce a delay in the program.
- SIM (Set Interrupt Mask) - Opcode: 30, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex Code: 30
  - This instruction is used to implement the different interrupts of 8085 microprocessor, such as RST 7.5, 6.5, and 5.5, and also serial data output. It does not affect the TRAP interrupt.
  - The instruction uses the accumulator to set or reset the interrupt mask bits and the serial output data bit as follows:

    | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
    | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
    | SOD   | RST 7.5 | RST 6.5 | RST 5.5 | M7.5 | M6.5 | M5.5 | EI/DI |

  - SOD: Serial Output Data. This bit is copied to the SOD pin of the processor when the SIM instruction is executed.
  - RST 7.5, 6.5, 5.5: These bits are used to reset the corresponding interrupt flip-flops when the SIM instruction is executed.
  - M7.5, M6.5, M5.5: These bits are used to mask or unmask the corresponding interrupts. A 1 in the bit position enables the interrupt, and a 0 disables it.
  - EI/DI: This bit is used to enable or disable all the maskable interrupts. A 1 in the bit position enables the interrupts, and a 0 disables them.

- RIM (Read Interrupt Mask) - Opcode: 20, Operand: None, Length: 1 byte, M-Cycles: 1, T-States: 4, Hex Code: 20
  - This instruction is used to read the status of the interrupt mask bits and the serial input data bit. It copies the status to the accumulator as follows:

    | Bit 7 | Bit 6 | Bit 5 | Bit 4 | Bit 3 | Bit 2 | Bit 1 | Bit 0 |
    | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
    | SID   | RST 7.5 | RST 6.5 | RST 5.5 | M7.5 | M6.5 | M5.5 | EI/DI |

  - SID: Serial Input Data. This bit is copied from the SID pin of the processor when the RIM instruction is executed.
  - RST 7.5, 6.5, 5.5: These bits indicate the status of the corresponding interrupt flip-flops. A 1 in the bit position means that the interrupt is pending, and a 0 means that it is not.
  - M7.5, M6.5, M5.5: These bits indicate the status of the corresponding interrupt mask bits. A 1 in the bit position means that the interrupt is enabled, and a 0 means that it is disabled.
  - EI/DI: This bit indicates the status of the global interrupt enable/disable bit. A



# Unit 3 - Architecture of 8086 microprocessor

The 8086 microprocessor is a 16-bit microprocessor with a 16-bit internal and external data bus. It can access up to 1 MB of memory with 20 address lines. It was designed by Intel between 1976 and 1978 and released on June 8, 1978.

The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)  . The figure below shows the block diagram of the architectural representation of the 8086 microprocessor:

8086 architecture

## Bus Interface Unit (BIU)

The bus interface unit interfaces 8086 with the external world. It handles all the data transfer functions. It consists of the following components:

- **Segment registers**: These are four 16-bit registers that store the starting addresses of four memory segments: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES). Each segment can be up to 64 KB in size.
- **Instruction pointer (IP)**: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
- **Address adder**: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O devices.
- **Instruction queue**: This is a 6-byte FIFO buffer that prefetches and stores the instructions from the memory. This increases the speed of instruction execution by reducing the wait states.
- **Data bus buffer**: This is a 16-bit bidirectional buffer that transfers data between the BIU and the EU.
- **Control bus**: This is a set of control signals that control the operation of the BIU and the EU.

## Execution Unit (EU)

The execution unit executes the instructions fetched by the BIU. It consists of the following components:

- **Arithmetic and logic unit (ALU)**: This is a 16-bit unit that performs arithmetic and logical operations on the operands.
- **General purpose registers**: These are eight 16-bit registers that can be used for various purposes. They are: accumulator (AX), base (BX), counter (CX), data (DX), source index (SI), destination index (DI), base pointer (BP), and stack pointer (SP). Each register can be accessed as a whole (16 bits) or as two halves (8 bits each).
- **Flag register**: This is a 16-bit register that stores the status of the EU after an operation. It has nine flags: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF), trap (TF), interrupt enable (IF), direction (DF), and overflow (OF).
- **Instruction decoder**: This is a circuit that decodes the instructions fetched by the BIU and generates the appropriate control signals for the EU.

## Memory addressing and memory segmentation

The 8086 microprocessor can address up to 1 MB of memory using 20 address lines. However, the 8086 uses a segmented memory model, which means that the memory is divided into segments of up to 64 KB each. Each segment has a base address and an offset address. The base address is stored in one of the segment registers (CS, DS, SS, or ES), and the offset address is stored in one of the general purpose registers or the instruction pointer. The physical address is calculated by adding the base address and the offset address, as shown below:

memory addressing

The advantage of memory segmentation is that it allows the programmer to access different types of data (code, data, stack, or extra) in different segments, and to relocate the segments easily. The disadvantage is that it limits the size of each segment to 64 KB, and requires more instructions to access the memory.

## Operating modes

The 8086 microprocessor has two operating modes: minimum mode and maximum mode. The minimum mode is used when the 8086 is the only processor in the system, and the maximum mode is used when the 8086 is part of a multiprocessor system.

In the minimum mode, the 8086 generates all the control signals for the memory and I/O devices, and uses



# Architecture of 8086 Microprocessor

The 8086 microprocessor is a 16-bit processor that can access up to 1 MB of memory using 20 address lines. It has a 16-bit internal and external data bus. It consists of two independent sections or units: the Bus Interface Unit (BIU) and the Execution Unit (EU).

## Bus Interface Unit (BIU)

The BIU provides the interface of 8086 to external memory and I/O devices via the system bus. It handles all the data transfer functions. It consists of the following components:

- **Segment registers**: These are four 16-bit registers that store the base addresses of four memory segments: code, data, stack, and extra. Each segment can be up to 64 KB in size. The BIU uses these registers to generate the physical address of any memory location by adding the segment base address and the offset address.
- **Instruction pointer**: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment. The BIU uses this register to fetch the instruction bytes from the memory and store them in the instruction queue.
- **Instruction queue**: This is a 6-byte FIFO buffer that holds the prefetched instruction bytes from the memory. The BIU fills the queue whenever it is not busy with other data transfers. The EU fetches the instruction bytes from the queue for execution.
- **Address adder**: This is a circuit that performs the addition of the segment base address and the offset address to generate the 20-bit physical address.

## Execution Unit (EU)

The EU performs the arithmetic and logical operations on the data. It consists of the following components:

- **General purpose registers**: These are eight 16-bit registers that can be used for various purposes such as data manipulation, address calculation, and temporary storage. They can be accessed as four 16-bit registers (AX, BX, CX, DX) or eight 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL).
- **Pointer and index registers**: These are four 16-bit registers that are used for address calculation and indexing. They are: stack pointer (SP), base pointer (BP), source index (SI), and destination index (DI).
- **Arithmetic and logic unit (ALU)**: This is a circuit that performs the arithmetic and logical operations on the data. It can operate on 8-bit or 16-bit operands. It also sets the flags in the flag register according to the result of the operation.
- **Flag register**: This is a 16-bit register that stores the status of the EU. It consists of nine flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow. These flags are used to control the flow of the program and to indicate the outcome of the operations.
- **Control unit**: This is a circuit that controls the operation of the EU. It consists of the following components:
  - **Decode unit**: This unit decodes the instruction bytes fetched from the instruction queue and generates the control signals for the execution of the instruction.
  - **Instruction pointer**: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment. The EU uses this register to update the instruction pointer in the BIU after the execution of the instruction.
  - **Temporary register**: This is a 16-bit register that is used for temporary storage of data during the execution of the instruction.



# Unit 3 - Architecture of 8086 microprocessor

## Register organization

- The 8086 microprocessor has 14 user-accessible 16-bit registers, which are divided into four groups: data, pointer and index, segment, and instruction pointer .
- The data registers are AX, BX, CX, and DX, which can store 16-bit data or two 8-bit data in their high (H) and low (L) parts. For example, AX can store AH and AL .
- The data registers are used for arithmetic, logic, data transfer, and I/O operations. AX is also called the accumulator, which is used by default for many operations.
- The pointer and index registers are SP, BP, SI, and DI, which are used for addressing memory locations. SP and BP are called stack pointer and base pointer, which are used for stack operations and accessing data in the stack segment. SI and DI are called source index and destination index, which are used for string operations and accessing data in the data segment .
- The segment registers are CS, DS, SS, and ES, which are used for defining the memory segments where the code, data, stack, and extra data are located. Each segment register can store a 16-bit segment base address, which is combined with a 16-bit offset address from a pointer or index register to form a 20-bit physical address .
- The instruction pointer register is IP, which is used for storing the offset address of the next instruction to be executed within the code segment. IP is automatically incremented by the length of the current instruction after each instruction execution .

## Bus interface unit

- The bus interface unit (BIU) is responsible for interfacing the 8086 microprocessor with the external memory and I/O devices via the system bus.
- The system bus consists of three parts: the address bus, the data bus, and the control bus. The address bus is 20-bit wide and can address up to 1 MB of memory. The data bus is 16-bit wide and can transfer 16-bit data or two 8-bit data in one cycle. The control bus consists of various signals that control the timing and direction of data transfer.
- The BIU contains a 6-byte instruction queue, which prefetches and stores the instructions from the code segment before they are executed by the execution unit (EU). This improves the performance of the 8086 by overlapping instruction fetch and execution.
- The BIU also contains the segment registers and the instruction pointer register, which are used for generating the physical addresses for memory access.

## Execution unit

- The execution unit (EU) is responsible for decoding and executing the instructions fetched by the BIU.
- The EU contains the data registers, the pointer and index registers, and the arithmetic logic unit (ALU), which are used for performing various operations on the data.
- The EU also contains the flags register, which is a 16-bit register that contains 9 status and control flags. The status flags are CF (carry flag), PF (parity flag), AF (auxiliary carry flag), ZF (zero flag), SF (sign flag), and OF (overflow flag), which are set or reset according to the result of an operation. The control flags are TF (trap flag), IF (interrupt flag), and DF (direction flag), which are used for controlling the execution mode and direction of the 8086.

## Memory addressing and memory segmentation

- The 8086 microprocessor can address up to 1 MB of memory, which is divided into four segments: code, data, stack, and extra.
- Each segment can be up to 64 KB in size, and can be located anywhere in the memory. Each segment is identified by a 16-bit segment base address, which is stored in a segment register.
- To access a memory location within a segment, a 16-bit offset address is required, which is stored in a pointer or index register or provided as an immediate operand. The offset address is relative to the start of the segment.
- To form a 20-bit physical address, the segment base address is shifted left by 4 bits and added to the offset address. For example, if CS = 1000H and IP = 2000



# Bus Interface Unit

- The bus interface unit (BIU) is one of the two sections or units of the 8086 microprocessor architecture. The other section is the execution unit (EU).
- The BIU provides the interface of 8086 to external memory and I/O devices via the system bus. It handles all the data transfer functions.
- The BIU performs read and write operations on data in the memory and on the external devices connected to the ports of the microprocessor, and it also sends out addresses.
- The BIU contains four 16-bit special purpose registers called as segment registers. They are:
  - Code segment register (CS): is used for addressing memory location in the code segment of the memory, where the executable program is stored.
  - Data segment register (DS): is used for addressing memory location in the data segment of the memory, where the data used by the program is stored.
  - Stack segment register (SS): is used for addressing memory location in the stack segment of the memory, where the stack data is stored.
  - Extra segment register (ES): is used for addressing memory location in the extra segment of the memory, which can be used for additional data storage.
- The BIU also contains a 16-bit instruction pointer (IP) register, which holds the offset address of the next instruction to be executed within the code segment.
- The BIU also contains a 6-byte instruction queue, which prefetches and stores the instructions from the memory before they are executed by the EU. This increases the speed of execution and allows pipelining.
- The BIU uses a technique called memory segmentation to divide the 1 MB physical memory into four logical segments of 64 KB each. Each segment is identified by a 16-bit segment base address, which is stored in the corresponding segment register. The segment base address is also called the segment selector.
- The BIU generates a 20-bit physical address by adding a 16-bit offset address to the segment base address. The offset address is also called the effective address or the displacement. The physical address is also called the linear address or the absolute address.
- The physical address is calculated by the BIU as follows:

  - Physical address = (Segment base address * 16) + Offset address
  - For example, if CS = 1000H and IP = 2000H, then the physical address of the next instruction is:

    - Physical address = (1000H * 16) + 2000H
    - Physical address = 10000H + 2000H
    - Physical address = 12000H
- The BIU uses three different buses to transfer data and instructions between the microprocessor and other components in a computer system. These buses are:

  - Address bus: The address bus is used to send the memory address of the instruction or data being read or written. It is a unidirectional bus, which means it can only carry data from the BIU to the memory or I/O devices. The address bus of 8086 is 20-bit wide, which means it can address up to 2^20 or 1 MB of memory locations.
  - Data bus: The data bus is used to send or receive the instruction or data being read or written. It is a bidirectional bus, which means it can carry data both ways, from the BIU to the memory or I/O devices, and vice versa. The data bus of 8086 is 16-bit wide, which means it can transfer 16 bits or 2 bytes of data at a time.
  - Control bus: The control bus is used to send control signals that synchronize the data transfer between the BIU and the memory or I/O devices. It is a bidirectional bus, which means it can carry control signals both ways, from the BIU to the memory or I/O devices, and vice versa. The control bus of 8086 consists of several control lines, such as:

    - Memory/IO: This line indicates whether the BIU is accessing the memory or an I/O device. It is a unidirectional line, which means it can only carry data from the BIU to the memory or I/O devices. When this line is high, it means the BIU is accessing the memory. When this line is low, it means the BIU is accessing an I/O device.
    - Read/Write: This line indicates whether the BIU is performing a read or a write operation. It is a unidirectional line, which means it can only carry data from the BIU to



# Execution Unit

- The execution unit (EU) is one of the two functional units of the 8086 microprocessor. The other functional unit is the bus interface unit (BIU).
- The EU receives program instruction codes and data from the BIU, decodes and executes them, and stores the results in the general registers.
- The EU can also store the data in a memory location or send them to an I/O device by passing the data back to the BIU.
- The EU consists of the following main components:

  - Arithmetic and Logic Unit (ALU): It performs arithmetic and logical operations on 8-bit or 16-bit data. It can also perform bit manipulation and shift/rotate operations. The ALU has a 16-bit accumulator, a 16-bit temporary register, and a 16-bit flag register.
  - Instruction Decoder: It decodes the instruction codes fetched by the BIU and generates the appropriate control signals for the ALU and other components of the EU.
  - Control Unit: It coordinates the activities of the EU and the BIU. It also handles the interrupts and exceptions that may occur during the execution of a program.
  - General Registers: The EU has eight 16-bit general registers that can be used for various purposes. They are:

    - AX: Accumulator Register. It is used for arithmetic, logical, and data transfer operations. It can also be divided into two 8-bit registers: AH (high byte) and AL (low byte).
    - BX: Base Register. It is used as a base pointer for memory access. It can also be divided into two 8-bit registers: BH (high byte) and BL (low byte).
    - CX: Count Register. It is used as a loop counter or a shift/rotate count. It can also be divided into two 8-bit registers: CH (high byte) and CL (low byte).
    - DX: Data Register. It is used as an extension of the accumulator for multiplication and division operations. It can also be divided into two 8-bit registers: DH (high byte) and DL (low byte).
    - SI: Source Index Register. It is used as a source pointer for string operations.
    - DI: Destination Index Register. It is used as a destination pointer for string operations.
    - BP: Base Pointer Register. It is used as a base pointer for stack operations.
    - SP: Stack Pointer Register. It is used as a pointer to the top of the stack.

  - Segment Registers: The EU has four 16-bit segment registers that are used to define the memory segments for code, data, stack, and extra data. They are:

    - CS: Code Segment Register. It holds the base address of the code segment.
    - DS: Data Segment Register. It holds the base address of the data segment.
    - SS: Stack Segment Register. It holds the base address of the stack segment.
    - ES: Extra Segment Register. It holds the base address of the extra data segment.

  - Pointer and Index Registers: The EU has two 16-bit pointer registers and two 16-bit index registers that are used to form effective addresses for memory access. They are:

    - IP: Instruction Pointer Register. It holds the offset address of the next instruction to be executed within the code segment.
    - FLAGS: Flag Register. It holds the status flags that indicate the result of the previous operation. The flags are:

      - CF: Carry Flag. It is set if there is a carry or borrow out of the most significant bit of the result.
      - PF: Parity Flag. It is set if the result has an even number of 1 bits.
      - AF: Auxiliary Carry Flag. It is set if there is a carry or borrow out of the least significant nibble (4 bits) of the result.
      - ZF: Zero Flag. It is set if the result is zero.
      - SF: Sign Flag. It is set if the result is negative.
      - TF: Trap Flag. It is set if the single-step mode is enabled for debugging.
      - IF: Interrupt Flag. It is set if the maskable interrupts are enabled.
      - DF: Direction Flag. It is set if the string operations are performed from high address to low address.
      - OF: Overflow Flag. It is set if there is a signed overflow in the result.

    - BP: Base Pointer Register. It is used as a base pointer for stack operations.
    - SP: Stack Pointer Register. It is used as a pointer to the top of the stack



# Memory Addressing for the Notes of the Unit 3 - Architecture of 8086 Microprocessor

- The 8086 microprocessor is a 16-bit processor that can access up to 1 MB of memory using 20 address lines .
- The memory is organized into segments of 64 KB each, which are identified by four segment registers: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES).
- The 8086 microprocessor uses a technique called **segmented addressing** to generate a 20-bit physical address from two 16-bit registers: a segment register and an offset register.
- The physical address is calculated by multiplying the segment register by 16 (or shifting it left by 4 bits) and adding the offset register. This is called the **segment:offset** notation.
- For example, if CS = 1000H and IP = 2000H, the physical address is 1000H * 16 + 2000H = 12000H. This is written as 1000:2000H.
- The offset register can be one of the following: instruction pointer (IP), stack pointer (SP), base pointer (BP), source index (SI), or destination index (DI).
- The 8086 microprocessor supports seven addressing modes: register, immediate, direct, register indirect, based, indexed, and based indexed .
- In the **register** addressing mode, the operand is stored in a register. For example, MOV AX, BX moves the contents of BX to AX .
- In the **immediate** addressing mode, the operand is a constant value that is part of the instruction. For example, MOV AX, 1234H moves the value 1234H to AX .
- In the **direct** addressing mode, the operand is stored in a memory location whose address is given in the instruction. For example, MOV AX, [1000H] moves the contents of memory location 1000H to AX .
- In the **register indirect** addressing mode, the operand is stored in a memory location whose address is stored in a register. For example, MOV AX, [BX] moves the contents of memory location pointed by BX to AX .
- In the **based** addressing mode, the operand is stored in a memory location whose address is calculated by adding a base register (BP or BX) and a displacement value. For example, MOV AX, [BP+10H] moves the contents of memory location BP+10H to AX .
- In the **indexed** addressing mode, the operand is stored in a memory location whose address is calculated by adding an index register (SI or DI) and a displacement value. For example, MOV AX, [SI+20H] moves the contents of memory location SI+20H to AX .
- In the **based indexed** addressing mode, the operand is stored in a memory location whose address is calculated by adding a base register, an index register, and a displacement value. For example, MOV AX, [BX+SI+30H] moves the contents of memory location BX+SI+30H to AX .
- The 8086 microprocessor has two operating modes: minimum mode and maximum mode. In minimum mode, the 8086 operates as a single processor in a system. In maximum mode, the 8086 operates as a master processor in a multiprocessor system.
- The 8086 microprocessor has three types of instruction sets: data transfer, arithmetic and logic, and control transfer.
- The 8086 microprocessor has three types of instruction formats: one-byte, two-byte, and three-byte. The instruction format consists of an opcode, a mod-reg-r/m byte, and a displacement or immediate data byte.
- The 8086 microprocessor has five types of instructions: data transfer, arithmetic, logic, string, and branch.
- The 8086 microprocessor has two types of interrupts: hardware and software. Hardware interrupts are generated by external devices, such as keyboard, mouse, printer, etc. Software interrupts are generated by the program, such



# Memory Segmentation for the Notes of the Unit 3 - Architecture of 8086 Microprocessor

- Memory segmentation is the process of dividing the memory into segments of various sizes, each with a starting address and a length.
- The main advantage of memory segmentation is that it allows programs to address more than 64 KB of memory, which is the limit of the 16-bit registers.
- The 8086 microprocessor has 20 address lines, which means it can interface 1 MB of memory. However, it segments the memory into 16 64 KB segments, each identified by a 16-bit segment number .
- The 8086 microprocessor works only with four 64 KB segments within the whole 1 MB memory at any instant of time. These four segments are called code segment, data segment, stack segment, and extra segment .
- The code segment contains the instructions to be executed by the processor. The data segment contains the data to be used by the program. The stack segment contains the stack data, such as return addresses and parameters. The extra segment is used for additional data or code.
- The four segment registers, CS, DS, SS, and ES, store the upper 16 bits of the starting addresses of the four segments. The lower 16 bits of the addresses are stored in the offset registers, such as IP, SI, DI, BP, and SP.
- The physical address of any location in the memory is calculated by adding the segment address and the offset address, and multiplying the result by 16. For example, if CS = 1000H and IP = 2000H, then the physical address of the instruction pointer is (1000H + 2000H) * 16 = 12000H.
- The memory segmentation allows the 8086 microprocessor to access different segments of memory using different registers, and to switch between segments by changing the segment registers. This increases the flexibility and efficiency of the memory management.



# Operating modes for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The 8086 microprocessor is a 16-bit, N-channel, HMOS microprocessor that can operate in two modes: minimum mode and maximum mode.
- In minimum mode, the 8086 is the only processor in the system and provides all the control signals for memory and I/O interfacing.
- In maximum mode, the 8086 can work with other processors such as 8087, 8089, or another 8086 and uses a bus controller chip (8288) to generate the control signals.
- The 8086 has a 20-bit address bus and a 16-bit data bus, which allows it to access 1 MB of memory and transfer 16 bits of data at a time.
- The 8086 has 14 registers, which are divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register.
- The general-purpose registers are AX, BX, CX, and DX, which can be used for arithmetic, logic, data transfer, and I/O operations. Each register can be accessed as a 16-bit word or as two 8-bit bytes.
- The segment registers are CS, DS, SS, and ES, which are used to define the four segments of memory: code segment, data segment, stack segment, and extra segment. Each segment register holds the upper 16 bits of the 20-bit segment base address.
- The pointer and index registers are SP, BP, SI, and DI, which are used to store offsets within the segments. SP and BP are used for stack operations, while SI and DI are used for string operations.
- The flag register is a 16-bit register that contains nine flags that indicate the status of the processor after an operation. The flags are carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow.
- The 8086 has a bus interface unit (BIU) and an execution unit (EU), which work in parallel to increase the performance of the processor.
- The BIU is responsible for fetching instructions from memory, decoding them, and sending them to the instruction queue. The BIU also generates the physical addresses for memory and I/O operations by adding the segment base address and the offset address.
- The EU is responsible for executing the instructions from the instruction queue, performing arithmetic and logic operations, and accessing the registers and the stack.
- The 8086 has a two-stage pipeline, which allows it to prefetch up to six bytes of instructions from memory and store them in the instruction queue. The EU can then execute the instructions from the queue without waiting for the BIU to fetch the next instruction.
- The 8086 has a memory addressing scheme that divides the 1 MB of memory into four segments of 64 KB each. Each segment is identified by a segment base address and an offset address. The segment base address is stored in one of the segment registers, while the offset address is specified by the instruction or by one of the pointer or index registers.
- The 8086 has a memory segmentation scheme that allows the programmer to organize the code, data, and stack in different segments of memory. This provides flexibility, modularity, and protection for the programs. The segment registers are used to select the current segment for each type of operation.
- The 8086 has an instruction set that consists of various types of instructions, such as data transfer, arithmetic, logic, control transfer, string, processor control, and interrupt instructions.
- The 8086 has an instruction format that consists of one or more bytes, which include the opcode, the addressing mode, the operands, and the prefixes. The opcode is a 6-bit or 8-bit code that specifies the operation to be performed. The addressing mode is a 2-bit or 4-bit code that specifies how the operands are accessed. The operands are the data or the addresses that are involved in the operation. The prefixes are optional bytes that modify the default segment, size, or direction of the operation.
- The 8086 has an interrupt mechanism that allows the processor to respond to



# Instruction sets for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

- The 8086 microprocessor is a 16-bit microprocessor with a 16-bit internal and external data bus. It can access up to 1 MB of memory with 20 address lines .
- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and Execution Unit (EU)  .
- The Bus Interface Unit (BIU) interfaces 8086 with the external world. It handles all the data transfer functions. It consists of the following components  :
  - Segment registers: These are four 16-bit registers that store the starting addresses of four memory segments: code segment (CS), data segment (DS), stack segment (SS), and extra segment (ES).
  - Instruction pointer (IP): This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
  - Address adder: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O devices.
  - Instruction queue: This is a 6-byte FIFO buffer that prefetches and stores the instructions from the memory for faster execution.
- The Execution Unit (EU) executes the instructions fetched by the BIU. It consists of the following components  :
  - General purpose registers: These are eight 16-bit registers that can be used for various arithmetic and logical operations. They are: accumulator (AX), base (BX), counter (CX), data (DX), source index (SI), destination index (DI), stack pointer (SP), and base pointer (BP).
  - Arithmetic and logic unit (ALU): This is a circuit that performs various arithmetic and logical operations on the data in the registers or memory.
  - Flags register: This is a 16-bit register that stores the status of the ALU operations and some control bits. It has nine active flags: carry (CF), parity (PF), auxiliary carry (AF), zero (ZF), sign (SF), trap (TF), interrupt enable (IF), direction (DF), and overflow (OF).
  - Control unit: This is a circuit that decodes the instructions and generates the control signals for the execution of the instructions.
- The memory addressing of the 8086 microprocessor is based on the concept of memory segmentation. The memory is divided into segments of 64 KB each, and each segment has a 16-bit address. The physical address of a memory location is calculated by multiplying the segment address by 16 and adding the offset address. For example, if the segment address is 1000H and the offset address is 2000H, then the physical address is 1000H * 16 + 2000H = 12000H  .
- The operating modes of the 8086 microprocessor are two: minimum mode and maximum mode. In minimum mode, the 8086 operates as a single processor in a system. In maximum mode, the 8086 operates as a master processor in a multiprocessor system  .
- The instruction set of the 8086 microprocessor is a collection of instructions that the 8086 can execute. The instructions are classified into five types: data transfer instructions, arithmetic instructions, logical instructions, control transfer instructions, and string instructions  .
- The instruction format of the 8086 microprocessor is a binary representation of an instruction. It consists of one or more bytes, each byte having eight bits. The instruction format has three fields: opcode, operand, and prefix  .
  - Opcode: This is the field that specifies the operation to be performed by the instruction. It can be one or two bytes long.
  - Operand: This is the field that specifies the source and destination of the data for the instruction. It can be one, two, or four bytes long. The operands can be registers



# Unit 3 - Architecture of 8086 Microprocessor

- The 8086 microprocessor is a 16-bit microprocessor with a 16-bit internal and external data bus. It can access up to 1 MB of memory with 20 address lines .
- The architecture of the 8086 microprocessor consists of two independent sections or units, the Bus Interface Unit (BIU) and the Execution Unit (EU)  .
- The Bus Interface Unit (BIU) interfaces the 8086 with the external world. It handles all the data transfer functions. It consists of the following components  :
  - Segment registers: These are four 16-bit registers that store the starting addresses of four memory segments: code, data, stack, and extra. Each segment can be up to 64 KB in size.
  - Instruction pointer: This is a 16-bit register that stores the offset address of the next instruction to be executed within the code segment.
  - Address adder: This is a circuit that combines the segment address and the offset address to form a 20-bit physical address that is sent to the memory or I/O device.
  - Instruction queue: This is a 6-byte FIFO buffer that prefetches and stores the instructions from the memory. This improves the speed of execution by reducing the wait states.
- The Execution Unit (EU) executes the instructions fetched by the BIU. It consists of the following components  :
  - General purpose registers: These are eight 16-bit registers that can be used for various arithmetic and logical operations. They can also be accessed as 8-bit registers by using their lower or higher halves. They are: AX, BX, CX, DX, AH, AL, BH, BL, CH, CL, DH, and DL.
  - Pointer and index registers: These are four 16-bit registers that can be used for addressing memory locations. They are: SP (stack pointer), BP (base pointer), SI (source index), and DI (destination index).
  - Arithmetic and logic unit (ALU): This is a circuit that performs various arithmetic and logical operations on the data. It can operate on 8-bit or 16-bit operands.
  - Flag register: This is a 16-bit register that stores the status of the ALU operations and some control bits. It has nine active flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow.
  - Control unit: This is a circuit that decodes the instructions and generates the control signals for the execution of the instructions. It also handles the interrupts and exceptions.
- The 8086 microprocessor has two operating modes: minimum mode and maximum mode  .
  - Minimum mode: This is the mode in which the 8086 operates as a single processor in a system. It uses the MN/MX pin to select this mode. In this mode, the 8086 generates all the control signals for the memory and I/O devices.
  - Maximum mode: This is the mode in which the 8086 operates as a master processor in a multiprocessor system. It uses the MN/MX pin to select this mode. In this mode, the 8086 relinquishes some of the control signals to an external coprocessor, such as the 8087 or the 8089.
- The 8086 microprocessor has a rich instruction set that can perform various operations on data, such as data transfer, arithmetic, logical, shift, rotate, branch, loop, string, and stack  .
- The instruction format of the 8086 microprocessor consists of one to six bytes. Each instruction has an opcode byte that specifies the operation to be performed, and optionally one or two operand bytes that specify the source and destination of the data, and one or two displacement or immediate bytes that specify the offset or constant value  .
- The types of instructions in the 8086 microprocessor are classified into the following categories  :
  - Data transfer instructions: These are instructions that move data between registers, memory, and I/O devices. Examples are: MOV, PUSH, POP, IN, OUT, etc.
  - Arithmetic instructions:



# Types of instructions for the notes of the Unit 3 - Architecture of 8086 microprocessor: register organization, bus interface unit, execution unit, memory addressing, and memory segmentation. Operating modes. Instruction sets, instruction format, Types of instructions. Interrupts: hardware and software interrupts.

## Architecture of 8086 microprocessor

- The 8086 microprocessor is a 16-bit microprocessor that was designed by Intel in 1976.
- It has 20 address lines and 16 data lines that provide up to 1 MB of memory space.
- It consists of two main components: the bus interface unit (BIU) and the execution unit (EU).
- The BIU is responsible for fetching instructions from memory, generating memory addresses, and transferring data to and from memory and I/O devices.
- The EU is responsible for decoding and executing instructions, performing arithmetic and logical operations, and controlling the flags and registers.
- The 8086 microprocessor has 14 registers, divided into four groups: general-purpose registers, segment registers, pointer and index registers, and flag register.
- The general-purpose registers are AX, BX, CX, and DX, each 16-bit wide and can be used as two 8-bit registers (AH, AL, BH, BL, CH, CL, DH, DL).
- The segment registers are CS, DS, SS, and ES, each 16-bit wide and used to store the base addresses of the code, data, stack, and extra segments respectively.
- The pointer and index registers are SP, BP, SI, and DI, each 16-bit wide and used to store the offsets of the stack, base, source, and destination respectively.
- The flag register is a 16-bit register that contains 9 flags: carry, parity, auxiliary carry, zero, sign, trap, interrupt, direction, and overflow.
- The 8086 microprocessor has two operating modes: minimum mode and maximum mode.
- In minimum mode, the 8086 operates as a single processor in a system and uses the pins MN/MX, S0, S1, and S2 for bus control.
- In maximum mode, the 8086 operates as a master processor in a multiprocessor system and uses the pins MN/MX, RQ/GT0, RQ/GT1, and LOCK for bus control.

## Instruction sets, instruction format, and types of instructions

- The 8086 microprocessor supports a powerful instruction set that provides operations like multiplication, division, string manipulation, and interrupts.
- The instruction set consists of 246 instructions, divided into 17 groups.
- The instruction format of the 8086 microprocessor consists of one or more bytes, each byte containing an opcode, an operand, or a prefix.
- The opcode is a 6-bit or 8-bit field that specifies the operation to be performed.
- The operand is a 4-bit, 8-bit, or 16-bit field that specifies the source or destination of the data.
- The prefix is an optional 8-bit field that modifies the operation of the instruction, such as segment override, repeat, lock, or address size.
- The types of instructions supported by the 8086 microprocessor are:
  - Data transfer instructions: These instructions are used to move data between registers, memory, and I/O devices. Examples are MOV, PUSH, POP, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations on data, such as addition, subtraction, multiplication, division, increment, decrement, etc. Examples are ADD, SUB, MUL, DIV, INC, DEC, etc.
  - Bit manipulation instructions: These instructions are used to perform logical operations on data, such as AND, OR, XOR, NOT, etc. Examples are AND, OR, XOR, NOT, TEST, etc.
  - String instructions: These instructions are used to perform operations on strings of data, such as compare, move, scan, load, store, etc. Examples are CMPS, MOVS, SCAS, LODS, STOS, etc.
  - Program execution transfer instructions: These instructions are used to change the sequence of execution of instructions, such as branch, loop, call, return, etc. Examples are JMP, JZ, J



# Interrupts

- Interrupts are signals that cause the CPU to suspend its current program and execute a predefined subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
- Hardware interrupts are triggered by external devices such as keyboards, timers, disk drives, etc. Software interrupts are triggered by instructions in the program such as INT, INTO, BOUND, etc.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR. NMI stands for non-maskable interrupt and INTR stands for maskable interrupt.
- NMI is a high-priority interrupt that cannot be disabled or ignored by the CPU. It is used for critical situations such as power failure, memory parity error, etc.
- INTR is a low-priority interrupt that can be enabled or disabled by the CPU using the EI and DI instructions. It is used for normal device communication such as keyboard input, disk I/O, etc.
- The 8086 microprocessor has 256 types of software interrupts, numbered from 0 to 255. Each interrupt has a corresponding ISR stored in a table called the interrupt vector table (IVT).
- The IVT is located at the beginning of the memory, from address 0000H to 03FFH. Each entry in the IVT is 4 bytes long and contains the segment and offset address of the ISR.
- When an interrupt occurs, the CPU performs the following steps:
  - It pushes the flags register, the code segment register, and the instruction pointer onto the stack.
  - It disables the INTR pin by clearing the IF bit in the flags register.
  - It calculates the address of the IVT entry based on the interrupt type number. For example, if the interrupt type is n, the IVT entry address is 4n.
  - It fetches the segment and offset address of the ISR from the IVT entry and loads them into the code segment register and the instruction pointer, respectively.
  - It executes the ISR until it encounters an IRET instruction, which returns the control to the interrupted program.
  - It pops the instruction pointer, the code segment register, and the flags register from the stack.
  - It resumes the execution of the interrupted program.



# Hardware and Software Interrupts

- An interrupt is a signal that causes the microprocessor to temporarily stop its current task and execute a special subroutine called an interrupt service routine (ISR).
- Interrupts can be classified into two types: hardware interrupts and software interrupts.

## Hardware Interrupts

- Hardware interrupts are caused by external devices that are connected to the microprocessor through dedicated pins.
- The 8086 microprocessor has two hardware interrupt pins: NMI and INTR.
- NMI stands for non-maskable interrupt and it has the highest priority among all interrupts. It cannot be disabled or ignored by the microprocessor. It is usually used for critical events such as power failure or memory parity error.
- INTR stands for interrupt request and it is a maskable interrupt that can be enabled or disabled by the microprocessor using the interrupt enable (IF) flag in the flags register. It has a lower priority than NMI and it is used for normal events such as keyboard input or disk access.
- When a hardware interrupt occurs, the microprocessor performs the following steps:
  - It completes the execution of the current instruction.
  - It pushes the flags register, the code segment (CS) register, and the instruction pointer (IP) register onto the stack. This saves the current state of the program.
  - It clears the IF flag to disable further maskable interrupts.
  - It acknowledges the interrupt by sending a signal to the interrupt controller, which is a separate chip that manages the interrupt requests from various devices.
  - It obtains the interrupt vector, which is a 16-bit address that points to the ISR in the memory. The interrupt vector is stored in a table called the interrupt vector table (IVT) that occupies the first 1 KB of the memory. The IVT has 256 entries, each corresponding to an interrupt type. The interrupt type is determined by the interrupt controller based on the priority and the source of the interrupt.
  - It loads the CS and IP registers with the interrupt vector, which transfers the control to the ISR.
  - It executes the ISR, which performs the necessary actions to handle the interrupt.
  - It executes an IRET (interrupt return) instruction at the end of the ISR, which pops the IP, CS, and flags registers from the stack and restores the original state of the program.
  - It resumes the execution of the program from where it was interrupted.

## Software Interrupts

- Software interrupts are caused by program instructions that are executed by the microprocessor.
- The 8086 microprocessor has 256 software interrupt types, which are identified by numbers from 0 to 255. Each software interrupt type has a corresponding interrupt vector in the IVT.
- Software interrupts are used for various purposes, such as:
  - To request services from the operating system or the BIOS (basic input/output system), such as reading a file, printing a character, or setting the video mode. For example, INT 21H is a software interrupt that invokes the DOS (disk operating system) service routine, which provides various functions for file and device management, memory allocation, and program execution.
  - To implement user-defined subroutines that can be called from different parts of the program. For example, INT 10H is a software interrupt that invokes the user-defined ISR at address 0010H in the memory.
  - To generate exceptions or errors, such as division by zero, overflow, or invalid opcode. For example, INT 0 is a software interrupt that is automatically generated by the microprocessor when a division by zero occurs.
- When a software interrupt occurs, the microprocessor performs the same steps as a hardware interrupt, except that it does not acknowledge the interrupt to the interrupt controller, and it obtains the interrupt vector directly from the interrupt type specified in the instruction. For example, INT 21H is a software interrupt instruction that causes the microprocessor to obtain the interrupt vector from the 21st entry in the IVT.



# Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions that the microprocessor can execute  .
- Assembly language is specific to a given processor, so the syntax and instruction set of 8085 and 8086 are different .
- 8085 is an 8-bit microprocessor that has 74 instructions and 246 opcodes  .
- 8086 is a 16-bit microprocessor that has 133 instructions and 255 opcodes .
- The instructions of 8085 and 8086 can be classified into the following categories   :
  - Data transfer instructions: These instructions are used to move data between registers, memory and I/O devices. Examples are MOV, MVI, LDA, STA, IN, OUT, etc.
  - Arithmetic instructions: These instructions are used to perform arithmetic operations such as addition, subtraction, multiplication, division, increment and decrement. Examples are ADD, SUB, MUL, DIV, INR, DCR, etc.
  - Logic instructions: These instructions are used to perform logical operations such as AND, OR, XOR, NOT, complement, shift and rotate. Examples are ANA, ORA, XRA, CMA, RLC, RRC, etc.
  - Branch instructions: These instructions are used to alter the sequence of execution based on certain conditions. Examples are JMP, JZ, JNZ, JC, JNC, CALL, RET, etc.
  - Looping, counting and indexing instructions: These instructions are used to repeat a block of code for a specified number of times or until a condition is met. They also use index registers to access data in memory. Examples are LOOP, CX, SI, DI, etc.
  - Programming techniques: These are the methods and strategies to write efficient and modular assembly programs. They include using labels, comments, directives, macros, subroutines, etc.
  - Counters and time delays: These are the techniques to generate a specific duration of time by using loops or timers. They are useful for interfacing with devices that require precise timing. Examples are DELAY, TIMER, etc.
  - Stacks and subroutines: These are the techniques to store and retrieve data or return addresses using a special memory area called stack. They are useful for implementing nested or recursive calls, parameter passing, etc. Examples are PUSH, POP, CALL, RET, etc.
  - Conditional call and return instructions: These are the instructions that perform a subroutine call or return only if a certain condition is met. They are useful for reducing the number of branch instructions and simplifying the program flow. Examples are CC, CNC, RC, RNC, etc.



# Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent machine instructions.
- Assembly language is specific to a particular microprocessor, such as intel 8085 or 8086.
- An assembler is a program that converts assembly language to machine language, which is a binary code that the microprocessor can execute.
- Assembly language programming requires knowledge of the microprocessor architecture, instruction set, addressing modes, registers, flags, memory organization, and interfacing devices.

## Instructions

- An instruction is a command that tells the microprocessor what to do.
- An instruction consists of two parts: an opcode and an operand.
- An opcode is a mnemonic that specifies the operation to be performed, such as ADD, MOV, JMP, etc.
- An operand is the data or the address of the data on which the operation is performed. An operand can be a register, a memory location, an immediate value, or a label.
- An instruction can have zero, one, or two operands, depending on the opcode.
- An instruction can be classified into four types: data transfer, arithmetic, logic, and branch.

## Data transfer instructions

- Data transfer instructions are used to move data between registers, memory, and I/O devices.
- The most common data transfer instruction is MOV, which copies the data from the source operand to the destination operand.
- The source and destination operands can be registers, memory locations, or immediate values, but both operands cannot be memory locations at the same time.
- The MOV instruction does not affect any flags in the flag register.
- Some examples of data transfer instructions are:

| Instruction | Description |
| --- | --- |
| MOV A, B | Copy the contents of register B to register A |
| MOV A, M | Copy the contents of the memory location pointed by HL pair to register A |
| MOV M, A | Copy the contents of register A to the memory location pointed by HL pair |
| MOV A, 55H | Copy the immediate value 55H to register A |
| MVI A, 55H | Same as MOV A, 55H |
| LXI H, 1234H | Load the immediate value 1234H to HL pair |
| LDA 2000H | Load the contents of the memory location 2000H to register A |
| STA 3000H | Store the contents of register A to the memory location 3000H |
| LHLD 4000H | Load the contents of the memory locations 4000H and 4001H to HL pair |
| SHLD 5000H | Store the contents of HL pair to the memory locations 5000H and 5001H |
| XCHG | Exchange the contents of HL pair and DE pair |

## Arithmetic instructions

- Arithmetic instructions are used to perform arithmetic operations on data, such as addition, subtraction, multiplication, and division.
- The arithmetic instructions affect the flags in the flag register, such as the carry flag, the sign flag, the zero flag, the parity flag, and the auxiliary carry flag.
- The arithmetic instructions can operate on registers, memory locations, or immediate values, but the result is always stored in the accumulator (register A).
- Some examples of arithmetic instructions are:

| Instruction | Description |
| --- | --- |
| ADD B | Add the contents of register B to the contents of register A and store the result in register A |
| ADD M | Add the contents of the memory location pointed by HL pair to the contents of register A and store the result in register A |
| ADI 55H | Add the immediate value 55H to the contents of register A and store the result in register A |
| ADC B | Add the contents of register B and the carry flag to the contents of register A and store the result in register A |
| ADC M | Add the contents of the memory location pointed by HL pair and the carry flag to the contents of register A and store the result in register A |
| ACI 55H | Add the immediate value 55H and the carry flag to the contents of register A and store the result in register A |
| SUB B | Subtract the contents of register B from the contents of register A and store the result in register A |
| SUB M | Subtract the contents of the memory location pointed by HL pair from the contents of register A and store the result in register A |
| SUI 55H | Subtract the immediate value 55H from the contents of register A and store the result in register



# Notes for Unit 4 - Assembly Language Programming Based on Intel 8085/8086

## Introduction

- Assembly language is a low-level language that uses mnemonics to represent machine instructions.
- Assembly language is specific to a given processor. For example, the assembly language of 8085 is different from that of 8086.
- The microprocessor cannot understand a program written in assembly language. A program known as an assembler is used to convert an assembly language program to machine code.
- Assembly language programming requires a good knowledge of the internal architecture and instruction set of the microprocessor.

## Instructions

- An instruction is a binary pattern that tells the microprocessor to perform a specific operation.
- An instruction consists of two parts: an opcode and an operand.
- The opcode specifies the operation to be performed, such as add, subtract, move, etc.
- The operand specifies the data or the address of the data on which the operation is to be performed.
- An instruction can have zero, one, or two operands, depending on the type of operation.
- An instruction can be classified into three types: data transfer, arithmetic/logic, and branch/loop.

## Data Transfer Instructions

- Data transfer instructions are used to move data between registers, memory, and I/O devices.
- Data transfer instructions do not affect the flags in the flag register.
- Some examples of data transfer instructions are:

  - MOV: moves data from source to destination without affecting the source.
  - MVI: moves immediate data (8-bit or 16-bit) to a register or a memory location.
  - LXI: loads a 16-bit immediate data to a register pair.
  - LDA: loads data from a memory location (specified by a 16-bit address) to the accumulator.
  - STA: stores data from the accumulator to a memory location (specified by a 16-bit address).
  - LDAX: loads data from a memory location (specified by the contents of a register pair) to the accumulator.
  - STAX: stores data from the accumulator to a memory location (specified by the contents of a register pair).
  - LHLD: loads data from two consecutive memory locations (specified by a 16-bit address) to a register pair.
  - SHLD: stores data from a register pair to two consecutive memory locations (specified by a 16-bit address).
  - XCHG: exchanges data between two register pairs.
  - PUSH: pushes data from a register pair to the stack.
  - POP: pops data from the stack to a register pair.
  - IN: reads data from an I/O device (specified by an 8-bit address) to the accumulator.
  - OUT: writes data from the accumulator to an I/O device (specified by an 8-bit address).

## Arithmetic Instructions

- Arithmetic instructions are used to perform arithmetic operations on data, such as addition, subtraction, increment, decrement, etc.
- Arithmetic instructions affect the flags in the flag register, such as carry, sign, zero, parity, and auxiliary carry.
- Some examples of arithmetic instructions are:

  - ADD: adds data from a register or a memory location to the accumulator and stores the result in the accumulator.
  - ADC: adds data from a register or a memory location and the carry flag to the accumulator and stores the result in the accumulator.
  - SUB: subtracts data from a register or a memory location from the accumulator and stores the result in the accumulator.
  - SBB: subtracts data from a register or a memory location and the borrow (complement of carry) from the accumulator and stores the result in the accumulator.
  - INR: increments data in a register or a memory location by one and affects the flags except the carry flag.
  - DCR: decrements data in a register or a memory location by one and affects the flags except the carry flag.
  - INX: increments data in a register pair by one and does not affect the flags.
  - DCX: decrements data in a register pair by one and does not affect the flags.
  - DAD: adds data from a register pair to the HL register pair and stores the result in the HL register pair. The carry flag is affected.
  - DAA: adjusts the result in the accumulator after a binary coded decimal (BCD) addition operation and affects the flags.

## Logic Instructions

- Logic instructions are used to perform logical operations on data, such as AND, OR, XOR, NOT, etc.
- Logic instructions affect the flags in the flag register, such as sign, zero, parity,



# Data Transfer Instructions in 8085/8086 Assembly Language

- Data transfer instructions are the instructions that transfer data in the microprocessor. They are also called copy instructions.
- Data transfer instructions can be classified into four categories: register to register, memory to register, register to memory, and memory to memory.
- Register to register data transfer instructions copy data from one register to another register. For example, MOV A, B copies the contents of register B to register A.
- Memory to register data transfer instructions copy data from a memory location to a register. For example, MOV A, M copies the contents of the memory location pointed by the HL register pair to register A.
- Register to memory data transfer instructions copy data from a register to a memory location. For example, MOV M, A copies the contents of register A to the memory location pointed by the HL register pair.
- Memory to memory data transfer instructions copy data from one memory location to another memory location. For example, MOV M1, M2 copies the contents of the memory location pointed by the DE register pair to the memory location pointed by the HL register pair.
- Data transfer instructions can also transfer data between the accumulator and the I/O ports, or between the stack pointer and the HL register pair.
- Data transfer instructions can also transfer data between the 8085 and the 8086 microprocessors using the XCHG instruction, which exchanges the contents of the HL register pair with the contents of the DE register pair.
- Data transfer instructions can also transfer data between the 8086 and the external devices using the IN and OUT instructions, which transfer data between the accumulator and the I/O ports.
- Data transfer instructions can also transfer data between the 8086 and the memory using the MOV, LDS, LES, LEA, and LAHF instructions, which transfer data between the registers and the memory, or load the effective address or the flags into the registers.
- Data transfer instructions can also transfer data between the 8086 and the string operands using the MOVS, LODS, STOS, CMPS, and SCAS instructions, which transfer data between the string operands pointed by the SI and DI registers, or compare or scan the string operands.
- Data transfer instructions can also transfer data between the 8086 and the segment registers using the MOV, PUSH, and POP instructions, which transfer data between the general registers and the segment registers, or push or pop the segment registers to or from the stack.



# Unit 4 - Assembly Language Programming Based on Intel 8085/8086

## Arithmetic Instructions in 8085 Microprocessor

- Arithmetic instructions are the instructions that perform basic arithmetic operations such as addition, subtraction, increment, and decrement on data stored in registers or memory locations.
- The destination operand of arithmetic instructions is generally the accumulator (register A), which holds the result of the operation.
- The source operand can be a register, a memory location, or an immediate data (8-bit or 16-bit).
- Some arithmetic instructions also affect the flags of the 8085 microprocessor, such as the sign flag (S), the zero flag (Z), the auxiliary carry flag (AC), the parity flag (P), and the carry flag (CY).
- The following table summarizes the arithmetic instructions in 8085 microprocessor, their mnemonics, operands, and functions.

| Mnemonic | Operands | Function |
| --- | --- | --- |
| ADD | r or M | Add the contents of register r or memory location M to the accumulator |
| ADI | data | Add the 8-bit immediate data to the accumulator |
| ADC | r or M | Add the contents of register r or memory location M and the carry flag to the accumulator |
| ACI | data | Add the 8-bit immediate data and the carry flag to the accumulator |
| SUB | r or M | Subtract the contents of register r or memory location M from the accumulator |
| SUI | data | Subtract the 8-bit immediate data from the accumulator |
| SBB | r or M | Subtract the contents of register r or memory location M and the borrow (complement of carry flag) from the accumulator |
| SBI | data | Subtract the 8-bit immediate data and the borrow from the accumulator |
| INR | r or M | Increment the contents of register r or memory location M by 1 |
| INX | rp | Increment the contents of register pair rp by 1 |
| DCR | r or M | Decrement the contents of register r or memory location M by 1 |
| DCX | rp | Decrement the contents of register pair rp by 1 |
| DAD | rp | Add the contents of register pair rp to the HL register pair |
| DAA | - | Adjust the accumulator after a binary coded decimal (BCD) addition |

- The following are some examples of arithmetic instructions in 8085 microprocessor:

```
; Add the contents of register B to the accumulator
ADD B

; Add the 8-bit immediate data 25H to the accumulator
ADI 25H

; Subtract the contents of memory location 2000H from the accumulator
SUB M
LHLD 2000H

; Increment the contents of register C by 1
INR C

; Decrement the contents of register pair BC by 1
DCX B

; Add the contents of register pair DE to the HL register pair
DAD D

; Adjust the accumulator after a BCD addition
DAA
```



# Logic for the notes of the Unit 4 - Assembly language programming based on intel 8085/8086

- Assembly language is a low-level language that uses mnemonics to represent the binary instructions of a microprocessor.
- Assembly language is specific to a given processor. For example, the assembly language of 8085 is different from that of 8086.
- Assembly language programming involves writing the source code in a text editor, assembling it into an object file, and linking it with other object files to generate an executable file.
- The basic elements of assembly language are:
  - Instructions: The commands that tell the microprocessor what to do. Each instruction consists of an operation code (opcode) and zero or more operands.
  - Operands: The data or addresses that are used by the instructions. Operands can be registers, memory locations, immediate values, or labels.
  - Registers: The internal storage locations of the microprocessor that can hold data or addresses. Each register has a name and a size. For example, the 8085 has eight 8-bit registers: A, B, C, D, E, H, L, and F (flags).
  - Memory: The external storage area that can hold data or instructions. Memory is organized into bytes, each with a unique address. For example, the 8085 can address up to 64 KB of memory, from 0000H to FFFFH.
  - Labels: The symbolic names that are used to identify memory locations or instructions. Labels are defined by the programmer and resolved by the assembler.
  - Directives: The commands that tell the assembler how to process the source code. Directives do not generate any machine code. For example, the ORG directive specifies the starting address of the program.
  - Comments: The remarks that are used to explain the source code. Comments are ignored by the assembler. For example, the ; symbol indicates the start of a comment.

- The 8085 and 8086 microprocessors have different instruction sets, addressing modes, and register sets. Some of the differences are:
  - The 8085 is an 8-bit microprocessor, while the 8086 is a 16-bit microprocessor.
  - The 8085 has a single 16-bit address bus and an 8-bit data bus, while the 8086 has a 20-bit address bus and a 16-bit data bus.
  - The 8085 has five addressing modes: immediate, register, direct, register indirect, and implied, while the 8086 has nine addressing modes: immediate, register, direct, register indirect, based, indexed, based indexed, relative, and segment override.
  - The 8085 has eight 8-bit registers: A, B, C, D, E, H, L, and F, while the 8086 has fourteen 16-bit registers: AX, BX, CX, DX, SP, BP, SI, DI, CS, DS, SS, ES, IP, and FLAGS.
  - The 8085 has 74 instructions, while the 8086 has 133 instructions.

- The assembly language programming of the 8085 and 8086 microprocessors involves the following steps:
  - Write the source code in a text editor, using the appropriate syntax, mnemonics, operands, labels, directives, and comments.
  - Assemble the source code into an object file, using an assembler program. The assembler converts the mnemonics into opcodes, resolves the labels into addresses, and generates an object file that contains the machine code and the relocation information.
  - Link the object file with other object files or libraries, using a linker program. The linker combines the object files into a single executable file, resolves the external references, and assigns the final addresses to the segments and symbols.
  - Load the executable file into the memory of the microprocessor, using a loader program. The loader transfers the executable file from the disk or other device to the memory, and sets the program counter to the starting address of the program.
  - Execute the program, using a monitor program or a debugger program. The monitor or debugger allows the user to control the execution of the program, examine or modify the registers or memory, set breakpoints, or trace the program flow.

- The assembly language programming of the 8085 and 8086 microprocessors requires the knowledge of the following topics:
  - Instructions: The types, formats, opcodes, operands, and effects of the instructions of the 8085 and 8086 microprocessors. The instructions can be classified



# Branch Operations

Branch operations are instructions that change the normal sequential flow of execution in a program. They are used to implement control structures such as loops, conditionals, subroutines, etc. Branch operations can be classified into three types:

- **Jump instructions**: These instructions transfer the program control to a specified memory address unconditionally or based on a flag condition. The operand of a jump instruction can be an immediate value, a register, or a memory location. For example, `JMP 1000H` jumps to the address 1000H unconditionally, while `JZ 2000H` jumps to the address 2000H only if the zero flag is set.
- **Call instructions**: These instructions transfer the program control to a subroutine, which is a sequence of instructions that performs a specific task. The call instruction also saves the return address on the stack, so that the program can resume from where it left off after the subroutine is completed. The operand of a call instruction can be an immediate value, a register, or a memory location. For example, `CALL SUB` calls the subroutine named SUB, and pushes the address of the next instruction on the stack.
- **Return instructions**: These instructions transfer the program control back to the main program after a subroutine is finished. The return instruction also pops the return address from the stack, and jumps to that address. The return instruction can be unconditional or conditional based on a flag condition. For example, `RET` returns from a subroutine unconditionally, while `RC` returns only if the carry flag is set.

Some examples of branch operations in assembly language are:

```assembly
; A loop that adds the numbers from 1 to 10 and stores the sum in AX
    MOV AX, 0 ; initialize AX to 0
    MOV CX, 10 ; initialize CX to 10 (loop counter)
LOOP1:
    ADD AX, CX ; add CX to AX
    DEC CX ; decrement CX
    JNZ LOOP1 ; jump to LOOP1 if CX is not zero
    ; AX now contains the sum of 1 to 10
```

```assembly
; A conditional branch that checks if a number in AL is even or odd
    MOV AL, 5 ; initialize AL to 5
    AND AL, 1 ; perform bitwise AND with 1
    JZ EVEN ; jump to EVEN if the result is zero (even number)
    ; otherwise, the number is odd
    ; do something for odd numbers
    JMP END ; jump to END
EVEN:
    ; do something for even numbers
END:
    ; end of program
```



# Looping in Assembly Language Programming

- Looping is a technique that allows a block of statements to be executed repeatedly until a condition is satisfied.
- Looping is useful for performing tasks such as counting, indexing, programming techniques, counters and time delays.
- The assembly language uses the JMP instruction to implement loops. The JMP instruction transfers the control to a specified label unconditionally.
- However, the processor set can also use the LOOP instruction to implement loops conveniently. The LOOP instruction decrements the ECX register and jumps to the specified label unless the ECX register is zero  .
- The LOOP instruction assumes that the ECX register contains the loop count. The loop count is the number of times the loop body is executed.
- The loop body is the block of statements that are repeated in the loop. The loop body should be placed between the label and the LOOP instruction.
- The loop body should not alter the ECX register value, unless it is intended to terminate the loop prematurely.
- The loop body can also contain conditional jumps to exit the loop or to skip some statements based on some conditions.
- The loop body can also contain nested loops, which are loops inside another loop. The nested loops should use different registers for their loop counts, such as EBX, EDX, etc.
- The following is an example of a loop that prints the numbers from 1 to 10 using the INT 21H service:

```assembly
mov ECX, 10 ; loop count
mov AH, 2 ; service to print a character
mov DL, '0' ; initial character
label: ; loop label
add DL, 1 ; increment character
int 21H ; print character
loop label ; repeat loop
```

- The following is an example of a nested loop that prints a 5x5 matrix of asterisks using the INT 21H service:

```assembly
mov ECX, 5 ; outer loop count
outer: ; outer loop label
mov EDX, 5 ; inner loop count
inner: ; inner loop label
mov AH, 2 ; service to print a character
mov DL, '*' ; character to print
int 21H ; print character
dec EDX ; decrement inner loop count
jnz inner ; repeat inner loop if not zero
mov DL, 10 ; line feed character
int 21H ; print line feed
mov DL, 13 ; carriage return character
int 21H ; print carriage return
loop outer ; repeat outer loop
```

