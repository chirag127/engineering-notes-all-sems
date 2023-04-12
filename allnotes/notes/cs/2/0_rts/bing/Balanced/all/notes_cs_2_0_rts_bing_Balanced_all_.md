

# Real Time System

A real time system is a system that can perform its tasks within a specified time limit, and can coordinate with other systems or devices that have different clocks or time frames. A real time system is often used to control or monitor an environment that changes rapidly or unpredictably, such as industrial processes, robotics, machine vision, flight control, etc.   

Some of the main characteristics of a real time system are:

- **Timeliness**: The system must produce the correct output or response within a given deadline, otherwise it may cause a system failure or unacceptable consequences. The deadline can be hard or soft, depending on the criticality of the task. A hard deadline means that missing it will result in a catastrophic failure, while a soft deadline means that missing it will degrade the system performance or quality, but not cause a failure.  
- **Time synchronization**: The system must be able to coordinate with other systems or devices that have different clocks or time frames, and ensure that the events or actions are executed in the correct order and at the correct time. The system may use various methods to synchronize the clocks, such as network time protocol (NTP), global positioning system (GPS), or atomic clocks.  
- **Concurrency**: The system must be able to handle multiple tasks or events that occur simultaneously or in parallel, and allocate the available resources (such as CPU, memory, disk, network, etc.) to them efficiently and fairly. The system may use various techniques to manage the concurrency, such as multitasking, multithreading, multiprocessing, or distributed computing.  
- **Determinism**: The system must be able to produce the same output or response for the same input or event, regardless of the system state or external factors. The system must avoid or minimize the sources of non-determinism, such as interrupts, exceptions, shared resources, or random numbers.  
- **Reliability**: The system must be able to perform its tasks correctly and consistently, and recover from any errors or faults that may occur. The system must ensure the integrity and availability of the data and the resources, and prevent or mitigate the impact of any failures. The system may use various mechanisms to enhance the reliability, such as redundancy, fault tolerance, error detection and correction, or backup and recovery.



# Unit 1 - Introduction of Real Time System

- A real-time system is a system that can process data and events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization) .
- A real-time system can be classified into two types based on the timing constraints: hard real-time system and soft real-time system .
  - A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur. For example, flight control systems, airbag systems, etc.
  - A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail. For example, video streaming, online gaming, etc.
- A real-time system requires a real-time operating system (RTOS) that can manage the system resources and tasks with a scheduler, data buffers, or fixed task priorities .
  - An RTOS is different from a time-sharing operating system, such as Unix, which does not guarantee the timeliness of the system response.
  - An RTOS can be preemptive or cooperative, depending on whether the tasks can be interrupted by higher priority tasks or not.
  - An RTOS can use different scheduling algorithms, such as rate-monotonic, earliest deadline first, least laxity first, etc., to assign priorities and deadlines to the tasks.



# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or stimuli within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a flight control system or a nuclear reactor control system.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system or a voice recognition system.
- A real time system can be characterized by four attributes: timeliness, concurrency, predictability and dependability.
- Timeliness means that the system must deliver the correct results at the correct time, according to the specified deadlines.
- Concurrency means that the system must handle multiple events or tasks simultaneously, without blocking or interfering with each other.
- Predictability means that the system must behave consistently and deterministically, without any unexpected delays or errors.
- Dependability means that the system must be reliable, available, safe and secure, without any faults or failures.



# Typical Real Time Applications

A real-time application (RTA) is an application that has strict time constraints on its performance and reliability. RTAs often interact with the physical world and require fast and accurate responses to external events. RTAs can be classified into two types: hard real-time and soft real-time. Hard real-time applications have absolute deadlines that must be met, otherwise the system may fail or cause severe consequences. Soft real-time applications have relative deadlines that can be occasionally missed, but the system can still function with reduced quality or performance.

Some examples of typical real-time applications are:

- **Video conferencing**: This is an application that allows users to communicate with each other through video and audio streams over the Internet. Video conferencing requires real-time processing and transmission of multimedia data, as well as synchronization and coordination among multiple participants. Video conferencing is a soft real-time application, as some delays or losses of data may be tolerable, but they may affect the user experience and satisfaction.
- **Voice over Internet Protocol (VoIP)**: This is an application that enables users to make voice calls over the Internet, instead of using traditional phone lines. VoIP requires real-time encoding and decoding of voice signals, as well as packetization and routing of data over the network. VoIP is a soft real-time application, as some jitter or distortion of voice may be acceptable, but they may reduce the quality and intelligibility of speech.
- **Online gaming**: This is an application that allows users to play games with other users over the Internet. Online gaming requires real-time rendering and animation of graphics, as well as interaction and synchronization among multiple players. Online gaming is a soft real-time application, as some lag or inconsistency of game state may be acceptable, but they may affect the fairness and enjoyment of the game.
- **Community storage applications**: These are applications that allow users to store and share data over the Internet, such as cloud storage, peer-to-peer file sharing, and distributed databases. Community storage applications require real-time replication and consistency of data, as well as fault tolerance and security of the system. Community storage applications are soft real-time applications, as some delay or unavailability of data may be acceptable, but they may affect the functionality and performance of the system.
- **Some e-commerce applications**: These are applications that allow users to buy and sell goods and services over the Internet, such as online shopping, online auctions, and online banking. Some e-commerce applications require real-time processing and verification of transactions, as well as coordination and communication among multiple parties. Some e-commerce applications are soft real-time applications, as some delay or failure of transactions may be acceptable, but they may affect the efficiency and trustworthiness of the system.
- **Real-time operating system (RTOS)**: This is a system software that provides the basic functions and services for real-time applications, such as scheduling, memory management, communication, and synchronization. RTOS is a hard real-time application, as it must guarantee the timely and correct execution of the tasks and processes in the system, otherwise the system may malfunction or crash.
- **Instant messaging (IM) applications**: These are applications that allow users to send and receive text, voice, or video messages over the Internet, such as WhatsApp, Skype, and Telegram. IM applications require real-time delivery and notification of messages, as well as encryption and authentication of data. IM applications are soft real-time applications, as some delay or loss of messages may be acceptable, but they may affect the convenience and privacy of the users.
- **Team collaboration applications**: These are applications that allow users to work together on projects or tasks over the Internet, such as Google Docs, Slack, and Trello. Team collaboration applications require real-time editing and updating of documents, as well as coordination and communication among team members. Team collaboration applications are soft real-time applications, as some delay or inconsistency of information may be acceptable, but they may affect the productivity and quality of the work.



# Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must respond to events within a specified time interval.
- A real-time system can be classified as either hard or soft, depending on the consequences of missing a deadline.
- A hard real-time system is one where missing a deadline can cause a catastrophic failure or unacceptable loss. For example, a nuclear reactor control system or an air traffic control system.
- A soft real-time system is one where missing a deadline can degrade the performance or quality of service, but not cause a failure. For example, a video streaming system or a multimedia application.
- A real-time system consists of a set of tasks that must be executed periodically or sporadically, depending on the arrival of events or requests.
- A task is a unit of computation that has a well-defined functionality and a set of timing constraints, such as a release time, a deadline, and an execution time.
- A release time is the earliest time at which a task can start its execution. A release time can be fixed or variable, depending on the nature of the task.
- A fixed release time is one that is known in advance and does not depend on the occurrence of any event or condition. For example, a periodic task that is executed every 10 milliseconds has a fixed release time of 0, 10, 20, ... milliseconds.
- A variable release time is one that is determined by the occurrence of an event or condition that is not known in advance. For example, a sporadic task that is triggered by a sensor reading or a user input has a variable release time that depends on when the sensor or the user generates the event.
- A release time is an important parameter for scheduling real-time tasks, as it determines the order and priority of the tasks that are ready to execute at any given time.
- A release time can also affect the feasibility and optimality of a real-time system, as it can impose constraints on the allocation and utilization of the system resources.



# Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by **Friday, 24 March 2023** before **5:00 PM**.
- The notes should be handwritten and scanned in PDF format.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be clear, concise, and accurate. They should include diagrams, tables, and examples wherever necessary.
- The notes should be uploaded on the online portal with the file name **RTS_Unit1_YourName_YourRollNumber.pdf**.
- The notes will be evaluated based on the following criteria:
  - Completeness and correctness of the content
  - Neatness and readability of the handwriting
  - Organization and presentation of the notes
  - Adherence to the format and deadline
- The notes will carry **10 marks** out of the total **100 marks** for the subject of Real Time System.
- Late submissions will not be accepted and will result in zero marks for the notes.



# Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system are known as Reliability Constraints.
- Some common types of performance constraints are:
  - Delay Constraint: A delay constraint describes the minimum time interval between the occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between the occurrence of two consecutive events.
  - Duration Constraint: A duration constraint describes the maximum or minimum time interval for the execution of a task.
- Some common types of reliability constraints are:
  - Synchronization Constraint: A synchronization constraint describes the order or precedence of events or tasks.
  - Consistency Constraint: A consistency constraint describes the validity or accuracy of data or information.
  - Availability Constraint: An availability constraint describes the minimum or maximum time interval for the availability of a resource or service.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.
- Timing constraints can be expressed using various constructs in requirements languages, such as temporal logic, interval logic, or event calculus.
- Timing constraints can be validated using automatic test systems that can measure the actual response time, execution time, or synchronization time of the system.



# Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- A hard real time system is also known as an immediate real time system .
- A hard real time system is typically found interacting at a low level with physical hardware, in embedded systems .
- Examples of hard real time systems are nuclear power plant control, air traffic control, missile guidance, medical devices, and video game systems  .
- Characteristics of hard real time systems are:
  - The size of data and code is small and fixed .
  - The response time is in milliseconds or microseconds .
  - The peak load performance should be predictable and consistent .
  - The safety is critical and the system cannot tolerate any errors .
  - The system is usually preemptive and uses priority-based scheduling algorithms .



# Soft Real Time Systems

- A soft real time system is a system that has a **flexible deadline** for completing its tasks, rather than a precise moment .
- A soft real time system can **tolerate some delay** or jitter in the execution of its tasks, without causing a system failure .
- A soft real time system can **run on multiple cores** and impose fewer restrictions on applications, unlike a hard real time system that requires a single core and strict scheduling policies .
- A soft real time system can **adapt to dynamic changes** in the workload or the environment, such as varying network latency or user input.
- A soft real time system can **trade off quality for timeliness**, meaning that it can produce lower quality output if it cannot meet the deadline, rather than aborting the task.
- Examples of soft real time systems are **streaming audio-video**, **multimedia applications**, **online gaming**, **voice over IP**, etc  .



# Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps us to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements :
  - A workload model: It specifies the application supported by the system, such as the set of tasks or jobs, their parameters (e.g., execution time, deadline, resource dependencies, etc.), and their relations (e.g., precedence graph, task graph, etc.).
  - A resource model: It describes the resources (e.g., CPU, memory, network, etc.) available to the system, their types (e.g., preemptive, non-preemptive, shared, exclusive, etc.), and their relations (e.g., hierarchy, contention, etc.).
  - A service model: It defines the policies and mechanisms used by the system to allocate resources to tasks, such as scheduling algorithms, synchronization protocols, admission control, etc.
- An example of a reference model is the Real-time Control System (RCS) architecture, which combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .



# Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. Examples of resources are memory, files, printers, and sensors.
- Processors and resources can be classified into two categories: dedicated and shared.
- Dedicated processors and resources are allocated to a single job or task and cannot be used by any other job or task. They are usually faster and more reliable than shared ones. Examples of dedicated processors and resources are private memory, registers, and caches.
- Shared processors and resources are accessible by multiple jobs or tasks, but they need to be managed and scheduled properly to avoid conflicts and delays. They are usually slower and less reliable than dedicated ones. Examples of shared processors and resources are CPU, disk, network, and printer.
- Processors and resources can also be classified into two categories: preemptive and non-preemptive.
- Preemptive processors and resources can be interrupted and released by a higher priority job or task at any time. They are usually more flexible and responsive than non-preemptive ones. Examples of preemptive processors and resources are CPU, disk, and network.
- Non-preemptive processors and resources cannot be interrupted and released by a higher priority job or task until they are finished or explicitly released. They are usually more stable and predictable than preemptive ones. Examples of non-preemptive processors and resources are memory, files, and printers.
- Processors and resources are critical for the performance and correctness of real-time systems. They need to be designed, configured, and optimized according to the requirements and constraints of the real-time applications .



# Temporal Parameters of Real Time Workload

- A real time workload is a set of jobs that need to be executed by a real time system within certain time constraints.
- A job is a unit of work that requires processor time and other resources to complete.
- A job can be periodic, aperiodic, or sporadic, depending on its arrival pattern and frequency.
- A job can be characterized by its temporal parameters, which describe its timing requirements and constraints.
- The temporal parameters of a job are:

  - Release time (r_i): the earliest time at which the job can start execution.
  - Absolute deadline (d_i): the latest time by which the job must finish execution.
  - Relative deadline (D_i): the maximum time allowed for the job to complete after its release time.
  - Feasible interval [(r_i, d_i)]: the time interval in which the job can be feasibly executed.
  - Execution time (e_i): the actual time required by the job to complete on the processor.
  - Laxity (l_i): the amount of time left for the job to complete before its deadline, given by l_i = d_i - e_i - t, where t is the current time.

- The temporal parameters of a job can be used to determine its priority, schedulability, and performance in a real time system.



# Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod, which is the least common multiple of all the periods.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion.
- The utilization of a periodic task is defined as the ratio of its execution time to its period: Ui = ei / Pi.
- The utilization of a set of periodic tasks is the sum of their individual utilizations: U = Σ Ui.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline slack Si for each task τi, to allow the flexibility that the actual deadline of a job may be at most Si time units earlier or later than the relative deadline of the task.
- The periodic task model can be used to analyze the schedulability of a set of tasks under different scheduling algorithms, such as rate-monotonic, earliest deadline first, or least laxity first .



# Precedence Constraints and Data Dependency

- Precedence constraints are the restrictions on the order of execution of jobs in a real time system. They are usually represented by a directed graph called a precedence graph, where the vertices are the jobs and the edges are the constraints  .
- Data dependency is the situation where the output of one job is used as the input of another job in a real time system. Data dependency cannot be captured by a precedence graph, but requires additional information such as the data flow and the synchronization mechanisms .
- Precedence constraints and data dependency are important factors to consider when scheduling real time systems, as they affect the feasibility, optimality, and performance of the system .




## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or before the system starts running. It is based on the known characteristics of the tasks, such as their periods, execution times, deadlines, and priorities. Static scheduling is suitable for systems that have fixed and periodic tasks, and that do not have unpredictable events or changes in the workload .
  - Dynamic scheduling is done at run time or during the system execution. It is based on the current state of the system, such as the ready queue, the available resources, the current time, and the events that occur. Dynamic scheduling is suitable for systems that have variable and aperiodic tasks, and that have unpredictable events or changes in the workload .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running. The lower priority task resumes its execution when the higher priority task finishes or is blocked. Preemptive scheduling can reduce the response time and the deadline miss ratio of the tasks, but it can also introduce overhead and complexity in the system .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running. The lower priority task completes its execution before the higher priority task can start. Non-preemptive scheduling can avoid the overhead and complexity of preemption, but it can also increase the response time and the deadline miss ratio of the tasks .
- Real time scheduling algorithms are the rules or methods that determine which task to execute next in the system. There are many real time scheduling algorithms, such as rate monotonic, earliest deadline first, least laxity first, round robin, etc. Each algorithm has its own advantages and disadvantages, and its own schedulability conditions or tests .
- Real time scheduling analysis is the process of evaluating and verifying the performance and correctness of the system and the algorithms under different scenarios and assumptions. Real time scheduling analysis can be done using mathematical models, simulation tools, or empirical methods .



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of allocating CPU time to tasks that have timing constraints, such as deadlines or periodicity. Real time scheduling aims to ensure that the system meets its timing requirements and delivers correct functionality. There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the environment. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival times, execution times, deadlines, and periods, are known at design time. In this approach, a static schedule is computed offline, based on the worst-case execution times of the tasks, and stored in a table. The table specifies the start and end times of each task in each cycle. A timer interrupts the system at predefined instants and triggers the execution of the next task in the table. This approach is simple, predictable, and easy to verify, but it is not flexible or adaptable to dynamic changes in the system or the environment. It also requires accurate estimation of the worst-case execution times of the tasks, which may be difficult or impossible for some applications.    

- **Round-robin approach**: This approach is a commonly used technique in time-shared systems, where the goal is to provide fair and responsive service to multiple users. In this approach, tasks are scheduled in a repetitive manner, based on a time slice allocated to each task. The scheduler maintains a queue of ready tasks and assigns the CPU to the first task in the queue for a fixed amount of time, called the quantum. After the quantum expires, the task is preempted and moved to the end of the queue, and the next task in the queue is executed. This approach is simple, fair, and easy to implement, but it does not consider the timing constraints or the priorities of the tasks. It may also cause high overhead and latency due to frequent context switches.  

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach, where tasks are assigned different weights or quanta, based on their importance or resource requirements. The scheduler maintains a queue of ready tasks and assigns the CPU to the first task in the queue for a time slice proportional to its weight. After the time slice expires, the task is preempted and moved to the end of the queue, and the next task in the queue is executed. This approach is more flexible and responsive than the round-robin approach, as it allows differentiating the service quality among tasks. However, it still does not consider the timing constraints or the deadlines of the tasks. It may also cause starvation or missed deadlines for low-weight tasks, if the high-weight tasks consume too much CPU time.  

- **Priority-driven approach**: This approach is widely used for soft or firm real time systems, where some tasks may tolerate occasional deadline misses or reduced service quality. In this approach, tasks are assigned different priorities, based on their timing constraints, importance, or resource requirements. The scheduler maintains a queue of ready tasks and assigns the CPU to the highest priority task in the queue. If a higher priority task arrives or becomes ready, the current task is preempted and the higher priority task is executed. This approach is more flexible and adaptable than the clock-driven approach, as it can handle dynamic changes in the system or the environment. It also considers the timing constraints and the deadlines of the tasks, and tries to minimize the number of deadline misses. However, this approach is more complex and difficult to verify, as it may cause unpredictable interactions and conflicts among tasks. It may also cause starvation or missed deadlines for low-priority tasks, if the high-priority tasks consume too much CPU time or block the shared resources.    

- **Dynamic versus static systems**: This classification refers to whether the system parameters, such as the task set, the task properties, the system state, or the environment, are fixed or variable during the system execution. A static system is one where all the system parameters are known and fixed at design time, and do not change during the system execution. A dynamic system is one where some or all of the system parameters are unknown or variable at design time, and may change during the system execution. Static systems are easier to analyze and schedule, as they



# Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling .
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A schedule of the jobs is computed off-line and is stored for use at run-time.
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling can be implemented using cyclic scheduling, table-driven scheduling, or hybrid scheduling.
- Cyclic scheduling is a simple method that assigns a fixed time slot to each job in a cycle.
- Table-driven scheduling is a more flexible method that uses a precomputed table to specify the start time and duration of each job.
- Hybrid scheduling is a combination of cyclic and table-driven scheduling that can handle both periodic and aperiodic jobs.
- Clock-driven scheduling has some advantages and disadvantages:
  - Advantages:
    - It is easy to implement and verify.
    - It can guarantee the deadlines of hard real-time jobs.
    - It can avoid priority inversion and blocking problems.
  - Disadvantages:
    - It is not suitable for dynamic or unpredictable workloads.
    - It may waste CPU time and resources if the jobs are not evenly distributed.
    - It may not be able to handle sporadic or urgent jobs.



# Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights  .
- The weight of a job serves to influence the portion of service time allocated to it.
- A job with a higher weight will receive more service opportunities than a job with a lower weight.
- The service opportunities are distributed proportionally to the weights of the jobs.
- For example, if there are three jobs with weights 1, 2, and 3, then the service opportunities will be allocated as follows: 1/6, 2/6, and 3/6.
- Weighted round robin can achieve a fair and efficient allocation of resources among different classes of jobs.
- It can also handle variable-length jobs and bursty traffic.
- However, it may not be suitable for hard real-time systems where strict deadlines and priorities are required.
- It may also suffer from starvation if the weights are not properly configured.



# Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Priority-driven scheduling can be applied to both periodic and aperiodic tasks.
- Periodic tasks have a fixed inter-arrival time and a fixed deadline.
- Aperiodic tasks have a variable inter-arrival time and a variable deadline.
- Priority-driven scheduling can also handle mixed-criticality tasks, which have different levels of importance and different requirements for timeliness.
- Priority-driven scheduling can improve the real-time performance and predictability of real-time systems by reducing the response time and the deadline miss ratio of tasks.
- However, priority-driven scheduling also faces some challenges, such as priority inversion, resource contention, and schedulability analysis.
- Priority inversion occurs when a lower-priority task holds a resource that is needed by a higher-priority task, thus delaying the execution of the latter.
- Resource contention occurs when multiple tasks compete for the same resource, thus increasing the waiting time and the blocking time of tasks.
- Schedulability analysis is the process of determining whether a set of tasks can meet their deadlines under a given scheduling algorithm and system configuration.
- Schedulability analysis can be complex and computationally expensive for priority-driven scheduling, especially for dynamic and mixed-criticality tasks.



# Dynamic Versus Static Systems

- A **dynamic system** is one that changes its behavior or configuration in response to external events or inputs, such as workload, resource availability, or user requests.
- A **static system** is one that has a fixed and predetermined behavior or configuration that does not change during its operation, such as task set, task priorities, or resource allocation.
- Dynamic and static systems have different advantages and disadvantages for real-time scheduling, depending on the characteristics and requirements of the application domain.

## Advantages of Dynamic Systems

- Dynamic systems can adapt to changing conditions and unpredictable events, such as varying workload, resource failures, or user preferences.
- Dynamic systems can optimize the performance metrics of the system, such as response time, throughput, or utilization, by making scheduling decisions based on the current state of the system and the environment.
- Dynamic systems can handle a larger and more diverse set of tasks, as they do not need to know the task parameters or dependencies in advance.

## Disadvantages of Dynamic Systems

- Dynamic systems incur more overhead and complexity for making scheduling decisions at run-time, as they need to collect and process information about the system and the environment.
- Dynamic systems are harder to analyze and verify, as they may exhibit non-deterministic or unpredictable behavior, depending on the inputs and events that occur during the system operation.
- Dynamic systems may not guarantee the satisfaction of the timing constraints of the tasks, as they may not have enough information or resources to schedule all the tasks within their deadlines.

## Advantages of Static Systems

- Static systems have less overhead and complexity for making scheduling decisions, as they are done before the system runs, based on the known task parameters and dependencies.
- Static systems are easier to analyze and verify, as they exhibit deterministic and predictable behavior, regardless of the inputs and events that occur during the system operation.
- Static systems can guarantee the satisfaction of the timing constraints of the tasks, as they can check the feasibility of the schedule before the system runs, and reject any task set that is not schedulable.

## Disadvantages of Static Systems

- Static systems cannot adapt to changing conditions and unpredictable events, such as varying workload, resource failures, or user preferences.
- Static systems may not optimize the performance metrics of the system, such as response time, throughput, or utilization, as they may not exploit the opportunities or cope with the challenges that arise during the system operation.
- Static systems can handle a smaller and more restricted set of tasks, as they need to know the task parameters and dependencies in advance, and may not accept any task set that is not schedulable.



# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints. This means that EDF can schedule any set of tasks that is schedulable by any other algorithm.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints. This means that LST can schedule any set of tasks that is schedulable by any other algorithm that respects the precedence constraints.
- However, EDF and LST are not optimal for non-preemptive scheduling or for tasks with shared resources or synchronization requirements. In these cases, EDF and LST may fail to produce a feasible schedule even if one exists.



# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a static priority scheduling algorithm for real-time systems .
- It assigns priorities to tasks based on their periods or cycle durations, such that shorter period tasks have higher priorities .
- It is a preemptive algorithm, meaning that a higher priority task can interrupt a lower priority task that is currently executing.
- It is optimal for a set of periodic, independent and deterministic tasks, meaning that it can always meet the deadlines of all tasks if they exist .
- It has a schedulability test that can determine if a given set of tasks can be scheduled by RMA or not .
- The schedulability test is based on the utilization factor of the tasks, which is the ratio of their execution time to their period .
- The utilization factor of a set of tasks must be less than or equal to a certain bound, which depends on the number of tasks, for RMA to be feasible .
- The bound is given by the formula: U <= n*(2^(1/n) - 1), where n is the number of tasks .
- If the utilization factor exceeds the bound, RMA may still be able to schedule the tasks, but it is not guaranteed .
- In that case, a more precise schedulability test can be used, which checks the worst-case response time of each task against its deadline .
- The worst-case response time of a task is the maximum time it takes to complete its execution, considering the interference from higher priority tasks .
- The worst-case response time can be calculated iteratively using the formula: R_i = C_i + sum(j=1 to i-1) ceil(R_i/T_j) * C_j, where C_i is the execution time of task i, T_j is the period of task j, and R_i is the response time of task i .
- The task set is schedulable by RMA if and only if R_i <= D_i for all tasks, where D_i is the deadline of task i .
- RMA has some advantages and disadvantages as a real-time scheduling algorithm.
- Some advantages are: simplicity, optimality for periodic tasks, low overhead, and predictability.
- Some disadvantages are: poor resource utilization, inability to handle aperiodic or sporadic tasks, priority inversion, and deadline misses for tasks with long periods.



# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system without knowledge about the future tasks.
- The advantages of offline scheduling are:
  - It can guarantee the schedulability of all tasks if the schedule is feasible.
  - It can reduce the overhead of run-time scheduling decisions.
  - It can optimize the resource utilization and energy consumption.
- The disadvantages of offline scheduling are:
  - It requires the complete knowledge of all task parameters, such as release time, execution time, deadline, resource requirement, etc.
  - It cannot handle dynamic changes in the system, such as task arrival, task cancellation, task migration, etc.
  - It may not be applicable for systems with unpredictable or stochastic behavior.
- The advantages of online scheduling are:
  - It can handle dynamic and unpredictable situations in the system.
  - It can adapt to the changing workload and resource availability.
  - It can provide flexibility and responsiveness to the user requests.
- The disadvantages of online scheduling are:
  - It may not guarantee the schedulability of all tasks, especially under overload conditions.
  - It may incur higher overhead of run-time scheduling decisions.
  - It may not optimize the resource utilization and energy consumption.
- Online scheduling can be further classified into static and dynamic scheduling.
  - Static scheduling is a technique that assigns a fixed priority to each task and schedules the tasks according to their priorities.
  - Dynamic scheduling is a technique that assigns a variable priority to each task and schedules the tasks according to their current priorities.
  - Static scheduling is simpler and faster than dynamic scheduling, but it may not be optimal or fair for all tasks.
  - Dynamic scheduling is more complex and slower than static scheduling, but it may provide better performance and fairness for all tasks.



# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have random arrival times and no deadlines. Sporadic jobs are jobs that have random arrival times and hard deadlines.
- Priority driven systems are systems that assign priorities to jobs and schedule them according to their priorities. Clock driven systems are systems that schedule jobs according to a predefined table that is based on the system clock.
- Scheduling aperiodic and sporadic jobs in priority driven systems can be challenging because they can interfere with the periodic jobs that have fixed arrival times and deadlines.
- Some of the algorithms for scheduling aperiodic and sporadic jobs in priority driven systems are:
  - Background scheduling: Aperiodic and sporadic jobs are executed only when there are no periodic jobs ready to run. This ensures that periodic jobs always meet their deadlines, but aperiodic and sporadic jobs may have long response times.
  - Polling server: A periodic task with a fixed priority and execution time is used to serve aperiodic and sporadic jobs. The server polls the queue of aperiodic and sporadic jobs at regular intervals and executes one or more of them. This reduces the response time of aperiodic and sporadic jobs, but may cause deadline misses for periodic jobs if the server priority is too high or too low.
  - Deferrable server: A periodic task with a fixed priority and execution time is used to serve aperiodic and sporadic jobs. The server defers its execution until there is an aperiodic or sporadic job in the queue. This avoids wasting the server capacity when there are no aperiodic or sporadic jobs, but may cause deadline misses for periodic jobs if the server priority is too high or too low.
  - Sporadic server: A periodic task with a variable priority and execution time is used to serve aperiodic and sporadic jobs. The server priority is equal to the highest priority of the aperiodic and sporadic jobs in the queue, and the server execution time is equal to the remaining execution time of the job being served. This allows the server to adapt to the arrival and execution time of aperiodic and sporadic jobs, but may cause deadline misses for periodic jobs if the server priority is too high.
  - Slack stealing: Aperiodic and sporadic jobs are executed using the slack time of periodic and sporadic jobs. The slack time is the difference between the deadline and the worst-case execution time of a job. This allows aperiodic and sporadic jobs to be completed early without affecting the periodic and sporadic jobs, but requires the knowledge of the worst-case execution time of all jobs and the computation of the slack time at each scheduling point.
- Scheduling aperiodic and sporadic jobs in clock driven systems can be simpler because the schedule is predetermined and does not depend on the arrival time of jobs. However, clock driven systems may not be able to handle aperiodic and sporadic jobs that have unpredictable execution times or deadlines that are not aligned with the schedule.
- Some of the algorithms for scheduling aperiodic and sporadic jobs in clock driven systems are:
  - Time-driven scheduling: Aperiodic and sporadic jobs are assigned fixed time slots in the schedule. The time slots are allocated according to the expected arrival rate and execution time of aperiodic and sporadic jobs. This ensures that aperiodic and sporadic jobs are executed within their time slots, but may waste the system capacity if the actual arrival rate or execution time is lower than the expected one.
  - Event-driven scheduling: Aperiodic and sporadic jobs are assigned variable time slots in the schedule. The time slots are allocated according to the actual arrival time and execution time of aperiodic and sporadic jobs. This allows the system to adapt to the variability of aperiodic and sporadic jobs, but may cause schedule conflicts if the actual execution time is longer than the allocated time slot.
  - Hybrid scheduling: A combination of time-driven and event-driven scheduling is used to schedule aperiodic and sporadic jobs. The schedule is divided into fixed and variable time slots. The fixed time slots are used for periodic and sporadic jobs, and the variable time slots are used for aperiodic and sporadic jobs. The variable time slots are allocated according to the actual arrival time and execution time of aperiodic and sporadic jobs, but are constrained by the fixed time slots. This allows the system to balance the predictability and adaptability of the schedule, but may require complex algorithms to resolve the schedule conflicts.



## Unit 3 - Resource Sharing

- Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, and network bandwidth, available to multiple users or processes.
- Resource sharing can improve the efficiency, performance, scalability, and reliability of a computer system, as well as reduce the cost and complexity of managing it.
- Resource sharing can be achieved by various methods, such as:
  - Multiprogramming: running multiple programs or processes concurrently on a single processor, by switching between them in a time-sharing manner.
  - Multiprocessing: using multiple processors or cores to execute multiple programs or processes simultaneously or in parallel.
  - Distributed computing: using multiple computers or devices connected by a network to perform a common task or share a common resource.
  - Cloud computing: using a network of remote servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer.
- Resource sharing can also involve different levels of abstraction, such as:
  - Physical level: sharing the physical components of a computer system, such as CPU, memory, disk, and network interface.
  - Logical level: sharing the logical entities of a computer system, such as files, directories, databases, and sockets.
  - Application level: sharing the application-specific resources of a computer system, such as web pages, documents, images, and videos.
- Resource sharing can pose various challenges and risks, such as:
  - Resource contention: the situation where multiple users or processes compete for the same resource, resulting in reduced performance, increased waiting time, or deadlock.
  - Resource allocation: the problem of deciding how to assign the available resources to the users or processes, based on their needs, priorities, and preferences.
  - Resource management: the process of monitoring, controlling, and optimizing the use of resources, to ensure their availability, quality, and security.
  - Resource security: the issue of protecting the resources from unauthorized access, modification, or damage, by enforcing proper authentication, authorization, encryption, and backup mechanisms.



# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, or a peripheral device.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the tasks .
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that a task that has acquired a resource cannot be preempted by another task until it releases the resource. This may cause priority inversion, where a high-priority task is blocked by a low-priority task that holds a resource.
  - Preemptive RAC means that a task that has acquired a resource can be preempted by another task, but the resource is not released until the preempted task resumes and finishes its critical section. This may cause timing anomalies, where a higher priority task may take longer to complete due to preemption.
- Some examples of RAC protocols are:
  - Non-preemptive protocols: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive protocols: Preemptive Priority Ceiling Protocol (PPCP), Preemptive Stack Resource Policy (PSRP), Preemptive Priority Inheritance Protocol (PPIP), etc .



# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, regardless of their original priorities  .
- This protocol is called non-preemptive critical section protocol (NPCS) .
- The advantages of NPCS are:
  - It is simple and easy to implement .
  - It prevents deadlock, as no job is ever blocked or waiting for a resource held by another job  .
- The disadvantages of NPCS are:
  - It may cause priority inversion, as a high-priority job may be delayed by a low-priority job that holds a resource .
  - It may cause resource underutilization, as a resource may be idle while a job that holds it is executing non-critical sections .
  - It may cause long blocking times, as a job may have to wait for the completion of a long critical section by another job .
  - It may not be applicable to some resources that cannot be allocated non-preemptively, such as interrupts or communication channels .



# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Real-time systems are systems that have strict timing constraints and need to execute tasks with different priorities in a predictable and efficient manner.
- Resource access control is the problem of ensuring that tasks that share resources (such as semaphores, locks, or buffers) do not interfere with each other's deadlines or cause priority inversion.
- Priority inversion is a situation where a higher-priority task is blocked by a lower-priority task that holds a resource that the higher-priority task needs.
- Priority-inheritance protocol (PIP) is a method for eliminating unbounded priority inversion by temporarily raising the priority of a task that holds a resource to the maximum priority of any other task waiting for that resource.
- Priority-ceiling protocol (PCP) is a method for minimizing the blocking time of a task to at most the duration of a single critical section of a lower-priority task by assigning a ceiling priority to each resource and preventing a task from accessing a resource if its priority is lower than the ceiling priority of any resource currently held by another task.
- The differences between PIP and PCP are:
  - PIP is greedy, while PCP is not. PIP allows a task to access a resource whenever the resource is free, while PCP may withhold access to a free resource if the task's priority is lower than the ceiling priority of any resource held by another task.
  - PIP may cause transitive blocking, while PCP does not. Transitive blocking is a situation where a task is blocked by another task that is blocked by a third task that holds a resource. PCP avoids this by preventing a task from accessing a resource if its priority is lower than the ceiling priority of any resource held by another task.
  - PIP may cause chained blocking, while PCP does not. Chained blocking is a situation where a task is blocked by another task that holds multiple resources. PCP avoids this by preventing a task from accessing a resource if its priority is lower than the ceiling priority of any resource held by another task.
  - PIP may cause deadlock, while PCP does not. Deadlock is a situation where two or more tasks are waiting for each other to release resources that they hold. PCP avoids this by preventing a task from accessing a resource if its priority is lower than the ceiling priority of any resource held by another task.



# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule  .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time  .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, the job is blocked and its priority is raised to the ceiling priority of the resource  .
- SBPCP guarantees that a job can be blocked by at most one lower-priority job, and that the blocking time is bounded by the maximum execution time of the blocking job  .
- SBPCP also prevents deadlock by ensuring that a job can only request a resource if its priority is higher than the ceiling priority of any other resource that it holds  .
- SBPCP is an improvement over the Priority Inheritance Protocol (PIP), which only raises the priority of a job when it is blocked by a lower-priority job, and does not prevent deadlock .
- SBPCP is also an improvement over the Original Ceiling Priority Protocol (OCPP), which raises the priority of a job to the ceiling priority of the resource as soon as it requests the resource, even if the resource is available .
- SBPCP is similar to the Immediate Ceiling Priority Protocol (ICPP), which also raises the priority of a job to the ceiling priority of the resource when it requests the resource, but only if the resource is unavailable .
- SBPCP, OCPP, and ICPP have the same worst-case behavior from a scheduling point of view, but SBPCP and ICPP have better average-case behavior than OCPP, as they reduce the number of priority changes and context switches .



# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that can access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no deadlock can occur.
- For example, consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in deadline driven system as below :

| Time | T1 | T2 | Resource X | Resource Y | System Ceiling |
|------|----|----|------------|------------|----------------|
| 0    | 1  | 2  | -          | -          | -              |
| 1    | 1  | 2  | T1         | -          | 1              |
| 2    | 1  | 2  | T1         | -          | 1              |
| 3    | 1  | 2  | T1         | -          | 1              |
| 4    | 2  | 1  | T1         | -          | 2              |
| 5    | 2  | 1  | -          | T2         | 2              |
| 6    | 2  | 1  | -          | T2         | 2              |
| 7    | 2  | 1  | -          | T2         | 2              |
| 8    | 2  | 1  | -          | T2         | 2              |
| 9    | 2  | 1  | -          | -          | -              |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The priority ceiling of Y is 2 from time 0 to 5 and becomes 1 from time 5 to 6 and so on .
- The system ceiling is updated accordingly whenever a resource is locked or released .
- T1 can lock X at time 1 because its priority is higher than the system ceiling .
- T2 can lock Y at time 5 because its priority is higher than the system ceiling .
- T1 cannot lock Y at time 2 because its priority is lower than the system ceiling .
- T2 cannot lock X at time 6 because its priority is lower than the system ceiling .
- Both tasks can complete their execution without blocking or deadlock .



# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources in real-time systems to avoid unbounded priority inversion and mutual deadlock.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources that are held by other tasks, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the current ceiling of the system, which is the maximum of the ceilings of all the locked resources.
- A task that locks a resource inherits the ceiling of that resource, and cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that no deadlock can occur.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns the ceilings of the resources at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceilings of the resources at run time, based on the actual priorities of the tasks that request them.
- Dynamic preemption ceiling protocol has lower overhead and better response time than static preemption ceiling protocol, but it requires more storage and complexity.
- Preemption ceiling protocol can be extended to support object-oriented real-time systems, where the shared resources are encapsulated in objects and accessed by methods.
- Dual ceiling protocol is a variant of preemption ceiling protocol that allows a task to invoke a method of an object without locking it, if the method does not modify the object state.
- Dual ceiling protocol assigns two ceilings to each object: a normal ceiling and a preemption ceiling.
- The normal ceiling is the highest priority of any task that can invoke a modifying method of the object, and the preemption ceiling is the highest priority of any task that can invoke a non-modifying method of the object.
- A task can invoke a method of an object only if its priority is higher than the current normal ceiling of the system, and it inherits the normal ceiling or the preemption ceiling of the object, depending on the type of the method.
- Dual ceiling protocol reduces the blocking time and improves the schedulability of object-oriented real-time systems.



# Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to avoid deadlock and unbounded priority inversion, while ensuring schedulability and resource utilization.
- Some of the protocols for access control in multiple-unit resources are:
  - The Priority Inheritance Protocol (PIP): A job that locks a resource inherits the priority of the highest-priority job that is blocked on that resource. The priority is restored when the resource is unlocked  .
  - The Priority Ceiling Protocol (PCP): Each resource is assigned a priority ceiling, which is the highest priority of any job that can lock that resource. A job can lock a resource only if its priority is higher than the priority ceilings of all locked resources. A job that locks a resource inherits the priority ceiling of that resource. The priority is restored when the resource is unlocked  .
  - The Stack Resource Policy (SRP): Each job is assigned a preemption level, which is fixed and independent of its priority. A job can lock a resource only if its preemption level is higher than the preemption levels of all jobs that have locked any resource. A job that locks a resource inherits the preemption level of the lowest-level job that has locked any resource. The preemption level is restored when the resource is unlocked .
  - The Multiprocessor Priority Ceiling Protocol (MPCP): A variant of PCP for multiprocessor systems, where each resource is assigned to a processor and can be locked by jobs running on that processor. A job can lock a resource only if its priority is higher than the priority ceilings of all locked resources on the same processor. A job that locks a resource inherits the priority ceiling of that resource. The priority is restored when the resource is unlocked .
  - The Multiprocessor Stack Resource Policy (MSRP): A variant of SRP for multiprocessor systems, where each resource is assigned to a processor and can be locked by jobs running on that processor. A job can lock a resource only if its preemption level is higher than the preemption levels of all jobs that have locked any resource on the same processor. A job that locks a resource inherits the preemption level of the lowest-level job that has locked any resource on the same processor. The preemption level is restored when the resource is unlocked .



# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information in a real-time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause data inconsistency or violation of timing constraints.
- To ensure data integrity and timeliness, it is common to require that reads and writes be serializable, meaning that the effect of concurrent accesses is equivalent to some sequential execution of the accesses.
- Concurrency control is the technique that manages concurrent accesses to data objects by transactions, which are units of work that access and update data objects.
- Concurrency control in real-time systems should consider both data consistency and timing constraints, as well as the dynamic nature of the operating environment and the criticality of the transactions.
- There are different types of concurrency control protocols, such as locking-based, timestamp-based, validation-based, and optimistic protocols, that use different mechanisms to coordinate concurrent accesses and resolve conflicts.
- Locking-based protocols use locks to grant exclusive access to data objects to one transaction at a time. Locks can be acquired and released at different levels of granularity, such as object-level, method-level, or attribute-level.
- Locking-based protocols can cause blocking, priority inversion, deadlock, or convoying problems, which can affect the timeliness and schedulability of transactions. To overcome these problems, various priority-based locking protocols have been proposed, such as priority ceiling protocol, immediate priority ceiling protocol, highest locker protocol, and convex ceiling protocol.
- Timestamp-based protocols assign timestamps to transactions and data objects to determine the order of accesses and detect conflicts. Timestamps can be based on logical clocks, physical clocks, or deadlines. Timestamp-based protocols can cause abortion, restart, or starvation problems, which can affect the timeliness and schedulability of transactions. To overcome these problems, various priority-based timestamp protocols have been proposed, such as earliest deadline first timestamp protocol, earliest deadline first with restart protocol, and earliest deadline first with compensation protocol.
- Validation-based protocols allow transactions to access data objects without locking, but validate their serializability before committing. Validation can be done at different phases of the transaction, such as before execution, during execution, or after execution. Validation-based protocols can cause abortion, restart, or starvation problems, which can affect the timeliness and schedulability of transactions. To overcome these problems, various priority-based validation protocols have been proposed, such as priority validation protocol, priority validation with restart protocol, and priority validation with compensation protocol.
- Optimistic protocols assume that conflicts are rare and allow transactions to access data objects without locking or validation, but check their serializability at commit time. If a conflict is detected, the transaction is aborted and restarted. Optimistic protocols can cause abortion, restart, or starvation problems, which can affect the timeliness and schedulability of transactions. To overcome these problems, various priority-based optimistic protocols have been proposed, such as priority optimistic protocol, priority optimistic with restart protocol, and priority optimistic with compensation protocol.
- Concurrency control protocols can also be classified as static or dynamic, depending on whether they use fixed or variable priority assignments for transactions. Static protocols are simpler and faster, but less flexible and adaptable. Dynamic protocols are more complex and slower, but more flexible and adaptable.
- Concurrency control protocols can also be classified as centralized or distributed, depending on whether they use a single or multiple coordinators to manage concurrent accesses. Centralized protocols are easier to implement and maintain, but less scalable and fault-tolerant. Distributed protocols are harder to implement and maintain, but more scalable and fault-tolerant.
- Concurrency control protocols can also be classified as pessimistic or optimistic, depending on whether they prevent or allow conflicts to occur. Pessimistic protocols are more conservative and safe, but less efficient and responsive. Optimistic protocols are more aggressive and risky, but more efficient and responsive.
- Concurrency control protocols can also be classified as blocking or non-blocking, depending on whether they suspend or abort transactions when conflicts occur. Blocking protocols are more stable and fair, but less timely and schedulable. Non-blocking protocols are more timely and schedulable, but less stable and fair.
- Concurrency control protocols can also be classified as strict or non-strict, depending on whether they allow or forbid cascading aborts. Cascading aborts occur when a transaction aborts and causes other transactions that have read its data to abort as well. Strict protocols are more consistent and recoverable, but less concurrent and available. Non-strict protocols are more concurrent and available, but less consistent and recoverable.
- Concurrency control protocols can also be classified



## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information between two or more parties without significant delay.
- RTC can be synchronous or asynchronous, depending on whether the parties are communicating at the same time or not.
- RTC can be text-based, voice-based, video-based, or a combination of these modalities.
- RTC can be one-to-one, one-to-many, or many-to-many, depending on the number of participants and the direction of communication.
- RTC can be facilitated by various technologies, such as:
  - Internet Protocol (IP) telephony, which uses the internet to transmit voice and video signals over a network.
  - Instant messaging (IM), which allows users to send and receive text messages in real time.
  - Chat rooms, which are online spaces where multiple users can communicate simultaneously via text, voice, or video.
  - Social media, which are online platforms that enable users to create and share content and interact with others.
  - Web conferencing, which is a form of online meeting that allows users to collaborate and share presentations, documents, and applications in real time.
  - Streaming media, which is the delivery of audio and video content over the internet in a continuous flow.
- RTC has various benefits and challenges, such as:
  - Benefits:
    - It can enhance collaboration and productivity among remote teams and individuals.
    - It can reduce travel costs and time for meetings and events.
    - It can provide immediate feedback and support for customers and clients.
    - It can create a sense of presence and social connection among participants.
  - Challenges:
    - It can require high bandwidth and reliable network connections to ensure quality and security of communication.
    - It can pose technical and compatibility issues among different devices and platforms.
    - It can cause distraction and interruption from other tasks and activities.
    - It can raise ethical and legal concerns regarding privacy, consent, and data protection.



# Basic Concepts in Real Time Communication

- Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays .
- In RTC, there is always a direct path between the source and the destination.
- RTC is synonymous with live communication.
- RTC is dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.
- RTC is necessary to support real time guarantees of real time computing, which is a type of computing that requires a system to respond to events within a specified time frame.
- Examples of RTC include voice over landlines and mobile phones, video conferencing, instant messaging, online gaming, live streaming, and telemedicine .
- RTC can be implemented using various protocols and technologies, such as Session Initiation Protocol (SIP), Web Real-Time Communication (WebRTC), Real-time Transport Protocol (RTP), Real-time Streaming Protocol (RTSP), and Real-time Messaging Protocol (RTMP).
- RTC can offer various benefits, such as improved collaboration, productivity, customer service, and user experience .
- RTC can also pose various challenges, such as security, privacy, interoperability, scalability, and quality of service (QoS) .



# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities with strict timing constraints.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- A hard real-time communication system is one that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable losses  . For example, a communication system for a nuclear power plant or an aircraft control system is a hard real-time communication system.
- A soft real-time communication system is one that can tolerate some deadline misses, without causing severe damage or degradation of performance  . For example, a communication system for a video conference or a multimedia streaming service is a soft real-time communication system.
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic. This means that hard real-time communication systems can guarantee the worst-case execution time and response time, while soft real-time communication systems can only provide statistical guarantees or average values.
- Hard real-time communication systems require more stringent design and verification methods, such as formal methods, model checking, or schedulability analysis . Soft real-time communication systems can use more flexible and adaptive techniques, such as feedback control, quality of service, or resource reservation .
- Hard real-time communication systems are often implemented using specialized hardware and software platforms, such as real-time operating systems, real-time networks, or real-time middleware . Soft real-time communication systems can use more general-purpose or standard platforms, such as Linux, TCP/IP, or HTTP .
- Hard real-time communication systems are more expensive and complex to develop and maintain, but they offer higher reliability and safety  . Soft real-time communication systems are more affordable and scalable, but they may suffer from occasional delays or quality degradation  .



# Model of Real Time Communication

- Real time communication (RTC) is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- RTC can include voice, video, text, and data transmission over landlines, mobile phones, VoIP, or other internet-based platforms .
- RTC is important for applications that require timely and accurate delivery of information, such as online gaming, telemedicine, e-learning, video conferencing, etc .
- RTC can be modeled as a network of sources, destinations, hosts, and network interfaces that generate, transmit, and receive messages.
- A message is a stream of data that is sent from a source to a destination on a continuous basis.
- A message can be characterized by a tuple of inter-packet spacing (Pi), message length (ei), and reception deadline (Di), where Pi is the time interval between two consecutive packets of the same message, ei is the number of bits in a packet, and Di is the maximum allowable delay for a packet to reach its destination.
- This traffic model is called the peak rate model in RTC.
- The performance of RTC can be measured by metrics such as throughput, delay, and jitter.
- Throughput is the rate of successful message delivery over a communication channel.
- Delay is the time taken for a message to travel from the source to the destination.
- Jitter is the variation in delay among different packets of the same message.
- The goal of RTC is to maximize throughput, minimize delay, and reduce jitter.
- RTC can be achieved by using various techniques such as buffering, scheduling, routing, congestion control, error control, etc  .
- Buffering is the process of temporarily storing packets in a queue before sending or receiving them.
- Scheduling is the process of deciding the order and timing of packet transmission or reception.
- Routing is the process of finding the best path for a packet to travel from the source to the destination.
- Congestion control is the process of avoiding or reducing network congestion by regulating the traffic flow.
- Error control is the process of detecting and correcting errors in packet transmission or reception.



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns different weights to different priority classes and serves packets in a circular order based on their weights.
- WRR does not require a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of scheduling.
- WRR can guarantee both bandwidth and fairness requirements for different priority classes, but it may not satisfy the delay and jitter requirements for real-time communication.
- A variation of WRR is the rate-controlled frame-based WRR (RFWRR), which divides the scheduler into two components: a rate controller and a frame-based WRR server.
- The rate controller adjusts the weights of the priority classes based on their delay requirements and the network conditions, while the frame-based WRR server serves packets within a fixed frame size.
- RFWRR can guarantee the delay jitter bound and satisfy a diverse set of delay requirements for different priority classes, while maintaining the bandwidth and fairness properties of WRR.
- Another variation of WRR is the class-based WRR (CBWRR), which uses a hierarchical structure of priority classes and sub-classes, and applies WRR at each level.
- CBWRR can provide finer granularity and flexibility for differentiating the service quality of different priority classes and sub-classes, while preserving the bandwidth and fairness properties of WRR.
- Priority-based service disciplines, such as WRR and its variations, are suitable for switched networks that need to support real-time communication with different quality of service requirements .



# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols are mechanisms that allow several users or transmitters to access a common medium or channel.
- MAC protocols play an important role in the development of both wired and wireless networks, especially in broadcast networks where a single transmission can reach multiple receivers .
- MAC protocols can be classified into two main categories: random access and scheduling .
- Random access protocols allow users to transmit whenever they have data to send, without any coordination with other users. However, this may result in collisions, where two or more users transmit at the same time and interfere with each other. To avoid or resolve collisions, random access protocols use techniques such as carrier sensing, backoff, and acknowledgment.
- Scheduling protocols assign transmission opportunities to users based on some criteria, such as priority, demand, or fairness. Scheduling protocols can avoid collisions and guarantee certain quality of service (QoS) requirements, such as delay, throughput, or reliability. However, scheduling protocols may incur more overhead and complexity than random access protocols.
- Some examples of random access protocols are: 
  - Carrier sense multiple access with collision detection (CSMA/CD), which is used in Ethernet networks. CSMA/CD requires users to sense the channel before transmitting and to abort transmission if a collision is detected.
  - Carrier sense multiple access with collision avoidance (CSMA/CA), which is used in wireless networks such as IEEE 802.11 (Wi-Fi). CSMA/CA requires users to wait for a random backoff time before transmitting and to use acknowledgment frames to confirm successful reception.
  - Slotted ALOHA, which is a simple random access protocol that divides time into slots and allows users to transmit in any slot with a certain probability. Slotted ALOHA does not use carrier sensing or collision detection, but relies on feedback from the receiver to retransmit lost packets.
- Some examples of scheduling protocols are: 
  - Time division multiple access (TDMA), which allocates a fixed time slot to each user in a round-robin fashion. TDMA can avoid collisions and provide equal access to all users, but it may waste bandwidth if some users have no data to send in their slots.
  - Frequency division multiple access (FDMA), which assigns a fixed frequency band to each user. FDMA can also avoid collisions and provide equal access to all users, but it may suffer from interference and frequency reuse issues.
  - Code division multiple access (CDMA), which allows users to transmit simultaneously using different codes that are orthogonal to each other. CDMA can achieve high spectral efficiency and robustness to interference, but it requires complex encoding and decoding schemes and power control mechanisms.
- For real-time communication, MAC protocols need to consider the timing constraints and QoS requirements of the data streams, such as deadlines, jitter, and reliability.
- Some MAC protocols that are designed for real-time communication are: 
  - An adaptive MAC protocol for reliable broadcast in wireless networks (ABROAD), which adapts the transmission rate and the number of retransmissions according to the channel conditions and the packet deadlines. ABROAD can achieve high reliability and low delay for broadcast packets in wireless networks.
  - A real-time MAC protocol for wireless sensor networks (RTMAC), which uses a hybrid approach of TDMA and CSMA/CA to support both periodic and sporadic data streams. RTMAC can guarantee the deadlines of periodic data streams and provide fair access to sporadic data streams in wireless sensor networks.
  - A real-time MAC protocol for wireless body area networks (RT-WBAN), which uses a dynamic TDMA scheme to allocate slots to nodes based on their priority and traffic load. RT-WBAN can provide QoS differentiation and energy efficiency for various biomedical applications in wireless body area networks.



# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses soft state approach, which means that the reservations are periodically refreshed and can be easily modified or deleted.
- RSVP supports both Integrated Services (IntServ) and Differentiated Services (DiffServ) models of QoS.
- IntServ uses RSVP to explicitly signal the QoS needs of an application's traffic along the devices in the end-to-end path through the network.
- DiffServ uses RSVP to aggregate the QoS requirements of multiple flows into a single reservation and mark the packets with different priorities.
- RSVP messages include PATH, RESV, PATHERR, RESVERR, PATHTEAR, and RESVTEAR.
- PATH messages are sent by the sender to establish the route and QoS parameters for the data flow.
- RESV messages are sent by the receiver to request a reservation along the path established by the PATH messages.
- PATHERR and RESVERR messages are sent by the intermediate nodes to report errors or failures in the reservation process.
- PATHTEAR and RESVTEAR messages are sent by the sender or the receiver to tear down the reservation and release the resources.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver.
- RSVP is useful for applications that require timely but not necessarily reliable data delivery, such as videoconferencing, IP telephony, and other forms of multimedia communications.



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can process data and events that have critically defined time constraints.
- An RTOS is different from a general-purpose operating system, such as Windows or Linux, which is designed for multitasking and user interaction, not for meeting strict deadlines.
- An RTOS typically has features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS can be used for applications that require high reliability, predictability, and responsiveness, such as industrial control, flight control, and embedded systems.
- A real-time database system (RTDBS) is a database system that can handle transactions with real-time constraints, such as deadlines, priorities, and temporal consistency.
- An RTDBS is different from a conventional database system, such as Oracle or MySQL, which is designed for batch processing and data analysis, not for meeting strict performance guarantees.
- An RTDBS typically has features such as concurrency control, scheduling, recovery, and replication.
- An RTDBS can be used for applications that require timely and accurate data access, such as online reservation, stock trading, and sensor networks.
- A real-time database system can be based on SQL or NoSQL, depending on the data model and query language.
- A time-series database is a special type of real-time database system that can store and analyze data that changes over time, such as temperature, pressure, or stock prices.
- A time-series database typically has features such as compression, aggregation, and interpolation.
- A time-series database can be used for applications that require fast and efficient data processing, such as monitoring, forecasting, and anomaly detection.



# Features of RTOS

A real-time operating system (RTOS) is an operating system that guarantees to meet the deadlines of time-critical tasks, such as controlling a robot arm, a pacemaker, or a missile guidance system. An RTOS has two key features: predictability and determinism.

Some of the features of an RTOS are:

- **Small size**: An RTOS is designed to occupy very less memory and consume fewer resources than a general-purpose operating system. This is because an RTOS is often used in embedded systems with limited hardware capabilities.
- **Fast response**: An RTOS is able to execute tasks quickly and efficiently, without unnecessary delays or overheads. An RTOS can switch between tasks in microseconds, while a general-purpose operating system may take milliseconds or more.
- **Reliability**: An RTOS is expected to respond as expected every time, without missing any deadlines or causing any errors. An RTOS is tested and verified to ensure that it can handle all possible scenarios and exceptions.
- **Scheduling algorithm**: An RTOS uses a scheduling algorithm that prioritizes the tasks based on their deadlines, importance, or other criteria. An RTOS can use either a co-operative scheduling or a pre-emptive scheduling algorithm. In co-operative scheduling, the tasks voluntarily yield the CPU to other tasks when they are done or when they need to wait for some event. In pre-emptive scheduling, the RTOS can interrupt a running task and switch to a higher-priority task at any time .
- **Concurrency control**: An RTOS supports concurrency control mechanisms that allow multiple tasks to access shared resources, such as memory, files, or devices, without causing conflicts or inconsistencies. An RTOS can use semaphores, mutexes, message queues, or other techniques to synchronize and communicate between tasks .
- **Real-time features**: An RTOS provides real-time features that enable the tasks to interact with the external environment, such as sensors, actuators, or networks, in a timely and accurate manner. An RTOS can support features such as timers, interrupts, signals, events, or real-time clocks, that allow the tasks to perform time-sensitive operations or react to external stimuli .



# Time Services

Time services are the mechanisms that provide the functionality of time measurement, synchronization, and scheduling in real-time systems. Time services are essential for ensuring the timeliness and correctness of real-time applications that have strict deadlines and constraints. Some of the topics related to time services are:

- **Time measurement**: Time measurement is the process of determining the current time or the elapsed time between two events. Time measurement can be done using hardware devices such as clocks, timers, and counters, or software methods such as system calls, interrupts, and timestamps. Time measurement can be affected by factors such as clock drift, resolution, accuracy, and precision. Time measurement can be used for performance analysis, debugging, logging, and monitoring of real-time systems.

- **Time synchronization**: Time synchronization is the process of aligning the clocks of multiple devices or processes that operate in a distributed or parallel manner. Time synchronization can be achieved using hardware methods such as wired or wireless communication, or software methods such as message passing, consensus algorithms, or clock synchronization protocols. Time synchronization can be classified into internal synchronization, which is the synchronization of clocks within a single device or system, and external synchronization, which is the synchronization of clocks across different devices or systems. Time synchronization can be used for coordination, consistency, and fault tolerance of real-time systems.

- **Time scheduling**: Time scheduling is the process of allocating the resources and tasks of a real-time system according to their priorities, deadlines, and dependencies. Time scheduling can be done using hardware methods such as preemptive or non-preemptive interrupts, or software methods such as scheduling algorithms, policies, or models. Time scheduling can be classified into static scheduling, which is the scheduling of tasks before the system execution, and dynamic scheduling, which is the scheduling of tasks during the system execution. Time scheduling can be used for optimizing the utilization, throughput, and responsiveness of real-time systems.



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- Processing time requirements need to be fully understood and bound rather than just kept as a minimum.
- Unix is not a RTOS by default, but it can be modified or extended to provide some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running process and switch to a higher priority one.
  - Real-time signals: the ability to deliver signals to processes without blocking or delaying them.
  - High-resolution timers: the ability to measure and control time with nanosecond precision.
  - Memory locking: the ability to prevent memory pages from being swapped out to disk.
  - Priority inheritance: the ability to avoid priority inversion, a situation where a low-priority process holds a resource needed by a high-priority process.
- Some examples of Unix variants or extensions that provide real-time features are:
  - RTLinux: a hard real-time extension for Linux that runs the Linux kernel as a low-priority process on top of a small real-time core.
  - Xenomai: a dual-kernel RTOS that coexists with the Linux kernel and provides a POSIX-compliant interface for real-time applications.
  - QNX: a microkernel-based RTOS that supports POSIX and Unix standards and provides a distributed architecture for embedded systems.
  - Solaris: a Unix-based OS that supports real-time scheduling, memory locking, and high-resolution timers.
  - VxWorks: a proprietary RTOS that supports POSIX and Unix standards and provides a modular and scalable architecture for embedded systems.



# POSIX Issues

- POSIX stands for Portable Operating System Interface, which is a set of standards that define how an application should interact with an operating system.
- POSIX aims to achieve portability, interoperability, and compatibility among different operating systems, especially UNIX and its variants.
- POSIX also covers extensions for real-time operating systems, which are systems that have strict timing constraints and need to respond to events within predictable and bounded time frames.
- POSIX real-time extensions include specifications for:
  - Scheduling policies and parameters, such as priority-based preemptive scheduling and deadline scheduling.
  - Timers and clocks, such as high-resolution timers and monotonic clocks.
  - Synchronization primitives, such as mutexes, condition variables, semaphores, and barriers.
  - Message passing and shared memory, such as message queues, memory mapping, and memory locking.
  - Signals and signal handling, such as real-time signals and signal masks.
  - Asynchronous and synchronous I/O, such as asynchronous notification, memory-mapped I/O, and scatter-gather I/O.
- POSIX real-time extensions aim to provide the necessary functionality and performance for real-time applications, such as embedded systems, robotics, multimedia, and control systems.
- However, POSIX real-time extensions also face some challenges and limitations, such as:
  - Implementation and conformance issues, such as the availability, completeness, and correctness of POSIX real-time features in different operating systems and platforms.
  - Compatibility and portability issues, such as the differences and conflicts among different versions and subsets of POSIX standards, and the trade-offs between adhering to the standards and exploiting the native features of the operating systems.
  - Performance and scalability issues, such as the overhead, latency, and variability of POSIX real-time services, and the impact of system load, contention, and interference on the real-time behavior of the applications.
  - Usability and flexibility issues, such as the complexity, verbosity, and rigidity of POSIX real-time interfaces, and the lack of support for dynamic adaptation, configuration, and optimization of the applications.



# Characteristic of Temporal Data

- Temporal data is the data that is **valid only for a prescribed time**. It becomes **invalid or obsolete** after a certain period of time .
- Temporal data can represent **time in some form**, such as dates, timestamps, intervals, durations, or periods. It can also allow other data to be **placed in a chronological sequence** or to be **analyzed chronologically**.
- Temporal data can have different **temporal aspects**, such as valid time, transaction time, or decision time. Valid time is the time period during or event time at which a fact is true in the real world. Transaction time is the time period during which a fact is stored in the database. Decision time is the time period during which a fact is considered for decision making.
- Temporal data can be stored and managed in **temporal databases**, which are databases that support temporal data types, operations, and queries. Temporal databases can be uni-temporal, bi-temporal, or tri-temporal, depending on how many temporal aspects they capture.
- Temporal data can be used for various purposes, such as **analyzing weather patterns** and other environmental variables, **monitoring traffic conditions**, **studying demographic trends**, and so on.



# Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most accurate and up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not represent the current state of the physical environment. Data staleness can be caused by delays in data acquisition, data transmission, data processing, or data storage.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other or with the physical environment. Data inconsistency can be caused by concurrent updates, data replication, data partitioning, or data corruption.
- Temporal consistency can be maintained by using various techniques, such as triggered updates, temporal validity, temporal constraints, temporal locking, temporal serialization, temporal freshness, or temporal coherency  .
  - Triggered updates are a technique that updates the data stored in the database whenever there is a significant change in the physical environment. Triggered updates can reduce data staleness and improve temporal consistency, but they can also increase the workload and the communication overhead of the system.
  - Temporal validity is a technique that assigns a validity interval to each data item stored in the database, indicating how long the data item is expected to be valid. Temporal validity can help to detect and avoid data staleness, but it can also introduce additional storage and computation costs for maintaining and checking the validity intervals.
  - Temporal constraints are a technique that specifies the temporal requirements of the transactions that access the data stored in the database, such as deadlines, periods, or freshness bounds. Temporal constraints can help to schedule and execute the transactions in a way that preserves temporal consistency, but they can also impose restrictions and trade-offs on the system performance and functionality.
  - Temporal locking is a technique that prevents concurrent transactions from accessing or updating the same data item stored in the database, if doing so would violate temporal consistency. Temporal locking can help to avoid data inconsistency and ensure temporal serialization, but it can also cause blocking, deadlock, or starvation of the transactions.
  - Temporal serialization is a technique that ensures that the execution order of the transactions that access or update the data stored in the database is consistent with the temporal order of the events that occur in the physical environment. Temporal serialization can help to maintain temporal consistency and avoid data inconsistency, but it can also limit the concurrency and parallelism of the transactions.
  - Temporal freshness is a technique that measures the degree of staleness of the data stored in the database, based on the difference between the current time and the last update time of the data item. Temporal freshness can help to quantify and control the quality of the data and the temporal consistency of the system, but it can also depend on the accuracy and synchronization of the clocks in the system.
  - Temporal coherency is a technique that ensures that the data stored in the database is consistent across different replicas, partitions, or nodes of the system, if the system is distributed or decentralized. Temporal coherency can help to improve the availability and reliability of the data and the system, but it can also introduce additional communication and coordination costs for maintaining and enforcing the coherency.



# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control techniques prevent conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and priority inheritance protocols.
  - Optimistic concurrency control techniques allow conflicts to occur and then resolve them by aborting or restarting the conflicting transactions. Examples of optimistic techniques are optimistic concurrency control, multiversion concurrency control, and wait-free synchronization.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as the performance criteria, the transaction model, the scheduling policy, the failure handling, and the correctness criteria.
  - Performance criteria: RTS are concerned with meeting deadlines and minimizing response time, while database systems are concerned with maximizing throughput and minimizing blocking time.
  - Transaction model: RTS transactions are often periodic, preemptive, and have different types of operations (such as read, write, and control), while database transactions are often sporadic, non-preemptive, and have only read and write operations.
  - Scheduling policy: RTS transactions are often scheduled by fixed or dynamic priority algorithms, while database transactions are often scheduled by first-come-first-served or round-robin algorithms.
  - Failure handling: RTS transactions are often required to complete within a deadline, and aborting or restarting them may not be feasible or desirable, while database transactions can be aborted or restarted without affecting the system functionality.
  - Correctness criteria: RTS transactions are required to satisfy both logical and temporal correctness, while database transactions are required to satisfy only logical correctness.
- Logical correctness of RTS transactions is usually defined by serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.
- Temporal correctness of RTS transactions is usually defined by timeliness, which means that the transactions meet their deadlines and do not cause deadline misses of other transactions.
- There are different types of serializability and timeliness criteria for RTS transactions, depending on the assumptions and goals of different classes of RTS.
  - Serializability criteria: linearizability, sequential consistency, causal consistency, and eventual consistency.
  - Timeliness criteria: hard, firm, and soft deadlines.



# Overview of Commercial Real Time Databases

- A real time database is a database system that uses real time processing to handle workloads whose state is constantly changing.
- Real time databases are useful for applications that require timely and consistent responses, such as accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real time databases can be classified into two types: hard real time and soft real time.
  - Hard real time databases guarantee that transactions meet their deadlines, otherwise the system may fail. They are suitable for critical systems, such as air traffic control, nuclear power plants, and military systems.
  - Soft real time databases allow some transactions to miss their deadlines, but try to minimize the number and severity of such violations. They are suitable for non-critical systems, such as online gaming, e-commerce, and social media.
- Some of the attributes of live real time databases are:
  - Concurrency control: The ability to handle multiple transactions accessing the same data without compromising data integrity or performance.
  - Data freshness: The degree to which the data reflects the current state of the real world.
  - Data distribution: The ability to store and access data across multiple nodes or locations for scalability, availability, and fault tolerance.
  - Data replication: The ability to create and maintain copies of data for backup, load balancing, or data locality.
  - Data consistency: The degree to which the data is coherent and accurate across all nodes or copies.
  - Data durability: The ability to preserve data in the event of system failures or crashes.
  - Data security: The ability to protect data from unauthorized access, modification, or deletion.
  - Data recovery: The ability to restore data to a previous or desired state after a failure or error.
  - Data analysis: The ability to perform queries, reports, or analytics on the data to derive insights or support decision making.
- Some of the examples of commercial real time databases are:
  - Google Cloud Firestore: A scalable, serverless, NoSQL document database for web, mobile, and IoT applications. It offers real time synchronization, offline support, and ACID transactions.
  - Google Cloud Bigtable: A highly performant, fully managed NoSQL database service for large analytical and operational workloads. It offers high availability, low latency, and strong consistency.
  - Google Cloud Spanner: A fully managed, relational database service that combines the benefits of SQL and NoSQL databases. It offers global scalability, strong consistency, and high availability.
  - Google Cloud SQL: A fully managed, relational database service that supports MySQL, PostgreSQL, and SQL Server. It offers high performance, security, and reliability.
  - Google Cloud Memorystore: A fully managed, in-memory data store service that supports Redis and Memcached. It offers low latency, high throughput, and scalability.

