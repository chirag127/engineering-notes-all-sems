### Interrupts

- An interrupt is a condition that causes the microprocessor to temporarily work on a different task, and then later return to its previous task.
- Interrupts can be internal or external.
  - Internal interrupts, or "software interrupts," are triggered by a software instruction and operate similarly to a jump or branch instruction.
  - External interrupts, or "hardware interrupts," are triggered by an external device, such as a keyboard, a mouse, a timer, or another microprocessor .
- Interrupts are used for data transfer between the peripheral and the microprocessor, or for handling errors or events that require immediate attention .
- The microprocessor has a fixed number of interrupt lines, which are prioritized according to their importance.
  - The highest priority interrupt is the non-maskable interrupt (NMI), which cannot be ignored by the microprocessor.
  - The lowest priority interrupt is the software interrupt (INTR), which can be enabled or disabled by the microprocessor.
- The microprocessor responds to an interrupt by completing the current instruction, saving the program counter and the status register on the stack, and jumping to a predefined address called the interrupt vector .
- The interrupt vector contains the address of the interrupt service routine (ISR), which is a program that performs the required task or handles the error .
- The ISR must end with a return from interrupt (RETI) instruction, which restores the program counter and the status register from the stack, and resumes the interrupted program .
- The microprocessor can handle multiple interrupts by using a technique called interrupt nesting, which allows a higher priority interrupt to interrupt a lower priority interrupt .
  - The lower priority interrupt is suspended until the higher priority interrupt is serviced .
  - The microprocessor can also use an interrupt controller, which is a device that manages the interrupt requests and signals the microprocessor accordingly .