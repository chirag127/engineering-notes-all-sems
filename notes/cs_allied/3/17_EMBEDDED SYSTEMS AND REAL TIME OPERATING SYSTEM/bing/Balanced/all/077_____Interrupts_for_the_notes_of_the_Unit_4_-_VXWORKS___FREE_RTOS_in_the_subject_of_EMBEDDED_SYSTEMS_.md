# Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Interrupts are events that occur asynchronously and notify the CPU that it should take some action.
- Interrupts can be triggered by hardware devices, such as timers, sensors, keyboards, etc., or by software exceptions, such as division by zero, illegal instruction, etc.
- Interrupts are handled by interrupt service routines (ISRs), which are special functions that run when an interrupt occurs and perform the necessary actions to service the interrupt.
- Interrupts are important for real-time embedded systems, as they allow the system to respond quickly and deterministically to external stimuli and events.
- Interrupts can also be used to wake up blocked tasks in a real-time operating system (RTOS), which are tasks that are waiting for some condition or event to occur before resuming execution.
- Interrupts can affect the performance and behavior of an RTOS, as they can preempt the running task and delay the scheduling of other tasks. Therefore, interrupts need to be managed carefully and efficiently by the RTOS.
- Different RTOSes have different methods and mechanisms to handle interrupts, such as interrupt priority levels, interrupt masking, interrupt nesting, interrupt latency, interrupt synchronization, etc.
- VxWorks and FreeRTOS are two popular RTOSes that are used for embedded systems. They have some similarities and differences in how they handle interrupts.

## VxWorks

- VxWorks is a preemptive, deterministic RTOS that prioritizes real-time embedded applications.
- VxWorks has low latency and minimal jitter, which means that it can respond to interrupts quickly and consistently.
- VxWorks has many security features that address the evolving security threats connected devices face at every stage, from boot-up to operation to data transfer to powered off.
- VxWorks supports multiple interrupt priority levels, which can be configured by the user. Higher priority interrupts can preempt lower priority interrupts, and lower priority interrupts can be masked by higher priority interrupts.
- VxWorks supports interrupt nesting, which means that an ISR can be interrupted by another ISR of higher priority. This allows the system to handle multiple interrupts without losing any interrupt requests.
- VxWorks supports interrupt synchronization, which means that an ISR can communicate with a task or another ISR using semaphores, message queues, signals, etc. This allows the system to coordinate the actions of different components in response to an interrupt.
- VxWorks supports interrupt-driven task activation, which means that an ISR can wake up a blocked task using a semaphore, a message queue, a signal, etc. This allows the system to resume the execution of a task that is waiting for an interrupt event.

## FreeRTOS

- FreeRTOS is a free, open-source, and portable RTOS that supports a wide range of embedded platforms.
- FreeRTOS is designed to be simple, small, and scalable, which means that it can run on constrained devices with limited resources.
- FreeRTOS offers various methods to handle interrupts that differ in both latency and the consumption of resources. These methods include, Standard ISR processing, Application Controlled Deferred Interrupt Handling, and Centralised Deferred Interrupt Handling.
- Standard ISR processing is the simplest and fastest method, which involves writing the ISR code directly in the interrupt vector table. This method has the lowest latency, but it also consumes the most resources and can interfere with the RTOS scheduler.
- Application Controlled Deferred Interrupt Handling is a more flexible and efficient method, which involves writing the ISR code in a separate function and calling it from the interrupt vector table using a macro. This method allows the ISR to defer some of its actions to a lower priority task, which reduces the interrupt latency and the resource consumption. However, this method requires the user to manage the synchronization and communication between the ISR and the deferred task.
- Centralised Deferred Interrupt Handling is a more advanced and automated method, which involves using a generic ISR that handles all interrupts and passes the interrupt requests to a queue. This method allows the RTOS to manage the synchronization and communication between the ISR and the deferred task, which simplifies the user code and reduces the interrupt latency and the resource consumption. However, this method requires the user to configure the RTOS tick interrupt and the interrupt queue.
- FreeRTOS supports interrupt-driven task activation, which means that an ISR can wake up a blocked task using a semaphore, a message queue, a signal,