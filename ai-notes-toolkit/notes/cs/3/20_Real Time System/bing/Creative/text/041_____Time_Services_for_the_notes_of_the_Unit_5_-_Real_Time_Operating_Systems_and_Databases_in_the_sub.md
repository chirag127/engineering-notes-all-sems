### Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Time services are the functions and mechanisms that provide the ability to measure, represent, and manipulate time in real-time systems.
- Time services are essential for real-time systems because they enable the following features :
  - Timeliness: the ability to produce the expected result within a defined deadline.
  - Time synchronization: the ability to coordinate independent clocks and operate together in unison.
  - Time representation: the ability to express and store time values in a consistent and accurate manner.
  - Time manipulation: the ability to perform arithmetic and logical operations on time values, such as comparison, addition, subtraction, etc.
- Time services can be implemented by hardware and software components, such as:
  - Clocks: devices that generate periodic signals to measure the passage of time.
  - Timers: devices that generate interrupts or signals after a specified amount of time has elapsed.
  - Schedulers: software modules that manage the execution of tasks according to their priorities and deadlines.
  - Time protocols: software algorithms that synchronize the clocks of different devices or systems.
  - Time libraries: software modules that provide functions and data structures for time representation and manipulation.
- Time services can be classified into two categories, depending on the type of real-time system they support:
  - Hard real-time systems: systems that have absolute deadlines, and if those allotted time spans are missed, a system failure will occur. Examples are air traffic control, nuclear power plant control, etc.
  - Soft real-time systems: systems that continue to function even if they are unable to execute within an allotted time. Examples are web browsing, gaming, etc.