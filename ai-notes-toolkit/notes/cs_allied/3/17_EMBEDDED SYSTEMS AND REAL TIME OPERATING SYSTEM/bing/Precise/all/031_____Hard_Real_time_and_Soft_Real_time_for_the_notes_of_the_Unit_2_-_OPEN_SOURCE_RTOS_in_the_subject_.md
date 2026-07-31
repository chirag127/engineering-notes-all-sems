# Hard Real-time and Soft Real-time

Real-time systems are classified into two types: hard real-time and soft real-time.

## Hard Real-time
- Hard real-time systems are those in which the correctness of the system depends not only on the logical correctness of the output but also on the time at which the output is produced.
- In hard real-time systems, missing a deadline is considered a system failure.
- Examples of hard real-time systems include air traffic control systems, missile guidance systems, and pacemakers.

## Soft Real-time
- Soft real-time systems are those in which the system can tolerate some degree of lateness in meeting deadlines.
- In soft real-time systems, missing a deadline may result in degraded system performance, but it is not considered a system failure.
- Examples of soft real-time systems include multimedia systems, online gaming, and virtual reality systems.

These concepts are important in the study of real-time operating systems, particularly in the context of open-source RTOS for embedded systems. Understanding the differences between hard and soft real-time systems can help in the selection and design of appropriate RTOS for a given application.