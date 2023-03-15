# Time Services for Real Time Operating Systems

- A real time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- A RTOS provides services for real time applications, such as industrial control, flight control, and telephone switching.
- A RTOS allows multiple tasks or programs to run simultaneously but based on their priorities.
- A RTOS uses a task scheduler to decide which thread to be executed, and can preempt the current task if a higher priority task arrives.
- A RTOS relies on clock interrupts to produce the interrupt service routine (ISR) that handles the incoming events.
- A RTOS also provides services for inter-thread communication and synchronization, such as message queues, semaphores, mutexes, and event flags.
- A RTOS also provides services for memory management, such as dynamic memory allocation, memory pools, and memory protection.
- A RTOS can be classified into two types: hard real time and soft real time.
  - A hard real time system guarantees that the deadlines of all tasks are met, and any failure to do so can result in a catastrophic consequence.
  - A soft real time system tries to meet the deadlines of most tasks, but some occasional delays are acceptable and do not cause a major impact.
- Some examples of RTOS are Azure RTOS ThreadX, FreeRTOS, VxWorks, QNX, and LynxOS .