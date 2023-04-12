

# Real Time System

A real time system is a system that can process and respond to inputs or events within a specified time limit. The time limit is usually determined by the requirements of the application or the environment that the system is controlling. A real time system must be able to meet its deadlines, otherwise it may cause a system failure or undesirable consequences.

Some examples of real time systems are:

- Flight control systems that control the movement and stability of aircrafts
- Industrial control systems that monitor and regulate the production processes in factories
- Machine vision systems that help machines to recognize and analyze images or videos
- Robotics systems that enable robots to perform tasks such as navigation, manipulation, or coordination
- Medical imaging systems that process and display the images of internal organs or tissues

## Types of real time systems

Real time systems can be classified into two types based on their timing constraints:

- Hard real time systems: These systems have absolute deadlines that must be met without any exception. Missing a deadline can result in a catastrophic failure or a severe loss. For example, a flight control system must respond to the inputs from the pilot or the sensors within a few milliseconds, otherwise the aircraft may crash or deviate from its course.
- Soft real time systems: These systems have relative deadlines that can be missed occasionally with some acceptable probability. Missing a deadline may degrade the performance or the quality of the system, but not cause a fatal error. For example, a video streaming system may drop some frames or reduce the resolution if the network bandwidth is low, but it can still provide a satisfactory service to the user.

## Characteristics of real time systems

Real time systems have some common characteristics that distinguish them from other types of systems, such as:

- Time sensitivity: Real time systems must be able to sense, process, and act on the inputs or events within a predefined time limit. The time limit may vary depending on the application or the environment, but it is usually much shorter than the human perception of time. For example, a human may not notice a delay of a few seconds, but a real time system may need to respond within a few microseconds or nanoseconds.
- Time synchronization: Real time systems must be able to coordinate and communicate with other systems or devices that have independent clocks and operate in parallel. The systems or devices must agree on a common notion of time and adjust their clocks accordingly to avoid errors or inconsistencies. For example, a robotic system may need to synchronize its movements with other robots or sensors to achieve a coordinated task.
- Predictability: Real time systems must be able to guarantee that they can meet their deadlines under any possible scenario or condition. The systems must be designed and tested to ensure that they can handle the worst-case situations and avoid any unexpected behavior or failure. For example, a real time system must be able to cope with the variations in the input data, the system load, the hardware failures, or the external disturbances.



## Unit 1 - Introduction of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to perform its intended function or cause undesirable consequences.
- Real time systems are often used in applications that require high reliability, safety, or performance, such as industrial control, avionics, robotics, medical devices, etc.
- Real time systems can be classified into two types: hard real time systems and soft real time systems.
- Hard real time systems are systems that must meet all their deadlines, otherwise they may cause catastrophic failure or loss of life. Examples of hard real time systems are nuclear reactor control, air traffic control, pacemakers, etc.
- Soft real time systems are systems that can tolerate some deadline misses, but the quality of service or user satisfaction may degrade. Examples of soft real time systems are multimedia, video games, online transactions, etc.
- Real time systems have some common characteristics, such as concurrency, predictability, responsiveness, dependability, and adaptability.
- Concurrency means that a real time system can handle multiple events or tasks simultaneously, using parallel or distributed processing techniques.
- Predictability means that a real time system can guarantee the worst-case execution time and resource usage of its tasks, using static or dynamic analysis methods.
- Responsiveness means that a real time system can react to events or inputs within a bounded time, using scheduling algorithms and priority mechanisms.
- Dependability means that a real time system can ensure the correctness and availability of its functions, using fault tolerance and error recovery techniques.
- Adaptability means that a real time system can adjust to changes in the environment or user requirements, using feedback and reconfiguration techniques.



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System.

### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time limit, otherwise it may fail to meet its objectives or cause undesirable consequences.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet its deadlines strictly, otherwise it may cause catastrophic failure or loss of life. For example, a nuclear reactor control system, a pacemaker, or an air traffic control system are hard real time systems.
- A soft real time system is a system that can tolerate some degree of deadline misses, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a multimedia system are soft real time systems.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic and aperiodic.
- A periodic system is a system that has events or inputs that occur at regular intervals, and the system must respond to them within a fixed time. For example, a sensor that measures the temperature every second, or a task that executes every 10 milliseconds are periodic systems.
- An aperiodic system is a system that has events or inputs that occur at irregular or unpredictable intervals, and the system must respond to them as soon as possible. For example, a keyboard input, a mouse click, or an interrupt are aperiodic systems.
- A real time system can also be classified into two types based on the number of processors or cores: single processor and multiprocessor.
- A single processor system is a system that has only one processor or core that executes all the tasks or processes. For example, a microcontroller, or a single core CPU are single processor systems.
- A multiprocessor system is a system that has more than one processor or core that can execute tasks or processes concurrently or in parallel. For example, a multicore CPU, a GPU, or a cluster are multiprocessor systems.



### Typical Real Time Applications

A real-time application (RTA) is an application that has strict time constraints on its functionality and performance. RTAs must respond to events or inputs within a predictable and specific time frame, otherwise they may fail or cause undesirable consequences. RTAs are often used in domains such as digital control, command and control, signal processing, tracking, real-time databases, and multimedia. Some examples of RTAs are:

- **Video conferencing**: This is an application that allows users to communicate with each other using audio and video streams over the Internet. Video conferencing requires high bandwidth, low latency, and synchronization of the streams to ensure a smooth and realistic interaction. Video conferencing is a soft real-time application, meaning that occasional delays or errors are tolerable, but may affect the quality of the service.

- **Voice over Internet Protocol (VoIP)**: This is an application that enables users to make phone calls over the Internet using digital packets instead of analog signals. VoIP requires low bandwidth, low latency, and high reliability to ensure a clear and uninterrupted conversation. VoIP is also a soft real-time application, meaning that occasional delays or errors are tolerable, but may affect the quality of the service.

- **Online gaming**: This is an application that allows users to play games with other users over the Internet. Online gaming requires high bandwidth, low latency, and synchronization of the game state to ensure a fair and enjoyable experience. Online gaming is a soft real-time application, meaning that occasional delays or errors are tolerable, but may affect the quality of the service.

- **Community storage applications**: These are applications that allow users to store and share data over the Internet using distributed and decentralized networks of nodes. Community storage applications require high bandwidth, low latency, and high availability to ensure a fast and reliable access to the data. Community storage applications are soft real-time applications, meaning that occasional delays or errors are tolerable, but may affect the quality of the service.

- **Some e-commerce applications**: These are applications that allow users to buy and sell goods and services over the Internet. Some e-commerce applications require high bandwidth, low latency, and high security to ensure a smooth and safe transaction. Some e-commerce applications are soft real-time applications, meaning that occasional delays or errors are tolerable, but may affect the quality of the service.

- **Real-time operating system (RTOS)**: This is an operating system that supports the execution of real-time applications by providing features such as preemptive scheduling, priority-based dispatching, inter-process communication, and resource management. RTOS must ensure that the real-time applications meet their deadlines and performance requirements. RTOS is a hard real-time application, meaning that any delay or error is unacceptable and may cause a system failure.

- **Instant messaging (IM) applications**: These are applications that allow users to send and receive text, audio, video, or other types of messages over the Internet. IM applications require low bandwidth, low latency, and high reliability to ensure a timely and accurate delivery of the messages. IM applications are soft real-time applications, meaning that occasional delays or errors are tolerable, but may affect the quality of the service.

- **Team collaboration applications**: These are applications that allow users to work together on a common project or task over the Internet. Team collaboration applications require high bandwidth, low latency, and synchronization of the project or task state to ensure a productive and efficient collaboration. Team collaboration applications are soft real-time applications, meaning that occasional delays or errors are tolerable, but may affect the quality of the service.

- **Digital control**: This is an application that uses a computer to control a physical system or process, such as a robot, a vehicle, or a plant. Digital control requires high bandwidth, low latency, and high accuracy to ensure a stable and optimal control. Digital control is a hard real-time application, meaning that any delay or error is unacceptable and may cause a system failure or instability.

- **Optimal control**: This is an application that uses a computer to find the best control strategy for a physical system or process, such as a rocket, a missile, or a power plant. Optimal control requires high bandwidth, low latency, and high precision to ensure a optimal and robust control. Optimal control is a hard real-time application, meaning that any delay or error is unacceptable and may cause a system failure or suboptimality.

- **Command and control**: This is an application that uses a computer to coordinate and direct the actions of multiple agents



Hello, I am Sydney, your AI assistant. I can help you with your studies and assignments. You have asked me to write the content for the topic of release times for the notes of the unit 1 - introduction of real time system in the subject of real time system. Here is the content I have written in markdown format:

### Release Times
- Release times are the moments when tasks become available for execution in a real time system.
- Release times can be specified by the task model, which defines the parameters and constraints of each task, such as period, deadline, execution time, etc.
- Release times can be either periodic or aperiodic, depending on the task model.
  - Periodic tasks have fixed and regular release times, such as every 10 milliseconds, 20 seconds, or 1 hour. Periodic tasks are usually associated with recurrent and predictable events, such as sensor readings, control loops, or alarms.
  - Aperiodic tasks have variable and irregular release times, such as upon user request, external interrupt, or random occurrence. Aperiodic tasks are usually associated with sporadic and unpredictable events, such as user inputs, faults, or emergencies.
- Release times can also be either hard or soft, depending on the task model.
  - Hard release times are the earliest possible moments when tasks can start execution. Hard release times are usually enforced by the system or the environment, and violating them can cause severe consequences, such as system failure, data loss, or safety hazards.
  - Soft release times are the preferred or desired moments when tasks can start execution. Soft release times are usually determined by the application or the user, and violating them can cause minor consequences, such as degraded performance, lower quality, or user dissatisfaction.
- Release times can affect the schedulability and feasibility of a real time system, which are the properties that determine whether all tasks can meet their deadlines under a given scheduling algorithm and system configuration.
  - Schedulability analysis is the process of checking whether a given set of tasks can be scheduled by a given algorithm without missing any deadlines.
  - Feasibility analysis is the process of finding a feasible system configuration, such as processor speed, memory size, or task parameters, that can schedule a given set of tasks without missing any deadlines.
- Release times can also affect the responsiveness and predictability of a real time system, which are the properties that determine how fast and how consistent the system can react to events and produce outputs.
  - Responsiveness is the measure of the delay between the release time and the completion time of a task. Responsiveness can be evaluated by metrics such as response time, latency, or jitter.
  - Predictability is the measure of the variation or uncertainty of the delay between the release time and the completion time of a task. Predictability can be evaluated by metrics such as worst-case execution time, best-case execution time, or deadline miss ratio.



Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Real Time System. Here is the content for the topic of Deadlines for the notes of the Unit 1 - Introduction of Real Time System:

### Deadlines for the notes of the Unit 1 - Introduction of Real Time System

- A deadline is a time constraint that specifies the latest time by which a task or an event should be completed or occur.
- Deadlines are important for real time systems because they ensure the timeliness and predictability of the system's behavior and performance.
- There are different types of deadlines for real time systems, such as:
  - Hard deadline: A hard deadline is a deadline that must be met without any exception. Missing a hard deadline can result in a catastrophic failure of the system or a severe violation of the system's requirements. For example, a hard deadline for a flight control system is the time by which the system must respond to a pilot's input or a sensor's signal.
  - Soft deadline: A soft deadline is a deadline that can be missed occasionally or with some tolerable degradation of the system's quality of service. Missing a soft deadline can result in a reduced performance or a lower satisfaction of the system's users or customers. For example, a soft deadline for a video streaming system is the time by which the system must deliver a video frame to the display device.
  - Firm deadline: A firm deadline is a deadline that lies between a hard deadline and a soft deadline. Missing a firm deadline can result in a waste of the system's resources or a loss of the system's utility. For example, a firm deadline for a data transmission system is the time by which the system must send a data packet to the receiver.

- Deadlines can be classified into two categories based on their relation to the task's execution time, such as:
  - Implicit deadline: An implicit deadline is a deadline that is equal to the task's period, which is the time interval between two consecutive activations of the task. For example, an implicit deadline for a periodic task that is activated every 10 milliseconds is 10 milliseconds.
  - Constrained deadline: A constrained deadline is a deadline that is less than or equal to the task's period. For example, a constrained deadline for a periodic task that is activated every 10 milliseconds is 8 milliseconds.
  - Arbitrary deadline: An arbitrary deadline is a deadline that is greater than the task's period. For example, an arbitrary deadline for a periodic task that is activated every 10 milliseconds is 15 milliseconds.

- Deadlines can also be classified into two categories based on their relation to the task's arrival time, such as:
  - Relative deadline: A relative deadline is a deadline that is measured from the task's arrival time, which is the time when the task becomes ready for execution. For example, a relative deadline for a task that arrives at time 0 and has a deadline of 10 milliseconds is 10 milliseconds.
  - Absolute deadline: An absolute deadline is a deadline that is measured from a fixed reference point, such as the system's start time or the current time. For example, an absolute deadline for a task that arrives at time 0 and has a deadline of 10 milliseconds is 10 milliseconds from the system's start time or the current time.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems.
- Timing constraints decide the total correctness of the result in real-time systems.
- The correctness of results in real-time system does not depend only on logical correctness but also the result should be obtained within the time constraint.
- Time constraints related with real-time systems simply means that time interval allotted for the response of the ongoing program.
- Real-time system is responsible for the completion of all tasks within their time intervals.
- For a real-time system to be capable of real-time computing, it must satisfy two requirements:
  - Timeliness: The ability to produce the expected result by a specific deadline.
  - Time synchronization: The capability of agents to coordinate independent clocks and operate together in unison.
- Timing constraints associated with the real-time system are classified to identify the different types of timing constraints in a real-time system.
- Timing constraints are broadly classified into two categories:
  - Performance Constraints: The constraints enforced on the response of the system is known as Performance Constraints.
  - Reliability Constraints: The constraints enforced on the behavior of the system is known as Reliability Constraints.
- Performance Constraints are further classified into three types:
  - Delay Constraint: A delay constraint describes the minimum time interval between occurrence of two consecutive events.
  - Deadline Constraint: A deadline constraint describes the maximum time interval between occurrence of two consecutive events.
  - Duration Constraint: Duration constraint describes the maximum time interval for which an event can occur.
- Reliability Constraints are further classified into two types:
  - Synchronization Constraint: A synchronization constraint describes the maximum time difference between occurrence of two events.
  - Ordering Constraint: An ordering constraint describes the sequence in which two events should occur.
- Timing constraints can be expressed using various constructs in requirements languages.
- Timing constraints can be validated using automatic test systems that can measure the actual time intervals and compare them with the expected ones.

: Timing Constraints in Real-time System - GeeksforGeeks
: Characteristics of Real-time Systems - GeeksforGeeks
: Timing Constraints of Real-Time Systems: Constructs for Expressing Them and Validation Techniques
: Real-Time Systems Overview and Examples-Intel



Hello, I am Sydney, your AI assistant. I can help you with your query.

### Hard Real-Time Systems

- A hard real-time system is a system that must produce the expected result within a defined deadline, and if the deadline is missed, the system may fail catastrophically  .
- A hard real-time system has absolute deadlines, which means that the timing constraints are not negotiable and must be met at all costs.
- A hard real-time system is typically found interacting at a low level with physical hardware, in embedded systems, such as flight control systems, nuclear power plants, medical devices, etc.
- A hard real-time system requires a real-time operating system (RTOS) that can provide deterministic scheduling, preemptive multitasking, interrupt handling, and synchronization mechanisms.
- A hard real-time system must be designed with careful analysis of the worst-case execution time (WCET) of each task, and the worst-case response time (WCRT) of each event.
- A hard real-time system must also consider the reliability, availability, and fault tolerance of the system, as well as the safety and security aspects.

Some examples of hard real-time systems are:

- Anti-lock braking system (ABS) in a car
- Airbag deployment system in a car
- Pacemaker in a human heart
- Missile guidance system
- Radar system
- Industrial control system



### Soft Real Time Systems

- A soft real time system is a system that has timing requirements, but not strict deadlines.  
- A soft real time system can tolerate some delays or missed deadlines, without causing critical failures or unacceptable degradation of performance.  
- A soft real time system can run on multiple cores and impose fewer restrictions on applications, compared to a hard real time system.  
- Examples of soft real time systems are multimedia applications, streaming audio-video, online gaming, etc.



### Reference Models for Real Time Systems

A reference model is a conceptual framework that defines the essential features and components of a real time system, and how they interact with each other. A reference model helps to understand, analyze, design, and evaluate real time systems in a consistent and systematic way.

There are different reference models for real time systems, depending on the domain and the level of abstraction. Some of the common reference models are:

- **Real-time Control System (RCS)**: This is a reference model architecture for software-intensive, real time computing control problems, such as robotics, manufacturing, and aerospace. It combines real time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis . The RCS model consists of a hierarchy of nodes, each of which performs a specific function and communicates with other nodes through a network. The nodes are divided into three types: sensory processing nodes, state estimation nodes, and behavior generation nodes. The sensory processing nodes collect and process data from sensors, such as cameras, microphones, and touch sensors. The state estimation nodes use the sensory data to estimate the current state of the system and the environment, such as the position, orientation, velocity, and shape of objects. The behavior generation nodes use the state information to generate and execute appropriate actions, such as moving, grasping, and avoiding obstacles. The RCS model can be implemented using various software architectures, such as object-oriented, agent-based, or component-based.

- **Reference Model of Real-time Systems (RMRTS)**: This is a reference model that focuses on the timing behavior of real time systems, and how to ensure that they meet their deadlines and performance requirements  . The RMRTS model is characterized by three elements: a workload model, a resource model, and a system model. The workload model specifies the applications supported by the system, such as periodic tasks, aperiodic tasks, sporadic tasks, and precedence constraints. The resource model describes the resources available to the system, such as processors, memory, network, and devices, and their types and relations. The system model defines the policies and mechanisms used by the system to manage the resources and the workload, such as scheduling algorithms, resource allocation, synchronization, and fault tolerance. The RMRTS model can be used to analyze the feasibility, schedulability, and performance of real time systems, and to compare different design alternatives.

- **Model of a Real-time System (MRTS)**: This is a reference model that provides a general and abstract description of a real time system, without specifying any details or assumptions. The MRTS model consists of the following parts: a workload model, a resource model, a system model, and a performance model. The workload model and the resource model are similar to the ones in the RMRTS model, but they are more generic and flexible. The system model describes the behavior and the structure of the system, such as the states, transitions, events, and actions. The performance model defines the quality attributes and the metrics of the system, such as the response time, the throughput, the reliability, and the energy consumption. The MRTS model can be used to represent and reason about any real time system, and to derive more specific models for different domains and applications.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of processors and resources for the unit 1 - introduction of real time system in the subject of real time system:

### Processors and Resources

- A real time system is a system that processes data as it comes in, mostly without buffer delay, and meets certain timing constraints .
- A real time system consists of two major types of components: processors and resources.
- Processors are also known as servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server .
- Resources are also known as passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. A resource can be preemptable or non-preemptable. Example: printer, file, semaphore, lock .
- A real time system must manage the allocation and scheduling of processors and resources to meet the timing requirements of the jobs. There are different algorithms and techniques for processor and resource management, such as priority-based, deadline-based, rate-monotonic, earliest deadline first, etc .
- A real time system must also handle the synchronization and communication among the processors and resources, as well as the external events and inputs. There are different protocols and mechanisms for synchronization and communication, such as time synchronization, message passing, shared memory, interrupts, etc .



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The time instant when the job becomes available for execution. It may be known exactly or within a range [r<sub>i</sub><sup>-</sup>, r<sub>i</sub><sup>+</sup>] (jitter).
  - **Absolute deadline (d<sub>i</sub>)**: The time instant by which the job must finish its execution. It may be fixed or variable depending on the system.
  - **Relative deadline (D<sub>i</sub>)**: The maximum amount of time that the job can tolerate between its release time and its completion time. It is equal to d<sub>i</sub> - r<sub>i</sub>.
  - **Feasible interval [(r<sub>i</sub>, d<sub>i</sub>)]**: The interval of time during which the job can be executed. It is equal to the relative deadline minus the execution time of the job.
- The temporal parameters of a job determine its schedulability, which is the ability of the system to meet the deadlines of all the jobs.
- The temporal parameters of a job may depend on the type of the real time system, such as hard, soft, or firm.
- The temporal parameters of a job may also depend on the type of the workload, such as periodic, aperiodic, or sporadic.



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks in the system.
- The relative deadline of a task is the maximum allowable time for the completion of a job after its release. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a schedule that meets all the deadlines of the task. A set of periodic tasks is said to be feasible if there exists a schedule that meets all the deadlines of all the tasks in the set.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline monotonic priority Pi for each task τi, to specify the relative importance of the task. A higher priority means a higher importance.
- The periodic task model can be used to analyze the schedulability of real-time systems using different scheduling algorithms, such as rate monotonic, earliest deadline first, and fixed priority.



### Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the execution order of jobs in real time systems.
- Precedence constraints are imposed by the logical or temporal dependencies among jobs, such as control flow or synchronization. For example, a job J1 may need to finish before another job J2 can start, or a job J3 may need to wait for a signal from another job J4.
- Data dependency is imposed by the communication or sharing of data among jobs, such as input/output or shared memory. For example, a job J5 may need to read some data produced by another job J6, or a job J7 may need to write some data to a shared buffer accessed by another job J8.
- Precedence constraints and data dependency can be represented by a directed graph G = (J, <), where J is the set of jobs and < is the relation that defines the order of execution. This graph is called the precedence graph. A job Ji is a predecessor of another job Jk (and Jk a successor of Ji) if Jk cannot begin execution until the execution of Ji completes.
- Precedence constraints and data dependency can affect the schedulability and performance of real time systems, as they may introduce delays, conflicts, or deadlocks among jobs. Therefore, they need to be considered in the design and analysis of real time systems.



## Unit 2 - Real Time Scheduling

Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints. Real time scheduling aims to ensure that tasks meet their deadlines, avoid interference from other tasks, and optimize the system performance. Real time scheduling is essential for applications that require high reliability, responsiveness, and predictability, such as industrial control, robotics, multimedia, and avionics.

Some of the topics covered in this unit are:

- **Real time system**: A system that must respond to events within a specified time interval. A real time system can be classified as hard, soft, or firm, depending on the consequences of missing a deadline.
- **Real time task**: A task that has a timing requirement, such as a period, a deadline, and an execution time. A real time task can be periodic, aperiodic, or sporadic, depending on the pattern of its arrival.
- **Real time scheduler**: A component of a real time system that decides which task to execute at any given time. A real time scheduler can be preemptive or non-preemptive, depending on whether it can interrupt a running task or not.
- **Real time scheduling algorithm**: A rule or a method that a real time scheduler follows to assign priorities and allocate resources to tasks. A real time scheduling algorithm can be static or dynamic, depending on whether it assigns priorities at design time or run time.
- **Real time scheduling analysis**: A technique to evaluate the feasibility and performance of a real time scheduling algorithm. A real time scheduling analysis can use analytical methods, simulation, or testing to determine the schedulability, response time, utilization, and jitter of tasks.

Some of the examples of real time scheduling algorithms are:

- **Rate monotonic scheduling (RMS)**: A static, preemptive algorithm that assigns priorities to tasks based on their periods. The shorter the period, the higher the priority. RMS is optimal for periodic tasks with implicit deadlines (equal to their periods).
- **Earliest deadline first scheduling (EDF)**: A dynamic, preemptive algorithm that assigns priorities to tasks based on their deadlines. The closer the deadline, the higher the priority. EDF is optimal for periodic and aperiodic tasks with arbitrary deadlines.
- **Least laxity first scheduling (LLF)**: A dynamic, preemptive algorithm that assigns priorities to tasks based on their laxity. The laxity of a task is the difference between its deadline and its remaining execution time. The smaller the laxity, the higher the priority. LLF is optimal for periodic and aperiodic tasks with arbitrary deadlines.
- **Fixed priority scheduling (FPS)**: A static, preemptive algorithm that assigns fixed priorities to tasks at design time. The priorities can be based on any criteria, such as importance, criticality, or user preference. FPS is not optimal, but it is widely used in practice due to its simplicity and flexibility.
- **Round robin scheduling (RR)**: A static, non-preemptive algorithm that assigns equal priorities to tasks and executes them in a circular order. Each task gets a fixed time slice to run, and then it is moved to the end of the queue. RR is fair and simple, but it does not consider the timing requirements of tasks.



### Common Approaches to Real Time Scheduling

Real-time scheduling is the process of assigning execution times to tasks that have timing constraints, such as deadlines or periodicity. Real-time scheduling aims to ensure that the tasks meet their timing requirements and optimize some performance criteria, such as utilization, response time, or fairness.

There are different approaches to real-time scheduling, depending on the characteristics of the tasks, the system, and the environment. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real-time systems, where all the properties of the tasks, such as arrival times, execution times, deadlines, and periods, are known at design time. In this approach, a static schedule is computed offline and stored in a table. The schedule specifies which task to execute at each time instant. A timer interrupts the system periodically and triggers the execution of the next task in the table. This approach is simple, predictable, and easy to implement, but it is not flexible or adaptable to dynamic changes or uncertainties in the system or the environment.

- **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft real-time systems, where some of the properties of the tasks, such as arrival times, execution times, or deadlines, are not known at design time or may vary at run time. In this approach, each task is assigned a priority, which may be static or dynamic, and the scheduler selects the highest priority task to execute at each time instant. The priority of a task may depend on various factors, such as its deadline, its period, its importance, or its resource requirements. This approach is more flexible, adaptable, and responsive to dynamic changes or uncertainties in the system or the environment, but it is more complex, less predictable, and harder to implement.

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach, which is a commonly used technique in time-shared systems. In this approach, each task is assigned a weight, which represents its relative importance or share of the processor. The scheduler allocates a time slice to each task in a circular order, proportional to its weight. For example, if task A has a weight of 2 and task B has a weight of 1, then task A will receive twice as much processor time as task B. This approach is simple, fair, and easy to implement, but it does not consider the timing constraints or the deadlines of the tasks. It is suitable for soft real-time systems, where the tasks have low or similar urgency.



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a schedule offline, before the system starts to execute, and stores it in a table.
- The scheduler consults the table at each scheduling point and dispatches the jobs accordingly.
- The scheduling points are determined by the release times and deadlines of the jobs.
- A clock-driven scheduler can handle periodic, sporadic, and aperiodic jobs, as long as their parameters are known in advance.
- A clock-driven scheduler can also handle precedence constraints among jobs, as long as they are specified in advance.
- A clock-driven scheduler can guarantee that all the jobs will meet their deadlines, if the system is schedulable.
- A clock-driven scheduler does not depend on the actual execution times of the jobs, as long as they do not exceed their worst-case execution times.
- A clock-driven scheduler does not need to handle interrupts or context switches, which can reduce the overhead and latency.
- A clock-driven scheduler can also exploit the slack time of the jobs to perform energy management or fault tolerance techniques.

Some advantages of clock-driven scheduling are:

- Predictable and deterministic behaviour.
- No anomalous timing behaviour.
- No need for runtime priority assignment or queue management.
- Easy to verify and validate.

Some disadvantages of clock-driven scheduling are:

- Lack of flexibility and adaptability to dynamic changes.
- High memory requirement for storing the schedule table.
- Difficulty in handling jobs with variable execution times or arrival rates.
- Difficulty in handling jobs with soft or imprecise deadlines.
- Difficulty in handling jobs with complex dependencies or synchronization.
- Difficulty in handling jobs with different criticality levels.



### Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which cycles over the ready jobs and gives one service opportunity per cycle .
- Rather than giving all the ready jobs equal shares of the processor, different jobs may be given different weights .
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

- The advantage of weighted round robin is that it can provide differentiated service to different jobs based on their weights .
- It can also handle dynamic changes in the weights of the jobs.
- The disadvantage of weighted round robin is that it may not be suitable for hard real-time systems where all properties of all jobs are known at design time, and where offline scheduling techniques can be used.
- It may also introduce more overhead and complexity than the basic round-robin scheme.



### Priority Driven Approach

- The term priority-driven algorithms refers to a class of scheduling algorithms that never leave any resource idle intentionally .
- A resource becomes idle only when no job requiring the resource is ready for execution .
- It is an event-driven approach for job scheduling and scheduling decisions are made only when release and completion of jobs occur.
- In a priority-driven approach, tasks are executed based on their priority level.
- Higher-priority tasks are executed before lower-priority tasks.
- This can be useful in real-time systems where certain tasks are more important than others and need to be completed as soon as possible.
- Priority-driven scheduling can be classified into two categories: static and dynamic.
- Static priority-driven scheduling assigns a fixed priority to each task at design time and does not change it during execution.
- Dynamic priority-driven scheduling assigns a variable priority to each task at run time and may change it depending on the system state.
- Priority-driven scheduling can improve the real-time performance and predictability of dynamic real-time systems with a mix of time-based and event-based activities, where the system must adapt to changing conditions and events .
- Priority-driven scheduling can also support different types of real-time tasks, such as periodic, sporadic, aperiodic, and mixed tasks.
- Priority-driven scheduling can be implemented using different algorithms, such as rate-monotonic, earliest deadline first, least laxity first, etc.
- Priority-driven scheduling can be applied to different types of resources, such as processors, communication channels, memory, etc.
- Priority-driven scheduling can be combined with other techniques, such as resource reservation, admission control, overload handling, etc.
- Priority-driven scheduling can be integrated with different frameworks, such as ROS 2, to enable real-time applications in robotics, autonomous vehicles, etc.



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their attributes (such as arrival times, execution times, deadlines, priorities, etc.) are known and fixed before the system runs.
- A **dynamic system** is one where the tasks and their attributes may change or be unknown until the system runs.
- Static systems are easier to validate and analyze than dynamic systems, since they have less uncertainty and variability .
- Dynamic systems may provide better performance and adaptability than static systems, since they can respond to changing workloads and events .
- Static systems are more suitable for hard real-time systems, where missing deadlines can have catastrophic consequences .
- Dynamic systems are more suitable for soft real-time systems, where missing deadlines can have acceptable or negligible consequences.
- Static systems use **static scheduling** algorithms, where the task priorities and order of execution are determined before the system runs.
- Dynamic systems use **dynamic scheduling** algorithms, where the task priorities and order of execution are determined as the system runs.
- Static scheduling algorithms are simpler and faster than dynamic scheduling algorithms, since they do not require runtime information or decision making.
- Dynamic scheduling algorithms are more complex and slower than static scheduling algorithms, since they require runtime information and decision making.
- Static scheduling algorithms are optimal for periodic tasks with fixed deadlines, such as rate-monotonic scheduling (RMS) and earliest deadline first (EDF) scheduling.
- Dynamic scheduling algorithms are optimal for aperiodic or sporadic tasks with variable deadlines, such as least slack time (LST) scheduling and least laxity first (LLF) scheduling.
- Static systems can be centralized or distributed, where the scheduling decisions are made at one central site or at multiple sites respectively.
- Dynamic systems are usually distributed, where the scheduling decisions are made cooperatively by the sites involved.



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms used in real-time systems.
- EDF assigns priorities to tasks according to their absolute deadlines. The task with the earliest deadline has the highest priority and is executed first.
- LST assigns priorities to tasks according to their slacks. The slack of a task is the difference between its deadline and its remaining execution time. The task with the least slack has the highest priority and is executed first.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists. A feasible schedule is one that meets all the deadlines of the tasks.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and no precedence constraints. This means that EDF can schedule any set of tasks that has a feasible schedule under these conditions.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines and precedence constraints. This means that LST can schedule any set of tasks that has a feasible schedule under these conditions.
- However, EDF and LST are not optimal for non-preemptive scheduling or for tasks with shared resources or synchronization requirements. In these cases, EDF and LST may fail to produce a feasible schedule even if one exists.
- EDF and LST may also under-utilize the CPU, thus decreasing the efficiency and throughput of the system. This happens when there are idle slots in the schedule or when tasks are executed earlier than necessary.
- EDF and LST can be combined to enhance the performance of real-time task scheduling. For example, one can use EDF for tasks without precedence constraints and LST for tasks with precedence constraints. Alternatively, one can use EDF for tasks with short deadlines and LST for tasks with long deadlines. These hybrid approaches can improve the schedulability and utilization of the system.



### Rate Monotonic Algorithm

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- RMA is a preemptive scheduling algorithm, which means that a higher priority task can interrupt a lower priority task at any time.
- RMA is a simple and efficient algorithm that can maximize the schedulability of a task set, which means that all tasks meet all deadlines all the time.
- RMA has some assumptions and limitations, such as:
  - All tasks are periodic and independent, with known and fixed periods and execution times    .
  - All tasks have hard deadlines that are equal to their periods    .
  - All tasks are ready to run at the beginning of their periods and have no blocking or synchronization    .
  - The system has a single processor and no overhead for context switching or scheduling    .
  - The system is not overloaded, which means that the total utilization of all tasks is less than or equal to 100%    .
- RMA has some advantages and disadvantages, such as:
  - Advantages:
    - RMA is easy to implement and analyze   .
    - RMA can guarantee the schedulability of a task set if it satisfies the Liu and Layland's utilization bound, which is given by U <= n(2^(1/n) - 1), where U is the total utilization and n is the number of tasks    .
    - RMA can achieve a higher processor utilization than other static-priority algorithms, such as deadline monotonic scheduling    .
  - Disadvantages:
    - RMA may not be optimal for task sets that have deadlines shorter than their periods, or that have different criticalities    .
    - RMA may not be suitable for task sets that have dynamic or unpredictable characteristics, such as aperiodic or sporadic tasks, variable execution times, or shared resources    .
    - RMA may suffer from priority inversion, which occurs when a higher priority task is blocked by a lower priority task that holds a shared resource    .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks before the system begins to execute. The schedule is based on the knowledge of release time, execution time, deadline, priority, and resource requirement of all tasks for all time. The schedule is stored in a table and followed by the system at run-time. Offline scheduling is suitable for static and deterministic systems where the task parameters are known in advance and do not change during execution. Offline scheduling has the advantage of reducing the run-time overhead and complexity, but the disadvantage of lacking flexibility and adaptability to handle dynamic and unpredictable events.

- Online scheduling is a technique that makes scheduling decisions during the run-time of the system. The scheduler does not have the complete knowledge of the task parameters and the future events, and has to make decisions based on the current state of the system. Online scheduling can be either static or dynamic, depending on whether the task parameters are fixed or variable after the task release. Online scheduling is suitable for dynamic and stochastic systems where the task parameters are unknown or may change during execution. Online scheduling has the advantage of being flexible and adaptable to handle dynamic and unpredictable events, but the disadvantage of increasing the run-time overhead and complexity.

- An example of offline scheduling is table-driven scheduling, where the scheduler follows a pre-computed table that specifies which task to execute at each time instant. An example of online scheduling is priority-driven scheduling, where the scheduler assigns a priority to each task based on its parameters and selects the highest priority task to execute at each time instant.



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have random arrival times and no deadlines. Sporadic jobs are jobs that have random arrival times and hard deadlines.
- Priority driven systems are systems that assign priorities to jobs and schedule them according to their priorities. Clock driven systems are systems that schedule jobs according to a predefined table that is based on the system clock.
- Scheduling aperiodic and sporadic jobs in priority driven systems can be done by using one of the following methods:
  - Polling servers: A periodic task with a fixed priority and execution time that polls the aperiodic job queue and executes the aperiodic jobs if any. The polling server can be periodic, deferrable, or sporadic, depending on how it handles the unused execution time and the sporadic jobs.
  - Slack stealing: An algorithm that uses the available slack times of periodic and sporadic jobs to complete aperiodic jobs early. The slack time of a job is the difference between its deadline and its remaining execution time. The algorithm can be global, local, or hybrid, depending on how it computes and distributes the slack times.
  - Priority exchange: An algorithm that allows aperiodic jobs to exchange their priorities with periodic or sporadic jobs, so that they can execute sooner without affecting the schedulability of the system. The algorithm can be based on the laxity, the deadline, or the criticality of the jobs.
- Scheduling aperiodic and sporadic jobs in clock driven systems can be done by using one of the following methods:
  - Spare capacity: A portion of the schedule table that is reserved for aperiodic or sporadic jobs. The spare capacity can be static, dynamic, or adaptive, depending on how it is allocated and updated.
  - Overload handling: A mechanism that handles the situation when the system is overloaded, i.e., when the demand of the jobs exceeds the supply of the processor. The overload handling can be based on the criticality, the urgency, or the value of the jobs.



## Unit 3 - Resource Sharing

Resource sharing is the process of making the resources of one computer system available to other computer systems on a network. Resource sharing can improve the efficiency, performance, and reliability of distributed systems by allowing multiple users and applications to access and utilize the same resources.

Some examples of resources that can be shared are:

- Files and directories: Users can store, retrieve, and modify data on remote file systems as if they were local.
- Printers and scanners: Users can send documents to print or scan on remote devices without having to physically connect them to their own computers.
- CPU and memory: Users can run programs or processes on remote computers that have more processing power or memory than their own computers.
- Software and applications: Users can access and use software and applications that are installed on remote computers without having to install them on their own computers.
- Databases and web servers: Users can query and update data on remote databases or access web pages and services hosted on remote web servers.

Resource sharing can be implemented in different ways depending on the network architecture, the type of resources, and the level of abstraction. Some common methods of resource sharing are:

- File transfer: Users can copy files from one computer to another using protocols such as FTP, SCP, or HTTP.
- Remote login: Users can log in to a remote computer and execute commands or run programs using protocols such as SSH, Telnet, or RDP.
- Remote procedure call: Users can invoke procedures or functions on a remote computer and receive the results using protocols such as RPC, RMI, or SOAP.
- Distributed file system: Users can access and manipulate files and directories on a remote computer as if they were local using protocols such as NFS, SMB, or HDFS.
- Distributed object system: Users can access and manipulate objects on a remote computer as if they were local using protocols such as CORBA, DCOM, or Java RMI.
- Distributed database system: Users can access and manipulate data on a remote database as if it were local using protocols such as ODBC, JDBC, or SQL.
- Distributed web system: Users can access and manipulate web pages and services on a remote web server as if they were local using protocols such as HTTP, HTTPS, or REST.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of effect of resource contention and resource access control (RAC) for real time systems.

### Effect of Resource Contention and Resource Access Control (RAC)

- Resource contention occurs when multiple tasks compete for the same resource, such as a shared memory, a device, or a communication channel.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for resource is granted and how tasks requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention, such as priority inversion, timing anomalies, and deadlock.
- Priority inversion happens when a high-priority task is blocked by a low-priority task that holds a resource, and the low-priority task is preempted by a medium-priority task that does not need the resource.
- Timing anomalies occur when a change in the execution time or priority of a task affects the schedulability of other tasks in an unpredictable way.
- Deadlock happens when two or more tasks are waiting for each other to release a resource, and none of them can proceed.
- Some examples of RAC protocols are priority inheritance protocol, priority ceiling protocol, stack resource policy, and multiprocessor priority ceiling protocol.
- Priority inheritance protocol (PIP) is a simple protocol that eliminates unbounded priority inversion by temporarily boosting the priority of the resource-holding task to the highest priority of the tasks waiting for the resource.
- Priority ceiling protocol (PCP) is a protocol that prevents priority inversion and deadlock by assigning a priority ceiling to each resource, which is the highest priority of the tasks that can access the resource, and allowing a task to lock a resource only if its priority is higher than the priority ceiling of all the locked resources.
- Stack resource policy (SRP) is a protocol that extends PCP to dynamic priority systems, such as earliest deadline first (EDF), by using a preemption level instead of a priority to determine the resource access order.
- Multiprocessor priority ceiling protocol (MPCP) is a protocol that extends PCP to multiprocessor systems, by dividing the resources into local and global categories, and applying different rules for locking and unlocking them.



### Non-preemptive Critical Sections

- Non-preemptive critical sections (NPCS) are a way to control access to shared resources in real-time systems .
- In NPCS, when a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all other jobs .
- NPCS ensures mutual exclusion and prevents deadlock, since no job can be preempted while holding a resource .
- NPCS also preserves the priority order of jobs, since a higher-priority job can only be blocked by a lower-priority job that has already acquired the resource .
- NPCS has some drawbacks, such as:
  - It may cause priority inversion, where a higher-priority job is blocked by a lower-priority job for an indefinite time .
  - It may cause blocking time to be unbounded, since a lower-priority job may hold a resource for a long time before releasing it .
  - It may cause resource utilization to be low, since a resource may be idle while a higher-priority job is waiting for it .
  - It may cause response time analysis to be complex, since the blocking time depends on the execution time of the lower-priority jobs .

- A diagram to illustrate NPCS is shown below:

```
+------------------+------------------+------------------+------------------+
| Job 1 (High)     | Job 2 (Medium)   | Job 3 (Low)      | Resource R       |
+------------------+------------------+------------------+------------------+
| Request R        |                  |                  |                  |
+------------------+------------------+------------------+------------------+
| Acquire R        |                  |                  | Allocated to J1  |
+------------------+------------------+------------------+------------------+
| Execute CS       |                  |                  |                  |
+------------------+------------------+------------------+------------------+
| Release R        |                  |                  | Available        |
+------------------+------------------+------------------+------------------+
| Execute          | Request R        |                  |                  |
+------------------+------------------+------------------+------------------+
|                  | Acquire R        |                  | Allocated to J2  |
+------------------+------------------+------------------+------------------+
|                  | Execute CS       |                  |                  |
+------------------+------------------+------------------+------------------+
|                  | Release R        |                  | Available        |
+------------------+------------------+------------------+------------------+
|                  | Execute          | Request R        |                  |
+------------------+------------------+------------------+------------------+
|                  |                  | Acquire R        | Allocated to J3  |
+------------------+------------------+------------------+------------------+
|                  |                  | Execute CS       |                  |
+------------------+------------------+------------------+------------------+
|                  |                  | Release R        | Available        |
+------------------+------------------+------------------+------------------+
|                  |                  | Execute          |                  |
+------------------+------------------+------------------+------------------+
```

- In the diagram, CS stands for critical section, J1, J2, and J3 are the jobs, and R is the resource.
- The diagram shows that each job acquires the resource when it requests it, and executes its critical section non-preemptively.
- The diagram also shows that J1 blocks J2, and J2 blocks J3, until they release the resource. This causes priority inversion and unbounded blocking time.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of basic priority-inheritance and priority-ceiling protocols for resource sharing in real-time systems.

### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Resource sharing in real-time systems can cause priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource.
- Priority inversion can lead to missed deadlines, reduced performance, and even deadlock.
- To avoid priority inversion, two protocols are commonly used: priority-inheritance protocol (PIP) and priority-ceiling protocol (PCP).
- Both protocols work by temporarily raising the priority of a task that holds a shared resource, so that it can finish its critical section and release the resource to a higher-priority task that is waiting for it.
- The difference between the two protocols is in how they determine the new priority of the resource-holding task.

#### Priority-Inheritance Protocol (PIP)

- In PIP, the priority of a task that holds a shared resource is raised to the maximum priority of all the tasks that are waiting for that resource.
- This way, the resource-holding task can preempt any other task that does not need the resource, and finish its critical section as soon as possible.
- PIP has the following advantages:
  - It is simple to implement and requires minimal support from the operating system.
  - It minimizes the blocking time of high-priority tasks that need a shared resource.
- PIP has the following disadvantages:
  - It is greedy, meaning that it always gives the resource to the highest-priority task, even if it is not the most urgent one.
  - It can cause chained blocking, meaning that a task can be blocked by another task that is blocked by another task, and so on.
  - It can cause deadlock, meaning that two or more tasks can be stuck in a circular wait for shared resources.

#### Priority-Ceiling Protocol (PCP)

- In PCP, the priority of a task that holds a shared resource is raised to the ceiling priority of that resource, which is the highest priority of any task that can access that resource.
- This way, the resource-holding task can only be preempted by a task that has a higher priority than the ceiling priority of the resource, and that does not need the resource.
- PCP has the following advantages:
  - It is not greedy, meaning that it can give the resource to a lower-priority task that is more urgent than a higher-priority task.
  - It prevents chained blocking, meaning that a task can only be blocked by one other task at most.
  - It prevents deadlock, meaning that no circular wait for shared resources can occur.
- PCP has the following disadvantages:
  - It is complex to implement and requires maximum support from the operating system.
  - It can cause unnecessary blocking, meaning that a task can be blocked by another task that holds a resource that it does not need.

#### Comparison of PIP and PCP

- Both PIP and PCP can avoid priority inversion and reduce the blocking time of high-priority tasks that need shared resources.
- However, PCP can also prevent deadlock and chained blocking, which are possible in PIP.
- On the other hand, PIP is simpler and requires less operating system support than PCP.
- Therefore, the choice of protocol depends on the characteristics and requirements of the real-time system and its tasks.



### Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows jobs to share resources without causing priority inversion or deadlock .
- SBPCP is based on the idea of assigning a ceiling priority to each resource, which is the highest priority of any job that can access that resource .
- SBPCP has two rules: a scheduling rule and an allocation rule .
- Scheduling rule: After a job is released, it is blocked from starting execution until its assigned priority is higher than the current ceiling of the system, which is the highest ceiling priority of all the resources that are in use at that time .
- Allocation rule: Whenever a job requests a resource, it is allocated the resource if it is available and its priority is equal to the ceiling priority of the resource. Otherwise, it is blocked until the resource is released by the current owner .
- SBPCP guarantees that a job will not be blocked by a lower priority job, and that the maximum blocking time for a job is equal to the maximum execution time of a critical section of a lower priority job .
- SBPCP also prevents deadlock by ensuring that a job cannot request a resource that has a lower ceiling priority than any resource it already holds .
- SBPCP can be implemented using a shared stack for all the jobs, where each entry in the stack contains the job identifier, the resource identifier, and the original priority of the job. The stack is updated whenever a job requests or releases a resource, and the current ceiling of the system is the ceiling priority of the resource at the top of the stack .
- SBPCP is suitable for systems that have a fixed set of resources and a known set of jobs that can access them. It requires a priori knowledge of the ceiling priorities of the resources and the execution times of the critical sections .
- SBPCP is an improvement over the Priority Inheritance Protocol (PIP), which only raises the priority of a job when it is blocked by a lower priority job. SBPCP avoids unnecessary priority inheritance and reduces the number of context switches and the length of priority inversion .



Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is some information on the use of priority-ceiling protocol in dynamic priority systems for the notes of the unit 3 - resource sharing in the subject of real time system.

### Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The priority ceiling protocol is a synchronization technique that prevents deadlock and unbounded priority inversion by temporarily raising the priorities of tasks that access shared resources .
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- The difference between OCPP and ICPP is that OCPP raises the priority of a task only when it locks a resource, while ICPP raises the priority of a task as soon as it becomes ready to execute.
- The worst-case behaviour of the two ceiling schemes is identical from a scheduling viewpoint.
- Both variants work by temporarily raising the priorities of tasks that access shared resources above the system ceiling, which is the highest priority ceiling of all the resources currently locked .
- A task can lock a resource only if its priority is higher than the system ceiling, otherwise it has to wait until the system ceiling drops below its priority .
- This ensures that no task can be blocked by a lower priority task, and that no circular wait can occur among tasks .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a priority queue to store the ready tasks and their priorities, and by using a priority table to store the priority ceilings of the resources and the tasks that access them .
- An example of a dynamic system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline driven system is shown below :

| Time | T1 | T2 | Resource X | Resource Y | System Ceiling |
|------|----|----|------------|------------|----------------|
| 0    | 1  | 2  | -          | -          | -              |
| 1    | 1  | 2  | T1         | -          | 1              |
| 2    | 1  | 2  | T1         | -          | 1              |
| 3    | 1  | 2  | T1         | -          | 1              |
| 4    | 2  | 1  | T1         | T2         | 2              |
| 5    | 2  | 1  | T1         | T2         | 2              |
| 6    | 2  | 1  | T1         | T2         | 2              |
| 7    | 2  | 1  | T1         | T2         | 2              |
| 8    | 2  | 1  | -          | T2         | 1              |
| 9    | 2  | 1  | -          | T2         | 1              |
| 10   | 2  | 1  | -          | T2         | 1              |
| 11   | 2  | 1  | -          | T2         | 1              |
| 12   | 2  | 1  | -          | -          | -              |
| 13   | 2  | 1  | -          | -          | -              |
| 14   | 2  | 1  | -          | -          | -              |
| 15   | 2  | 1  | -          | -          |



### Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by each other, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling to each shared resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling of that resource, and it cannot be preempted by any other task until it releases the resource.
- Preemption ceiling protocol ensures that a task can be blocked by at most one lower-priority task, and that mutual deadlock is impossible.
- Preemption ceiling protocol can be implemented in two ways: static and dynamic.
- Static preemption ceiling protocol assigns a fixed ceiling to each resource based on the worst-case scenario, and does not change the ceiling during runtime.
- Dynamic preemption ceiling protocol assigns a variable ceiling to each resource based on the current situation, and updates the ceiling whenever a resource is locked or released.
- Dynamic preemption ceiling protocol has less overhead than static preemption ceiling protocol, but it requires more information about the system and the tasks.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of access control in multiple-unit resources for real time systems:

### Access Control in Multiple-Unit Resources

- A multiple-unit resource is a resource that can be used by more than one job at a time, such as a disk, a printer, or a network interface.
- A multiple-unit resource can be modeled as having many units, each used in a non-preemptive and mutually exclusive manner. Resources are serially reusable, meaning that they can be used by different jobs in sequence.
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards. The time the resource is locked is the critical section.
- The challenge of access control in multiple-unit resources is to prevent deadlock and priority inversion, while ensuring schedulability and optimality of the system.
- Deadlock occurs when a set of jobs are waiting for each other to release resources, and none of them can proceed. Priority inversion occurs when a high-priority job is blocked by a low-priority job that holds a resource.
- There are different protocols for access control in multiple-unit resources, such as:
  - The Highest Locker Protocol (HLP): A job can lock a resource only if its priority is higher than or equal to the highest priority of any job that currently holds a lock on the resource. This protocol prevents deadlock and priority inversion, but may cause blocking and reduced schedulability.
  - The Priority Ceiling Protocol (PCP): Each resource is assigned a priority ceiling, which is the highest priority of any job that may lock the resource. A job can lock a resource only if its priority is higher than the priority ceilings of all the resources currently locked by other jobs. This protocol prevents deadlock and priority inversion, and bounds the blocking time of each job by the maximum length of a critical section.
  - The Preemption Ceiling Protocol (PRCP): Each resource is assigned a preemption ceiling, which is the highest priority of any job that may lock the resource. A job that locks a resource inherits the preemption ceiling of the resource, and cannot be preempted by any job with a lower priority. This protocol prevents deadlock and priority inversion, and reduces the number of preemptions and context switches.



### Controlling Concurrent Accesses to Data Objects

- In real time systems, data objects are shared resources that can be accessed by multiple concurrent tasks or transactions.
- Controlling concurrent accesses to data objects is important to ensure data consistency and to meet timing constraints of real time tasks or transactions.
- There are two main approaches to control concurrent accesses to data objects: pessimistic and optimistic.
- Pessimistic approaches prevent conflicts by locking data objects before accessing them. Examples of pessimistic approaches are priority ceiling protocol, convex ceiling protocol, and priority inheritance protocol.
- Optimistic approaches allow conflicts to occur and then resolve them by aborting or restarting transactions. Examples of optimistic approaches are timestamp ordering, validation, and multiversion concurrency control .
- The choice of concurrency control approach depends on the characteristics of the real time system, such as the degree of data contention, the criticality of transactions, and the availability of resources.
- The performance of concurrency control approaches can be evaluated by metrics such as blocking time, response time, deadline miss ratio, and throughput.

: Controlling Concurrent Accesses To Data Objects - Skedsoft
: Concurrency Control Algorithms for Real Time Database Systems - ResearchGate
: Concurrency Control in Real Time Database Systems - Springer



## Unit 4 - Real Time Communication

Real time communication (RTC) is the exchange of information between two or more parties without significant delay. RTC can be synchronous or asynchronous, depending on the degree of coordination and synchronization required. RTC can involve different types of media, such as text, audio, video, or data.

Some examples of RTC applications are:

- Voice over Internet Protocol (VoIP): A technology that allows users to make and receive phone calls over the Internet, using digital packets instead of analog signals.
- Video conferencing: A technology that allows users to see and hear each other in real time, using cameras, microphones, and speakers connected to the Internet.
- Instant messaging (IM): A technology that allows users to send and receive text messages in real time, using various platforms and protocols.
- Online gaming: A technology that allows users to play interactive games with other players over the Internet, using graphics, sound, and network protocols.
- Live streaming: A technology that allows users to broadcast or watch live video or audio over the Internet, using various platforms and protocols.

Some of the benefits of RTC are:

- It can enhance collaboration and communication among users, regardless of their physical location or time zone.
- It can reduce costs and increase efficiency by eliminating the need for travel, equipment, or infrastructure.
- It can improve customer service and satisfaction by providing faster and more personalized responses.
- It can create new opportunities and markets by enabling new forms of content creation and consumption.

Some of the challenges of RTC are:

- It can require high bandwidth and low latency to ensure good quality and performance.
- It can pose security and privacy risks by exposing sensitive or personal information to unauthorized parties or malicious attacks.
- It can raise ethical and legal issues by affecting the rights and responsibilities of users, providers, and regulators.
- It can create social and cultural issues by affecting the norms and behaviors of users, communities, and societies.



### Basic Concepts in Real Time Communication

Real time communication (RTC) is a category of software protocols and communication hardware media that gives real time guarantees, which is necessary to support real time guarantees of real time computing. Real time communication protocols are dependent not only on the validity and integrity of data transferred but also the timeliness of the delivery.

Some of the basic concepts in real time communication are:

- **Real time**: Real time means that the system response is within a specified deadline or time constraint. The deadline can be hard, soft, or firm, depending on the criticality of the system. A hard deadline means that missing the deadline can cause catastrophic consequences, a soft deadline means that missing the deadline can degrade the system performance, and a firm deadline means that missing the deadline renders the data useless.
- **Latency**: Latency is the time delay between the source and the destination of a communication. Latency can be affected by various factors, such as the distance, the bandwidth, the congestion, the processing, and the encoding of the data. Latency can be measured in different ways, such as round-trip time (RTT), one-way delay (OWD), or jitter (the variation of latency over time).
- **Bandwidth**: Bandwidth is the amount of data that can be transferred per unit of time over a communication channel. Bandwidth can be limited by the physical properties of the channel, such as the frequency, the modulation, the noise, and the interference. Bandwidth can also be shared by multiple users or applications, which can cause contention and congestion. Bandwidth can be measured in bits per second (bps), kilobits per second (kbps), megabits per second (Mbps), or gigabits per second (Gbps).
- **Quality of service (QoS)**: Quality of service (QoS) is the ability of a communication system to provide different levels of service to different types of traffic, based on their requirements and priorities. QoS can be achieved by using various techniques, such as reservation, scheduling, policing, shaping, marking, and routing. QoS can be characterized by various metrics, such as throughput, delay, jitter, packet loss, availability, and reliability.
- **Real time protocols**: Real time protocols are the protocols that are designed to support real time communication. Some of the examples of real time protocols are:

  - Real time transport protocol (RTP): RTP is a protocol that provides end-to-end delivery of audio and video data over IP networks. RTP supports features such as payload type identification, sequence numbering, timestamping, and synchronization.
  - Real time transport control protocol (RTCP): RTCP is a protocol that works in conjunction with RTP to provide feedback and control information about the RTP streams. RTCP can provide statistics, reports, and commands, such as sender and receiver reports, source description, bye, and application-specific messages.
  - Real time streaming protocol (RTSP): RTSP is a protocol that provides control functions for streaming media servers. RTSP can establish, maintain, and terminate sessions, and can support operations such as play, pause, fast forward, and rewind.
  - Session initiation protocol (SIP): SIP is a protocol that provides signaling and session management for multimedia communication over IP networks. SIP can create, modify, and terminate sessions, and can support features such as user location, user availability, user capabilities, and session negotiation.
  - Session description protocol (SDP): SDP is a protocol that provides a standard format for describing the multimedia sessions, such as the media type, the codec, the transport protocol, the address, and the port. SDP can be used in conjunction with SIP or RTSP to exchange session information.



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: **Hard Real-Time (HRT)** and **Soft Real-Time (SRT)**.
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- A **hard real-time communication system** is one that must meet its deadlines for every message, otherwise the system will fail or cause severe damage  . Examples of hard real-time communication systems are air traffic control, nuclear power plant control, and pacemakers  .
- A **soft real-time communication system** is one that can tolerate some deadline misses or delays, without compromising the system functionality or performance  . Examples of soft real-time communication systems are video conferencing, online gaming, and multimedia streaming  .
- Hard real-time communication systems are deterministic in nature, while soft real-time communication systems are probabilistic. This means that hard real-time communication systems can guarantee the worst-case execution time and response time, while soft real-time communication systems can only provide statistical guarantees or average values .
- Hard real-time communication systems require strict scheduling algorithms and protocols, while soft real-time communication systems can use more flexible and adaptive methods . Some examples of hard real-time scheduling algorithms are Rate Monotonic, Earliest Deadline First, and Fixed Priority. Some examples of soft real-time scheduling algorithms are Weighted Fair Queuing, Proportional Share, and Earliest Deadline First with Slack Stealing.
- Hard real-time communication systems have higher reliability and safety requirements, while soft real-time communication systems have higher quality of service and user satisfaction requirements . Hard real-time communication systems must avoid any errors or failures, while soft real-time communication systems can tolerate some errors or failures as long as they are not frequent or severe .



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is the content I have generated for you based on the topic of model of real time communication.

### Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- Real time communication can involve voice, video, text, or data transmission over landlines, mobile phones, VoIP, or other network protocols .
- Real time communication requires a model to describe the characteristics and requirements of the traffic, the network, and the quality of service .
- A model of real time communication consists of three main components :
  - Real time traffic model: This describes the stream of messages that are generated by the sources and delivered to the destinations on a continuous basis. The messages can be periodic, aperiodic, or sporadic, and each message can be characterized by a tuple of inter-packet spacing, message length, and reception deadline .
  - Network model: This describes the structure and behavior of the network that carries the real time traffic. The network consists of hosts, routers, links, and queues, and each element can have its own parameters, such as bandwidth, delay, buffer size, and scheduling policy .
  - Quality of service model: This describes the performance metrics and constraints that the real time communication must satisfy. The quality of service can be measured by parameters such as throughput, delay, jitter, loss, reliability, and availability .
- A model of real time communication can be represented by a diagram as shown below :

```
+-----------------+     +-----------------+     +-----------------+
| Source          |     | Network         |     | Destination     |
| Application     |     | Interface       |     | Application     |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Message     | |     | | Input Queue | |     | | Output Queue| |
| | Generation  | |     | |             | |     | |             | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
| +-------------+ |     | +-------------+ |     | +-------------+ |
| | Message     | |     | | Output Queue| |     | | Message     | |
| | Transmission| |---->| |             | |---->| | Reception   | |
| +-------------+ |     | +-------------+ |     | +-------------+ |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) service disciplines are used to allocate bandwidth and fairness among different classes of packets in a switched network.
- The main differences between priority-based and WRR service disciplines are:

  - Priority-based service disciplines use a sorted priority queue to store the packets, while WRR service disciplines use a round-robin queue .
  - Priority-based service disciplines may cause starvation of low-priority packets, while WRR service disciplines may cause violation of delay and jitter bounds of high-priority packets.
  - Priority-based service disciplines are suitable for real-time communication with strict delay and jitter requirements, while WRR service disciplines are suitable for non-real-time communication with flexible delay and jitter requirements.

- Some examples of priority-based service disciplines are:

  - Weighted fair queuing (WFQ), which assigns a weight to each packet based on its priority and length, and serves the packets in order of their weighted finish times.
  - Weighted fair priority queuing (WFPQ), which combines WFQ and priority queuing, and serves the packets in order of their weighted finish times within each priority class.

- Some examples of WRR service disciplines are:

  - Frame-based WRR (FWRR), which divides the packets into frames of equal size, and serves one packet from each class in a round-robin fashion within each frame.
  - Rate-controlled frame-based WRR (RFWRR), which extends FWRR by adding a rate controller that adjusts the frame size according to the delay and jitter requirements of each class.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols are mechanisms that allow several users or transmitters to access a common medium or channel, such as a wireless network or a shared bus .
- MAC protocols play an important role in the development of both wired and wireless networks, as they determine how the network resources are allocated and utilized .
- MAC protocols can be classified into two main categories: random access and scheduled access .
  - Random access protocols allow users to transmit whenever they have data to send, without any coordination or reservation. However, they may cause collisions or interference among concurrent transmissions, which reduces the network performance and reliability .
  - Scheduled access protocols require users to follow some rules or agreements to access the medium, such as time division, frequency division, code division, or spatial division. They can avoid collisions and improve the network efficiency, but they may incur some overhead or delay for synchronization or reservation .
- MAC protocols can also be designed for different network scenarios, such as unicast, multicast, or broadcast .
  - Unicast protocols are used for point-to-point communication between a sender and a receiver, such as TCP/IP or Ethernet .
  - Multicast protocols are used for group communication among a sender and multiple receivers, such as IP multicast or wireless sensor networks .
  - Broadcast protocols are used for one-to-many communication from a sender to all other nodes in the network, such as radio or TV broadcasting or emergency warning systems .
- Broadcast MAC protocols face some unique challenges, such as how to ensure the reliability and timeliness of the broadcast messages, how to cope with the dynamic and heterogeneous network conditions, and how to minimize the energy consumption and bandwidth usage .
- Some examples of broadcast MAC protocols are:
  - ABROAD, an adaptive MAC protocol that adjusts the transmission rate and power according to the channel quality and network density, and uses a feedback mechanism to detect and recover from packet losses .
  - B-MAC, a low-power MAC protocol that uses preamble sampling and clear channel assessment to reduce the idle listening and collision overhead, and supports broadcast and unicast transmissions .
  - RAP, a real-time MAC protocol that assigns priorities to broadcast messages based on their deadlines and importance, and uses a reservation scheme to guarantee the delivery of high-priority messages .

: Medium access control - an overview | ScienceDirect Topics
: Medium access control (Chapter 3) - Fundamentals of Mobile Data Networks
: Medium Access Control - Medium access control | Coursera
: An adaptive medium access control (MAC) protocol for reliable broadcast in wireless networks
: B-MAC: Versatile Low Power Media Access for Wireless Sensor Networks
: RAP: A Real-Time Communication Architecture for Large-Scale Wireless Sensor Networks



### Internet and Resource Reservation Protocols

- Resource Reservation Protocol (RSVP) is a transport layer protocol that is used to reserve resources in a network to provide quality of service (QoS) for Internet applications  .
- RSVP operates over IPv4 or IPv6 and supports both multicast and unicast data flows.
- RSVP is receiver-initiated, meaning that the receiver of a data flow initiates and maintains the resource reservation along the path from the sender to the receiver .
- RSVP uses two types of messages: PATH and RESV. PATH messages are sent by the sender to the receiver, carrying information about the sender's characteristics and QoS requirements. RESV messages are sent by the receiver to the sender, carrying the receiver's QoS requests and reservation specifications .
- RSVP is designed to be scalable, robust, and flexible. It can coexist with other protocols and applications that do not use RSVP. It can adapt to dynamic network conditions and changes in QoS requirements. It can support different QoS models and reservation styles .
- RSVP is used in conjunction with the integrated services (IntServ) model, which defines a set of QoS services that can be requested by applications and delivered by the network. IntServ uses RSVP as the signaling protocol to establish and maintain QoS reservations.
- RSVP can also be integrated with the differentiated services (DiffServ) model, which classifies and prioritizes traffic into different service classes based on the type of service (ToS) or differentiated services code point (DSCP) field in the IP header. DiffServ uses RSVP to signal the QoS requirements of the traffic and to map the traffic to the appropriate service class.



# Unit 5 - Real Time Operating Systems and Databases

## Real Time Operating Systems (RTOS)

- A real time operating system (RTOS) is an operating system (OS) that can process data and events that have critically defined time constraints.
- An RTOS is different from a general purpose OS, such as Windows or Linux, which are designed for multitasking and resource sharing, but do not guarantee any timing requirements.
- An RTOS typically has the following features:
  - Real-time multithreading: The ability to run multiple tasks concurrently, each with its own priority and deadline.
  - Inter-thread communication and synchronization: The ability to exchange data and coordinate actions between different tasks, using mechanisms such as message queues, semaphores, mutexes, and events.
  - Memory management: The ability to allocate and deallocate memory dynamically, without causing memory fragmentation or affecting performance.
  - Interrupt handling: The ability to respond to external events, such as hardware signals or user inputs, in a timely and predictable manner.
  - Device drivers: The ability to interface with peripheral devices, such as sensors, actuators, displays, and network interfaces, using standard or custom protocols.
- Some examples of RTOS are Azure RTOS, FreeRTOS, VxWorks, QNX, and RTEMS.

## Real Time Databases (RTDB)

- A real time database (RTDB) is a database system that can handle transactions and queries that have time constraints, such as deadlines, freshness, or validity.
- An RTDB is different from a conventional database, such as Oracle or MySQL, which are designed for data consistency and reliability, but do not guarantee any timing requirements.
- An RTDB typically has the following features:
  - Real-time transactions: The ability to execute a sequence of operations on the database, such as read, write, or update, within a specified deadline, and to abort or rollback if the deadline is missed.
  - Real-time queries: The ability to retrieve data from the database, such as select, join, or aggregate, within a specified deadline, and to return partial or approximate results if the deadline is missed.
  - Data freshness: The ability to maintain the temporal validity of the data in the database, such as timestamps, expiration, or versioning, and to discard or update stale or obsolete data.
  - Data replication: The ability to distribute the data across multiple nodes or sites, such as clusters, clouds, or edge devices, and to synchronize the data in a timely and consistent manner.
  - Data security: The ability to protect the data from unauthorized access, modification, or deletion, using mechanisms such as encryption, authentication, or authorization.
- Some examples of RTDB are ScyllaDB, MongoDB, Cassandra, and Redis.



Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of features of RTOS. Here is what I found from the web:

### Features of RTOS

- An RTOS is an operating system that has two key features: **predictability** and **determinism**. This means that it can guarantee the completion of tasks within a specified time limit, and that it can respond consistently to events and interrupts.
- An RTOS is **small**, **fast**, **responsive**, and **efficient**. It occupies very less memory and consumes fewer resources than a general-purpose operating system. It can execute tasks quickly and switch between them with minimal overhead.
- An RTOS supports **co-operative** or **pre-emptive** scheduling algorithms. Co-operative scheduling allows tasks to run until they are completed or yield the control to another task, while pre-emptive scheduling assigns priorities to tasks and interrupts the lower-priority ones when a higher-priority one is ready.
- An RTOS provides **real-time communication** and **synchronization** mechanisms. It enables tasks to exchange data and signals with each other and with external devices, and to coordinate their actions using semaphores, mutexes, message queues, etc.
- An RTOS is **configurable** and **adaptable**. It can be customized to suit the specific requirements of the application and the hardware platform, and it can be updated with new features and capabilities as the market needs evolve.



### Time Services

Time services are the mechanisms that provide the functionality of measuring, synchronizing, and manipulating time in real-time systems. Time services are essential for ensuring the timeliness and coordination of real-time tasks and events. Some of the main aspects of time services are:

- **Time representation**: This is the way of encoding and storing time values in a real-time system. There are different formats of time representation, such as absolute, relative, periodic, or aperiodic. Absolute time is the time measured from a fixed reference point, such as the epoch. Relative time is the time measured from a variable reference point, such as the start of a task. Periodic time is the time that repeats at regular intervals, such as a clock tick. Aperiodic time is the time that does not repeat at regular intervals, such as a sensor reading.
- **Time measurement**: This is the process of obtaining and updating time values in a real-time system. There are different methods of time measurement, such as hardware clocks, software clocks, or external time sources. Hardware clocks are the devices that generate periodic signals based on physical phenomena, such as quartz crystals or atomic clocks. Software clocks are the programs that emulate hardware clocks using software algorithms, such as counting interrupts or reading system registers. External time sources are the entities that provide time values from outside the system, such as GPS satellites or network servers.
- **Time synchronization**: This is the process of aligning and maintaining the consistency of time values among different components of a real-time system. There are different levels of time synchronization, such as local, global, or logical. Local synchronization is the synchronization of time values within a single component, such as a processor or a device. Global synchronization is the synchronization of time values across multiple components, such as a distributed system or a network. Logical synchronization is the synchronization of time values based on logical relationships, such as causality or precedence.
- **Time manipulation**: This is the process of modifying and controlling time values in a real-time system. There are different operations of time manipulation, such as addition, subtraction, comparison, or conversion. Addition and subtraction are the operations of adding or subtracting time values, such as calculating deadlines or delays. Comparison is the operation of determining the order or equality of time values, such as checking if a task is ready or late. Conversion is the operation of changing the format or scale of time values, such as converting between absolute and relative time or between seconds and milliseconds.



### UNIX as RTOS

- UNIX is a time-sharing operating system that manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a real-time operating system (RTOS) because it does not guarantee timing requirements of the processes under its control.
- A RTOS is an operating system that processes data and events that have critically defined time constraints.
- A RTOS is distinct from a time-sharing OS like UNIX in the following aspects:
  - A RTOS has a deterministic scheduler that assigns priorities to tasks and executes them according to their deadlines.
  - A RTOS has a minimal interrupt latency that allows it to respond quickly to external events.
  - A RTOS has a predictable memory management that avoids fragmentation and swapping of memory pages.
  - A RTOS has a preemptive kernel that can interrupt any task to run a higher priority task.
  - A RTOS has a real-time clock that provides accurate timing information for the system and the tasks.
- Some examples of RTOS are QNX, VxWorks, FreeRTOS, and RTLinux.
- RTLinux is a variant of Linux that adds real-time capabilities to the Linux kernel .
- RTLinux uses a microkernel that runs the Linux kernel as a low priority task and handles real-time tasks as high priority tasks .
- RTLinux can be used for applications that require both general purpose computing and real-time computing, such as aerospace, robotics, and industrial control .



### POSIX Issues

- POSIX stands for Portable Operating System Interface, which is a set of standards that define how an application should interact with an operating system.
- POSIX aims to achieve portability, interoperability, and compatibility among different operating systems, especially for applications that require long-term maintenance and support.
- POSIX covers various aspects of operating system services, such as file operations, process management, signals, devices, threads, and real-time extensions.
- POSIX real-time extensions are defined in the POSIX.1b and POSIX.1j standards, which specify the requirements and interfaces for real-time operating systems .
- POSIX real-time extensions include features such as:
  - Priority-based preemptive scheduling
  - Real-time signals and timers
  - Semaphores and message queues
  - Memory locking and shared memory
  - Asynchronous and synchronous I/O
  - Clocks and timers
  - Sporadic server scheduling
  - Trace and performance analysis
- POSIX real-time extensions aim to provide a common and consistent way for real-time applications to access the operating system services that are needed for deterministic and predictable behavior.
- POSIX real-time extensions also aim to enhance the performance, reliability, and scalability of real-time systems by reducing the overhead and latency of system calls and context switches.
- However, POSIX real-time extensions also face some challenges and limitations, such as:
  - The lack of a widely accepted conformance testing suite and certification process for POSIX-compliant operating systems.
  - The difficulty of achieving real-time performance guarantees on general-purpose operating systems that are not designed for real-time applications.
  - The trade-off between portability and performance, as some operating system features may not be supported or optimized by all POSIX-compliant platforms.
  - The complexity and diversity of real-time applications and requirements, which may not be fully addressed by the POSIX standards.
  - The evolution and innovation of operating system technologies and architectures, which may introduce new challenges and opportunities for real-time systems.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some points on the characteristics of temporal data for your notes:

- Temporal data is the data that represents time in some form, and allows other data to be placed in a chronological sequence, or to be analyzed chronologically.
- Temporal data can be of different types, such as event time, valid time, transaction time, or decision time.
- Event time is the time when an event occurs in the real world, such as a birth, a death, or a purchase.
- Valid time is the time period during which a fact is true in the real world, such as the current temperature, the current address, or the current status .
- Transaction time is the time period during which a fact is stored in the database, such as the insertion time, the update time, or the deletion time.
- Decision time is the time when a decision is made based on the available data, such as the approval time, the rejection time, or the revision time.
- Temporal data can be used to analyze trends, patterns, changes, and causality over time.
- Temporal data can also be used to ensure consistency, accuracy, and validity of the data.
- Temporal data can be stored and managed using temporal databases, which are databases that support temporal data types, operations, and queries.
- Temporal databases can be uni-temporal, bi-temporal, or tri-temporal, depending on the number of temporal aspects they capture.
- Uni-temporal databases capture only one temporal aspect, such as valid time or transaction time.
- Bi-temporal databases capture two temporal aspects, such as valid time and transaction time, or valid time and decision time.
- Tri-temporal databases capture three temporal aspects, such as valid time, transaction time, and decision time.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not reflect the current state of the physical environment. This can happen due to the delay in sensing, processing, and updating the data.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other. This can happen due to the concurrency and interference of multiple transactions that access and update the data.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the occurrence of some events or conditions in the physical environment or the database. Triggered updates can reduce data staleness by updating the data as soon as possible.
  - Absolute validity, which is a temporal constraint that specifies the maximum allowable age of the data that can be read by a transaction. Absolute validity can prevent transactions from reading stale data by checking the timestamp of the data.
  - Relative validity, which is a temporal constraint that specifies the maximum allowable difference between the values of two data items that are related by some functional dependency. Relative validity can prevent transactions from reading inconsistent data by checking the difference between the values of the data items.
  - Serialization, which is a concurrency control technique that ensures that the execution of multiple transactions is equivalent to some sequential order of the transactions. Serialization can prevent data inconsistency by avoiding the interference and conflicts of the transactions.
  - Priority assignment, which is a scheduling technique that assigns different priorities to different transactions based on their deadlines, criticality, and data freshness requirements. Priority assignment can improve the temporal consistency by giving higher priority to the transactions that need more up-to-date data.



### Concurrency Control

- Concurrency control is a database management systems (DBMS) concept that is used to address occur with a multi-user system.
- Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity.
- A transaction is a logical unit of work that accesses or modifies one or more data items in a database.
- A transaction is said to be successfully completed if and only if, it satisfies the ACID properties, namely, atomicity, consistency, isolation, and durability.
- A concurrent execution of a set of transactions is said to be serializable if and only if the database operations carried out by them is equivalent to some serial execution of these transactions.
- Serializability is a desirable property for concurrency control, as it ensures the correctness and consistency of the database state.

### Concurrency Control in Real-Time Database Systems

- A real-time database system (RTDBS) is a database system that supports applications with timing constraints, such as deadline, urgency, and freshness.
- A real-time transaction is a transaction that has a deadline by which it must be completed, otherwise it may cause undesirable consequences.
- A real-time transaction may also have a value function that indicates its importance or utility over time.
- Concurrency control in RTDBS is more challenging than in conventional DBMS, as it has to consider not only the correctness and consistency of the database state, but also the timeliness and freshness of the data and transactions.
- Concurrency control in RTDBS has to balance the trade-off between concurrency and serialization, as well as the trade-off between data consistency and data currency.
- Concurrency control in RTDBS has to cope with the dynamic and unpredictable nature of real-time workloads, as well as the resource limitations and failures of real-time systems.

### Concurrency Control Techniques for RTDBS

- There are various concurrency control techniques that have been proposed for RTDBS, such as locking-based, timestamp-based, optimistic, and hybrid techniques.
- Locking-based techniques use locks to prevent conflicting accesses to data items by concurrent transactions. They can be classified into two-phase locking (2PL), priority-based locking (PBL), and real-time locking (RTL) techniques.
- Timestamp-based techniques assign timestamps to transactions and data items, and use them to order and validate the accesses. They can be classified into basic timestamp ordering (BTO), optimistic concurrency control (OCC), and multiversion concurrency control (MVCC) techniques.
- Optimistic techniques assume that conflicts are rare, and allow transactions to execute without any synchronization until the validation phase, where they check for conflicts and abort or restart the conflicting transactions. They can be classified into wait-free, restart-free, and restart-based techniques.
- Hybrid techniques combine the advantages of different techniques, such as locking and timestamping, or optimistic and pessimistic, to achieve better performance and flexibility. They can be classified into lock-based optimistic concurrency control (LOCC), optimistic two-phase locking (O2PL), and multiversion two-phase locking (MV2PL) techniques.

### Concurrency Control Issues and Challenges for RTDBS

- Some of the issues and challenges that concurrency control techniques for RTDBS have to address are:
  - How to handle the priority inversion problem, where a high-priority transaction is blocked by a low-priority transaction that holds a lock on a data item.
  - How to handle the blocking and starvation problems, where a transaction is delayed or aborted due to the unavailability of a data item or a resource.
  - How to handle the data freshness problem, where a transaction reads or writes a data item that is outdated or stale.
  - How to handle the deadline miss problem, where a transaction fails to complete within its deadline.
  - How to handle the data consistency problem, where a transaction violates the integrity constraints or the serializability property of the database.
  - How to handle the data currency problem, where a transaction uses a data item that is not the most recent or the most relevant version.
  - How to handle the data replication problem, where a transaction accesses or updates a data item that is replicated on multiple sites or nodes.
  - How to handle the data



### Overview of Commercial Real Time databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service.
- Some of the attributes of live real-time databases are:
  - Concurrency control: the ability to handle multiple transactions accessing the same data without compromising the consistency and integrity of the database.
  - Data freshness: the degree to which the data reflects the current state of the real world.
  - Data distribution: the ability to store and access data across multiple nodes or locations, which may improve availability, scalability, and fault tolerance.
  - Data replication: the process of creating and maintaining copies of data on different nodes or locations, which may improve availability, scalability, and fault tolerance.
  - Data partitioning: the process of dividing data into smaller subsets based on some criteria, such as key range, hash function, or geographic location, which may improve performance and scalability.
  - Data compression: the process of reducing the size of data by removing redundancy or using encoding techniques, which may improve storage efficiency and network bandwidth.
  - Data encryption: the process of transforming data into an unreadable form using a secret key, which may improve security and privacy.
  - Data backup: the process of creating and storing copies of data for recovery purposes, which may improve reliability and durability.
  - Data indexing: the process of creating and maintaining data structures that facilitate fast and efficient data retrieval, which may improve performance and usability.
- Some of the examples of commercial real-time databases are:
  - Google Cloud Firestore: a highly scalable, fully managed NoSQL database service for large analytical and operational workloads, offering up to 99.999% availability and processing more than 5 billion requests per second at peak.
  - Google Cloud Bigtable: a highly performant, fully managed NoSQL database service for large analytical and operational workloads, offering up to 99.999% availability and processing more than 10 Exabytes of data under management.
  - Google Cloud Spanner: a fully managed relational database service that combines the scalability and availability of NoSQL databases with the consistency and transactional capabilities of SQL databases, offering up to 99.999% availability and supporting up to 15 regions and 1000 nodes per instance.
  - Google Cloud SQL: a fully managed relational database service that supports MySQL, PostgreSQL, and SQL Server, offering up to 99.95% availability and supporting up to 416 GB of RAM and 64 TB of storage per instance.

