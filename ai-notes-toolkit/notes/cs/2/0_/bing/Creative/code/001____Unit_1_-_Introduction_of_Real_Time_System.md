## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems are systems that must meet their deadlines strictly, otherwise they may cause catastrophic failures or losses. For example, a nuclear reactor control system, an air traffic control system, or a pacemaker.
  - Soft real time systems are systems that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- Real time systems can also be classified into two types based on the predictability of their inputs or events: periodic systems and aperiodic systems.
  - Periodic systems are systems that have inputs or events that occur at regular intervals, such as sensor readings, clock ticks, or data packets. Periodic systems can be analyzed using techniques such as rate monotonic scheduling, earliest deadline first scheduling, or cyclic executive.
  - Aperiodic systems are systems that have inputs or events that occur at irregular or unpredictable intervals, such as user commands, interrupts, or faults. Aperiodic systems can be analyzed using techniques such as sporadic server, polling server, or deferrable server.
- Real time systems face many challenges and trade-offs, such as limited resources, concurrency, synchronization, fault tolerance, security, testing, verification, etc. Real time systems require careful design, implementation, and evaluation to ensure their correctness, efficiency, and robustness.