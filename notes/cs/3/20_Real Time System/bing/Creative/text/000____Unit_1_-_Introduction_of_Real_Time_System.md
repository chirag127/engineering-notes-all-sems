## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems are systems that must meet their deadlines strictly, otherwise they may cause catastrophic failures or losses. For example, a nuclear reactor control system, a pacemaker, or an anti-lock braking system are hard real time systems.
  - Soft real time systems are systems that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server are soft real time systems.
- Real time systems have some common characteristics, such as concurrency, unpredictability, resource constraints, and dependability.
  - Concurrency means that a real time system may have multiple tasks or processes running simultaneously, and they may need to communicate or synchronize with each other.
  - Unpredictability means that a real time system may face dynamic and uncertain situations, such as varying workload, external disturbances, or faults.
  - Resource constraints means that a real time system may have limited resources, such as memory, CPU, bandwidth, or power, and they may need to be allocated or managed efficiently.
  - Dependability means that a real time system must be able to deliver its services correctly and reliably, even in the presence of faults or errors.
- Real time systems have some common challenges, such as timing analysis, scheduling, synchronization, communication, fault tolerance, and verification.
  - Timing analysis means that a real time system must be able to estimate or measure the worst-case execution time (WCET) of its tasks or processes, and ensure that they can meet their deadlines.
  - Scheduling means that a real time system must be able to assign priorities or orderings to its tasks or processes, and decide when and how to execute them on the available resources.
  - Synchronization means that a real time system must be able to coordinate or control the access or exchange of shared resources or data among its concurrent tasks or processes, and avoid conflicts or deadlocks.
  - Communication means that a real time system must be able to transmit or receive data or messages among its tasks or processes, or with external devices or networks, and ensure the timeliness and correctness of the communication.
  - Fault tolerance means that a real time system must be able to detect or recover from faults or errors that may occur in its hardware, software, or environment, and maintain its functionality or performance.
  - Verification means that a real time system must be able to prove or test its correctness or reliability, and ensure that it meets its specifications or requirements.