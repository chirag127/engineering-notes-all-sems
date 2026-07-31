### Reference Models for Real Time Systems

Real-time systems are computer systems that are designed to interact with the external environment in a timely manner. These systems are used in a variety of applications, including control systems, multimedia systems, and communication systems. To ensure that real-time systems meet their timing requirements, several reference models have been developed. These models provide a framework for the design and analysis of real-time systems.

1. **Rate Monotonic Scheduling (RMS)**: This model is used for scheduling periodic tasks in a real-time system. In this model, tasks are assigned priorities based on their periods, with shorter periods being assigned higher priorities. The RMS model guarantees that all tasks will meet their deadlines if the total utilization of the system is less than or equal to a specific bound.

2. **Earliest Deadline First (EDF)**: This model is used for scheduling tasks with deadlines in a real-time system. In this model, tasks are assigned priorities based on their deadlines, with earlier deadlines being assigned higher priorities. The EDF model guarantees that all tasks will meet their deadlines if the total utilization of the system is less than or equal to 100%.

3. **Sporadic Server**: This model is used for scheduling aperiodic tasks in a real-time system. In this model, a server task is used to handle the execution of aperiodic tasks. The server is assigned a specific capacity and period, and it can execute aperiodic tasks whenever it has available capacity.

4. **Constant Bandwidth Server (CBS)**: This model is an extension of the sporadic server model. In this model, the server is assigned a specific bandwidth, which determines the amount of CPU time that the server can use in each period. The CBS model guarantees that the server will not exceed its assigned bandwidth, and it can be used to provide temporal isolation between different tasks in a real-time system.

These are some of the reference models used in the design and analysis of real-time systems. Each model has its own strengths and limitations, and the choice of model depends on the specific requirements of the system being designed.