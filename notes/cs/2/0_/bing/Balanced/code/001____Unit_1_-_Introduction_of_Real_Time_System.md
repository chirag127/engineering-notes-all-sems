## Unit 1 - Introduction of Real Time System

A real-time system is a system that can process data and events within predictable and specific time constraints. Real-time systems are often used for applications that require high reliability, safety, and performance, such as flight control systems, industrial automation, robotics, and medical devices.

There are two main types of real-time systems based on their timing constraints:

- **Hard real-time systems**: These systems have absolute deadlines that must be met, otherwise a system failure or a catastrophic consequence will occur. For example, a missile guidance system must compute the correct trajectory and fire the missile within a certain time limit, otherwise the target may be missed or the missile may explode.
- **Soft real-time systems**: These systems have relative deadlines that can be occasionally missed, but the quality of service or the performance of the system will degrade. For example, a video streaming system must deliver the frames to the display device within a certain time limit, otherwise the video quality will be affected or the frames will be dropped.

A real-time system consists of hardware and software components that interact with each other and with the environment. A real-time system typically has the following components:

- **Real-time operating system (RTOS)**: This is a special type of operating system that can handle real-time tasks and events with minimal latency and overhead. An RTOS provides features such as preemptive scheduling, priority-based dispatching, inter-task communication, synchronization, and memory management.
- **Real-time application**: This is the software program that implements the real-time functionality and logic of the system. A real-time application consists of one or more real-time tasks or processes that execute on the RTOS. A real-time task or process has a priority, a deadline, and a set of input and output parameters.
- **Real-time hardware**: This is the physical device or platform that runs the RTOS and the real-time application. A real-time hardware can be a microcontroller, a microprocessor, a field-programmable gate array (FPGA), or a system-on-chip (SoC). A real-time hardware must have sufficient processing power, memory, and input/output (I/O) capabilities to meet the real-time requirements of the system.
- **Real-time environment**: This is the external context or situation that influences the behavior and performance of the real-time system. A real-time environment can be dynamic, unpredictable, noisy, or hostile. A real-time system must be able to sense, adapt, and respond to the changes and events in the real-time environment.