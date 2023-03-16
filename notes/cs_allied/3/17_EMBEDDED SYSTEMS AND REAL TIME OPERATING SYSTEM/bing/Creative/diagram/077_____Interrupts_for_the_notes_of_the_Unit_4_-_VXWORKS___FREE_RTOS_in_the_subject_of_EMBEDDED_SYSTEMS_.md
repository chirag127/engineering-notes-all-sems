### Interrupts for the notes of the Unit 4 - VXWORKS / FREE RTOS in the subject of EMBEDDED SYSTEMS AND REAL TIME OPERATING SYSTEM

- Interrupts are events that occur asynchronously and require immediate attention from the processor.
- Interrupts can be triggered by hardware devices, such as timers, buttons, or communication peripherals, or by software exceptions, such as division by zero, illegal instruction, or memory access violation.
- Interrupts are handled by interrupt service routines (ISRs), which are special functions that run in response to interrupts and perform the necessary actions to service the interrupt source.
- ISRs have some limitations and restrictions, such as:
  - They should be as short and fast as possible, to avoid blocking other interrupts or tasks.
  - They should not use any blocking or non-reentrant functions, such as malloc, printf, or semaphore operations.
  - They should not access any shared resources without proper synchronization, such as mutexes or critical sections.
  - They should not call any RTOS API functions that are not interrupt-safe, such as xQueueSend or xTaskCreate.
- Interrupts can affect the scheduling and timing of RTOS tasks, as they can preempt the execution of tasks and delay their resumption.
- Interrupts can also cause priority inversion, which occurs when a high-priority task is blocked by a low-priority task that is waiting for an interrupt to complete.
- To avoid these problems, RTOSes provide different methods to handle interrupts, such as:
  - Standard ISR processing, which involves running the ISR directly in interrupt context and resuming the interrupted task or switching to a higher-priority task after the ISR returns.
  - Application controlled deferred interrupt handling, which involves deferring some or all of the ISR work to a task or a callback function that runs in task context and can use RTOS API functions.
  - Centralized deferred interrupt handling, which involves using a common mechanism, such as a work queue, to queue the deferred ISR work and execute it in a dedicated task or thread.
- VxWorks and FreeRTOS are two popular open-source RTOSes that support interrupts and provide various features and tools to manage them, such as:
  - VxWorks:
    - It supports nested interrupts, which means that an ISR can be interrupted by another ISR of higher priority.
    - It provides a work queue mechanism, which allows ISRs to defer some of their work to a kernel task that runs at a configurable priority.
    - It provides a watchdog timer mechanism, which allows ISRs to monitor the execution time of tasks and trigger an exception if a task exceeds a specified timeout.
    - It provides an exception handling and diagnostic reporting (ED&R) system, which allows ISRs to handle software exceptions and generate diagnostic information for debugging purposes.
  - FreeRTOS:
    - It supports interrupt nesting, which means that an ISR can be interrupted by another ISR of higher priority, but only if the interrupt controller supports it.
    - It provides an interrupt safe version of queue API, which allows ISRs to read and write data from queues using special functions, such as xQueueSendToBackFromISR and xQueueReceiveFromISR.
    - It provides a software timer mechanism, which allows ISRs to create and start timers that execute a callback function in task context after a specified period.
    - It provides a configASSERT macro, which allows ISRs to check the validity of parameters and conditions and trigger a breakpoint if an assertion fails.

: https://microcontrollerslab.com/freertos-interrupt-management-examples-with-arduino/
: https://www.freertos.org/implementation/a00011.html
: https://scienceprog.com/most-popular-open-source-rtos-comparison-for-embedded-systems/
: https://www.digikey.com/en/maker/projects/introduction-to-rtos-solution-to-part-9-hardware-interrupts/3ae7a68462584e1eb408e1638002e9ed
: https://www.youtube.com/watch?v=tlHLaA8ib1M
: https://learning.windriver.com/vxworks-exceptions-interrupts-and-watchdog-timers