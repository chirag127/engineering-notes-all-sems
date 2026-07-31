# Basics of RTOS

- RTOS stands for Real-Time Operating System     .
- It is a software system that provides the necessary hard real-time computing capabilities, and it does so in an embedded environment.
- It is used for controlling devices that require timing synchronization with their environment or with other devices.
- It creates multiple threads of software execution and a scheduler for managing these threads.
- It also creates a multi-tasking and deterministic run-time environment.
- It is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- It can be classified into three types based on the time constraints of the tasks:
  - Hard Real-Time operating system: These operating systems guarantee that critical tasks be completed within a range of predefined deadlines.
  - Soft real-time operating system: This operating system provides some relaxation in the time limit. For example, a video streaming application can tolerate some delay in the data transmission.
  - Firm Real-time Operating System: RTOS of this type have to complete the task within the deadline, otherwise, the task is discarded. For example, a sensor data collection application can discard the old data if it is not processed in time.
- Some of the features of an RTOS are :
  - Preemptive scheduling: The scheduler can interrupt a running task and switch to a higher priority task at any time.
  - Fast context switching: The time required to save and restore the state of a task is minimal.
  - Low interrupt latency: The time required to respond to an external event is minimal.
  - Inter-task communication: The tasks can communicate with each other using mechanisms such as message queues, semaphores, mutexes, etc.
  - Memory management: The RTOS can allocate and deallocate memory for the tasks dynamically or statically.
  - Device drivers: The RTOS can provide interfaces to interact with the hardware devices such as sensors, actuators, etc.
  - Debugging and testing tools: The RTOS can provide tools to monitor, debug, and test the performance and functionality of the tasks.