# Interrupt management in RTOS environment

- Interrupts are events that occur asynchronously and require immediate attention from the processor.
- Interrupts can be triggered by external devices, such as sensors, timers, or communication interfaces, or by internal sources, such as software exceptions or system calls.
- Interrupts can improve the responsiveness and efficiency of an embedded system, but they can also introduce challenges and complexities, especially when using a real-time operating system (RTOS).
- An RTOS is a software layer that provides services for managing tasks, resources, synchronization, and communication in a real-time system.
- An RTOS typically uses a scheduler to determine which task should run at any given time, based on their priorities and deadlines.
- An RTOS also provides mechanisms for tasks to communicate and synchronize with each other, such as queues, semaphores, mutexes, and events.
- When an interrupt occurs, the processor suspends the current task and jumps to a predefined address, where an interrupt service routine (ISR) is executed.
- An ISR is a special function that handles the interrupt source and performs the necessary actions, such as reading or writing data, clearing flags, or sending signals.
- An ISR should be as short and simple as possible, to minimize the interrupt latency and the impact on the RTOS scheduler and other tasks.
- Interrupt latency is the time between the occurrence of an interrupt and the execution of the corresponding ISR.
- Interrupt latency can be affected by several factors, such as the processor architecture, the interrupt controller, the interrupt priority, the interrupt nesting, and the RTOS configuration.
- Interrupt nesting is the ability of the processor to handle multiple interrupts at the same time, by allowing higher priority interrupts to preempt lower priority ones.
- Interrupt nesting can reduce the interrupt latency for critical interrupts, but it can also increase the stack usage and the complexity of the ISR code.
- When using an RTOS, the ISR should not perform any complex or time-consuming operations, such as memory allocation, file access, or blocking calls.
- Instead, the ISR should defer most of the processing to another thread, such as a task, by using the RTOS services, such as queues, semaphores, events, or software timers.
- This way, the ISR can return quickly and allow the RTOS scheduler to resume the normal execution of the tasks, while the deferred processing can be done at a lower priority and with proper synchronization.
- The RTOS services that can be used from an ISR are usually marked as "fromISR" or "ISR safe" in the RTOS documentation or API.
- These services are designed to be fast and deterministic, and to avoid any conflicts or deadlocks with the RTOS scheduler or other tasks.
- Some examples of RTOS services that can be used from an ISR are:

  - xQueueSendFromISR: Sends a message to a queue from an ISR.
  - xSemaphoreGiveFromISR: Gives a semaphore from an ISR.
  - xEventGroupSetBitsFromISR: Sets one or more bits in an event group from an ISR.
  - xTimerPendFunctionCallFromISR: Defers the execution of a function to a timer service task from an ISR.

- The use of these services from an ISR may require some additional steps, such as:

  - Enabling the interrupt source and setting the interrupt priority in the interrupt controller.
  - Registering the ISR function with the RTOS interrupt dispatcher or the interrupt vector table.
  - Calling the RTOS yield function at the end of the ISR, to request a context switch if a higher priority task is ready to run.

- The following code snippet shows an example of an ISR that uses the FreeRTOS API to defer the processing of a UART interrupt to a task:

```c
// UART ISR
void vUARTHandler(void)
{
  // Declare a variable to hold the received byte
  char cRxedChar;
  // Declare a variable to indicate if a context switch is needed
  BaseType_t xHigherPriorityTaskWoken = pdFALSE;
  // Read the received byte from the UART register
  cRxedChar = UART_RX_REG;
  // Send the received byte to a queue
  xQueueSendFromISR(xRxQueue, &cRxedChar, &xHigherPriorityTaskWoken);
  // Clear the UART interrupt flag
  UART_INT_FLAG = 0;
  // Request a context switch if a higher priority task is ready to run
  portYIELD_FROM_ISR(xHigherPriorityTaskWoken);
}
```

- The following code snippet shows an example of a task that receives the bytes from the queue and processes them: