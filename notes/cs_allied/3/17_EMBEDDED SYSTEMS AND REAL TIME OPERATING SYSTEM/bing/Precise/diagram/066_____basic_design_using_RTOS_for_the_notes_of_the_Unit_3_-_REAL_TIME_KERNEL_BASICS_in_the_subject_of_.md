### Basic Design using RTOS

- An RTOS is an operating system designed to manage hardware resources of an embedded system; it creates multiple threads of software execution and a scheduler for managing these threads.
- RTOS are built with a preemptive multitasking design paradigm, which is what allows tasks to switch from one to another based on need.
- Write short interrupt routines, but not too short.
- Large number of tasks has pros such as better control of the priorities and by this of the relative response times, better modularity, cleaner code, and more effective encapsulation of data.
- Large number of tasks also has cons such as more data sharing, more semaphores, more time on handling them and more bugs, more time on message passing between tasks.
- Avoid creating and destroying tasks while the system is running, because it is time consuming, it may be difficult to destroy a task without leaving something behind, and it may be better to create all the tasks at system startup and leave them.
- Use RMS (Rate Monotonic Scheduling) to verify your design. RMS is an analysis technique that designers can use to test their assumptions about whether the tasks in their system can be scheduled successfully.