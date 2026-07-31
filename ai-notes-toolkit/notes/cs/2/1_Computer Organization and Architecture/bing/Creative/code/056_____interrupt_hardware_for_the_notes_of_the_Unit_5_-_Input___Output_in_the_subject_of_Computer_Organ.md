### Interrupt Hardware

- An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention.
- Interrupts are commonly used by hardware devices to indicate electronic or physical state changes that require time-sensitive attention, such as clicking a mouse, dragging a cursor, printing a document, etc .
- Interrupts are also commonly used to implement computer multitasking, especially in real-time computing. Systems that use interrupts in these ways are said to be interrupt-driven.
- Interrupt hardware consists of the following components :
  - Interrupt Request Line (IRQ): A single request line is used for all the n devices. It is a wire through which devices can send interrupt signals to the processor.
  - Interrupt Service Routine (ISR): A piece of code that is executed when an interrupt occurs. It performs the required work or handles any errors before handing back control to the interrupted application.
  - Interrupt Controller: A device that manages the interrupt requests from multiple devices. It prioritizes the requests and sends them to the processor one by one. It also enables and disables interrupts according to the processor's instructions.
  - Interrupt Vector Table (IVT): A table that stores the addresses of the ISRs for each interrupt type. It is used by the processor to locate the appropriate ISR when an interrupt occurs.
- The interrupt hardware works as follows :
  - When a device needs to interrupt the processor, it sends a signal to the IRQ.
  - The interrupt controller detects the signal and checks the priority of the interrupt request.
  - If the interrupt request has a higher priority than the current task, the interrupt controller sends an interrupt signal to the processor.
  - The processor acknowledges the interrupt signal and saves the current state of the program counter and other registers.
  - The processor uses the IVT to find the address of the ISR for the interrupt type.
  - The processor jumps to the ISR and executes it.
  - The ISR returns control to the processor after completing the required work or handling any errors.
  - The processor restores the saved state of the program counter and other registers and resumes the interrupted task.