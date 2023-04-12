

## Unit 1 - Introduction of Real Time System

A real time system is a system that must respond to events or inputs within a specified time limit. The correctness of a real time system depends not only on the logical results of the computations, but also on the time at which the results are produced.

Some examples of real time systems are:

- Air traffic control system
- Nuclear power plant control system
- Industrial automation system
- Multimedia system
- Online gaming system
- Embedded system

Some characteristics of real time systems are:

- They have deadlines for completing tasks or responding to events
- They have concurrency, meaning that multiple tasks or events can occur simultaneously and need to be coordinated
- They have unpredictability, meaning that the occurrence and duration of tasks or events can vary and are not known in advance
- They have resource constraints, meaning that they have limited memory, processing power, bandwidth, energy, etc.
- They have dependability, meaning that they have to be reliable, available, safe, secure, etc.

Some challenges of designing and developing real time systems are:

- They have to meet the timing requirements and guarantee the deadlines
- They have to manage the concurrency and synchronization of tasks or events
- They have to handle the unpredictability and uncertainty of tasks or events
- They have to optimize the resource utilization and allocation
- They have to ensure the dependability and quality of service

Some techniques and tools for designing and developing real time systems are:

- Real time scheduling algorithms, such as rate-monotonic, earliest deadline first, etc.
- Real time operating systems, such as VxWorks, QNX, RTLinux, etc.
- Real time communication protocols, such as CAN, Ethernet, Bluetooth, etc.
- Real time modeling and analysis methods, such as UML, Petri nets, statecharts, etc.
- Real time testing and verification tools, such as simulators, emulators, debuggers, etc.



### Definition of Real Time System

- A real time system is a system that can process and respond to input data within a specified time constraint, which is often determined by the environment or the application .
- A real time system is also able to synchronize its internal clock with external clocks and operate in unison with other systems.
- A real time system can be classified into two types based on the severity of the consequences of missing the deadline:
  - A hard real time system has absolute deadlines, and any delay or failure to meet them can result in catastrophic outcomes, such as loss of life or damage to property. Examples are flight control systems, nuclear power plant control systems, etc.
  - A soft real time system has relative deadlines, and some delay or failure to meet them can result in degraded performance or quality of service, but not fatal consequences. Examples are video streaming, online gaming, etc.



### Typical Real Time Applications

A real-time application (RTA) is an application that requires a program to respond to stimuli within a certain time. RTAs often involve concurrent processes that must be synchronized and coordinated. RTAs are used in various domains, such as:

- **Video conferencing**: This is an application that allows users to communicate with each other using video and audio over the internet. It requires low latency and high bandwidth to ensure smooth and clear transmission of data. It also requires synchronization of audio and video streams, as well as encryption and compression of data. 
- **Voice over Internet Protocol (VoIP)**: This is an application that allows users to make phone calls over the internet. It requires low latency and high quality of service to ensure clear and uninterrupted voice communication. It also requires packetization, encoding, decoding, and routing of voice data. 
- **Online gaming**: This is an application that allows users to play games with other users over the internet. It requires low latency and high reliability to ensure fair and consistent gameplay. It also requires synchronization of game states, events, and actions, as well as authentication and security of data. 
- **Community storage applications**: These are applications that allow users to store and share data over the internet. They require high availability and scalability to ensure access and performance of data. They also require replication, consistency, and fault tolerance of data. 
- **Some e-commerce applications**: These are applications that allow users to buy and sell goods and services over the internet. They require high responsiveness and accuracy to ensure customer satisfaction and business efficiency. They also require transaction processing, inventory management, and payment processing. 
- **Real-time operating system (RTOS)**: This is an application that manages the resources and tasks of a real-time system. It requires high predictability and determinism to ensure timely and correct execution of tasks. It also requires scheduling, memory management, and interrupt handling. 
- **Instant messaging (IM) applications**: These are applications that allow users to send and receive text, voice, and video messages over the internet. They require low latency and high availability to ensure instant and continuous communication. They also require encryption, compression, and delivery of messages. 
- **Team collaboration applications**: These are applications that allow users to work together on projects over the internet. They require high concurrency and consistency to ensure coordination and collaboration of work. They also require version control, conflict resolution, and notification of changes. 
- **Digital control**: This is an application that uses sensors and actuators to control physical processes, such as temperature, pressure, speed, etc. It requires high precision and stability to ensure safety and quality of control. It also requires sampling, filtering, and feedback of signals.  
- **Optimal control**: This is an application that uses mathematical models and algorithms to optimize the performance of physical processes, such as fuel consumption, energy efficiency, etc. It requires high accuracy and adaptability to ensure optimal and robust control. It also requires modeling, simulation, and optimization of systems.  
- **Command and control**: This is an application that uses sensors and actuators to monitor and control complex systems, such as military, aerospace, transportation, etc. It requires high reliability and security to ensure safety and effectiveness of control. It also requires data acquisition, processing, and dissemination.  
- **Signal processing**: This is an application that uses mathematical techniques to analyze and manipulate signals, such as audio, video, image, etc. It requires high speed and quality to ensure fidelity and functionality of signals. It also requires transformation, filtering, compression, and enhancement of signals.  
- **Tracking**: This is an application that uses sensors and actuators to track the position and movement of objects, such as vehicles, people, animals, etc. It requires high accuracy and responsiveness to ensure identification and localization of objects. It also requires detection, estimation, and prediction of trajectories.  
- **Real-time databases**: These are applications that use databases to store and retrieve data that have temporal constraints, such as deadlines, freshness, etc. They require high consistency and timeliness to ensure validity and availability of data. They also require concurrency control, transaction management, and recovery.  
- **Multimedia**: These are applications that



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events within a specified time interval, otherwise it may cause undesirable consequences or failure.
- A real time system consists of a set of tasks that have deadlines to meet, and a scheduler that assigns priorities and execution order to the tasks.
- A task is a unit of work that can be executed by a processor. A task can be periodic, aperiodic, or sporadic, depending on its arrival pattern.
- A periodic task is a task that arrives at regular intervals, and has a fixed execution time and deadline. For example, a task that reads a sensor every 10 milliseconds and has a deadline of 15 milliseconds is a periodic task.
- An aperiodic task is a task that arrives at irregular intervals, and has a variable execution time and deadline. For example, a task that handles user input or network packets is an aperiodic task.
- A sporadic task is a task that arrives at unpredictable intervals, and has a minimum inter-arrival time, a variable execution time, and a deadline. For example, a task that responds to an emergency signal is a sporadic task.
- The release time of a task is the time when the task becomes available for execution. For a periodic task, the release time is equal to the arrival time. For an aperiodic or sporadic task, the release time is determined by the scheduler, based on the task's priority and the availability of the processor.
- The release time of a task is important for the analysis and design of a real time system, as it affects the feasibility, schedulability, and performance of the system. A feasible system is a system that can meet all the deadlines of the tasks. A schedulable system is a system that has a feasible schedule, i.e., a sequence of task executions that meets all the deadlines. A performance metric is a measure of the quality of service of the system, such as response time, utilization, or throughput.
- The release time of a task can be computed by using different algorithms, depending on the type of the task and the scheduling policy of the system. Some common algorithms are:
  - Earliest Deadline First (EDF): This algorithm assigns the highest priority to the task with the earliest deadline, and releases the task as soon as it arrives. This algorithm is optimal for a single processor system, i.e., it can schedule any set of tasks that is feasible on a single processor.
  - Rate Monotonic (RM): This algorithm assigns the highest priority to the task with the shortest period, and releases the task at the beginning of each period. This algorithm is optimal for a set of periodic tasks on a single processor system, i.e., it can schedule any set of periodic tasks that is feasible on a single processor.
  - Least Laxity First (LLF): This algorithm assigns the highest priority to the task with the least laxity, where laxity is the difference between the deadline and the remaining execution time of the task. This algorithm releases the task as soon as it arrives. This algorithm is also optimal for a single processor system, but it requires more dynamic priority changes than EDF or RM.
  - Fixed Priority (FP): This algorithm assigns a fixed priority to each task, and releases the task as soon as it arrives. The priority can be based on any criteria, such as deadline, period, or importance. This algorithm is not optimal for a single processor system, i.e., there may exist some sets of tasks that are feasible on a single processor, but cannot be scheduled by this algorithm. However, this algorithm is simpler and more practical than the optimal algorithms, and can be extended to multiprocessor systems.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by **Friday, 24 March 2023**.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in a clear and concise manner, using proper terminology and notation.
- The notes should include diagrams, tables, graphs, and equations wherever necessary to illustrate the concepts and methods.
- The notes should be formatted according to the guidelines given in the syllabus and the assignment instructions.
- The notes should be submitted in a PDF file via the online portal before the deadline.
- Late submissions will be penalized by 10% of the total marks for each day of delay.
- Plagiarism will not be tolerated and will result in a zero mark for the assignment.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must produce the correct results within a specific time frame, otherwise it may cause undesirable consequences or failures  .
- Timing constraints are the requirements that specify the deadlines or the acceptable ranges of response times for the real-time system  .
- Timing constraints are essential for ensuring the timeliness and the correctness of the real-time system, as well as for coordinating the actions of multiple agents or components in the system .
- Timing constraints can be classified into two categories :
  - Performance constraints: These are the constraints that define the desired or acceptable response times of the system or its tasks. For example, a performance constraint may specify that a task must finish within 10 milliseconds after an event occurs.
  - Reliability constraints: These are the constraints that define the maximum tolerable response times of the system or its tasks. For example, a reliability constraint may specify that a task must finish within 20 milliseconds after an event occurs, otherwise the system will fail or degrade.
- Timing constraints can be further classified into three types based on their relation to events or tasks :
  - Hard constraints: These are the constraints that must be met by the system or its tasks at all times, otherwise the system will fail or cause catastrophic consequences. For example, a hard constraint may specify that a task must finish before a deadline, otherwise the system will crash or damage the equipment.
  - Soft constraints: These are the constraints that should be met by the system or its tasks as often as possible, but occasional violations are acceptable or tolerable. For example, a soft constraint may specify that a task should finish before a deadline, but a small delay will not affect the system significantly or cause noticeable degradation.
  - Firm constraints: These are the constraints that must be met by the system or its tasks until a certain point, after which the results are useless or irrelevant. For example, a firm constraint may specify that a task must finish before a deadline, otherwise the results will be discarded or ignored by the system or the user.
- Timing constraints can be expressed using various constructs or notations in the requirements or specifications of the real-time system. Some of the common constructs are:
  - Temporal operators: These are the symbols or keywords that indicate the temporal relations or properties of events or tasks, such as before, after, within, until, etc.
  - Temporal intervals: These are the ranges or bounds of time values that specify the deadlines or the acceptable response times of events or tasks, such as [0, 10], (5, 15], etc.
  - Temporal variables: These are the variables or parameters that represent the time values or durations of events or tasks, such as t, d, T, etc.
  - Temporal expressions: These are the formulas or equations that combine the temporal operators, intervals, and variables to define the timing constraints of events or tasks, such as t < 10, d = T - t, etc.
- Timing constraints can be validated or verified using various methods or techniques, such as testing, simulation, analysis, or formal methods. Some of the common methods are:
  - Testing: This is the method of executing the real-time system or its tasks under different scenarios or inputs and measuring or observing the actual response times or behaviors of the system or its tasks, and comparing them with the expected or specified timing constraints.
  - Simulation: This is the method of modeling the real-time system or its tasks using a software or hardware tool and running the model under different scenarios or inputs and estimating or predicting the response times or behaviors of the system or its tasks, and comparing them with the expected or specified timing constraints.
  - Analysis: This is the method of applying mathematical or logical techniques or algorithms to the real-time system or its tasks and calculating or deriving the worst-case or best-case response times or behaviors of the system or its tasks, and comparing them with the expected or specified timing constraints.
  - Formal methods: This is the method of using rigorous or precise languages or notations to specify the real-time system or its tasks and the timing constraints, and using automated or semi-automated tools or procedures to check or prove the consistency or correctness of the specification or the satisfaction of the timing constraints.



### Hard Real Time Systems

- A hard real-time system is a system that must produce the expected result within a defined deadline, otherwise it will cause a system failure or a catastrophic consequence  .
- A hard real-time system has absolute deadlines, meaning that missing even a single deadline is unacceptable and intolerable .
- A hard real-time system is usually found interacting at a low level with physical hardware, such as sensors, actuators, controllers, etc., in embedded systems.
- Examples of hard real-time systems are flight control systems, nuclear reactor control systems, air traffic control systems, pacemakers, etc .
- A hard real-time system requires a real-time operating system (RTOS) that can provide predictable and deterministic scheduling, interrupt handling, synchronization, and communication .
- A hard real-time system must be designed and verified with rigorous methods and tools to ensure its correctness, reliability, and safety .



### Soft Real Time Systems

- A soft real time system is a system that has **flexible deadlines** for completing its tasks, meaning that missing some deadlines occasionally is **acceptable** and does not cause **critical consequences**  .
- A soft real time system can **tolerate** some **jitter** or **delay** in the execution of its tasks, as long as the overall **quality of service** is maintained .
- A soft real time system can run on **multiple cores** and impose **fewer restrictions** on the applications than a hard real time system.
- Some examples of soft real time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video applications.
  - Online gaming and virtual reality systems.
  - Multimedia systems and user interfaces.



### Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements :
  - A workload model: It specifies the applications supported by the system, such as tasks, jobs, parameters, deadlines, resource dependencies, etc. It can be represented by a precedence graph or a task graph .
  - A resource model: It describes the resources available to the system, such as CPU, memory, network, sensors, actuators, etc. It also defines the types and relations of the resources, such as shared, dedicated, preemptive, non-preemptive, etc. It can be represented by a resource graph .
  - A service model: It defines the policies and mechanisms used by the system to allocate resources to the workload, such as scheduling algorithms, synchronization protocols, admission control, etc. It can be represented by a service graph .
- An example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .
- A reference model can be used to analyze, design, implement, and evaluate real time systems, as well as to compare and contrast different real time systems .



### Processors and Resources for Real Time System

- A real time system is a system that must respond to events or inputs within a specified time window, often with strict deadlines and constraints.
- A real time system consists of hardware and software components that work together to process, analyze, and act on the incoming data in real time.
- Processors and resources are two important components of a real time system that affect its performance, reliability, and functionality.

#### Processors

- Processors are also known as active resources. They are essential for the execution of a job. A job is a unit of work that must be completed by a real time system.
- A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission links.
- Processors can be classified into two types: single-processor and multiprocessor systems.
- Single-processor systems have only one processor that executes all the jobs in the system. They are simpler, cheaper, and easier to program than multiprocessor systems. However, they have limited processing power and may not be able to handle complex or concurrent jobs.
- Multiprocessor systems have two or more processors that can execute jobs in parallel or distributed manner. They are more powerful, scalable, and flexible than single-processor systems. However, they are more expensive, complex, and challenging to program and coordinate than single-processor systems.
- Processors can also be classified into two types: general-purpose and dedicated processors.
- General-purpose processors are multipurpose and can serve a wide range of use cases, which include data crunching in the cloud and data centers, gaming and media PCs, office laptop, and devices at the edge. They have more compute within the allotted time window.
- Dedicated processors are specialized and optimized for specific real time applications, such as industrial control, automotive, robotics, and aerospace. They have more predictable and deterministic behavior and can meet strict timing and performance requirements.
- Intel® Time Coordinated Computing (Intel® TCC) enabled processors are examples of dedicated processors that deliver optimal compute and time performance for real time applications. They can pair with Intel® Ethernet Controllers featuring IEEE 802.1 Time-Sensitive Networking (TSN), or with any number of other popular networking devices to power complex real time systems .

#### Resources

- Resources are also known as passive resources. A job may or may not require a resource during its execution. A resource is a shared entity that can be used by one or more jobs at a time. Example: memory, disk, printer, sensor, actuator.
- Resources can be classified into two types: preemptable and non-preemptable resources.
- Preemptable resources can be taken away from a job before it finishes using them. They can be allocated and deallocated dynamically based on the priority and demand of the jobs. Example: memory, disk, processor.
- Non-preemptable resources cannot be taken away from a job before it finishes using them. They can be allocated and deallocated only at the beginning and end of the job. Example: printer, sensor, actuator.
- Resources can also be classified into two types: consumable and reusable resources.
- Consumable resources are depleted after being used by a job. They can be replenished or regenerated after some time or by some external action. Example: battery, fuel, ink.
- Reusable resources are not depleted after being used by a job. They can be used again by another job without any delay or intervention. Example: memory, disk, processor.
- Resources can also be classified into two types: local and global resources.
- Local resources are accessible only by the jobs running on the same processor or node. They have lower access time and overhead than global resources. Example: cache, register, local memory.
- Global resources are accessible by the jobs running on any processor or node in the system. They have higher access time and overhead than local resources. Example: disk, network, shared memory.



### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>-</sub>, r<sub>+</sub>] (jitter).
  - Absolute deadline (d<sub>i</sub>): The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - Relative deadline (D<sub>i</sub>): The maximum time allowed for a job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval [(r<sub>i</sub>, d<sub>i</sub>]: The time interval in which a job can be feasibly executed. It is equal to D<sub>i</sub>.
- The temporal parameters of a job determine its urgency, priority, and schedulability in a real time system. They also affect the performance metrics of the system, such as response time, utilization, and deadline miss ratio.



### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline.
- Phase is the time at which the first instance of the task is released.
- Period is the time interval between two consecutive releases of the task.
- Execution time is the worst-case time required by the task to complete its execution.
- Deadline is the time by which the task must finish its execution.
- A periodic task can be represented by a tuple: T = <Φ, P, e, D> where Φ is the phase, P is the period, e is the execution time, and D is the deadline.
- A periodic task can also be represented by a timeline diagram, showing the release times, execution times, and deadlines of the task instances.
- The periodic task model is a deterministic workload model that can accurately capture many hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission.
- The periodic task model has some assumptions and limitations, such as:
  - The task parameters are known and fixed.
  - The task execution time does not depend on the input data or the system state.
  - The task instances are independent and do not share any resources.
  - The task instances are released exactly at the start of their periods.
- The periodic task model can be extended by adding some parameters, such as:
  - Jitter, which is the maximum deviation of the actual release time of a task instance from the exact start time of its period.
  - Offset, which is the time difference between the release time of a task instance and the start of its hyperperiod.
  - Priority, which is the relative importance of a task among other tasks.
  - Utilization, which is the ratio of the execution time to the period of a task.




Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on precedence constraints and data dependency for the notes of the unit 1 - Introduction of Real Time System in the subject of Real Time System.

### Precedence Constraints and Data Dependency

- Precedence constraints are the restrictions on the order of execution of jobs in a real time system. They are usually represented by a directed graph, where the vertices are the jobs and the edges indicate the precedence relation. For example, if job J1 must finish before job J2 can start, then there is an edge from J1 to J2 in the graph  .
- Data dependency is the situation where the output of one job is used as the input of another job in a real time system. Data dependency can affect the schedulability and correctness of the system, as the jobs need to synchronize and communicate via shared data. Data dependency cannot be captured by a precedence graph, as it does not imply a fixed order of execution .
- Some examples of precedence constraints and data dependency in real time systems are:
  - A control system that consists of a sensor, a controller and an actuator. The sensor reads the input from the environment, the controller computes the output based on the input, and the actuator applies the output to the environment. The controller depends on the sensor for the input data, and the actuator depends on the controller for the output data. The sensor, the controller and the actuator also have precedence constraints, as they need to execute in a specific order to achieve the desired control effect.
  - A multimedia system that plays a video stream. The video stream consists of frames that are encoded and decoded by different jobs. The decoder job depends on the encoder job for the encoded frames, and the display job depends on the decoder job for the decoded frames. The encoder, the decoder and the display jobs also have precedence constraints, as they need to execute in a timely manner to avoid jitter and lag in the video playback.



## Unit 2 - Real Time Scheduling

Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines. Real time scheduling aims to ensure that the system can respond to events and requests in a timely and predictable manner, without missing any deadlines or compromising the quality of service. Real time scheduling is essential for applications that require high performance, reliability, and safety, such as industrial control, robotics, multimedia, and embedded systems.

Some of the topics covered in this unit are:

- **Real time system**: A system that has to respond to events or requests within a specified time interval, or risk failure or degradation of service. A real time system consists of the scheduler, clock, and the processing hardware elements. A real time system can be classified as hard, soft, or firm, depending on the consequences of missing a deadline. 
- **Real time task**: A task that has a timing constraint or deadline associated with its execution. A real time task can be periodic, aperiodic, or sporadic, depending on the pattern of its arrival. A real time task can also be preemptive or non-preemptive, depending on whether it can be interrupted by a higher priority task or not.  
- **Real time scheduling algorithm**: An algorithm that determines the order and timing of task execution in a real time system. A real time scheduling algorithm can be static or dynamic, depending on whether the task parameters and priorities are fixed or variable. A real time scheduling algorithm can also be optimal or heuristic, depending on whether it guarantees to meet all the deadlines or not. Some examples of real time scheduling algorithms are rate-monotonic, earliest deadline first, least laxity first, and round-robin.  
- **Real time scheduling analysis**: The process of evaluating, testing, and verifying the performance and correctness of a real time scheduling system and the algorithms employed. Real time scheduling analysis involves measuring and comparing the parameters such as utilization, response time, deadline miss ratio, and schedulability of the system and the tasks. Real time scheduling analysis can be done using analytical methods, simulation methods, or empirical methods.



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning tasks to processors or resources in a way that meets the timing constraints of the system. Real time systems are those whose correctness depends on both functionality and timing. There are different approaches to real time scheduling, depending on the characteristics and requirements of the system and the tasks. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks (such as arrival time, execution time, deadline, period, etc.) are known at design time. In this approach, the scheduling decisions are made at specific time instants, which are chosen a priori before the system begins its execution. A table or a cyclic executive is used to specify which task or segment of code should be executed at each time instant. The advantage of this approach is that it is simple, predictable, and easy to verify. The disadvantage is that it is inflexible, inefficient, and cannot handle dynamic or aperiodic tasks  .

- **Priority-driven approach**: This approach is also known as event-driven or preemptive approach. It is mainly used for soft or firm real time systems, where some of the properties of the tasks (such as arrival time, execution time, deadline, etc.) are not known at design time or may vary at run time. In this approach, the scheduling decisions are made whenever a task arrives, completes, or is preempted by another task. Each task is assigned a priority, which may be static or dynamic, and the scheduler always selects the highest priority task to run. The advantage of this approach is that it is flexible, efficient, and can handle dynamic or aperiodic tasks. The disadvantage is that it is complex, unpredictable, and hard to verify  .

- **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority and are scheduled in a circular order. Each task is allocated a time slice or a quantum, which is the maximum amount of time it can run before being preempted by the next task in the queue. The advantage of this approach is that it is fair, simple, and easy to implement. The disadvantage is that it does not consider the timing constraints or the importance of the tasks, and may cause deadline misses or poor performance .

- **Weighted round-robin approach**: This approach is a variation of round-robin approach, where the tasks have different weights or priorities, and are scheduled in a circular order according to their weights. Each task is allocated a time slice or a quantum, which is proportional to its weight or priority. The advantage of this approach is that it is fair, simple, and can accommodate different levels of importance of the tasks. The disadvantage is that it still does not consider the timing constraints of the tasks, and may cause deadline misses or poor performance .

- **Hybrid approach**: This approach is a combination of different approaches, such as clock-driven and priority-driven, or round-robin and priority-driven. It is used to exploit the benefits of each approach and overcome their limitations. For example, a hybrid approach may use a clock-driven scheduler for periodic tasks and a priority-driven scheduler for aperiodic tasks, or a round-robin scheduler for low-priority tasks and a priority-driven scheduler for high-priority tasks. The advantage of this approach is that it is adaptable, efficient, and can handle different types of tasks. The disadvantage is that it is complex, unpredictable, and hard to verify  .



### Clock Driven Approach

- Clock driven scheduling is also called as time-driven scheduling.
- When scheduling is clock driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock driven scheduler computes a static schedule for the jobs before the system starts to execute.
- The static schedule is periodic and cyclic, meaning that it repeats itself after a fixed amount of time .
- The scheduler uses a clock to trigger the execution of the jobs according to the static schedule.
- The clock driven approach is suitable for real-time systems that require predictable and deterministic behaviour.
- The advantages of clock driven scheduling are :
  - It is easy to verify the schedulability of the system and guarantee the deadlines of the jobs.
  - It avoids the overhead of dynamic scheduling decisions and context switches.
  - It eliminates the possibility of priority inversion and timing anomalies.
- The disadvantages of clock driven scheduling are :
  - It is inflexible and cannot handle aperiodic or sporadic jobs easily.
  - It is inefficient and may waste processor time if the jobs are not evenly distributed.
  - It is sensitive to changes in the system parameters and may require recomputation of the schedule.



### Weighted Round Robin Approach

- The weighted round robin approach is a generalization of the round robin approach for scheduling real-time tasks or traffic.
- In the round robin approach, each ready task gets an equal share of the processor for a fixed time quantum, and the tasks are served in a circular order.
- In the weighted round robin approach, each ready task gets a fixed number of time quanta, as specified by its weight, and the tasks are served in a circular order.
- The weight of a task reflects its relative importance or priority, and influences the portion of the processor time it receives.
- The weighted round robin approach is mainly used for scheduling real-time traffic in high-speed switched networks, where different types of traffic may have different bandwidth requirements and quality of service guarantees.
- The advantages of the weighted round robin approach are that it is simple, fair, and easy to implement.
- The disadvantages of the weighted round robin approach are that it may not be optimal for some real-time tasks, and it may suffer from high context switching overhead and poor cache performance.



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Examples of static priority-driven scheduling algorithms are rate-monotonic scheduling (RMS) and deadline-monotonic scheduling (DMS).
- Examples of dynamic priority-driven scheduling algorithms are earliest deadline first (EDF) and least laxity first (LLF).
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to prioritize critical tasks and reduce the interference from non-critical tasks.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as the lack of a unified priority model, the heterogeneity of hardware platforms, and the complexity of the middleware layer.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters are known in advance and do not change during execution. A **dynamic system** is one where the tasks and their parameters may vary unpredictably at run time.
- Static systems can be validated offline, whereas dynamic systems may require online verification and adaptation. Static systems are more suitable for hard real-time systems that have strict timing constraints and require predictability. Dynamic systems are more flexible and adaptable to changing workloads and environments, but may incur higher overhead and complexity.
- Static scheduling is a technique where the task priorities and execution order are determined before the system runs, based on the task parameters and system constraints. Dynamic scheduling is a technique where the task priorities and execution order are determined at run time, based on the current state of the system and the tasks.
- Static scheduling has the advantages of being simpler, faster, and more predictable than dynamic scheduling, but it may not be able to handle unexpected events or variations in task parameters. Dynamic scheduling has the advantages of being more responsive, adaptable, and efficient than static scheduling, but it may introduce more uncertainty, overhead, and complexity.
- Static scheduling can be centralized or distributed, depending on whether the scheduling decisions are made by a single site or by multiple sites cooperatively. Dynamic scheduling can also be centralized or distributed, but it may require more communication and synchronization among the sites.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems.
- EDF assigns priorities to tasks based on their absolute deadlines. The earlier the deadline, the higher the priority.
- LST assigns priorities to tasks based on their slacks. The smaller the slack, the higher the priority. Slack is the difference between the remaining time to the deadline and the remaining execution time of the task.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints. It can achieve 100% CPU utilization.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints. It can achieve 100% CPU utilization if the tasks are independent and have equal deadlines.
- EDF and LST may not be optimal for non-preemptive scheduling, aperiodic tasks, tasks with shared resources, or tasks with different criticality levels.
- EDF and LST may have different performance in terms of response time, jitter, power consumption, and overhead. EDF tends to favor tasks with shorter deadlines, while LST tends to favor tasks with shorter execution times.



### Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- RMA is preemptive in nature, meaning that a higher priority task can interrupt a lower priority task at any time .
- RMA is optimal for periodic tasks with fixed deadlines, meaning that it can schedule any set of tasks that is schedulable by any other static-priority algorithm .
- A set of tasks is schedulable by RMA if it satisfies the following sufficient condition  :

  - The total utilization of the tasks is less than or equal to n(2^(1/n) - 1), where n is the number of tasks.

- RMA can also be applied to aperiodic and sporadic tasks, but with some limitations and modifications .
- RMA has some advantages and disadvantages compared to other scheduling algorithms:

  - Advantages:
    - Simple and easy to implement
    - Optimal for periodic tasks with fixed deadlines
    - Predictable and deterministic behavior
    - Low overhead and context switching
  - Disadvantages:
    - Not suitable for tasks with variable deadlines or execution times
    - Not optimal for aperiodic or sporadic tasks
    - May cause priority inversion or starvation of lower priority tasks
    - May waste processor time if tasks finish early or miss deadlines



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have the prior information related to the tasks and the parameters of each task are known to the scheduler only after the release of the task. Online scheduling can be either static or dynamic.
- The advantages of offline scheduling are:
  - It can guarantee the schedulability of all hard real-time tasks, as the schedule is computed in advance and verified before execution.
  - It can optimize the system performance, as the scheduler can choose the best order and allocation of tasks based on the global information.
  - It can reduce the run-time overhead, as the scheduler only needs to follow the pre-computed schedule and does not need to perform complex computations or comparisons at run-time.
- The disadvantages of offline scheduling are:
  - It requires the system to be predictable and deterministic, i.e., the tasks must have fixed and known parameters and the system must not have any uncertainties or disturbances.
  - It cannot handle dynamic changes or events, such as task arrivals, failures, or variations, as the schedule is fixed and cannot be modified at run-time.
  - It may not be feasible or practical, as the offline computation of the schedule may be too complex or time-consuming, especially for large-scale or heterogeneous systems.
- The advantages of online scheduling are:
  - It can handle dynamic changes or events, such as task arrivals, failures, or variations, as the scheduler can adapt the schedule according to the current system state and the available information.
  - It does not require the system to be predictable and deterministic, i.e., the tasks can have variable or unknown parameters and the system can have uncertainties or disturbances.
  - It can be feasible and practical, as the online computation of the schedule can be simpler or faster, especially for small-scale or homogeneous systems.
- The disadvantages of online scheduling are:
  - It may not guarantee the schedulability of all hard real-time tasks, as the scheduler may not have enough information or time to make the optimal scheduling decisions.
  - It may not optimize the system performance, as the scheduler may only choose the local optimal or suboptimal order and allocation of tasks based on the partial information.
  - It may increase the run-time overhead, as the scheduler may need to perform complex computations or comparisons at run-time.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System.

### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have random arrival times and no deadlines. Sporadic jobs are jobs that have random arrival times and hard deadlines.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, or utilization. Clock driven systems are systems that assign fixed time slots to jobs based on a predefined schedule.
- The main challenge of scheduling aperiodic and sporadic jobs in real time systems is to balance the responsiveness of aperiodic and sporadic jobs and the schedulability of periodic jobs.
- Some of the algorithms for scheduling aperiodic and sporadic jobs in priority driven systems are:
  - Background scheduling: aperiodic and sporadic jobs are executed only when there are no periodic jobs ready to run. This algorithm is simple and guarantees the schedulability of periodic jobs, but it may result in poor response times for aperiodic and sporadic jobs.
  - Polling server: a periodic task with a fixed period and execution time is created to serve aperiodic and sporadic jobs. The server has a priority assigned to it, and it can preempt periodic tasks with lower priorities. This algorithm improves the responsiveness of aperiodic and sporadic jobs, but it may introduce overhead and waste of server capacity.
  - Deferrable server: a periodic task with a fixed period and execution time is created to serve aperiodic and sporadic jobs. The server has a priority assigned to it, and it can preempt periodic tasks with lower priorities. However, the server can defer its execution until there are aperiodic or sporadic jobs ready to run. This algorithm reduces the overhead and waste of server capacity, but it may increase the response times of aperiodic and sporadic jobs.
  - Sporadic server: a periodic task with a variable period and execution time is created to serve aperiodic and sporadic jobs. The server has a priority assigned to it, and it can preempt periodic tasks with lower priorities. The server replenishes its capacity whenever it completes a job, and it adjusts its period according to the arrival time of the next job. This algorithm adapts to the dynamic arrival of aperiodic and sporadic jobs, but it may require complex analysis and implementation.
  - Slack stealing: aperiodic and sporadic jobs are executed using the available slack times of periodic and sporadic jobs. Slack time is the difference between the worst-case execution time and the actual execution time of a job. This algorithm maximizes the utilization of the system, but it may require frequent computation of slack times and coordination among tasks.
- Some of the algorithms for scheduling aperiodic and sporadic jobs in clock driven systems are:
  - Skip-over: aperiodic and sporadic jobs are executed in the time slots that are skipped by periodic jobs. This algorithm is simple and guarantees the schedulability of periodic jobs, but it may result in poor response times for aperiodic and sporadic jobs.
  - Spare capacity: aperiodic and sporadic jobs are executed in the time slots that are reserved for them in the schedule. The spare capacity can be distributed evenly or unevenly among the schedule frames. This algorithm improves the responsiveness of aperiodic and sporadic jobs, but it may reduce the utilization of the system.
  - Dynamic adjustment: aperiodic and sporadic jobs are executed in the time slots that are dynamically adjusted according to their arrival times and deadlines. The adjustment can be done by shifting, swapping, or compressing the time slots of periodic jobs. This algorithm adapts to the dynamic arrival of aperiodic and sporadic jobs, but it may require complex analysis and implementation.



## Unit 3 - Resource Sharing

- Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, and network bandwidth, available to multiple users or processes.
- Resource sharing can improve the efficiency, performance, and reliability of a computer system by reducing the duplication of resources, increasing the utilization of resources, and enabling the sharing of information and services.
- Resource sharing can also pose some challenges, such as security, privacy, compatibility, coordination, and fairness.
- Resource sharing can be classified into two types: local and distributed.
  - Local resource sharing refers to the sharing of resources within a single computer system, such as a personal computer or a server. Examples of local resource sharing are:
    - Sharing the CPU among multiple processes using scheduling algorithms.
    - Sharing the memory among multiple processes using memory management techniques.
    - Sharing the disk space among multiple files using file systems.
    - Sharing the peripheral devices, such as printers and scanners, among multiple users or processes using device drivers and spooling.
  - Distributed resource sharing refers to the sharing of resources across multiple computer systems that are connected by a network, such as the Internet. Examples of distributed resource sharing are:
    - Sharing the processing power among multiple computers using parallel computing or distributed computing techniques.
    - Sharing the storage space among multiple computers using distributed file systems or cloud storage services.
    - Sharing the network bandwidth among multiple computers using network protocols and routing algorithms.
    - Sharing the information and services among multiple computers using web servers, databases, and web services.



### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when multiple jobs compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of jobs, especially in priority-driven systems.
- Resource contention can cause undesirable effects such as:
  - Priority inversion: when a high-priority job is blocked by a low-priority job that holds a resource.
  - Timing anomalies: when a change in the execution time of a job affects the schedulability of other jobs in an unpredictable way.
  - Deadlock: when a set of jobs are waiting for each other to release resources, resulting in a circular dependency.
- Resource access control (RAC) is a set of rules that govern:
  - When and under what conditions each request for a resource is granted.
  - How jobs requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention and ensure the feasibility of the schedule.
- RAC can be classified into two categories:
  - Non-preemptive RAC: when a job that holds a resource cannot be preempted by another job until it releases the resource.
  - Preemptive RAC: when a job that holds a resource can be preempted by another job, but the resource is not released until the preempted job resumes and finishes its critical section.
- Examples of RAC protocols are:
  - Non-preemptive RAC: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), etc.
  - Preemptive RAC: Priority Inheritance Protocol (PIP), Slack Inheritance Protocol (SIP), etc.



### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access of shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that contains shared variables or resources that need to be synchronized to maintain the consistency of data .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- The advantages of NPCS are:
  - It is simple and easy to implement.
  - It prevents deadlock, since no job is ever preempted when it holds any resource.
  - It preserves the priority order of jobs, since no job can be blocked by a lower-priority job.
- The disadvantages of NPCS are:
  - It may cause priority inversion, since a higher-priority job may have to wait for a lower-priority job to finish its critical section.
  - It may cause blocking, since a job may have to wait for a resource that is held by another job.
  - It may cause resource underutilization, since a job may hold a resource longer than necessary.
  - It may cause long response times, since a job may be delayed by the critical sections of other jobs.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources  .
- PIP works by temporarily elevating the priority of a low-priority task that holds a shared resource to the highest priority of any task that is blocked by it or that may block it in the future  . This way, the low-priority task can finish using the resource and release it to the high-priority task as soon as possible  .
- PCP works by assigning a priority ceiling to each shared resource, which is the highest priority of any task that can access that resource    . A task can only access a resource if its priority is higher than the priority ceilings of all the resources currently in use    . This way, the protocol prevents deadlocks and reduces the number of context switches    .
- The main difference between PIP and PCP is that PIP is greedy while PCP is not . This means that PIP allows a task to access a resource whenever it is free, while PCP may deny a task to access a resource even if it is free, depending on the priority ceilings of the other resources in use . This can lead to different blocking times and schedulability of the tasks .
- Another difference between PIP and PCP is that PIP requires minimum support from the operating system, while PCP requires maximum support from the operating system. This means that PIP is easier to implement and more portable, while PCP is more complex and less portable.
- A third difference between PIP and PCP is that PIP cannot prevent deadlocks, while PCP can prevent deadlocks   . This means that PIP may cause a situation where two or more tasks are waiting for each other to release resources, while PCP avoids such situations by enforcing a strict order of resource access   .



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- In this protocol, each resource is assigned a priority ceiling, which is a priority equal to the highest priority of any task that may lock the resource .
- The protocol works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is updated accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered accordingly.
- The advantages of SBPCP are :
  - It prevents priority inversion and deadlock by ensuring that a task can lock a resource only if it can preempt all the tasks that may need that resource in the future.
  - It reduces the blocking time of tasks by allowing a task to lock multiple resources without being blocked by lower priority tasks that have locked some of the resources.
  - It simplifies the stack management by allowing tasks to share a common stack, which reduces the memory requirement and the context switch overhead.
- The disadvantages of SBPCP are :
  - It may cause unnecessary priority boosting of tasks that do not need to access the resources that have high priority ceilings.
  - It may increase the response time of lower priority tasks that are not involved in resource sharing by delaying their execution due to the priority boosting of higher priority tasks.
  - It requires the knowledge of the resource usage patterns and the priority assignments of all the tasks in the system, which may not be available or may change dynamically.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique that prevents priority inversion and deadlock in real-time systems that use shared resources .
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a resource needed by the high-priority task.
- Deadlock occurs when two or more tasks are waiting for each other to release a resource, resulting in a circular dependency.
- In priority-ceiling protocol, each resource is assigned a priority ceiling, which is the highest priority of any task that can access that resource .
- A task can lock a resource only if its current priority is higher than the priority ceiling of all the resources currently locked by other tasks .
- This ensures that a task cannot be blocked by a lower-priority task, and that a task cannot cause a deadlock by locking a resource that is needed by a higher-priority task .
- In dynamic priority systems, the priorities of the tasks may change over time, depending on factors such as deadlines, arrival times, or execution times.
- This means that the priority ceilings of the resources may also change over time, depending on the current priorities of the tasks that can access them.
- Therefore, in dynamic priority systems, the priority-ceiling protocol requires updating the priority ceilings of the resources and the system each time the task priorities change.
- The system priority ceiling is the highest priority ceiling of all the resources in the system .
- A task can preempt another task only if its current priority is higher than the system priority ceiling .
- This ensures that a task cannot preempt another task that is holding a resource that is needed by a higher-priority task .
- An example of a dynamic priority system is a deadline-driven system, where the priorities of the tasks are inversely proportional to their deadlines.
- In such a system, the priority of a task may increase or decrease as its deadline approaches or recedes.
- Consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3), where the first number is the period and the second number is the execution time.
- Assume that both tasks share a resource X, and that T1 has higher priority than T2 at time 0.
- The priority ceiling of X is initially 1, which is the priority of T1.
- The system priority ceiling is also 1.
- At time 0, T1 starts executing and locks X.
- At time 2, T2 arrives and preempts T1, since its priority is higher than the system priority ceiling.
- At time 4, T1's deadline is closer than T2's, so T1's priority becomes higher than T2's.
- The priority ceiling of X also becomes 2, which is the new priority of T1.
- The system priority ceiling also becomes 2.
- T1 preempts T2 and resumes execution, since its priority is higher than the system priority ceiling.
- T1 unlocks X and finishes execution at time 4.9.
- T2 resumes execution and finishes at time 5.2.
- Both tasks meet their deadlines and no priority inversion or deadlock occurs.

: Priority ceiling protocol - Wikipedia
: Priority Ceiling Protocol - GeeksforGeeks
: Use of Priority Ceiling Protocol in Dynamic Priority Systems: - Benchpartner.com



### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for others in a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that no deadlock can occur.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Dynamic preemption ceiling protocol has lower overhead and better responsiveness than static preemption ceiling protocol, but it requires more memory and synchronization primitives.
- Preemption ceiling protocol can be integrated with other scheduling schemes, such as preemption threshold scheduling (PTS), which allows a task to specify a threshold priority below which it cannot be preempted.
- Preemption threshold scheduling can improve the schedulability, reduce the context switches, and decrease the memory requirements of fixed priority systems.
- Preemption ceiling protocol can also be extended to support object-oriented real-time systems, which require synchronization considerations to maintain consistent object states.
- Preemption ceiling protocol is better than priority inheritance protocol, which allows a low-priority task to inherit the priority of a high-priority task that is blocked by it, in terms of bounded blocking time, reduced context switches, and avoidance of deadlock.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to prevent deadlock and ensure schedulability of real-time jobs.
- Deadlock occurs when a set of jobs are waiting for each other to release resources, and none of them can proceed  .
- Schedulability is the property that all jobs can meet their deadlines under a given scheduling algorithm and resource access protocol  .
- There are different resource access protocols for multiple-unit resources, such as:
  - Priority Inheritance Protocol (PIP): A job that locks a resource inherits the highest priority of all the jobs waiting for that resource, and returns to its original priority when it unlocks the resource  .
  - Priority Ceiling Protocol (PCP): A job can lock a resource only if its priority is higher than the ceiling of all the resources currently locked by other jobs, where the ceiling of a resource is the highest priority of any job that may lock that resource  .
  - Stack Resource Policy (SRP): A job can lock a resource only if its preemption level is higher than the ceiling of all the resources currently locked by other jobs, where the preemption level of a job is the highest priority of any job that may preempt it, and the ceiling of a resource is the highest preemption level of any job that may lock that resource  .
- These protocols have different properties and trade-offs, such as blocking time, response time, memory overhead, and implementation complexity  .
- The choice of a resource access protocol depends on the characteristics of the system, such as the number and type of resources, the number and priority of jobs, the length and frequency of critical sections, and the deadline and utilization of jobs  .



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real-time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are used to coordinate the accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts from occurring by locking data objects before accessing them. They require a priori knowledge of the data access patterns of the jobs and may cause blocking or priority inversion.
  - Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting some jobs. They do not require a priori knowledge of the data access patterns of the jobs and may cause wasted computation or missed deadlines.
- Some examples of pessimistic algorithms are:
  - Priority inheritance protocol (PIP): When a job is blocked by a lower-priority job that holds a lock on a data object, the lower-priority job inherits the priority of the blocked job until it releases the lock. This reduces the blocking time and preserves the priority order of the jobs.
  - Priority ceiling protocol (PCP): Each data object is assigned a priority ceiling, which is the highest priority of any job that may access it. A job can lock a data object only if its priority is higher than the current priority ceiling of the system, which is the maximum of the priority ceilings of all locked data objects. This prevents deadlock and reduces the blocking time and the number of context switches.
  - Convex ceiling protocol (CCP): Each data object is assigned a convex ceiling, which is a set of priority levels that may access it. A job can lock a data object only if its priority belongs to the convex ceiling of the data object and is higher than the current convex ceiling of the system, which is the union of the convex ceilings of all locked data objects. This allows more concurrency and flexibility than PCP and prevents deadlock and priority inversion.
- Some examples of optimistic algorithms are:
  - Wait-free algorithm: Each job accesses a private copy of the data object and updates it atomically at the end of its execution. If the update conflicts with another job's update, the job with the lower priority is aborted and restarted. This ensures that each job can complete its execution without waiting for other jobs, but may cause high abort rate and memory overhead.
  - Timestamp ordering algorithm: Each job is assigned a timestamp based on its priority and deadline. A job can access a data object only if its timestamp is smaller than the timestamp of the last job that accessed the data object. If the access is denied, the job is aborted and restarted. This ensures that the data object is always updated by the job with the smallest timestamp, but may cause high abort rate and synchronization overhead.



## Unit 4 - Real Time Communication

Real time communication is the exchange of information between two or more parties without any significant delay. It allows the parties to interact with each other in a natural and synchronous manner. Some examples of real time communication are:

- Voice calls
- Video calls
- Instant messaging
- Online gaming
- Live streaming

Real time communication has several advantages, such as:

- It enhances collaboration and productivity among teams and individuals.
- It reduces the need for travel and physical meetings, saving time and money.
- It enables social interaction and entertainment across distances and platforms.
- It supports emergency and crisis management by providing timely and accurate information.

Real time communication also has some challenges, such as:

- It requires high bandwidth and low latency networks to ensure quality and reliability.
- It poses security and privacy risks due to the potential exposure of sensitive data and identity.
- It may cause distraction and overload due to the abundance and diversity of communication channels and sources.
- It may affect interpersonal skills and social norms due to the lack of non-verbal cues and feedback.

To implement real time communication, some technologies and protocols are needed, such as:

- Real time transport protocol (RTP) - a standard for delivering audio and video over IP networks.
- Session initiation protocol (SIP) - a standard for establishing, modifying, and terminating multimedia sessions over IP networks.
- Web real time communication (WebRTC) - a set of APIs and protocols that enable browser-based real time communication without plugins or downloads.
- SignalR - a library for ASP.NET that enables real time communication between web servers and clients using web sockets or other techniques.



### Basic Concepts in Real Time Communication

Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In this context, the term real time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Streaming media and live broadcasting

Some basic concepts in real time communication are:

- Bandwidth: The amount of data that can be transmitted or received per unit of time. It is measured in bits per second (bps) or megabits per second (Mbps). Bandwidth affects the quality and speed of RTC.
- Latency: The time it takes for a signal to travel from the sender to the receiver. It is measured in milliseconds (ms) or seconds. Latency affects the responsiveness and synchronicity of RTC.
- Jitter: The variation in latency over time. It is caused by network congestion, packet loss, or routing changes. Jitter affects the smoothness and continuity of RTC.
- Packet loss: The percentage of data packets that are lost or corrupted during transmission. It is caused by network errors, interference, or congestion. Packet loss affects the reliability and clarity of RTC.
- Codec: A software or hardware device that compresses and decompresses data for transmission or storage. Codec stands for coder-decoder. Codec affects the quality and efficiency of RTC.
- Protocol: A set of rules and standards that govern how data is formatted, transmitted, and received over a network. Protocol affects the compatibility and security of RTC.
- Encryption: A process of transforming data into an unreadable form to prevent unauthorized access or modification. Encryption affects the privacy and integrity of RTC.



### Soft and Hard Real-Time Communication Systems

Real-time communication systems are systems that exchange information between two or more entities within a specified time bound. These systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT). The difference between a hard and soft real-time communication system is the consequences of incorrect operation.

- Hard Real-Time Communication Systems
  - A hard real-time communication system is a system that must meet its deadlines strictly, otherwise it may cause catastrophic failure or unacceptable loss. For example, a communication system for a nuclear power plant, a flight control system, or a pacemaker must be hard real-time, as any delay or error could result in severe damage or loss of life.
  - A hard real-time communication system is deterministic, meaning that it can guarantee the worst-case execution time and response time for any task or message. It also has high reliability and fault tolerance, as it cannot afford to fail or malfunction under any circumstances.
  - A hard real-time communication system requires a real-time operating system (RTOS) that can support preemptive scheduling, priority-based scheduling, and synchronization mechanisms. It also requires a real-time network protocol that can provide bounded delay, jitter, and packet loss. Some examples of hard real-time network protocols are Time-Triggered Protocol (TTP), Controller Area Network (CAN), and Time-Sensitive Networking (TSN).

- Soft Real-Time Communication Systems
  - A soft real-time communication system is a system that can tolerate some degree of deadline misses or errors, without causing serious harm or degradation of performance. For example, a communication system for a video conference, a multimedia streaming, or a online gaming can be soft real-time, as some delay or error may affect the quality of service, but not the functionality or safety of the system.
  - A soft real-time communication system is probabilistic, meaning that it can provide a high probability of meeting the deadlines and response times, but not a guarantee. It also has lower reliability and fault tolerance, as it can cope with some failures or malfunctions by using recovery or adaptation techniques.
  - A soft real-time communication system can use a general-purpose operating system (GPOS) that can support non-preemptive scheduling, best-effort scheduling, and resource allocation mechanisms. It can also use a non-real-time network protocol that can provide variable delay, jitter, and packet loss. Some examples of non-real-time network protocols are Transmission Control Protocol (TCP), User Datagram Protocol (UDP), and Hypertext Transfer Protocol (HTTP).



### Model of Real Time Communication

- Real time communication (RTC) is any live telecommunications method in which all users can interact in a live capacity, with negligible latency  .
- RTC can be classified into two types: real time traffic and real time control.
- Real time traffic means isochronous or synchronous traffic, consisting of a stream of messages that are generated by their sources and delivered to their respective destinations on a continuous basis.
- Real time traffic includes periodic, aperiodic and sporadic messages.
- Real time control means the coordination and synchronization of the activities of different entities involved in the communication process.
- Real time control includes flow control, error control, congestion control and quality of service (QoS) management.
- A model of real time communication consists of the following components:
  - End users: the source and destination of the messages, residing in different hosts.
  - Network interface: the hardware and software that connects the host to the network, containing input and output queues and buffers.
  - Network: the physical and logical infrastructure that provides the transmission medium and the routing mechanism for the messages.
  - Protocol: the set of rules and procedures that govern the communication process, such as format, encoding, addressing, sequencing, acknowledgement, etc.
- A model of real time communication can be characterized by the following parameters :
  - Throughput: the rate of successful message delivery over the network, measured in bits per second (bps) or packets per second (pps).
  - Delay: the time elapsed between the generation of a message by the source and its reception by the destination, measured in seconds or milliseconds.
  - Jitter: the variation in the delay of the messages, measured in seconds or milliseconds.
  - Reliability: the probability of successful message delivery over the network, measured in percentage or fraction.
  - QoS: the degree of satisfaction of the end users' requirements and expectations, measured by various metrics such as delay, jitter, reliability, bandwidth, etc.

: Model of Real Time Communication - Bench Partner
: What is Real-Time Communications (RTC)? - SearchUnifiedCommunications
: What Is Real-Time Communications? | Vonage
: What is Real-Time Communication? RTC Tools & Examples - Agora
: Real-time communications - Wikipedia



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are scheduling algorithms that assign different priorities to different packets or classes of packets in a switched network, and transmit them according to their priority levels.
- Weighted round-robin (WRR) service discipline is a special case of priority-based service discipline, where each priority queue is assigned a weight that determines the proportion of service it receives.
- The advantages of priority-based service disciplines are that they can provide different levels of quality of service (QoS) to different packets or classes of packets, such as delay, jitter, throughput, and loss.
- The disadvantages of priority-based service disciplines are that they may cause starvation of lower priority packets or classes of packets, and they may not be fair or efficient in allocating the network resources.
- Some examples of priority-based service disciplines are:
  - Strict priority (SP) service discipline, where the highest priority queue is always served first, and the lower priority queues are served only when the higher priority queues are empty.
  - Weighted fair queuing (WFQ) service discipline, where each priority queue is assigned a weight that determines the share of the network bandwidth it receives, and the packets are served in order of their virtual finish times, which are calculated based on their arrival times, lengths, and weights.
  - Weighted fair priority queuing (WFPQ) service discipline, where each priority queue is assigned a weight and a delay bound, and the packets are served in order of their virtual finish times, which are calculated based on their arrival times, lengths, weights, and delay bounds.
  - Rate-controlled frame-based weighted round-robin (RFWRR) service discipline, where each priority queue is assigned a weight and a jitter bound, and the packets are served in frames, where each frame consists of a fixed number of packets from each queue, and the frames are scheduled by a rate controller that ensures the jitter bound and the bandwidth allocation.
- In a switched network, a downstream switch can begin to transmit an earlier portion of the message as soon as it receives the portion, without waiting for the arrival of the rest of the message. This is called cut-through switching.
- The advantage of cut-through switching is that it can reduce the end-to-end delay and the buffer requirements of the switches.
- The disadvantage of cut-through switching is that it may increase the error rate and the overhead of the network, as the switches do not perform error checking or filtering on the packets.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast network.
- Broadcast networks are networks where a single transmission from one node can reach all other nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to determine which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but suffer from collisions and low efficiency.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next, such as token passing or polling. These protocols are reliable and fair, but introduce overhead and delay.
- Reservation-based protocols use a separate control channel or a dedicated time slot to reserve the access to the data channel, such as TDMA or CDMA. These protocols are efficient and scalable, but require synchronization and coordination.
- Real-time communication in broadcast networks requires MAC protocols that can provide bounded access delay, guaranteed throughput, and reliable transmission.
- Some examples of MAC protocols that support real-time communication in broadcast networks are:

  - ABROAD: An adaptive MAC protocol that incorporates a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay.
  - IEEE 802.11: A standard for wireless LANs that uses CSMA/CA with binary exponential backoff and optional request-to-send/clear-to-send (RTS/CTS) handshake to avoid collisions and hidden terminal problem. It also supports real-time traffic with enhanced distributed channel access (EDCA) and hybrid coordination function controlled channel access (HCCA) mechanisms.
  - MACAW: A MAC protocol for wireless ad hoc networks that uses RTS/CTS handshake, link-layer acknowledgments, and exponential backoff to improve the reliability and efficiency of CSMA.



### Internet and Resource Reservation Protocols

- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain different qualities of service (QoS) for their data flows     .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP is designed to support the integrated services model, which defines two classes of QoS: guaranteed service and controlled-load service .
- Guaranteed service provides a firm bound on end-to-end delay and packet loss, while controlled-load service provides a close approximation of best-effort service under unloaded conditions .
- RSVP uses soft state, which means that the reservations are periodically refreshed and automatically removed if not refreshed .
- RSVP messages are sent as IP datagrams with protocol number 46 and can be classified into two types: PATH and RESV .
- PATH messages are sent by the sender to inform the receivers and intermediate routers about the QoS requirements and the characteristics of the data flow .
- RESV messages are sent by the receivers to request a specific QoS level and to reserve resources along the path .
- RSVP also supports modification and deletion of reservations, as well as error reporting and confirmation .
- RSVP can coexist with other routing protocols, such as OSPF, RIP, or BGP, and can adapt to changes in the network topology or traffic conditions .
- RSVP can also interoperate with other resource reservation protocols, such as ST-II or ATM signaling, using protocol translation or encapsulation .
- RSVP is suitable for real-time systems that require timely and reliable delivery of data, such as videoconferencing, IP telephony, or multimedia streaming   .



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations .
- An RTOS provides features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS can be classified into two types: hard real-time and soft real-time. A hard real-time system guarantees that tasks will be completed within their deadlines, while a soft real-time system allows some tasks to miss their deadlines occasionally .
- A real-time database is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock prices, and online transactions.
- A real-time database provides features such as concurrency control, data consistency, data freshness, and data recovery.
- A real-time database can be based on SQL or NoSQL, depending on the data model and the query requirements.
- A real-time database can be distinguished from a time-series database, which is a database system that stores and analyzes data that changes over time, such as metrics, events, and logs.
- A time-series database provides features such as high ingestion rate, compression, aggregation, and visualization.
- A time-series database can also be distinguished from a real-time analytics system, which is a system that processes and analyzes data in real-time, such as streaming data, dashboards, and alerts.



### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load. An RTOS has two key features: predictability and determinism.

Some of the features and advantages of an RTOS are  :

- It occupies very less memory and consumes fewer resources than a general-purpose operating system (GPOS).
- It is small, fast, responsive, and deterministic, meaning that it will execute tasks quickly and efficiently, responding as expected every time.
- It supports multitasking and multiprogramming, allowing multiple tasks to run concurrently and share system resources.
- It uses either co-operative scheduling or pre-emptive scheduling algorithms to manage the execution of tasks. Co-operative scheduling means that a task will run until it is completed or it voluntarily yields the CPU to another task. Pre-emptive scheduling means that a task can be interrupted by a higher-priority task at any time, and resume when the higher-priority task is finished.
- It provides mechanisms for inter-task communication and synchronization, such as message queues, semaphores, mutexes, and events.
- It offers real-time services, such as timers, clocks, interrupts, and device drivers, that can handle time-critical events and operations.
- It can handle hard real-time and soft real-time requirements. Hard real-time means that a task must meet its deadline, otherwise the system will fail. Soft real-time means that a task should meet its deadline, but occasional delays are acceptable.
- It can be customized and optimized for specific applications and hardware platforms, depending on the needs and constraints of the system.



### Time Services

- Time services are the mechanisms that provide the notion of time and timing to a real-time system.
- Time services are essential for ensuring the timeliness and synchronization of real-time tasks and events.
- Time services can be classified into two categories: clock services and timer services.

#### Clock Services

- Clock services are the functions that provide the current time value to a real-time system.
- Clock services can be implemented by using hardware clocks or software clocks.
- Hardware clocks are physical devices that generate periodic signals based on a quartz crystal or an atomic oscillator.
- Software clocks are logical entities that derive the time value from the hardware clock or other sources, such as network time protocols.
- Clock services can support different time domains, such as absolute time, relative time, or logical time.
- Absolute time is the time measured from a fixed reference point, such as the Unix epoch.
- Relative time is the time measured from a variable reference point, such as the start of a task or an event.
- Logical time is the time that reflects the causal order of events in a distributed system, such as Lamport's timestamps.

#### Timer Services

- Timer services are the functions that provide the ability to schedule actions or events based on time values.
- Timer services can be implemented by using hardware timers or software timers.
- Hardware timers are physical devices that generate interrupts or signals when a predefined time interval expires.
- Software timers are logical entities that use the clock services or other mechanisms to trigger actions or events based on time values.
- Timer services can support different types of timers, such as one-shot timers, periodic timers, or deadline timers.
- One-shot timers are timers that expire only once after a specified time interval.
- Periodic timers are timers that expire repeatedly at regular time intervals.
- Deadline timers are timers that expire at a specific absolute time value.



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- A RTOS is different from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS because it does not guarantee timing requirements of the processes under its control. UNIX strives to provide good average performance, but not correct timing, which is the key feature of a RTOS.
- However, some variants of UNIX, such as Linux, have been modified to provide real-time capabilities by adding patches, modules, or extensions to the kernel .
- Some examples of real-time Linux systems are RTLinux, Xenomai, PREEMPT_RT, and RTAI.
- These systems use different approaches to achieve real-time performance, such as co-kernels, microkernels, hybrid kernels, or preemptible kernels.
- The advantages of using Linux as a RTOS are its open source nature, its wide range of supported hardware and software, its large user and developer community, and its compatibility with UNIX standards and applications .
- The challenges of using Linux as a RTOS are its complexity, its lack of certification, its variability, its dependency on external factors, and its trade-offs between performance and functionality .



### POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interact with an operating system.
- POSIX was originally designed for UNIX-like systems, but it does not cover all the features and requirements of real-time operating systems (RTOS).
- RTOS are operating systems that can guarantee timely and predictable responses to events, such as sensors, actuators, or user inputs.
- POSIX has several extensions and subsets that address some of the issues and challenges of RTOS, such as:
  - POSIX.1b: Real-time extensions, which define interfaces for timers, clocks, semaphores, message queues, shared memory, and asynchronous I/O.
  - POSIX.1c: Threads extensions, which define interfaces for creating, managing, and synchronizing multiple threads of execution within a process.
  - POSIX.4: Application programming interfaces for real-time, which define interfaces for scheduling, memory locking, priority inheritance, and sporadic servers.
- However, POSIX still has some limitations and drawbacks for RTOS, such as:
  - POSIX does not specify the scheduling policies or algorithms for real-time tasks, nor the minimum or maximum number of priority levels.
  - POSIX does not provide mechanisms for deadline or resource reservation, which are important for ensuring temporal isolation and quality of service.
  - POSIX does not support nested interrupts or interrupt handlers, which are essential for handling high-frequency or high-priority events.
  - POSIX does not define the semantics or behavior of signals in a multi-threaded environment, which can cause inconsistencies or race conditions.
  - POSIX does not address the issues of distributed or networked real-time systems, such as communication protocols, fault tolerance, or security.



### Characteristic of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, events, cycles, or sequences.
- Temporal data can be used to analyze weather patterns, traffic conditions, demographic trends, and other phenomena that change over time.
- Temporal data can be stored in the form of a tuple that contains the data value, the validity time, and the generation time.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon.
- Temporal data can be classified into different types, such as historical, current, future, or predictive.
  - Historical data is the data that was valid in the past.
  - Current data is the data that is valid at the present time.
  - Future data is the data that will be valid in the future.
  - Predictive data is the data that is estimated or projected based on historical or current data.
- Temporal data can be modeled using different approaches, such as timestamping, snapshotting, or versioning.
  - Timestamping is the approach of adding time attributes to the data to indicate its validity or transaction time.
  - Snapshotting is the approach of storing the state of the data at different points in time as separate records.
  - Versioning is the approach of maintaining the history of the data changes as a linked list of records.
- Temporal data can be queried using different operators, such as temporal selection, temporal projection, temporal join, or temporal aggregation.
  - Temporal selection is the operator of retrieving the data that satisfies a temporal condition.
  - Temporal projection is the operator of extracting the temporal attributes from the data.
  - Temporal join is the operator of combining the data from different sources based on their temporal overlap.
  - Temporal aggregation is the operator of summarizing the data over a temporal interval.
- Temporal data can be visualized using different techniques, such as timelines, charts, maps, or animations.
  - Timelines are the techniques of displaying the data as a sequence of events or intervals along a horizontal or vertical axis.
  - Charts are the techniques of displaying the data as a graphical representation of numerical values, such as bars, lines, or pies.
  - Maps are the techniques of displaying the data as a spatial representation of geographical locations, such as points, regions, or routes.
  - Animations are the techniques of displaying the data as a dynamic representation of changes over time, such as transitions, movements, or transformations.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to process data that is time-sensitive and relevant to the current situation. If the data is outdated or inaccurate, it may lead to incorrect decisions or actions that can compromise the safety or performance of the system.
- Temporal consistency can be measured by the temporal validity of the data, which is the difference between the time when the data was measured and the time when the data was read by a transaction. The temporal validity of the data should be within a predefined limit, otherwise the data is considered temporally inconsistent.
- Temporal consistency can be maintained by using various techniques, such as triggered updates, temporal caching, temporal grouping, temporal locking, and temporal broadcasting  . These techniques aim to update the data in the database as frequently as possible, or to provide the transactions with the most recent data available, or to prevent the transactions from reading or modifying the data that is temporally inconsistent.



### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency control is the process of managing the access and modification of shared data resources by multiple concurrent processes or transactions in a system.
- Concurrency control is essential for ensuring both logical and timing correctness of real-time systems (RTS), which are systems that respond to their environment within specified time constraints.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking or reserving the data resources before accessing or modifying them. Examples of pessimistic concurrency control methods are two-phase locking (2PL), timestamp ordering (TO), and priority inheritance protocol (PIP).
  - Optimistic concurrency control allows conflicts to occur and resolves them after they are detected. Examples of optimistic concurrency control methods are multiversion concurrency control (MVCC), validation-based concurrency control (VBCC), and optimistic locking.
- Concurrency control methods for RTS must consider both the data consistency and the timing constraints of the processes or transactions. Data consistency means that the shared data resources must reflect a correct and coherent state of the system. Timing constraints mean that the processes or transactions must meet their deadlines or response times.
- Concurrency control methods for RTS must also deal with the challenges of concurrency, such as deadlock, livelock, starvation, priority inversion, and blocking.
  - Deadlock occurs when two or more processes or transactions are waiting for each other to release the data resources they hold, and none of them can proceed.
  - Livelock occurs when two or more processes or transactions are constantly changing their state in response to each other, but none of them can make any progress.
  - Starvation occurs when a process or transaction is indefinitely postponed or denied access to the data resources it needs due to the interference of other processes or transactions.
  - Priority inversion occurs when a high-priority process or transaction is blocked by a low-priority process or transaction that holds a data resource it needs, and the low-priority process or transaction is preempted by a medium-priority process or transaction.
  - Blocking occurs when a process or transaction has to wait for a data resource to be released by another process or transaction before it can proceed.
- Concurrency control methods for RTS must also cope with the characteristics of real-time data, such as temporal validity, freshness, and accuracy.
  - Temporal validity means that the data has a limited time span in which it is valid and useful for the system.
  - Freshness means that the data reflects the most recent state of the system or the environment.
  - Accuracy means that the data has a certain degree of precision and reliability.
- Concurrency control methods for RTS must also balance the trade-offs between performance and complexity, such as throughput, response time, overhead, memory, and scalability.
  - Throughput means the number of processes or transactions that can be completed per unit time.
  - Response time means the time elapsed from the initiation to the completion of a process or transaction.
  - Overhead means the extra time or resources required to implement the concurrency control method.
  - Memory means the amount of storage space required to store the data or the metadata for the concurrency control method.
  - Scalability means the ability of the concurrency control method to handle increasing numbers of processes, transactions, or data resources.



### Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail or cause severe consequences.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service.
- Some of the challenges and requirements for real-time databases are:
  - Concurrency control: ensuring that concurrent transactions do not interfere with each other and maintain the consistency and integrity of the data.
  - Scheduling: deciding the order and priority of transactions to meet their deadlines and optimize the system performance.
  - Data freshness: ensuring that the data reflects the current state of the real world and is not outdated or stale.
  - Fault tolerance: ensuring that the system can recover from failures and continue to operate normally.
  - Security: ensuring that the data is protected from unauthorized access and modification.
- Some of the examples of commercial real-time databases are :
  - Dealpath: a cloud-based platform that provides data and analytics for commercial real estate transactions and investments.
  - Altus Group: a data provider that offers historical and current information on commercial real estate markets, properties, and deals.
  - CoStar: a leading provider of commercial real estate data and analytics, covering more than 5.5 million properties and 18 million tenants.
  - Google Cloud Firestore: a highly scalable, fully managed NoSQL database service that supports real-time data synchronization and offline access for web and mobile applications.

