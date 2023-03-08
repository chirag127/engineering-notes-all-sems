### Real Time System

A real time system is a system that must respond to events or inputs within a specified time limit. The system's correctness depends not only on the logical results of the computation, but also on the time at which the results are produced. A real time system can be classified into two types: hard real time system and soft real time system.

#### Hard Real Time System

A hard real time system is a system that must meet the deadlines for all the tasks, otherwise the system will fail. The deadlines are usually very strict and cannot be missed. For example, a flight control system, a nuclear reactor control system, or a pacemaker are hard real time systems. A hard real time system requires a real time operating system (RTOS) that can guarantee the timely execution of the tasks.

#### Soft Real Time System

A soft real time system is a system that can tolerate some degree of deadline misses, but the quality of the service will degrade. The deadlines are usually flexible and can be adjusted according to the system load. For example, a video streaming system, a voice over IP system, or a multimedia system are soft real time systems. A soft real time system can use a general purpose operating system (GPOS) that can provide some real time features, such as priority scheduling, interrupt handling, or memory management.

#### Real Time Operating System (RTOS)

A real time operating system (RTOS) is an operating system that is designed to support real time applications. An RTOS has two key features: predictability and determinism. Predictability means that the system can guarantee the worst-case execution time of the tasks, and determinism means that the system can guarantee the order of the events or inputs. An RTOS typically provides the following functions:

- Real time multithreading: The RTOS can create and manage multiple threads of execution, each with a priority and a deadline. The RTOS can schedule the threads according to the priority and the deadline, and can preempt the lower priority threads when a higher priority thread is ready to run.
- Inter-thread communication and synchronization: The RTOS can provide mechanisms for the threads to communicate and synchronize with each other, such as message queues, semaphores, mutexes, or events. The RTOS can ensure that the communication and synchronization are done in a timely and consistent manner.
- Memory management: The RTOS can allocate and deallocate memory for the threads, and can avoid memory fragmentation and memory leaks. The RTOS can also provide memory protection and isolation for the threads, to prevent unauthorized access or corruption of the memory.
- Input/output management: The RTOS can handle the input/output devices, such as sensors, actuators, or network interfaces, and can provide drivers and protocols for the devices. The RTOS can also support interrupt-driven or polling-based input/output, and can prioritize the input/output requests according to the real time requirements.
- Power management: The RTOS can optimize the power consumption of the system, by adjusting the clock frequency, voltage, or sleep mode of the processor or the devices. The RTOS can also balance the power saving and the performance of the system, according to the real time constraints.

Some possible mnemonics and learning tricks for the topic are:

- To remember the difference between hard and soft real time systems, you can use the acronym HATS: Hard real time systems must Always meet the deadlines, otherwise the system will fail. Soft real time systems can Tolerate some deadline misses, but the quality of the Service will degrade.
- To remember the key features of an RTOS, you can use the acronym PDM: Predictability, Determinism, and Multithreading. An RTOS can guarantee the worst-case execution time of the tasks (Predictability), the order of the events or inputs (Determinism), and the creation and management of multiple threads of execution (Multithreading).
- To remember the functions of an RTOS, you can use the acronym MIMIP: Multithreading, Inter-thread communication and synchronization, Memory management, Input/output management, and Power management. An RTOS can provide these functions to support real time applications.