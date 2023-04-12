

# Real Time System

A real time system is a system that can process and respond to inputs or events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to meet its deadlines, otherwise it may cause a system failure or undesirable consequences.

Some examples of real time systems are:

- Process control systems, such as chemical plants, power plants, or nuclear reactors, that monitor and regulate physical processes continuously and precisely .
- Machine vision systems, such as face recognition, object detection, or autonomous driving, that use cameras and sensors to capture and interpret visual data rapidly and accurately.
- Robotics systems, such as industrial robots, drones, or surgical robots, that use actuators and feedback mechanisms to perform complex tasks and movements in coordination with other systems .
- Flight control systems, such as autopilot, air traffic control, or collision avoidance, that use sensors and algorithms to ensure the safety and efficiency of aircraft operations.

There are two main types of real time systems based on their timing constraints:

- Hard real time system: This type of system has absolute deadlines, and if those deadlines are missed, a system failure will occur. For example, a flight control system must respond to a sudden change in wind speed or direction within milliseconds, otherwise the aircraft may crash.
- Soft real time system: This type of system has relative deadlines, and if those deadlines are missed occasionally, the system performance will degrade but not fail. For example, a video streaming system must deliver frames to the display device within a certain time interval, otherwise the video quality will suffer but not stop.

Some of the challenges and characteristics of real time systems are:

- Time synchronization: Real time systems must be able to coordinate their clocks and operate together in unison, especially in distributed or networked systems. For example, a robotic system must synchronize its sensors and actuators to perform a coordinated movement.
- Resource management: Real time systems must be able to allocate and deallocate resources, such as memory, CPU, or bandwidth, efficiently and dynamically, according to the changing demands and priorities of the tasks. For example, a machine vision system must be able to adjust its resolution and frame rate depending on the available processing power and network speed.
- Fault tolerance: Real time systems must be able to detect and recover from errors, failures, or disruptions, without compromising their functionality and reliability. For example, a process control system must be able to switch to a backup mode or a safe state in case of a sensor malfunction or a power outage.



## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, or multimedia.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
- Hard real time systems are systems that must meet their deadlines strictly, otherwise they may cause catastrophic failure or loss of life. For example, a nuclear reactor control system or a pacemaker.
- Soft real time systems are systems that can tolerate some degree of deadline miss, but the quality of service or user satisfaction may degrade. For example, a video streaming system or a video game.
- Real time systems can also be classified into two types based on their workload: periodic systems and aperiodic systems.
- Periodic systems are systems that have a set of tasks that repeat at regular intervals, such as sensor sampling, data processing, or actuator control. The period of a task is the time between two consecutive executions of the same task.
- Aperiodic systems are systems that have a set of tasks that are triggered by unpredictable events, such as user inputs, interrupts, or alarms. The inter-arrival time of a task is the time between two consecutive arrivals of the same task.
- Real time systems face many challenges and issues, such as concurrency, synchronization, scheduling, resource management, fault tolerance, security, and verification. These issues require careful design and analysis of the system to ensure its correctness and efficiency.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of definition for the notes of the unit 1 - introduction of real time system in the subject of real time system.

# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic real time system and aperiodic real time system.
- A periodic real time system is a system that has events or inputs that occur at regular intervals, and the deadlines are known in advance. For example, a sensor that samples data every 10 milliseconds, or a task that executes every 5 seconds.
- An aperiodic real time system is a system that has events or inputs that occur at irregular intervals, and the deadlines are not known in advance. For example, a user request, a network packet, or an interrupt.
- A real time system can also be classified into two types based on the number of processors: single processor real time system and multiprocessor real time system.
- A single processor real time system is a system that has only one processor to execute all the tasks. The processor may use scheduling algorithms to manage the execution order and priority of the tasks.
- A multiprocessor real time system is a system that has more than one processor to execute the tasks. The processors may communicate and synchronize with each other to achieve the system goals. The multiprocessor real time system can be further divided into two types: homogeneous multiprocessor real time system and heterogeneous multiprocessor real time system.
- A homogeneous multiprocessor real time system is a system that has processors with the same architecture, speed, and functionality. The processors may share the same memory and resources, or have their own memory and resources.
- A heterogeneous multiprocessor real time system is a system that has processors with different architecture, speed, and functionality. The processors may have different roles and responsibilities, such as master-slave, client-server, or peer-to-peer.



# Typical Real Time Applications

A real-time application (RTA) is an application that has strict time constraints on its performance and reliability. RTAs often interact with the physical world and require fast and accurate responses to external events. RTAs can be classified into two types: hard real-time and soft real-time. Hard real-time applications have absolute deadlines that must be met, otherwise the system may fail or cause severe consequences. Soft real-time applications have relative deadlines that can be occasionally missed, but the system performance may degrade or lose some functionality.

Some examples of typical real-time applications are:

- **Video conferencing**: This is an application that allows users to communicate with each other through video and audio streams over the Internet. Video conferencing requires high bandwidth, low latency, and synchronization of the data streams. Video conferencing is a soft real-time application, as missing some frames or packets may not affect the overall quality of the communication, but may cause some glitches or delays.

- **Voice over Internet Protocol (VoIP)**: This is an application that enables users to make phone calls over the Internet. VoIP requires low bandwidth, low latency, and high quality of the audio signals. VoIP is a hard real-time application, as missing some packets or exceeding the delay threshold may cause the call to drop or become unintelligible.

- **Online gaming**: This is an application that allows users to play games with other users over the Internet. Online gaming requires high bandwidth, low latency, and consistency of the game state. Online gaming is a soft real-time application, as missing some packets or experiencing some jitter may not affect the gameplay, but may cause some lag or unfairness.

- **Community storage applications**: These are applications that allow users to store and share data over the Internet. Community storage applications require high bandwidth, high availability, and security of the data. Community storage applications are soft real-time applications, as missing some data or experiencing some delay may not affect the functionality, but may cause some inconvenience or loss of performance.

- **Some e-commerce applications**: These are applications that allow users to buy and sell goods and services over the Internet. Some e-commerce applications require high availability, security, and accuracy of the transactions. Some e-commerce applications are hard real-time applications, as missing some transactions or experiencing some errors may cause financial losses or legal issues.

- **Real-time operating system (RTOS)**: This is an operating system that supports the execution of real-time applications. RTOS provides mechanisms for scheduling, synchronization, communication, and resource management of the real-time tasks. RTOS is a hard real-time application, as failing to meet the deadlines or violating the constraints of the real-time tasks may cause the system to malfunction or crash.

- **Instant messaging (IM) applications**: These are applications that allow users to send and receive text, voice, or video messages over the Internet. IM applications require low bandwidth, low latency, and security of the messages. IM applications are soft real-time applications, as missing some messages or experiencing some delay may not affect the communication, but may cause some annoyance or confusion.

- **Team collaboration applications**: These are applications that allow users to work together on projects or tasks over the Internet. Team collaboration applications require high bandwidth, low latency, and synchronization of the data and actions. Team collaboration applications are soft real-time applications, as missing some updates or experiencing some delay may not affect the collaboration, but may cause some inefficiency or inconsistency.

- **Digital control**: This is an application that uses sensors and actuators to control a physical system or process. Digital control requires fast and accurate feedback and output. Digital control is a hard real-time application, as failing to meet the deadlines or violating the constraints of the control system may cause instability or damage .

- **Optimal control**: This is an application that uses mathematical models and algorithms to optimize the performance or efficiency of a physical system or process. Optimal control requires high computational power and accuracy. Optimal control is a hard real-time application, as failing to meet the deadlines or violating the constraints of the optimization problem may cause suboptimal or unacceptable results .

- **Command and control**: This is an application that uses sensors and actuators to monitor and manage a complex system or environment. Command and control requires high reliability, availability, and security. Command and control is a hard real-time application, as failing to meet the deadlines or violating the constraints of the management system may cause failure or catastrophe [^



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Real Time System. Here is the content for the topic of Release Times for the notes of the Unit 1 - Introduction of Real Time System:

# Release Times

- Release times are the moments when tasks become available for execution in a real time system.
- Release times can be specified in different ways, depending on the type of task and the system model.
- Some common ways to specify release times are:

  - **Periodic tasks**: These are tasks that have a fixed interval between their consecutive releases, called the period. For example, a task that is released every 10 milliseconds has a period of 10 milliseconds. The release time of the first instance of a periodic task can be given as an offset from the start of the system or as a deadline from the previous instance.
  - **Sporadic tasks**: These are tasks that have a minimum inter-arrival time between their consecutive releases, called the minimum separation. For example, a task that is released at least 5 milliseconds after the previous release has a minimum separation of 5 milliseconds. The release time of the first instance of a sporadic task can be given as an offset from the start of the system or as a deadline from the previous instance.
  - **Aperiodic tasks**: These are tasks that have no regular pattern in their release times. They can be released at any time, depending on external events or user inputs. For example, a task that is released when a button is pressed is an aperiodic task. The release time of an aperiodic task can be given as an absolute time or as a relative time from the current time.
  - **Mixed tasks**: These are tasks that have a combination of periodic, sporadic, and aperiodic components. For example, a task that is released periodically every 20 milliseconds, but can also be triggered by a sensor event every 50 milliseconds, is a mixed task. The release time of a mixed task can be given as a function of the periodic, sporadic, and aperiodic components.

- Release times are important for the analysis and scheduling of real time systems, as they determine the feasibility and optimality of different solutions.
- Release times can also affect the performance and quality of service of real time systems, as they influence the response time, jitter, and deadline miss ratio of tasks.



# Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are due on **Friday, March 24, 2023** by **11:59 PM**.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in **Markdown** format and uploaded to the **Moodle** platform.
- The notes should be **clear, concise, and accurate**. They should include **diagrams, tables, and equations** where appropriate.
- The notes should follow the **IEEE citation style** and include a **reference list** at the end.
- The notes will be graded based on the following criteria:
  - Completeness and coverage of the topics
  - Quality and clarity of the writing
  - Correctness and relevance of the examples
  - Originality and creativity of the presentation
  - Adherence to the format and citation guidelines
- The notes will be worth **10%** of the final grade for the subject of Real Time System.
- Late submissions will incur a **penalty of 10%** per day, up to a maximum of **50%**.
- No submissions will be accepted after **Wednesday, March 29, 2023**.



# Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems.
- Timing constraints decide the total correctness of the result in real-time systems.
- The correctness of results in real-time system does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Time constraints related with real-time systems simply means that time interval allotted for the response of the ongoing program.
- This deadline means that the task should be completed within this time interval.
- Real-time system is responsible for the completion of all tasks within their time intervals.
- Timing constraints associated with the real-time system are classified to identify the different types of timing constraints in a real-time system.
- Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system is known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system is known as Reliability Constraints.
- Performance Constraints are further classified into three types:
  - Delay Constraint: A delay constraint describes the minimum time interval between occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between occurrence of two consecutive events.
  - Duration Constraint: Duration constraint describes the maximum time interval for the execution of a task.
- Reliability Constraints are further classified into two types:
  - Synchronization Constraint: A synchronization constraint describes the order of execution of tasks or events.
  - Exclusion Constraint: An exclusion constraint describes the mutual exclusion of tasks or events.
- Timing constraints can be expressed using various constructs in requirements languages.
- Timing constraints can be validated using automatic test systems that can measure the actual response time of the system.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.



# Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization).
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur .
- A hard real time system is also known as an immediate real time system.
- A hard real time system is usually found interacting at a low level with physical hardware, in embedded systems.
- Examples of hard real time systems are:
  - Nuclear power plant control systems
  - Air traffic control systems
  - Medical devices such as pacemakers and defibrillators
  - Automotive systems such as anti-lock braking systems and engine control units
  - Industrial robots and automation systems
  - Early video game systems such as the Atari 2600 and Cinematronics vector graphics
- Characteristics of hard real time systems are:
  - The size of data and code is small and fixed
  - The response time is in milliseconds or microseconds
  - The peak load performance should be predictable and consistent
  - The safety is critical and the system must be reliable and fault-tolerant 
  - The system must be able to handle concurrent events and interrupts
  - The system must be able to synchronize with external devices and signals



# Soft Real Time Systems

- A soft real time system is a system that has timing requirements, but not as strict as a hard real time system .
- A soft real time system can tolerate some degree of jitter, latency, or missed deadlines, without causing catastrophic failure or unacceptable degradation of performance  .
- A soft real time system can run on multiple cores and impose fewer restrictions on applications than a hard real time system.
- Examples of soft real time systems are multimedia streaming, video conferencing, online gaming, voice over IP, etc  .
- A soft real time system can use various scheduling algorithms, such as earliest deadline first, rate monotonic, or proportional share, to allocate resources and prioritize tasks.



# Reference Models for Real Time Systems

A reference model is a canonical form that describes the essential features and properties of a system, without specifying the implementation details. A reference model can help us to reason about the system, to compare different systems, and to design new systems.

A reference model for real time systems consists of three main elements:

- A workload model that describes the applications supported by the system, such as the tasks, jobs, deadlines, resource dependencies, etc.
- A resource model that describes the resources available in the system, such as the processors, memory, network, sensors, actuators, etc.
- A system model that describes the behavior and performance of the system, such as the scheduling policies, resource allocation, fault tolerance, etc.

Some examples of reference models for real time systems are:

- The Real-time Control System (RCS) model, which combines real-time motion planning and control with high-level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis .
- The Real-time CORBA model, which defines a set of standard interfaces and services for distributed real-time systems based on the Common Object Request Broker Architecture (CORBA) middleware.
- The Real-time UML model, which extends the Unified Modeling Language (UML) with real-time concepts and notations, such as timing constraints, concurrency, communication, and synchronization.



# Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. Examples of resources are memory, files, printers, and sensors.
- Processors and resources can be classified into two categories: dedicated and shared.
- Dedicated processors and resources are allocated to a single job or task and cannot be used by any other job or task. Dedicated processors and resources can guarantee predictable and deterministic performance for real-time applications.
- Shared processors and resources are accessible by multiple jobs or tasks and can be used by any job or task that needs them. Shared processors and resources can improve the utilization and efficiency of the system, but they can also introduce contention and interference among the jobs or tasks that share them. Shared processors and resources can cause unpredictable and nondeterministic performance for real-time applications.
- Real-time systems need to manage the allocation and scheduling of processors and resources to meet the timing constraints and quality of service requirements of the real-time applications.
- Real-time systems can use different techniques and algorithms to manage the processors and resources, such as priority-based scheduling, resource reservation, resource locking, resource access protocols, and resource reclaiming .
- Real-time systems can also use different hardware and software features to support the processors and resources, such as real-time operating systems (RTOS), real-time configuration and optimization, time synchronization and communication, and real-time computing platforms  .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of temporal parameters of real time workload for the unit 1 - introduction of real time system in the subject of real time system.

# Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics.
- The temporal parameters of a job are :
  - Release time (ri): the earliest time at which the job can start execution.
  - Absolute deadline (di): the latest time by which the job must finish execution.
  - Relative deadline (Di): the maximum time allowed for the job to complete execution after its release time. Di = di - ri.
  - Feasible interval [(ri, di)]: the time interval in which the job can be feasibly executed. The job must start and finish within this interval.
- The temporal parameters of a job can be known in advance (static) or determined at run time (dynamic).
- The temporal parameters of a job can be fixed (deterministic) or variable (stochastic).
- The temporal parameters of a job can be affected by factors such as jitter, precedence constraints, resource requirements, and interarrival times.



# Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks in the system.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a schedule that can meet all the deadlines of the task. A set of periodic tasks is said to be feasible if there exists a schedule that can meet all the deadlines of all the tasks in the set.
- A periodic task is said to be implicit-deadline if its relative deadline is equal to its period, i.e., Di = Pi. A periodic task is said to be constrained-deadline if its relative deadline is less than or equal to its period, i.e., Di ≤ Pi. A periodic task is said to be arbitrary-deadline if its relative deadline can be any value, i.e., Di can be greater than, equal to, or less than Pi.
- A periodic task is said to be synchronous if its phase is zero, i.e., Φi = 0. A periodic task is said to be asynchronous if its phase is non-zero, i.e., Φi > 0.
- A periodic task is said to be independent if it does not share any resources or communicate with any other tasks. A periodic task is said to be dependent if it shares some resources or communicates with some other tasks.
- A periodic task is said to be preemptive if it can be interrupted by a higher priority task and resume later. A periodic task is said to be non-preemptive if it cannot be interrupted once it starts execution.
- A periodic task is said to be sporadic if it has a minimum inter-arrival time between two consecutive jobs, which is equal to or greater than its period. A periodic task is said to be jittery if it has a maximum deviation from its ideal release time, which is called the jitter.



# Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real-time systems.
- Precedence constraints are imposed by the logical or temporal order of the jobs, while data dependency is caused by the communication or sharing of data among the jobs.
- Precedence constraints can be represented by a directed graph called a precedence graph, where the vertices are the jobs and the edges indicate the precedence relations. A job can only start execution after all its predecessors have finished execution.
- Data dependency cannot be captured by a precedence graph, as it depends on the data values and the synchronization mechanisms used by the jobs. Data dependency may introduce delays or blocking in the execution of the jobs, and may affect the schedulability and feasibility of the system.
- Precedence constraints and data dependency are important factors to consider in the design and analysis of real-time systems, as they may affect the performance, reliability, and correctness of the system.



# Unit 2 - Real Time Scheduling

- Real time scheduling is the process of allocating CPU time to tasks that have strict timing constraints and deadlines.
- Real time scheduling aims to ensure that tasks are completed within their deadlines, without compromising the quality of service or the system performance.
- Real time scheduling can be classified into two categories: hard real time and soft real time.
  - Hard real time scheduling requires that tasks meet their deadlines without any exceptions. Missing a deadline can result in catastrophic consequences for the system or the environment. Examples of hard real time systems are nuclear reactors, air traffic control, and pacemakers.
  - Soft real time scheduling allows some tasks to miss their deadlines occasionally, as long as the system can recover from the delay. Missing a deadline can result in degraded performance or quality of service, but not in fatal errors. Examples of soft real time systems are multimedia applications, online gaming, and voice over IP.
- Real time scheduling can also be classified into two types: static and dynamic.
  - Static real time scheduling assigns priorities to tasks before the system starts running, and does not change them during the execution. Static scheduling is simpler and faster, but less flexible and adaptable to changing conditions. Examples of static scheduling algorithms are rate monotonic, deadline monotonic, and earliest deadline first.
  - Dynamic real time scheduling assigns priorities to tasks at run time, based on their current state and the system conditions. Dynamic scheduling is more complex and slower, but more flexible and adaptable to changing conditions. Examples of dynamic scheduling algorithms are least laxity first, least slack time, and earliest deadline first with deadline inheritance.
- Real time scheduling involves the following components:
  - Tasks: the units of work that need to be executed by the system. Tasks can be periodic, aperiodic, or sporadic, depending on their arrival pattern and frequency.
  - Scheduler: the component that decides which task to execute next, based on their priorities and deadlines. The scheduler can be preemptive or non-preemptive, depending on whether it can interrupt a running task or not.
  - Clock: the component that provides the time reference for the system and the tasks. The clock can be internal or external, depending on whether it is synchronized with the environment or not.
  - Processor: the hardware element that executes the tasks. The processor can be single or multiple, depending on whether the system has one or more CPUs.



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution time to tasks that have timing constraints, such as deadlines, periods, or release times. Real time scheduling aims to ensure that the tasks meet their timing requirements and the system behaves correctly and predictably.

There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the performance criteria. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks are known at design time, such as their periods, execution times, deadlines, and dependencies. In this approach, a scheduler generates a static schedule offline, based on a table that specifies which task to execute at each time instant. The scheduler uses a timer to trigger the execution of the tasks according to the table. This approach is simple, predictable, and efficient, but it is not flexible or adaptable to dynamic changes or uncertainties in the system  .

- **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft or firm real time systems, where some of the properties of the tasks are not known at design time, such as their arrival times, execution times, or resource requirements. In this approach, a scheduler assigns a priority to each task based on some criteria, such as its deadline, period, or importance. The scheduler uses a priority queue to select the highest priority task to execute at each time instant. The scheduler may preempt the execution of a lower priority task if a higher priority task arrives. This approach is flexible, adaptable, and responsive, but it may incur more overhead, complexity, and unpredictability  .

- **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority. It is commonly used for time-shared systems, where the goal is to provide fair and responsive service to multiple users or applications. In this approach, a scheduler allocates a fixed time slice to each task in a circular order. The scheduler switches to the next task in the queue after the current task finishes its time slice or blocks. This approach is simple, fair, and easy to implement, but it may not guarantee the timing requirements of the tasks .

- **Weighted round-robin approach**: This approach is a variation of round-robin approach, where the tasks have different weights that reflect their relative importance or resource demand. It is commonly used for multimedia systems, where the goal is to provide quality of service to different types of data streams. In this approach, a scheduler allocates a proportional time slice to each task based on its weight. The scheduler switches to the next task in the queue after the current task finishes its time slice or blocks. This approach is more flexible and adaptable than round-robin approach, but it may still not guarantee the timing requirements of the tasks .



# Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling .
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A schedule of the jobs is computed off-line and is stored for use at run-time.
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling can be implemented using cyclic scheduling, table-driven scheduling, or hybrid scheduling.
- Cyclic scheduling is a simple method that assigns a fixed time slot to each job in a cycle.
- Table-driven scheduling is a more flexible method that uses a precomputed table of start times for each job.
- Hybrid scheduling is a combination of cyclic and table-driven scheduling that can handle both periodic and aperiodic jobs.
- Clock-driven scheduling has some advantages and disadvantages:
  - Advantages:
    - It is easy to implement and verify.
    - It can guarantee the deadlines of hard real-time jobs.
    - It can reduce the overhead of context switching and scheduling decisions.
  - Disadvantages:
    - It is not suitable for dynamic or unpredictable workloads.
    - It may waste CPU time if the jobs finish earlier than their allocated time slots.
    - It may not be able to handle sporadic or urgent events.



# Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights  .
- The weight of a job serves to influence the portion of service time allocated to it.
- A job with a higher weight will receive more service opportunities than a job with a lower weight.
- The service opportunities are distributed proportionally to the weights of the jobs.
- For example, if there are three jobs with weights 1, 2, and 3, then the service opportunities will be allocated as follows:

| Job | Weight | Service Opportunities |
| --- | ------ | --------------------- |
| A   | 1      | 1                     |
| B   | 2      | 2                     |
| C   | 3      | 3                     |

- The total number of service opportunities in a cycle is equal to the sum of the weights of the jobs.
- In this example, the total number of service opportunities is 6, and the portion of service time allocated to each job is:

| Job | Weight | Portion of Service Time |
| --- | ------ | ----------------------- |
| A   | 1      | 1/6                     |
| B   | 2      | 2/6                     |
| C   | 3      | 3/6                     |

- The advantage of weighted round robin is that it can provide differentiated service to different jobs based on their weights .
- It can also handle variable-length jobs by adjusting the weights dynamically.
- The disadvantage of weighted round robin is that it may not be suitable for hard real-time systems where all jobs have strict deadlines and fixed priorities.
- It may also introduce more overhead and complexity than the basic round-robin scheme.



# Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two types: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state and events.
- Priority-driven scheduling can be applied to both periodic and aperiodic tasks.
- Periodic tasks are tasks that have a fixed inter-arrival time and a fixed execution time.
- Aperiodic tasks are tasks that have a variable inter-arrival time and a variable execution time.
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, which is a framework for developing robotic applications.
- ROS 2 uses a weighted round-robin scheduling approach, which allocates a fixed amount of time to each task in a circular order.
- This approach can cause delays and jitter for high-priority tasks, especially when the system is overloaded or has a mix of time-based and event-based activities.
- Priority-driven scheduling can overcome these limitations by giving higher priority to more critical tasks and adapting to changing conditions and events.



# Dynamic Versus Static Systems

- A **dynamic system** is one that changes its behavior or configuration in response to external events or inputs, such as workload, user requests, or environmental conditions.
- A **static system** is one that has a fixed and predetermined behavior or configuration that does not change during the system execution.
- Dynamic and static systems have different advantages and disadvantages for real-time scheduling, which is the process of assigning priorities and resources to tasks that have timing constraints.
- Some of the factors that affect the choice of dynamic or static scheduling are:

  - The **predictability** of the system workload and environment. Static scheduling is more suitable for systems that have a known and fixed set of tasks and deadlines, while dynamic scheduling is more flexible for systems that have variable and unpredictable workloads and events .
  - The **complexity** of the system and the scheduling algorithm. Static scheduling is simpler and faster to implement and execute, while dynamic scheduling requires more computation and overhead to determine the optimal priorities and resources for each task at run time .
  - The **validation** of the system and the scheduling algorithm. Static scheduling is easier to verify and guarantee the correctness and feasibility of the schedule, while dynamic scheduling is harder to analyze and prove the schedulability and optimality of the schedule .
  - The **performance** of the system and the scheduling algorithm. Dynamic scheduling can achieve better performance in terms of response time, resource utilization, and adaptability, while static scheduling can suffer from poor performance due to over-provisioning, under-utilization, and rigidity .

- Some of the examples of dynamic and static scheduling algorithms are:

  - **Earliest Deadline First (EDF)**: A dynamic scheduling algorithm that assigns the highest priority to the task with the earliest absolute deadline .
  - **Least Slack Time (LST)**: A dynamic scheduling algorithm that assigns the highest priority to the task with the least amount of slack time, which is the difference between the deadline and the remaining execution time .
  - **Rate Monotonic (RM)**: A static scheduling algorithm that assigns the highest priority to the task with the shortest period or inter-arrival time .
  - **Deadline Monotonic (DM)**: A static scheduling algorithm that assigns the highest priority to the task with the shortest relative deadline .

- Depending on the requirements and characteristics of the real-time system, one may choose a dynamic or a static scheduling algorithm, or a combination of both, to achieve the desired performance and reliability.



# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints. This means that EDF can schedule any set of tasks that is schedulable by any other algorithm.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints. This means that LST can schedule any set of tasks that is schedulable by any other algorithm that respects the precedence constraints.
- However, EDF and LST are not optimal for non-preemptive scheduling or for tasks with shared resources or synchronization requirements. In these cases, EDF and LST may fail to produce a feasible schedule even if one exists.



# Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can always schedule any set of periodic tasks that is schedulable by any other static-priority algorithm .
- RMA has some advantages and disadvantages compared to other scheduling algorithms, such as:
  - Advantages:
    - Simple and easy to implement .
    - Predictable and deterministic .
    - Low overhead and context switching .
  - Disadvantages:
    - Not suitable for aperiodic or sporadic tasks .
    - Not optimal for tasks with different deadlines and periods .
    - May suffer from priority inversion and blocking .
- RMA has some feasibility tests to check if a given set of tasks can be scheduled by RMA, such as:
  - Utilization test: The total utilization of the tasks must be less than or equal to the number of tasks times the difference between 2 and the inverse of the number of tasks .
  - Response time test: The worst-case response time of each task must be less than or equal to its deadline .
  - Schedulability test: The worst-case response time of the highest priority task must be less than or equal to its period, and the worst-case response time of each lower priority task must be less than or equal to its deadline minus the interference from higher priority tasks .



# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task.
- Offline scheduling has the advantage of being optimal, since it can exploit the complete knowledge of the task set and the system state, but it has the disadvantage of being inflexible, since it cannot handle dynamic changes or uncertainties in the task parameters or the system environment.
- Online scheduling has the advantage of being adaptive, since it can react to dynamic changes or uncertainties in the task parameters or the system environment, but it has the disadvantage of being suboptimal, since it has to make decisions based on incomplete or inaccurate information.
- Offline scheduling is suitable for static or periodic task sets, where the task parameters and the system state are known and fixed in advance, and the system behavior is predictable and deterministic.
- Online scheduling is suitable for dynamic or aperiodic task sets, where the task parameters and the system state are unknown or variable in advance, and the system behavior is unpredictable and stochastic.
- Examples of offline scheduling algorithms are table-driven scheduling, cyclic executive scheduling, and time-triggered scheduling.
- Examples of online scheduling algorithms are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.



# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, utilization, etc. The scheduler always selects the highest priority job to execute at any time. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign fixed time slots to jobs based on their arrival patterns and execution times. The scheduler follows a pre-computed schedule that is determined offline. Examples are cyclic executive, time triggered, etc.

## Scheduling Aperiodic and Sporadic jobs in Priority Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic jobs and the schedulability of periodic and sporadic jobs.
- There are two main approaches to schedule aperiodic and sporadic jobs in priority driven systems: background scheduling and slack stealing.

### Background Scheduling

- Background scheduling is a simple and intuitive approach that assigns the lowest priority to aperiodic jobs and executes them only when there are no periodic or sporadic jobs ready to run. This ensures that aperiodic jobs do not interfere with the schedulability of periodic and sporadic jobs, but it also results in poor responsiveness of aperiodic jobs, especially when the system is heavily loaded with periodic and sporadic jobs.
- Background scheduling can be improved by using a server task, which is a periodic task that reserves a portion of the processor time for aperiodic jobs. The server task has a fixed priority and a fixed budget, and it replenishes its budget periodically. When the server task is ready to run, it executes the aperiodic jobs in a first-come first-served order until its budget is exhausted or there are no more aperiodic jobs. This way, the server task can provide a guaranteed service level to aperiodic jobs, while still respecting the priorities of periodic and sporadic jobs. There are different types of server tasks, such as polling server, deferrable server, sporadic server, etc., that differ in how they replenish their budgets and handle sporadic jobs.

### Slack Stealing

- Slack stealing is a more sophisticated approach that exploits the available slack times of periodic and sporadic jobs to complete aperiodic jobs early. Slack time is the amount of time that a job can be delayed without missing its deadline. Slack stealing algorithms monitor the slack times of periodic and sporadic jobs and dynamically adjust the priorities of aperiodic jobs to execute them when there is enough slack time. This way, slack stealing algorithms can improve the responsiveness of aperiodic jobs, while still ensuring the schedulability of periodic and sporadic jobs.
- Slack stealing algorithms require online computation of slack times, which can be costly and complex. There are different types of slack stealing algorithms, such as total slack stealing, dynamic slack stealing, hybrid slack stealing, etc., that differ in how they compute and distribute slack times and handle sporadic jobs.

## Scheduling Aperiodic and Sporadic jobs in Clock Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to handle the unpredictability of their arrival times and execution times. Since the schedule is pre-computed offline, it cannot accommodate the dynamic behavior of aperiodic and sporadic jobs.
- There are two main approaches to schedule aperiodic and sporadic jobs in clock driven systems: overloading and sporadic servers.

### Overloading

- Overloading is a simple and intuitive approach that assigns a fixed time slot to aperiodic jobs and executes them in a first-come first-served order. If an aperiodic job arrives when the time slot is occupied by another aperiodic job, it is queued until the next time slot. This ensures that aperiodic jobs do not interfere with the schedule of periodic jobs, but it also results in poor responsiveness of aperiodic jobs, especially when the time slot is too small or too infrequent.
- Overloading can be improved by using a priority queue, which assigns priorities to aperiodic jobs based on some criteria, such as deadline



# Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of one computer system available to other computer systems on a network. Resource sharing can improve the efficiency, performance, and reliability of distributed systems by allowing multiple users and applications to access and utilize the same resources.

Some examples of resources that can be shared are:

- Files and directories: Users can store, retrieve, and modify data on remote file systems as if they were local.
- Printers and scanners: Users can send documents to print or scan on remote devices without having to physically connect them to their own computers.
- CPU and memory: Users can run programs or processes on remote computers that have more processing power or memory than their own computers.
- Software and applications: Users can access and use software and applications that are installed on remote computers without having to install them on their own computers.
- Databases and web servers: Users can query and update data on remote databases or access web pages and services hosted on remote web servers.

Resource sharing can be implemented in different ways depending on the network architecture, the type of resources, and the level of transparency and security required. Some common methods of resource sharing are:

- File transfer: Users can copy files from one computer to another using protocols such as FTP, SCP, or HTTP.
- Remote login: Users can log in to a remote computer and execute commands or run programs using protocols such as SSH, Telnet, or RDP.
- Remote procedure call: Users can invoke procedures or functions on a remote computer and receive the results using protocols such as RPC, SOAP, or REST.
- Distributed file system: Users can access and manipulate files and directories on a remote computer as if they were local using protocols such as NFS, SMB, or HDFS.
- Distributed object system: Users can access and manipulate objects on a remote computer as if they were local using protocols such as CORBA, RMI, or DCOM.
- Distributed database system: Users can access and manipulate data on a remote database as if it were local using protocols such as SQL, ODBC, or JDBC.
- Distributed web system: Users can access and manipulate web pages and services on a remote web server as if they were local using protocols such as HTTP, HTTPS, or SOAP.



# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, or a peripheral device .
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for a resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the tasks .
- RAC can be classified into two categories: non-preemptive and preemptive .
  - Non-preemptive RAC means that once a task acquires a resource, it cannot be preempted by another task until it releases the resource .
  - Preemptive RAC means that a task can be preempted by another task while holding a resource, but the resource is not released until the preempted task resumes and finishes its critical section .
- Some examples of RAC protocols are:
  - Non-preemptive protocols: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive protocols: Multiprocessor Priority Ceiling Protocol (MPCP), Multiprocessor Stack Resource Policy (MSRP), Preemptive Priority Inheritance Protocol (PPIP), etc .



# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that contains shared variables or resources that need to be synchronized to maintain the consistency of data.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- Non-preemptive critical sections have the following properties :
  - When a job requests a resource, it is always allocated the resource.
  - When a job holds any resource, it executes at a priority higher than the priorities of all other jobs.
  - Because no job is ever preempted when it holds any resource, deadlock can never occur.
- Non-preemptive critical sections have some advantages and disadvantages :
  - Advantages:
    - Simplicity: no need for complex synchronization mechanisms or protocols.
    - Efficiency: no overhead of context switching or blocking.
    - Safety: no possibility of deadlock or priority inversion.
  - Disadvantages:
    - Conservativeness: a job may hold a resource longer than necessary, preventing other jobs from accessing it.
    - Unfairness: a job may be delayed indefinitely by higher-priority jobs that keep requesting the same resource.
    - Non-optimality: the worst-case response time of a job may be increased by the non-preemptive execution of critical sections.



# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems that involve shared resources and preemptive scheduling.
- The goal of these protocols is to prevent or minimize unbounded priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a resource needed by the high-priority task.
- Priority inversion can cause deadline misses, reduced system utilization, and increased response times.

## Priority-Inheritance Protocol

- The basic idea of the priority-inheritance protocol is that when a high-priority task is blocked by a low-priority task that holds a resource, the low-priority task inherits the priority of the high-priority task until it releases the resource.
- This way, the low-priority task can finish its critical section faster and unblock the high-priority task, reducing the blocking time.
- The priority-inheritance protocol can be implemented using a priority queue for each resource, where the highest-priority task that requests the resource is at the head of the queue.
- When a task requests a resource, it checks the queue and if it is empty, it acquires the resource and becomes the owner of the queue. If the queue is not empty, it appends itself to the queue and blocks until the resource is available.
- When a task releases a resource, it removes itself from the queue and restores its original priority. If the queue is not empty, it transfers the ownership of the queue and the resource to the next task in the queue, and boosts its priority to the highest priority of any task in the queue.
- The priority-inheritance protocol guarantees that the blocking time of a task is bounded by the duration of the longest critical section of any lower-priority task that shares a resource with it.
- However, the priority-inheritance protocol has some drawbacks, such as:
  - It can cause chained blocking, where a medium-priority task is blocked by a low-priority task that inherits the priority of a high-priority task, and the high-priority task is blocked by another task that holds a different resource.
  - It can cause multiple priority inversions, where a high-priority task is blocked by a low-priority task that holds a resource, and then the low-priority task is preempted by another high-priority task that does not need the resource.
  - It can cause unnecessary priority boosting, where a low-priority task inherits the priority of a high-priority task that requests a resource, but the high-priority task is blocked by another task that holds a different resource.

## Priority-Ceiling Protocol

- The basic idea of the priority-ceiling protocol is that each resource is assigned a priority ceiling, which is the highest priority of any task that can access the resource.
- A task can acquire a resource only if its priority is higher than the priority ceiling of all the resources currently held by other tasks.
- This way, the priority-ceiling protocol prevents a task from blocking a higher-priority task that needs a different resource, and avoids chained blocking and multiple priority inversions.
- The priority-ceiling protocol can be implemented using a system ceiling, which is the highest priority ceiling of all the resources currently held by any task, and a local ceiling, which is the highest priority ceiling of all the resources that a task can access.
- When a task requests a resource, it checks the system ceiling and if it is lower than its priority, it acquires the resource and raises the system ceiling to the priority ceiling of the resource. If the system ceiling is higher than its priority, it blocks until the system ceiling is lower than its priority.
- When a task releases a resource, it lowers the system ceiling to the highest priority ceiling of all the resources still held by any task. If the system ceiling is lower than the local ceiling of the task, it restores its original priority. If the system ceiling is higher than the local ceiling of the task, it boosts its priority to the system ceiling.
- The priority-ceiling protocol guarantees that the blocking time of a task is bounded by the duration of the shortest critical section of any lower-priority task that shares a resource with it.
- However, the priority-ceiling protocol has some drawbacks, such as:
  - It can cause avoidance blocking, where a task is denied access to a free resource because the system ceiling is higher than its priority, and the resource is held by a lower-priority task that does not need it.
  - It can cause unnecessary priority boosting, where a task inherits the system ceiling even



# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked until the resource is released by the current owner .
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the maximum blocking time for a job is equal to the worst-case execution time of the highest priority job that can access any of the resources needed by the blocked job .
- SBPCP also prevents deadlock by ensuring that a job cannot request a resource that is already held by a lower priority job, and that a job cannot request a resource that has a lower ceiling priority than any of the resources it already holds .
- SBPCP is suitable for systems that have a fixed set of resources and a known set of jobs that can access them. It requires a priori knowledge of the ceiling priorities of the resources and the resource requests of the jobs .
- SBPCP is also known as the Original Ceiling Priority Protocol (OCPP) or the Highest Locker Protocol (HLP).



# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- This ensures that a higher priority task will not be blocked by a lower priority task that holds a resource .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a priority queue or a sorted list to store the tasks and their priorities, and by using a table or a map to store the resources and their priority ceilings .
- Whenever a task requests a resource, we check if its priority is higher than the system ceiling, and if so, we grant the resource and update the system ceiling .
- Whenever a task releases a resource, we update the priority ceiling of the resource and the system ceiling .
- The priority ceiling protocol can prevent deadlock and unbounded priority inversion in dynamic priority systems, but it may introduce some overhead in updating the priority ceilings and the system ceiling .
- The priority ceiling protocol can also be applied to static priority systems, where the priority ceilings and the system ceiling do not change over time .
- There are two variants of the priority ceiling protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- The difference between them is that in OCPP, a task inherits the priority ceiling of the resource only when it is blocked by a lower priority task that holds the resource, while in ICPP, a task inherits the priority ceiling of the resource as soon as it locks the resource.
- The worst-case behaviour of the two variants is identical from a scheduling viewpoint, but ICPP may reduce the number of context switches and the blocking time of tasks.



# Preemption Ceiling Protocol for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Preemption ceiling protocol (PCP) is a job task synchronization protocol in a real-time system that is better than priority inheritance protocol in many ways.
- PCP assigns a priority ceiling to each shared resource, which is the highest priority of any task that can access that resource .
- PCP prevents a task from accessing a resource if its priority is lower than the priority ceiling of any resource currently locked by another task .
- PCP avoids priority inversion, deadlock, and chained blocking by ensuring that a task can be preempted only by a higher priority task that does not need any of the resources locked by the preempted task  .
- PCP can be implemented in two ways: static PCP and dynamic PCP.
  - Static PCP assigns a fixed priority ceiling to each resource based on the worst-case scenario, which is the highest priority of any task that may request that resource.
  - Dynamic PCP assigns a variable priority ceiling to each resource based on the actual scenario, which is the priority of the task that currently holds the resource.
- PCP can be extended to support preemption threshold scheduling (PTS), which is a technique that allows a task to specify a lower priority level at which it can be preempted by other tasks.
  - PTS enables a scalable real-time system design by reducing the number of preemptions and context switches.
  - PTS requires a dual ceiling protocol (DCP), which combines the priority ceiling and the preemption threshold of each resource to determine the blocking and preemption conditions for each task.
  - DCP prevents long priority inversion and maintains consistent object states in object-oriented real-time systems.



# Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The simplest resource access control protocol is to assign the highest priority to the job that acquires a resource and make it non-preemptable. However, this protocol has poor timing performance, as every job can be blocked by every lower-priority job with a critical section, even if there is no resource conflict.
- A better resource access control protocol is to use the priority-ceiling protocol or the preemption-ceiling protocol, which are extensions of the priority-inheritance protocol for single-unit resources.
- The priority-ceiling protocol assigns a priority ceiling to each resource, which is the highest priority of any job that may lock that resource. A job can lock a resource only if its priority is higher than the priority ceilings of all the resources currently locked by other jobs. This prevents deadlock and reduces blocking.
- The preemption-ceiling protocol assigns a preemption ceiling to each resource, which is the priority of the highest-priority job that may lock that resource. A job can lock a resource only if it is currently executing at the highest priority level. When a job locks a resource, its priority is raised to the preemption ceiling of that resource. This also prevents deadlock and reduces blocking.
- Both the priority-ceiling protocol and the preemption-ceiling protocol can be applied to multiple-unit resources by treating each unit of a resource as a separate resource with the same priority ceiling or preemption ceiling.



# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs or transactions in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in inconsistent or incorrect data values.
- To ensure data consistency and correctness, concurrent accesses to data objects must be controlled by using some concurrency control protocols or algorithms.
- Concurrency control protocols or algorithms aim to prevent or resolve conflicts among concurrent accesses to data objects, while satisfying the timing constraints of the jobs or transactions.
- There are different types of concurrency control protocols or algorithms, such as locking-based, timestamp-based, optimistic, and hybrid protocols.
- Locking-based protocols use locks to grant or deny access to data objects. A job or transaction must acquire a lock on a data object before accessing it, and release the lock after finishing the access. Locks can be exclusive or shared, depending on the type of access (read or write).
- Timestamp-based protocols use timestamps to order the accesses to data objects. A job or transaction is assigned a timestamp when it is activated, and its accesses to data objects are compared with the timestamps of other concurrent accesses. If the timestamp order is violated, the access is aborted or restarted.
- Optimistic protocols assume that conflicts among concurrent accesses to data objects are rare, and allow the accesses to proceed without any control. However, before committing the changes to the data objects, the accesses are validated to check for any conflicts. If a conflict is detected, the access is aborted or restarted.
- Hybrid protocols combine the features of locking-based, timestamp-based, and optimistic protocols to achieve better performance and flexibility. For example, a protocol may use locks for some data objects and timestamps for others, or use optimistic validation for some accesses and locking or timestamping for others.



# Unit 4 - Real Time Communication

- Real time communication (RTC) is a term used to refer to any live telecommunications that occur without transmission delays or with negligible latency.
- RTC data and messages are not stored between transmission and reception.
- RTC is necessary to support real time guarantees of real time computing, which is a type of computing that requires a system to respond to events within a specified time frame.
- RTC can be achieved using various software protocols and communication hardware media that give real time guarantees.
- Some examples of RTC applications are:
  - Voice over IP (VoIP), which allows users to make phone calls over the internet.
  - Video conferencing, which enables users to see and hear each other in real time.
  - Instant messaging, which allows users to exchange text, images, audio, and video messages in real time.
  - Online gaming, which allows users to interact with each other and the game environment in real time.
  - Streaming media, which allows users to access and play audio and video content in real time.



# Basic Concepts in Real time Communication

Real time communication (RTC) is a category of software protocols and communication hardware media that gives real-time guarantees, which is necessary to support real-time guarantees of real-time computing. Real-time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.

Some of the basic concepts in real time communication are:

- **Real time**: Real time means that the communication happens in the same time frame as the events being communicated. There is no significant delay or latency between the sender and the receiver of the information . Real time communication is synonymous with live communication.
- **Latency**: Latency is the time it takes for a message or a packet of data to travel from the source to the destination. Latency is measured in milliseconds (ms) and affects the quality and performance of real time communication. Low latency means that the communication is fast and responsive, while high latency means that the communication is slow and laggy .
- **Bandwidth**: Bandwidth is the amount of data that can be transferred per unit of time over a communication channel. Bandwidth is measured in bits per second (bps) and affects the capacity and speed of real time communication. High bandwidth means that the communication can support more data and higher quality, while low bandwidth means that the communication can support less data and lower quality .
- **Jitter**: Jitter is the variation in latency over time. Jitter is caused by network congestion, interference, routing changes, or other factors that affect the stability and consistency of the communication channel. Jitter can result in packet loss, out-of-order delivery, or delayed delivery of data, which can degrade the quality and reliability of real time communication .
- **Reliability**: Reliability is the ability of the communication system to deliver data correctly and completely without errors or losses. Reliability is affected by the characteristics of the communication channel, such as noise, interference, or congestion, as well as the protocols and mechanisms used to ensure data integrity, such as error detection, error correction, or retransmission .
- **Synchronization**: Synchronization is the coordination of the timing and order of data transmission and reception among multiple communication nodes. Synchronization is important for real time communication that involves multiple sources or destinations, such as video conferencing, online gaming, or distributed computing. Synchronization can be achieved by using common clocks, timestamps, or sequence numbers to align the data streams .



# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: **Hard Real-Time (HRT)** and **Soft Real-Time (SRT)**.
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- A **hard real-time communication system** is a system that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable loss  . For example, a nuclear reactor control system, a flight control system, or a pacemaker system are hard real-time communication systems .
- A **soft real-time communication system** is a system that can tolerate some deadline misses, but still tries to achieve the best possible performance  . For example, a video conferencing system, a multimedia streaming system, or a web server are soft real-time communication systems .
- Hard real-time communication systems are **deterministic** in nature, meaning they can guarantee the worst-case execution time and response time for each task .
- Soft real-time communication systems are **probabilistic** in nature, meaning they can estimate the average or expected execution time and response time for each task, but not the worst-case .
- Hard real-time communication systems require **strict** scheduling algorithms and protocols that can ensure the timely delivery of messages and the avoidance of conflicts and deadlocks .
- Soft real-time communication systems can use **relaxed** scheduling algorithms and protocols that can adapt to the dynamic changes in the workload and the network conditions .
- Hard real-time communication systems have **higher** priority, reliability, and safety requirements than soft real-time communication systems .
- Soft real-time communication systems have **higher** flexibility, scalability, and efficiency requirements than hard real-time communication systems .



# Model of Real Time Communication

- Real time communication (RTC) is any live telecommunications method in which all users can interact in a live capacity, with negligible latency  .
- RTC can involve different types of data, such as voice, video, text, images, etc.
- RTC can be implemented using various technologies, such as landlines, mobile phones, VoIP, WebRTC, etc.
- RTC can be used for various applications, such as online gaming, video conferencing, telemedicine, remote education, etc.
- RTC can be modeled using different parameters, such as traffic, throughput, delay, jitter, etc.

## Real Time Traffic Model

- The real time traffic means isochronous or synchronous traffic, consisting stream of message that are generated by their sources and delivered to their respective destination on continuous basis.
- The traffic includes the periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals, such as sensor data, audio samples, etc.
- Aperiodic messages are generated at irregular intervals, such as alarms, events, etc.
- Sporadic messages are generated at random intervals, such as user inputs, commands, etc.
- In real time traffic model, each message (Mi) can be characterized by tuples of inter-packet spacing (Pi), message length (ei), reception deadline (Di) as below:

  Mi = (pi, ei, Di)

- This traffic model is called peak rate model in real time communication.

## Throughput, Delay and Jitter

- Throughput is the amount of data that can be transmitted or received per unit time in a communication channel.
- Throughput can be affected by factors such as bandwidth, congestion, errors, etc.
- Delay is the time taken for a message to travel from the source to the destination in a communication channel.
- Delay can be affected by factors such as propagation, transmission, processing, queuing, etc.
- Jitter is the variation in delay for different messages in a communication channel.
- Jitter can be affected by factors such as network load, routing, buffering, etc.
- Throughput, delay and jitter are important metrics for evaluating the performance and quality of service (QoS) of real time communication.



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Priority-based service disciplines can provide different delay and jitter bounds, bandwidth guarantees, and fairness properties for different classes of packets  .
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns a weight to each class of packets and serves them in a circular order according to their weights  .
- WRR does not require a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of the scheduler.
- WRR can guarantee the minimum bandwidth for each class of packets, but it cannot guarantee the maximum delay or jitter bound for each class of packets.
- WRR can also suffer from the problem of head-of-line blocking, where a large packet at the head of a queue can delay the transmission of smaller packets in the same queue.
- To overcome the limitations of WRR, some variations and extensions of WRR have been proposed, such as:
  - Weighted fair queuing (WFQ), which serves packets in proportion to their weights and lengths, and can provide delay and jitter bounds for each class of packets.
  - Rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server, and can guarantee the delay jitter bound and satisfy diverse delay requirements for each class of packets.
  - Class-based weighted fair queuing (CBWFQ) and weighted fair priority queuing (WFPQ), which combine the features of WFQ and priority queuing, and can provide different service levels for different classes of packets.



# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel. They play an important role in the development of both wired and wireless networks.
- Broadcast networks are networks where a single transmission can reach all the nodes in the network. They are useful for applications such as real-time communication, data dissemination, and network management.
- MAC protocols for broadcast networks can be classified according to the access strategy employed. There are two main categories: probabilistic contention protocols and deterministic scheduling protocols.
- Probabilistic contention protocols utilize direct, asynchronous competition between neighboring nodes to determine which node will transmit next. They are simple, distributed, and adaptive, but they suffer from collisions, hidden terminal problem, and unbounded access delay. Examples include Aloha, CSMA, and IEEE 802.11  .
- Deterministic scheduling protocols allocate transmission slots to nodes in advance, based on some criteria such as priority, fairness, or demand. They avoid collisions, provide bounded access delay, and support quality of service, but they require synchronization, coordination, and overhead. Examples include TDMA, FDMA, and CDMA  .
- Some MAC protocols combine both probabilistic and deterministic approaches to achieve a trade-off between performance and flexibility. For example, ABROAD is an adaptive MAC protocol for reliable broadcast in wireless networks that incorporates a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay .



# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams    .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver. It is generally used by the receiver side for the fast delivery of the transmission packets from the sender to the receiver.
- RSVP uses the integrated services model, which defines two QoS classes: guaranteed service and controlled-load service .
- Guaranteed service provides a firm bound on end-to-end delay and ensures that packets are delivered in order with minimal loss .
- Controlled-load service provides a QoS closely approximating the QoS that same flow would receive from an unloaded network element, but uses less resources than guaranteed service .
- RSVP uses soft state, which means that the reservations are periodically refreshed and automatically removed if not refreshed .
- RSVP messages are sent as IP datagrams with protocol number 46. There are four types of RSVP messages: PATH, RESV, PATHERR, and RESVERR .
- PATH messages are sent by the sender to establish the route and QoS requirements for the data flow. They carry information such as sender IP address, destination IP address, data flow identifier, QoS class, and traffic specification .
- RESV messages are sent by the receiver to request a resource reservation along the path established by the PATH messages. They carry information such as receiver IP address, data flow identifier, QoS class, and reservation specification .
- PATHERR and RESVERR messages are sent by intermediate nodes or receivers to report errors or failures in the reservation process. They carry information such as error code, error value, and error node .
- RSVP supports both unicast and multicast communication. For unicast, there is a single sender and a single receiver. For multicast, there is a single sender and multiple receivers. RSVP uses multicast routing protocols such as DVMRP, MOSPF, and PIM to establish and maintain multicast group membership and routing .
- RSVP is designed to be scalable, robust, and flexible. It can coexist with other protocols and applications that do not use RSVP. It can also adapt to changes in network topology, traffic load, and QoS requirements .



# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed to optimize the average performance and resource utilization, but not the worst-case performance or predictability.
- An RTOS typically has the following features :
  - Real-time multithreading: The ability to create and manage multiple tasks or threads that can run concurrently and independently, each with its own priority and deadline.
  - Inter-thread communication and synchronization: The ability to exchange data and signals between threads, and to coordinate their execution using mechanisms such as semaphores, mutexes, message queues, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, and to prevent memory fragmentation and leaks.
  - Interrupt handling: The ability to respond to external or internal events that require immediate attention, such as hardware inputs or timers, and to resume the normal execution afterwards.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, displays, and network interfaces, and to provide a uniform and abstracted access to them.
- Some examples of applications that use RTOS are industrial control, telephone switching, flight control, and real-time simulations.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can perform transactions and queries with real-time constraints.
- A real-time constraint is a requirement that a database operation must be completed within a specified time interval, or else it is considered invalid or obsolete.
- A RTDB is different from a conventional database, such as Oracle or MySQL, which are designed to optimize the throughput and consistency, but not the timeliness or freshness of the data.
- A RTDB typically has the following features:
  - Real-time transactions: The ability to execute database operations, such as insert, update, delete, and select, with deadlines and priorities, and to abort or restart them if they miss their deadlines or encounter conflicts.
  - Real-time queries: The ability to retrieve data from the database with temporal constraints, such as freshness, validity, and accuracy, and to handle data inconsistencies or uncertainties.
  - Real-time data: The ability to store and manage data that have temporal properties, such as timestamps, expiration dates, and versions, and to reflect the changes in the external environment or the internal state of the system.
  - Real-time concurrency control: The ability to coordinate the access and modification of the data by multiple transactions or queries, and to prevent or resolve data conflicts, such as deadlock, starvation, or inconsistency.
- Some examples of applications that use RTDB are stock market, air traffic control, online gaming, and sensor networks.



# Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load or external events. An RTOS has two key features: predictability and determinism.

Some of the features of an RTOS are:

- **Small and fast**: An RTOS is designed to occupy very less memory and consume fewer resources, as it has to run on embedded devices with limited hardware capabilities. An RTOS is also optimized to execute tasks quickly and efficiently, with minimal overhead and latency.
- **Responsive and deterministic**: An RTOS can respond to events or interrupts within a tight time boundary, without missing any deadlines or compromising the quality of service. An RTOS can also ensure that the same task will always take the same amount of time to complete, regardless of the system state or other tasks.
- **Co-operative or pre-emptive scheduling**: An RTOS can use different scheduling algorithms to manage the execution of tasks, depending on the application requirements. Co-operative scheduling means that a task will run until it is completed or it voluntarily yields the CPU to another task. Pre-emptive scheduling means that a task can be interrupted by a higher priority task at any time, and resume when the higher priority task is finished.
- **Priority-based or time-slice scheduling**: An RTOS can also use different criteria to assign priorities to tasks, depending on the application requirements. Priority-based scheduling means that a task with a higher priority value will always run before a task with a lower priority value. Time-slice scheduling means that a task will run for a fixed amount of time, and then switch to another task in a round-robin fashion.
- **Task synchronization and communication**: An RTOS can provide various mechanisms to synchronize and communicate between tasks, such as semaphores, mutexes, message queues, event flags, etc. These mechanisms can help to avoid race conditions, deadlocks, and data inconsistency, as well as to coordinate the execution of tasks.
- **Memory management and protection**: An RTOS can provide different levels of memory management and protection, depending on the application requirements. Memory management can include dynamic allocation and deallocation, memory pools, memory fragmentation, etc. Memory protection can include memory isolation, access control, fault detection, etc.
- **Device drivers and middleware**: An RTOS can provide device drivers and middleware to interface with various hardware and software components, such as sensors, actuators, communication protocols, file systems, databases, etc. These components can help to abstract the low-level details and provide a uniform and consistent interface to the application layer.



# Time Services

Time services are essential components of real-time systems that provide the following functions :

- **Timeliness**: Time services ensure that the system can produce the expected results within a defined deadline, which is a critical requirement for real-time systems. Timeliness can be classified into two types: hard and soft. Hard timeliness means that missing the deadline will cause a system failure, while soft timeliness means that the system can still function with degraded performance or quality.
- **Time synchronization**: Time services enable the coordination of independent clocks and events across different devices or components of the system, which is necessary for distributed or parallel real-time systems. Time synchronization can be achieved by using various protocols or algorithms, such as the Network Time Protocol (NTP), the Precision Time Protocol (PTP), or the Lamport's logical clocks.
- **Time measurement**: Time services provide the means to measure the elapsed time or the current time of the system, which is useful for scheduling, monitoring, or debugging purposes. Time measurement can be done by using hardware or software timers, counters, or clocks, depending on the accuracy and resolution needed.
- **Time management**: Time services allow the system to control the flow of time or the execution of tasks, which is important for managing the resources and priorities of the system. Time management can be done by using various techniques, such as preemptive or non-preemptive scheduling, deadline-based or priority-based scheduling, or rate-monotonic or earliest-deadline-first scheduling.

Some examples of real-time systems that use time services are:

- **Flight control systems**: These systems use time services to ensure the safety and stability of the aircraft, by coordinating the sensors, actuators, and controllers, and by executing the control algorithms within the required deadlines.
- **Real-time monitors**: These systems use time services to collect and analyze the data from various sources, such as sensors, cameras, or networks, and to provide timely feedback or alerts to the users or other systems.
- **Gaming systems**: These systems use time services to provide a realistic and immersive experience to the players, by synchronizing the graphics, audio, and physics, and by measuring and managing the latency and frame rate.



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like Unix strives to provide good average performance, for a RTOS, correct timing is the key feature.
- Unix is not a RTOS by default, but it can be modified or extended to provide some real-time capabilities, such as:
  - Using real-time extensions, such as POSIX.1b or POSIX.4, which define a set of interfaces and services for real-time applications.
  - Using real-time patches, such as RTLinux or RTAI, which add a thin layer between the hardware and the Linux kernel, allowing real-time tasks to run in kernel space with minimal interference from the non-real-time tasks.
  - Using real-time libraries, such as Xenomai or PREEMPT_RT, which provide a user-space API for real-time applications, and a kernel module that handles the scheduling and synchronization of the real-time tasks.
- However, using Unix as a RTOS also poses some challenges, such as:
  - The complexity and size of the Unix kernel, which may introduce unpredictability and latency in the system.
  - The lack of standardization and compatibility among different real-time extensions, patches, and libraries, which may limit the portability and interoperability of the real-time applications.
  - The trade-off between performance and functionality, which may require careful tuning and testing of the system parameters and configuration.
- Therefore, using Unix as a RTOS depends on the specific requirements and constraints of the real-time application, and the availability and suitability of the real-time solutions for the Unix platform.



# POSIX Issues

- POSIX stands for Portable Operating System Interface, which is a set of standards that define how an application should interact with an operating system.
- POSIX aims to achieve portability, interoperability, and compatibility among different operating systems, especially UNIX and its variants.
- POSIX also covers extensions for real-time operating systems, which are systems that have strict timing constraints and need to respond to events within predictable and bounded time frames.
- POSIX real-time extensions include specifications for:
  - Timers, clocks, and calendar functions, which provide high-resolution and monotonic time measurements and operations.
  - Signals, which are asynchronous notifications of events or conditions that can interrupt or resume a process or thread.
  - Semaphores, which are synchronization mechanisms that control access to shared resources or coordinate activities among processes or threads.
  - Message queues, which are communication mechanisms that allow processes or threads to exchange data in a FIFO (first-in, first-out) manner.
  - Shared memory, which is a memory region that can be accessed by multiple processes or threads for data exchange or interprocess communication.
  - Memory locking, which is a mechanism that prevents a memory region from being swapped out to disk or relocated by the operating system.
  - Priority scheduling, which is a mechanism that assigns different levels of importance or urgency to processes or threads and determines the order of their execution.
  - Real-time signals, which are extensions of the standard signals that have higher priority and can carry additional information.
  - Timed waits, which are extensions of the standard wait functions that allow processes or threads to block until a specified time or a signal occurs.
  - Asynchronous I/O, which is a mechanism that allows processes or threads to perform input/output operations without blocking or waiting for their completion.
  - Memory mapping, which is a mechanism that maps a file or a device into a memory region that can be accessed by processes or threads.
  - Threads, which are independent units of execution that share the same address space and resources of a process.
  - Thread synchronization, which is a mechanism that coordinates the activities and interactions of multiple threads within a process.
  - Thread cancellation, which is a mechanism that allows a thread to be terminated by another thread or by itself.
  - Thread-specific data, which is a mechanism that allows a thread to store and retrieve data that is local to itself and not shared with other threads.
  - Thread scheduling, which is a mechanism that determines the order and duration of thread execution within a process.
  - Sporadic server, which is a mechanism that allows a thread to execute periodically with a specified minimum interarrival time and a specified execution budget.
- POSIX real-time issues include:
  - The trade-off between portability and performance, as some POSIX features may not be supported or optimized by some operating systems or hardware platforms.
  - The trade-off between functionality and complexity, as some POSIX features may introduce additional overhead, latency, or unpredictability to the system.
  - The trade-off between standardization and innovation, as some POSIX features may not reflect the latest advances or best practices in real-time system design and implementation.
  - The trade-off between compatibility and flexibility, as some POSIX features may impose constraints or limitations on the system configuration or behavior.



# Characteristic of Temporal Data

- Temporal data is the data that is **valid only for a prescribed time** and becomes **invalid or obsolete** after a certain period of time .
- Temporal data can represent **time in some form**, such as dates, timestamps, intervals, durations, or periods, and allow other data to be placed in a **chronological sequence** or to be analyzed **chronologically**.
- Temporal data can have different **temporal aspects**, such as valid time, transaction time, or decision time, depending on the **application domain** and the **purpose of the data**.
- Valid time is the time period during or event time at which a fact is **true in the real world**. For example, the date of birth of a person is a valid time attribute.
- Transaction time is the time period during or event time at which a fact is **stored in the database**. For example, the date of entry of a record in a database is a transaction time attribute.
- Decision time is the time period during or event time at which a fact is **decided or acted upon**. For example, the date of approval of a loan application is a decision time attribute.
- Temporal data can be **uni-temporal**, **bi-temporal**, or **tri-temporal**, depending on the number of temporal aspects involved.
- Uni-temporal data has **one temporal aspect**, either valid time, transaction time, or decision time. For example, a weather report that records the temperature at a given location and time is uni-temporal data with valid time aspect.
- Bi-temporal data has **two temporal aspects**, either valid time and transaction time, or valid time and decision time. For example, a customer account that records the balance and the date of change, as well as the date of entry in the database, is bi-temporal data with valid time and transaction time aspects.
- Tri-temporal data has **three temporal aspects**, valid time, transaction time, and decision time. For example, a legal document that records the facts, the dates of validity, the dates of storage, and the dates of decision, is tri-temporal data with all three temporal aspects.



# Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not reflect the current state of the physical environment. This can happen due to the delay in sensing, processing, and updating the data.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other. This can happen due to the concurrency and interference of multiple transactions that access and update the data.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the occurrence of some events or conditions in the physical environment or the database. Triggered updates can reduce data staleness by updating the data as soon as possible.
  - Absolute validity, which is a temporal constraint that specifies the maximum allowable age of the data that can be read by a transaction. Absolute validity can prevent transactions from reading stale data by checking the timestamp of the data.
  - Relative validity, which is a temporal constraint that specifies the maximum allowable difference between the values of two data items that are related to each other. Relative validity can prevent transactions from reading inconsistent data by comparing the values of the data items.
  - Serialization, which is a concurrency control technique that ensures that the execution of multiple transactions is equivalent to some sequential order. Serialization can prevent data inconsistency by avoiding conflicts and interference among transactions.
  - Priority assignment, which is a scheduling technique that assigns different priorities to different transactions based on their importance and urgency. Priority assignment can ensure that the most critical transactions are executed before the less critical ones and meet their deadlines.



# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic concurrency control are two-phase locking, timestamp ordering, and priority inheritance protocol.
  - Optimistic concurrency control allows conflicts to occur and resolves them after they are detected. Examples of optimistic concurrency control are multiversion concurrency control, validation-based concurrency control, and optimistic locking.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as performance considerations, correctness criteria, and transaction models.
  - Performance considerations for RTS include meeting deadlines, minimizing blocking time, and maximizing concurrency.
  - Correctness criteria for RTS include serializability, recoverability, and temporal consistency.
  - Transaction models for RTS include periodic, aperiodic, sporadic, and soft transactions.
- Concurrency control techniques for RTS should be tailored to the specific characteristics and requirements of the application domain, such as automotive, aerospace, robotics, energy, transportation, and finance.



# Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases have to meet certain requirements, such as timeliness, concurrency, consistency, reliability, and availability.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have to guarantee strict deadlines for every transaction, and any missed deadline is considered a failure.
  - Soft real-time databases have to meet most of the deadlines, but some occasional deadline misses are acceptable.
- Some examples of commercial real-time databases are:
  - Raima Database Manager (RDM): a cross-platform, embedded, in-memory, SQL, and NoSQL database that supports hard and soft real-time applications.
  - Google Cloud Firestore: a scalable, serverless, cloud-native NoSQL database that supports soft real-time applications with low latency and high availability.
  - CoStar: a leading provider of commercial real estate information, analytics, and online marketplaces that supports soft real-time applications with historical and current data.

