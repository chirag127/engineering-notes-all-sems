### Hard Real time and Soft Realtime

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-world applications.
- A real-time system is one where the correctness of the system depends not only on the logical results of the computations, but also on the time at which the results are produced.
- Real-time systems can be classified into two types: hard real-time and soft real-time   .
- **Hard real-time systems** are deterministic in nature and have absolute deadlines, meaning that the system must complete its tasks within a specified time span, otherwise a system failure will occur .
- Examples of hard real-time systems are air traffic control systems, nuclear power plant control systems, pacemakers, etc .
- **Soft real-time systems** are probabilistic in nature and have flexible deadlines, meaning that the system can tolerate some degree of lateness in completing its tasks, but with a lower quality of output .
- Examples of soft real-time systems are multimedia applications, online gaming, video conferencing, etc .
- The main difference between hard and soft real-time systems is the degree of strictness and the consequence of missing deadlines.
- Hard real-time systems are highly restrictive and do not tolerate any system failure, while soft real-time systems are less strict and can stand the system failure.
- Hard real-time systems require precise timing analysis and verification, while soft real-time systems can use statistical methods and heuristics to estimate the timing performance .
- Hard real-time systems are often implemented using dedicated hardware and specialized software, while soft real-time systems can use general-purpose hardware and software with some modifications .
- Hard real-time systems are more challenging to design, develop, and test, while soft real-time systems are more flexible and adaptable .