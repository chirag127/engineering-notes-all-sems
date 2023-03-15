### Functional units of digital system and their interconnections

A digital system is a system that processes and stores data in binary form, using electronic devices such as transistors, logic gates, and memory cells. A digital system can perform various functions, such as arithmetic, logic, control, input, output, and communication.

A digital system consists of several functional units that work together to perform a specific task. The functional units are interconnected by buses, which are sets of wires or lines that carry data, address, and control signals between the units. The main functional units of a digital system are:

- **Input unit**: This unit receives data from external sources, such as keyboards, mouse, microphones, etc. and converts them into binary code that can be processed by the system. The input unit also sends the data to the memory unit or the central processing unit (CPU) through the input bus .
- **Central processing unit (CPU)**: This unit is the brain of the digital system, as it performs all the processing and computation operations. The CPU consists of two subunits: the arithmetic and logic unit (ALU) and the control unit (CU). The ALU performs arithmetic and logic operations on the data, such as addition, subtraction, multiplication, division, and comparison. The CU controls the sequence and timing of the operations, and generates control signals to coordinate the activities of other units. The CPU also communicates with the memory unit and the input/output units through the system bus .
- **Memory unit**: This unit stores data and instructions that are needed by the CPU or the input/output units. The memory unit consists of two types of memory: primary memory and secondary memory. Primary memory, also known as main memory or internal memory, is the memory that is directly accessible by the CPU. It is fast but volatile, meaning that it loses its contents when the power is turned off. Examples of primary memory are random access memory (RAM) and read-only memory (ROM). Secondary memory, also known as auxiliary memory or external memory, is the memory that is not directly accessible by the CPU. It is slow but non-volatile, meaning that it retains its contents even when the power is turned off. Examples of secondary memory are hard disk, floppy disk, CD-ROM, etc. The memory unit also communicates with the CPU and the input/output units through the memory bus .
- **Output unit**: This unit sends data from the system to external devices, such as monitors, printers, speakers, etc. It converts the binary data into a form that can be understood by the user or another system. The output unit also receives data from the memory unit or the CPU through the output bus .

The functional units of a digital system and their interconnections are shown in the following diagram:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Unit   |     |   Memory Unit  |     |   Output Unit  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Input Bus    |     |   Memory Bus   |     |   Output Bus   |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       +----------------------+----------------------+
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
                              |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   AL