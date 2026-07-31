# Time Services for Real Time Operating Systems

- A real time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- A RTOS provides services for real time applications, such as industrial control, flight control, and telephone switching.
- A RTOS allows multiple tasks or programs to run simultaneously but based on their priorities. The task planning unit decides which thread to be executed. The processor stops active work (if any) and starts execution for the high priority task it finds.
- A RTOS is dependent on the clock interrupts. This system produces the Interrupt Service Routine (ISR) interrupts.
- A RTOS provides time services such as:
  - Clock and timer management: A RTOS maintains a system clock that measures the elapsed time since the system started. A RTOS also provides timers that can be used to trigger events or actions after a specified time interval or at a specific time point.
  - Time slicing: A RTOS can divide the CPU time among the ready tasks or threads according to their priorities or other criteria. This allows the tasks or threads to share the CPU and achieve concurrency.
  - Deadline scheduling: A RTOS can schedule the tasks or threads according to their deadlines, which are the time points by which they must finish their execution. A RTOS can also handle the situations when the tasks or threads miss their deadlines or when the deadlines are not feasible.
  - Time synchronization: A RTOS can synchronize the system clock with an external time source, such as a GPS or a network server. This ensures that the system time is accurate and consistent with other systems or devices.