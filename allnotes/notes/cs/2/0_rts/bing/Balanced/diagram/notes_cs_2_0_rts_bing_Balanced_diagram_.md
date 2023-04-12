

# Real Time System

A real time system is an information processing system that can respond to events within predictable and specific time constraints . A real time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization). A real time system can be classified into two types based on the timing constraints: hard real time system and soft real time system.

- A hard real time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur . For example, a flight control system, a nuclear reactor control system, or a pacemaker are hard real time systems.
- A soft real time system can miss its deadline occasionally with some acceptably low probability. For example, a video streaming system, a voice over IP system, or a web server are soft real time systems.

Real time systems are used in a variety of industries and applications, such as process control systems, machine vision, robotics, medical imaging, video wall, and industrial controls applications . Real time systems require special hardware and software components that can handle the real time requirements, such as real time operating systems, real time communication protocols, real time scheduling algorithms, and real time sensors and actuators .



## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
- Hard real time systems are systems that must meet all their deadlines, otherwise they may cause catastrophic failures or unacceptable losses. For example, a nuclear reactor control system or an air traffic control system are hard real time systems.
- Soft real time systems are systems that can tolerate some deadline misses, but the quality of service or the user satisfaction may degrade. For example, a video streaming system or a voice recognition system are soft real time systems.
- Real time systems can also be classified into two types based on the predictability of their events or inputs: periodic systems and aperiodic systems.
- Periodic systems are systems that have events or inputs that occur at regular intervals, such as sensor readings, clock ticks, etc. Periodic systems can be analyzed using techniques such as rate monotonic scheduling or earliest deadline first scheduling.
- Aperiodic systems are systems that have events or inputs that occur at irregular or unpredictable intervals, such as user commands, interrupts, faults, etc. Aperiodic systems can be analyzed using techniques such as sporadic server, polling server, or slack stealing.
- Real time systems face many challenges and trade-offs, such as limited resources, concurrency, synchronization, fault tolerance, security, etc. Real time systems must be designed, implemented, tested, and verified carefully to ensure their correctness and efficiency.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of definition for the notes of the unit 1 - introduction of real time system in the subject of real time system.

### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or stimuli within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or stimuli: periodic and aperiodic.
- A periodic event or stimulus is one that occurs at regular intervals, such as a sensor reading, a clock tick, or a heartbeat. A periodic event or stimulus has a known period, which is the time between two consecutive occurrences of the event or stimulus.
- An aperiodic event or stimulus is one that occurs irregularly or unpredictably, such as a user input, a network packet, or an interrupt. An aperiodic event or stimulus has an unknown or variable period, which is the time between two consecutive occurrences of the event or stimulus.
- A real time system can also be classified into two types based on the number of processors or cores: uniprocessor and multiprocessor.
- A uniprocessor system is a system that has only one processor or core, which executes all the tasks or processes of the system. A uniprocessor system can use different scheduling algorithms to manage the execution of the tasks or processes, such as rate monotonic, earliest deadline first, or round robin.
- A multiprocessor system is a system that has more than one processor or core, which can execute the tasks or processes of the system in parallel. A multiprocessor system can use different architectures to distribute the tasks or processes among the processors or cores, such as homogeneous, heterogeneous, symmetric, or asymmetric.



### Typical Real Time Applications

A real-time application (RTA) is an application that has strict time constraints on its performance and reliability. RTAs often interact with the physical world and must respond to events or inputs within predictable and specific time frames. RTAs can be classified into two types: hard real-time and soft real-time. Hard real-time applications have absolute deadlines that must be met, otherwise the system may fail or cause severe consequences. Soft real-time applications have preferred deadlines that should be met, but occasional delays are tolerable and do not compromise the system functionality.

Some examples of typical real-time applications are:

- **Video conferencing**: This is an application that allows users to communicate with each other through video and audio streams over the internet. Video conferencing requires real-time processing and transmission of multimedia data, as well as synchronization and quality of service (QoS) mechanisms to ensure smooth and natural interaction. Video conferencing is a soft real-time application, as some delays or losses of data packets may not affect the overall communication quality significantly.

- **Voice over Internet Protocol (VoIP)**: This is an application that enables users to make voice calls over the internet using digital signals. VoIP also requires real-time processing and transmission of audio data, as well as encryption and compression techniques to reduce bandwidth and enhance security. VoIP is a soft real-time application, as some delays or losses of data packets may cause some degradation of voice quality, but not render the call unintelligible.

- **Online gaming**: This is an application that allows users to play games with other users over the internet. Online gaming involves real-time rendering and simulation of graphics, physics, and sound, as well as network communication and synchronization among multiple players. Online gaming is a soft real-time application, as some delays or losses of data packets may affect the game performance and user experience, but not prevent the game from running.

- **Community storage applications**: These are applications that allow users to store and share data over the internet using distributed and decentralized systems. Community storage applications require real-time coordination and consistency among multiple nodes, as well as fault tolerance and security mechanisms to ensure data availability and integrity. Community storage applications are soft real-time applications, as some delays or losses of data packets may cause some temporary unavailability or inconsistency of data, but not result in permanent data loss or corruption.

- **Some e-commerce applications**: These are applications that allow users to buy and sell goods and services over the internet. Some e-commerce applications require real-time processing and verification of transactions, as well as encryption and authentication techniques to ensure data security and privacy. Some e-commerce applications are soft real-time applications, as some delays or losses of data packets may cause some inconvenience or dissatisfaction for the users, but not affect the validity or legality of the transactions.

- **Real-time operating system (RTOS)**: This is a system software that provides the basic functions and services for real-time applications. RTOS manages the hardware resources, such as CPU, memory, and I/O devices, and schedules the tasks and processes of the real-time applications according to their priorities and deadlines. RTOS also provides mechanisms for inter-task communication, synchronization, and exception handling. RTOS is a hard real-time application, as any delays or failures of the system functions or services may cause the real-time applications to miss their deadlines or malfunction.

- **Instant messaging (IM) applications**: These are applications that allow users to send and receive text, voice, or video messages over the internet. IM applications require real-time processing and transmission of multimedia data, as well as encryption and compression techniques to reduce bandwidth and enhance security. IM applications are soft real-time applications, as some delays or losses of data packets may cause some degradation of message quality, but not prevent the message from being delivered.

- **Team collaboration applications**: These are applications that allow users to work together on projects or tasks over the internet. Team collaboration applications require real-time processing and transmission of multimedia data, as well as synchronization and QoS mechanisms to ensure smooth and effective collaboration. Team collaboration applications are soft real-time applications, as some delays or losses of data packets may affect the collaboration quality and productivity, but not prevent the collaboration from taking place.

- **Digital control**: This is an application that uses a digital device, such as a microcontroller or a microprocessor, to control a physical system, such as a motor, a robot, or a plant. Digital control requires real-time sensing and actuation of the physical system, as well as real-time computation and implementation of the control algorithm. Digital



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must respond to events within a specified time interval, otherwise it may fail to meet its requirements or cause undesirable consequences.
- A real-time system can be classified into two types: hard real-time and soft real-time.
- A hard real-time system is a system that must meet its deadlines strictly, otherwise it may cause catastrophic failure or severe damage. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real-time system is a system that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real-time task is a unit of work that must be executed by a real-time system. A real-time task has three main attributes: release time, execution time, and deadline.
- The release time of a real-time task is the earliest time that the task is ready to be executed by the system. The release time may be periodic, aperiodic, or sporadic.
- A periodic task is a task that has a fixed release time interval, which is also called the period. For example, a task that is released every 10 milliseconds.
- An aperiodic task is a task that has a variable release time interval, which may depend on external events or user inputs. For example, a task that is released whenever a user presses a button.
- A sporadic task is a task that has a minimum release time interval, which is also called the minimum inter-arrival time. For example, a task that is released at least 5 milliseconds apart, but may be longer.
- The execution time of a real-time task is the amount of time that the task needs to complete its work. The execution time may be deterministic, probabilistic, or unknown.
- A deterministic task is a task that has a fixed execution time, which is also called the worst-case execution time. For example, a task that always takes 3 milliseconds to finish.
- A probabilistic task is a task that has a variable execution time, which follows a certain probability distribution. For example, a task that takes 2 milliseconds with 90% probability, and 4 milliseconds with 10% probability.
- An unknown task is a task that has an unpredictable execution time, which may depend on the input data, the system state, or the environment. For example, a task that takes different time to process different images.
- The deadline of a real-time task is the latest time that the task must finish its execution, otherwise it may miss its deadline. The deadline may be implicit, explicit, or constrained.
- An implicit deadline is a deadline that is equal to the release time of the next instance of the same task. For example, a periodic task with a period of 10 milliseconds and an execution time of 3 milliseconds has an implicit deadline of 10 milliseconds.
- An explicit deadline is a deadline that is specified separately from the release time and the period. For example, an aperiodic task with a release time of 15 milliseconds and an execution time of 4 milliseconds has an explicit deadline of 25 milliseconds.
- A constrained deadline is a deadline that is less than or equal to the release time of the next instance of the same task. For example, a periodic task with a period of 10 milliseconds and an execution time of 3 milliseconds has a constrained deadline of 8 milliseconds.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by the end of the week, i.e., by Sunday, 19 March 2023, 11:59 PM.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in a clear, concise, and accurate manner, using proper terminology and notation.
- The notes should be formatted according to the guidelines given in the syllabus, using markdown syntax.
- The notes should be submitted as a single file, named as `RTS_Unit1_Notes_YourName.md`, to the online platform specified by the instructor.
- The notes will be evaluated based on the following criteria:
  - Completeness and correctness of the content
  - Organization and clarity of the presentation
  - Adherence to the format and style requirements
  - Originality and creativity of the examples and illustrations
- The notes will carry 10% of the total marks for the subject of Real Time System.
- Late submissions will incur a penalty of 10% per day, up to a maximum of 50%.
- No submissions will be accepted after Friday, 24 March 2023, 11:59 PM.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system are known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system are known as Reliability Constraints.
- Performance Constraints are further divided into three types:
  - Delay Constraint: A delay constraint describes the minimum time interval between the occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between the occurrence of two consecutive events.
  - Duration Constraint: A duration constraint describes the maximum or minimum time interval for the execution of a task.
- Reliability Constraints are further divided into two types:
  - Synchronization Constraint: A synchronization constraint describes the order or precedence of events or tasks in a system.
  - Consistency Constraint: A consistency constraint describes the logical or temporal relationship between the states or values of variables in a system.
- A real-time system must satisfy both performance and reliability constraints to ensure the correct functioning of the system.
- A real-time system must also have the ability to produce the expected result by a specific deadline (timeliness) and the capability of agents to coordinate independent clocks and operate together in unison (time synchronization).
- An example of a real-time system with timing constraints is an air traffic control system, which must monitor and control the movements of aircrafts in a timely and reliable manner.



### Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- A hard real time system is also known as an immediate real time system .
- A hard real time system is usually found interacting at a low level with physical hardware, in embedded systems .
- Examples of hard real time systems are:
  - Nuclear power plant control systems 
  - Air traffic control systems 
  - Medical devices such as pacemakers and defibrillators 
  - Early video game systems such as the Atari 2600 and Cinematronics vector graphics 
- Characteristics of hard real time systems are:
  - The size of data and code is small and fixed 
  - The response time is in milliseconds or microseconds 
  - The peak load performance should be predictable and consistent 
  - The safety is critical and the system must be reliable and fault-tolerant  
- Challenges of hard real time systems are:
  - Meeting the strict timing constraints and ensuring correctness 
  - Handling concurrency and synchronization issues 
  - Managing limited resources and power consumption 
  - Testing and debugging the system in realistic scenarios



### Soft Real Time Systems

- A soft real time system is a system that has **flexible deadlines** for completing its tasks, meaning that missing some deadlines occasionally is **acceptable** and does not cause critical consequences .
- A soft real time system can **tolerate** some degree of **jitter**, which is the variation in the response time of the system.
- A soft real time system can run on **multiple cores** and impose **fewer restrictions** on applications than a hard real time system.
- A soft real time system can **adapt** to the **available resources** and **vary** the **quality of service** according to the **system load**.
- Examples of soft real time systems are **streaming audio-video**, **multimedia applications**, **online gaming**, **voice over IP**, etc.  .



### Reference Models for Real Time Systems

A reference model is a conceptual framework that defines the essential features and characteristics of a real time system. It helps to understand, analyze, design, and evaluate real time systems in a systematic and consistent way. A reference model is not a specific system design, but rather a general template that can be instantiated for different applications and domains.

There are different reference models for real time systems, depending on the level of abstraction, the scope of coverage, and the focus of attention. Some of the common reference models are:

- **Real-time Control System (RCS)**: This is a reference model architecture that combines real-time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis . It defines the types of functions needed in a real time intelligent control system, and how they relate to each other. RCS is suitable for many software-intensive, real time computing control problem domains, such as robotics, manufacturing, and aerospace.
- **Reference Model of Real-time Systems (RMRTS)**: This is a reference model that focuses on the timing behavior of the systems   . It is characterized by three elements: a workload model, a resource model, and a system model. The workload model specifies the application supported by the system, such as the set of tasks, jobs, and their parameters. The resource model describes the resources available in the system, such as the CPU, memory, network, and their types and relations. The system model defines the policies and mechanisms used by the system to manage the resources and the workload, such as the scheduling algorithm, the synchronization protocol, and the fault tolerance scheme.
- **Real-time CORBA (RT-CORBA)**: This is a reference model that extends the Common Object Request Broker Architecture (CORBA) to support real time distributed applications. It defines a set of standard interfaces and services that enable the interoperability and portability of real time objects across different platforms and networks. RT-CORBA provides features such as priority-based scheduling, thread pools, explicit binding, priority inheritance, and real time event service.

These are some of the reference models for real time systems that can be used to study and learn the concepts and principles of real time system design and analysis. They can also be used as a basis for developing and implementing real time systems for various domains and applications.



### Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers .
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource is a system component that can be shared by multiple jobs, but only one job can use it at a time. Examples of resources are memory, files, printers, and sensors .
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors or resources can be interrupted and resumed by another job. For example, a CPU can be preempted by a higher priority job and resume the execution of the lower priority job later.
- Non-preemptable processors or resources cannot be interrupted and resumed by another job. For example, a printer cannot be preempted by another job until it finishes printing the current job.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors or resources are assigned to a single job and cannot be used by any other job. For example, a dedicated CPU can only execute one job at a time.
- Shared processors or resources can be used by multiple jobs, but only one job can use them at a time. For example, a shared memory can be accessed by multiple jobs, but only one job can read or write to it at a time.
- Processors and resources can affect the performance and schedulability of real-time systems. Therefore, they need to be managed and allocated efficiently and effectively .
- Some of the challenges and techniques for managing and allocating processors and resources in real-time systems are:
  - Processor scheduling: deciding which job to execute on which processor at any given time .
  - Resource allocation: deciding which job to grant access to which resource at any given time .
  - Processor affinity: assigning a job to a specific processor or a set of processors to reduce the overhead of context switching and cache misses.
  - Processor tuning and optimization: adjusting the processor parameters and settings to improve the performance and predictability of real-time applications .
  - Resource locking and synchronization: preventing concurrent access to shared resources by multiple jobs to avoid data inconsistency and deadlock .
  - Resource reservation: allocating a portion of a resource to a specific job or a class of jobs to guarantee their quality of service.
  - Resource reclaiming: utilizing the unused or underutilized resources by other jobs to improve the system utilization and throughput.



### Temporal Parameters of Real Time Workload

- Temporal parameters are the time-related attributes of a real time job or task that specify its timing constraints and requirements.
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The earliest time at which a job can start execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - Absolute deadline (d<sub>i</sub>): The latest time by which a job must finish execution. It may be hard (must be met) or soft (can be missed occasionally).
  - Relative deadline (D<sub>i</sub>): The maximum time allowed for a job to finish execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval [(r<sub>i</sub>, d<sub>i</sub>]: The time interval in which a job can be feasibly executed. It is the difference between the release time and the absolute deadline.
- The temporal parameters of a job can be represented graphically as follows:

```
|<----------------- D_i ----------------->|
|<----- r_i ----->|<------ C_i ------->|<----- d_i ----->|
|-----------------|--------------------|-----------------|
0                 r_i                  d_i               t
```

- Where C<sub>i</sub> is the worst-case execution time of the job, and t is the time axis.
- The temporal parameters of a job can be used to determine its schedulability, priority, and performance metrics.



### Periodic Task Model

- A periodic task is a task that repeats itself after a fixed time interval, called the period.
- A periodic task is characterized by four parameters: phase, period, execution time, and deadline.
- Phase is the time at which the first instance of the task is released.
- Period is the time interval between two consecutive releases of the task.
- Execution time is the worst-case time required by the task to complete its execution.
- Deadline is the time by which the task must finish its execution.
- A periodic task can be represented by a tuple: T = <Φ, P, e, D> where Φ is the phase, P is the period, e is the execution time, and D is the deadline.
- The periodic task model is a deterministic workload model that can accurately capture many hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission.
- The periodic task model can be extended by adding a jitter parameter, which allows the flexibility that the actual release time of a task may be at most J time units earlier or later than the exact start time of the period.
- The periodic task model can be analyzed using various scheduling algorithms, such as rate-monotonic, earliest deadline first, and fixed priority.




### Precedence Constraints and Data Dependency

- Precedence constraints are the restrictions on the order of execution of jobs in a real time system. They are usually represented by a directed graph called a precedence graph, where the vertices are the jobs and the edges are the constraints. A job can only start execution after all its predecessors have completed execution  .
- Data dependency is the situation where the output of one job is used as the input of another job in a real time system. Data dependency cannot be captured by a precedence graph, as it does not imply a strict ordering of jobs. Data dependency may cause problems such as data inconsistency, data loss, or data corruption if not handled properly .
- Some examples of real time systems that have precedence constraints and data dependency are:
  - A robotic arm that has to perform a sequence of movements to assemble a product. The movements have to follow a certain order and depend on the feedback from sensors.
  - A video streaming application that has to encode, transmit, and decode video frames. The encoding and decoding have to be done in a timely manner and depend on the availability and quality of the data.
  - A flight control system that has to monitor and control various subsystems of an aircraft. The monitoring and control tasks have to be executed periodically and depend on the data from sensors and actuators.



## Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, and to avoid missing deadlines or violating timing constraints .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or before the system starts running. It is based on the known characteristics of the tasks, such as their periods, execution times, deadlines, and priorities. Static scheduling is suitable for systems that have fixed and periodic tasks, and that do not require much flexibility or adaptability .
  - Dynamic scheduling is done at run time or during the system execution. It is based on the current state of the system, such as the availability of resources, the arrival of new tasks, the completion of existing tasks, and the occurrence of events. Dynamic scheduling is suitable for systems that have variable and aperiodic tasks, and that require more flexibility and adaptability .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running. The lower priority task resumes its execution when the higher priority task finishes or is blocked. Preemptive scheduling can reduce the response time and the deadline miss ratio of the tasks, but it can also introduce more overhead and complexity .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running. The higher priority task has to wait until the lower priority task finishes or is blocked. Non-preemptive scheduling can reduce the overhead and complexity of the system, but it can also increase the response time and the deadline miss ratio of the tasks .
- Real time scheduling algorithms are the rules or methods that determine which task to execute next in a real time system. There are many real time scheduling algorithms, such as rate monotonic, earliest deadline first, least laxity first, etc. Each algorithm has its own advantages and disadvantages, and its own schedulability conditions or tests .
- Real time scheduling analysis is the process of evaluating and verifying the performance and correctness of a real time system and its scheduling algorithm. It can be done by using mathematical models, simulation tools, or empirical methods. The main metrics or criteria for real time scheduling analysis are feasibility, schedulability, utilization, response time, deadline miss ratio, etc .



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of allocating CPU time to tasks that have timing constraints, such as deadlines or periodicity. Real time scheduling aims to ensure that the system meets its timing requirements and performs its functionality correctly. There are different approaches to real time scheduling, depending on the characteristics of the tasks and the system. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, and period, are known at design time. In this approach, a schedule is computed offline and stored in a table. The table specifies which task should be executed at each time instant. A timer interrupts the system periodically and triggers the execution of the next task in the table. This approach has the advantages of simplicity, predictability, and low overhead, but it is not flexible or adaptable to dynamic changes in the system or the task set  .

- **Priority-driven approach**: This approach is also known as event-driven or preemptive approach. It is mainly used for soft or firm real time systems, where some of the properties of the tasks, such as arrival time or execution time, are not known at design time or may vary at run time. In this approach, each task is assigned a priority based on some criteria, such as deadline, period, or criticality. A scheduler runs whenever a task arrives, finishes, or blocks, and selects the highest priority task to execute. A task may preempt another task if it has a higher priority. This approach has the advantages of flexibility, adaptability, and responsiveness, but it has higher overhead and complexity than the clock-driven approach  .

- **Round-robin approach**: This approach is a special case of the priority-driven approach, where all the tasks have the same priority. It is mainly used for time-shared systems, where the goal is to provide fair and equal service to all the tasks. In this approach, each task is allocated a fixed amount of CPU time, called a time slice or a quantum. The scheduler runs in a circular order, giving each task a time slice to execute. If a task finishes or blocks before its time slice expires, the scheduler moves to the next task. If a task does not finish or block within its time slice, the scheduler preempts it and moves to the next task. This approach has the advantages of simplicity, fairness, and balance, but it may not meet the timing requirements of real time tasks .

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach, where the tasks have different priorities. It is mainly used for time-shared systems, where the goal is to provide proportional service to the tasks according to their weights. In this approach, each task is assigned a weight, which reflects its relative importance or demand. The scheduler runs in a circular order, giving each task a time slice proportional to its weight. For example, if task A has a weight of 2 and task B has a weight of 1, then task A will get twice as much CPU time as task B. This approach has the advantages of simplicity, fairness, and proportionality, but it may not meet the timing requirements of real time tasks .



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling .
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A schedule of the jobs is computed off-line and is stored for use at run-time.
- The scheduler schedules the jobs according to this schedule at each scheduling decision time.
- Clock-driven scheduling can be useful for real-time systems that require predictable and deterministic behaviour.
- Clock-driven scheduling can handle periodic tasks and aperiodic tasks with known arrival times.
- Clock-driven scheduling can also handle tasks with precedence constraints and resource sharing.
- Clock-driven scheduling can be implemented using table-driven or cyclic executive methods.
- Table-driven method uses a precomputed table that specifies the start time and duration of each job.
- Cyclic executive method uses a precomputed cyclic program that consists of a sequence of fixed-length slots.
- Clock-driven scheduling has some advantages and disadvantages:
  - Advantages:
    - It is simple and easy to implement.
    - It is efficient and has low overhead.
    - It can guarantee the deadlines of hard real-time tasks.
    - It can avoid priority inversion and deadlock problems.
  - Disadvantages:
    - It is inflexible and cannot handle dynamic changes in the system.
    - It is wasteful and may underutilize the processor.
    - It is difficult to design and verify the schedule.
    - It may not be optimal for some performance criteria.



### Weighted Round Robin Approach

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

- The advantage of weighted round robin is that it can provide differentiated service to different jobs based on their weights.
- The disadvantage of weighted round robin is that it may not be suitable for dynamic real-time systems with a mix of time-based and event-based activities, where the system must adapt to changing conditions and events.
- In such systems, priority-driven scheduling algorithms may be more appropriate.



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
- Examples of static priority-driven scheduling algorithms are rate-monotonic (RM) and deadline-monotonic (DM) algorithms.
- Examples of dynamic priority-driven scheduling algorithms are earliest deadline first (EDF) and least laxity first (LLF) algorithms.
- Priority-driven scheduling can improve the real-time performance and predictability of ROS 2, a framework for developing robotic applications.
- ROS 2 can leverage the priority-driven scheduling approach to prioritize critical tasks and reduce the interference from non-critical tasks.
- However, priority-driven scheduling also faces some challenges in ROS 2, such as the lack of priority inheritance, the heterogeneity of hardware platforms, and the complexity of the middleware layer.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their attributes (such as arrival times, execution times, deadlines, etc.) are known in advance and do not change during the system execution. A **dynamic system** is one where the tasks and their attributes may vary unpredictably during the system execution.
- Static systems can be **validated** before the system runs, i.e., it can be verified that the system will meet all the timing constraints under all possible scenarios. Dynamic systems may not be always validated, as some scenarios may be unknown or unforeseeable.
- Static systems can use **static scheduling**, i.e., the task priorities and the order of execution are determined before the system runs and do not change during the system execution. Dynamic systems may need **dynamic scheduling**, i.e., the task priorities and the order of execution are determined at run time based on the current system state and workload.
- Static scheduling is **simpler** and **faster** than dynamic scheduling, as it does not require any run time decision making or overhead. Dynamic scheduling is **more complex** and **slower** than static scheduling, as it requires run time decision making and overhead.
- Static scheduling can provide **guaranteed** and **optimal** performance for static systems, as it can exploit the full knowledge of the system characteristics and behavior. Dynamic scheduling can provide **adaptive** and **robust** performance for dynamic systems, as it can cope with the changing system conditions and workload.
- Static systems may provide **poor performance** in comparison with dynamic systems in terms of overall response time or resource utilization, as they may not be able to take advantage of the variations in the system workload or behavior. Dynamic systems may provide **better performance** in comparison with static systems in terms of overall response time or resource utilization, as they may be able to take advantage of the variations in the system workload or behavior.
- Static systems are more suitable for **hard real-time systems**, where the timing constraints are strict and must be met under all circumstances. Dynamic systems are more suitable for **soft real-time systems**, where the timing constraints are flexible and can be violated occasionally.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints. This means that EDF can schedule any set of tasks that is schedulable by any other algorithm.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints. This means that LST can schedule any set of tasks that is schedulable by any other algorithm that respects the precedence constraints.
- However, EDF and LST are not optimal for non-preemptive scheduling or for tasks with shared resources or synchronization requirements. In these cases, EDF and LST may fail to produce a feasible schedule even if one exists, or may under-utilize the CPU, thus decreasing the efficiency and throughput.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class  .
- The static priorities are assigned according to the cycle duration of the job, so a shorter cycle duration results in a higher job priority  .
- RMA is preemptive in nature, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for a set of periodic and independent jobs, meaning that it can always meet the deadlines of all the jobs if there exists any feasible schedule  .
- RMA has a simple and efficient implementation, as it only requires the knowledge of the cycle durations of the jobs and does not need any dynamic information such as deadlines or execution times .
- RMA has some limitations, such as:
  - It does not consider the actual execution times of the jobs, which may lead to underutilization of the processor .
  - It does not handle aperiodic or sporadic jobs, which may have unpredictable arrival times or deadlines .
  - It does not guarantee the schedulability of all feasible sets of jobs, as it may fail to meet the deadlines of some jobs even if the processor utilization is less than 100% .
- RMA has a sufficient and necessary schedulability test, which is based on the utilization bound of the processor  . The utilization bound is given by:

  U = n * (2^(1/n) - 1)

  where n is the number of jobs and U is the maximum utilization that can be achieved by RMA.

  The test states that a set of jobs is schedulable by RMA if and only if the total utilization of the jobs is less than or equal to U  .

- RMA can be illustrated by the following example:

  Suppose there are three periodic and independent jobs, J1, J2, and J3, with the following parameters:

  | Job | Cycle Duration | Execution Time | Priority |
  | --- | -------------- | -------------- | -------- |
  | J1  | 20             | 5              | 3        |
  | J2  | 10             | 2              | 2        |
  | J3  | 5              | 1              | 1        |

  The priorities are assigned according to the cycle durations, so J3 has the highest priority and J1 has the lowest priority.

  The utilization bound for n = 3 is:

  U = 3 * (2^(1/3) - 1) = 0.7798

  The total utilization of the jobs is:

  U = 5/20 + 2/10 + 1/5 = 0.65

  Since U < 0.7798, the set of jobs is schedulable by RMA.

  The following diagram shows the schedule of the jobs by RMA:

  ```
  Time: 0   5   10  15  20  25  30  35  40  45  50
  J3  : |---|---|---|---|---|---|---|---|---|---|---|
  J2  : |   |   |---|   |   |---|   |   |---|   |   |
  J1  : |   |   |   |   |---|   |   |   |   |   |---|
  ```

  As can be seen, all the jobs meet their deadlines and no job is interrupted by a lower priority job.



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute. The schedule is based on the knowledge of release time, execution time, deadline, priority, and resource requirement of all tasks for all time . The schedule is stored in a table and used during the run-time . Offline scheduling is suitable for static and deterministic systems, where the task parameters and arrival patterns are known in advance. Offline scheduling has the advantage of reducing the run-time overhead and complexity, but the disadvantage of lacking flexibility and adaptability to handle dynamic and unpredictable events.

- Online scheduling is a technique that makes scheduling decisions during the run-time of the system . The scheduler does not have the complete knowledge about the tasks that will be released in the future, and the parameters of each task are known to the scheduler only after the release of the task . Online scheduling can be either static or dynamic, depending on whether the priority of a task is fixed or can change over time . Online scheduling is suitable for dynamic and stochastic systems, where the task parameters and arrival patterns are not known in advance or may vary unpredictably. Online scheduling has the advantage of being flexible and adaptable to handle dynamic and unpredictable events, but the disadvantage of increasing the run-time overhead and complexity.

- An example of offline scheduling is table-driven scheduling, where the scheduler follows a pre-computed table that specifies which task to execute at each time instant. An example of online scheduling is priority-driven scheduling, where the scheduler selects the task with the highest priority among the ready tasks at each scheduling point .



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time between successive jobs, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are sensor readings, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, criticality, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a predefined schedule that is determined offline. The scheduler follows the schedule and switches jobs at predefined instants. Examples are cyclic executive, time triggered, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven and clock driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the schedulability of periodic jobs.
- In priority driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: background scheduling and slack stealing.
  - Background scheduling assigns the lowest priority to aperiodic and sporadic jobs, and executes them only when no periodic job is ready. This ensures that periodic jobs always meet their deadlines, but may result in poor response time for aperiodic and sporadic jobs.
  - Slack stealing assigns higher priority to aperiodic and sporadic jobs, and executes them by using the available slack time of periodic and sporadic jobs. Slack time is the amount of time that a job can be delayed without affecting the schedulability of other jobs. This improves the response time of aperiodic and sporadic jobs, but may require more complex algorithms to compute and track the slack time.
- In clock driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: spare capacity scheduling and dynamic scheduling.
  - Spare capacity scheduling allocates some slots in the predefined schedule for aperiodic and sporadic jobs, and executes them in a first-come first-served or priority based order. This provides some guaranteed service for aperiodic and sporadic jobs, but may waste some slots if no aperiodic or sporadic job arrives.
  - Dynamic scheduling modifies the predefined schedule at runtime to accommodate aperiodic and sporadic jobs, by shifting or skipping some periodic jobs. This provides more flexibility for aperiodic and sporadic jobs, but may introduce more overhead and complexity for the scheduler.



## Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of a computer system, such as hardware, software, data, or network bandwidth, available to multiple users or processes.

Resource sharing can have various benefits, such as:

- Improving the efficiency and utilization of the system resources
- Reducing the cost and complexity of the system administration
- Enhancing the scalability and reliability of the system
- Enabling the collaboration and communication among the users or processes

Resource sharing can also have some challenges, such as:

- Managing the access and allocation of the shared resources
- Ensuring the security and privacy of the shared resources
- Handling the conflicts and contention among the users or processes
- Dealing with the heterogeneity and compatibility of the system components

Resource sharing can be implemented at different levels of the system, such as:

- Hardware level: sharing the physical devices or components of the system, such as CPU, memory, disk, printer, etc.
- Software level: sharing the logical entities or services of the system, such as files, databases, applications, etc.
- Network level: sharing the communication channels or protocols of the system, such as TCP/IP, HTTP, FTP, etc.

Resource sharing can be achieved by different methods or techniques, such as:

- Centralized: using a single server or controller to manage and provide the shared resources to the users or processes
- Distributed: using multiple servers or controllers to cooperate and coordinate the shared resources among the users or processes
- Peer-to-peer: using the users or processes themselves to exchange and share the resources without any central authority
- Virtualization: using software to create and manage the virtual instances or copies of the shared resources
- Cloud computing: using the internet to access and use the shared resources provided by remote servers or providers



### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Timing anomalies occur when a change in the execution time of a task affects the schedulability of other tasks in an unpredictable way, such as when a shorter execution time leads to a longer response time.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Some examples of RAC protocols are:
  - Priority inheritance protocol (PIP), which assigns the highest priority of the blocked tasks to the task that holds the resource, and restores the original priority when the resource is released.
  - Priority ceiling protocol (PCP), which assigns a ceiling priority to each resource, and prevents a task from locking a resource if its priority is lower than the ceiling priority of any locked resource.
  - Stack resource policy (SRP), which assigns a preemption level to each task, and prevents a task from locking a resource if its preemption level is lower than the preemption level of any locked resource.
  - Multiprocessor priority ceiling protocol (MPCP), which extends PCP to multiprocessor systems, and allows tasks to migrate between processors while holding resources.
  - Multiprocessor stack resource policy (MSRP), which extends SRP to multiprocessor systems, and requires tasks to release resources before migrating between processors.



### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access to shared resources in real-time systems .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs  .
- NPCS has the following properties:
  - Mutual exclusion: No two jobs can access the same resource at the same time.
  - Deadlock-free: No job can be blocked indefinitely by another job holding a resource.
  - Priority inversion-free: No job can be preempted by a lower-priority job while holding a resource.
  - Bounded blocking: The maximum blocking time of a job is bounded by the longest critical section of any job.
- NPCS can be implemented by using a global lock variable that indicates whether any resource is in use or not. A job that wants to enter a critical section must first check the lock variable and wait until it is free. Then, it sets the lock variable to indicate that a resource is in use and raises its priority to the highest level. After exiting the critical section, it restores its original priority and clears the lock variable .
- NPCS has some advantages and disadvantages:
  - Advantages:
    - Simplicity: NPCS is easy to implement and understand.
    - Efficiency: NPCS does not require any additional data structures or overheads for managing resources.
    - Robustness: NPCS can handle any number of resources and jobs without causing deadlock or priority inversion.
  - Disadvantages:
    - Utilization: NPCS can reduce the processor utilization by delaying the execution of lower-priority jobs that do not need any resources.
    - Responsiveness: NPCS can increase the response time of higher-priority jobs that are blocked by lower-priority jobs holding resources.
    - Fairness: NPCS can cause starvation of lower-priority jobs that are repeatedly blocked by higher-priority jobs holding resources.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance protocol (PIP) and priority-ceiling protocol (PCP) are two methods for resolving priority inversion problem in real-time systems.
- Priority inversion occurs when a higher-priority task is blocked by a lower-priority task that holds a shared resource, and the lower-priority task is preempted by a medium-priority task that does not need the resource.
- PIP and PCP aim to reduce the blocking time of higher-priority tasks and prevent deadlock situations.

#### Priority-Inheritance Protocol

- PIP works by temporarily boosting the priority of the lower-priority task that holds the resource to the priority of the highest-priority task that requests the resource.
- This way, the lower-priority task can finish its critical section and release the resource, allowing the higher-priority task to resume execution.
- PIP can be applied to nested resources, where a task may hold more than one resource at a time. In this case, the priority of the task is boosted to the highest priority of any task that requests any of the resources it holds.
- PIP has the following properties:
  - It eliminates unbounded priority inversion, as the blocking time of a higher-priority task is limited by the duration of the critical sections of the lower-priority tasks that hold the resources it needs.
  - It is greedy, as it allows a task to access a resource whenever it is free, regardless of the priorities of other tasks that may request the same resource in the future.
  - It may cause chained blocking, where a task is blocked by another task that is blocked by another task, and so on, resulting in a long chain of blocked tasks.
  - It may cause deadlock, if there is a circular dependency among the tasks and the resources they need.

#### Priority-Ceiling Protocol

- PCP works by assigning a static priority ceiling to each resource, which is the highest priority of any task that may access the resource.
- A task can access a resource only if its priority is higher than the priority ceilings of all the resources currently held by other tasks.
- This way, the priority ceiling of a resource acts as a barrier that prevents lower-priority tasks from accessing the resource and blocking higher-priority tasks.
- PCP can be applied to nested resources, where a task may hold more than one resource at a time. In this case, the priority of the task is raised to the highest priority ceiling of any resource it holds.
- PCP has two variants: original ceiling priority protocol (OCPP) and immediate ceiling priority protocol (ICPP).
  - OCPP raises the priority of a task only when it accesses a resource, and lowers it when it releases the resource.
  - ICPP raises the priority of a task as soon as it becomes ready to run, and lowers it when it finishes execution.
- PCP has the following properties:
  - It eliminates unbounded priority inversion, as the blocking time of a higher-priority task is limited by the duration of a single critical section of a lower-priority task.
  - It is not greedy, as it may withhold access to a free resource, causing a task to be blocked by a lower-priority task that does not hold the requested resource. This is called avoidance blocking.
  - It prevents chained blocking, as a task can be blocked by at most one lower-priority task at a time.
  - It prevents deadlock, as it ensures that a task can access a resource only if it has a higher priority than any other task that may need the same resource.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules :
  - Scheduling Rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at the time.
  - Allocation Rule: Whenever a job requests a resource, it is allocated the resource if it is free and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked and its priority is raised to the ceiling priority of the resource.
- SBPCP guarantees that :
  - No deadlock can occur, since a job can only request a resource with a ceiling priority equal to or higher than its own priority, and a lower priority job cannot block a higher priority job from accessing a resource.
  - The maximum blocking time for any job is equal to the execution time of one critical section with the highest ceiling priority among all the resources accessed by the job.
  - The priority inversion problem is minimized, since a job can only be blocked by a lower priority job that holds a resource with a ceiling priority equal to or higher than its own priority, and the blocking time is bounded by the critical section length.



### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a job task synchronization protocol in a real-time system that prevents deadlocks and unbounded priority inversions.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- The priority ceiling of a resource is the highest priority of any task that can access that resource.
- The system ceiling is the highest priority ceiling of any resource currently locked.
- A task can lock a resource only if its priority is higher than the system ceiling.
- A task that locks a resource inherits the priority ceiling of that resource until it releases it.
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- This ensures that no task is blocked by a lower priority task and that no circular wait can occur.
- An example of using the priority ceiling protocol in a dynamic priority system is given below :

| Time | Task | Resource | Priority Ceiling | System Ceiling |
|------|------|----------|------------------|----------------|
| 0    | T1   | X        | 1                | 1              |
| 1    | T1   | X        | 1                | 1              |
| 2    | T1   | X        | 1                | 1              |
| 3    | T1   | X        | 1                | 1              |
| 4    | T2   | Y        | 2                | 2              |
| 5    | T2   | Y        | 2                | 2              |
| 6    | T2   | Y        | 2                | 2              |
| 7    | T2   | Y        | 2                | 2              |
| 8    | T1   | X        | 2                | 2              |
| 9    | T1   | X        | 2                | 2              |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on.
- The priority ceiling of Y is 2 from time 4 to 9.
- The system ceiling is the maximum of the priority ceilings of the locked resources at any time.
- T1 locks X at time 0 and inherits its priority ceiling of 1.
- T2 locks Y at time 4 and inherits its priority ceiling of 2.
- T1 cannot lock Y at time 5 because its priority is lower than the system ceiling of 2.
- T2 cannot lock X at time 6 because its priority is lower than the system ceiling of 2.
- T1 releases X at time 9 and resumes its original priority of 1.
- T2 releases Y at time 9 and resumes its original priority of 2.



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
  - It reduces the number of context switches and the overhead of priority management.
  - It allows for a simpler and more efficient implementation of semaphores.
- Preemption ceiling protocol can be combined with preemption threshold scheduling (PTS) to enable a scalable real-time system design.
- PTS is a scheduling policy that assigns a preemption threshold to each task, which is the lowest priority level at which the task can be preempted.
- PTS allows a task to execute at a lower priority level than its assigned priority, thus reducing the preemption overhead and improving the system utilization.
- However, PTS may lead to long priority inversion if not combined with a proper synchronization protocol, such as preemption ceiling protocol.
- The combination of PTS and preemption ceiling protocol is called dual ceiling protocol, which has the following properties:
  - A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks, and its preemption threshold is higher than the ceiling priority of the resource it wants to lock.
  - When a task locks a resource, its priority and preemption threshold are temporarily raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
  - The ceiling priority of a resource is dynamically determined by the maximum of the preemption thresholds of all the tasks that can access that resource.
  - The dual ceiling protocol guarantees bounded priority inversion, deadlock freedom, and optimal priority inheritance.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that have more than one unit of the same type, such as printers, disks, or processors.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- If a resource can be used by more than one job at a time, we model that resource as having many units, each used mutually exclusively  .
- Access to multiple-unit resources is controlled using locks  .
- Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge is to design a locking protocol that ensures mutual exclusion, deadlock freedom, and bounded blocking time for real-time jobs.
- One possible protocol is the **Multiple-Unit Priority Ceiling Protocol (MUPCP)** , which is an extension of the Priority Ceiling Protocol (PCP) for single-unit resources.
- The MUPCP assigns a priority ceiling to each unit of each resource, which is the highest priority of any job that may lock that unit.
- The MUPCP also maintains a system ceiling, which is the highest priority ceiling of any locked unit of any resource.
- A job can lock a unit of a resource only if its priority is higher than the system ceiling; otherwise, it is blocked.
- A job that locks a unit of a resource inherits the priority ceiling of that unit until it unlocks it.
- The MUPCP ensures mutual exclusion by preventing two jobs from locking the same unit of a resource at the same time.
- The MUPCP ensures deadlock freedom by preventing circular waiting among jobs that lock different units of different resources.
- The MUPCP ensures bounded blocking time by limiting the number of jobs that can block a higher-priority job to at most one per resource.



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs or transactions.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause inconsistency or deadlock problems.
- Concurrency control is the technique of managing concurrent accesses to data objects by jobs or transactions, while ensuring data consistency, timing constraints, and system performance.
- Concurrency control can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking data objects before accessing them. Examples of pessimistic concurrency control protocols are priority ceiling protocol, affected set priority ceiling protocol, and convex ceiling protocol.
  - Optimistic concurrency control allows conflicts to occur and resolves them by aborting or restarting transactions. Examples of optimistic concurrency control protocols are wait-free protocol, timestamp ordering protocol, and multiversion protocol.
- Concurrency control protocols should consider the temporal characteristics of data objects, such as deadlines, validity, and freshness, as well as the temporal constraints of jobs or transactions, such as deadlines, priorities, and criticality.



## Unit 4 - Real Time Communication

Real time communication (RTC) is the exchange of information between two or more parties without significant delay. RTC can be synchronous or asynchronous, depending on the degree of coordination and synchronization required. RTC can involve different types of media, such as text, audio, video, or data.

Some examples of RTC are:

- Voice over Internet Protocol (VoIP), which allows users to make and receive phone calls over the internet.
- Video conferencing, which enables users to see and hear each other in real time, using webcams and microphones.
- Instant messaging (IM), which allows users to send and receive text messages in real time, using applications or web browsers.
- Chatbots, which are software programs that can interact with users in natural language, using text or voice.
- Online gaming, which allows users to play games with other players over the internet, using consoles, computers, or mobile devices.
- Live streaming, which allows users to broadcast or watch live video or audio over the internet, using platforms or applications.

Some benefits of RTC are:

- It can improve collaboration and productivity, by allowing users to communicate and share information more efficiently and effectively.
- It can reduce costs and travel time, by enabling users to communicate and work remotely, without the need for physical meetings or phone calls.
- It can enhance customer service and satisfaction, by allowing users to interact with businesses or organizations in real time, using their preferred mode of communication.
- It can create new opportunities and experiences, by allowing users to access and participate in various events, activities, or communities online.

Some challenges of RTC are:

- It can require high bandwidth and low latency, to ensure good quality and performance of the communication.
- It can pose security and privacy risks, by exposing users' personal or sensitive information to potential hackers or eavesdroppers.
- It can create social and ethical issues, by affecting users' behavior, relationships, or values, such as online addiction, cyberbullying, or digital divide.



### Basic Concepts in Real time Communication

Real-time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays. In this context, the term real-time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some of the basic concepts in RTC are:

- **Real-time guarantees**: RTC systems are designed to provide certain guarantees on the timeliness, validity and integrity of the data transferred. These guarantees are essential for applications that require high reliability, safety and quality of service.
- **Real-time protocols**: RTC systems use specific protocols that enable the efficient and reliable transmission of data in real-time. Some of the common RTC protocols are RTP (Real-time Transport Protocol), RTCP (Real-time Control Protocol), RTSP (Real-time Streaming Protocol), SIP (Session Initiation Protocol) and WebRTC (Web Real-Time Communication).
- **Real-time media**: RTC systems use various types of media to convey information, such as audio, video, text, images, etc. These media have different characteristics and requirements, such as bandwidth, latency, jitter, compression, encryption, etc. RTC systems must adapt to these media and provide the best possible quality and user experience.
- **Real-time applications**: RTC systems enable various applications that involve real-time communication, such as voice and video calls, online gaming, live streaming, telemedicine, remote education, etc. These applications have different needs and challenges, such as scalability, security, interoperability, etc. RTC systems must meet these needs and overcome these challenges.



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT).
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- A hard real-time communication system is one that must meet its deadlines, otherwise it may cause catastrophic failure or unacceptable loss    .
- Examples of hard real-time communication systems are air traffic control, nuclear power plant control, and missile guidance  .
- A soft real-time communication system is one that can tolerate some deadline misses, but the quality of service may degrade    .
- Examples of soft real-time communication systems are video conferencing, online gaming, and multimedia streaming  .
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic.
- Hard real-time communication systems require strict timing guarantees and high reliability, while soft real-time communication systems can trade off some performance for flexibility and adaptability .
- Hard real-time communication systems are often implemented using dedicated hardware and software, while soft real-time communication systems can use general-purpose platforms and protocols .



### Model of Real Time Communication

- Real time communication is any online communication that happens in real time, with negligible latency and without intermediate storage  .
- Real time communication can be classified into two types: real time traffic and real time control.
- Real time traffic consists of streams of messages that are generated by their sources and delivered to their respective destinations on a continuous basis.
- Real time traffic can be further divided into three categories: periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals and have fixed deadlines.
- Aperiodic messages are generated at irregular intervals and have variable deadlines.
- Sporadic messages are generated randomly and have unpredictable deadlines.
- Real time control consists of commands and feedback signals that are used to control the behavior of real time systems.
- Real time control can be further divided into two categories: hard and soft control.
- Hard control requires that the commands and feedback signals are delivered within strict deadlines, otherwise the system may fail or cause damage.
- Soft control allows some flexibility in the delivery of commands and feedback signals, as long as the system performance is not degraded significantly.

- A model of real time communication can be represented by the following diagram:

```
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
|    Source      |      |    Network     |      |   Destination  |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Output Buffer  |      | Input Buffer   |      | Input Buffer   |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
|                |      |                |      |                |
| Output Queue   |      | Input Queue    |      | Input Queue    |
|                |      |                |      |                |
+----------------+      +----------------+      +----------------+
```

- In this model, the source and destination are the end users of the real time application systems residing in different hosts.
- The network is the medium that connects the source and destination hosts.
- The network interface of each host contains an input queue and an output queue.
- Two buffer areas called input/output buffers are allocated to the input and output queues to store queuing information.
- The input buffer stores the incoming messages from the network before they are delivered to the destination.
- The output buffer stores the outgoing messages from the source before they are transmitted to the network.
- The input and output queues manage the order and priority of the messages in the buffers.

- A model of real time communication can be characterized by three parameters: throughput, delay and jitter .
- Throughput is the rate at which the messages are successfully delivered from the source to the destination .
- Delay is the time elapsed between the generation of a message at the source and its delivery at the destination .
- Jitter is the variation in the delay of different messages in the same stream .
- The goal of real time communication is to maximize the throughput and minimize the delay and jitter, while satisfying the deadlines and quality of service requirements of the messages .



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns different weights to different priority classes and serves packets in a round-robin fashion according to their weights.
- WRR does not require a sorted priority queue, only a round-robin queue.
- WRR can guarantee both bandwidth and fairness requirements, but it may not satisfy the delay and jitter requirements of real-time packets.
- A variation of WRR is the rate-controlled frame-based WRR (RFWRR), which divides the scheduler into two components: a rate controller and a frame-based WRR server.
- The rate controller adjusts the weights of the priority classes based on their delay requirements and the network conditions.
- The frame-based WRR server serves packets in fixed-size frames, where each frame consists of a number of slots proportional to the weights of the priority classes.
- RFWRR can guarantee the delay jitter bound and satisfy a diverse set of delay requirements for real-time packets.
- Other priority-based service disciplines include the class-based weighted fair queuing (CBWFQ) and the weighted fair priority queuing (WFPQ), which use different algorithms to allocate bandwidth and priority to different classes of packets.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel by multiple nodes or transmitters.
- Broadcast networks are networks where a single transmission can be received by all nodes in the network, such as wireless networks or bus networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use random or probabilistic methods to determine which node will transmit next, such as Aloha, slotted Aloha, or carrier-sense multiple access (CSMA) protocols. These protocols are simple, decentralized, and adaptive, but they suffer from collisions, low channel utilization, and unbounded access delay.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next, such as round-robin, token passing, or priority-based protocols. These protocols avoid collisions, provide bounded access delay, and guarantee fairness, but they require synchronization, coordination, and overhead.
- Reservation-based protocols use a two-phase approach, where nodes first reserve a slot for transmission and then transmit in the reserved slot, such as time division multiple access (TDMA), frequency division multiple access (FDMA), or code division multiple access (CDMA) protocols. These protocols achieve high channel utilization, avoid collisions, and provide quality of service (QoS) guarantees, but they require reservation overhead, synchronization, and fixed allocation of resources.
- Adaptive MAC protocols are protocols that can adjust their parameters or behavior according to the network conditions, such as traffic load, node connectivity, channel quality, or QoS requirements. These protocols aim to improve the performance, efficiency, and reliability of broadcast transmission, while maintaining the simplicity and flexibility of MAC protocols.
- An example of an adaptive MAC protocol for reliable broadcast in wireless networks is ABROAD (Adaptive Broadcast Reliable On-demand Access Delay-bounded) protocol, which incorporates a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay. ABROAD provides worst-case performance guarantees while remaining adaptive to local changes in traffic load and node connectivity. ABROAD outperforms broadcast protocols based on reliable unicast packet delivery schemes, such as the IEEE 802.11 MAC standard.



### Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP, HTTP, FTP, etc.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, etc.
- Quality of Service (QoS) is the ability of a network to provide different levels of service to different applications or data flows, according to their needs and preferences.
- Resource Reservation Protocol (RSVP) is a network control protocol that enables Internet applications to obtain specific QoS for their data flows.
- RSVP operates over IPv4 or IPv6 and supports both multicast and unicast data flows.
- RSVP is receiver-initiated, meaning that the receiver of a data flow requests the desired QoS from the network and the sender adapts to the available resources.
- RSVP uses soft state, meaning that the reservations are periodically refreshed and can be easily modified or removed.
- RSVP uses PATH and RESV messages to establish and maintain reservations along the end-to-end path of a data flow.
- RSVP uses filterspecs and flowspecs to specify the characteristics of the data flow and the requested QoS, respectively.
- RSVP uses admission control and policy control mechanisms to determine whether a reservation request can be granted or not, based on the available resources and the authorization of the user.
- RSVP is integrated with the IntServ model, which defines a set of QoS classes that can be requested by applications, such as Guaranteed Service, Controlled Load Service, and Best Effort Service.
- RSVP can also interoperate with the DiffServ model, which uses packet marking and traffic conditioning to provide different levels of service to different classes of traffic.



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can process data and events that have critically defined time constraints.
- An RTOS is different from a general-purpose operating system, such as Windows or Linux, which is designed for multitasking and sharing system resources.
- An RTOS provides features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS can be used for applications that require high performance, reliability, and responsiveness, such as industrial control, flight control, and embedded systems.
- A real-time database system (RTDBS) is a database system that can perform database operations with real-time constraints.
- An RTDBS is different from a conventional database system, such as Oracle or MySQL, which is designed for batch processing and data warehousing.
- An RTDBS provides features such as concurrency control, transaction management, data consistency, and recovery.
- An RTDBS can be used for applications that require timely and accurate data access, such as online reservation, stock trading, and sensor networks.
- A real-time database system can be based on SQL or NoSQL, depending on the data model and query language.
- A time series database is a type of real-time database system that can store and analyze data that changes over time, such as temperature, pressure, or stock prices.
- A time series database provides features such as compression, aggregation, interpolation, and anomaly detection.
- A time series database can be used for applications that require historical and predictive analysis, such as monitoring, forecasting, and optimization.



### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load. An RTOS has the following features   :

- **Small and fast**: An RTOS is designed to occupy very less memory and consume fewer resources, as it often runs on embedded devices with limited hardware capabilities. An RTOS also has a fast boot time and low interrupt latency, which means it can respond quickly to external events.
- **Responsive and deterministic**: An RTOS can meet the deadlines and timing constraints of real-time tasks, by using scheduling algorithms that prioritize the most urgent and critical tasks. An RTOS can also ensure that the same input will always produce the same output, regardless of the system state or external factors.
- **Co-operative or pre-emptive scheduling**: An RTOS can use either co-operative or pre-emptive scheduling to manage the execution of tasks. Co-operative scheduling means that a task will run until it is completed or voluntarily yields the CPU to another task. Pre-emptive scheduling means that a task can be interrupted by a higher-priority task at any time, and resume when the higher-priority task is finished or blocked.
- **Main and background loops**: An RTOS can use a main and background loop structure to handle tasks. The main loop is a high-priority loop that executes the most critical and time-sensitive tasks, such as interrupt handling, sensor reading, and actuator control. The background loop is a low-priority loop that executes the less critical and time-consuming tasks, such as user interface, logging, and communication. The main loop can pre-empt the background loop whenever necessary.
- **Task synchronization and communication**: An RTOS can provide mechanisms for tasks to synchronize and communicate with each other, such as semaphores, mutexes, message queues, and event flags. These mechanisms can help prevent race conditions, deadlocks, and data corruption, as well as facilitate data exchange and coordination among tasks.



### Time Services

Time services are the functions and mechanisms that provide the ability to measure, represent, and manipulate time in real-time systems. Time services are essential for ensuring the timeliness and synchronization of real-time systems, which are systems that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.

Some of the time services that are commonly used in real-time systems are:

- **Clocks**: Clocks are devices that generate periodic signals to measure the passage of time. Clocks can be either hardware or software based, and can have different levels of accuracy, resolution, and stability. Clocks can also be synchronized with other clocks using various protocols and algorithms, such as the Network Time Protocol (NTP) or the Precision Time Protocol (PTP).
- **Timers**: Timers are devices that generate interrupts or signals after a specified amount of time has elapsed. Timers can be used to trigger events, schedule tasks, measure durations, or implement timeouts. Timers can be either hardware or software based, and can have different modes of operation, such as one-shot, periodic, or countdown.
- **Time stamps**: Time stamps are data structures that represent a specific point in time. Time stamps can be used to record the occurrence of events, compare the order of events, or measure the latency or jitter of events. Time stamps can have different formats, such as absolute, relative, or logical, and can have different levels of granularity, such as seconds, milliseconds, or nanoseconds.
- **Time zones**: Time zones are regions that have a uniform standard time for legal, commercial, or social purposes. Time zones can be used to convert between local and universal time, or between different time zones. Time zones can have different offsets from the Coordinated Universal Time (UTC), and can have different rules for daylight saving time (DST).
- **Calendars**: Calendars are systems that organize time into units, such as days, weeks, months, or years. Calendars can be used to represent dates, schedule events, or calculate durations. Calendars can have different types, such as Gregorian, Julian, or lunar, and can have different formats, such as year-month-day, month-day-year, or day-month-year.



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS by default, but it can be modified or extended to provide some real-time features, such as:
  - Preemptive scheduling: The ability to interrupt a running process and switch to a higher priority one when an event occurs.
  - Priority inheritance: The mechanism to avoid priority inversion, which occurs when a low priority process holds a resource needed by a high priority process.
  - Real-time signals: The signals that are delivered to a process immediately, without being queued or blocked.
  - POSIX real-time extensions: The set of standards that define interfaces and behavior for real-time applications on UNIX-like systems.
- However, UNIX still faces some challenges when used as a RTOS, such as:
  - Non-deterministic latency: The delay between an event and the response of the system, which can vary depending on the system load, memory management, device drivers, etc.
  - Non-real-time components: The parts of the system that are not designed for real-time applications, such as the file system, the network stack, the graphical user interface, etc.
  - Non-real-time hardware: The hardware that does not support real-time operations, such as the CPU, the memory, the disk, the network, etc.
- Therefore, UNIX is not a suitable choice for hard real-time applications, which require strict and predictable timing guarantees, but it can be used for soft real-time applications, which can tolerate some degree of latency or deadline misses.



### POSIX Issues

- POSIX stands for Portable Operating System Interface, which is a set of standards that define how an application should interact with an operating system.
- POSIX aims to achieve portability, interoperability, and compatibility among different operating systems, especially for applications that require long-term maintenance and support.
- POSIX covers various aspects of operating system services, such as file operations, process management, signals, devices, threads, and real-time extensions.
- POSIX real-time extensions are defined in the POSIX.1b and POSIX.1j standards, which specify the requirements and interfaces for real-time operating systems and applications.
- POSIX real-time extensions include features such as:
  - Priority-based scheduling and preemption
  - Timers and clocks
  - Synchronization primitives (mutexes, condition variables, semaphores, etc.)
  - Asynchronous and synchronous I/O
  - Memory locking and mapping
  - Message queues and shared memory
  - Signals and signal handlers
- POSIX real-time extensions aim to provide deterministic and predictable behavior for real-time applications, which have strict timing constraints and deadlines.
- POSIX real-time extensions also support the notion of process and thread attributes, which allow the application to specify the scheduling policy, priority, stack size, and other parameters for each process or thread.
- POSIX real-time extensions are not mandatory for all operating systems, and some operating systems may not support all the features or may have different implementations or performance characteristics.
- POSIX real-time extensions may also have some limitations or trade-offs, such as:
  - Increased complexity and overhead
  - Reduced portability and compatibility with non-POSIX systems
  - Potential conflicts or inconsistencies with other POSIX standards or features
  - Lack of support for some real-time requirements, such as deadline scheduling, resource reservation, or fault tolerance
- POSIX real-time extensions are not sufficient for all real-time applications, and some applications may require additional or alternative mechanisms or services, such as:
  - Real-time communication protocols and networks
  - Real-time databases and file systems
  - Real-time middleware and frameworks
  - Real-time analysis and verification tools
- POSIX real-time extensions are still evolving and improving, and new standards and revisions are being developed and proposed, such as:
  - POSIX.1d, which defines additional real-time features, such as sporadic servers, timers, and clocks
  - POSIX.1e, which defines security extensions, such as access control and auditing
  - POSIX.1g, which defines networking extensions, such as sockets and protocols
  - POSIX.1h, which defines system administration extensions, such as user and group management and logging
  - POSIX.1i, which defines additional real-time features, such as trace and event logging and notification
  - POSIX.1m, which defines additional real-time features, such as resource limits and reservations



### Characteristics of Temporal Data

- Temporal data is the data that represents time in some form, and allows other data to be placed in a chronological sequence, or to be analyzed chronologically.
- Temporal data is the temporary data that is valid only for a prescribed time. Temporal data becomes invalid or obsolete after a certain period of time.
- Temporal data can be uni-temporal, bi-temporal or tri-temporal, depending on the number of temporal aspects it includes. The temporal aspects usually include valid time, transaction time or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time period during which a fact is stored in the database.
  - Decision time is the time period during which a fact is considered to be in effect by an authority.
- Temporal data can be used to analyze weather patterns, traffic conditions, demographic trends, and so on.
- Temporal data can be collected from various sources, such as manual data entry, observational sensors, or simulation models.
- Temporal data requires special data structures and query languages to store and manipulate it in a database.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to process data that is time-sensitive and relevant to the current situation. If the data is outdated or inaccurate, the system may make wrong decisions or miss deadlines.
- Temporal consistency can be measured by the difference between the actual value of a physical entity and the value of the corresponding data object in the database. This difference is called temporal error or temporal skew.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates: updating the data objects periodically or when a significant change occurs in the physical environment.
  - Temporal validity: assigning a validity interval to each data object and checking if the data object is still valid before reading it.
  - Temporal caching: caching the data objects in the memory of the processors and updating them when needed.
  - Temporal locking: locking the data objects for a certain duration and preventing other transactions from accessing them until they are updated.
- Temporal consistency can be traded off with other performance metrics, such as throughput, response time, deadline miss ratio, and memory usage. Different real-time systems may have different requirements and preferences for temporal consistency and other metrics.



### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic concurrency control are two-phase locking, timestamp ordering, and priority inheritance protocols.
  - Optimistic concurrency control allows conflicts to occur and then resolves them by aborting or restarting the conflicting transactions. Examples of optimistic concurrency control are optimistic concurrency control with backward validation, optimistic concurrency control with forward validation, and multiversion concurrency control.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as the performance criteria, the assumptions, and the goals of different classes of RTS .
  - Performance criteria: RTS are more concerned with meeting deadlines and minimizing response time than maximizing throughput and minimizing abort rate.
  - Assumptions: RTS often have predictable workloads, periodic transactions, and static data, while database systems often have unpredictable workloads, non-periodic transactions, and dynamic data.
  - Goals: RTS often aim to achieve predictability, schedulability, and feasibility, while database systems often aim to achieve serializability, recoverability, and consistency.
- Concurrency control techniques for RTS should consider the following factors:
  - The correctness criteria for the transactions, such as serializability, linearizability, or precedence graph correctness.
  - The priority assignment for the transactions, such as fixed priority, dynamic priority, or earliest deadline first.
  - The synchronization mechanism for the transactions, such as blocking, non-blocking, or wait-free.
  - The conflict resolution policy for the transactions, such as abort, restart, or compensation.
  - The data replication strategy for the transactions, such as primary copy, majority voting, or quorum consensus.
- Concurrency control techniques for RTS should also be compatible with the scheduling algorithms and the communication protocols used in the system.



### Overview of Commercial Real Time databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service.
- Some of the attributes of live real-time databases are:
  - High availability: the database must be accessible and operational at all times, even in the event of failures or disasters.
  - High performance: the database must be able to process large volumes of data and transactions with low latency and high throughput.
  - High scalability: the database must be able to handle increasing workloads and data sizes without compromising the availability and performance.
  - High reliability: the database must ensure the consistency and integrity of the data and transactions, and prevent data loss or corruption.
  - High security: the database must protect the data and transactions from unauthorized access, modification, or deletion.
  - High adaptability: the database must be able to adjust to changing workloads and data characteristics, and support different types of queries and transactions.
  - High interoperability: the database must be able to communicate and integrate with other systems and applications, and support different data formats and protocols.
  - High maintainability: the database must be easy to manage and monitor, and support backup and recovery operations.
  - High usability: the database must be easy to use and understand, and provide a user-friendly interface and documentation.
- Some of the examples of commercial real-time databases are  :
  - Raima Database Manager (RDM): a high-performance, embedded, in-memory database that supports hard and soft real-time applications, and offers ACID transactions, SQL and NoSQL interfaces, replication, encryption, compression, and more.
  - Altus Group: a data and analytics platform that provides historical and current information on commercial real estate deals, markets, and trends, and helps investors and developers make informed decisions.
  - CoStar: a leading provider of commercial real estate data and analytics, that offers comprehensive information on properties, tenants, leases, sales, and market conditions, and supports various tools and services for research, marketing, and valuation.
  - Google Cloud Firestore: a highly scalable, fully managed NoSQL database service for large analytical and operational workloads, that offers up to 99.999% availability, and processes more than 5 billion requests per second at peak, and with more than 10 Exabytes of data under management.

