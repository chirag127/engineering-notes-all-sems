### Interrupt Handling

- An interrupt is a signal to the processor emitted by hardware or software that indicates an event that needs immediate attention.
- Interrupts are indispensable when writing any practical embedded firmware, as they allow the CPU to respond to external events without wasting time in polling.
- Interrupts can be classified into two types: hardware interrupts and software interrupts.
  - Hardware interrupts are triggered by peripheral devices outside the microcontroller, such as timers, sensors, buttons, etc.
  - Software interrupts are called from software, using a specified command, such as a system call or a breakpoint.
- Interrupt handling involves the following steps:
  - When an interrupt occurs, the CPU executes the current instruction, then saves the necessary stack pointer and program counter (PC) information somewhere in RAM allocated for the current function.
  - The CPU then jumps to a predefined address in the memory, where the interrupt service routine (ISR) is stored. The ISR is a special function that performs the task associated with the interrupt source.
  - After the ISR is executed, the CPU restores the stack pointer and PC information from the RAM, and resumes the execution of the interrupted program.
- Interrupts can be masked or unmasked, depending on whether the CPU can accept or ignore them.
  - Masking an interrupt means disabling it temporarily, so that the CPU does not respond to it until it is unmasked.
  - Unmasking an interrupt means enabling it, so that the CPU can respond to it when it occurs.
- Interrupts can also be prioritized, depending on their importance and urgency.
  - Higher priority interrupts can preempt lower priority interrupts, meaning that they can interrupt the execution of the ISR of a lower priority interrupt.
  - Lower priority interrupts can be nested, meaning that they can be executed after the ISR of a higher priority interrupt is completed.
- Interrupt handling in multicore scenarios can be challenging, as there can be conflicts and synchronization issues among the cores.
  - One approach is to assign different interrupt sources to different cores, so that each core handles a subset of interrupts.
  - Another approach is to use a global interrupt controller, which distributes the interrupts to the cores based on some criteria, such as load balancing or affinity.