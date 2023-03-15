## Unit 1 - Introduction of Real Time System

A real time system is a system that can process data and events within a specified time constraint. The system must produce the expected result within a defined deadline, otherwise it may cause a system failure or undesirable consequences. A real time system may also need to coordinate with other systems or devices that operate with different clocks and synchronize their actions.

Some examples of real time systems are:

- Flight control systems
- Industrial automation systems
- Medical devices
- Multimedia systems
- Online gaming systems
- Robotics

Real time systems can be classified into two types based on their timing constraints:

- Hard real time systems: These systems have absolute deadlines that must be met, otherwise the system may fail or cause severe damage. For example, a flight control system must respond to the pilot's commands within milliseconds, otherwise the plane may crash.
- Soft real time systems: These systems have relative deadlines that can be missed occasionally, but the system performance may degrade or the quality of service may be reduced. For example, a video streaming system may drop some frames or reduce the resolution if the network bandwidth is low, but the user can still watch the video.

Real time systems require a special type of operating system that can handle the timing requirements and the concurrency issues of the system. A real time operating system (RTOS) is an operating system that can provide predictable and deterministic response times to the system events and tasks. An RTOS typically has the following features:

- Preemptive scheduling: The RTOS can interrupt a running task and switch to a higher priority task when an event occurs, without waiting for the current task to finish.
- Priority-based scheduling: The RTOS can assign different priorities to different tasks and execute them according to their importance and urgency.
- Inter-task communication and synchronization: The RTOS can provide mechanisms for the tasks to communicate and synchronize with each other, such as message queues, semaphores, mutexes, etc.
- Memory management: The RTOS can allocate and deallocate memory for the tasks and avoid memory fragmentation and leakage.
- Device drivers: The RTOS can provide interfaces for the system to interact with the hardware devices, such as sensors, actuators, network cards, etc.

Some examples of RTOS are:

- FreeRTOS
- VxWorks
- QNX
- RTLinux
- Windows CE