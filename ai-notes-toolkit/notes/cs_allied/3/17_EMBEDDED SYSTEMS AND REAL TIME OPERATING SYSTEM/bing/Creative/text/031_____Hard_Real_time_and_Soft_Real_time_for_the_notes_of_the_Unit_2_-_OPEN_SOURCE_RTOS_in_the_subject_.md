### Hard Real time and Soft Realtime

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-world applications.
- A real-time system is one where the correctness of the system depends not only on the logical results of the computations, but also on the time at which the results are produced.
- A real-time system can be classified into two types: hard real-time and soft real-time, based on the consequences of missing a deadline.
- A deadline is the maximum allowable time for a task to complete its execution.

#### Hard Real-Time Systems

- A hard real-time system is one where the time taken is deterministic to an exact moment.
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
- A hard real-time system is highly restrictive and doesn’t tolerate any system failure.
- A hard real-time system is deterministic in nature, meaning that the behavior of the system can be predicted exactly.
- Examples of hard real-time systems are nuclear power plants, air traffic control systems, pacemakers, etc.

#### Soft Real-Time Systems

- A soft real-time system is one where the time taken is deterministic to a range of moments.
- A soft real-time system has flexible deadlines, and if those allotted time spans are missed, the system continues to function but with undesirable lower quality of output.
- A soft real-time system is less strict and can stand the system failure.
- A soft real-time system is probabilistic in nature, meaning that the behavior of the system can be predicted with some probability.
- Examples of soft real-time systems are multimedia applications, online gaming, video conferencing, etc.

: https://techdifferences.com/difference-between-hard-and-soft-real-time-systems.html
: https://www.geeksforgeeks.org/difference-between-hard-real-time-and-soft-real-time-system/
: https://learn.microsoft.com/en-us/windows/iot/iot-enterprise/soft-real-time/soft-real-time
: https://www.intel.com/content/www/us/en/robotics/real-time-systems.html