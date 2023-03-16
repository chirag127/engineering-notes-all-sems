### Reference Models for Real Time Systems

Real-time systems are computer systems that are designed to interact with the external environment in a timely manner. These systems are used in a wide range of applications, including control systems, multimedia systems, and communication systems. To ensure that real-time systems meet their timing requirements, several reference models have been developed. These models provide a framework for the design and analysis of real-time systems.

1. **Rate Monotonic Scheduling (RMS)**: This is a priority-based scheduling algorithm for periodic tasks. In this model, tasks are assigned priorities based on their periods, with shorter periods being assigned higher priorities. This model is widely used in the design of real-time systems.

2. **Earliest Deadline First (EDF)**: This is another priority-based scheduling algorithm for periodic tasks. In this model, tasks are assigned priorities based on their deadlines, with earlier deadlines being assigned higher priorities. This model is also widely used in the design of real-time systems.

3. **Sporadic Server**: This model is used to handle aperiodic tasks in a real-time system. In this model, a server task is created to handle the execution of aperiodic tasks. The server task is assigned a fixed priority and is scheduled along with the periodic tasks using a priority-based scheduling algorithm.

4. **Constant Bandwidth Server (CBS)**: This is an extension of the sporadic server model. In this model, the server task is assigned a variable priority and is scheduled using the EDF algorithm. This model provides better support for aperiodic tasks in a real-time system.

These are some of the reference models used in the design and analysis of real-time systems. These models provide a framework for ensuring that real-time systems meet their timing requirements. It is important to choose the appropriate model for the specific requirements of the real-time system being designed.