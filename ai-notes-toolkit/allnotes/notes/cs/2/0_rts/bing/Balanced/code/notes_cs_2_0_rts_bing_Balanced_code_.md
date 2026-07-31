

# Real Time System

A real time system is a system that can process and respond to events within a specific and predictable time frame. A real time system must meet its deadlines, otherwise it may cause a system failure or undesirable consequences. A real time system is often used to control or interact with an environment that changes dynamically and requires timely responses.

Some examples of real time systems are:

- Process control systems: These systems are used to monitor and regulate industrial processes, such as chemical plants, power plants, oil refineries, etc. They use sensors, actuators, and controllers to maintain the desired state of the system and prevent accidents or malfunctions.
- Machine vision: These systems are used to help machines interpret visual data, such as images, videos, or 3D scans. They can be used for various purposes, such as face recognition, object detection, quality inspection, navigation, etc. They require high-speed processing and low-latency communication to perform their tasks effectively.
- Robotics: These systems are used to control robots that can perform various actions, such as manipulation, locomotion, exploration, etc. They use sensors, motors, and algorithms to coordinate the movements and behaviors of the robots and adapt to the environment and the goals.
- Flight control: These systems are used to control the flight of aircraft, such as airplanes, helicopters, drones, etc. They use sensors, actuators, and computers to stabilize the flight, follow the flight plan, avoid collisions, and handle emergencies.

There are two types of real time systems based on their timing constraints:

- Hard real time system: This type of system has absolute deadlines, and if those deadlines are missed, the system will fail or cause severe damage. For example, a flight control system must respond to the pilot's commands or the sensor inputs within milliseconds, otherwise the aircraft may crash.
- Soft real time system: This type of system has relative deadlines, and if those deadlines are missed, the system will degrade its performance or quality of service, but not fail completely. For example, a video streaming system must deliver the video frames within a certain time, otherwise the video quality will be reduced or the frames will be skipped.

Some characteristics of real time systems are:

- Concurrency: A real time system may have multiple tasks or processes that run simultaneously and share resources, such as CPU, memory, or I/O devices. The system must manage the concurrency and ensure that the tasks are executed in the correct order and without conflicts or deadlocks.
- Scheduling: A real time system must allocate the CPU time to the tasks according to their priorities and deadlines. The system must use a scheduling algorithm that can guarantee the timeliness and fairness of the tasks and handle the dynamic changes in the system load and the task arrival.
- Synchronization: A real time system must synchronize the clocks and the events of the system components, such as the sensors, the actuators, and the controllers. The system must use a synchronization protocol that can ensure the accuracy and consistency of the system state and the data exchange.
- Reliability: A real time system must be able to handle faults and errors that may occur in the system components or the environment. The system must use fault-tolerance techniques that can detect, isolate, and recover from the faults and maintain the system functionality and safety.



## Unit 1 - Introduction of Real Time System

A real time system is a system that can process data and events within a specified time constraint. The system must produce the expected result within a defined deadline, otherwise it may cause a system failure or undesirable consequences. A real time system may also need to coordinate with other systems or devices that operate with different clocks and synchronize their actions.

Some examples of real time systems are:

- Flight control systems
- Real time monitors
- Industrial control systems
- Telecommunication systems
- Multimedia systems
- Embedded systems

Real time systems can be classified into two types based on their timing constraints:

- Hard real time systems: These systems have absolute deadlines that must be met, otherwise the system may fail or cause severe damage. For example, a flight control system must respond to the pilot's commands within milliseconds, otherwise the plane may crash.
- Soft real time systems: These systems have relative deadlines that can be missed occasionally, but the system performance may degrade or the quality of service may be reduced. For example, a video streaming system may drop some frames or reduce the resolution if the network bandwidth is low, but the user can still watch the video.

Real time systems require a special type of operating system that can handle the timing requirements and the concurrency issues of the system. A real time operating system (RTOS) is an operating system that can provide predictable and deterministic response times to the system events and tasks. An RTOS typically has the following features:

- Preemptive scheduling: The RTOS can interrupt a running task and switch to a higher priority task when an event occurs, without waiting for the current task to finish.
- Priority-based scheduling: The RTOS can assign different priorities to different tasks and execute them according to their importance and urgency.
- Inter-task communication and synchronization: The RTOS can provide mechanisms for the tasks to communicate and synchronize with each other, such as message queues, semaphores, mutexes, etc.
- Memory management: The RTOS can allocate and deallocate memory for the tasks and the system resources, and avoid memory fragmentation and leakage.
- Interrupt handling: The RTOS can handle the interrupts from the hardware devices and the software events, and dispatch them to the appropriate tasks or handlers.
- Device drivers: The RTOS can provide interfaces for the system to interact with the external devices, such as sensors, actuators, displays, etc.



### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can be characterized by four attributes: timeliness, concurrency, predictability, and dependability.
- Timeliness means that the system must deliver the correct results at the correct time, according to the deadlines and the temporal constraints of the application.
- Concurrency means that the system must handle multiple events or tasks simultaneously, without blocking or interfering with each other.
- Predictability means that the system must behave consistently and deterministically, without any unexpected delays or variations.
- Dependability means that the system must be reliable, available, safe, and secure, without any faults or errors.



### Typical Real Time Applications

A real-time application (RTA) is an application that has strict time constraints on its functionality and performance. RTAs must respond to events or inputs within a predictable and specific time frame, otherwise they may fail or cause undesirable consequences. RTAs are often used in domains such as digital control, signal processing, command and control, multimedia, and real-time databases. Some examples of RTAs are:

- **Video conferencing**: This is an application that allows users to communicate with each other using audio and video streams over the Internet. Video conferencing requires high bandwidth, low latency, and synchronization of the streams to ensure a smooth and realistic interaction. Video conferencing also needs to handle packet loss, jitter, and network congestion gracefully.
- **Voice over Internet Protocol (VoIP)**: This is an application that enables users to make phone calls over the Internet using digital signals. VoIP requires low latency, high quality, and security of the voice data. VoIP also needs to deal with packet loss, jitter, and network congestion effectively.
- **Online gaming**: This is an application that allows users to play games with other users over the Internet. Online gaming requires fast and consistent response time, high frame rate, and synchronization of the game state among the players. Online gaming also needs to cope with packet loss, jitter, and network congestion efficiently.
- **Community storage applications**: These are applications that allow users to store and share data over the Internet using distributed storage systems. Community storage applications require high availability, reliability, and consistency of the data. Community storage applications also need to handle network failures, data replication, and load balancing intelligently.
- **Some e-commerce applications**: These are applications that allow users to buy and sell goods and services over the Internet using online platforms. Some e-commerce applications require real-time processing of transactions, inventory management, and payment verification. Some e-commerce applications also need to handle security, fraud detection, and customer service promptly.
- **Real-time operating system (RTOS)**: This is an operating system that supports the execution of RTAs by providing features such as preemptive scheduling, priority-based dispatching, inter-process communication, and real-time memory management. RTOS must ensure that the RTAs meet their deadlines, avoid resource conflicts, and handle errors and exceptions gracefully.
- **Instant messaging (IM) applications**: These are applications that allow users to send and receive text, voice, and video messages over the Internet. IM applications require low latency, high quality, and security of the messages. IM applications also need to deal with network failures, message delivery, and encryption effectively.
- **Team collaboration applications**: These are applications that allow users to work together on projects over the Internet using tools such as document editing, file sharing, and video conferencing. Team collaboration applications require high bandwidth, low latency, and synchronization of the data and activities among the users. Team collaboration applications also need to handle access control, version control, and conflict resolution efficiently.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System will be released on the course website on Monday, 20 March 2023 at 10:00 AM GMT.
- The notes will cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes will be in PDF format and will contain text, diagrams, tables, and examples.
- The notes will be accompanied by a set of self-assessment questions and answers to help you review the concepts and test your understanding.
- The notes are expected to take about two hours to read and comprehend.
- You are advised to read the notes carefully and make notes of your own to prepare for the quizzes and exams.
- You are also encouraged to participate in the online discussion forum and ask any doubts or clarifications you may have regarding the notes or the topics covered.
- The instructor will be available for online consultation on Wednesdays and Fridays from 2:00 PM to 4:00 PM GMT. You can also email the instructor at rts@university.edu with any queries or feedback.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by **Friday, 24 March 2023** before **5:00 PM**.
- The notes should be handwritten and scanned in PDF format.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be clear, concise, and accurate. They should include diagrams, tables, and examples wherever necessary.
- The notes should be uploaded on the online portal with the file name **RTS_Unit1_Name_RollNo.pdf**.
- The notes will be evaluated based on the following criteria:
  - Completeness and correctness of the content
  - Neatness and readability of the handwriting
  - Organization and presentation of the notes
  - Adherence to the format and deadline
- The notes will carry **10 marks** out of the total **100 marks** for the subject of Real Time System.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also on the result being obtained within the time constraint.
- Time constraints related with real-time systems mean that there is a time interval allotted for the response of the ongoing program. This deadline means that the task should be completed within this time interval.
- Real-time systems are responsible for the completion of all tasks within their time intervals.
- Timing constraints associated with the real-time system are classified to identify the different types of timing constraints in a real-time system. Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system are known as Reliability Constraints.
- Performance Constraints are further classified into three types:
  - Delay Constraint: A delay constraint describes the minimum time interval between the occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between the occurrence of two consecutive events.
  - Duration Constraint: A duration constraint describes the maximum or minimum time interval for which an event should occur or a condition should hold.
- Reliability Constraints are further classified into two types:
  - Synchronization Constraint: A synchronization constraint describes the temporal relationship between two or more events or conditions.
  - Ordering Constraint: An ordering constraint describes the precedence or succession relationship between two or more events or conditions.
- Timing constraints can be expressed using various constructs in requirements languages, such as temporal logic, interval logic, event calculus, etc.
- Timing constraints can be validated using automatic test systems that can measure the actual response time and behavior of the system and compare them with the expected values.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.



### Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- A hard real time system is also known as an immediate real time system .
- A hard real time system is usually found interacting at a low level with physical hardware, in embedded systems .
- Examples of hard real time systems are nuclear power plant control systems, air traffic control systems, pacemakers, automotive systems, etc.  .
- A hard real time system requires a real time operating system (RTOS) that can handle the scheduling, synchronization, communication, and fault tolerance of the system  .
- A hard real time system must have predictable and deterministic behavior, meaning that the system must always respond in the same way and within the same time frame for a given input .
- A hard real time system must also have high reliability and availability, meaning that the system must be able to function correctly and continuously under normal and abnormal conditions .
- A hard real time system must also have low latency and jitter, meaning that the system must have minimal delay and variation in the response time .
- A hard real time system must also have high throughput and efficiency, meaning that the system must be able to process a large amount of data and perform complex computations with minimal resources .



### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing a failure or a significant degradation of performance.  
- A soft real-time system has a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system. 
- A soft real-time system can be run on multiple cores and impose fewer restrictions on applications. 
- A soft real-time system is typically used for applications that have high throughput and quality of service requirements, but can tolerate occasional deadline misses.  
- Examples of soft real-time systems are multimedia streaming, video conferencing, online gaming, voice over IP, etc.



### Reference Models for Real Time Systems

A reference model is a canonical form that describes the essential features and properties of a system, without specifying the implementation details. A reference model can help us to reason about the system, to compare different systems, and to design new systems.

A reference model for real time systems consists of three main elements:

- A workload model that describes the applications supported by the system, such as the tasks, jobs, deadlines, resource dependencies, etc.
- A resource model that describes the resources available in the system, such as the CPU, memory, network, etc., and their types and relations.
- A system model that describes how the system manages the workload and the resources, such as the scheduling policies, the synchronization mechanisms, the fault tolerance techniques, etc.

One example of a reference model for real time systems is the Real-time Control System (RCS) architecture, which is suitable for many software-intensive, real-time computing control problem domains. The RCS architecture combines real-time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .

Some benefits of using a reference model for real time systems are:

- It provides a common terminology and framework for understanding and analyzing real time systems.
- It helps to identify the essential requirements and constraints of real time systems, and to evaluate their performance and correctness.
- It facilitates the reuse and adaptation of existing solutions and components for different real time systems.
- It supports the development and verification of new solutions and components for real time systems.



### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion.
- Examples of processors are computers, transmission links, disks, and database servers.
- Processors can be configured and optimized for real-time applications by using workload-aware tuning and optimizations that help bound data access timings.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs or allocated exclusively to one job.
- Examples of resources are memory, files, printers, and sensors.
- Resources can be managed by using different policies and protocols that ensure mutual exclusion, deadlock avoidance, and priority inheritance.
- Real-time systems need to coordinate the access and allocation of processors and resources among multiple jobs that have timing constraints and deadlines.
- Real-time operating systems (RTOS) are specialized operating systems that serve real-time applications that process data without any buffering delay .
- RTOS have features such as preemptive scheduling, fast context switching, interrupt handling, inter-task communication, and time synchronization .
- Examples of RTOS are FreeRTOS, VxWorks, QNX, and RTLinux.



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics.
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The time instant when the job becomes available for execution.
  - Absolute deadline (d<sub>i</sub>): The time instant by which the job must finish its execution.
  - Relative deadline (D<sub>i</sub>): The time interval between the release time and the absolute deadline of the job.
  - Feasible interval ([r<sub>i</sub>, d<sub>i</sub>]): The time interval during which the job can be executed.
- The temporal parameters of a job can be specified by the application or the system designer, or they can be derived from other parameters such as the period or the frequency of the job.
- The temporal parameters of a job can be used to determine the schedulability and the performance of the real time system.
- The temporal parameters of a job can be fixed or variable, depending on the nature of the application and the system. For example, a hard real time system may have fixed and known temporal parameters, while a soft real time system may have variable and uncertain temporal parameters.



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period. A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The periodic task model assumes that each task has a known and fixed period, execution time, and deadline, and that each task is released at the beginning of its period. The periodic task model also assumes that tasks are independent and preemptive, meaning that they do not share resources or communicate with each other, and that they can be interrupted and resumed by the scheduler.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period. The jitter can be used to model uncertainties in the task arrival times, such as delays in the sensors or the network.
- The periodic task model can be used to analyze the schedulability of a set of tasks, that is, whether the tasks can meet their deadlines under a given scheduling algorithm. The schedulability analysis can be done by using different methods, such as utilization-based tests, response-time analysis, or simulation. The schedulability analysis can help to design and optimize the real-time system, by choosing appropriate parameters for the tasks and the scheduler.



### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal order of the jobs, while data dependency is caused by the communication or sharing of data among the jobs.
- Precedence constraints can be represented by a directed graph, called a precedence graph, where the vertices are the jobs and the edges indicate the order of execution. For example, if job J1 must finish before job J2 can start, then there is an edge from J1 to J2 in the precedence graph  .
- Data dependency cannot be captured by a precedence graph, as it depends on the data values and the synchronization mechanisms used by the jobs. For example, if job J1 writes to a shared variable that is read by job J2, then J2 is data dependent on J1, but the precedence graph does not show this dependency .
- Precedence constraints and data dependency may affect the schedulability and feasibility of real time systems, as they limit the possible execution sequences and parallelism of the jobs. Therefore, they must be taken into account by the scheduling algorithms and the system design .



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or before the system starts running. It is based on the known characteristics of the tasks, such as their periods, execution times, deadlines, and priorities. Static scheduling is suitable for systems that have fixed and periodic tasks, and that do not require much flexibility or adaptability .
  - Dynamic scheduling is done at run time or during the system execution. It is based on the current state of the system, such as the availability of resources, the arrival of new tasks, the completion of existing tasks, and the occurrence of events. Dynamic scheduling is suitable for systems that have variable and aperiodic tasks, and that require more flexibility and adaptability .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running. The lower priority task resumes its execution when the higher priority task finishes or is blocked. Preemptive scheduling can reduce the response time and the deadline miss ratio of the tasks, but it can also introduce more overhead and complexity .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running. The higher priority task has to wait until the lower priority task finishes or is blocked. Non-preemptive scheduling can reduce the overhead and complexity of the system, but it can also increase the response time and the deadline miss ratio of the tasks .
- Real time scheduling algorithms are the rules or methods that determine which task to execute next in a real time system. There are many real time scheduling algorithms, such as rate monotonic, earliest deadline first, least laxity first, etc. Each algorithm has its own advantages and disadvantages, and its own applicability and suitability for different types of real time systems .
- Real time scheduling analysis is the process of evaluating and verifying the performance and correctness of a real time system and its scheduling algorithm. It can be done using mathematical models, simulation tools, or empirical methods. The main metrics or criteria for real time scheduling analysis are schedulability, feasibility, optimality, and robustness .



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution priorities and time slots to tasks or processes that have timing constraints. Real time systems are those whose correctness depends on both functionality and timing. There are different approaches to real time scheduling, depending on the characteristics and requirements of the system and the tasks. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, period, etc. are known at design time. The scheduler uses a precomputed table that specifies which task to execute at each time instant. The table is generated offline using static analysis and optimization techniques. The advantage of this approach is that it guarantees the schedulability of all the tasks and avoids runtime overhead. The disadvantage is that it is inflexible and cannot handle dynamic changes or uncertainties in the system.   

- **Round-robin approach**: This approach is a simple and fair technique that is commonly used in time-shared systems. It assigns a fixed time slice or quantum to each task in a circular order. The scheduler switches to the next task when the current task finishes its quantum or blocks for I/O. The advantage of this approach is that it is easy to implement and provides good response time for interactive tasks. The disadvantage is that it does not consider the timing constraints or the priorities of the tasks, and may cause deadline misses or starvation for some tasks.  

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach that assigns different weights or quanta to different tasks based on their importance or resource requirements. The scheduler allocates more time to the tasks with higher weights and less time to the tasks with lower weights. The advantage of this approach is that it can improve the performance and fairness of the system by giving more attention to the critical or demanding tasks. The disadvantage is that it still does not consider the timing constraints or the deadlines of the tasks, and may not be suitable for hard real time systems.  

- **Priority-driven approach**: This approach is the most widely used and flexible technique for real time scheduling. It assigns a priority to each task based on its timing constraints, such as deadline, period, urgency, etc. The scheduler always selects the task with the highest priority to execute, and preempts the current task if a higher priority task arrives. The advantage of this approach is that it can handle dynamic and unpredictable situations, and can achieve optimal or near-optimal schedulability for different classes of tasks. The disadvantage is that it may incur more runtime overhead and complexity, and may suffer from priority inversion or blocking problems.    

Some examples of priority-driven scheduling algorithms are:

- **Rate-monotonic scheduling (RMS)**: This algorithm assigns a fixed priority to each periodic task based on its period, such that the shorter the period, the higher the priority. It is optimal for preemptive scheduling of periodic tasks with implicit deadlines (equal to periods) on a single processor.   

- **Deadline-monotonic scheduling (DMS)**: This algorithm assigns a fixed priority to each periodic task based on its relative deadline, such that the shorter the deadline, the higher the priority. It is optimal for preemptive scheduling of periodic tasks with arbitrary deadlines on a single processor.   

- **Earliest deadline first (EDF)**: This algorithm assigns a dynamic priority to each task based on its absolute deadline, such that the closer the deadline, the higher the priority. It is optimal for preemptive scheduling of periodic or sporadic tasks with arbitrary deadlines on a single processor.   

- **Least slack time (LST)**: This algorithm assigns a dynamic priority to each task based on its slack time, which is the difference between its deadline and its remaining execution time. The smaller the slack time, the higher the priority. It is optimal for preemptive scheduling of periodic or sporadic tasks with arbitrary deadlines on a single processor.



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
    - It avoids run-time overheads such as context switching and priority management.
    - It can handle periodic, aperiodic and sporadic tasks with known parameters.
    - It can guarantee the deadlines of all the tasks if the schedule is feasible.
  - Disadvantages:
    - It is inflexible and cannot handle dynamic changes in the system such as task arrivals, failures or resource availability.
    - It requires a priori knowledge of all the task parameters and system states.
    - It may waste CPU time if the schedule is not fully utilized.
    - It may not be optimal in terms of performance metrics such as response time or throughput.

- Some examples of clock-driven scheduling algorithms are:

  - Cyclic executive: A simple algorithm that divides the schedule into fixed-length cycles and assigns tasks to slots within each cycle.
  - Time-driven table-driven scheduling: An algorithm that uses a table to store the schedule of tasks for each scheduling decision time.
  - Time-driven state-machine scheduling: An algorithm that uses a state machine to represent the schedule of tasks and transitions between states based on events or conditions.

- A graphical representation of clock-driven scheduling is shown below:

```
|<----------------- Hyperperiod ----------------->|
|<-- Cycle 1 -->|<-- Cycle 2 -->|<-- Cycle 3 -->|...
| T1 | T2 | T3 | T1 | T2 | T4 | T1 | T2 | T3 |...
```

- In this example, there are four tasks: T1, T2, T3 and T4. T1 and T2 are periodic tasks with periods of 3 and 6 units, respectively. T3 and T4 are aperiodic tasks with deadlines of 9 and 12 units, respectively. The schedule is divided into cycles of length 3 units, which is the least common multiple of the periods of T1 and T2. The tasks are assigned to slots within each cycle according to their deadlines and priorities. The hyperperiod is the length of the schedule that repeats itself, which is 12 units in this case.



### Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights  .
- The weight of a job serves to influence the portion of service time allocated to it.
- A job with a higher weight will receive more service opportunities than a job with a lower weight.
- The service opportunities are distributed proportionally to the weights of the jobs.
- For example, if there are three jobs with weights 1, 2, and 3, then the job with weight 3 will receive twice as many service opportunities as the job with weight 2, and three times as many as the job with weight 1.
- Weighted round robin can achieve a fair and efficient allocation of resources among different jobs.
- It can also handle different types of traffic with different quality of service requirements.
- However, weighted round robin may not be suitable for hard real-time systems where all properties of all jobs are known at design time, and where offline scheduling techniques can be used.
- Weighted round robin may also suffer from long waiting times and poor response times for some jobs, especially if the weights are not well balanced.



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
- These challenges need to be addressed by using appropriate mechanisms and protocols to ensure the correctness and timeliness of real-time tasks.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their parameters are known in advance and do not change during execution. A **dynamic system** is one where the tasks and their parameters may vary unpredictably during execution.
- Static systems are easier to analyze and validate than dynamic systems, since the worst-case scenarios can be determined offline. Dynamic systems require online scheduling algorithms that can adapt to changing conditions and uncertainties.
- Static systems can provide better performance guarantees and lower overheads than dynamic systems, since the scheduling decisions can be optimized offline and embedded in the system code. Dynamic systems can provide more flexibility and robustness than static systems, since they can handle new tasks and events that were not anticipated offline.
- Static systems are more suitable for hard real-time systems, where missing deadlines can have catastrophic consequences. Dynamic systems are more suitable for soft real-time systems, where missing deadlines can have acceptable degradation of quality of service.
- Static systems can be implemented using **table-driven scheduling**, where a precomputed schedule is stored in a table and executed by a simple dispatcher. Dynamic systems can be implemented using **priority-driven scheduling**, where each task is assigned a priority and the highest priority task is executed by a preemptive scheduler.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints.
- EDF and LST may not be optimal for non-preemptive scheduling or for tasks with shared resources or synchronization requirements.
- EDF and LST may under-utilize the CPU, thus decreasing the efficiency and throughput of the system.
- EDF and LST may suffer from priority inversion, which occurs when a high-priority task is blocked by a low-priority task that holds a shared resource.
- EDF and LST may not be suitable for hard real-time systems, which require guaranteed response times and predictable behavior.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always schedule any set of periodic tasks that is feasible (i.e., the total utilization of the tasks is less than or equal to 100%) .
- RMA has a simple schedulability test that can determine if a set of periodic tasks is feasible or not. The test is based on the utilization bound, which is a function of the number of tasks and their relative deadlines .
- RMA has some advantages and disadvantages compared to other real-time scheduling algorithms. Some advantages are: simplicity, predictability, low overhead, and optimality for periodic tasks. Some disadvantages are: poor performance for aperiodic and sporadic tasks, priority inversion, and deadline misses for tasks with long cycle durations  .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute. The schedule is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time. The scheduler follows the pre-determined schedule during the run-time and does not need to make any decisions. Offline scheduling is suitable for static and deterministic systems that have fixed and known task parameters.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system. The scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known only after its release. Online scheduling is suitable for dynamic and unpredictable systems that have variable and unknown task parameters. Online scheduling can be either static or dynamic, depending on whether the priority of a task is fixed or can change during its execution.
- The advantages of offline scheduling are that it can guarantee the schedulability of all tasks, it can optimize the resource utilization, and it can reduce the overhead of scheduling. The disadvantages of offline scheduling are that it requires complete and accurate knowledge of all task parameters, it cannot handle any changes or uncertainties in the system, and it can be computationally expensive to generate the optimal schedule.
- The advantages of online scheduling are that it can handle any changes or uncertainties in the system, it can adapt to the varying workload and resource availability, and it can be simpler and faster to implement. The disadvantages of online scheduling are that it cannot guarantee the schedulability of all tasks, it can waste some resources due to scheduling decisions, and it can incur more overhead of scheduling.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival or execution pattern, and may have soft or firm deadlines.
- Sporadic jobs are jobs that have a minimum inter-arrival time between successive jobs, and may have hard or firm deadlines.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, or utilization, and schedule the highest priority job at any time.
- Clock driven systems are systems that schedule jobs based on a pre-computed table that specifies the start and end times of each job in each cycle.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the schedulability of periodic jobs.
- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to accommodate the variability of aperiodic and sporadic jobs and the rigidity of the pre-computed table.

- Some of the algorithms for scheduling aperiodic and sporadic jobs in priority driven systems are:

  - Background scheduling: aperiodic and sporadic jobs are executed only when no periodic job is ready, and have the lowest priority in the system. This algorithm is simple and guarantees the schedulability of periodic jobs, but may result in long response times for aperiodic and sporadic jobs.
  - Polling server: a periodic task with a fixed period and execution time is created to serve aperiodic and sporadic jobs. The server has a priority assigned by the priority driven algorithm, and can preempt periodic jobs with lower priority. The server can either execute aperiodic and sporadic jobs immediately when they arrive, or defer them until the next server activation. This algorithm improves the responsiveness of aperiodic and sporadic jobs, but may introduce overhead and waste server capacity.
  - Deferrable server: a periodic task with a fixed period and execution time is created to serve aperiodic and sporadic jobs. The server has a priority assigned by the priority driven algorithm, and can preempt periodic jobs with lower priority. The server can only execute aperiodic and sporadic jobs when it is activated, and defers them otherwise. The server can replenish its capacity at the beginning of each period, or carry over unused capacity to the next period. This algorithm reduces the overhead and waste of server capacity, but may increase the response times of aperiodic and sporadic jobs.
  - Sporadic server: a periodic task with a variable period and execution time is created to serve aperiodic and sporadic jobs. The server has a priority assigned by the priority driven algorithm, and can preempt periodic jobs with lower priority. The server can execute aperiodic and sporadic jobs immediately when they arrive, and replenishes its capacity after a minimum inter-arrival time. The server can also borrow capacity from future periods, or lend capacity to past periods. This algorithm adapts to the variability of aperiodic and sporadic jobs, but may require complex analysis and implementation.
  - Slack stealing: aperiodic and sporadic jobs are executed by stealing the slack time of periodic and sporadic jobs. The slack time of a job is the difference between its deadline and its remaining execution time. A slack stealing algorithm can either use global slack, which is the minimum slack time of all jobs in the system, or local slack, which is the slack time of the job with the same priority as the aperiodic or sporadic job. This algorithm maximizes the utilization of the system, but may require frequent computation and monitoring of slack times.

- Some of the algorithms for scheduling aperiodic and sporadic jobs in clock driven systems are:

  - Offline scheduling: aperiodic and sporadic jobs are assumed to be known in advance, and are incorporated into the pre-computed table along with periodic jobs. This algorithm guarantees the schedulability of all jobs, but may not be feasible or realistic for dynamic systems.
  - Online scheduling: aperiodic and sporadic jobs are handled at runtime, and are inserted into the pre-computed table when they arrive. This algorithm can either use spare capacity, which is the unused time slots in the table, or reschedule capacity, which is the time slots allocated to periodic jobs that can be shifted or preempted. This algorithm can accommodate dynamic aperiodic and sporadic jobs, but may require complex and costly online computation and modification of the table.



# Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, or network bandwidth, available to multiple users or processes.

Some of the benefits of resource sharing are:

- It can improve the efficiency and performance of the system by reducing duplication and waste of resources.
- It can enhance the functionality and usability of the system by providing access to a wider range of resources and services.
- It can promote collaboration and cooperation among users or processes by enabling them to share information and work together.

Some of the challenges of resource sharing are:

- It can increase the complexity and cost of the system by requiring additional hardware, software, or protocols to support resource sharing.
- It can introduce security and privacy risks by exposing the resources to unauthorized or malicious access or modification.
- It can create conflicts and contention among users or processes by competing for the same or limited resources.

Some of the methods of resource sharing are:

- Hardware sharing: This involves sharing physical devices or components of a computer system, such as CPU, memory, disk, printer, scanner, etc. Hardware sharing can be achieved by using multiplexing, virtualization, or distributed computing techniques.
- Software sharing: This involves sharing logical entities or components of a computer system, such as files, databases, applications, services, etc. Software sharing can be achieved by using file systems, databases, middleware, or web technologies.
- Data sharing: This involves sharing information or knowledge among users or processes, such as documents, images, videos, etc. Data sharing can be achieved by using data formats, standards, protocols, or platforms.



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple jobs or tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of jobs or tasks, especially in priority-driven systems, where higher-priority jobs may be blocked or delayed by lower-priority jobs that hold the resource.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how jobs requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock.
- Priority inversion occurs when a higher-priority job is prevented from executing by a lower-priority job that holds a resource needed by the higher-priority job.
- Timing anomalies occur when a change in the execution time of a job affects the schedulability of other jobs in an unpredictable way, such as when a shorter execution time leads to a longer response time.
- Deadlock occurs when a set of jobs are waiting for each other to release resources, resulting in a circular dependency that prevents any of them from making progress.
- RAC protocols can be classified into two categories: non-preemptive and preemptive.
- Non-preemptive protocols do not allow a job to be preempted while holding a resource, such as the mutual exclusion protocol (MEP) and the priority ceiling protocol (PCP).
- Preemptive protocols allow a job to be preempted while holding a resource, such as the stack resource policy (SRP) and the multiprocessor priority ceiling protocol (MPCP).
- Non-preemptive protocols can avoid deadlock, but may suffer from priority inversion and timing anomalies.
- Preemptive protocols can avoid priority inversion and timing anomalies, but may introduce additional overhead and complexity.



### Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or suspended by another job until it finishes the critical section .
- When a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs. This protocol is called non-preemptive critical section protocol (NPCS) .
- The advantages of NPCS are:
  - It is simple and easy to implement .
  - It prevents deadlock, since no job is ever preempted when it holds any resource .
- The disadvantages of NPCS are:
  - It may cause priority inversion, which means that a high-priority job may be blocked by a low-priority job that holds a resource .
  - It may cause blocking, which means that a job may have to wait for a resource that is held by another job .
  - It may cause long response times and low utilization of the processor .



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for resolving the problem of priority inversion in real-time systems.
- Priority inversion occurs when a higher-priority task is blocked by a lower-priority task that holds a shared resource, and the lower-priority task is preempted by a medium-priority task that does not need the resource.
- Priority-inheritance protocol (PIP) works by temporarily elevating the priority of the lower-priority task that holds the resource to the highest priority of any task that is waiting for the resource. This way, the lower-priority task can finish its critical section and release the resource, allowing the higher-priority task to resume execution.
- Priority-ceiling protocol (PCP) works by assigning a priority ceiling to each resource, which is the highest priority of any task that can access the resource. A task can only lock a resource if its priority is higher than the priority ceiling of all the resources that are currently locked by other tasks. This way, the priority ceiling prevents lower-priority tasks from preempting higher-priority tasks that may need the resource in the future.
- The differences between PIP and PCP are:
  - PIP is greedy, while PCP is not. PIP allows a task to lock a resource whenever the resource is free, while PCP may deny a task access to a free resource if its priority is lower than the priority ceiling of another resource that is locked by a lower-priority task. This is called avoidance blocking.
  - PIP can cause chained blocking, while PCP cannot. Chained blocking occurs when a task is blocked by another task that is blocked by another task, and so on. PCP avoids chained blocking by ensuring that a task can only be blocked by at most one lower-priority task that holds a resource with a higher priority ceiling than the task.
  - PIP can cause deadlock, while PCP cannot. Deadlock occurs when two or more tasks are waiting for each other to release a resource. PCP prevents deadlock by ensuring that a task can only lock a resource if it does not hold any other resource with a lower priority ceiling. This is called the preemption level property.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource.
- SBPCP has two rules: a scheduling rule and an allocation rule.
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time.
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource.
- SBPCP guarantees that a job will not be blocked by a lower priority job that holds a resource, and that a job will not be blocked by more than m-1 higher priority jobs, where m is the number of resources in the system.
- SBPCP also guarantees that there will be no deadlock, since a circular wait among jobs is impossible.
- SBPCP is similar to the Original Ceiling Priority Protocol (OCPP), but it differs in that it allows a job to request multiple resources at the same time, and it does not require a job to release all its resources before requesting a new one.
- SBPCP is also similar to the Immediate Ceiling Priority Protocol (ICPP), but it differs in that it does not raise the priority of a job until it requests a resource, and it does not lower the priority of a job until it releases all its resources.
- SBPCP has the same worst-case behavior as OCPP and ICPP from a scheduling viewpoint, but it may have better average-case performance and lower overhead.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time. The priority ceiling of a resource is the highest priority of any task that can access that resource.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- The ceiling of the system is the highest priority ceiling of all the resources currently locked.
- A task can lock a resource only if its priority is higher than the ceiling of the system. Otherwise, it has to wait until the resource is released.
- This ensures that a task can be blocked by at most one lower priority task, and that task can be blocked by at most one lower priority task, and so on.
- This reduces the blocking time and improves the schedulability of the system.
- An example of using the priority ceiling protocol in a dynamic priority system is given below :

- Consider a system with two tasks Tasks T1 (2, 0.9), T2 (5, 2.3) executed in deadline driven system as below.

| Time | Task | Resource |
| --- | --- | --- |
| 0 | T1 | X |
| 0.9 | T1 | - |
| 1 | T2 | Y |
| 2 | T1 | X |
| 2.9 | T1 | - |
| 3 | T2 | Y |
| 4 | T1 | X |
| 4.9 | T1 | - |
| 5 | T2 | Y |
| 6 | T1 | X |
| 6.9 | T1 | - |
| 7 | T2 | Y |
| 8 | T1 | X |
| 8.9 | T1 | - |
| 9 | T2 | Y |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority ceiling of Y is 2 from time 1 to 5 and becomes 1 from time 5 to 9 and so on.
- The ceiling of the system is the maximum of the priority ceilings of X and Y at any time.
- Using the priority ceiling protocol, the tasks can access the resources as follows:

| Time | Task | Resource | Ceiling |
| --- | --- | --- | --- |
| 0 | T1 | X | 1 |
| 0.9 | T1 | - | 0 |
| 1 | T2 | Y | 2 |
| 2 | T1 | X | 2 |
| 2.9 | T1 | - | 2 |
| 3 | T2 | Y | 2 |
| 4 | T1 | X | 2 |
| 4.9 | T1 | - | 2 |
| 5 | T2 | Y | 2 |
| 6 | T1 | X | 2 |
| 6.9 | T1 | - | 2 |
| 7 | T2 | Y | 2 |
| 8 | T1 | X | 2 |
| 8.9 | T1 | - | 2 |
| 9 | T2 | Y | 2 |

- Note that no task is blocked by a lower priority task, and the system is schedulable.



### Preemption Ceiling Protocol

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
  - It prevents deadlock due to circular waiting, where two or more tasks wait for each other to release the resources they hold.
  - It reduces the number of context switches, since a task can lock multiple resources without being preempted.
  - It simplifies the analysis of the worst-case response time of tasks, since the blocking time is bounded by the ceiling priority of the resources.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to prevent deadlock and priority inversion, while ensuring schedulability and resource utilization.
- There are different protocols for access control in multiple-unit resources, such as:
  - The **Priority Inheritance Protocol (PIP)**: A job that locks a resource inherits the highest priority of all the jobs that are blocked on that resource. When the job unlocks the resource, it returns to its original priority  .
  - The **Priority Ceiling Protocol (PCP)**: Each resource is assigned a priority ceiling, which is the highest priority of any job that can lock that resource. A job can lock a resource only if its priority is higher than the priority ceilings of all the locked resources. A job that locks a resource inherits the priority ceiling of that resource. When the job unlocks the resource, it returns to its original priority  .
  - The **Stack Resource Policy (SRP)**: Each job is assigned a preemption level, which is the highest priority of any resource that the job can lock. A job can lock a resource only if its preemption level is higher than the preemption levels of all the jobs that have locked any resource. A job that locks a resource cannot be preempted by any other job. When the job unlocks the resource, it can be preempted by any higher-priority job .
- The advantages and disadvantages of these protocols depend on the characteristics of the system, such as the number and type of resources, the number and priority of jobs, the length and frequency of critical sections, and the schedulability and performance requirements.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of controlling concurrent accesses to data objects in real time systems:

### Controlling Concurrent Accesses to Data Objects

- In real time systems, multiple tasks or jobs may need to access shared data objects concurrently, which may cause inconsistency or deadlock problems.
- To ensure data consistency and meet timing constraints, real time systems need to use concurrency control algorithms or protocols to regulate the accesses to data objects.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
- Pessimistic algorithms prevent conflicts from happening by locking the data objects before accessing them. Examples of pessimistic algorithms are priority ceiling protocol, convex ceiling protocol, and immediate ceiling protocol.
- Optimistic algorithms allow conflicts to happen and then resolve them by aborting or restarting some transactions. Examples of optimistic algorithms are timestamp ordering, multiversion concurrency control, and validation-based protocols.
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the degree of data contention, the criticality of transactions, and the available resources.

Some key points of each algorithm are:

- Priority ceiling protocol: Each data object has a priority ceiling, which is the highest priority of any job that can access it. The system ceiling is the highest priority ceiling of any locked data object. A job can lock a data object only if its priority is higher than the system ceiling. This prevents deadlock and priority inversion problems.
- Convex ceiling protocol: Each data object has a convex ceiling, which is the smallest convex set of priorities that contains the priorities of all jobs that can access it. A job can lock a data object only if its priority is in the convex ceiling of the data object. This reduces the blocking time and the number of preemptions compared to the priority ceiling protocol.
- Immediate ceiling protocol: Each data object has an immediate ceiling, which is the priority of the first job that locks it. A job can lock a data object only if its priority is higher than the immediate ceiling of the data object. This reduces the blocking time and the number of preemptions compared to the convex ceiling protocol, but may cause deadlock problems.
- Timestamp ordering: Each transaction has a timestamp, which is assigned when the transaction starts. A transaction can access a data object only if its timestamp is smaller than the timestamp of any other transaction that accesses the same data object. This ensures serializability, but may cause high abort rate and wasted resources.
- Multiversion concurrency control: Each data object has multiple versions, each with a timestamp. A transaction can read the latest version of a data object that has a timestamp smaller than or equal to its own timestamp. A transaction can write a new version of a data object only if its timestamp is larger than the timestamp of any other transaction that accesses the same data object. This allows more concurrency and reduces the abort rate, but requires more storage space and overhead.
- Validation-based protocols: Each transaction has a validation phase, in which it checks whether its accesses to data objects are consistent with other transactions. A transaction can commit only if it passes the validation phase. Otherwise, it has to abort and restart. This avoids locking and allows more concurrency, but may cause high abort rate and wasted resources.



## Unit 4 - Real Time Communication

Real time communication (RTC) is the exchange of information between two or more parties without significant delay. RTC can involve various modes of communication, such as voice, video, text, or data. RTC can enable collaboration, entertainment, education, health care, and other applications that require synchronous interaction.

Some of the topics covered in this unit are:

- **RTC protocols and standards**: The protocols and standards that enable RTC, such as Session Initiation Protocol (SIP), Real-time Transport Protocol (RTP), Web Real-Time Communication (WebRTC), and others.
- **RTC architectures and components**: The architectures and components that support RTC, such as servers, clients, gateways, media servers, signaling channels, and data channels.
- **RTC security and privacy**: The security and privacy challenges and solutions for RTC, such as encryption, authentication, authorization, access control, and data protection.
- **RTC quality of service and performance**: The quality of service and performance metrics and techniques for RTC, such as bandwidth, latency, jitter, packet loss, throughput, and congestion control.
- **RTC applications and use cases**: The applications and use cases that demonstrate the benefits and challenges of RTC, such as video conferencing, online gaming, telemedicine, social networking, and emergency services.



### Basic Concepts in Real Time Communication

Real time communication (RTC) is a category of software protocols and communication hardware media that gives real time guarantees, which is necessary to support real time guarantees of real time computing. Real time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.

Some of the basic concepts in real time communication are:

- **Real time**: Real time means that the communication happens in the same time frame as the events being communicated. There is no significant delay or latency between the sender and the receiver of the information. Real time communication is synonymous with live communication .
- **Latency**: Latency is the time it takes for a message to travel from the sender to the receiver. Latency can be affected by various factors, such as the distance between the sender and the receiver, the bandwidth of the communication channel, the processing speed of the devices involved, and the congestion or interference in the network. Low latency is desirable for real time communication, as it ensures that the information is delivered as close to the event as possible .
- **Quality of service (QoS)**: Quality of service is a measure of how well a communication system can deliver the desired level of performance, reliability, and availability for the users. QoS can be influenced by various parameters, such as the bandwidth, latency, jitter, packet loss, and error rate of the communication channel. QoS can be specified by the users or the applications, and can be enforced by the network or the devices using various mechanisms, such as prioritization, reservation, admission control, and congestion control .
- **Synchronization**: Synchronization is the process of aligning the timing or the state of two or more communication entities, such as devices, applications, or users. Synchronization can be achieved by using various methods, such as clocks, timestamps, sequence numbers, or acknowledgments. Synchronization is important for real time communication, as it ensures that the information is delivered and processed in the correct order and at the correct time .
- **Security**: Security is the protection of the communication system from unauthorized access, modification, or disclosure of the information. Security can be achieved by using various techniques, such as encryption, authentication, authorization, or integrity checking. Security is important for real time communication, as it ensures that the information is delivered and processed only by the intended parties and that the information is not tampered with or leaked .

: https://www.techtarget.com/searchunifiedcommunications/definition/real-time-communications
: https://www.agora.io/en/blog/real-time-communication-tools-for-online-messaging/
: https://www.vonage.com/resources/articles/real-time-communications/
: https://en.wikipedia.org/wiki/Real-time_communication
: https://en.wikipedia.org/wiki/Real-time_computing



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities with strict timing constraints.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- A hard real-time communication system is one that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable losses    .
- Examples of hard real-time communication systems are air traffic control, nuclear power plant control, and pacemakers  .
- A soft real-time communication system is one that can tolerate some deadline misses, without causing severe damage or degradation of performance    .
- Examples of soft real-time communication systems are video conferencing, online gaming, and multimedia streaming  .
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic.
- Hard real-time communication systems require strict guarantees on the worst-case execution time, latency, jitter, and reliability of the communication channels   .
- Soft real-time communication systems can accept some variations on the quality of service, as long as they are within acceptable bounds   .
- Hard real-time communication systems often use dedicated hardware, specialized protocols, and preemptive scheduling algorithms to achieve their goals   .
- Soft real-time communication systems can leverage general-purpose hardware, standard protocols, and cooperative or hybrid scheduling algorithms to optimize their performance   .



### Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- Real time communication can be classified into two types: real time traffic and real time control.
- Real time traffic consists of streams of messages that are generated by their sources and delivered to their respective destinations on a continuous basis, such as voice, video, or audio  .
- Real time control consists of commands or signals that are sent from a controller to a controlled device or system, such as a robot, a sensor, or a machine.
- Real time communication requires certain quality of service (QoS) parameters to be met, such as throughput, delay, and jitter .
- Throughput is the amount of data that can be transmitted or received per unit time .
- Delay is the time elapsed between the generation of a message at the source and its reception at the destination .
- Jitter is the variation in delay among different messages in the same stream .
- A model of real time communication can be used to analyze and design the communication system and network that support real time applications .
- A model of real time communication consists of the following components:
  - Sources and destinations: the end users of the real time applications that generate and consume messages.
  - Hosts: the devices that run the real time applications and interface with the network.
  - Network interface: the hardware and software that connect the hosts to the network and provide input and output queues for messages.
  - Network: the physical and logical infrastructure that carries the messages from the sources to the destinations.
  - Protocols: the rules and algorithms that govern the communication process and ensure the QoS requirements.
- A model of real time communication can be represented by a graph, where the nodes are the sources, destinations, hosts, and network interface, and the edges are the links and queues that connect them.
- A model of real time communication can be characterized by different traffic models, such as the peak rate model, the token bucket model, the leaky bucket model, and the generic cell rate model .
- A traffic model specifies the properties of the messages generated by the sources, such as the inter-packet spacing, the message length, and the reception deadline .
- A traffic model can be used to determine the bandwidth and buffer requirements of the network and the network interface, as well as the scheduling and admission control policies of the protocols .
- A traffic model can also be used to evaluate the performance of the real time communication system and network, such as the throughput, delay, and jitter of the messages .



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns different weights to different priority classes and serves packets in a circular order based on their weights.
- WRR does not require a sorted priority queue, only a round-robin queue.
- WRR can guarantee bandwidth and fairness requirements, but it cannot guarantee delay and jitter bounds for different classes of packets.
- A variation of WRR is weighted fair queuing (WFQ), which assigns different weights to different flows of packets and serves packets in a proportional fair manner based on their weights and arrival times.
- WFQ can guarantee delay and jitter bounds for different flows of packets, but it requires more computation and memory than WRR.
- Another variation of WRR is rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server.
- RFWRR can guarantee delay jitter bounds and satisfy diverse delay requirements for different classes of packets, but it requires more complexity and overhead than WRR.
- A different priority-based service discipline is class-based weighted fair queuing (CBWFQ), which combines WFQ and priority queuing to provide different service levels for different classes of packets.
- CBWFQ can guarantee bandwidth, delay, and jitter bounds for different classes of packets, but it requires more computation and memory than WRR.
- Another different priority-based service discipline is weighted fair priority queuing (WFPQ), which combines WFQ and strict priority queuing to provide different service levels for different classes of packets.
- WFPQ can guarantee bandwidth, delay, and jitter bounds for different classes of packets, but it requires more computation and memory than WRR and may cause starvation for low-priority packets.



# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast channel.
- Broadcast networks are networks where a single transmission can be received by all nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks need to deal with the challenges of interference, collisions, hidden terminals, and exposed terminals, which can affect the reliability and efficiency of data transmission.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to determine which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but can suffer from high collision rates and unbounded access delays.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next, such as TDMA or token passing. These protocols can provide bounded access delays and guaranteed throughput, but can be inefficient and inflexible under dynamic traffic and network conditions.
- Reservation-based protocols use a combination of contention and reservation phases to allocate slots for data transmission, such as PRMA or ABROAD. These protocols can achieve high channel utilization and reliability, but can incur overhead and complexity in the reservation process.



### Internet and Resource Reservation Protocols

- Internet applications have different network performance requirements, such as reliability, timeliness, and quality of service (QoS).
- Resource Reservation Protocol (RSVP) is a network control protocol that enables Internet applications to obtain specific QoS for their data flows or streams .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses soft state approach, which means that the reservations are periodically refreshed and automatically removed if not refreshed.
- RSVP supports both unicast and multicast receivers, and allows receivers to join and leave a multicast group dynamically.
- RSVP can coexist with other protocols, such as IP routing protocols, and can adapt to changes in the network topology or traffic conditions.
- RSVP messages are sent as IP datagrams with protocol number 46 and are processed by each RSVP-capable node along the path of the data flow.
- RSVP messages can be classified into two types: PATH and RESV.
  - PATH messages are sent by the sender to establish the route and inform the receivers and intermediate nodes about the QoS requirements of the data flow.
  - RESV messages are sent by the receivers to request and confirm the resource reservations along the path of the data flow.
- RSVP uses filterspecs and flowspecs to specify the characteristics of the data flow and the QoS request.
  - A filterspec identifies a data flow by its source address and port number.
  - A flowspec defines the QoS parameters, such as bandwidth, delay, and packet loss rate.
- RSVP supports three reservation styles: Fixed Filter (FF), Shared Explicit (SE), and Wildcard Filter (WF).
  - FF style allows each receiver to make an individual reservation for a specific data flow.
  - SE style allows a group of receivers to share a reservation for a specific data flow.
  - WF style allows a receiver to make a single reservation for all data flows from the same sender.
- RSVP can be integrated with IntServ model, which defines a set of QoS classes, such as Guaranteed Service and Controlled Load Service.
  - Guaranteed Service provides a firm bound on end-to-end delay and jitter, and ensures that no packet loss occurs due to congestion.
  - Controlled Load Service provides a QoS level similar to that of an unloaded network, and allows some packet loss and delay variation due to congestion.
- RSVP can also be used in real-time systems for an efficient quality band transmission to a particular receiver.
  - RSVP can help real-time systems to achieve timely and reliable delivery of data, and to cope with dynamic changes in the network conditions.
  - RSVP can also enable real-time systems to support different types of multimedia applications, such as videoconferencing, IP telephony, and online gaming.



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can process data and events that have critically defined time constraints.
- An RTOS is different from a general-purpose operating system, such as Windows or Linux, which is designed for multitasking and resource sharing, but not for meeting strict deadlines.
- An RTOS typically has features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS can be used for applications that require high performance, reliability, and responsiveness, such as industrial control, flight control, and real-time simulations.
- A real-time database system (RTDBS) is a database system that can perform database operations with real-time constraints.
- An RTDBS is different from a conventional database system, such as Oracle or MySQL, which is designed for batch processing and data analysis, but not for meeting strict deadlines.
- An RTDBS typically has features such as real-time transactions, concurrency control, data consistency, and recovery.
- An RTDBS can be used for applications that require fast and accurate data processing, such as online reservation, stock trading, and sensor networks.
- A real-time database system can be based on SQL or NoSQL, depending on the data model and the query language.
- A real-time database system can also be classified as a time-series database or a real-time analytics database, depending on the data type and the query performance.



### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee a certain level of performance and reliability for time-critical applications. Some of the features of an RTOS are:

- **Predictability and determinism**: An RTOS can respond to events and tasks within a known and bounded time frame, without unpredictable delays or variations. This is also called 'jitter'.
- **Small and fast**: An RTOS is designed to be lightweight and efficient, with minimal overhead and memory footprint. It can execute tasks quickly and with low latency.
- **Preemptive scheduling**: An RTOS can interrupt a lower-priority task to run a higher-priority task when an event occurs, ensuring that the most urgent tasks are always handled first. The priority of each task is assigned by the programmer.
- **Cooperative scheduling**: An RTOS can also allow tasks to voluntarily yield the processor to other tasks when they are not in need of it, or when they are waiting for an external resource. This can improve the overall utilization of the system.
- **Concurrency and synchronization**: An RTOS can support multiple tasks running simultaneously on the same or different processors, and provide mechanisms to coordinate and communicate among them. For example, semaphores, mutexes, message queues, and events are some of the common synchronization primitives in an RTOS.
- **Real-time clock and timers**: An RTOS can provide accurate and precise timing functions, such as a real-time clock that keeps track of the current date and time, and timers that can trigger tasks or events at specific intervals or deadlines.
- **Interrupt handling**: An RTOS can handle hardware and software interrupts, which are signals that indicate the occurrence of an event that requires immediate attention. An RTOS can prioritize and dispatch interrupts to the appropriate tasks or handlers, and resume the normal execution after the interrupt is serviced.
- **Device drivers and I/O**: An RTOS can provide interfaces to interact with various input and output devices, such as sensors, actuators, displays, keyboards, and network adapters. An RTOS can also provide device drivers, which are software modules that control the operation of a specific device. Device drivers can be integrated into the kernel or loaded as separate modules.
- **Memory management**: An RTOS can manage the allocation and deallocation of memory for tasks and data structures, and ensure that the memory is used efficiently and safely. An RTOS can also provide different types of memory, such as static, dynamic, or shared memory, depending on the needs of the application.
- **File system and data storage**: An RTOS can provide a file system, which is a way of organizing and accessing data on a storage device, such as a hard disk, a flash memory, or a network server. An RTOS can also support different types of file systems, such as FAT, NTFS, or NFS, depending on the compatibility and performance requirements of the application.
- **Networking and communication**: An RTOS can provide networking and communication capabilities, such as TCP/IP, UDP, HTTP, MQTT, or Bluetooth, to enable data exchange and interaction among different devices, systems, or users. An RTOS can also support different types of networks, such as wired, wireless, or cellular, depending on the availability and reliability of the connection.
- **Security and reliability**: An RTOS can provide security and reliability features, such as encryption, authentication, error detection and correction, fault tolerance, and backup and recovery, to protect the data and the system from unauthorized access, corruption, or failure. An RTOS can also support different levels of security and reliability, such as hard, firm, or soft, depending on the criticality and consequences of the application. 

These are some of the common features of an RTOS, but they may vary depending on the specific implementation and configuration of the RTOS. An RTOS can also provide other features, such as graphical user interface, power management, debugging and testing tools, and application programming interfaces, to enhance the functionality and usability of the system.  

: Real-time operating system - Wikipedia
: What Is A Real-Time Operating Systems (RTOS) | Wind River
: Real Time Operating Systems | What, Concepts & Features



### Time Services

Time services are the functions and mechanisms that provide the ability to measure, represent, and manipulate time in real-time systems. Time services are essential for ensuring the timeliness and synchronization of real-time systems, which are systems that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.

Some of the main time services for real-time systems are:

- **Clocks**: Clocks are devices that generate periodic signals to measure the passage of time. Clocks can be either hardware or software based, and they can have different levels of accuracy, resolution, and stability. Clocks can also be synchronized with other clocks using various protocols and algorithms, such as the Network Time Protocol (NTP) or the Precision Time Protocol (PTP).
- **Timers**: Timers are devices that generate interrupts or signals after a specified amount of time has elapsed. Timers can be used to trigger events, schedule tasks, measure durations, or implement timeouts. Timers can be either hardware or software based, and they can have different modes of operation, such as one-shot, periodic, or countdown.
- **Time stamps**: Time stamps are data structures that represent a specific point in time or a duration of time. Time stamps can be used to record the occurrence of events, measure the performance of tasks, compare the order of events, or calculate the deadlines of tasks. Time stamps can have different formats, such as absolute, relative, or logical.
- **Time services APIs**: Time services APIs are the interfaces that provide access to the time services functions and mechanisms. Time services APIs can be either standard or proprietary, and they can have different levels of abstraction, functionality, and portability. Time services APIs can also support different time domains, such as local, global, or logical.



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like UNIX strives to provide good average performance, for an RTOS, correct timing is the key feature.
- UNIX is not a RTOS by default, but it can be modified or extended to provide some real-time capabilities, such as:
  - Using real-time extensions, such as POSIX.1b or POSIX.4, which define a set of interfaces and services for real-time applications.
  - Using real-time patches, such as RTLinux or RTAI, which add a thin layer between the hardware and the Linux kernel, and allow real-time tasks to run in kernel space with minimal interference from the non-real-time tasks.
  - Using real-time libraries, such as Xenomai or PREEMPT_RT, which provide a user-space API for real-time programming, and implement mechanisms to reduce the latency and jitter of the Linux kernel.
- However, using UNIX as an RTOS also poses some challenges, such as:
  - The complexity and size of the UNIX kernel, which makes it difficult to verify its correctness and predictability.
  - The lack of standardization and compatibility among different real-time extensions, patches, and libraries, which may limit the portability and interoperability of real-time applications.
  - The trade-off between performance and functionality, which may require tuning and customization of the UNIX system to meet the specific requirements of the real-time application.



### POSIX Issues

- POSIX stands for Portable Operating System Interface, which is a set of standards that define how an application should interact with an operating system.
- POSIX aims to achieve portability, interoperability, and compatibility among different operating systems, especially for applications that require long-term maintenance and support.
- POSIX also covers extensions for real-time operating systems, which are systems that have strict timing constraints and need to respond to events within predictable and bounded time frames.
- POSIX real-time extensions include specifications for:
  - Scheduling policies and parameters, such as priority-based preemptive scheduling and deadline scheduling.
  - Clocks and timers, such as high-resolution timers and periodic timers.
  - Synchronization primitives, such as mutexes, condition variables, semaphores, and barriers.
  - Message passing and shared memory, such as message queues and memory-mapped files.
  - Signals and signal handlers, such as real-time signals and asynchronous I/O notification.
  - Memory management, such as memory locking and memory protection.
- POSIX real-time extensions aim to provide a common and consistent interface for real-time applications across different platforms, but they also pose some challenges and limitations, such as:
  - Implementation complexity and overhead, as some POSIX features may require additional layers of abstraction or emulation on top of the native operating system services.
  - Performance variability and unpredictability, as some POSIX features may introduce non-determinism or interference in the system behavior, such as dynamic memory allocation, signal delivery, or context switching.
  - Incompleteness and ambiguity, as some POSIX features may not cover all the aspects or requirements of real-time systems, such as resource reservation, fault tolerance, or quality of service.
  - Portability trade-off, as some POSIX features may not be supported or implemented consistently by all operating systems, or may require specific hardware or software configurations, which may limit the portability or compatibility of the applications.



### Characteristic of Temporal Data

- Temporal data are any data that represent time in some form, and allow other data to be placed in a chronological sequence, or to be analyzed chronologically.
- Temporal data can be classified into three types: valid time, transaction time, and decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world. For example, the date of birth of a person is a valid time attribute.
  - Transaction time is the time period during or event time at which a fact is stored in the database. For example, the date of entry of a person's record in the database is a transaction time attribute.
  - Decision time is the time period during or event time at which a fact is decided or acted upon. For example, the date of approval of a loan application is a decision time attribute.
- Temporal data can have different characteristics depending on the type of time they represent and the application domain. Some of these characteristics are :
  - Temporality: the extent to which the data are affected by time. For example, the current temperature of a region is highly temporal, as it changes frequently and becomes obsolete after a certain period of time.
  - Granularity: the level of detail or precision of the data. For example, the temperature of a region can be measured in degrees Celsius, Fahrenheit, or Kelvin, with different levels of granularity.
  - Periodicity: the frequency or regularity of the data. For example, the temperature of a region can be measured hourly, daily, weekly, or monthly, with different levels of periodicity.
  - Duration: the length or span of the data. For example, the temperature of a region can be measured for a single point in time, a time interval, or a time period, with different levels of duration.
  - Consistency: the degree of agreement or coherence of the data. For example, the temperature of a region can be consistent or inconsistent with other sources of data, such as weather stations, satellites, or sensors.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to process data that is time-sensitive and relevant to the current situation. If the data is outdated or inaccurate, it may lead to incorrect decisions or actions that may have serious consequences.
- Temporal consistency can be measured by the temporal error, which is the difference between the actual value of a data item and the value stored in the database. The temporal error should be within a predefined limit, otherwise the data item is considered temporally inconsistent .
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the database system when a data item becomes temporally inconsistent. The update is performed by a special transaction that has a high priority and a short deadline.
  - Periodic updates, which are updates that are performed by the data sources at regular intervals. The update interval is determined by the temporal error limit and the data change rate.
  - Eager updates, which are updates that are performed by the data sources as soon as a data item changes. This technique minimizes the temporal error, but may increase the communication and computation overhead.
  - Lazy updates, which are updates that are performed by the data sources only when a data item is requested by a transaction. This technique reduces the communication and computation overhead, but may increase the temporal error.
- Temporal consistency can be affected by various factors, such as:
  - The data change rate, which is the frequency of changes in the physical environment that affect the data items.
  - The data access pattern, which is the frequency and type of transactions that access the data items.
  - The concurrency control algorithm, which is the mechanism that coordinates the access and update of the data items by multiple transactions.
  - The system load, which is the amount of transactions and data items that the system has to process.
  - The system architecture, which is the structure and configuration of the system components, such as the data sources, the database system, and the communication network.



# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control techniques prevent conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and priority inheritance protocols.
  - Optimistic concurrency control techniques allow conflicts to occur and then resolve them by aborting or restarting the conflicting transactions. Examples of optimistic techniques are optimistic concurrency control, multiversion concurrency control, and snapshot isolation.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as performance considerations, timing constraints, correctness criteria, and transaction models.
  - Performance considerations: RTS require fast response time, low overhead, and high throughput, while database systems focus on data consistency, durability, and recovery.
  - Timing constraints: RTS have deadlines and temporal validity of data, while database systems have no explicit time requirements.
  - Correctness criteria: RTS have to satisfy both logical and timing correctness, while database systems only need to ensure logical correctness. Logical correctness means that the concurrent execution of transactions preserves the consistency of the database. Timing correctness means that the transactions meet their deadlines and access temporally valid data.
  - Transaction models: RTS have different types of transactions, such as hard, soft, and firm, with different characteristics and requirements, while database systems have a uniform transaction model based on the ACID properties (atomicity, consistency, isolation, and durability).
- Concurrency control techniques for RTS have to balance the trade-off between concurrency and correctness, and adapt to the dynamic and unpredictable nature of the real-time environment.
- Concurrency control techniques for RTS have to consider various factors, such as the priority of transactions, the temporal validity of data, the deadline of transactions, the abort rate of transactions, the blocking time of transactions, and the resource utilization.
- Concurrency control techniques for RTS have to be evaluated based on various metrics, such as the number of transactions completed, the number of transactions missed their deadlines, the number of transactions aborted, the response time of transactions, the overhead of concurrency control, and the throughput of the system.



### Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses.
- Some of the attributes of live real-time databases are:
  - Concurrency control: the ability to handle multiple transactions accessing the same data without compromising data integrity or consistency.
  - Data freshness: the degree to which the data reflects the current state of the real world.
  - Data distribution: the ability to store and access data across multiple nodes or locations for scalability and availability.
  - Data replication: the ability to create and maintain copies of data for fault tolerance and performance.
  - Data recovery: the ability to restore data to a consistent state after a failure or error.
  - Data security: the ability to protect data from unauthorized access or modification.
  - Data quality: the ability to ensure that data is accurate, complete, and reliable.
  - Data analysis: the ability to perform queries and computations on data to derive insights and intelligence.
- Some of the examples of commercial real-time databases are :
  - Dealpath: a cloud-based platform that provides data and tools for commercial real estate investment and development.
  - Altus Group: a data and software provider that offers historical and current market information for commercial real estate valuation and analysis.
  - CoStar: a leading provider of commercial real estate data and analytics that covers over 5.5 million properties and 18 billion square feet of space.
  - Google Cloud Firestore: a highly performant, fully managed NoSQL database service for large analytical and operational workloads that offers up to 99.999% availability.

