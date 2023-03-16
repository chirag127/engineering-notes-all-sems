### UNIX as RTOS

- UNIX is a time-sharing operating system that manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a real-time operating system (RTOS) because it does not guarantee timing requirements of the processes under its control.
- A RTOS is an operating system that processes data and events that have critically defined time constraints.
- A RTOS is distinct from a time-sharing OS like UNIX in the following aspects:
  - A RTOS has a deterministic scheduler that assigns priorities to tasks and executes them according to their deadlines.
  - A RTOS has a minimal interrupt latency that allows it to respond quickly to external events.
  - A RTOS has a predictable memory management that avoids fragmentation and swapping of memory pages.
  - A RTOS has a preemptive kernel that can interrupt any task to run a higher priority task.
  - A RTOS has a real-time clock that provides accurate timing information for the system and the tasks.
- Some examples of RTOS are QNX, VxWorks, FreeRTOS, and RTLinux.
- RTLinux is a variant of Linux that adds real-time capabilities to the Linux kernel .
- RTLinux uses a microkernel that runs the Linux kernel as a low priority task and handles real-time tasks as high priority tasks .
- RTLinux can be used for applications that require both general purpose computing and real-time computing, such as aerospace, robotics, and industrial control .