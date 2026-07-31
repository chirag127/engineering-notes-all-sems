## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
- Hard real time systems are systems that must meet all their deadlines, otherwise they may cause catastrophic failures or unacceptable losses. For example, a nuclear reactor control system or an air traffic control system are hard real time systems.
- Soft real time systems are systems that can tolerate some deadline misses, but the quality of service or the user satisfaction may degrade. For example, a video streaming system or a voice recognition system are soft real time systems.
- Real time systems can also be classified into two types based on the predictability of their events or inputs: periodic systems and aperiodic systems.
- Periodic systems are systems that have events or inputs that occur at regular intervals, such as sensor readings, clock ticks, etc. Periodic systems can be analyzed using techniques such as rate monotonic scheduling or earliest deadline first scheduling.
- Aperiodic systems are systems that have events or inputs that occur at irregular or unpredictable intervals, such as user commands, interrupts, faults, etc. Aperiodic systems can be analyzed using techniques such as sporadic server, polling server, or slack stealing.
- Real time systems face many challenges and trade-offs, such as limited resources, concurrency, synchronization, fault tolerance, security, etc. Real time systems must be designed, implemented, tested, and verified carefully to ensure their correctness and efficiency.