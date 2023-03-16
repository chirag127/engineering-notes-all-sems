### Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- An interrupt is a signal to the processor emitted by hardware or software indicating an event that needs immediate attention.
- An interrupt alerts the processor to a high-priority condition requiring the interruption of the current code the processor is executing.
- The processor responds by suspending its current activities, saving its state, and executing a function called an interrupt handler to deal with the event.
- This interruption is temporary, and, after the interrupt handler finishes, the processor resumes normal activities.
- There are two types of interrupts: hardware interrupts and software interrupts.
- Hardware interrupts are used by devices to communicate that they require attention from the operating system.
- Software interrupts are usually implemented as instructions in the instruction set, which cause a context switch to an interrupt handler similar to a hardware interrupt.
- Interrupts are an important part of an operating system's functionality, as they allow the operating system to respond to asynchronous events.
- In the context of VXWORKS and FREE RTOS, interrupts are used to handle events such as incoming data from a network interface or a timer expiration.
- Both VXWORKS and FREE RTOS provide APIs for configuring and handling interrupts.
- Proper handling of interrupts is crucial for the performance and reliability of real-time systems.
