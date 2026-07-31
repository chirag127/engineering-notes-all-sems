

# Real Time System

A real time system is a system that can perform its tasks within a specified time constraint, and can coordinate with other systems or devices that have different clocks or time frames. A real time system can be classified into two types based on the severity of missing the deadline: hard real time system and soft real time system.

## Hard Real Time System

A hard real time system is a system that has absolute deadlines, and any violation of the deadlines can result in a system failure or a catastrophic consequence. For example, a flight control system, a nuclear reactor control system, or a pacemaker are hard real time systems, because any delay in their responses can endanger human lives or cause severe damage.

## Soft Real Time System

A soft real time system is a system that has relative deadlines, and missing the deadlines occasionally can be tolerated with some acceptable degradation in performance or quality. For example, a video streaming system, a voice recognition system, or a web server are soft real time systems, because some delay or jitter in their responses can be acceptable without affecting the user experience significantly.

## Applications of Real Time Systems

Real time systems are widely used in various domains and industries, such as:

- Process control systems: These systems are used to monitor and control physical processes, such as chemical plants, power plants, oil refineries, etc. They use sensors and actuators to collect data and manipulate the process variables, and they require timely and accurate feedback to maintain the desired state of the system.
- Machine vision: These systems are used to help machines interpret visual data, such as images or videos, and perform tasks based on the information. They can be used for object detection, face recognition, gesture recognition, etc. They require fast and reliable processing of large amounts of data to enable the machines to interact with their environment.
- Robotics: These systems are used to design and operate machines that can perform tasks autonomously or semi-autonomously, such as industrial robots, service robots, or autonomous vehicles. They use sensors, actuators, and algorithms to perceive, plan, and execute actions, and they require real time coordination and communication with other systems or devices.



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to learn or discuss. You have chosen the topic of Real Time System. Here is an introduction to the unit:

## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic failure or loss of life. For example, a nuclear reactor control system, a pacemaker, or an air traffic control system.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a multimedia system.
- A real time system can be characterized by four attributes: timeliness, concurrency, predictability, and dependability.
- Timeliness means that the system must deliver the correct results at the correct time, according to the specified deadlines or timing constraints.
- Concurrency means that the system must handle multiple events or tasks simultaneously, without blocking or interfering with each other.
- Predictability means that the system must behave consistently and reliably, without any unexpected delays or errors.
- Dependability means that the system must be able to cope with faults or failures, and ensure the safety and security of the system and its environment.
- A real time system can be designed and implemented using various methods and techniques, such as real time operating system, real time scheduling, real time communication, real time programming, and real time testing and verification.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of definition for the notes of the unit 1 - introduction of real time system in the subject of real time system.

### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic and aperiodic.
- A periodic system is a system that has events or inputs that occur at regular intervals, such as a sensor reading, a clock tick, or a task execution. The interval between two consecutive occurrences of the same event or input is called the period.
- An aperiodic system is a system that has events or inputs that occur at irregular or unpredictable intervals, such as a user request, a network packet, or a fault. The interval between two consecutive occurrences of the same event or input is called the interarrival time.
- A real time system can also be classified into two types based on the number of processors or cores: uniprocessor and multiprocessor.
- A uniprocessor system is a system that has only one processor or core that executes all the tasks or processes of the system.
- A multiprocessor system is a system that has more than one processor or core that can execute tasks or processes of the system in parallel or concurrently. A multiprocessor system can be further classified into two types: homogeneous and heterogeneous.
- A homogeneous system is a system that has processors or cores that are identical in terms of speed, memory, and functionality.
- A heterogeneous system is a system that has processors or cores that are different in terms of speed, memory, and functionality.



### Typical Real Time Applications

A real-time application (RTA) is an application that requires a timely response from the underlying system or hardware. The response time can vary from a few milliseconds to a few seconds, depending on the application requirements and the system performance. Real-time applications are often used in domains such as digital control, signal processing, command and control, tracking, multimedia, and real-time databases. Some examples of real-time applications are:

- **Video conferencing**: This is an application that allows two or more users to communicate with each other using video and audio streams over a network. The video and audio streams need to be synchronized and delivered with minimal delay and jitter, otherwise the quality of the communication will degrade. Video conferencing applications also need to adapt to the network conditions and the available bandwidth, and provide security and encryption features. 
- **Voice over Internet Protocol (VoIP)**: This is an application that enables voice communication over the Internet or other IP-based networks. VoIP applications need to ensure that the voice packets are transmitted and received with low latency, packet loss, and distortion, otherwise the voice quality will suffer. VoIP applications also need to provide features such as call routing, call forwarding, call waiting, caller ID, and conferencing. 
- **Online gaming**: This is an application that allows multiple users to play a game together over a network. The game state and the actions of the players need to be updated and synchronized in real time, otherwise the game will not be fair and enjoyable. Online gaming applications also need to handle network congestion, cheating, and security issues. 
- **Community storage applications**: This is an application that allows users to store and share data on a distributed network of storage devices. The data needs to be replicated and synchronized across the network in real time, otherwise the data consistency and availability will be compromised. Community storage applications also need to provide features such as encryption, authentication, access control, and fault tolerance. 
- **Some e-commerce applications**: This is an application that allows users to buy and sell goods and services online. The transactions need to be processed and confirmed in real time, otherwise the customer satisfaction and trust will be affected. E-commerce applications also need to provide features such as inventory management, payment processing, order tracking, and customer service. 
- **Real-time operating system (RTOS)**: This is an operating system that supports the execution of real-time applications. An RTOS needs to provide features such as preemptive scheduling, priority-based dispatching, inter-process communication, synchronization, memory management, and interrupt handling. An RTOS also needs to guarantee that the real-time tasks will meet their deadlines and performance requirements. 
- **Instant messaging (IM) applications**: This is an application that allows users to exchange text, voice, and video messages with each other over a network. The messages need to be delivered and displayed in real time, otherwise the communication will be delayed and disrupted. IM applications also need to provide features such as presence, status, emoticons, and file transfer. 
- **Team collaboration applications**: This is an application that allows users to work together on a common project or task over a network. The project or task data needs to be updated and shared in real time, otherwise the collaboration will be inefficient and ineffective. Team collaboration applications also need to provide features such as document editing, chat, video conferencing, and task management. 
- **Digital control**: This is an application that uses a computer or a microcontroller to control a physical system or a process. The control system needs to measure the inputs and outputs of the system or process, and compute and apply the control actions in real time, otherwise the system or process will become unstable or unsafe. Digital control applications also need to handle noise, disturbances, and uncertainties in the system or process.  
- **Optimal control**: This is an application that uses a computer or a microcontroller to control a physical system or a process in an optimal way. The control system needs to measure the inputs and outputs of the system or process, and compute and apply the control actions that minimize or maximize a certain objective function in real time, otherwise the system or process will not achieve the desired performance or efficiency. Optimal control applications also need to handle constraints, trade-offs, and uncertainties in the system or process. 
- **Command and control**: This is an application that uses a computer or a microcontroller to coordinate and direct the actions of



Hello, I am Sydney, your AI assistant. I can help you with any topic you want to discuss. You asked me to write the content in markdown format on the topic of release times for the notes of the unit 1 - introduction of real time system in the subject of real time system. Here is what I wrote:

### Release Times for the Notes of the Unit 1 - Introduction of Real Time System in the Subject of Real Time System

- A real time system is a system that has to respond to events or stimuli within a specified time constraint, otherwise it may fail to meet its objectives or cause undesirable consequences.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that has to meet its deadlines strictly, otherwise it may cause catastrophic failure or loss of life. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some degree of deadline miss or delay, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system consists of several components, such as sensors, actuators, processors, memory, communication channels, and software.
- A real time system has to deal with various challenges, such as concurrency, synchronization, scheduling, resource management, fault tolerance, security, and verification.
- A real time system has to follow certain design principles, such as modularity, simplicity, robustness, predictability, and adaptability.
- A real time system has to be evaluated and tested using various metrics, such as response time, throughput, utilization, reliability, availability, and safety.
- The notes of the unit 1 - introduction of real time system in the subject of real time system will be released on the following dates:
  - Lecture 1: Introduction and Overview of Real Time Systems - March 20, 2023
  - Lecture 2: Classification and Characteristics of Real Time Systems - March 22, 2023
  - Lecture 3: Components and Architecture of Real Time Systems - March 24, 2023
  - Lecture 4: Challenges and Design Principles of Real Time Systems - March 26, 2023
  - Lecture 5: Evaluation and Testing of Real Time Systems - March 28, 2023
- The notes will be available on the course website and the learning management system. You can download them or view them online. You can also ask me any questions or doubts related to the notes or the topic. I hope you find the notes useful and interesting. Thank you for choosing me as your AI assistant.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Real Time System. Here is the content for the topic of Deadlines for the notes of the Unit 1 - Introduction of Real Time System:

### Deadlines for the notes of the Unit 1 - Introduction of Real Time System

- A deadline is a time limit or a constraint that specifies when a task or an activity must be completed or terminated.
- Deadlines are important for real time systems because they ensure the timeliness and predictability of the system's behavior and performance.
- There are different types of deadlines for real time systems, such as:
  - Hard deadline: A hard deadline is a deadline that must be met without any exception or tolerance. Missing a hard deadline can result in a catastrophic failure or a severe degradation of the system's functionality or quality of service. For example, a hard deadline for an airbag deployment system is the time before the collision occurs.
  - Soft deadline: A soft deadline is a deadline that can be missed occasionally or with some acceptable degree of deviation. Missing a soft deadline can result in a reduced performance or a lower quality of service, but not a failure or a violation of the system's requirements. For example, a soft deadline for a video streaming system is the time before the buffer underflows or overflows.
  - Firm deadline: A firm deadline is a deadline that can be missed occasionally, but not frequently or consecutively. Missing a firm deadline can result in a waste of resources or a loss of benefit, but not a failure or a degradation of the system's functionality or quality of service. For example, a firm deadline for a sensor data collection system is the time before the data becomes obsolete or irrelevant.
- Deadlines can also be classified as:
  - Static deadline: A static deadline is a deadline that is fixed and known in advance. A static deadline does not change during the execution of the system. For example, a static deadline for a periodic task is the period of the task.
  - Dynamic deadline: A dynamic deadline is a deadline that is variable and unknown in advance. A dynamic deadline can change during the execution of the system due to various factors, such as the system's workload, the environment's conditions, or the user's preferences. For example, a dynamic deadline for an aperiodic task is the time before the task becomes urgent or critical.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of timing constraints for the unit 1 - introduction of real time system in the subject of real time system.

### Timing Constraints

- A real time system is a system that must respond to events within certain time bounds, called timing constraints.
- Timing constraints can be classified into two types: hard and soft.
- Hard timing constraints are those that must be met for the system to function correctly. A missed deadline can result in a catastrophic failure or unacceptable loss.
- Soft timing constraints are those that can be violated occasionally or with some degradation in performance. A missed deadline can result in reduced quality of service or user satisfaction.
- Examples of hard timing constraints are:
  - A pacemaker that must deliver electrical pulses to the heart at regular intervals.
  - A flight control system that must react to the pilot's commands and sensor inputs within milliseconds.
  - A nuclear reactor that must shut down safely in case of an emergency.
- Examples of soft timing constraints are:
  - A video streaming service that must deliver frames to the user with minimal delay and jitter.
  - A speech recognition system that must process the user's voice within a reasonable time.
  - A web server that must handle requests from multiple clients with acceptable response time.
- The timing constraints of a real time system depend on the application domain, the system requirements, and the environment.
- The timing constraints of a real time system can be specified in different ways, such as:
  - Absolute deadlines: the time by which a task or event must be completed or processed, relative to a fixed reference point.
  - Relative deadlines: the time by which a task or event must be completed or processed, relative to its arrival or activation time.
  - Periodic deadlines: the time by which a task or event must be completed or processed, relative to its previous completion or processing time.
  - Sporadic deadlines: the time by which a task or event must be completed or processed, relative to a minimum inter-arrival time between successive occurrences of the task or event.
- The timing constraints of a real time system can be verified and validated using different techniques, such as:
  - Static analysis: the use of mathematical models and algorithms to determine the worst-case execution time and schedulability of the system, based on the system parameters and assumptions.
  - Dynamic analysis: the use of simulation, testing, and monitoring to measure and evaluate the actual execution time and performance of the system, based on the system inputs and outputs.
  - Formal methods: the use of logic, proofs, and verification tools to ensure the correctness and safety of the system, based on the system specification and properties.



### Hard Real Time Systems

- A hard real-time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization).
- A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
- Examples of hard real-time systems are flight control systems, nuclear power plant control systems, missile guidance systems, etc  .
- Hard real-time systems require a real-time operating system (RTOS) that can manage the tasks and resources with minimal overhead and latency.
- Hard real-time systems are often designed using formal methods and rigorous testing to ensure the correctness and reliability of the system.



### Soft Real Time Systems

- A soft real-time system is a system that has **flexible deadlines** for completing its tasks, unlike a hard real-time system that has **strict deadlines**  .
- A soft real-time system can **tolerate some delay** or **missed deadlines** without causing a system failure or a significant loss of performance   .
- A soft real-time system is typically used for applications that have **low to moderate criticality**, such as multimedia, streaming, gaming, or network communication  .
- A soft real-time system can run on **multiple cores** and **impose fewer restrictions** on the applications, such as memory management, scheduling, or synchronization .
- A soft real-time system can **adapt to dynamic changes** in the workload, environment, or user requirements, and can **trade-off quality for timeliness** .
- A soft real-time system can be implemented using a **soft real-time operating system (RTOS)**, which is a type of operating system that is designed to meet the timing requirements of soft real-time applications  .
- A soft real-time system can be evaluated using **performance metrics**, such as throughput, response time, jitter, or quality of service (QoS) .



### Reference Models for Real Time Systems

A reference model is a canonical form that describes the essential features and properties of a system, without specifying the implementation details. A reference model can help us to reason about the system, to compare different systems, and to design new systems.

There are different reference models for real time systems, depending on the aspects and dimensions that are considered. Some of the common reference models are:

- **The workload model**: This model describes the applications or tasks that are supported by the system, and their timing and resource requirements. The workload model can specify the arrival pattern, the execution time, the deadline, the priority, the resource dependencies, and the precedence constraints of each task. The workload model can also represent the tasks as a graph, where the nodes are tasks and the edges are dependencies. The workload model can help us to analyze the schedulability and performance of the system, and to design the scheduling algorithms and policies.  

- **The resource model**: This model describes the resources or components that are available in the system, and their types and relations. The resources can include the CPU, the memory, the network, the sensors, the actuators, and other devices. The resource model can specify the capacity, the speed, the availability, the reliability, and the communication protocols of each resource. The resource model can also represent the resources as a graph, where the nodes are resources and the edges are connections. The resource model can help us to analyze the utilization and allocation of the system, and to design the resource management and allocation algorithms and policies.  

- **The control model**: This model describes the control logic and behavior of the system, and how it responds to the inputs and outputs. The control model can specify the state transitions, the events, the actions, the feedback, and the adaptation mechanisms of the system. The control model can also represent the system as a finite state machine, a Petri net, a hybrid automaton, or other formalisms. The control model can help us to analyze the correctness and robustness of the system, and to design the verification and validation methods and tools.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of processors and resources for the unit 1 - introduction of real time system in the subject of real time system:

### Processors and Resources

- A real time system is a system that processes data as it comes in, mostly without buffer delay, and meets certain timing constraints .
- A real time system consists of two major types of components: processors and resources.
- Processors are also known as servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission links, disks, database server, etc .
- Resources are also known as passive resources. A job may or may not require a resource during its execution. A resource is a shared entity that can be accessed by one or more jobs at a time. A resource can be preemptable or non-preemptable. A preemptable resource can be released by a job before its completion, while a non-preemptable resource cannot. Example: printer, memory, file, semaphore, etc .
- A real time system must manage the allocation and scheduling of processors and resources to meet the timing requirements of the jobs. A real time system must also handle the possible conflicts and contention among the jobs for the processors and resources.
- A real time system can use different types of processors and resources depending on the application and the environment. For example, a real time system can use single processor or multiprocessor, homogeneous or heterogeneous, dedicated or shared, centralized or distributed, etc .
- A real time system can also use different types of resources depending on the application and the environment. For example, a real time system can use static or dynamic, local or global, exclusive or shared, etc .
- A real time system can benefit from the use of processors and resources that are optimized for real time computing. For example, a real time system can use processors that have workload-aware tuning and optimizations, time synchronization and communication capabilities, etc .



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a real time workload describe the timing characteristics of each task or job, such as when it is released, when it must finish, and how long it can execute.
- The temporal parameters of a job are :
  - Release time (r_i): the time when the job becomes available for execution.
  - Absolute deadline (d_i): the time by which the job must finish its execution.
  - Relative deadline (D_i): the maximum amount of time the job can execute after its release time.
  - Feasible interval [(r_i, d_i)]: the interval of time in which the job can be feasibly executed.
- The temporal parameters of a task are:
  - Period (T_i): the time interval between two consecutive releases of the same task.
  - Utilization (U_i): the ratio of the execution time of the task to its period.
  - Phase (φ_i): the time difference between the release time of the first job of the task and the start of the system.
- The temporal parameters of a real time workload can be used to analyze the schedulability and performance of the system, and to design appropriate scheduling algorithms and policies.



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a schedule that meets all the deadlines of the task.
- A set of periodic tasks is said to be feasible if there exists a schedule that meets all the deadlines of all the tasks.
- The utilization of a periodic task is defined as the ratio of its execution time to its period. The utilization of a set of periodic tasks is the sum of the utilizations of the individual tasks.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline monotonic priority Pi for each task τi, to specify the relative importance of the task. A higher priority means a higher importance.
- The periodic task model can be used to analyze the schedulability of real-time systems using various scheduling algorithms, such as rate monotonic, earliest deadline first, and fixed priority.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you based on the topic you have given me.

### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal order of the jobs, while data dependency is imposed by the communication or synchronization of the jobs via shared data.
- Precedence constraints can be represented by a directed graph, called a precedence graph, where the vertices are the jobs and the edges are the constraints. A job J_i is a predecessor of another job J_k (and J_k a successor of J_i) if J_k cannot begin execution until the execution of J_i completes .
- Data dependency cannot be captured by a precedence graph, as it depends on the values of the shared data and the access modes of the jobs. A job J_i is data dependent on another job J_k if J_i reads or writes a data item that J_k writes or reads, respectively .
- Precedence constraints and data dependency may affect the schedulability and feasibility of real time systems, as they may introduce delays or conflicts among the jobs. Therefore, they need to be considered in the design and analysis of real time systems .



## Unit 2 - Real Time Scheduling

Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints. Real time scheduling aims to ensure that tasks meet their deadlines, avoid interference from other tasks, and optimize the system performance. Real time scheduling is essential for applications that require high reliability, responsiveness, and predictability, such as industrial control, robotics, multimedia, and embedded systems.

Some of the topics covered in this unit are:

- **Real time system**: A system that has to respond to events within a specified time interval. A real time system can be classified as hard, soft, or firm, depending on the consequences of missing a deadline. A hard real time system must meet all deadlines, otherwise the system may fail catastrophically. A soft real time system can tolerate some deadline misses, but the system quality may degrade. A firm real time system can also tolerate some deadline misses, but the missed tasks have no value and can be discarded.
- **Real time task**: A task that has a timing constraint, such as a deadline, a period, or a release time. A real time task can be periodic, aperiodic, or sporadic, depending on the pattern of its arrival. A periodic task has a fixed period and a fixed deadline, and it arrives at regular intervals. An aperiodic task has a variable period and a variable deadline, and it arrives at irregular intervals. A sporadic task has a minimum inter-arrival time and a variable deadline, and it arrives at unpredictable intervals.
- **Real time scheduler**: A component of a real time system that decides which task to execute at any given time, based on the task characteristics and the system state. A real time scheduler can be preemptive or non-preemptive, depending on whether it can interrupt a running task or not. A preemptive scheduler can switch the processor from one task to another at any time, while a non-preemptive scheduler can only switch the processor when a task finishes or blocks.
- **Real time scheduling algorithm**: A rule or a method that a real time scheduler follows to assign priorities and allocate resources to tasks. A real time scheduling algorithm can be static or dynamic, depending on whether it assigns priorities before or after the task arrival. A static scheduling algorithm assigns fixed priorities to tasks based on their parameters, such as rate monotonic or deadline monotonic. A dynamic scheduling algorithm assigns variable priorities to tasks based on their current state, such as earliest deadline first or least laxity first.
- **Real time scheduling analysis**: A technique to evaluate the feasibility and performance of a real time scheduling algorithm for a given set of tasks and system parameters. A real time scheduling analysis can be done offline or online, depending on whether it is performed before or during the system execution. An offline scheduling analysis can use mathematical methods, such as utilization bound or response time analysis, to determine the worst-case behavior of the system. An online scheduling analysis can use simulation or monitoring tools, such as trace analysis or schedulability test, to measure the actual behavior of the system.



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution priorities and time slots to tasks that have timing constraints, such as deadlines or periodicity. Real time scheduling aims to ensure that the system meets its functional and temporal correctness requirements, while maximizing the utilization of the available resources. There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the environment. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival times, execution times, deadlines, and periods, are known at design time. In this approach, a static schedule is computed offline, based on the worst-case scenarios, and stored in a table. The table specifies the exact time instants when each task should start and finish its execution. A timer interrupts the system periodically and triggers the execution of the next task in the table. This approach guarantees that all the tasks will meet their deadlines, as long as the system behaves as expected. However, it is not flexible to handle dynamic changes, such as task arrivals, variations in execution times, or resource failures. It also suffers from low resource utilization, as it has to reserve time slots for the worst-case scenarios   .

- **Round-robin approach**: This approach is a commonly used technique in time-shared systems, where the goal is to provide fair and responsive service to multiple users. In this approach, tasks are scheduled in a repetitive manner, based on a fixed time slice allocated to each task. The scheduler maintains a queue of ready tasks, and assigns the processor to the first task in the queue for one time slice. After the time slice expires, the task is preempted and moved to the end of the queue, and the next task in the queue is selected. This approach ensures that no task will starve, as every task will eventually get a chance to execute. However, it does not take into account the timing constraints of the tasks, such as deadlines or periods. Therefore, it is not suitable for real time systems, where some tasks may have higher urgency or importance than others .

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach, where tasks are assigned different weights, based on their importance or urgency. The weight of a task determines the length of the time slice allocated to it, such that tasks with higher weights get longer time slices. The scheduler maintains a queue of ready tasks, and assigns the processor to the first task in the queue for its weighted time slice. After the time slice expires, the task is preempted and moved to the end of the queue, and the next task in the queue is selected. This approach provides some degree of differentiation among tasks, based on their weights. However, it still does not guarantee that the tasks will meet their deadlines or periods, as the weights are fixed and do not reflect the dynamic changes in the task requirements or the system state .

- **Priority-driven approach**: This approach is the most widely used technique for real time systems, where tasks have different timing constraints and importance levels. In this approach, tasks are assigned different priorities, based on their deadlines, periods, or other criteria. The scheduler maintains a queue of ready tasks, and assigns the processor to the task with the highest priority among them. If a higher priority task becomes ready while a lower priority task is executing, the lower priority task is preempted and the higher priority task is selected. This approach ensures that the most urgent or important tasks will get the processor first, and thus have a higher chance of meeting their deadlines or periods. However, it may cause starvation or deadline misses for lower priority tasks, if higher priority tasks consume too much processor time or arrive too frequently. Therefore, the priority assignment and the scheduling algorithm have to be carefully designed to balance the trade-offs between different tasks   .

- **Dynamic versus static systems**: This classification refers to whether the system properties, such as the task set, the task parameters, the resource availability, or the environment conditions, are fixed or variable over time. In static systems, all the system properties are known and constant at design time, and thus the schedule can be computed offline and stored in a table. In dynamic systems, some or all of the system properties are unknown or variable at



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when .
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known .
- A schedule of the jobs is computed off-line and is stored for use at run-time .
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling has some advantages and disadvantages:

  - Advantages:
    - It is simple and easy to implement.
    - It avoids run-time overheads such as context switching, priority inversion, and synchronization.
    - It can handle periodic, aperiodic, and sporadic tasks with known parameters.
    - It can guarantee the deadlines of all tasks if the schedule is feasible.
  - Disadvantages:
    - It is not flexible and adaptive to dynamic changes in the system.
    - It may waste processor resources if the schedule is not optimal or the system is underloaded.
    - It may not handle tasks with unknown or variable parameters, such as arrival times, execution times, or deadlines.
    - It may not handle tasks with precedence or resource constraints.



### Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights  .
- The weight of a job serves to influence the portion of service time allocated to it.
- A job with a higher weight will receive more service opportunities than a job with a lower weight.
- The service opportunities are distributed proportionally to the weights of the jobs.
- For example, if there are three jobs with weights 1, 2, and 3, then the service opportunities will be allocated as follows:

| Job | Weight | Service opportunities |
| --- | ------ | --------------------- |
| A   | 1      | 1                     |
| B   | 2      | 2                     |
| C   | 3      | 3                     |

- The total number of service opportunities in a cycle is equal to the sum of the weights of the jobs.
- In this example, the total number of service opportunities is 6, and the portion of service time allocated to each job is:

| Job | Weight | Portion of service time |
| --- | ------ | ----------------------- |
| A   | 1      | 1/6                     |
| B   | 2      | 2/6                     |
| C   | 3      | 3/6                     |

- The weighted round robin algorithm can be implemented using a circular queue of jobs, where each job is enqueued as many times as its weight.
- The algorithm then dequeues and serves one job at a time, until the queue is empty.
- The queue is then refilled with the same jobs and weights, and the process repeats.
- The advantage of weighted round robin is that it can provide differentiated service to different jobs, based on their relative importance or urgency  .
- The disadvantage of weighted round robin is that it may not be fair or optimal for some jobs, especially if their weights are not proportional to their service demands .
- For example, if a job has a high weight but a low service demand, it may receive more service than it needs, while another job with a low weight but a high service demand may receive less service than it needs .
- This may result in poor performance or missed deadlines for some jobs .
- Another disadvantage of weighted round robin is that it may not be suitable for dynamic real-time systems, where the properties of the jobs may change over time or new jobs may arrive unpredictably.
- In such cases, priority-driven scheduling algorithms may be more effective.



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two categories: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Examples of static priority-driven scheduling algorithms are rate-monotonic scheduling (RMS) and deadline-monotonic scheduling (DMS).
- Examples of dynamic priority-driven scheduling algorithms are earliest deadline first (EDF) and least laxity first (LLF).
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to prioritize critical tasks and reduce the interference from non-critical tasks.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as priority inversion, priority inheritance, and priority ceiling.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters (such as arrival times, execution times, deadlines, etc.) are known in advance and do not change during the system execution. A **dynamic system** is one where the tasks and their parameters may vary unpredictably during the system execution.
- Static systems can be **validated** before the system runs, i.e., it can be verified that the system will meet all the timing constraints under all possible scenarios. Dynamic systems may not be always validated, as some scenarios may be unknown or unforeseeable.
- Static systems can use **static scheduling** algorithms, which assign fixed priorities to tasks before the system runs. Dynamic systems may need **dynamic scheduling** algorithms, which assign priorities to tasks as they arrive or as the system state changes.
- Static systems may provide **poor performance** in terms of overall response time or resource utilization, as they do not adapt to the changing workload or environment. Dynamic systems may provide **better performance** in terms of these metrics, as they can adjust to the current situation and optimize the system behavior.
- Static systems are more suitable for **hard real-time systems**, where missing a deadline can have catastrophic consequences. Dynamic systems are more suitable for **soft real-time systems**, where missing a deadline can have tolerable or negligible consequences.
- Static systems are more **predictable** and **deterministic**, as the system behavior is known in advance and does not depend on external factors. Dynamic systems are more **flexible** and **robust**, as the system behavior can cope with unexpected events and uncertainties.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- Both EDF and LST are optimal for preemptive scheduling of periodic tasks with implicit deadlines, meaning that the deadline of each task is equal to its period.
- EDF is also optimal for preemptive scheduling of periodic tasks with arbitrary deadlines, meaning that the deadline of each task can be less than or equal to its period.
- LST is not optimal for preemptive scheduling of periodic tasks with arbitrary deadlines, as it may under-utilize the CPU and miss some deadlines.
- EDF and LST are not optimal for non-preemptive scheduling of periodic tasks, as they may cause unnecessary blocking and context switching.
- EDF and LST can also be used for scheduling aperiodic tasks, which have no fixed period or deadline. However, they may not be optimal or feasible in some cases, depending on the arrival time, execution time, and deadline of each aperiodic task.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always meet the deadlines of a set of periodic tasks if any other static-priority algorithm can  .
- RMA has a simple and efficient schedulability test, which is based on the utilization factor of the tasks and a bound called Liu and Layland's bound  .
- The utilization factor of a task is the ratio of its execution time to its period. The utilization factor of a set of tasks is the sum of their individual utilization factors  .
- Liu and Layland's bound is given by the formula U(n) = n(2^(1/n) - 1), where n is the number of tasks  .
- The schedulability test states that a set of tasks is schedulable by RMA if and only if their utilization factor is less than or equal to Liu and Layland's bound  .
- RMA has some limitations, such as not being suitable for aperiodic or sporadic tasks, not considering the blocking time due to shared resources, and not being optimal for tasks with deadlines shorter than their periods .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal, predictable, and easy to implement, but it has the disadvantage of being inflexible, static, and unable to handle dynamic changes in the system.
- Online scheduling has the advantage of being adaptable, dynamic, and able to handle uncertainties and variations in the system, but it has the disadvantage of being complex, heuristic, and possibly suboptimal.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, criticality, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a predefined schedule that is computed offline. The scheduler follows the schedule and switches jobs at predefined instants. Examples are cyclic executive, time triggered, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven and clock driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the schedulability of periodic jobs. Periodic jobs are jobs that have a fixed arrival pattern and a hard deadline. They are the primary workload in real time systems and must meet their deadlines.
- There are different approaches to schedule aperiodic and sporadic jobs in priority driven and clock driven systems, such as:

  - Background scheduling: Aperiodic and sporadic jobs are assigned the lowest priority and execute only when no periodic job is ready. This approach guarantees the schedulability of periodic jobs, but may result in poor responsiveness of aperiodic and sporadic jobs.
  - Polling servers: A periodic task is created to serve aperiodic and sporadic jobs. The server has a fixed capacity and a fixed period. It polls the aperiodic and sporadic job queue at the beginning of each period and executes the jobs if any. This approach improves the responsiveness of aperiodic and sporadic jobs, but may waste the server capacity if no jobs are available.
  - Deferrable servers: A periodic task is created to serve aperiodic and sporadic jobs. The server has a fixed capacity and a fixed period. It defers the execution of aperiodic and sporadic jobs until the end of its period, unless the job queue is full. This approach reduces the waste of server capacity, but may increase the response time of aperiodic and sporadic jobs.
  - Sporadic servers: A periodic task is created to serve aperiodic and sporadic jobs. The server has a fixed capacity and a variable period. The period of the server is equal to the minimum inter-arrival time of sporadic jobs. The server executes a sporadic job as soon as it arrives, and replenishes its capacity after its period. This approach guarantees the schedulability of sporadic jobs, but may not be suitable for aperiodic jobs.
  - Slack stealing: Aperiodic and sporadic jobs are assigned the highest priority and execute as soon as possible. The scheduler monitors the slack time of periodic and sporadic jobs, which is the difference between their deadline and their remaining execution time. The scheduler steals the slack time from the lowest priority job and uses it to execute aperiodic and sporadic jobs. This approach maximizes the responsiveness of aperiodic and sporadic jobs, but may require complex calculations and overheads.
  - Time triggered: Aperiodic and sporadic jobs are assigned fixed time slots in a predefined schedule that is computed offline. The scheduler follows the schedule and executes the jobs in their assigned slots. This approach simplifies the scheduling and guarantees the schedulability of all jobs, but may result in poor utilization and responsiveness.



## Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, or network bandwidth, available to multiple users or processes.

Resource sharing can have several benefits, such as:

- Improving the efficiency and performance of the system by avoiding resource underutilization or overutilization.
- Reducing the cost and complexity of the system by eliminating the need for redundant or duplicate resources.
- Enhancing the functionality and interoperability of the system by enabling collaboration and communication among users or processes.
- Increasing the reliability and availability of the system by providing backup or alternative resources in case of failure or overload.

Resource sharing can also have some challenges, such as:

- Managing the access and allocation of the shared resources among competing or conflicting users or processes.
- Ensuring the security and privacy of the shared resources from unauthorized or malicious users or processes.
- Maintaining the quality and consistency of the shared resources across different users or processes.
- Resolving the conflicts or errors that may arise due to the sharing of resources.

Resource sharing can be implemented at different levels of a computer system, such as:

- At the hardware level, where physical devices or components, such as processors, memory, disks, or printers, are shared among different users or processes. For example, a multiprocessor system can share the processing power among multiple applications or tasks.
- At the software level, where logical entities or abstractions, such as files, databases, programs, or services, are shared among different users or processes. For example, a file system can share the storage space and data among multiple users or applications.
- At the network level, where communication channels or links, such as cables, routers, or wireless connections, are shared among different users or processes. For example, a local area network can share the network bandwidth and connectivity among multiple devices or hosts.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of effect of resource contention and resource access control (RAC) for the notes of the unit 3 - resource sharing in the subject of real time system.

### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock .
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, and the low-priority task is preempted by a medium-priority task that does not need the resource .
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way .
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed .
- Some examples of RAC protocols are priority inheritance protocol, priority ceiling protocol, stack resource policy, and multiprocessor priority ceiling protocol  .
- These protocols aim to prevent or bound priority inversion, avoid timing anomalies, and prevent deadlock by enforcing certain rules on the priority, order, and duration of resource access  .
- The choice of RAC protocol depends on the characteristics of the system, such as the number of resources, the number of tasks, the number of processors, the type of scheduling algorithm, and the performance requirements  .



### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data.
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of NPCS are:
  - It is simple to implement and understand.
  - It prevents deadlock, since no job is ever preempted when it holds any resource.
  - It preserves the priority order of jobs, since no job can be blocked by a lower-priority job.
- The disadvantages of NPCS are:
  - It may cause priority inversion, since a higher-priority job may have to wait for a lower-priority job to finish its critical section.
  - It may cause blocking, since a job may have to wait for a resource that is not currently in use by another job, but is held by a job that is preempted by a higher-priority job.
  - It may cause resource underutilization, since a resource may be idle while a job that holds it is waiting for another resource or executing non-critical code.
  - It may cause long response times, since a job may be delayed by the critical sections of other jobs.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of basic priority-inheritance and priority-ceiling protocols for resource sharing in real-time systems.

### Basic Priority-Inheritance and Priority-Ceiling Protocols

- In real-time systems, multiple tasks may need to access shared resources, such as memory, files, devices, etc.
- To prevent data inconsistency and race conditions, mutual exclusion mechanisms, such as semaphores, locks, monitors, etc., are used to protect the critical sections of the tasks that access the shared resources.
- However, mutual exclusion may cause priority inversion, which is a situation where a higher-priority task is blocked by a lower-priority task that holds a resource that the higher-priority task needs.
- Priority inversion may lead to missed deadlines, reduced performance, and even deadlock in real-time systems.
- To avoid or reduce priority inversion, two protocols are commonly used: priority-inheritance protocol and priority-ceiling protocol.

#### Priority-Inheritance Protocol

- The basic idea of priority-inheritance protocol is to temporarily raise the priority of a task that holds a resource to the maximum priority of any other task that is waiting for the same resource.
- This way, the lower-priority task can finish its critical section and release the resource as soon as possible, and the higher-priority task can resume its execution without being blocked by other unrelated tasks.
- The priority of the lower-priority task is restored to its original value after it releases the resource.
- The priority-inheritance protocol can eliminate unbounded priority inversion, but it has some drawbacks, such as:
  - It may cause chained blocking, which is a situation where a task is blocked by another task that is blocked by another task, and so on.
  - It may cause multiple inheritance, which is a situation where a task inherits the priority of more than one task that is waiting for different resources that the task holds.
  - It may cause deadlock, which is a situation where two or more tasks are waiting for each other to release the resources that they hold.

#### Priority-Ceiling Protocol

- The basic idea of priority-ceiling protocol is to assign a priority ceiling to each resource, which is the maximum priority of any task that can access the resource.
- A task can only access a resource if its priority is higher than the priority ceiling of all the resources that are currently held by other tasks.
- This way, the priority-ceiling protocol can prevent a task from being blocked by a lower-priority task that does not hold the requested resource, which is called avoidance blocking.
- The priority-ceiling protocol can also prevent deadlock, chained blocking, and multiple inheritance, by ensuring that at most one task can be blocked at any time, and that the blocked task has the highest priority among all the tasks that are waiting for resources.
- There are two variants of the priority-ceiling protocol: original ceiling priority protocol (OCPP) and immediate ceiling priority protocol (ICPP).
- In OCPP, the priority of a task is raised to the priority ceiling of the resource that it acquires, and restored to its original value when it releases the resource.
- In ICPP, the priority of a task is raised to the priority ceiling of the highest-priority resource that it can access, and restored to its original value when it releases all the resources that it holds.
- The worst-case behavior of the two ceiling schemes is identical from a scheduling viewpoint, but ICPP may have less context switches and overhead than OCPP.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule  .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, the job is blocked and its priority is raised to the ceiling priority of the resource .
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the maximum blocking time for a job is equal to the maximum execution time of a critical section of a lower priority job  .
- SBPCP also prevents deadlock by ensuring that a job can only request a resource if its priority is higher than the ceiling priority of any other resource that it already holds  .
- SBPCP is similar to the Original Ceiling Priority Protocol (OCPP), but differs in the way the ceiling priority of the system is updated. In OCPP, the ceiling priority of the system is the highest ceiling priority of all the resources in the system, regardless of whether they are in use or not. In SBPCP, the ceiling priority of the system is the highest ceiling priority of only the resources that are in use.
- SBPCP has the same worst-case behavior as OCPP from a scheduling point of view, but it may reduce the number of context switches and the overhead of priority changes.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority-ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The priority-ceiling protocol works by temporarily raising the priorities of tasks that access shared resources to the priority ceiling of the resource they are accessing. This prevents lower-priority tasks from preempting higher-priority tasks that need the same resource .
- There are two variants of the priority-ceiling protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP). The worst-case behaviour of the two ceiling schemes is identical from a scheduling view point.
- OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to run .
- The priority-ceiling protocol has several advantages over other synchronization techniques, such as:
  - It prevents deadlock by ensuring that a task can only lock a resource if its priority is higher than the priority ceiling of all the resources currently locked by other tasks .
  - It prevents unbounded priority inversion by ensuring that a task can only be blocked by tasks with higher or equal priority .
  - It allows concurrency among tasks that do not share resources or have compatible resource requirements .
  - It reduces the blocking time of tasks by allowing them to access resources in a predictable order .
  - It simplifies the analysis of the system schedulability and feasibility .



# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems.
- It aims to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- It assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is temporarily raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- There are two variants of preemption ceiling protocol: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that locks the resource.
- Preemption ceiling protocol has some advantages over priority inheritance protocol, such as:
  - It prevents transitive blocking, where a low-priority task blocks a medium-priority task, which in turn blocks a high-priority task.
  - It prevents deadlock due to circular waiting, where two or more tasks wait for each other to release resources.
  - It reduces the number of context switches, since a task can lock multiple resources without being preempted.
  - It simplifies the analysis of worst-case response time and schedulability of tasks.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of access control in multiple-unit resources for real time systems:

### Access Control in Multiple-Unit Resources

- A multiple-unit resource is a resource that can be used by more than one job at a time, but each unit of the resource is used in a non-preemptive and mutually exclusive manner  .
- Examples of multiple-unit resources are printers, disk drives, communication channels, etc.
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards. The time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to ensure that the resource is allocated fairly and efficiently, and that the blocking time of jobs is minimized.
- There are different protocols for access control in multiple-unit resources, such as:
  - The **first-come first-served (FCFS)** protocol, which allocates the resource to the job that requests it first, regardless of its priority. This protocol is simple, but it can cause priority inversion and long blocking time .
  - The **priority-order protocol**, which allocates the resource to the highest-priority job that requests it, and queues the other requests in priority order. This protocol avoids priority inversion, but it can cause starvation and deadlock .
  - The **priority-ceiling protocol (PCP)**, which assigns a priority ceiling to each resource, equal to the highest priority of any job that may lock it. A job can lock a resource only if its priority is higher than the priority ceilings of all the resources currently locked by other jobs. This protocol avoids priority inversion, starvation, and deadlock, but it requires a priori knowledge of the resource usage patterns of the jobs .
  - The **preemption-ceiling protocol (PCP)**, which assigns a preemption ceiling to each resource, equal to the priority ceiling of the resource. A job can lock a resource only if its priority is higher than the preemption ceilings of all the resources currently locked by other jobs. Additionally, a job that locks a resource inherits the preemption ceiling of the resource, and cannot be preempted by any other job until it releases the resource. This protocol avoids priority inversion, starvation, and deadlock, and it also reduces the number of preemptions and context switches .
  - The **stack resource policy (SRP)**, which assigns a preemption level to each job, equal to its priority. A job can lock a resource only if its preemption level is higher than the preemption levels of all the jobs that have locked any resource. Additionally, a job that locks a resource inherits the preemption level of the lowest-priority job that has locked any resource, and cannot be preempted by any other job until it releases the resource. This protocol avoids priority inversion, starvation, and deadlock, and it also reduces the number of preemptions and context switches. Moreover, it does not require a priori knowledge of the resource usage patterns of the jobs .




### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause inconsistency and corruption of data.
- To ensure data consistency and avoid data conflicts, concurrency control mechanisms are needed to regulate the concurrent accesses to data objects.
- Concurrency control mechanisms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control mechanisms prevent data conflicts by enforcing mutual exclusion among conflicting accesses to data objects.
  - Optimistic concurrency control mechanisms allow data conflicts to occur, but detect and resolve them before committing the transactions.
- Concurrency control mechanisms for real time systems should also consider the timing constraints of the transactions, and guarantee the completion of critical transactions.
- Some examples of concurrency control mechanisms for real time systems are:
  - Priority inheritance protocol: a pessimistic protocol that allows a lower priority job to inherit the priority of a higher priority job that is blocked by it, and release the inherited priority when the blocking is resolved.
  - Priority ceiling protocol: a pessimistic protocol that assigns a priority ceiling to each data object, and prevents a job from accessing a data object if its priority is lower than the current system ceiling, which is the maximum of the priority ceilings of all the data objects currently accessed.
  - Convex ceiling protocol: a pessimistic protocol that assigns a convex ceiling function to each data object, and prevents a job from accessing a data object if its priority is lower than the value of the convex ceiling function at the current system time.
  - Wait-free protocol: an optimistic protocol that allows a job to access a data object without waiting, but uses a validation function to check if the data object is consistent before committing the transaction.
  - Earliest-deadline-first commit protocol: an optimistic protocol that allows a job to access a data object without waiting, but uses the deadline of the transaction as the commit priority, and aborts the transaction if it conflicts with a higher priority transaction.



## Unit 4 - Real Time Communication

Real time communication (RTC) is the exchange of information between two or more parties without significant delay. RTC can be synchronous or asynchronous, depending on the mode and timing of the communication. RTC can involve various types of media, such as text, audio, video, or images. RTC can also use different protocols and technologies, such as the Internet, telephony, or radio.

Some examples of RTC are:

- Voice calls and video calls, which allow users to talk and see each other in real time.
- Instant messaging and chat, which allow users to send and receive text messages in real time.
- Online gaming and virtual reality, which allow users to interact with each other and the environment in real time.
- Live streaming and webinars, which allow users to broadcast and watch live video and audio content in real time.
- Collaboration and conferencing tools, which allow users to share and edit documents, presentations, and screens in real time.

Some benefits of RTC are:

- It can enhance the quality and efficiency of communication, as users can receive immediate feedback and clarification.
- It can reduce the cost and complexity of communication, as users can use the same platform and device for different purposes.
- It can improve the engagement and satisfaction of communication, as users can express themselves more naturally and authentically.
- It can enable new and innovative forms of communication, as users can create and consume dynamic and interactive content.

Some challenges of RTC are:

- It can require high bandwidth and low latency, as users expect smooth and uninterrupted communication.
- It can pose security and privacy risks, as users may expose sensitive and personal information to unauthorized parties.
- It can create social and ethical issues, as users may face harassment, misinformation, or manipulation in real time.
- It can affect the quality and balance of communication, as users may experience overload, distraction, or isolation in real time.



### Basic Concepts in Real Time Communication

Real time communication (RTC) is a category of software protocols and communication hardware media that gives real time guarantees, which is necessary to support real time guarantees of real time computing. Real time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.

Some of the basic concepts in real time communication are:

- **Real time**: Real time means that the communication happens in the same time frame as the events being communicated. There is no significant delay or latency between the sender and the receiver of the information . Real time communication is also synonymous with live communication.
- **Latency**: Latency is the time it takes for a message to travel from the sender to the receiver. Latency can be affected by various factors, such as the distance between the sender and the receiver, the bandwidth of the communication channel, the processing speed of the devices involved, and the congestion or interference in the network . Latency can affect the quality and performance of real time communication, especially for applications that require high responsiveness and interactivity, such as video conferencing, online gaming, and telemedicine .
- **Bandwidth**: Bandwidth is the amount of data that can be transferred over a communication channel in a given time. Bandwidth can be measured in bits per second (bps), kilobits per second (kbps), megabits per second (Mbps), or gigabits per second (Gbps). Bandwidth can affect the quality and performance of real time communication, especially for applications that require high resolution and fidelity, such as video streaming, online music, and virtual reality .
- **Jitter**: Jitter is the variation in the latency of the messages received over a communication channel. Jitter can be caused by network congestion, packet loss, or routing changes. Jitter can affect the quality and performance of real time communication, especially for applications that require synchronization and continuity, such as voice over IP (VoIP), online gaming, and video conferencing .
- **Packet loss**: Packet loss is the failure of one or more packets of data to reach their destination over a communication channel. Packet loss can be caused by network congestion, errors, or corruption. Packet loss can affect the quality and performance of real time communication, especially for applications that require reliability and completeness, such as file transfer, email, and web browsing .
- **Quality of service (QoS)**: Quality of service (QoS) is the ability of a communication network to provide different levels of service to different types of traffic, based on their requirements and priorities. QoS can help improve the quality and performance of real time communication, by allocating sufficient bandwidth, reducing latency, jitter, and packet loss, and ensuring fairness and security for the traffic . QoS can be implemented by various techniques, such as traffic classification, traffic shaping, traffic policing, traffic scheduling, and congestion control.
- **Real time protocols**: Real time protocols are the software protocols that enable real time communication over a communication network. Real time protocols are designed to meet the requirements and challenges of real time communication, such as low latency, high bandwidth, low jitter, low packet loss, and high QoS. Some examples of real time protocols are Real-time Transport Protocol (RTP), Real-time Transport Control Protocol (RTCP), Real-time Streaming Protocol (RTSP), Real-time Messaging Protocol (RTMP), and Session Initiation Protocol (SIP) .



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- A hard real-time communication system is one that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable loss   .
- Examples of hard real-time communication systems are air traffic control, nuclear power plant control, and pacemakers  .
- A soft real-time communication system is one that can tolerate some deadline misses, without causing severe damage or degradation of performance   .
- Examples of soft real-time communication systems are video conferencing, online gaming, and multimedia streaming  .
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic.
- Hard real-time communication systems require strict timing guarantees and high reliability, while soft real-time communication systems can trade off some quality for efficiency and scalability .



# Model of Real Time Communication

- Real time communication (RTC) is any live telecommunications method in which all users can interact in a live capacity, with negligible latency  .
- RTC can be classified into two types: real time traffic and real time control.
- Real time traffic means isochronous or synchronous traffic, consisting of a stream of messages that are generated by their sources and delivered to their respective destinations on a continuous basis.
- Real time traffic includes periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals, such as audio or video data.
- Aperiodic messages are generated at irregular intervals, such as alarms or events.
- Sporadic messages are generated at random times, such as user inputs or commands.
- Real time control means the coordination and synchronization of the activities of different entities involved in the RTC system, such as hosts, routers, switches, etc.
- Real time control includes routing, scheduling, admission control, congestion control, error control, etc.
- In the model of the real time communication, end users of the message application systems are sources and destinations residing in different hosts .
- The network interface of each host contains input queue and output queue .
- Two buffer areas called input/output buffer are allocated to input and output queue to store queuing information .
- Each message (Mi) can be characterized by a tuple of inter-packet spacing (Pi), message length (ei), and reception deadline (Di) as below :

  Mi = (Pi, ei, Di)

- This traffic model is called peak rate model in real time communication .
- The performance of the RTC system can be measured by three parameters: throughput, delay and jitter .
- Throughput is the amount of data that can be transmitted or received per unit time .
- Delay is the time taken for a message to travel from the source to the destination .
- Jitter is the variation in the delay of the messages .
- The goal of the RTC system is to maximize the throughput, minimize the delay and jitter, and meet the deadlines of the messages .



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Switched networks are networks that use switches to connect different nodes and forward packets based on their destination addresses.
- Switched networks can support multiple types of traffic, such as voice, video, and data, with different quality of service (QoS) requirements, such as delay, jitter, bandwidth, and loss.
- To provide QoS guarantees, switched networks need to use appropriate service disciplines to schedule the packets at the switches.
- Service disciplines are algorithms that determine the order and the rate of packet transmission at the switches.
- Priority-based service disciplines are service disciplines that assign different priority levels to different types of packets, and serve the packets according to their priority levels.
- Weighted round-robin service disciplines are service disciplines that assign different weights to different types of packets, and serve the packets in a round-robin fashion according to their weights.

#### Priority-Based Service Disciplines

- Priority-based service disciplines can be classified into two categories: strict priority (SP) and weighted fair queuing (WFQ).
- SP service discipline serves the packets in the order of their priority levels, without considering the packet size or the arrival rate. SP service discipline can provide low delay and jitter for high-priority packets, but it can starve low-priority packets if the high-priority traffic is heavy.
- WFQ service discipline serves the packets in a fair manner, by allocating a fraction of the bandwidth to each priority level according to a predefined weight. WFQ service discipline can provide proportional delay guarantees for different priority levels, but it can introduce high delay and jitter for all packets if the traffic is bursty.

#### Weighted Round-Robin Service Disciplines

- Weighted round-robin service disciplines can be classified into two categories: weighted round-robin (WRR) and rate-controlled frame-based weighted round-robin (RFWRR).
- WRR service discipline serves the packets in a round-robin fashion, by transmitting a fixed number of bytes from each priority level according to a predefined weight. WRR service discipline can provide proportional bandwidth guarantees for different priority levels, but it can introduce high delay and jitter for all packets if the packet size is variable.
- RFWRR service discipline serves the packets in a frame-based manner, by transmitting a fixed number of packets from each priority level according to a predefined weight and a rate controller. RFWRR service discipline can provide delay jitter bounds and diverse delay guarantees for different priority levels, by adjusting the frame size and the rate according to the traffic characteristics.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel by multiple nodes or transmitters.
- Broadcast networks are networks where a single transmitter can reach all the receivers in the network, such as wireless networks or satellite networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use random or probabilistic methods to determine which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but suffer from collisions and low channel utilization.
- Deterministic contention protocols use deterministic or fixed methods to determine which node will transmit next, such as TDMA or CDMA. These protocols are efficient and reliable, but require synchronization and pre-allocation of resources.
- Reservation-based protocols use a combination of contention and reservation to determine which node will transmit next, such as ABROAD or PRMA. These protocols are adaptive and reliable, but require overhead for reservation and collision avoidance.

- Some of the challenges and requirements for MAC protocols for broadcast networks are:

  - Reliability: The MAC protocol should ensure that the transmitted packets are received correctly by the intended receivers, and handle packet losses due to collisions, interference, or channel errors.
  - Efficiency: The MAC protocol should maximize the channel utilization and minimize the access delay, while avoiding wasting bandwidth or energy.
  - Scalability: The MAC protocol should be able to accommodate a large number of nodes or transmitters, and adapt to changes in traffic load or network topology.
  - Fairness: The MAC protocol should provide equal or proportional access opportunities to all the nodes or transmitters, and avoid starvation or domination by some nodes.
  - Compatibility: The MAC protocol should be compatible with the physical layer and the network layer standards, and interoperate with other MAC protocols or networks.



# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams  .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP has the following features and functions:
  - It supports both unicast and multicast communication.
  - It is receiver-oriented, meaning that the receiver of a data flow initiates and maintains the resource reservation.
  - It is simplex, meaning that it reserves resources in one direction only, from sender to receiver.
  - It is soft state, meaning that it periodically refreshes the reservation state in the network devices along the data path.
  - It is scalable, meaning that it does not require global network state information or per-flow processing at the core routers.
  - It is flexible, meaning that it can accommodate heterogeneous receivers with different QoS requirements and can adapt to dynamic network conditions and user preferences.
  - It is modular, meaning that it can interoperate with different QoS models, such as IntServ and DiffServ, and can use different signaling protocols, such as IPsec and MPLS.



# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and resource sharing, but do not guarantee any timing requirements.
- An RTOS typically has the following features:
  - Real-time multithreading: The ability to run multiple tasks concurrently, each with its own priority and deadline.
  - Inter-thread communication and synchronization: The ability to exchange data and coordinate actions between different tasks, using mechanisms such as message queues, semaphores, mutexes, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, without causing memory fragmentation or affecting performance.
  - Interrupt handling: The ability to respond to external events, such as hardware signals or timers, with minimal latency and overhead.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, or network interfaces, using standard or custom protocols.
- Some examples of applications that use RTOS are industrial control, telephone switching, flight control, and real-time simulations.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can perform read and write operations within a strict performance envelope, usually defined on the order of seconds to milliseconds.
- An RTDB is different from a conventional database, such as Oracle or MySQL, which are designed for batch processing, data warehousing, and business analytics, but do not guarantee any timing requirements.
- An RTDB typically has the following features:
  - Temporal consistency: The ability to maintain the validity and freshness of data, which may change over time or expire after a certain period.
  - Concurrency control: The ability to handle multiple transactions that access or modify the same data, while ensuring data integrity and isolation.
  - Scheduling: The ability to assign priorities and deadlines to transactions, and execute them in an optimal order, while avoiding conflicts and deadlocks.
  - Recovery: The ability to restore the database to a consistent state, in case of failures or errors, without violating the timing constraints.
- Some examples of applications that use RTDB are stock trading, online gaming, sensor networks, and multimedia systems.



### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks in a system that has strict timing constraints. An RTOS is different from a general-purpose operating system, which may not be able to meet the deadlines or respond as quickly as required by the system.

Some of the features of an RTOS are:

- **Small and fast**: An RTOS is designed to be compact and efficient, occupying less memory and consuming fewer resources than a general-purpose operating system. An RTOS can also boot up and shut down quickly, minimizing the downtime of the system.
- **Responsive and deterministic**: An RTOS can respond to events and interrupts in a timely and consistent manner, ensuring that the system behaves as expected every time. An RTOS can also prioritize the tasks according to their urgency and importance, and preempt the lower-priority tasks if necessary, to meet the deadlines of the higher-priority tasks.
- **Scalable and adaptable**: An RTOS can be customized and configured to suit the specific needs and requirements of the system, such as the number of tasks, the hardware platform, the communication protocols, the security features, etc. An RTOS can also support the addition and modification of features and capabilities as the system evolves, without compromising the performance or reliability of the system.
- **Cooperative or preemptive scheduling**: An RTOS can use different scheduling algorithms to manage the tasks in the system. A cooperative scheduling algorithm allows the tasks to run until they are completed or voluntarily yield the control to the kernel, while a preemptive scheduling algorithm allows the kernel to interrupt and suspend the tasks based on their priority and the availability of resources. A cooperative scheduling algorithm is simpler and easier to implement, but it may not be suitable for systems that have critical or time-sensitive tasks. A preemptive scheduling algorithm is more complex and requires more overhead, but it can ensure that the deadlines of the tasks are met and the system is responsive.



# Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time system is a system that is subjected to real-time constraints, i.e., the response should be guaranteed within a specified timing constraint or the system should meet the specified deadline .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization).
- Time services are the functions and mechanisms that provide the real-time system with the ability to measure, manipulate, and synchronize time.
- Time services can be classified into two categories: clock services and timer services.
- Clock services are the functions and mechanisms that provide the real-time system with the ability to measure the current time and the elapsed time. Clock services can be further divided into two types: physical clocks and logical clocks.
  - Physical clocks are the hardware devices that generate periodic signals based on some physical phenomenon, such as quartz crystal oscillation or atomic transition. Physical clocks can be used to measure the absolute time (also called wall-clock time or UTC time) or the relative time (also called monotonic time or elapsed time) of the system.
  - Logical clocks are the software algorithms that assign logical timestamps to the events and messages that occur in the system. Logical clocks can be used to establish a partial or total order among the events and messages, and to ensure the consistency and causality of the system.
- Timer services are the functions and mechanisms that provide the real-time system with the ability to manipulate the time and to execute actions at specified time instants or intervals. Timer services can be further divided into two types: one-shot timers and periodic timers.
  - One-shot timers are the timers that trigger a single action or event after a specified delay or at a specified absolute time. One-shot timers can be used to implement timeouts, deadlines, or alarms in the system.
  - Periodic timers are the timers that trigger a repeated action or event at a specified interval or frequency. Periodic timers can be used to implement periodic tasks, sampling, or synchronization in the system.



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like Unix strives to provide good average performance, for a RTOS, correct timing is the key feature.
- Unix is not a RTOS by design, but it can be modified or extended to support some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running process and switch to a higher priority one.
  - Priority inheritance: the mechanism to avoid priority inversion, where a low priority process blocks a high priority one.
  - Real-time signals: the signals that are delivered immediately and have a fixed size.
  - POSIX real-time extensions: the standards that define interfaces and behavior for real-time applications on Unix-like systems.
- Linux is a Unix-like OS that has been used as a RTOS for some applications, such as NASA and SpaceX simulations and launch vehicles .
- However, Linux faces some challenges as a RTOS, such as:
  - Kernel architecture: Linux is designed for general purpose computing, not for real-time applications. The kernel is not fully preemptible and has some non-deterministic components, such as memory management and device drivers.
  - Hardware support: Linux may not support some hardware features that are useful for real-time applications, such as timers, interrupts, and watchdogs.
  - Testing and validation: Linux is a complex and evolving system that may introduce bugs and regressions that affect real-time performance. Testing and validating Linux as a RTOS is a difficult and costly task.
- Therefore, Unix and Linux are not ideal choices for RTOS, but they can be adapted or combined with other solutions to meet some real-time requirements.



### POSIX Issues

- POSIX stands for Portable Operating System Interface, which is a family of standards that define a common interface for operating systems, especially UNIX-based ones.
- POSIX aims to promote portability and interoperability of applications across different platforms, which is important for long-lived and complex systems.
- POSIX also covers real-time extensions and multi-threading, which are essential for real-time systems that require predictable and timely responses to events.
- However, POSIX also faces some issues and challenges when applied to real-time systems, such as:
  - POSIX does not specify the performance or quality of service of the operating system services, which may vary depending on the implementation and hardware.
  - POSIX does not address some real-time specific features, such as priority inheritance, sporadic servers, or deadline scheduling.
  - POSIX does not guarantee the compatibility or conformance of different operating systems to the standard, which may result in inconsistencies and incompatibilities.
  - POSIX may not be able to keep up with the evolving needs and requirements of real-time systems, which may demand more advanced and specialized features and functionalities.
- Therefore, POSIX may not be sufficient or optimal for some real-time systems, and may require additional extensions, modifications, or adaptations to meet the real-time constraints and goals .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the characteristics of temporal data for the unit 5 of real time systems and databases.

### Characteristics of Temporal Data

- Temporal data is the data that represents time in some form, and allows other data to be placed in a chronological sequence, or to be analyzed chronologically.
- Temporal data can be classified into three types: event time, valid time, and transaction time.
  - Event time is the time when a fact occurs in the real world, such as the birth date of a person, the start date of a project, or the date of a purchase.
  - Valid time is the time period during which a fact is true in the real world, such as the duration of a person's employment, the validity of a contract, or the availability of a product.
  - Transaction time is the time when a fact is recorded in the database, such as the timestamp of an insertion, an update, or a deletion.
- Temporal data can be used to support various applications that require historical, current, or future information, such as weather forecasting, traffic monitoring, demographic analysis, or business intelligence.
- Temporal data can be stored and manipulated using temporal databases, which are databases that support temporal data types, temporal queries, and temporal integrity constraints.
- Temporal databases can be uni-temporal, bi-temporal, or tri-temporal, depending on the number of temporal aspects they capture.
  - Uni-temporal databases capture only one temporal aspect, such as event time, valid time, or transaction time.
  - Bi-temporal databases capture two temporal aspects, such as event time and valid time, or valid time and transaction time.
  - Tri-temporal databases capture all three temporal aspects, such as event time, valid time, and transaction time.
- Temporal data can be represented using various models, such as the snapshot model, the state model, the timestamp model, the interval model, or the bitemporal model.
  - The snapshot model represents temporal data as a series of snapshots, each corresponding to a point in time.
  - The state model represents temporal data as a series of states, each corresponding to a time interval.
  - The timestamp model represents temporal data as a set of tuples, each with a timestamp attribute that indicates the event time or the transaction time.
  - The interval model represents temporal data as a set of tuples, each with a pair of attributes that indicate the start and end of the valid time.
  - The bitemporal model represents temporal data as a set of tuples, each with four attributes that indicate the event time, the valid time, the transaction time, and the decision time.
- Temporal data can be queried using various languages, such as SQL, temporal SQL, temporal relational algebra, or temporal relational calculus.
  - SQL is the standard query language for relational databases, but it does not support temporal data types or temporal queries natively.
  - Temporal SQL is an extension of SQL that supports temporal data types, such as date, time, interval, or period, and temporal queries, such as temporal selection, temporal projection, temporal join, or temporal aggregation.
  - Temporal relational algebra is an extension of relational algebra that supports temporal data types and temporal operators, such as temporal union, temporal difference, temporal intersection, or temporal product.
  - Temporal relational calculus is an extension of relational calculus that supports temporal data types and temporal predicates, such as temporal equality, temporal inclusion, temporal overlap, or temporal precedence.
- Temporal data can be maintained using various techniques, such as temporal consistency, temporal normalization, or temporal indexing .
  - Temporal consistency is the property that ensures that the temporal data in the database reflects the temporal facts in the real world, and that the temporal data does not contain any contradictions, anomalies, or redundancies.
  - Temporal normalization is the process of decomposing the temporal data into smaller and simpler temporal relations, such that the temporal data satisfies certain temporal normal forms, such as temporal first normal form, temporal second normal form, or temporal Boyce-Codd normal form.
  - Temporal indexing is the process of creating and maintaining temporal indexes, which are data structures that facilitate the efficient retrieval and manipulation of temporal data, such as temporal B-trees, temporal R-trees, or temporal hash tables.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to process data that is time-sensitive and relevant to the current situation. If the data is outdated or inaccurate, the real-time system may produce incorrect or unsafe results.
- Temporal consistency can be measured by the temporal validity and the temporal accuracy of the data .
  - Temporal validity is the degree to which the data stored in the database is within a predefined freshness interval from the current time. Data that is older than the freshness interval is considered invalid and should not be used by the real-time system .
  - Temporal accuracy is the degree to which the data stored in the database matches the actual value of the physical entity that it represents. Data that has a large deviation from the actual value is considered inaccurate and should not be used by the real-time system .
- Temporal consistency can be maintained by using various techniques, such as periodic updates, triggered updates, imprecise computation, and temporal caching  .
  - Periodic updates are updates that are performed at regular intervals to refresh the data stored in the database. Periodic updates can ensure temporal validity, but they may incur high overhead and may not capture the changes in the physical environment in a timely manner .
  - Triggered updates are updates that are performed when a certain condition is met, such as a change in the physical environment or a request from a real-time transaction. Triggered updates can ensure temporal accuracy, but they may incur high contention and may not guarantee temporal validity .
  - Imprecise computation is a technique that allows the real-time system to use data that is not temporally consistent, but has a bounded error. Imprecise computation can reduce the overhead and contention of updates, but it may compromise the quality and safety of the results .
  - Temporal caching is a technique that stores the data that is frequently accessed by the real-time system in a local memory, such as a cache or a buffer. Temporal caching can reduce the access time and the contention of the data, but it may introduce inconsistency and coherence issues .



### Concurrency Control

Concurrency control is a technique to ensure the correctness and consistency of data in a database system when multiple transactions are executed concurrently. Concurrency control aims to prevent conflicts among transactions that may access or modify the same data items, such as lost updates, dirty reads, unrepeatable reads, and phantom reads.

Concurrency control can be achieved by using different methods, such as locking, timestamping, validation, and multiversioning. Each method has its own advantages and disadvantages, and may be suitable for different scenarios and requirements.

Concurrency control is especially important for real-time database systems, which have to deal with transactions that have timing constraints and deadlines. Real-time database systems must ensure that transactions are not only serializable, but also schedulable, meaning that they can be executed within their deadlines. Moreover, real-time database systems must be able to adapt to changes in the workload and the environment, and prioritize the most critical transactions.

Some of the challenges and issues of concurrency control in real-time database systems are:

- How to balance the trade-off between data consistency and timeliness?
- How to handle transactions with different priorities and deadlines?
- How to cope with resource contention and overload situations?
- How to deal with data freshness and staleness?
- How to integrate concurrency control with real-time scheduling algorithms?

Some of the approaches and techniques for concurrency control in real-time database systems are:

- Lock-based protocols, such as two-phase locking (2PL), priority inheritance protocol (PIP), priority ceiling protocol (PCP), and optimistic concurrency control (OCC).
- Timestamp-based protocols, such as basic timestamp ordering (BTO), optimistic timestamp ordering (OTO), and timestamp ordering with restart (TOR).
- Validation-based protocols, such as optimistic concurrency control with validation (OCCV), and validation with priority inheritance (VPI).
- Multiversion protocols, such as multiversion two-phase locking (MV2PL), multiversion timestamp ordering (MVTO), and multiversion optimistic concurrency control (MVOCC).

Each protocol has its own assumptions, rules, and performance characteristics, and may be suitable for different types of transactions and applications. For example, lock-based protocols are more suitable for transactions that have high data contention and low abort rates, while timestamp-based protocols are more suitable for transactions that have low data contention and high abort rates. Validation-based protocols are more suitable for transactions that have short execution times and low validation costs, while multiversion protocols are more suitable for transactions that have long execution times and high validation costs.

The choice of the concurrency control protocol for a real-time database system depends on various factors, such as the data access patterns, the transaction characteristics, the system parameters, and the performance objectives. A good concurrency control protocol should be able to achieve high concurrency, low blocking, low aborting, low overhead, and high schedulability.



### Overview of Commercial Real Time databases for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases have some special characteristics that distinguish them from traditional databases, such as:
  - Timeliness: the ability to provide correct and consistent responses within specified deadlines.
  - Concurrency: the ability to handle multiple transactions or queries simultaneously without compromising data integrity or performance.
  - Predictability: the ability to guarantee a certain level of service quality or performance under varying workloads or system conditions.
  - Availability: the ability to ensure continuous operation and data accessibility even in the presence of failures or faults.
- Real-time databases can be classified into two types based on their timing constraints:
  - Hard real-time databases: these databases must meet all the deadlines, otherwise the system may fail or cause severe consequences. Examples of hard real-time applications are air traffic control, nuclear power plant control, and missile guidance systems.
  - Soft real-time databases: these databases can tolerate some deadline misses, but the system performance or quality may degrade. Examples of soft real-time applications are online gaming, video streaming, and e-commerce.
- Some of the commercial real-time databases available in the market are  :
  - Raima Database Manager (RDM): a high-performance, embedded, in-memory database that supports hard and soft real-time applications. It offers ACID transactions, SQL and NoSQL interfaces, data replication, encryption, compression, and more.
  - Altus Group: a leading provider of commercial real estate data and analytics that offers historical and current market information, property valuations, investment analysis, and more.
  - CoStar: a leading provider of commercial real estate information, analytics, and online marketplaces that covers over 5.5 million properties and 18 billion square feet of space.
  - Google Cloud Firestore: a highly scalable, fully managed NoSQL database service for large analytical and operational workloads. It offers up to 99.999% availability, real-time updates, offline support, and more.

