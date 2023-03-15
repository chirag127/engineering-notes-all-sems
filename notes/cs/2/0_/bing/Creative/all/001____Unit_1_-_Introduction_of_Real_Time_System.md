## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems are systems that must meet their deadlines strictly, otherwise they may cause catastrophic failures or unacceptable losses. For example, a nuclear reactor control system, an air traffic control system, or a pacemaker.
  - Soft real time systems are systems that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- Real time systems can also be classified into two types based on the predictability of their workload: periodic systems and aperiodic systems.
  - Periodic systems are systems that have a regular and predictable pattern of events or inputs, such as sensor readings, control signals, or alarms. Periodic systems can be analyzed using techniques such as rate monotonic scheduling, earliest deadline first scheduling, or cyclic executive.
  - Aperiodic systems are systems that have an irregular and unpredictable pattern of events or inputs, such as user requests, network packets, or interrupts. Aperiodic systems can be analyzed using techniques such as sporadic server, polling server, or deferrable server.
- Real time systems face many challenges and trade-offs in their design and implementation, such as:
  - Timing constraints: real time systems must ensure that their tasks meet their deadlines, which may require careful analysis, scheduling, and synchronization of the system components.
  - Resource constraints: real time systems may have limited resources, such as memory, CPU, or power, which may require efficient allocation, management, and optimization of the system resources.
  - Dependability: real time systems must ensure that they function correctly and reliably, even in the presence of faults, errors, or uncertainties, which may require techniques such as fault tolerance, error detection and recovery, or redundancy.
  - Adaptability: real time systems may have to cope with changing requirements, environments, or workloads, which may require techniques such as reconfiguration, self-adaptation, or learning.