

## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to perform its intended function or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
  - Hard real time systems have strict deadlines that must be met at all costs, otherwise the system may fail catastrophically or cause severe damage. For example, a pacemaker must deliver electrical pulses to the heart within a certain time interval, otherwise the patient may die.
  - Soft real time systems have deadlines that are desirable but not mandatory, and missing some deadlines may only degrade the system performance or quality of service. For example, a video streaming service may drop some frames or reduce the resolution if the network bandwidth is insufficient, but the user can still watch the video.
- Real time systems have some common characteristics and challenges, such as:
  - Concurrency: Real time systems often have to handle multiple events or tasks simultaneously, and coordinate their execution and communication.
  - Predictability: Real time systems must be able to guarantee that they can meet their deadlines under all possible scenarios and conditions, and avoid any unexpected delays or failures.
  - Resource constraints: Real time systems often have limited resources, such as memory, CPU, power, bandwidth, etc., and must optimize their utilization and allocation.
  - Dependability: Real time systems must be able to cope with faults, errors, or uncertainties, and ensure their correctness, reliability, availability, and security.
- Real time systems require special design methods, tools, and techniques, such as:
  - Real time operating systems (RTOS): An RTOS is a specialized operating system that provides services and features for real time systems, such as scheduling, synchronization, communication, memory management, etc.
  - Real time programming languages (RTPL): An RTPL is a programming language that supports the development of real time systems, such as providing timing constructs, concurrency mechanisms, exception handling, etc.
  - Real time analysis and verification: Real time analysis and verification are techniques that aim to ensure the correctness and feasibility of real time systems, such as checking the timing constraints, resource requirements, fault tolerance, etc.
  - Real time testing and debugging: Real time testing and debugging are techniques that aim to detect and correct the errors or defects of real time systems, such as measuring the timing behavior, tracing the execution, injecting faults, etc.



# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic and aperiodic.
- A periodic system is a system that has events or inputs that occur at regular intervals, such as a sensor reading, a clock tick, or a task execution. The interval between two consecutive occurrences of the same event or input is called the period.
- An aperiodic system is a system that has events or inputs that occur at irregular or unpredictable intervals, such as a user request, a network packet, or a fault. The interval between two consecutive occurrences of the same event or input is called the interarrival time.
- A real time system can also be classified into two types based on the number of processors or cores: uniprocessor and multiprocessor.
- A uniprocessor system is a system that has only one processor or core that executes all the tasks or processes of the system. The processor or core may switch between different tasks or processes using a scheduling algorithm.
- A multiprocessor system is a system that has more than one processor or core that can execute tasks or processes of the system concurrently or in parallel. The processors or cores may communicate with each other using shared memory or message passing.



# Typical Real Time Applications

A real-time application (RTA) is an application that has strict time constraints on its performance and reliability. RTAs often interact with the physical world and require fast and accurate responses to external events. RTAs can be classified into two types: hard real-time and soft real-time. Hard real-time applications have absolute deadlines that must be met, otherwise the system may fail or cause severe consequences. Soft real-time applications have relative deadlines that can be occasionally missed, but the system can still function with reduced quality or performance.

Some examples of typical real-time applications are:

- **Digital control**: Digital control systems use sensors and actuators to monitor and manipulate physical processes, such as temperature, pressure, speed, etc. Digital control systems can be found in many domains, such as aerospace, automotive, manufacturing, robotics, etc. Digital control systems often have hard real-time requirements, as missing or delaying a control action can lead to instability or damage of the system.
- **Optimal control**: Optimal control systems use mathematical models and algorithms to optimize the performance or efficiency of a physical process, such as fuel consumption, power generation, etc. Optimal control systems can also be found in many domains, such as aerospace, automotive, energy, etc. Optimal control systems often have soft real-time requirements, as missing or delaying an optimization action can result in suboptimal or wasteful operation of the system.
- **Command and control**: Command and control systems are used to coordinate and direct the actions of multiple agents, such as humans, machines, or vehicles, in complex and dynamic environments, such as military, emergency, or traffic management. Command and control systems often have mixed real-time requirements, as some actions may have hard deadlines, while others may have soft deadlines or no deadlines at all.
- **Signal processing**: Signal processing systems are used to process, analyze, or transform signals, such as audio, video, radar, etc. Signal processing systems can be used for various purposes, such as communication, encryption, compression, recognition, etc. Signal processing systems often have soft real-time requirements, as missing or delaying a signal processing action can result in degraded quality or performance of the system.
- **Tracking**: Tracking systems are used to monitor and estimate the state or location of a target, such as a person, an object, or a phenomenon, using sensors, such as cameras, radars, etc. Tracking systems can be used for various purposes, such as surveillance, navigation, identification, etc. Tracking systems often have soft real-time requirements, as missing or delaying a tracking action can result in inaccurate or outdated information about the target.
- **Real-time databases**: Real-time databases are databases that store and manipulate data that have temporal constraints, such as deadlines, validity periods, freshness, etc. Real-time databases can be used to support various real-time applications, such as process control, command and control, signal processing, etc. Real-time databases often have mixed real-time requirements, as some data operations may have hard deadlines, while others may have soft deadlines or no deadlines at all.
- **Multimedia**: Multimedia systems are systems that handle multiple types of media, such as text, graphics, audio, video, etc. Multimedia systems can be used for various purposes, such as entertainment, education, communication, etc. Multimedia systems often have soft real-time requirements, as missing or delaying a multimedia action can result in reduced quality or performance of the system.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Real Time System.

### Release Times for the notes of the Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events within a specified time interval, otherwise it may cause undesirable consequences or failure.
- A real time system consists of a set of tasks that must be executed periodically or aperiodically, depending on the arrival of events or requests.
- A task is a unit of computation that has a deadline, which is the latest time by which it must finish its execution.
- A task also has a release time, which is the earliest time at which it can start its execution.
- The release time of a task may be fixed or variable, depending on the type of the task and the system.
- A periodic task is a task that has a fixed release time and a fixed period, which is the time interval between two consecutive releases of the same task.
- For example, a task that monitors the temperature of a reactor every 10 seconds has a fixed release time of 0 and a fixed period of 10 seconds.
- A periodic task can be represented by a tuple (C, T, D), where C is the worst-case execution time, T is the period, and D is the relative deadline, which is equal to or less than the period.
- For example, a task (2, 10, 10) has a worst-case execution time of 2 seconds, a period of 10 seconds, and a relative deadline of 10 seconds.
- A periodic task can also be represented by a timeline, which shows the release times and deadlines of the task instances over time.
- For example, the timeline of the task (2, 10, 10) is shown below:

```
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
0    2    4    6    8    10   12   14   16   18   20   22   24   26   28   30   32   34   36   38
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
|<--->|<--->|<--->|<--->|<--->|<--->|<--->|<--->|<--->|<--->|
  C     C     C     C     C     C     C     C     C     C
|<----------------->|<----------------->|<----------------->|
         T                 T                 T
|<----------------->|<----------------->|<----------------->|
         D                 D                 D
```

- An aperiodic task is a task that has a variable release time and no fixed period, which means that it can arrive at any time and with any frequency.
- For example, a task that handles user inputs or external interrupts is an aperiodic task.
- An aperiodic task can be represented by a tuple (C, D), where C is the worst-case execution time and D is the absolute deadline, which is the latest time by which the task must finish its execution.
- For example, a task (3, 15) has a worst-case execution time of 3 seconds and an absolute deadline of 15 seconds.
- An aperiodic task can also be represented by a timeline, which shows the release times and deadlines of the task instances over time.
- For example, the timeline of the task (3, 15) is shown below, assuming that it arrives at time 5 and 12:

```
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
0    2    4    6    8    10   12   14   16   18   20   22   24   26   28   30   32   34   36   38
|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
     |<--->|              |<--->|
       C                    C
     |

```




# Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Unit 1 - Introduction of Real Time System covers the following topics:

  - Definition and characteristics of real time systems
  - Types and examples of real time systems
  - Real time system design issues and challenges
  - Real time system development life cycle and models
  - Real time system standards and tools

- The notes for Unit 1 - Introduction of Real Time System are expected to be completed by the following deadlines:

  - The first draft of the notes should be submitted by **March 25, 2023** for feedback and review.
  - The final version of the notes should be submitted by **April 5, 2023** for evaluation and grading.

- The notes for Unit 1 - Introduction of Real Time System should follow the following guidelines:

  - The notes should be written in a clear, concise, and coherent manner, using proper grammar, spelling, and punctuation.
  - The notes should include relevant examples, diagrams, tables, and figures to illustrate the concepts and applications of real time systems.
  - The notes should cite the sources of information and references using the APA style.
  - The notes should be formatted using the markdown syntax, with appropriate headings, subheadings, lists, code blocks, and links.
  - The notes should be saved as a .md file and uploaded to the online platform.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of timing constraints for the unit 1 - introduction of real time system in the subject of real time system.

# Timing Constraints

- A real time system is a system that must respond to events within certain time bounds, called timing constraints.
- Timing constraints can be classified into two types: hard and soft.
- Hard timing constraints are those that must be met for the system to function correctly. If a hard timing constraint is violated, the system may fail or cause severe consequences. For example, a pacemaker must deliver electrical pulses to the heart within a precise interval, otherwise the patient may die.
- Soft timing constraints are those that can be violated occasionally without compromising the system functionality, but may degrade the system performance or quality of service. For example, a video streaming application may drop some frames or reduce the resolution if the network bandwidth is insufficient, but the user can still watch the video.
- Timing constraints can be specified in different ways, such as deadlines, periodicity, jitter, latency, and response time.
- A deadline is the latest time by which a task or an event must be completed or processed. A deadline can be absolute or relative. An absolute deadline is a fixed point in time, such as 10:00 AM. A relative deadline is an offset from the occurrence of an event, such as 5 seconds after receiving a request.
- A periodic task or event is one that occurs or must be executed at regular intervals, such as every 10 milliseconds. The interval between two consecutive occurrences or executions is called the period. A periodic task or event may have a deadline equal to or less than its period.
- Jitter is the variation in the arrival time or execution time of a task or an event. Jitter can cause uncertainty and unpredictability in the system behavior. For example, if a sensor sends data to a processor with a jitter of 1 millisecond, the processor may receive the data at different times within a 1 millisecond window.
- Latency is the delay between the occurrence of an event and the start of its processing. Latency can be caused by factors such as communication, scheduling, and synchronization. For example, if a camera captures an image and sends it to a processor, the latency is the time between the image capture and the processor receiving the image.
- Response time is the delay between the occurrence of an event and the completion of its processing. Response time can be measured as the sum of latency and execution time. For example, if a processor receives an image from a camera, processes it, and displays it on a screen, the response time is the time between the image capture and the image display.



# Hard Real Time Systems

- A hard real-time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur .
- Examples of hard real-time systems are flight control systems, nuclear reactor control systems, pacemakers, airbag systems, etc.  .
- Hard real-time systems require a real-time operating system (RTOS) that can manage the tasks and resources with minimal overhead and latency .
- Hard real-time systems are often designed with redundancy and fault tolerance to ensure reliability and safety .



# Soft Real Time Systems

- A soft real time system is a system that has a **flexible deadline** for completing its tasks, meaning that it can tolerate some **delay** or **jitter** in the execution time without causing a **system failure** or a **significant degradation** in the quality of service   .
- A soft real time system is typically used to handle **concurrent** and **dynamic** situations where the system needs to **adapt** to changing conditions and **update** the state of multiple connected components.
- Some examples of soft real time systems are:
  - **Multimedia applications** such as streaming audio and video, where a small delay or loss of data does not affect the overall user experience .
  - **Network protocols** such as TCP/IP, where packets can be retransmitted or dropped if the network is congested or unreliable.
  - **Air traffic control systems** such as flight planning and scheduling, where the system can adjust the routes and timings of the flights based on the weather, traffic, and other factors.
- The main characteristics of soft real time systems are:
  - They have **non-deterministic** timing behavior, meaning that the execution time of a task can vary depending on the system load, the input data, the hardware, and other factors  .
  - They have **probabilistic** timing requirements, meaning that the system can specify a **desired** or **average** deadline for a task, but not a **guaranteed** or **worst-case** deadline  .
  - They have **degradable** performance, meaning that the system can **trade-off** the quality of the output or the service for the timeliness of the execution, depending on the **priority** or the **importance** of the task   .
  - They can run on **multiprocessor** or **multicore** platforms, meaning that the system can **distribute** the workload among multiple processing units and **exploit** the parallelism and the concurrency of the tasks .
  - They have **fewer** or **looser** restrictions on the applications, meaning that the system can **support** a wider range of functionalities and features, such as dynamic memory allocation, garbage collection, exception handling, and so on .



# Reference Models for Real Time Systems

A reference model is a conceptual framework that defines the essential features and characteristics of a real time system. It helps to understand, analyze, design, and evaluate real time systems in a consistent and systematic way. A reference model is not a specific system design, but rather a general template that can be instantiated for different applications and domains.

There are different reference models for real time systems, depending on the level of abstraction, the scope of coverage, and the focus of attention. Some of the common reference models are:

- **Real-time Control System (RCS)**: This is a reference model architecture that combines real-time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis. It is suitable for many software-intensive, real-time computing control problem domains, such as robotics, manufacturing, and aerospace. The RCS model consists of a hierarchical structure of nodes, each of which performs a specific function and communicates with other nodes through a network. The nodes are organized into three layers: the sensory processing layer, the state estimation layer, and the goal decomposition layer. The sensory processing layer collects and processes data from various sensors, such as cameras, microphones, and touch sensors. The state estimation layer uses the sensory data to estimate the current state of the system and the environment, such as the position, orientation, velocity, and shape of objects. The goal decomposition layer uses the state information to generate and execute plans to achieve the desired goals, such as moving, grasping, or manipulating objects. The RCS model can be implemented using various software and hardware platforms, such as Java, C++, Linux, Windows, or embedded systems.

- **Reference Model of Real-Time Systems**: This is a reference model that focuses on the timing behavior of the systems, and provides a consistent terminology and notation to reason about real-time systems  . It is characterized by three elements: a workload model, a resource model, and a system model. The workload model specifies the applications supported by the system, such as tasks, jobs, deadlines, resource dependencies, and precedence constraints. The resource model describes the resources available in the system, such as processors, memory, network, and devices, and their types and relations. The system model defines the policies and mechanisms used by the system to manage the resources and the workload, such as scheduling algorithms, synchronization protocols, and fault tolerance techniques. The reference model can be used to analyze the performance, feasibility, and optimality of real-time systems, and to compare and evaluate different system designs and implementations.

- **Real Time Systems**: This is a reference model that covers the basic concepts and principles of real-time systems, and provides a comprehensive overview of the various aspects and challenges of real-time systems. It is divided into four parts: introduction, specification and design, implementation, and validation and verification. The introduction part introduces the definition, characteristics, and classification of real-time systems, and the common application domains and examples of real-time systems. The specification and design part discusses the methods and tools for specifying and designing real-time systems, such as requirements analysis, modeling languages, design patterns, and architectures. The implementation part presents the techniques and technologies for implementing real-time systems, such as programming languages, operating systems, middleware, and communication protocols. The validation and verification part describes the approaches and standards for testing and verifying the correctness and quality of real-time systems, such as simulation, debugging, testing, and certification.

These are some of the reference models for real time systems that can be used for studying and learning the subject of real time system. They provide different perspectives and levels of detail on the essential features and characteristics of real time systems, and can help to understand, analyze, design, and evaluate real time systems in a consistent and systematic way.



# Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can use it at a time. Examples of resources are memory, files, printers, and sensors.
- Processors and resources can be classified into two categories: preemptable and non-preemptable.
- Preemptable processors or resources can be interrupted and resumed by another job. For example, a CPU can be preempted by a higher priority job and resume the execution of the lower priority job later.
- Non-preemptable processors or resources cannot be interrupted and resumed by another job. For example, a printer cannot be preempted by another job until it finishes printing the current job.
- Processors and resources can also be classified into two categories: dedicated and shared.
- Dedicated processors or resources are assigned to a single job and cannot be used by any other job. For example, a dedicated CPU can only execute one job at a time.
- Shared processors or resources can be used by multiple jobs, but only one job can use them at a time. For example, a shared memory can be accessed by multiple jobs, but only one job can read or write to it at a time.
- Processors and resources can affect the performance and correctness of real-time systems. Therefore, they need to be managed and scheduled properly to meet the timing constraints and quality of service requirements of the real-time applications .



# Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and behavior .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The time when the job becomes available for execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The time by which the job must finish its execution. It may be fixed or variable depending on the system and the job.
  - **Relative deadline (D<sub>i</sub>)**: The maximum time allowed for the job to complete its execution after its release time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The interval of time during which the job can be executed. It is equal to the relative deadline minus the execution time of the job.
- The temporal parameters of a job determine its priority, schedulability and performance in a real time system .
- A real time system must ensure that all the jobs meet their temporal parameters and constraints, otherwise the system may fail or produce incorrect results .



# Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, 
  - Φi – is the phase of the task, which is the time instant when the first job of the task is released.
  - Pi – is the period of the task, which is the time interval between two consecutive job releases of the task.
  - ei – is the worst-case execution time of the task, which is the maximum time required by any job of the task to complete its execution on a given processor.
  - Di – is the relative deadline of the task, which is the maximum time allowed for any job of the task to finish its execution after its release.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a priority Pi for each task τi, to specify the order of execution of the tasks in case of resource contention.
- The periodic task model can be used to analyze the schedulability of a set of tasks on a single processor or a multiprocessor system, using various scheduling algorithms, such as rate-monotonic, earliest-deadline-first, or fixed-priority  .



# Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real-time systems.
- Precedence constraints are imposed by the logical or temporal order of the jobs, while data dependency is caused by the communication or sharing of data among the jobs.
- Precedence constraints can be represented by a directed graph, called a precedence graph, where the vertices are the jobs and the edges indicate the precedence relations. A job J_i is a predecessor of another job J_k (and J_k a successor of J_i) if J_k cannot begin execution until the execution of J_i completes  .
- Data dependency cannot be captured by a precedence graph. In many real-time systems, jobs communicate via shared data, such as buffers, queues, or variables. A job J_i is data dependent on another job J_k if J_i needs to read or write some data that is produced or consumed by J_k .
- Precedence constraints and data dependency may affect the schedulability and feasibility of real-time systems. They may introduce delays, blocking, or deadlocks in the execution of the jobs. Therefore, they need to be considered in the design and analysis of real-time systems. Some possible solutions are to use synchronization mechanisms, such as semaphores, locks, or monitors, to ensure mutual exclusion and data consistency, or to use data replication or partitioning techniques to reduce data contention and communication overhead  .



# Unit 2 - Real Time Scheduling

Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines. Real time scheduling aims to ensure that the system can respond to events and requests in a timely and predictable manner, without missing any deadlines or compromising the quality of service.

Some of the topics covered in this unit are:

- **Real time system**: A system that has to react to events or requests within a specified time interval, otherwise it may cause unacceptable consequences or failures. Examples of real time systems are air traffic control, industrial automation, multimedia applications, etc.
- **Real time task**: A task that has a timing constraint or deadline associated with it, which specifies the latest time by which the task has to be completed. A real time task can be periodic, aperiodic, or sporadic, depending on the pattern of its arrival or activation.
- **Real time scheduler**: A component of a real time system that decides which task to execute at any given time, based on the priority, deadline, and resource requirements of the tasks. A real time scheduler can be preemptive or non-preemptive, depending on whether it can interrupt a running task or not.
- **Real time scheduling algorithm**: A rule or method that determines the priority and order of execution of the tasks in a real time system. A real time scheduling algorithm can be static or dynamic, depending on whether the priority of the tasks is fixed or can change during the execution. Some examples of real time scheduling algorithms are rate-monotonic, earliest deadline first, least laxity first, etc.
- **Real time schedulability**: A property of a real time system that indicates whether it can meet all the deadlines of the tasks under a given scheduling algorithm and workload. A real time system is said to be schedulable if it can guarantee that no deadline will be missed. A real time system can be analyzed for schedulability using various methods, such as utilization bound, response time analysis, simulation, etc.



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning tasks to processors or resources in a way that meets the timing constraints of the system. Real time systems are those whose correctness depends on both the functionality and the timing of the tasks. There are different approaches to real time scheduling, depending on the characteristics and requirements of the system. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, period, etc., are known at design time. In this approach, a static schedule is generated offline, based on the worst-case execution times of the tasks, and stored in a table. The table specifies the exact time instants when each task should start and finish execution. A timer interrupts the system at these time instants and triggers the execution of the corresponding task. The advantage of this approach is that it guarantees the schedulability of the tasks and avoids runtime overhead. The disadvantage is that it is inflexible and cannot handle dynamic changes in the system, such as task arrivals, resource failures, or variations in execution times   .

- **Round-robin approach**: This approach is a commonly used technique in time-shared systems. It is based on dividing the processor time into equal slices, called quantum or time slice, and allocating them to the tasks in a circular order. Each task gets a chance to execute for one quantum, and then it is preempted and moved to the end of the ready queue. The next task in the queue gets the processor for the next quantum, and so on. The advantage of this approach is that it is simple and fair, and it provides a good average response time for the tasks. The disadvantage is that it does not consider the priority or the deadline of the tasks, and it may cause unnecessary preemptions and context switches .

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach, where each task is assigned a weight that reflects its relative importance or urgency. The weight determines the number of quanta that the task gets in each round. For example, a task with weight 2 gets two quanta, while a task with weight 1 gets one quantum. The advantage of this approach is that it can differentiate between the tasks based on their weights, and it can provide a better service to the more critical tasks. The disadvantage is that it still does not consider the exact deadline of the tasks, and it may cause some tasks to miss their deadlines if their weights are not properly assigned .

- **Priority-driven approach**: This approach is based on assigning a priority to each task, either statically or dynamically, and scheduling the tasks according to their priorities. The task with the highest priority gets the processor, and it can preempt any lower priority task that is currently executing. The priority of a task can be determined by various factors, such as its deadline, its period, its criticality, its resource requirements, etc. The advantage of this approach is that it can handle dynamic changes in the system, such as task arrivals, resource failures, or variations in execution times, and it can provide a better guarantee for the schedulability of the tasks. The disadvantage is that it may cause priority inversion, where a high priority task is blocked by a low priority task that holds a shared resource, or starvation, where a low priority task is indefinitely postponed by higher priority tasks    .

Some examples of priority-driven scheduling algorithms are:

  - **Rate-monotonic scheduling (RMS)**: This is a static priority scheduling algorithm, where the priority of a task is inversely proportional to its period. That is, the shorter the period, the higher the priority. This algorithm is optimal for periodic tasks with implicit deadlines (equal to their periods) and fixed execution times, meaning that it can schedule any set of tasks that is schedulable by any other static priority algorithm  .

  - **Deadline-monotonic scheduling (DMS)**: This is a static priority scheduling algorithm, where the priority of a task is inversely proportional to its relative deadline. That is, the shorter the deadline, the higher the priority. This algorithm is optimal for periodic or sporadic tasks with arbitrary



# Clock Driven Approach

- Clock driven approach is also known as time driven approach or cyclic scheduling .
- In this approach, the system executes tasks according to a predetermined schedule .
- The schedule is computed offline before the system starts running  .
- The schedule is based on the known parameters of the tasks, such as period, deadline, execution time, and precedence constraints  .
- The schedule is usually stored in a table or a cyclic executive  .
- The system follows the schedule at each clock interrupt, which occurs at regular intervals  .
- The system does not depend on the events, such as task arrivals or completions, that occur in the system  .
- The advantages of clock driven approach are  :
  - It is predictable and deterministic, which is desirable for hard real-time systems.
  - It is easy to verify the schedulability of the tasks and the correctness of the system.
  - It avoids the overhead of dynamic scheduling, such as priority assignment, queue management, and context switching.
  - It does not exhibit the anomalous timing behavior of priority driven systems, such as priority inversion or deadline misses.
- The disadvantages of clock driven approach are  :
  - It is inflexible and rigid, which makes it difficult to handle dynamic changes in the system, such as task arrivals, failures, or resource variations.
  - It is inefficient and wasteful, as it may leave some processor idle time or unused resources.
  - It is complex and tedious, as it requires a careful analysis and design of the schedule for all possible scenarios and modes of operation.
  - It is not scalable, as it may not be feasible to compute and store the schedule for a large number of tasks or a long time horizon.



# Weighted Round Robin Approach

- The weighted round robin (WRR) algorithm is a variation of the basic round robin (RR) algorithm that assigns different weights to different jobs based on their importance or priority .
- The WRR algorithm has been used for scheduling real-time traffic in high-speed switched networks, where different types of packets may have different quality of service (QoS) requirements .
- The WRR algorithm works as follows:
  - Each job in the ready queue is assigned a weight that represents its share of the processor time. The weight can be a fixed value or a dynamic value that changes over time.
  - The algorithm maintains a pointer that points to the current job in the queue. The pointer is initialized to point to the first job in the queue.
  - The algorithm allocates the processor to the current job for a time slice that is proportional to its weight. For example, if the weight of the current job is 3 and the time slice unit is 1, then the job gets 3 time slices of the processor.
  - After the current job finishes its time slice, the pointer moves to the next job in the queue. If the end of the queue is reached, the pointer wraps around to the first job in the queue.
  - The algorithm repeats the above steps until all the jobs in the queue are completed or preempted by a higher priority job.
- The advantages of the WRR algorithm are:
  - It is simple and easy to implement.
  - It can handle different types of jobs with different QoS requirements by adjusting their weights.
  - It can achieve a fair allocation of the processor among the jobs, as each job gets a share of the processor that is proportional to its weight.
- The disadvantages of the WRR algorithm are:
  - It may cause starvation of low-weight jobs if the high-weight jobs dominate the queue.
  - It may not be suitable for hard real-time systems, as it does not guarantee the deadlines of the jobs.
  - It may not be optimal for minimizing the average response time or the average waiting time of the jobs, as it does not consider the job lengths or arrival times.



# Priority Driven Approach

- The priority driven approach is a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur .
- In a priority driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- The priority driven approach is primarily used for more dynamic real-time systems with a mix of time-based and event-based activities, where the system must adapt to changing conditions and events.
- The priority driven approach can improve the real-time performance and predictability of real-time systems by reducing the response time and deadline misses of high-priority tasks.
- The priority driven approach can also support different types of tasks, such as periodic, sporadic, aperiodic, and mixed tasks, with different characteristics and constraints .
- The priority driven approach can be implemented using different priority assignment schemes, such as fixed priority, dynamic priority, or hybrid priority .
- The priority driven approach can also be combined with other techniques, such as resource reservation, admission control, or overload handling, to enhance the system robustness and quality of service .



# Dynamic Versus Static Systems

- A **static system** is one where the tasks and their attributes (such as arrival time, execution time, deadline, priority, etc.) are known in advance and do not change during the system execution. A static system can be scheduled offline, i.e., before the system runs, using a **static scheduling algorithm** that assigns a fixed priority to each task .
- A **dynamic system** is one where the tasks and their attributes may vary unpredictably during the system execution. A dynamic system requires online scheduling, i.e., during the system runs, using a **dynamic scheduling algorithm** that adjusts the priority of each task according to the current system state .
- Static systems are easier to analyze and validate than dynamic systems, since they have a fixed set of tasks and parameters. Static systems are suitable for hard real-time systems, where missing a deadline can have catastrophic consequences .
- Dynamic systems are more flexible and adaptable than static systems, since they can handle changes in the workload and the environment. Dynamic systems are suitable for soft real-time systems, where missing a deadline can have acceptable degradation in performance .
- Static scheduling algorithms are simpler and faster than dynamic scheduling algorithms, since they do not need to monitor the system state or make decisions at runtime. Static scheduling algorithms can achieve optimal utilization of the system resources, if the tasks are periodic and independent .
- Dynamic scheduling algorithms are more complex and slower than static scheduling algorithms, since they need to monitor the system state and make decisions at runtime. Dynamic scheduling algorithms can handle aperiodic and dependent tasks, as well as overload and fault situations .
- Static systems can be centralized or distributed, i.e., the scheduling decisions can be made at one central site or at multiple sites cooperatively. Centralized static systems are easier to design and implement, but they have a single point of failure and a communication bottleneck. Distributed static systems are more robust and scalable, but they have higher communication and synchronization overhead.
- Dynamic systems can also be centralized or distributed, i.e., the scheduling decisions can be made at one central site or at multiple sites cooperatively. Centralized dynamic systems have the advantage of global information and coordination, but they have the disadvantage of high complexity and latency. Distributed dynamic systems have the advantage of local information and autonomy, but they have the disadvantage of inconsistency and instability.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the optimality of EDF and LST algorithms for real time scheduling.

# Optimality of EDF and LST Algorithms

## EDF Algorithm

- EDF stands for Earliest Deadline First.
- It is a dynamic priority-driven scheduling algorithm used in real time systems.
- It assigns the highest priority to the task with the shortest deadline at every scheduling point.
- It is optimal for preemptive single processor systems, meaning that it can schedule any feasible set of tasks without missing any deadlines.
- It can also be extended to multiprocessor systems, but it is not optimal in general.
- It may suffer from high context switching overhead and priority inversion problems.

## LST Algorithm

- LST stands for Least Slack Time First.
- It is another dynamic priority-driven scheduling algorithm used in real time systems.
- It assigns the highest priority to the task with the least slack time at every scheduling point, where slack time is the difference between the deadline and the remaining execution time of the task.
- It is also optimal for preemptive single processor systems, and it is equivalent to EDF when all the tasks have the same execution time.
- It can also be applied to multiprocessor systems, but it is not optimal in general.
- It may have better performance than EDF in terms of reducing the number of missed deadlines and the average response time of the tasks, especially when the tasks have variable execution times.
- However, it may be impractical to implement LST in some real time systems, because it requires the accurate estimation of the execution time of the tasks, which may be difficult or impossible to obtain.



# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- RMA is preemptive in nature, meaning that a higher priority task can interrupt a lower priority task at any time .
- RMA is optimal for periodic tasks with fixed deadlines, meaning that it can always schedule any set of tasks that is schedulable by any other static-priority algorithm  .
- RMA has a simple schedulability test that can determine if a set of tasks can meet all their deadlines under RMA. The test is based on the utilization factor of the tasks, which is the ratio of their execution time to their period  .
- The schedulability test for RMA is:

  - For n tasks, the utilization factor U must satisfy U <= n(2^(1/n) - 1), which is a sufficient but not necessary condition  .
  - For n tasks, the utilization factor U must satisfy U <= n, which is a necessary but not sufficient condition  .
  - For n tasks, if U <= 0.69, then the set of tasks is always schedulable under RMA, which is a sufficient and necessary condition .

- RMA has some advantages and disadvantages:

  - Advantages:
    - Simple and easy to implement .
    - Optimal for periodic tasks with fixed deadlines .
    - Provides predictable and deterministic behavior.
  - Disadvantages:
    - Not suitable for aperiodic or sporadic tasks .
    - Not suitable for tasks with variable deadlines or execution times .
    - May suffer from priority inversion, where a low priority task blocks a high priority task due to shared resources .



# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler makes each scheduling decision without knowledge about the tasks that will be released in future and parameter of each task known to scheduler only after release of task.
- Offline scheduling has the advantage of being optimal and predictable, as the scheduler can allocate the resources to the tasks in the best possible way and avoid any deadline violations or resource conflicts.
- Online scheduling has the advantage of being flexible and adaptive, as the scheduler can handle dynamic changes in the system such as arrival of new tasks, variations in execution time, or failures of resources.
- Offline scheduling has the disadvantage of being rigid and static, as the scheduler cannot cope with any uncertainty or unpredictability in the system such as changes in task parameters, workload, or environment.
- Online scheduling has the disadvantage of being complex and heuristic, as the scheduler has to make quick and efficient decisions based on limited and incomplete information and trade-off between different objectives and constraints.
- Offline scheduling is suitable for systems that have fixed and known set of tasks, deterministic and constant execution time, and no external disturbances or interferences.
- Online scheduling is suitable for systems that have variable and unknown set of tasks, stochastic and varying execution time, and external disturbances or interferences.
- Examples of offline scheduling are table-driven scheduling, cyclic scheduling, and time-triggered scheduling.
- Examples of online scheduling are priority-driven scheduling, event-triggered scheduling, and hybrid scheduling.



# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user requests, interrupts, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time between successive instances, but no fixed arrival pattern. They have hard or firm deadlines and are usually generated by external events. Examples are sensor readings, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, criticality, etc. The scheduler always selects the highest priority job that is ready to execute. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign priorities to jobs based on a predefined schedule that is computed offline. The scheduler follows the schedule and switches jobs at predefined instants. Examples are cyclic executive, time triggered, etc.

## Scheduling Aperiodic and Sporadic jobs in Priority Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the schedulability of periodic jobs.
- There are two main approaches to schedule aperiodic and sporadic jobs in priority driven systems: background scheduling and server-based scheduling.
- Background scheduling is a simple approach that assigns the lowest priority to aperiodic and sporadic jobs, and executes them only when no periodic job is ready. This ensures that periodic jobs always meet their deadlines, but it may result in poor response time for aperiodic and sporadic jobs.
- Server-based scheduling is a more sophisticated approach that allocates a portion of the processor time to aperiodic and sporadic jobs, and treats them as periodic tasks with a certain budget and period. This allows aperiodic and sporadic jobs to execute at higher priorities than some periodic jobs, and improves their response time. However, it may also introduce some overhead and complexity in the system.
- There are different types of servers that can be used to schedule aperiodic and sporadic jobs in priority driven systems, such as polling server, deferrable server, sporadic server, priority exchange server, etc. Each server has its own advantages and disadvantages, and the choice of the server depends on the system requirements and characteristics.

## Scheduling Aperiodic and Sporadic jobs in Clock Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to handle the unpredictability and variability of their arrival and execution times, and to accommodate them in the predefined schedule without violating the deadlines of periodic jobs.
- There are two main approaches to schedule aperiodic and sporadic jobs in clock driven systems: slack stealing and dynamic scheduling.
- Slack stealing is an approach that exploits the unused processor time or slack in the schedule to execute aperiodic and sporadic jobs. The scheduler monitors the slack in the schedule and assigns it to the highest priority aperiodic or sporadic job that is ready. This improves the response time of aperiodic and sporadic jobs, but it may also introduce some overhead and complexity in the system.
- Dynamic scheduling is an approach that modifies the schedule at runtime to accommodate aperiodic and sporadic jobs. The scheduler uses some online algorithm, such as earliest deadline first, to select the next job to execute, and adjusts the schedule accordingly. This allows aperiodic and sporadic jobs to execute at higher priorities than some periodic jobs, but it may also result in schedule instability and unpredictability.



# Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of one computer system available to other computer systems on a network. Resource sharing can improve the efficiency, performance, and reliability of distributed systems by allowing multiple users and applications to access and utilize the same resources.

Some examples of resources that can be shared are:

- Files and directories: Users can store, retrieve, and modify data on remote file systems as if they were local.
- Printers and scanners: Users can send documents to print or scan on remote devices without having to physically connect them to their own computers.
- CPU and memory: Users can run programs or tasks on remote computers that have more processing power or memory than their own computers.
- Software and applications: Users can access and use software and applications that are installed on remote computers without having to install them on their own computers.
- Databases and web servers: Users can query and update data on remote databases or access web pages and services hosted on remote web servers.

Resource sharing can be implemented in different ways depending on the network architecture, the type of resources, and the level of abstraction. Some common methods of resource sharing are:

- File transfer: Users can copy files from one computer to another using protocols such as FTP, SCP, or HTTP.
- Remote login: Users can log in to a remote computer and execute commands or run programs using protocols such as SSH, Telnet, or RDP.
- Remote procedure call: Users can invoke procedures or functions on a remote computer and receive the results using protocols such as RPC, SOAP, or REST.
- Distributed file system: Users can access and manipulate files and directories on a remote computer as if they were local using protocols such as NFS, SMB, or HDFS.
- Distributed computing: Users can run programs or tasks on a remote computer that can be parallelized or distributed using frameworks such as MPI, MapReduce, or Spark.
- Cloud computing: Users can access and use resources such as storage, computation, or software that are provided by a remote service provider over the internet using platforms such as AWS, Azure, or Google Cloud.



# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a shared memory, a communication channel, a peripheral device, etc.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- RAC aims to minimize the undesirable effects of resource contention and ensure the correctness and timeliness of tasks.
- Some of the common RAC protocols are:
  - Priority inheritance protocol (PIP): A task that holds a resource inherits the priority of any higher-priority task that requests the same resource, and restores its original priority when it releases the resource. This protocol prevents unbounded priority inversion and ensures that the highest-priority task that needs the resource will eventually get it.
  - Priority ceiling protocol (PCP): A task that requests a resource is blocked if there is a higher-priority task that may also request the same resource, even if the resource is currently available. This protocol prevents deadlock and reduces the blocking time of tasks. It also requires assigning a priority ceiling to each resource, which is the highest priority of any task that may request it.
  - Stack resource policy (SRP): A task that requests a resource is blocked if there is a higher-priority task that may also request any resource currently held by a lower-priority task, even if the requested resource is available. This protocol prevents deadlock and reduces the blocking time of tasks. It also requires assigning a preemption level to each task, which is the highest priority of any resource that it may request.
  - Non-preemptive critical sections (NPCS): A task that enters a critical section (a section of code that accesses a shared resource) cannot be preempted by any other task until it exits the critical section. This protocol prevents priority inversion and deadlock, but it may increase the response time of higher-priority tasks and introduce timing anomalies.



# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables.
- Non-preemptive means that once a job enters a critical section, it cannot be interrupted or preempted by another job until it finishes the critical section .
- This implies that when a job requests a resource, it is always allocated the resource, and when a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- The advantages of non-preemptive critical sections are:
  - They are simple to implement and understand.
  - They prevent deadlock, since no job is ever preempted when it holds any resource.
  - They preserve the temporal correctness of the system, since no job can miss its deadline due to blocking by a lower-priority job.
- The disadvantages of non-preemptive critical sections are:
  - They can cause priority inversion, where a higher-priority job is blocked by a lower-priority job that holds a resource.
  - They can reduce the processor utilization, since a job holding a resource may not use the processor fully while blocking other jobs.
  - They can increase the response time and jitter of the system, since a job may have to wait for a long time before entering a critical section.



# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Both protocols aim to prevent unbounded priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource.
- Both protocols also aim to prevent deadlock, which is a situation where two or more tasks are waiting for each other to release a resource.

## Priority-Inheritance Protocol

- The basic idea of priority-inheritance protocol is that when a high-priority task is blocked by a low-priority task that holds a resource, the low-priority task inherits the priority of the high-priority task until it releases the resource.
- This way, the low-priority task can finish its critical section faster and unblock the high-priority task sooner.
- The priority-inheritance protocol has the following properties:
  - It is greedy, meaning that a task can access a resource whenever it is free, regardless of the priorities of other tasks that may request the same resource later.
  - It is transitive, meaning that if a task inherits the priority of another task, it also inherits the priority of any other task that the latter task inherits from.
  - It is dynamic, meaning that the priority of a task can change during its execution depending on the blocking situation.
  - It guarantees that the blocking time of a task is bounded by the duration of the longest critical section of any lower-priority task that shares a resource with it .

## Priority-Ceiling Protocol

- The basic idea of priority-ceiling protocol is that each resource is assigned a priority ceiling, which is the highest priority of any task that can access that resource.
- A task can access a resource only if its priority is higher than the priority ceiling of all the resources currently held by other tasks.
- This way, the priority-ceiling protocol prevents a task from being blocked by a lower-priority task that does not hold the requested resource, which is called avoidance blocking.
- The priority-ceiling protocol has the following properties:
  - It is not greedy, meaning that a task may be denied access to a free resource if its priority is lower than the priority ceiling of another resource held by another task.
  - It is not transitive, meaning that a task does not inherit the priority of any other task that holds a resource.
  - It is static, meaning that the priority of a task does not change during its execution.
  - It guarantees that the blocking time of a task is bounded by the duration of a single (outermost) critical section of any lower-priority task that shares a resource with it .

## Comparison

- The priority-ceiling protocol is better than the priority-inheritance protocol in terms of reducing the blocking time, preventing deadlock, and simplifying the analysis of schedulability  .
- However, the priority-ceiling protocol requires a priori knowledge of the resource usage and priority assignment of all the tasks, which may not be available or feasible in some situations .
- The priority-inheritance protocol is more flexible and adaptable to dynamic changes in the system, but it may incur more overhead and complexity in the implementation .



# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share a common run-time stack, in order to reduce overall memory demand.
- SBPCP is based on the original ceiling priority protocol (OCPP), which assigns a ceiling priority to each resource and raises the priority of a job that accesses a resource to the ceiling priority of that resource .
- SBPCP differs from OCPP in two ways :
  - SBPCP uses a scheduling rule that prevents a job from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at any time.
  - SBPCP uses an allocation rule that allows a job to access a resource only if its assigned priority is higher than the ceiling priority of all the resources that are currently in use, except the ones that are already allocated to the job.
- SBPCP has the following properties  :
  - SBPCP prevents deadlock, since a job cannot access a resource that is already allocated to a lower-priority job, and a job cannot be blocked by a lower-priority job that is waiting for a resource.
  - SBPCP prevents unbounded priority inversion, since a job can be blocked by at most one lower-priority job, and the blocking time is bounded by the maximum execution time of the blocking job.
  - SBPCP is optimal for fixed-priority scheduling, since it guarantees that the highest-priority job that is ready to execute will always run, and no job will miss its deadline if the system is feasible.
  - SBPCP is stack-optimal, since it minimizes the number of stack frames that are needed to execute the jobs, and it ensures that the stack size is bounded by the maximum number of jobs that can be active at any time.



# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- This ensures that a higher priority task will not be blocked by a lower priority task that holds a resource .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a table that stores the priority ceiling of each resource for each possible priority level of the tasks .
- For example, consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline driven system as below :

| Time | T1 | T2 | Priority |
|------|----|----|----------|
| 0    | 1  | 2  | T1 > T2  |
| 1    | 1  | 2  | T1 > T2  |
| 2    | 1  | 2  | T1 > T2  |
| 3    | 1  | 2  | T1 > T2  |
| 4    | 2  | 1  | T2 > T1  |
| 5    | 2  | 1  | T2 > T1  |
| 6    | 2  | 1  | T2 > T1  |
| 7    | 2  | 1  | T2 > T1  |

- Suppose both tasks need to access a shared resource X. The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The table for the priority ceiling of X is as follows:

| Priority | Ceiling |
|----------|---------|
| 1        | 2       |
| 2        | 1       |

- The system ceiling is initially 0 and changes according to the resource locking and unlocking by the tasks .
- If T1 locks X at time 0, the system ceiling becomes 2 and T2 cannot lock X until T1 releases it .
- If T2 locks X at time 4, the system ceiling becomes 1 and T1 cannot lock X until T2 releases it .
- This way, the priority ceiling protocol prevents deadlock and priority inversion in dynamic priority systems .



# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Mutual deadlock is a situation where two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Preemption ceiling protocol assigns a ceiling priority to each shared resource, which is the highest priority of any task that can access the resource .
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks .
- When a task locks a resource, its priority is temporarily raised to the ceiling priority of the resource, and it cannot be preempted by any other task until it releases the resource .
- Preemption ceiling protocol guarantees that a task can be blocked by at most one lower-priority task, and that deadlock is impossible .
- Preemption ceiling protocol can be applied to both static-priority and dynamic-priority systems, such as rate-monotonic and earliest-deadline-first scheduling .
- Preemption ceiling protocol can be implemented in two ways: original ceiling protocol (OCP) and immediate ceiling protocol (ICP).
  - OCP raises the priority of a task only when it is blocked by a lower-priority task that holds a resource.
  - ICP raises the priority of a task as soon as it locks a resource, regardless of whether it is blocked or not.
  - ICP has better performance than OCP in terms of response time, blocking time, and context switches.
- Preemption ceiling protocol can be extended to support nested resources, multiple resources, and inheritance relations among resources .
- Preemption ceiling protocol can also be combined with other techniques, such as preemption threshold scheduling (PTS), to achieve better scalability and flexibility for real-time systems .
  - PTS allows a task to specify a preemption threshold, which is the lowest priority level at which it can be preempted.
  - PTS reduces the number of preemptions and context switches, and improves the schedulability of fixed-priority systems.
  - PTS can be integrated with preemption ceiling protocol to handle synchronization issues among tasks that share resources .
  - PTS can also be adapted to dynamic-priority systems, such as deadline-driven systems, by using fixed preemption levels.



# Access Control in Multiple-Unit Resources

- A multiple-unit resource is a resource that can be used by more than one job at a time, such as a printer, a disk, or a network interface.
- A multiple-unit resource can be modeled as having many units, each used mutually exclusively and non-preemptively by a job. For example, a printer with four trays can be modeled as having four units of the resource.
- Access to multiple-unit resources is controlled using locks. A job must lock a unit of the resource before using it, and unlock it after using it. The time the resource is locked is the critical section of the job.
- The challenge of access control in multiple-unit resources is to ensure that the jobs are scheduled in a way that avoids deadlock, priority inversion, and unnecessary blocking.
- There are different protocols for access control in multiple-unit resources, such as:
  - The **Priority Inheritance Protocol (PIP)**: A job that locks a unit of a resource inherits the priority of the highest-priority job that is blocked on that resource. The job releases the inherited priority when it unlocks the resource.
  - The **Priority Ceiling Protocol (PCP)**: Each unit of a resource is assigned a priority ceiling, which is the highest priority of any job that can lock that unit. A job can lock a unit of a resource only if its priority is higher than the priority ceilings of all the units of the resources that are currently locked. A job that locks a unit of a resource inherits the priority ceiling of that unit. The job releases the inherited priority when it unlocks the resource.
  - The **Stack Resource Policy (SRP)**: Each job has a preemption level, which is assigned statically and does not change during execution. A job can lock a unit of a resource only if its preemption level is higher than the preemption levels of all the jobs that have locked any unit of any resource. A job that locks a unit of a resource pushes the preemption level of that unit onto a stack. The preemption level of the unit is the highest preemption level of any job that can lock that unit. The job pops the preemption level of the unit from the stack when it unlocks the resource.
- These protocols have different properties and trade-offs, such as:
  - The PIP is simple to implement, but it can cause long blocking times and unbounded priority inversion.
  - The PCP and the SRP can prevent deadlock and bound the blocking time and the priority inversion of any job. However, they require more information about the resource usage of the jobs and the priority ceilings or the preemption levels of the resources.
  - The PCP and the SRP are not equivalent. The PCP can cause more blocking than the SRP, but the SRP can cause more preemptions than the PCP. The choice of the protocol depends on the characteristics of the system and the application.



# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timeliness.
- Concurrency control algorithms for real time systems can be classified into two categories: locking-based and optimistic.
- Locking-based algorithms use locks to grant exclusive access to data objects to one job at a time. They can be further divided into static and dynamic locking algorithms.
- Static locking algorithms assign locks to data objects before the execution of jobs, based on their priority or deadline. Examples of static locking algorithms are priority ceiling protocol (PCP) and immediate ceiling protocol (ICP).
- Dynamic locking algorithms assign locks to data objects during the execution of jobs, based on their requests or conflicts. Examples of dynamic locking algorithms are wait-free protocol (WFP) and wound-wait protocol (WWP).
- Optimistic algorithms allow concurrent accesses to data objects without locks, but detect and resolve conflicts after the accesses. They can be further divided into validation-based and compensation-based algorithms.
- Validation-based algorithms check the validity of the accessed data objects at the end of the jobs, and abort and restart the jobs if they are invalid. Examples of validation-based algorithms are optimistic concurrency control (OCC) and timestamp ordering (TO).
- Compensation-based algorithms compensate for the effects of the accessed data objects at the end of the jobs, and update the data objects accordingly. Examples of compensation-based algorithms are compensation-based concurrency control (CCC) and compensation-based timestamp ordering (CTO).
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the data consistency requirements, the timing constraints, the workload, and the operating environment.



# Unit 4 - Real Time Communication

- Real time communication (RTC) is a category of software protocols and communication hardware media that gives real time guarantees, which is necessary to support real time guarantees of real time computing.
- RTC data and messages are not stored between transmission and reception.
- RTC is nearly instant with minimal latency or transmission delays .
- RTC is synonymous with live communication.
- RTC is dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.
- Examples of RTC include voice over IP (VoIP), video conferencing, instant messaging, live streaming, online gaming, and telemedicine.



# Basic Concepts in Real Time Communication

Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In this context, the term real time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Streaming media and live broadcasting

Some of the basic concepts in real time communication are:

- **Bandwidth**: The amount of data that can be transmitted or received per unit of time. Bandwidth is measured in bits per second (bps) and affects the quality and speed of RTC.
- **Latency**: The time it takes for a data packet to travel from the source to the destination. Latency is measured in milliseconds (ms) and affects the responsiveness and synchronicity of RTC.
- **Jitter**: The variation in latency of data packets. Jitter is caused by network congestion, interference, or routing changes and affects the smoothness and continuity of RTC.
- **Packet loss**: The percentage of data packets that are lost or corrupted during transmission. Packet loss is caused by network errors, congestion, or interference and affects the reliability and completeness of RTC.
- **Codec**: A software or hardware device that encodes and decodes data for transmission and reception. Codec stands for coder-decoder and affects the compression, quality, and compatibility of RTC.
- **Protocol**: A set of rules and standards that govern how data is formatted, transmitted, and received. Protocol affects the interoperability, security, and functionality of RTC.
- **Application**: A software program that enables users to perform RTC tasks. Application affects the user interface, features, and performance of RTC.



# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: **Hard Real-Time (HRT)** and **Soft Real-Time (SRT)**.
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation.
- A hard real-time communication system is one that must meet its deadlines, otherwise it may cause catastrophic damage or loss of life  . For example, a nuclear reactor control system, a flight control system, or a pacemaker system are hard real-time communication systems .
- A soft real-time communication system is one that can tolerate some deadline misses, without causing severe harm or degradation of service  . For example, a video conferencing system, a multimedia streaming system, or a web server are soft real-time communication systems .
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic. This means that hard real-time communication systems can guarantee the worst-case execution time and response time, while soft real-time communication systems can only provide statistical guarantees.
- Hard real-time communication systems require strict scheduling algorithms, priority assignment, and resource management to ensure that all tasks meet their deadlines . Soft real-time communication systems can use more flexible and adaptive scheduling algorithms, such as earliest deadline first, rate monotonic, or feedback control .
- Hard real-time communication systems are often designed with safety and reliability as the primary objectives, while soft real-time communication systems are often designed with performance and quality of service as the primary objectives .
- Hard real-time communication systems are usually more expensive and complex to develop and maintain, while soft real-time communication systems are usually more cost-effective and scalable .



# Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination.
- Examples of real time communication include voice calls, video calls, instant messaging, online gaming, live streaming, etc .
- Real time communication requires a network that can support the quality of service (QoS) parameters such as throughput, delay and jitter .
- Throughput is the amount of data that can be transmitted or received per unit time.
- Delay is the time taken for a message to travel from the source to the destination.
- Jitter is the variation in the delay of the messages.
- Real time communication can be classified into two types: real time traffic and non-real time traffic.
- Real time traffic is also called isochronous or synchronous traffic, which consists of a stream of messages that are generated by their sources and delivered to their respective destinations on a continuous basis.
- Real time traffic includes periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals and have fixed deadlines.
- Aperiodic messages are generated at irregular intervals and have variable deadlines.
- Sporadic messages are generated randomly and have unpredictable deadlines.
- Non-real time traffic is also called asynchronous traffic, which consists of messages that are generated by their sources and delivered to their destinations without any strict timing constraints.
- Non-real time traffic includes bursty and smooth messages.
- Bursty messages are generated in bursts and have high variability in inter-arrival times and lengths.
- Smooth messages are generated at a constant rate and have low variability in inter-arrival times and lengths.
- In the model of real time communication, the end users of the message application systems are sources and destinations residing in different hosts.
- The network interface of each host contains an input queue and an output queue.
- Two buffer areas called input/output buffers are allocated to the input and output queues to store queuing information.
- In real time traffic model, each message (Mi) can be characterized by a tuple of inter-packet spacing (Pi), message length (ei), and reception deadline (Di) as below :

  Mi = (Pi, ei, Di)

- This traffic model is called the peak rate model in real time communication .



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are scheduling algorithms that assign different priorities to different packets or flows in a switched network, such as a router or a switch.
- The priority of a packet or a flow determines the order in which it is transmitted or forwarded by the network device, and the amount of bandwidth or resources it receives.
- Priority-based service disciplines can improve the quality of service (QoS) for real-time communication, such as voice or video, by reducing the delay, jitter, and packet loss for high-priority packets or flows.
- Some examples of priority-based service disciplines are:

  - Weighted Fair Queuing (WFQ): This discipline assigns a weight to each packet or flow, and serves them in proportion to their weights. The weight can reflect the priority, the size, or the rate of the packet or flow. WFQ can achieve fairness and differentiation among different packets or flows, and can approximate the ideal Generalized Processor Sharing (GPS) discipline.
  - Weighted Round Robin (WRR): This discipline assigns a weight to each packet or flow, and serves them in a round-robin fashion, but with a variable number of packets or bytes per round. The number of packets or bytes per round is proportional to the weight of the packet or flow. WRR can achieve fairness and differentiation among different packets or flows, but it can introduce more delay and jitter than WFQ.
  - Strict Priority (SP): This discipline assigns a fixed priority to each packet or flow, and serves them in a strict order, from the highest priority to the lowest priority. SP can achieve the lowest delay and jitter for the highest priority packets or flows, but it can cause starvation or unfairness for the lower priority packets or flows.
  - Probabilistic Priority (PP): This discipline assigns a fixed priority and a parameter to each packet or flow, and serves them in a probabilistic manner. The parameter determines the probability with which the packet or flow is served when it is polled by the server. PP can achieve a trade-off between SP and WRR, by allowing some flexibility and randomness in the service order.

- Some variations or extensions of these priority-based service disciplines are:

  - Class-Based Weighted Fair Queuing (CBWFQ): This discipline classifies the packets or flows into different classes, and assigns a weight to each class. Within each class, the packets or flows are served in a FIFO manner. Between different classes, the packets or flows are served in proportion to their class weights. CBWFQ can achieve fairness and differentiation among different classes of packets or flows, and can support hierarchical or nested classes.
  - Weighted Fair Priority Queuing (WFPQ): This discipline classifies the packets or flows into different classes, and assigns a priority and a weight to each class. Within each class, the packets or flows are served in a FIFO manner. Between different classes, the packets or flows are served in a strict priority order, but with a variable number of packets or bytes per priority level. The number of packets or bytes per priority level is proportional to the class weight. WFPQ can achieve a trade-off between SP and CBWFQ, by allowing some flexibility and differentiation in the service order.
  - Rate-Controlled Frame-Based Weighted Round Robin (RFWRR): This discipline divides the packets or flows into different classes, and assigns a rate and a weight to each class. The rate determines the maximum bandwidth or resources that the class can receive. The weight determines the relative share of the bandwidth or resources that the class can receive. The discipline also divides the time into frames, and serves the packets or flows in a round-robin fashion within each frame, but with a variable number of packets or bytes per round. The number of packets or bytes per round is proportional to the class weight. RFWRR can achieve fairness and differentiation among different classes of packets or flows, and can guarantee the delay jitter bound and satisfy a diverse set of delay requirements.

: https://benchpartner.com/priority-based-service-disciplines-for-switched-network
: https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.24.5285
: https://www.sciencedirect.com/science/article/abs/pii/S0045790612002285
: https://ieeexplore.ieee.org/document/896391/
[assistant



# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless broadcast network.
- Broadcast networks allow multiple nodes to transmit data to all other nodes in the network, which can be useful for real-time communication applications such as video conferencing, sensor networks, or vehicular networks.
- However, broadcast networks also face challenges such as interference, collisions, hidden terminals, and exposed terminals, which can degrade the performance and reliability of the communication.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based.
- Probabilistic contention protocols, such as Aloha and CSMA, use direct, asynchronous competition between neighboring nodes to determine which node will transmit next. They are simple, distributed, and adaptive, but they are also unreliable, inefficient, and unbounded in access delay .
- Deterministic contention protocols, such as TDMA and CDMA, use a fixed, synchronous transmission schedule that assigns slots to nodes in a round-robin or code-division manner. They are reliable, efficient, and bounded in access delay, but they are also rigid, centralized, and non-adaptive .
- Reservation-based protocols, such as ABROAD and IEEE 802.11, use a hybrid approach that combines a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay. They are adaptive, distributed, and provide worst-case performance guarantees, but they are also complex, overhead-intensive, and sensitive to synchronization errors .
- The choice of MAC protocol depends on the requirements and characteristics of the broadcast network and the real-time communication application, such as the traffic load, the node connectivity, the channel quality, the latency, the throughput, and the reliability  .



# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, jitter, and delay.
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams    .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP is used in real-time systems for an efficient quality band transmission to a particular receiver.
- RSVP uses resource reservation and admission control mechanisms as key building blocks to establish and maintain QoS.
- RSVP is not a routing protocol, but rather works with existing routing protocols to reserve resources along the path of a data flow.
- RSVP uses soft state, which means that the reservations are periodically refreshed and can be easily modified or deleted.
- RSVP messages are classified into two types: PATH and RESV.
  - PATH messages are sent by the sender to the receiver along the route of the data flow, carrying information about the sender's characteristics and QoS requirements.
  - RESV messages are sent by the receiver to the sender along the reverse path of the data flow, carrying the receiver's QoS request and reservation confirmation.
- RSVP supports two service models: Integrated Services (IntServ) and Differentiated Services (DiffServ).
  - IntServ provides end-to-end QoS guarantees for individual data flows, using per-flow reservation and classification .
  - DiffServ provides aggregate QoS guarantees for groups of data flows, using per-class reservation and marking .
- RSVP has some limitations, such as scalability, complexity, overhead, and security .
  - Scalability: RSVP requires per-flow state information to be maintained by all the routers along the path of the data flow, which can be impractical for large networks with many flows .
  - Complexity: RSVP requires coordination and cooperation among multiple network components, such as applications, hosts, routers, and network management systems, which can be challenging to implement and maintain .
  - Overhead: RSVP introduces additional traffic and processing load on the network and the routers, which can affect the performance and efficiency of the network .
  - Security: RSVP is vulnerable to various attacks, such as denial of service, spoofing, modification, and replay, which can compromise the QoS and integrity of the network .



## Unit 5 - Real Time Operating Systems and Databases

- A **real-time operating system (RTOS)** is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations  .
- A **real-time database** is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock prices, and online transactions .
- Some of the characteristics of real-time operating systems and databases are:
  - **Predictability**: They must guarantee that the tasks and queries are completed within a specified deadline, regardless of the system load or external factors.
  - **Concurrency**: They must support multiple tasks and queries running simultaneously and sharing the system resources, such as CPU, memory, and disk.
  - **Responsiveness**: They must react quickly to the changes in the data and events, and provide timely feedback to the users and applications.
  - **Fault tolerance**: They must be able to recover from failures and errors, and ensure the data integrity and availability.
- Some of the challenges of real-time operating systems and databases are:
  - **Scheduling**: They must use efficient algorithms to assign priorities and deadlines to the tasks and queries, and to decide which ones to execute, preempt, or abort.
  - **Memory management**: They must allocate and deallocate memory for the tasks and queries, and avoid memory fragmentation and leakage.
  - **Data consistency**: They must ensure that the data is consistent and correct, and handle the conflicts and concurrency issues that may arise from multiple tasks and queries accessing the same data.
  - **Performance**: They must optimize the system performance and throughput, and minimize the overhead and latency.



# Features of RTOS

A real-time operating system (RTOS) is an operating system with two key features: predictability and determinism. This means that it can guarantee that a certain task will be completed within a specified time limit, regardless of the system load or other factors. Some of the features and advantages of an RTOS are:

- **Small and fast**: An RTOS is designed to occupy very less memory and consume fewer resources, making it suitable for embedded systems and devices with limited hardware capabilities.
- **Responsive**: An RTOS can respond quickly to external events and interrupts, without significant delays or overheads.
- **Deterministic**: An RTOS can ensure that the same task will always take the same amount of time to execute, regardless of the system state or other tasks.
- **Scalable**: An RTOS can support the addition of new features and capabilities to products as market needs evolve, while leveraging the existing code base and hardware platform.
- **Reliable**: An RTOS can provide fault tolerance and error handling mechanisms to ensure the system's functionality and safety in case of failures or malfunctions.

Some of the common types of RTOS are:

- **Co-operative scheduling**: In this type of RTOS, the tasks run until they are completed or they voluntarily yield the CPU to another task. The kernel can only be set up in one way, and the tasks have equal priority.
- **Pre-emptive scheduling**: In this type of RTOS, each task has a unique priority value, and the scheduler always runs the highest priority task that is ready. The tasks can be pre-empted by higher priority tasks or interrupts at any time.
- **Time-slicing**: In this type of RTOS, the tasks have equal priority, but the scheduler assigns a fixed time slice to each task. The tasks are executed in a round-robin fashion, and the scheduler switches to the next task when the time slice expires or the current task yields the CPU.

Some of the examples of RTOS are:

- **Wind River VxWorks**: This is a commercial RTOS that supports a wide range of architectures and platforms, and provides features such as security, networking, graphics, and IoT connectivity.
- **FreeRTOS**: This is an open source RTOS that is designed for microcontrollers and small embedded systems, and provides features such as task management, timers, queues, and semaphores.
- **Linux**: This is a general-purpose operating system that can be configured to run in real-time mode, by using patches such as PREEMPT_RT or Xenomai, or by using a co-kernel such as RTAI or RTLinux.



# Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- A real-time system is a system that must produce the expected result within a defined deadline and coordinate independent clocks and operate together in unison.
- A real-time system can be classified into hard real-time and soft real-time based on the timing constraints  .
  - A hard real-time system has absolute deadlines, and if those deadlines are missed, a system failure will occur.
  - A soft real-time system has relative deadlines, and if those deadlines are missed, the system performance will degrade but not fail.
- Time services are the mechanisms that provide the system with the notion of time and enable the system to measure, compare, and synchronize time.
- Time services are essential for real-time systems because they allow the system to:
  - Schedule tasks and events according to their deadlines and priorities.
  - Monitor the execution time of tasks and events and detect any timing violations.
  - Communicate and coordinate with other real-time systems and devices using a common time reference.
- Time services can be implemented using hardware and software components, such as:
  - Synchronous programming languages, which enforce a deterministic and predictable execution of tasks and events.
  - Real-time operating systems (RTOSes), which provide the system with a kernel that supports time-critical operations and services.
  - Real-time networks, which enable the system to exchange time-sensitive data and messages with other systems and devices.
  - Clocks and timers, which generate and measure time signals and trigger interrupts and actions.
  - Synchronization protocols, which ensure that the system and its components have a consistent and accurate view of time.



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like UNIX strives to provide good average performance, for a RTOS, correct timing is the key feature.
- UNIX is not a RTOS by default, but it can be modified or extended to support some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running process and switch to a higher priority one when an event occurs.
  - Priority inheritance: the mechanism to avoid priority inversion, which occurs when a low priority process holds a resource needed by a high priority process.
  - Real-time signals: the signals that are delivered to a process immediately, without being queued or blocked.
  - Memory locking: the function to prevent the memory pages of a process from being swapped out to disk, which would cause delays.
  - High-resolution timers: the timers that can measure time intervals with nanosecond precision.
- Some examples of UNIX variants or extensions that support real-time features are:
  - RTLinux: a hard real-time extension to the Linux kernel that runs Linux as a low priority thread on a small real-time core.
  - Xenomai: a dual kernel approach that provides a hard real-time co-kernel to Linux, which can preempt the Linux kernel at any time.
  - PREEMPT_RT: a patch set that transforms the Linux kernel into a fully preemptible kernel, with improved latency and determinism.
  - QNX: a commercial UNIX-like RTOS that uses a microkernel architecture and a message passing model.
  - Solaris: a commercial UNIX-like OS that supports real-time scheduling, memory locking, and high-resolution timers.



# POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interact with an operating system.
- POSIX was originally designed for UNIX-like systems, but it does not cover all the features and requirements of real-time operating systems (RTOS).
- RTOS are operating systems that can guarantee timely and predictable responses to events, such as sensors, actuators, or user inputs.
- POSIX issues for RTOS include:
  - The lack of real-time scheduling policies and priority inheritance mechanisms, which are essential for ensuring that high-priority tasks can preempt low-priority ones and avoid priority inversion problems.
  - The lack of real-time synchronization primitives, such as mutexes, semaphores, condition variables, and message queues, which are needed for coordinating concurrent tasks and sharing resources in a real-time manner.
  - The lack of real-time memory management, such as memory locking and allocation, which are needed to prevent page faults and memory fragmentation that can cause unpredictable delays.
  - The lack of real-time signal handling, which is a way of notifying tasks about events occurring in the system, such as timers, interrupts, or exceptions. POSIX signals are not queued, prioritized, or associated with specific tasks, and thus some events may be lost or handled too late.
  - The lack of real-time timers, which are needed to measure time intervals and trigger actions at precise moments.
  - The lack of real-time I/O, which is needed to communicate with external devices and networks in a timely and reliable way.
- To address these issues, POSIX has developed several extensions and amendments to the original standard, such as:
  - POSIX.1b (or POSIX.4), which defines real-time extensions, such as real-time scheduling, synchronization, memory management, signal handling, and timers.
  - POSIX.1c (or POSIX.4a), which defines threads extensions, such as thread creation, termination, synchronization, and scheduling.
  - POSIX.1d (or POSIX.4b), which defines additional real-time extensions, such as asynchronous I/O, memory mapped files, and message passing.
  - POSIX.1j (or POSIX.4c), which defines advanced real-time extensions, such as sporadic server scheduling, priority protection, and timers with overrun counts.
  - POSIX.1q (or POSIX.4d), which defines dynamic scheduling extensions, such as deadline scheduling and resource reservation.
- These extensions aim to provide a common and portable interface for developing real-time applications across different RTOS platforms, but they also introduce some challenges and limitations, such as:
  - The complexity and overhead of implementing and complying with the POSIX standards, which may affect the performance and efficiency of the RTOS.
  - The variability and incompleteness of the POSIX standards, which may leave some features undefined, optional, or platform-dependent, and thus reduce the portability and interoperability of the applications.
  - The trade-off between generality and specificity of the POSIX standards, which may not cover all the needs and scenarios of real-time applications, and thus require additional or alternative solutions.



# Characteristic of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as date, time, duration, interval, or event.
- Temporal data can be used to analyze weather patterns, traffic conditions, demographic trends, and other phenomena that change over time.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon by an agent.
- Temporal data can be stored in different ways, such as using timestamps, intervals, or temporal elements.
  - Timestamps are discrete points in time that mark the occurrence of an event or the validity of a fact.
  - Intervals are continuous spans of time that represent the duration or validity of a fact.
  - Temporal elements are abstract units of time that can be used to define temporal granularity or periodicity.
- Temporal data can be queried and manipulated using different techniques, such as temporal algebra, temporal logic, or temporal SQL.
  - Temporal algebra is a set of operations that can be applied to temporal data to perform temporal aggregation, projection, selection, join, or difference.
  - Temporal logic is a formal system that can be used to reason about temporal data and express temporal constraints, properties, or queries.
  - Temporal SQL is an extension of SQL that can be used to define, query, and update temporal data in a relational database.



# Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to process data that is time-sensitive and relevant to the current situation. If the data is outdated or inaccurate, the system may make wrong decisions or miss deadlines.
- Temporal consistency can be measured by the temporal error, which is the difference between the actual value of a data item and the value stored in the database. The temporal error should be within a predefined limit, otherwise the data is considered temporally inconsistent.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the system when the data changes in the environment, rather than by the user transactions.
  - Periodic refreshes, which are updates that are performed at regular intervals, regardless of the data changes in the environment.
  - Temporal validity, which is a property of data items that specifies the time interval during which they are valid and can be used by transactions.
  - Temporal isolation, which is a property of transactions that specifies the maximum temporal error that they can tolerate when accessing data items.
  - Temporal locking, which is a concurrency control mechanism that prevents transactions from accessing data items that are being updated or have a high temporal error.
  - Temporal caching, which is a technique that stores frequently accessed data items in a local memory to reduce the access time and the temporal error.



# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency control is a procedure of managing simultaneous operations on a shared database without conflicting with each other.
- Concurrency control ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the respective database.
- Concurrency control is important for real-time database systems, which have to deal with both data consistency and timing constraints.
- A real-time database system must adapt to changes in the operating environment and guarantee the completion of critical transactions.
- A transaction is a logical unit of work that accesses or modifies one or more data items in a database.
- A transaction is said to be successfully completed if and only if, it satisfies the ACID properties: Atomicity, Consistency, Isolation, and Durability.
- A transaction is said to be serializable if and only if the database operations carried out by it is equivalent to some serial execution of these transactions.
- A serial execution of transactions is one in which no two transactions are executed concurrently.
- A serializable execution of transactions preserves the consistency of the database.
- There are two main approaches to achieve concurrency control: locking-based protocols and timestamp-based protocols.
- Locking-based protocols use locks to prevent conflicting operations on the same data item by different transactions.
- A lock is a mechanism that grants exclusive access to a data item to a transaction that requests it.
- A lock can be either shared or exclusive, depending on the mode of access (read or write) requested by the transaction.
- A shared lock allows multiple transactions to read the same data item, but prevents any transaction from writing it.
- An exclusive lock allows only one transaction to read or write the data item, and prevents any other transaction from accessing it.
- A transaction must acquire the appropriate lock on a data item before accessing it, and release the lock after finishing the access.
- A transaction must follow the two-phase locking protocol, which requires that all lock requests precede all lock releases in the transaction.
- A transaction can be in one of the following phases: growing phase, shrinking phase, or committed phase.
- In the growing phase, the transaction can acquire locks but cannot release any lock.
- In the shrinking phase, the transaction can release locks but cannot acquire any new lock.
- In the committed phase, the transaction has released all its locks and has either committed or aborted.
- The two-phase locking protocol ensures serializability, but may cause deadlocks, which occur when two or more transactions are waiting for each other to release locks on the data items they need.
- Deadlocks can be prevented or detected and resolved by using various techniques, such as timeout, deadlock prevention, deadlock avoidance, or deadlock detection and recovery.
- Timestamp-based protocols use timestamps to order the transactions and determine the precedence of conflicting operations on the same data item by different transactions.
- A timestamp is a unique identifier that reflects the relative starting time of a transaction.
- A timestamp can be either generated by the system (system timestamp) or assigned by the application (logical timestamp).
- A transaction must have a timestamp before it can access any data item in the database.
- A data item has two timestamps: read timestamp (RTS) and write timestamp (WTS), which record the latest time when the data item was read or written by any transaction.
- A transaction can read or write a data item only if its timestamp is compatible with the timestamps of the data item.
- The compatibility rules are as follows:
  - A transaction T can read a data item X only if TS(T) >= WTS(X), where TS(T) is the timestamp of T and WTS(X) is the write timestamp of X. This ensures that T does not read an older version of X that was overwritten by a later transaction.
  - A transaction T can write a data item X only if TS(T) > RTS(X) and TS(T) > WTS(X), where RTS(X) is the read timestamp of X. This ensures that T does not overwrite a newer version of X that was read or written by a later transaction.
- If a transaction violates any of the compatibility



# Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses.
- Some of the attributes of live real-time databases are:
  - Concurrency control: The ability to handle multiple transactions accessing the same data without compromising data integrity or consistency.
  - Data freshness: The degree to which the data reflects the current state of the real world.
  - Data distribution: The ability to store and access data across multiple nodes or locations for scalability, availability, and performance.
  - Data replication: The ability to create and maintain copies of data on different nodes or locations for fault tolerance, load balancing, and data locality.
  - Data recovery: The ability to restore data to a consistent state after a failure or a crash.
  - Data security: The ability to protect data from unauthorized access, modification, or deletion.
  - Data quality: The ability to ensure that data is accurate, complete, and reliable.
  - Data analysis: The ability to perform queries, aggregations, and transformations on data to derive insights and intelligence.
  - Data visualization: The ability to present data in a graphical or interactive form to facilitate understanding and decision making.
- Some of the examples of commercial real-time databases are :
  - Dealpath: A cloud-based platform that provides data and workflow management for commercial real estate transactions.
  - Altus Group: A data and software provider that offers historical and current market data, valuation, and analytics for commercial real estate.
  - CoStar: A leading provider of commercial real estate information, analytics, and online marketplaces.
  - Google Cloud Firestore: A highly performant, fully managed NoSQL database service for large analytical and operational workloads.

