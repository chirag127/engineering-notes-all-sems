### Interrupts

- An interrupt is a condition that causes the microprocessor to temporarily work on a different task, and then later return to its previous task.
- Interrupts can be internal or external.
  - Internal interrupts, or "software interrupts," are triggered by a software instruction and operate similarly to a jump or branch instruction.
  - External interrupts, or "hardware interrupts," are triggered by an external device, such as a keyboard, a mouse, a timer, or another microprocessor .
- Interrupts are used for data transfer between the peripheral and the microprocessor, or for handling errors or events that require immediate attention .
- The microprocessor has a fixed number of interrupt lines, which are prioritized according to their importance.
  - The highest priority interrupt is the non-maskable interrupt (NMI), which cannot be ignored by the microprocessor.
  - The lowest priority interrupt is the software interrupt (INTR), which can be enabled or disabled by the microprocessor.
- The microprocessor has an interrupt service routine (ISR) for each interrupt, which is a piece of code that performs the required task or work when the interrupt occurs .
  - The ISR is usually stored in a fixed location in the memory, or in a table called the interrupt vector table (IVT) .
  - The ISR must save the current state of the microprocessor, such as the program counter, the flags, and the registers, before executing the interrupt task .
  - The ISR must restore the saved state of the microprocessor, and return control to the interrupted program, after completing the interrupt task .
- The microprocessor has an interrupt acknowledge (INTA) signal, which is used to communicate with the external device that generated the interrupt .
  - The INTA signal is sent by the microprocessor to the device, to indicate that the interrupt has been recognized and the ISR is being executed .
  - The device can send an interrupt type (or vector) to the microprocessor, to specify which ISR should be executed .
- The microprocessor has an interrupt enable (EI) and an interrupt disable (DI) instruction, which are used to control the interrupt system .
  - The EI instruction sets a flag in the microprocessor, which allows the microprocessor to accept interrupts .
  - The DI instruction clears the flag in the microprocessor, which prevents the microprocessor from accepting interrupts .