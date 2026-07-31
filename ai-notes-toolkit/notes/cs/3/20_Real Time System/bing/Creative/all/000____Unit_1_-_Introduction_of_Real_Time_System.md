## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to perform its intended function or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems have strict deadlines that must be met at all costs, otherwise the system may fail catastrophically or cause severe damage. For example, a pacemaker must deliver electrical pulses to the heart within a certain time interval, otherwise the patient may die.
  - Soft real time systems have deadlines that are desirable but not mandatory, and missing some deadlines may only degrade the system performance or quality of service. For example, a video streaming service may drop some frames or reduce the resolution if the network bandwidth is insufficient, but the user can still watch the video.
- Real time systems have some common characteristics and challenges, such as:
  - Concurrency: Real time systems often have to handle multiple events or tasks simultaneously, and coordinate their execution and communication.
  - Predictability: Real time systems must be able to guarantee that they can meet their deadlines under all possible scenarios and conditions, and avoid any unexpected delays or failures.
  - Resource constraints: Real time systems often have limited resources, such as memory, CPU, power, bandwidth, etc., and must optimize their utilization and allocation.
  - Dependability: Real time systems must be able to cope with faults, errors, or uncertainties, and ensure their correctness, reliability, availability, and security.
- Real time systems require special design methods, tools, and techniques, such as:
  - Real time operating systems (RTOS): An RTOS is a specialized operating system that provides services and features for real time systems, such as scheduling, synchronization, communication, memory management, etc.
  - Real time programming languages (RTPL): An RTPL is a programming language that supports the development of real time systems, such as providing timing constructs, concurrency mechanisms, exception handling, etc.
  - Real time analysis and verification: Real time analysis and verification are techniques that aim to ensure the correctness and feasibility of real time systems, such as checking the timing constraints, resource requirements, fault tolerance, etc.
  - Real time testing and debugging: Real time testing and debugging are techniques that aim to detect and correct the errors or defects of real time systems, such as measuring the timing behavior, tracing the execution, injecting faults, etc.