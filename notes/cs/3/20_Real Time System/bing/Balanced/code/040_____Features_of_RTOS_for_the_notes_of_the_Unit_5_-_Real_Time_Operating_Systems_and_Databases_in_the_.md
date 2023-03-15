### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load. An RTOS has the following features   :

- **Small size**: An RTOS is designed to occupy very less memory and consume fewer resources, as it often runs on embedded devices with limited hardware capabilities.
- **Fast response**: An RTOS can quickly switch between tasks and handle interrupts, as it has a low overhead and minimal latency.
- **Determinism**: An RTOS can ensure that tasks will meet their deadlines and respond as expected every time, as it has a fixed scheduling algorithm and priority-based task management.
- **Co-operative or pre-emptive scheduling**: An RTOS can use either co-operative or pre-emptive scheduling to manage tasks. In co-operative scheduling, tasks run until they are completed or voluntarily yield the CPU. In pre-emptive scheduling, tasks are assigned a priority and the highest priority task always runs, while lower priority tasks are suspended or delayed.
- **Main loop or event-driven**: An RTOS can use either a main loop or an event-driven approach to execute tasks. In a main loop, tasks are executed in a fixed order in an infinite loop. In an event-driven approach, tasks are triggered by external or internal events, such as interrupts or timers.