### Hard Real Time and Soft Real Time

- A real-time operating system (RTOS) is a type of operating system that is designed to meet the timing constraints of real-time applications.
- A real-time application is one that has to respond to external events within a specified time limit, such as controlling a robot, processing sensor data, or playing audio or video.
- Real-time systems can be classified into two categories: hard real-time and soft real-time, based on the consequences of missing a deadline.
- A deadline is the maximum time allowed for a task to complete its execution.
- A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
- A system failure can result in catastrophic consequences, such as loss of life, property, or money.
- Examples of hard real-time systems are air traffic control, nuclear power plant control, and pacemakers.
- A hard real-time system is deterministic in nature, meaning that it can guarantee the worst-case execution time of every task.
- A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system continues to function but with undesirable lower quality of output.
- A lower quality of output can result in reduced performance, user dissatisfaction, or loss of revenue.
- Examples of soft real-time systems are video streaming, online gaming, and voice over IP.
- A soft real-time system is probabilistic in nature, meaning that it can estimate the average or expected execution time of every task, but not the worst-case.
- A soft real-time system can tolerate some deadline misses, but not too frequently or too severely.
- A soft real-time system can trade off between timeliness and quality of service.