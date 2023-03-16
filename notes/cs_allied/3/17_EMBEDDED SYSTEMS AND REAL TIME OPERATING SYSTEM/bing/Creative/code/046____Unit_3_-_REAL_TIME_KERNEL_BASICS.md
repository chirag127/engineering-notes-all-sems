## Unit 3 - REAL TIME KERNEL BASICS

- A real time kernel is a software component that manages the execution of tasks in a real time system.
- A real time system is a system that must respond to events within a specified time constraint, such as a control system, a multimedia system, or a communication system.
- A task is a unit of work that can be executed by the kernel. A task can be periodic, aperiodic, or sporadic, depending on its activation pattern.
- A periodic task is activated at regular intervals, such as every 10 milliseconds. An aperiodic task is activated by an external event, such as a button press. A sporadic task is activated by an external event, but has a minimum inter-arrival time, such as a sensor reading.
- A real time kernel must schedule the tasks according to their priority, deadline, and resource requirements, while ensuring that no task misses its deadline.
- A real time kernel can use different scheduling algorithms, such as rate-monotonic, earliest deadline first, or fixed priority preemptive scheduling, depending on the characteristics of the tasks and the system.
- A real time kernel can also provide other services, such as inter-task communication, synchronization, memory management, and exception handling, to support the development of real time applications.