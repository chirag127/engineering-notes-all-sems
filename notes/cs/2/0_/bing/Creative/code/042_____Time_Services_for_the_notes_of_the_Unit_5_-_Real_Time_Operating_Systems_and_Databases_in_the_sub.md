# Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time system is a system that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.
- A real-time system can be classified into hard real-time and soft real-time based on the timing constraints  .
  - A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
  - A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- Time services are the mechanisms that provide the system with the notion of time and enable the system to measure, compare, and synchronize time.
- Time services are essential for real-time systems because they allow the system to:
  - Schedule tasks and events according to their deadlines and priorities.
  - Monitor the execution time of tasks and events and detect any timing violations.
  - Communicate and coordinate with other real-time systems and devices using a common time reference.
- Time services can be implemented using hardware and software components, such as:
  - Synchronous programming languages, which support the specification and verification of timing constraints and properties.
  - Real-time operating systems (RTOSes), which provide the system with a scheduler, a timer, and a clock.
  - Real-time networks, which enable the system to exchange time-sensitive data and synchronize clocks with other systems and devices.