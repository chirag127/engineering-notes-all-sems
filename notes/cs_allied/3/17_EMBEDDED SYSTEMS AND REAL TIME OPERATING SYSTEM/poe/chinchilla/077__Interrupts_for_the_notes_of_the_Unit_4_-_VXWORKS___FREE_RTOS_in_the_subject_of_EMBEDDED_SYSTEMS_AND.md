### Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

Interrupts are a crucial aspect of embedded systems and real-time operating systems (RTOS). Interrupts help in handling events that require immediate attention, such as hardware signals, timers, and software events. The following are some important points to keep in mind when working with interrupts in VXWORKS and FREE RTOS:

1. Interrupt Service Routine (ISR): An ISR is a function that is executed when an interrupt occurs. The ISR is responsible for handling the interrupt and performing the necessary actions. In VXWORKS, ISRs are registered using the `intConnect()` function, while in FREE RTOS, ISRs are registered using the `xQueueSendFromISR()` function.

2. Interrupt Vector Table (IVT): An IVT is a table that contains the addresses of all the ISRs in the system. In VXWORKS, the IVT is stored in memory and can be modified using the `intVecSet()` function. In FREE RTOS, the IVT is created automatically when an ISR is registered.

3. Interrupt Priority: Interrupts can have different priorities, and the priority determines which interrupt is serviced first when multiple interrupts occur simultaneously. In VXWORKS, interrupt priorities are set using the `intPrioritySet()` function, while in FREE RTOS, interrupt priorities are set using the `xQueueCreate()` function.

4. Interrupt Latency: Interrupt latency is the time it takes for the ISR to start executing after the interrupt occurs. Interrupt latency is an important factor to consider when designing real-time systems, as it can affect the system's responsiveness. In VXWORKS, interrupt latency can be reduced by disabling interrupts during critical sections of code using the `intLock()` and `intUnlock()` functions. In FREE RTOS, interrupt latency can be reduced by using the `xQueueSendFromISR()` function to send a message to a task that handles the interrupt.

5. Nested Interrupts: Nested interrupts occur when an interrupt occurs while another interrupt is being serviced. In VXWORKS, nested interrupts are supported, but care must be taken to ensure that the system is not overwhelmed with interrupts. In FREE RTOS, nested interrupts are also supported, but the system must be designed to handle them properly.

6. Interrupt Masking: Interrupt masking is the process of disabling interrupts for a period of time to prevent them from occurring during a critical section of code. In VXWORKS, interrupt masking can be achieved using the `intLock()` and `intUnlock()` functions. In FREE RTOS, interrupt masking can be achieved using the `taskENTER_CRITICAL()` and `taskEXIT_CRITICAL()` functions.

In conclusion, interrupts are a critical aspect of embedded systems and RTOS. Understanding how interrupts work and how to use them effectively is essential for developing reliable and responsive systems. VXWORKS and FREE RTOS provide powerful tools for working with interrupts, and the points mentioned above will help in designing and implementing interrupt-driven systems.