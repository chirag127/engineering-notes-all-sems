# Unit 1 - Introduction of Real Time System

- A real-time system is a system that can process data and events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization) .
- A real-time system can be classified into two types based on the timing constraints: hard real-time system and soft real-time system .
  - A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur . For example, flight control systems, nuclear power plants, etc.
  - A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail . For example, video streaming, online gaming, etc.
- A real-time system requires a real-time operating system (RTOS) that can manage the system resources and tasks with a scheduler, data buffers, or fixed task priorities .
- A real-time system can have various applications in domains such as robotics, industrial automation, healthcare, aerospace, etc. .