### Operating modes

- The 8086 microprocessor has two operating modes: **minimum mode** and **maximum mode**.
- In **minimum mode**, the 8086 is the only processor in the system and provides all the control signals for memory and I/O interfacing.
- In **maximum mode**, the 8086 can work with other processors such as 8087, 8089, 8088, etc. and uses a bus controller chip (8288) to generate the control signals.
- The operating mode is selected by the **MN/MX** pin of the 8086. If it is high (1), the 8086 operates in minimum mode. If it is low (0), the 8086 operates in maximum mode.
- In addition, the 80386 microprocessor and later support a **virtual 8086 mode** that allows the execution of real mode applications in protected mode.