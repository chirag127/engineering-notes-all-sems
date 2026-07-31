### Interrupts

- An interrupt is a condition that causes the microprocessor to temporarily work on a different task, and then later return to its previous task.
- Interrupts can be internal or external.
  - Internal interrupts, or "software interrupts," are triggered by a software instruction and operate similarly to a jump or branch instruction.
  - External interrupts, or "hardware interrupts," are triggered by an external device or signal that needs the microprocessor's attention .
- Interrupts are used for data transfer between the peripheral and the microprocessor, error handling, timing and synchronization, and event-driven processing .
- The microprocessor has a dedicated interrupt request (IRQ) line that can be activated by an external device to signal an interrupt .
- The microprocessor also has an interrupt acknowledge (INTA) line that is used to acknowledge the receipt of an interrupt and to request the device to send the interrupt vector.
- The interrupt vector is a number that identifies the interrupt and the corresponding interrupt service routine (ISR) that needs to be executed.
- The microprocessor has a priority logic that determines which interrupt to service first if multiple interrupts are pending.
- The microprocessor also has an interrupt enable (IE) flag that can be set or cleared by software to enable or disable interrupts .
- The microprocessor follows a sequence of steps to handle an interrupt :
  - It completes the current instruction and saves the program counter (PC) and the flags on the stack.
  - It clears the IE flag to disable further interrupts.
  - It sends a low signal on the INTA line to acknowledge the interrupt and request the interrupt vector from the device.
  - It receives the interrupt vector and uses it to fetch the address of the ISR from a predefined memory location.
  - It jumps to the ISR and executes it.
  - It restores the PC and the flags from the stack and sets the IE flag to enable interrupts.
  - It returns to the interrupted program and resumes execution.