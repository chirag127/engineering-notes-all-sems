# Hard Real Time and Soft Real Time

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-time applications.
- A real-time application is one that requires a timely and predictable response from the system.
- There are two types of real-time systems: hard real-time and soft real-time .

## Hard Real Time

- A hard real-time system is one where the time taken is deterministic to an exact moment.
- A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
- A hard real-time system is highly restrictive and does not tolerate any system failure.
- Examples of hard real-time systems are nuclear power plants, air traffic control systems, pacemakers, etc.

## Soft Real Time

- A soft real-time system is one where the time taken is deterministic to a range of values.
- A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- A soft real-time system is less strict and can stand the system failure.
- Examples of soft real-time systems are multimedia applications, online gaming, video conferencing, etc.