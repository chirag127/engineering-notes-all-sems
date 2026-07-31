# Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time system is a system that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.
- A real-time system can be classified into hard real-time and soft real-time based on the timing constraints  .
  - A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
  - A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- Time services are the mechanisms that provide the functionality of time measurement, time synchronization, and time management in a real-time system.
- Time services are essential for real-time systems because they enable the following:
  - Timeliness: the ability to execute tasks and deliver results within the specified deadlines.
  - Schedulability: the ability to determine the feasibility of a set of tasks and allocate resources accordingly.
  - Predictability: the ability to ensure that the system behavior is consistent and deterministic under all possible scenarios.
  - Fault tolerance: the ability to detect and recover from errors and failures without compromising the system functionality.
- Time services can be implemented using various hardware and software components, such as :
  - Synchronous programming languages: languages that support the specification and verification of timing properties and constraints in the code.
  - Real-time operating systems (RTOSes): operating systems that provide the features and services for real-time applications, such as task scheduling, interrupt handling, inter-process communication, memory management, etc.
  - Real-time networks: networks that support the transmission and reception of data with bounded latency and jitter, such as Ethernet, CAN, TTP, etc.