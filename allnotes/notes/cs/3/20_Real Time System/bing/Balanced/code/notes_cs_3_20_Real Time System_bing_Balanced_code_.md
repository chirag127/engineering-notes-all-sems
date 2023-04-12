

## Unit 1 - Introduction of Real Time System

A real time system is a system that can process data and events within a specified time constraint. The system must produce the expected result within a defined deadline, otherwise it may cause a system failure or undesirable consequences. A real time system may also need to coordinate with other systems or devices that operate with different clocks and synchronize their actions.

Some examples of real time systems are:

- Flight control systems
- Industrial automation systems
- Medical devices
- Multimedia systems
- Online gaming systems
- Robotics

Real time systems can be classified into two types based on their timing constraints:

- Hard real time systems: These systems have absolute deadlines that must be met, otherwise the system may fail or cause severe damage. For example, a flight control system must respond to the pilot's commands within milliseconds, otherwise the plane may crash.
- Soft real time systems: These systems have relative deadlines that can be missed occasionally, but the system performance may degrade or the quality of service may be reduced. For example, a video streaming system may drop some frames or reduce the resolution if the network bandwidth is low, but the user can still watch the video.

Real time systems require a special type of operating system that can handle the timing requirements and the concurrency issues of the system. A real time operating system (RTOS) is an operating system that can provide predictable and deterministic response times to the system events and tasks. An RTOS typically has the following features:

- Preemptive scheduling: The RTOS can interrupt a running task and switch to a higher priority task when an event occurs, without waiting for the current task to finish.
- Priority-based scheduling: The RTOS can assign different priorities to different tasks and execute them according to their importance and urgency.
- Inter-task communication and synchronization: The RTOS can provide mechanisms for the tasks to communicate and synchronize with each other, such as message queues, semaphores, mutexes, etc.
- Memory management: The RTOS can allocate and deallocate memory for the tasks and avoid memory fragmentation and leakage.
- Device drivers: The RTOS can provide interfaces for the system to interact with the hardware devices, such as sensors, actuators, network cards, etc.

Some examples of RTOS are:

- FreeRTOS
- VxWorks
- QNX
- RTLinux
- Windows CE



### Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a nuclear reactor control system, a flight control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic and aperiodic.
- A periodic system is a system that has events or inputs that occur at regular intervals, and the deadlines are known in advance. For example, a sensor that samples data every 10 milliseconds, or a task that executes every 5 seconds.
- An aperiodic system is a system that has events or inputs that occur at irregular intervals, and the deadlines are not known in advance. For example, a user request, a network packet, or an interrupt.
- A real time system can also be classified into two types based on the complexity of the system: single processor and multiprocessor.
- A single processor system is a system that has only one processor or CPU that executes all the tasks or processes. For example, a microcontroller, a smartphone, or a laptop.
- A multiprocessor system is a system that has more than one processor or CPU that can execute tasks or processes in parallel. For example, a supercomputer, a server, or a cluster.



# Typical Real Time Applications

- A real-time application (RTA) is an application that requires a program to respond to stimuli within a specific and predictable time frame. 
- Real-time applications are often used for tasks that involve critical operations, such as digital control, signal processing, command and control, tracking, and multimedia.   
- Some examples of real-time applications are:

  - Video conferencing: This application allows users to communicate with each other through audio and video streams over the internet. It requires low latency and high bandwidth to ensure smooth and synchronized communication. 
  - Voice over Internet Protocol (VoIP): This application enables users to make phone calls over the internet using digital signals. It requires real-time processing and transmission of voice data to ensure clear and uninterrupted conversation. 
  - Online gaming: This application allows users to play games with other players over the internet. It requires fast and accurate response from the game server and the game client to ensure fair and realistic gameplay. 
  - Community storage applications: These applications allow users to store and access data on a distributed network of storage devices. They require real-time coordination and synchronization of data access and replication to ensure data consistency and availability. 
  - Some e-commerce applications: These applications allow users to buy and sell goods and services online. They require real-time processing and verification of transactions and payments to ensure security and efficiency. 
  - Real-time operating system (RTOS): This is a type of operating system that supports the execution of real-time applications. It provides features such as preemptive scheduling, priority-based dispatching, inter-process communication, and real-time synchronization to ensure timely and predictable behavior of the system.  
  - Instant messaging (IM) applications: These applications allow users to send and receive text, audio, and video messages over the internet. They require real-time delivery and notification of messages to ensure effective and convenient communication. 
  - Team collaboration applications: These applications allow users to work together on a common project or task over the internet. They require real-time sharing and updating of information and resources to ensure productivity and quality.



### Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events within a specified time interval.
- A real time system can be classified as hard, soft, or firm, depending on the consequences of missing a deadline.
- A hard real time system is one where missing a deadline can cause catastrophic failure or unacceptable loss. For example, a nuclear reactor control system or a pacemaker.
- A soft real time system is one where missing a deadline can degrade the performance or quality of service, but not cause failure. For example, a video streaming service or a voice recognition system.
- A firm real time system is one where missing a deadline can result in some loss, but not failure. For example, a stock trading system or a multimedia application.
- The notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System will be released on the following dates:
  - Lecture 1: Introduction and Overview of Real Time Systems - March 20, 2023
  - Lecture 2: Real Time System Characteristics and Requirements - March 22, 2023
  - Lecture 3: Real Time System Design and Analysis - March 24, 2023
  - Lecture 4: Real Time Scheduling Algorithms - March 27, 2023
  - Lecture 5: Real Time Operating Systems and Middleware - March 29, 2023
  - Lecture 6: Real Time Communication and Synchronization - March 31, 2023
  - Lecture 7: Real Time Fault Tolerance and Testing - April 3, 2023
  - Lecture 8: Real Time System Applications and Case Studies - April 5, 2023
- The notes will be available on the course website and the learning management system. The notes will be in PDF format and will contain the slides, examples, exercises, and references for each lecture.
- The notes are intended to supplement the lectures and the textbook, not to replace them. The students are expected to attend the lectures, read the textbook, and do the exercises to fully understand the concepts and techniques of real time systems.
- The notes are subject to change and update based on the feedback and progress of the course. The students are advised to check the course website and the learning management system regularly for any updates or announcements.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- The notes of the Unit 1 - Introduction of Real Time System are to be submitted by **Friday, 24 March 2023** before **5:00 PM**.
- The notes should cover the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Real time system design issues and challenges
  - Real time scheduling algorithms and analysis
  - Real time operating systems and middleware
- The notes should be written in a clear, concise and accurate manner, using proper terminology and notation.
- The notes should be formatted according to the guidelines given by the instructor, including font size, margins, headings, subheadings, bullet points, diagrams, tables, references, etc.
- The notes should be submitted in a PDF file, with the file name as **RTS_Unit1_Notes_YourName.pdf**.
- The notes should be uploaded to the online platform specified by the instructor, before the deadline.
- Late submissions will not be accepted and will result in a zero grade for the assignment.
- Plagiarism will not be tolerated and will result in a severe penalty, as per the academic integrity policy of the institution.
- If you have any questions or doubts regarding the notes, you can contact the instructor via email or during the office hours.



### Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real-time system is a system that must produce the correct results within a specific time frame, otherwise it may fail or cause undesirable consequences .
- Timing constraints are the requirements that specify the deadlines or the acceptable ranges of response times for the real-time system  .
- Timing constraints are essential for ensuring the timeliness and the correctness of the real-time system, as well as for designing, testing, and verifying the system .
- Timing constraints can be classified into two categories: performance constraints and behavioral constraints.
  - Performance constraints are the constraints that define the desired or acceptable response times of the system or its components .
    - For example, a performance constraint may specify that the system must respond to an event within 10 milliseconds, or that the average response time of the system must be less than 5 milliseconds.
  - Behavioral constraints are the constraints that define the temporal relationships or dependencies among the events, tasks, or data of the system.
    - For example, a behavioral constraint may specify that a task must start after another task finishes, or that a data item must be updated every second.
- Timing constraints can also be classified into two types: hard and soft.
  - Hard timing constraints are the constraints that must be met by the system at all times, otherwise the system may fail or cause catastrophic consequences.
    - For example, a hard timing constraint may specify that a safety-critical system must stop a nuclear reactor before it overheats.
  - Soft timing constraints are the constraints that can be occasionally violated by the system without causing failure or severe consequences, but may degrade the performance or the quality of the system.
    - For example, a soft timing constraint may specify that a multimedia system must play a video without noticeable delays or glitches.
- Timing constraints can be expressed using various constructs, such as constants, variables, operators, functions, predicates, or temporal logic.
  - For example, a timing constraint may be expressed as `T1 + T2 <= 100`, where `T1` and `T2` are the response times of two tasks, and `100` is the deadline.
  - Another example of a timing constraint may be expressed as `always(event1 -> eventually(event2))`, where `event1` and `event2` are two events, and `->` and `eventually` are temporal logic operators that mean "implies" and "sometime in the future", respectively. This constraint means that whenever `event1` occurs, `event2` must occur at some point after it.



### Hard Real Time Systems

- A hard real-time system is a system that must produce the expected result within a defined deadline, otherwise it will cause a system failure or a catastrophic consequence  .
- A hard real-time system has absolute deadlines, meaning that missing even a single deadline is unacceptable and intolerable .
- A hard real-time system is usually interacting at a low level with physical hardware, such as sensors, actuators, or embedded systems.
- Examples of hard real-time systems are flight control systems, nuclear power plant control systems, pacemakers, airbag systems, etc .
- A hard real-time system requires a real-time operating system (RTOS) that can provide deterministic scheduling, preemptive multitasking, priority-based interrupt handling, and time synchronization .
- A hard real-time system must be designed with careful analysis of the worst-case execution time (WCET) of each task, the deadline of each task, the priority of each task, and the possible interference of each task.
- A hard real-time system must be tested and verified rigorously to ensure its correctness, reliability, and safety.



### Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing a failure or a significant degradation of performance  .
- A soft real-time system has a small window of time for program completion rather than a precise moment due to a bit of jitter from the operating system.
- A soft real-time system can be run on multiple cores and impose fewer restrictions on applications.
- A soft real-time system is typically used to solve issues of concurrent access and the need to keep a number of connected systems up-to-date through changing situations.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video applications.
  - Online gaming and virtual reality systems.
  - Multimedia systems and interactive user interfaces.
- A soft real-time system is different from a hard real-time system, which is a system that must execute its tasks within a strict deadline, otherwise it will result in a catastrophic failure or unacceptable consequences .
- Some examples of hard real-time systems are:
  - Air traffic control systems.
  - Nuclear power plant control systems.
  - Medical devices and life support systems.
  - Automotive and avionics systems.
- A soft real-time system is also different from a firm real-time system, which is a system that can tolerate some missed deadlines, but the usefulness of the results decreases rapidly after the deadline.
- Some examples of firm real-time systems are:
  - Online reservation systems.
  - Stock market trading systems.
  - E-commerce and banking systems.
  - Sensor networks and data acquisition systems.



### Reference Models for Real Time Systems

A reference model is a conceptual framework that defines the essential features and components of a real time system, and how they interact with each other. A reference model helps to understand, analyze, design, and evaluate real time systems, using consistent terminology and abstraction levels. A reference model is not a specific system design or implementation, but a generic form that can be instantiated for different applications and domains.

There are different reference models for real time systems, depending on the focus and scope of the model. Some of the common reference models are:

- **Real-time Control System (RCS)**: This is a reference model architecture for software-intensive, real-time computing control problems, such as robotics, manufacturing, and aerospace. It combines real-time motion planning and control with high level task planning, problem solving, world modeling, recursive state estimation, tactile and visual image processing, and acoustic signature analysis . The RCS model consists of a hierarchical structure of nodes, each of which performs a specific function and communicates with other nodes through a blackboard. The nodes are organized into three layers: sensory processing, state estimation, and behavior generation. The RCS model supports both reactive and deliberative control, as well as learning and adaptation.

- **Reference Model of Real-time Systems (RMRTS)**: This is a reference model that focuses on the timing behavior and schedulability of real time systems  . It is characterized by three elements: a workload model, a resource model, and a system model. The workload model specifies the application supported by the system, in terms of tasks, jobs, deadlines, resource dependencies, and precedence constraints. The resource model describes the resources available in the system, such as CPU, memory, network, and their types and relations. The system model defines the system policies and mechanisms for managing the resources and the workload, such as scheduling algorithms, synchronization protocols, and fault tolerance techniques. The RMRTS model allows to analyze the feasibility and performance of real time systems, and to compare different system designs and implementations.

- **Model of a Real-time System (MRTS)**: This is a reference model that focuses on the structural and behavioral aspects of real time systems, such as components, interfaces, communication, and coordination. It comprises of the following parts: a workload model, a resource model, a component model, a communication model, and a coordination model. The workload model and the resource model are similar to the RMRTS model, but with more details and variations. The component model describes the software and hardware components that constitute the system, and their properties and functions. The communication model defines the communication channels and protocols among the components, and the data types and formats. The coordination model specifies the rules and patterns for coordinating the components, such as event triggers, message passing, and shared variables. The MRTS model supports the design and implementation of real time systems, and the verification and validation of their properties and behavior.



### Processors and Resources

- Processors and resources are two major types of system components that are involved in the execution of real-time tasks.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Example: computer, transmission link, disk, database server.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. A resource can be preemptable or non-preemptable. Example: printer, file, semaphore, lock.
- A real-time system must manage the allocation and scheduling of processors and resources to meet the timing constraints of the tasks. A real-time operating system (RTOS) is an operating system that serves real-time applications that process data without any buffering delay .
- A real-time system can have different types of processors and resources, such as single processor, multiprocessor, distributed, homogeneous, heterogeneous, dedicated, shared, etc. The type of processor and resource affects the design and analysis of the real-time system.
- A real-time system can also use different techniques to optimize the performance and utilization of processors and resources, such as workload-aware processor tuning, time synchronization, communication protocols, etc .



### Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are :
  - Release time (r<sub>i</sub>): The time instant when the job becomes available for execution.
  - Absolute deadline (d<sub>i</sub>): The time instant by which the job must finish its execution.
  - Relative deadline (D<sub>i</sub>): The maximum allowed time between the release time and the absolute deadline of the job. D<sub>i</sub> = d<sub>i</sub> - r<sub>i</sub>.
  - Feasible interval ([r<sub>i</sub>, d<sub>i</sub>]): The time interval in which the job can be executed.
- The temporal parameters of a job may be fixed, variable, or unknown, depending on the nature of the real time system and the workload .
- The temporal parameters of a job may be specified by the application, the system, or the user .
- The temporal parameters of a job may be expressed in absolute or relative terms, depending on the reference point of the time measurement .
- The temporal parameters of a job may be hard or soft, depending on the consequences of missing the deadline .
- The temporal parameters of a job may be periodic or aperiodic, depending on the regularity of the job arrival pattern .
- The temporal parameters of a job may be independent or dependent, depending on the existence of precedence or synchronization constraints among jobs .



### Periodic Task Model

- The periodic task model is a well-known deterministic workload model that characterizes accurately many traditional hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .
- A periodic task is one that repeats itself after a fixed time interval, called the period.
- A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di > Where, Φi – is the phase of the task, Pi – is the period of the task, ei – is the worst-case execution time of the task, and Di – is the relative deadline of the task.
- The phase of a task is the time difference between the start of the first job and the start of the hyperperiod. The hyperperiod is the least common multiple of the periods of all the tasks in the system.
- The relative deadline of a task is the maximum allowable time between the release of a job and its completion. The absolute deadline of a job is the sum of its release time and its relative deadline.
- A periodic task is said to be feasible if there exists a schedule that can meet all the deadlines of the task. A set of periodic tasks is said to be feasible if there exists a schedule that can meet all the deadlines of all the tasks in the set.
- The utilization of a periodic task is defined as the ratio of its execution time to its period. The utilization of a set of periodic tasks is defined as the sum of the utilizations of all the tasks in the set.
- The periodic task model can be extended by adding a jitter Ji for each task τi, to allow the flexibility that the actual release time of a job may be at most Ji time units earlier or later than the exact start time of the period.
- The periodic task model can also be extended by adding a deadline monotonic priority Pi for each task τi, to specify the relative importance of the task. A higher priority means a higher importance.
- The periodic task model can be used to analyze the schedulability of real-time systems using various scheduling algorithms, such as rate monotonic, earliest deadline first, and fixed priority.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on precedence constraints and data dependency in real time systems:

### Precedence Constraints and Data Dependency

- Precedence constraints are the restrictions on the order of execution of jobs in a real time system. They are usually represented by a directed graph, where the vertices are the jobs and the edges are the constraints. A job can only start execution after all its predecessors have completed execution  .
- Data dependency is the situation where the output of one job is used as the input of another job in a real time system. Data dependency can affect the schedulability and correctness of the system, as it may introduce delays or inconsistencies in the data flow .
- Precedence constraints and data dependency are related concepts, as they both impose constraints on the execution order of jobs. However, they are not equivalent, as precedence constraints are explicit and static, while data dependency is implicit and dynamic .
- Some examples of real time systems that have precedence constraints and data dependency are:
  - A robotic arm that has to perform a sequence of movements and use sensor data to adjust its position and orientation.
  - A multimedia system that has to process audio and video streams and synchronize them for playback.
  - A flight control system that has to execute different tasks based on the mode of operation and the sensor data.



# Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling involves breaking a program into multiple threads or processes that can run concurrently and independently on a processor or a multiprocessor system .
- Real time scheduling aims to reduce the response time and meet the deadlines of each task, while maximizing the system utilization and throughput .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or before the system starts running. It is based on the known characteristics of the tasks, such as their arrival time, execution time, deadline, and priority. Static scheduling is suitable for periodic and deterministic tasks that have fixed and predictable behavior .
  - Dynamic scheduling is done at run time or when the system is running. It is based on the current state of the system, such as the availability of resources, the arrival of new tasks, the completion of existing tasks, and the occurrence of events. Dynamic scheduling is suitable for aperiodic and stochastic tasks that have variable and unpredictable behavior .
- Real time scheduling algorithms can be classified into two categories: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running on the processor. The lower priority task resumes its execution when the higher priority task finishes or is blocked. Preemptive scheduling can reduce the response time and improve the schedulability of tasks, but it can also incur more overhead and complexity .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running on the processor. The lower priority task completes its execution before the higher priority task can start. Non-preemptive scheduling can reduce the overhead and complexity, but it can also increase the response time and degrade the schedulability of tasks .
- Some examples of real time scheduling algorithms are:
  - Rate monotonic scheduling (RMS): a static and preemptive algorithm that assigns priorities to tasks based on their periods, such that the shorter the period, the higher the priority .
  - Earliest deadline first scheduling (EDF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their deadlines, such that the earlier the deadline, the higher the priority .
  - Least laxity first scheduling (LLF): a dynamic and preemptive algorithm that assigns priorities to tasks based on their laxity, which is the difference between their deadline and their remaining execution time, such that the smaller the laxity, the higher the priority .
  - Round robin scheduling (RR): a dynamic and preemptive algorithm that assigns equal priorities to tasks and allocates them a fixed amount of time (quantum) to run on the processor. The tasks are arranged in a circular queue and the processor switches to the next task in the queue after each quantum .
  - First come first served scheduling (FCFS): a dynamic and non-preemptive algorithm that assigns priorities to tasks based on their arrival time, such that the earlier the arrival, the higher the priority .
  - Priority scheduling: a dynamic and non-preemptive algorithm that assigns priorities to tasks based on some criteria, such as their importance, urgency, or resource requirements, such that the higher the priority, the earlier the execution .
- Real time scheduling can be applied to various domains and applications, such as embedded systems, robotics, multimedia, industrial control, aerospace, and health care .
- Real time scheduling can also be supported by various tools and platforms, such as real time operating systems (RTOS), real time schedulers, real time kernels, and real time middleware .
- Real time scheduling can be evaluated and verified by various methods and metrics, such as schedulability analysis, simulation, testing, and performance measurement .
- Real time scheduling can be enhanced and optimized by various techniques and strategies, such as task partitioning



### Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution priorities and time slots to tasks or processes that have timing constraints. Real time systems are those whose correctness depends on both functionality and timing. There are different approaches to real time scheduling, depending on the characteristics and requirements of the system and the tasks. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, period, etc., are known at design time. In this approach, a static schedule is computed offline, based on the worst-case execution times of the tasks and their timing constraints. The schedule is stored in a table, which is consulted by a timer at specific time instants to determine which task should be executed next. The advantage of this approach is that it guarantees the schedulability of the tasks and avoids runtime overhead. The disadvantage is that it is inflexible and cannot handle dynamic changes or uncertainties in the system or the tasks.    

- **Priority-driven approach**: This approach is also known as event-driven or dynamic approach. It is mainly used for soft or firm real time systems, where some of the properties of the tasks, such as arrival time, execution time, deadline, etc., are not known at design time or may vary at runtime. In this approach, each task is assigned a priority, which may be static or dynamic, and the scheduler selects the highest priority task that is ready to run at each scheduling point. The advantage of this approach is that it is flexible and can handle dynamic changes or uncertainties in the system or the tasks. The disadvantage is that it may incur more runtime overhead and may not guarantee the schedulability of the tasks.    

- **Round-robin approach**: This approach is a special case of priority-driven approach, where all the tasks have the same priority and are scheduled in a circular order based on a fixed time slice allocated to each task. This approach is commonly used in time-shared systems, where the goal is to provide fair and responsive service to multiple users or applications. The advantage of this approach is that it is simple and easy to implement. The disadvantage is that it may not meet the timing constraints of the tasks and may cause frequent context switches.  

- **Weighted round-robin approach**: This approach is a variation of round-robin approach, where the tasks have different weights and are scheduled in a circular order based on a variable time slice allocated to each task proportional to its weight. This approach is used to provide differentiated service to multiple users or applications, where some tasks may have higher importance or demand than others. The advantage of this approach is that it can balance the fairness and performance of the system. The disadvantage is that it may not meet the timing constraints of the tasks and may cause frequent context switches.  

- **Earliest deadline first (EDF) approach**: This approach is a dynamic priority-driven approach, where the priority of each task is inversely proportional to its absolute deadline, i.e., the task with the earliest deadline has the highest priority. This approach is optimal for preemptive scheduling of periodic or sporadic tasks on a single processor, i.e., it can schedule any set of tasks that is feasible, i.e., whose total utilization does not exceed 100%. The advantage of this approach is that it can maximize the resource utilization and minimize the deadline misses. The disadvantage is that it may cause priority inversion and may not be feasible for multiprocessor or distributed systems.  

- **Least slack time (LST) approach**: This approach is a dynamic priority-driven approach, where the priority of each task is inversely proportional to its slack time, i.e., the difference between its deadline and its remaining execution time. This approach is optimal for preemptive scheduling of aperiodic tasks on a single processor, i.e., it can schedule any set of tasks that is feasible, i.e., whose total demand does not exceed the available time. The advantage of this approach is that it can minimize the tardiness and maximize the throughput of the system. The disadvantage is that it may cause priority inversion and may not be feasible for multiprocessor or distributed systems.  

-



### Clock Driven Approach

- Clock-driven scheduling is also called as time-driven scheduling.
- When scheduling is clock-driven, decisions are made at specific time instants on what jobs should execute when.
- Typically in clock-driven scheduling system, all the parameters of hard real-time jobs are fixed and known.
- A clock-driven scheduler computes a schedule offline, before the system starts to execute, and stores it in a table.
- The schedule is repeated periodically, and each period is called a major cycle.
- The major cycle is the least common multiple of the periods of all the tasks.
- The scheduler uses a clock to determine when to switch tasks according to the schedule table.
- The clock-driven approach is suitable for real-time systems that require predictable and deterministic behaviour.
- The advantages of clock-driven scheduling are :
  - It is easy to verify the schedulability of the system.
  - It avoids the overhead of dynamic scheduling decisions and priority inversion.
  - It can handle aperiodic and sporadic tasks by reserving slots for them in the schedule table.
  - It can exploit the slack time of the tasks to reduce the power consumption of the system.
- The disadvantages of clock-driven scheduling are :
  - It is not flexible to handle dynamic changes in the system, such as task arrivals, deadlines, or resource availability.
  - It may waste processor time if some tasks do not execute or finish early.
  - It requires accurate knowledge of the task parameters and the clock frequency.
  - It may not be scalable for large and complex systems with many tasks and resources.



### Weighted Round Robin Approach

- The weighted round robin approach is a generalization of the round robin approach for scheduling real-time tasks or traffic.
- In the round robin approach, each ready task is given an equal share of the processor for a fixed time quantum, and the tasks are served in a circular order.
- In the weighted round robin approach, each ready task is given a fixed number of time quanta according to its weight, which represents its priority or importance .
- The tasks are still served in a circular order, but the number of service opportunities for each task is proportional to its weight .
- The weighted round robin approach can be used for scheduling real-time traffic in high-speed switched networks, where different types of traffic may have different quality of service requirements .
- The advantages of the weighted round robin approach are that it is simple, fair, and easy to implement.
- The disadvantages of the weighted round robin approach are that it may not meet the deadlines of some tasks, it may cause high overhead due to frequent context switches, and it may not utilize the processor efficiently.



### Priority Driven Approach

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



### Dynamic Versus Static Systems

- A **static system** is one where the tasks and their attributes (such as arrival time, execution time, deadline, priority, etc.) are known in advance and do not change during the system execution. A static system can be scheduled offline using a fixed priority or a fixed order of execution. A static system provides the advantage of being predictable and verifiable, but it may not be able to handle unexpected events or changes in the workload. Static systems are suitable for hard real-time systems that require strict guarantees on the timing behavior of the tasks .
- A **dynamic system** is one where the tasks and their attributes may vary or be unknown until the system execution. A dynamic system requires online scheduling using a variable priority or a variable order of execution. A dynamic system provides the advantage of being adaptable and responsive, but it may not be able to guarantee the timing behavior of the tasks. Dynamic systems are suitable for soft real-time systems that can tolerate some degree of uncertainty or variability in the workload .
- The choice between static and dynamic systems depends on the characteristics and requirements of the real-time application. Static systems are preferred when the tasks are deterministic, periodic, independent, and have fixed deadlines. Dynamic systems are preferred when the tasks are stochastic, aperiodic, interdependent, and have variable deadlines .



### Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two algorithms for scheduling preemptive jobs on one processor in real time systems.
- EDF assigns the highest priority to the job with the earliest absolute deadline, and preempts the current job if a higher priority job arrives.
- LST assigns the highest priority to the job with the least slack (or laxity), which is the difference between the deadline and the remaining execution time, and preempts the current job if a higher priority job arrives.
- Both EDF and LST are optimal for scheduling independent jobs, meaning that if there exists a feasible schedule that meets all the deadlines, then EDF and LST will also produce a feasible schedule that meets all the deadlines .
- EDF and LST are also optimal for scheduling jobs with precedence constraints, meaning that some jobs depend on the completion of other jobs, as long as the precedence graph is a forest (a collection of trees) and the jobs have implicit deadlines (equal to their periods) .
- EDF and LST have different advantages and disadvantages in terms of performance and implementation.
  - EDF is easier to implement than LST, as it only requires sorting the jobs by their deadlines, while LST requires calculating the slack of each job at every scheduling point.
  - EDF has better average response time than LST, as it tends to finish the jobs earlier than their deadlines, while LST may delay some jobs until close to their deadlines.
  - LST has better worst-case response time than EDF, as it minimizes the maximum tardiness (the amount of time a job misses its deadline) of any job, while EDF may have large tardiness for some jobs if the system is overloaded.
  - LST is more robust than EDF to variations in execution times and arrival times, as it adapts to the changing slack of the jobs, while EDF may fail to meet some deadlines if the jobs take longer or arrive earlier than expected  .



### Rate Monotonic Algorithm for the notes of the Unit 2 - Real Time Scheduling in the subject of Real Time System

- Rate Monotonic Algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class   .
- The static priorities are assigned according to the cycle duration of the task, so that a shorter cycle duration results in a higher task priority   .
- RMA is preemptive in nature, meaning that a higher priority task can interrupt a lower priority task at any time .
- RMA is optimal for periodic tasks, meaning that it can schedule any set of periodic tasks that is feasible, i.e., that can be scheduled by any other algorithm  .
- RMA has a simple schedulability test, which is based on the utilization factor of the task set, defined as the sum of the ratios of execution time to period for each task  .
- The schedulability test states that a task set is schedulable by RMA if its utilization factor is less than or equal to n(2^(1/n) - 1), where n is the number of tasks  .
- RMA has some advantages, such as easy implementation, low overhead, and guaranteed performance for feasible task sets .
- RMA also has some disadvantages, such as poor resource utilization, inability to handle aperiodic or sporadic tasks, and priority inversion problem .



### Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, processor time as well as resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler makes each scheduling decision without knowledge about the tasks that will be released in future and parameter of each task is known to the scheduler only after release of the task.
- Offline scheduling has the advantage of being optimal and predictable, but it requires complete and accurate information about the tasks and it cannot handle dynamic changes in the system.
- Online scheduling has the advantage of being flexible and adaptive, but it requires efficient and effective algorithms to make scheduling decisions in real time and it may not guarantee the optimal solution.
- Examples of offline scheduling are table-driven scheduling and cyclic executive scheduling, where a fixed sequence of tasks is executed periodically .
- Examples of online scheduling are priority-driven scheduling and earliest deadline first scheduling, where the scheduler assigns priorities to the tasks based on their deadlines or other criteria and selects the highest priority task to execute at each instant .



### Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user inputs, network packets, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time constraint, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are interrupts, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, criticality, etc. The scheduler always selects the job with the highest priority to execute at any time. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign fixed time slots to jobs based on their arrival patterns and execution times. The scheduler follows a pre-computed schedule that specifies which job to execute at each time slot. Examples are cyclic executive, time triggered, etc.

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven and clock driven systems is to balance the responsiveness of aperiodic and sporadic jobs and the schedulability of periodic jobs. Periodic jobs are jobs that have fixed arrival patterns and hard deadlines. They are the primary workload of real-time systems and must be guaranteed to meet their deadlines.
- In priority driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: background scheduling and slack stealing.
  - Background scheduling is a simple and efficient approach that assigns the lowest priority to aperiodic and sporadic jobs. This means that they can only execute when there is no periodic job ready to execute. This ensures that periodic jobs always meet their deadlines, but it may result in long response times or missed deadlines for aperiodic and sporadic jobs.
  - Slack stealing is a more sophisticated and dynamic approach that assigns higher priorities to aperiodic and sporadic jobs when there is enough slack time in the system. Slack time is the amount of time that a periodic or sporadic job can be delayed without affecting its deadline. The scheduler monitors the slack time of each job and steals it to execute aperiodic and sporadic jobs as soon as possible. This improves the responsiveness of aperiodic and sporadic jobs, but it requires more computation and overhead to track the slack time and adjust the priorities.
- In clock driven systems, there are two main approaches to schedule aperiodic and sporadic jobs: spare capacity scheduling and overloading.
  - Spare capacity scheduling is a static and conservative approach that reserves some time slots in the pre-computed schedule for aperiodic and sporadic jobs. This means that they can only execute when there is a spare slot available. This ensures that periodic jobs always meet their deadlines, but it may result in low utilization and wasted capacity if there are no aperiodic and sporadic jobs to execute.
  - Overloading is a dynamic and aggressive approach that allows aperiodic and sporadic jobs to execute in any time slot, even if it is allocated to a periodic job. This means that they can execute as soon as they arrive, but they may preempt or delay periodic jobs. This improves the responsiveness of aperiodic and sporadic jobs, but it requires more computation and overhead to check the feasibility and adjust the schedule.



## Unit 3 - Resources Sharing

- Resource sharing is the practice of making the resources of one entity available to another entity efficiently and effectively .
- Resources can include library materials, manpower, services, space, equipment, technology, finances, etc .
- Resource sharing can be done among libraries, institutions, projects, investigators, or private industries   .
- Resource sharing can have various benefits, such as reducing costs, increasing access, enhancing quality, improving efficiency, and fostering collaboration .
- Resource sharing can also have some challenges, such as legal issues, technical issues, policy issues, and cultural issues .
- Resource sharing can be facilitated by various methods, such as interlibrary loan, consortia, networks, agreements, contracts, etc  .



### Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when multiple jobs or tasks compete for the same resource, such as a processor, a memory, a disk, or a communication channel.
- Resource contention affects the execution behavior and schedulability of jobs or tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock.
- Resource access control (RAC) is a set of rules or protocols that govern when and under what conditions each request for a resource is granted and how jobs or tasks requiring resources are scheduled.
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of the system.
- RAC can be classified into two categories: non-preemptive and preemptive.
  - Non-preemptive RAC means that once a job or task acquires a resource, it cannot be interrupted or preempted by another job or task until it releases the resource.
  - Preemptive RAC means that a job or task holding a resource can be interrupted or preempted by another job or task with higher priority or urgency, and the resource can be transferred or shared among them.
- Some examples of non-preemptive RAC are: no access control, priority ceiling protocol, stack-based protocol, and priority inheritance protocol.
- Some examples of preemptive RAC are: immediate ceiling protocol, preemptive ceiling protocol, and slack-based protocol.



Hello, I am Sydney, your AI assistant. I can help you with your query. Here are some notes on the topic of Non-preemptive Critical Sections for the subject of Real Time System.

### Non-preemptive Critical Sections

- A critical section is a code segment that accesses shared resources or variables that need to be synchronized to maintain the consistency of data.
- A non-preemptive critical section is a critical section that is scheduled on the processor without interruption or preemption by other tasks or jobs .
- When a job requests a resource, it is always allocated the resource. When a job holds any resource, it executes at a priority higher than the priorities of all jobs. This protocol is called non-preemptive critical section protocol (NPCS).
- The advantages of NPCS are:
  - It is simple and easy to implement.
  - It avoids deadlock, as no job is ever preempted when it holds any resource.
  - It preserves the order of resource requests, as the first job to request a resource gets it.
- The disadvantages of NPCS are:
  - It may cause priority inversion, as a low-priority job holding a resource may block a high-priority job from executing.
  - It may cause blocking, as a job may have to wait for a resource that is held by another job.
  - It may cause resource underutilization, as a job holding a resource may not use it for the entire duration of its critical section.
  - It may cause long response times, as a job may have to wait for a long time to access a resource.



### Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-inheritance and priority-ceiling protocols are two methods for managing resource access control in real-time systems.
- Both protocols aim to prevent unbounded priority inversion, which is a situation where a high-priority task is blocked by a low-priority task that holds a shared resource.
- Priority-inheritance protocol allows a low-priority task that holds a resource to temporarily inherit the priority of the highest-priority task that is waiting for the same resource. This way, the low-priority task can finish its critical section and release the resource sooner, reducing the blocking time of the high-priority task.
- Priority-ceiling protocol assigns a priority ceiling to each resource, which is the highest priority of any task that can access that resource. A task can only access a resource if its priority is higher than the priority ceiling of all the resources currently held by other tasks. This way, the priority-ceiling protocol prevents a low-priority task from accessing a resource that may be needed by a higher-priority task later, avoiding blocking and deadlock.
- The differences between the two protocols are:
  - Priority-inheritance protocol is greedy, while priority-ceiling protocol is not. The former allows a task to access a resource whenever it is free, while the latter may deny a task access to a free resource if its priority is lower than the priority ceiling of the resource.
  - Priority-inheritance protocol can cause chained blocking, while priority-ceiling protocol can cause avoidance blocking. Chained blocking is when a task is blocked by another task that is blocked by another task, and so on. Avoidance blocking is when a task is blocked by a lower-priority task that does not hold the requested resource, but may access it later.
  - Priority-inheritance protocol has a higher runtime overhead, while priority-ceiling protocol has a higher memory overhead. The former requires dynamic priority changes and tracking of blocked tasks, while the latter requires static priority ceiling assignment and checking of resource status.



# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its current priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task releases a resource, its current priority is restored to its original priority, and the current ceiling of the system is lowered accordingly.
- SBPCP prevents priority inversion, deadlock, and chain blocking, and guarantees bounded blocking time for each task .
- SBPCP is suitable for systems that have limited memory and need to share a run-time stack among tasks .



# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- There are two variants of the protocol: Original Ceiling Priority Protocol (OCPP) and Immediate Ceiling Priority Protocol (ICPP).
- OCPP works by temporarily raising the priority of a task that accesses a shared resource to the highest priority of any task that may access the same resource.
- ICPP works by raising the priority of a task that accesses a shared resource to the ceiling priority of the resource, which is the highest priority of any task that may access the resource.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the ceiling of the system each time task priorities change .
- An example of a dynamic system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in deadline driven system is shown below :

| Time | Task | Resource | Priority | Ceiling |
|------|------|----------|----------|---------|
| 0    | T1   | X        | 1        | 1       |
| 1    | T1   | X        | 1        | 1       |
| 2    | T1   | X        | 1        | 1       |
| 3    | T1   | X        | 1        | 1       |
| 4    | T2   | Y        | 2        | 2       |
| 5    | T2   | Y        | 2        | 2       |
| 6    | T2   | Y        | 2        | 2       |
| 7    | T2   | Y        | 2        | 2       |
| 8    | T1   | X        | 1        | 2       |
| 9    | T1   | X        | 1        | 2       |

- The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The priority ceiling of Y is 2 from time 4 to 8 and becomes 1 from time 8 to 9 and so on .
- The ceiling of the system is the maximum of the priority ceilings of all the resources.
- The ceiling of the system is 1 from time 0 to 4 and becomes 2 from time 4 to 8 and so on .
- The priority ceiling protocol ensures that a task can access a resource only if its priority is higher than the ceiling of the system.
- This prevents deadlock and unbounded priority inversion, as well as reduces the blocking time of higher priority tasks .

: Use of Priority Ceiling Protocol in Dynamic Priority Systems: https://benchpartner.com/use-of-priority-ceiling-protocol-in-dynamic-priority-systems
: Use of Priority Ceiling Protocol in Dynamic Priority Systems: http://benchpartner.com/use-of-priority-ceiling-protocol-in-dynamic-priority-systems
: Priority ceiling protocol - Wikipedia: https://en.wikipedia.org/wiki/Priority_ceiling_protocol
: Priority Ceiling Protocol - GeeksforGeeks: https://www.geeksforgeeks.org/priority-ceiling-protocol/



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
- Dual ceiling protocol is a variant of preemption ceiling protocol that allows a task to lock an object with two different ceiling priorities: a read ceiling and a write ceiling.
- A task can lock an object for reading if its priority is higher than the read ceiling of all the objects currently locked by other tasks, and it can lock an object for writing if its priority is higher than the write ceiling of all the objects currently locked by other tasks.
- Dual ceiling protocol can reduce the priority inversion and increase the concurrency of object-oriented real-time systems.



### Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable.
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section.
- The challenge of access control in multiple-unit resources is to avoid deadlock and priority inversion, while ensuring schedulability and resource utilization.
- There are different protocols for access control in multiple-unit resources, such as:
  - Priority Inheritance Protocol (PIP): A job that locks a resource inherits the priority of the highest-priority job that is blocked on that resource. The priority is restored when the resource is unlocked.
  - Priority Ceiling Protocol (PCP): Each resource is assigned a priority ceiling, which is the highest priority of any job that can lock that resource. A job can lock a resource only if its priority is higher than the priority ceiling of all locked resources. A job that locks a resource inherits the priority ceiling of that resource. The priority is restored when the resource is unlocked.
  - Stack Resource Policy (SRP): Each job is assigned a preemption level, which is fixed and independent of its priority. A job can lock a resource only if its preemption level is higher than the preemption level of all jobs that have locked any resource. A job that locks a resource inherits the preemption level of the lowest-level job that has locked any resource. The preemption level is restored when the resource is unlocked.
- The advantages and disadvantages of these protocols depend on the characteristics of the system, such as the number of resources, the number of units per resource, the length of critical sections, and the priority assignment scheme.



### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts from occurring by locking data objects before accessing them. Examples are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
  - Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting transactions. Examples are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- Pessimistic algorithms are suitable for hard real time systems where deadlines are strict and aborts are costly. Optimistic algorithms are suitable for soft real time systems where deadlines are flexible and aborts are acceptable.
- Some of the factors that affect the performance of concurrency control algorithms are blocking time, priority inversion, deadlock, abort rate, response time, and schedulability.



```
## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information between two or more parties without significant delay.
- RTC can be synchronous or asynchronous, depending on the degree of coordination and synchronization required by the participants.
- Examples of RTC include voice calls, video calls, instant messaging, live streaming, online gaming, and collaborative editing.
- RTC can be implemented using various technologies, such as:
  - Internet Protocol (IP) networks, which provide the infrastructure for data transmission and routing.
  - Session Initiation Protocol (SIP), which is a signaling protocol for establishing, modifying, and terminating multimedia sessions over IP networks.
  - Real-time Transport Protocol (RTP), which is a protocol for delivering audio and video data over IP networks with minimal delay and loss.
  - Web Real-Time Communication (WebRTC), which is a set of standards and APIs that enable browser-based RTC applications without the need for plugins or downloads.
- RTC can offer many benefits, such as:
  - Enhancing social interaction and collaboration among geographically dispersed individuals and groups.
  - Reducing travel costs and environmental impact by enabling remote work and education.
  - Improving customer service and satisfaction by providing instant feedback and support.
  - Enabling new forms of entertainment and creativity by allowing live participation and interaction.
- RTC can also pose some challenges, such as:
  - Ensuring security and privacy of the communication data and participants' identities.
  - Managing bandwidth and network congestion to avoid degradation of quality and performance.
  - Dealing with interoperability and compatibility issues among different devices, platforms, and standards.
  - Addressing ethical and legal implications of RTC, such as consent, ownership, and regulation.
```



### Basic Concepts in Real Time Communication

Real time communication (RTC) is a mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In RTC, there is always a direct path between the source and the destination. The term real time is synonymous with live.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Streaming media and live broadcasting

Some basic concepts in real time communication are:

- Bandwidth: The amount of data that can be transmitted or received per unit of time. It is measured in bits per second (bps) or bytes per second (Bps). Bandwidth affects the quality and speed of RTC.
- Latency: The time it takes for a data packet to travel from the source to the destination. It is measured in milliseconds (ms) or seconds (s). Latency affects the responsiveness and synchronicity of RTC.
- Jitter: The variation in latency of data packets. It is caused by network congestion, routing changes, or other factors. Jitter affects the smoothness and continuity of RTC.
- Packet loss: The percentage of data packets that are lost or corrupted during transmission. It is caused by network errors, interference, or congestion. Packet loss affects the reliability and quality of RTC.
- Quality of service (QoS): The ability of a network to provide different levels of priority and performance to different types of data traffic. QoS helps to ensure that RTC applications get the required bandwidth, latency, jitter, and packet loss parameters.
- Encryption: The process of transforming data into an unreadable form to prevent unauthorized access or modification. Encryption helps to ensure the security and privacy of RTC.
- Codec: The software or hardware that compresses and decompresses data for transmission and reception. Codec affects the size and quality of data in RTC.
- Protocol: The set of rules and standards that govern how data is formatted, transmitted, and received in a network. Protocol affects the compatibility and interoperability of RTC.

Some common protocols used in RTC are:

- Real-time Transport Protocol (RTP): A protocol that provides end-to-end delivery of audio and video data over IP networks. RTP supports QoS, encryption, and synchronization.
- Real-time Transport Control Protocol (RTCP): A protocol that works with RTP to provide feedback and control information about the RTP data streams. RTCP helps to monitor and adjust the QoS parameters of RTC.
- Real-time Streaming Protocol (RTSP): A protocol that controls the delivery of streaming media over IP networks. RTSP allows the user to play, pause, rewind, and fast-forward the media stream.
- Session Initiation Protocol (SIP): A protocol that establishes, modifies, and terminates multimedia sessions over IP networks. SIP enables the user to initiate and join RTC sessions with other users.
- Web Real-Time Communication (WebRTC): A set of technologies that enable RTC in web browsers and mobile applications. WebRTC uses RTP, RTCP, and SIP to provide peer-to-peer RTC without requiring any plugins or downloads.



### Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT) .
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- Hard real-time systems are deterministic in nature, meaning that they guarantee to meet the deadlines for all tasks .
- Soft real-time systems are probabilistic in nature, meaning that they may occasionally miss the deadlines for some tasks, but with a very low probability .
- Hard real-time systems are used for applications where missing a deadline can result in catastrophic consequences, such as safety-critical systems, nuclear reactors, avionics, etc.  .
- Soft real-time systems are used for applications where missing a deadline can result in degraded performance, but not fatal outcomes, such as multimedia, video games, web servers, etc.  .
- Hard real-time systems require strict scheduling algorithms, such as rate-monotonic, earliest deadline first, etc., to ensure that all tasks are executed within their deadlines .
- Soft real-time systems can use more flexible scheduling algorithms, such as round-robin, priority-based, etc., to optimize the system performance and resource utilization .
- Hard real-time systems have higher predictability, reliability, and robustness than soft real-time systems .
- Soft real-time systems have higher adaptability, scalability, and efficiency than hard real-time systems .



### Model of Real Time Communication

- Real time communication is any online communication that happens in real-time, with negligible latency and without storing data en route to the destination  .
- Examples of real time communication include voice calls, video calls, instant messaging, live streaming, online gaming, etc.
- Real time communication can be classified into two types: real time traffic and real time control.
- Real time traffic consists of streams of messages that are generated by their sources and delivered to their respective destinations on a continuous basis.
- Real time traffic can be further divided into three categories: periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals and have fixed deadlines and lengths.
- Aperiodic messages are generated at irregular intervals and have variable deadlines and lengths.
- Sporadic messages are generated randomly and have unpredictable deadlines and lengths.
- Real time control consists of commands and feedbacks that are exchanged between controllers and controlled devices in a real time system.
- Real time control can be further divided into two categories: hard and soft real time control.
- Hard real time control requires that all commands and feedbacks are delivered within strict deadlines, otherwise the system may fail or cause damage.
- Soft real time control allows some commands and feedbacks to be delivered after their deadlines, but with a degradation in performance or quality.
- In the model of real time communication, end users of the message application systems are sources and destinations residing in different hosts .
- The network interface of each host contains input queue and output queue .
- Two buffer areas called input/output buffer are allocated to input and output queue to store queuing information .
- The network interface also contains a scheduler that decides the order of sending and receiving messages based on their priorities and deadlines .
- The network consists of routers and links that connect the hosts and transfer the messages .
- The network also contains a network manager that monitors and controls the network resources and traffic .
- The model of real time communication can be represented by the following diagram :

```
+-----------------+      +-----------------+
| Source          |      | Destination     |
| Application     |      | Application     |
+-----------------+      +-----------------+
| Input Queue     |      | Output Queue    |
| Input Buffer    |      | Output Buffer   |
| Scheduler       |      | Scheduler       |
+-----------------+      +-----------------+
| Network         |      | Network         |
| Interface       |      | Interface       |
+-----------------+      +-----------------+
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
         |                        |
+-----------------+      +-----------------+
| Router          |      | Router          |
| Network Manager |      | Network Manager |
+-----------------+      +-----------------+
```

- The performance of the model of real time communication can be measured by three parameters: throughput, delay and jitter .
- Throughput is the amount of data that can be transferred per unit time .
- Delay is the time taken for a message to travel from the source to the destination .
- Jitter is the variation in delay for different messages .
- The goal of the model of real time communication is to maximize the throughput, minimize the delay and jitter, and meet the deadlines and quality of service requirements of the messages .



### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) is a simple and fair priority-based service discipline that assigns a weight to each queue and serves them in a circular order, proportional to their weights.
- WRR does not require a sorted priority queue, only a round-robin queue. It can guarantee the minimum bandwidth for each queue and avoid starvation of low-priority queues.
- However, WRR cannot provide strict delay and jitter bounds for different classes of packets, as it does not consider the packet size or arrival rate.
- To overcome this limitation, some variants of WRR have been proposed, such as:
  - Rate-controlled frame-based WRR (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server. The rate controller adjusts the weights of the queues according to their delay requirements, and the frame-based WRR server serves the packets within a fixed frame size.
  - Probabilistic priority (PP) scheduling, which assigns a parameter to each priority queue that determines the probability of serving the queue when it is polled by the server. The parameter can be adjusted dynamically to balance the trade-off between fairness and priority.
  - Class-based WRR (CBWRR), which groups the queues into different classes and applies WRR within each class. The classes are served according to their priority levels, and the weights of the queues within each class can be changed to achieve different service objectives.
- These variants of WRR can provide better performance than the basic WRR in terms of delay, jitter, fairness and bandwidth allocation for different classes of packets in a switched network.



### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast network.
- Broadcast networks are networks where a single transmission can reach all the nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to determine which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but they suffer from collisions and low efficiency.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next, such as token passing or polling. These protocols are reliable and fair, but they have high overhead and delay.
- Reservation-based protocols use a separate control channel or a dedicated time slot to reserve the access to the data channel, such as TDMA or CDMA. These protocols are efficient and scalable, but they require synchronization and coordination among the nodes.
- Some MAC protocols combine different access strategies to achieve better performance, such as ABROAD, which incorporates a collision-avoidance handshake within each slot of a synchronous transmission schedule, allowing nodes to reclaim and/or reuse idle slots while maintaining bounded access delay.



### Internet and Resource Reservation Protocols

- Internet applications have different network performance requirements, such as reliability, timeliness, and quality of service (QoS).
- Resource Reservation Protocol (RSVP) is a network-control protocol that enables Internet applications to obtain specific QoS for their data flows or streams .
- RSVP operates over IPv4 or IPv6 and provides receiver-initiated setup of resource reservations for multicast or unicast data flows.
- RSVP uses soft state and periodic refresh messages to maintain the resource reservations along the end-to-end path through the network.
- RSVP supports both Integrated Services (IntServ) and Differentiated Services (DiffServ) models of QoS.
- RSVP can be used in real-time systems for efficient and fast delivery of transmission packets from the sender to the receiver.



## Unit 5 - Real Time Operating Systems and Databases

- A real-time operating system (RTOS) is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations  .
- A real-time database is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock market data, and online gaming data .
- The main characteristics of real-time operating systems and databases are:
  - **Predictability**: The system must be able to guarantee that the tasks and transactions will be completed within a specified deadline, regardless of the workload or external factors.
  - **Responsiveness**: The system must be able to react quickly to the changes in the data and events, and provide timely feedback to the users or other systems.
  - **Reliability**: The system must be able to handle failures and errors gracefully, and ensure the consistency and integrity of the data and operations.
  - **Scalability**: The system must be able to handle increasing amounts of data and events, and support concurrent and distributed processing.
- The main challenges of real-time operating systems and databases are:
  - **Resource management**: The system must be able to allocate and deallocate the limited resources, such as CPU, memory, disk, and network, efficiently and fairly among the tasks and transactions.
  - **Scheduling**: The system must be able to prioritize and execute the tasks and transactions according to their deadlines, importance, and dependencies, and avoid conflicts and starvation.
  - **Data management**: The system must be able to store, update, query, and analyze the data that is dynamic, heterogeneous, and multidimensional, and ensure the freshness, accuracy, and relevance of the data.
  - **Security**: The system must be able to protect the data and operations from unauthorized access, modification, or deletion, and ensure the confidentiality, integrity, and availability of the data and operations.



### Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee the timely and predictable execution of tasks, regardless of the system load. An RTOS has the following features   :

- **Small size**: An RTOS is designed to occupy very less memory and consume fewer resources, as it often runs on embedded devices with limited hardware capabilities.
- **Fast response**: An RTOS can quickly switch between tasks and handle interrupts, as it has a low overhead and minimal latency.
- **Determinism**: An RTOS can ensure that tasks will meet their deadlines and respond as expected every time, as it has a fixed scheduling algorithm and priority-based task management.
- **Co-operative or pre-emptive scheduling**: An RTOS can use either co-operative or pre-emptive scheduling to manage tasks. In co-operative scheduling, tasks run until they are completed or voluntarily yield the CPU. In pre-emptive scheduling, tasks are assigned a priority and the highest priority task always runs, while lower priority tasks are suspended or delayed.
- **Main loop or event-driven**: An RTOS can use either a main loop or an event-driven approach to execute tasks. In a main loop, tasks are executed in a fixed order in an infinite loop. In an event-driven approach, tasks are triggered by external or internal events, such as interrupts or timers.



# Time Services for Real Time Operating Systems

- A real time operating system (RTOS) is an operating system that processes data and events that have critically defined time constraints.
- A RTOS provides services for real time applications, such as industrial control, flight control, and telephone switching.
- A RTOS allows multiple tasks or programs to run simultaneously but based on their priorities. The task planning unit decides which thread to be executed. The processor stops active work (if any) and starts execution for the high priority task it finds.
- A RTOS is dependent on the clock interrupts. This system produces the Interrupt Service Routine (ISR) interrupts.
- A RTOS provides time services such as:
  - Clock and timer management: A RTOS maintains a system clock that measures the elapsed time since the system started. A RTOS also provides timers that can be used to trigger events or actions after a specified time interval or at a specific time point.
  - Time slicing: A RTOS can divide the CPU time among the ready tasks or threads according to their priorities or other criteria. This allows the tasks or threads to share the CPU and achieve concurrency.
  - Deadline scheduling: A RTOS can schedule the tasks or threads according to their deadlines, which are the time points by which they must finish their execution. A RTOS can also handle the situations when the tasks or threads miss their deadlines or when the deadlines are not feasible.
  - Time synchronization: A RTOS can synchronize the system clock with an external time source, such as a GPS or a network server. This ensures that the system time is accurate and consistent with other systems or devices.



### UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- UNIX is not a RTOS because it does not guarantee timing requirements of the processes under its control. UNIX strives to provide good average performance, but not correct timing, which is the key feature of a RTOS.
- However, some variants of UNIX, such as Linux, have been modified to add real-time capabilities, such as preemptive scheduling, low-latency interrupts, and real-time libraries .
- These modifications allow Linux to be used as a RTOS for some applications, such as human-in-the-loop simulations, launch vehicles, and spacecrafts .
- However, using Linux as a RTOS also poses some challenges, such as compatibility issues, security risks, and performance trade-offs .
- Therefore, UNIX and its variants are not ideal RTOS, but they can be adapted to meet some real-time requirements with careful design and testing.



### POSIX Issues

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interact with an operating system.
- POSIX was originally designed for UNIX-like systems, but it does not address the specific needs of real-time applications, such as predictable timing, priority scheduling, and inter-process communication.
- To address these needs, a real-time working group was established in POSIX, and it developed several extensions to the POSIX standard, such as POSIX.1b (real-time extensions), POSIX.1c (threads), and POSIX.4 (timers and clocks).
- Some of the issues that POSIX real-time extensions address are:
  - Scheduling: POSIX.1b defines two scheduling policies for real-time processes: FIFO (first-in first-out) and RR (round-robin). These policies allow real-time processes to have higher priority than non-real-time processes, and to run until they block, yield, or complete. POSIX.1b also defines a minimum number of priority levels for real-time processes, and allows processes to change their own priority dynamically.
  - Timers and clocks: POSIX.4 defines high-resolution timers and clocks that can be used by real-time applications to measure time intervals, set timeouts, and generate periodic events. POSIX.4 also defines a monotonic clock that is not affected by system time changes, and a real-time clock that is synchronized with the wall clock.
  - Signals: POSIX.1b improves the signal mechanism defined in POSIX.1 by allowing signals to be queued, prioritized, and delivered to specific threads. POSIX.1b also defines a new type of signal, called a real-time signal, that can carry additional information, such as an integer value or a pointer to a data structure.
  - Semaphores: POSIX.1b defines a new type of synchronization primitive, called a semaphore, that can be used to coordinate access to shared resources among multiple processes or threads. POSIX.1b semaphores can be either named or unnamed, and can have an initial value that indicates the number of available resources. POSIX.1b semaphores also support priority inheritance, which prevents priority inversion problems.
  - Message queues: POSIX.4 defines a new type of inter-process communication mechanism, called a message queue, that can be used to send and receive messages among processes or threads. POSIX.4 message queues can be either named or unnamed, and can have a fixed or variable size. POSIX.4 message queues also support priority ordering, which ensures that messages are delivered according to their urgency.
  - Memory locking: POSIX.1b defines a new function, called mlock, that can be used to lock a portion of the process's address space into physical memory, preventing it from being swapped out by the operating system. This can improve the performance and predictability of real-time applications, as it reduces the page fault overhead. POSIX.1b also defines a function, called mlockall, that can lock the entire address space of the process.



### Characteristic of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, or timestamps.
- Temporal data can be used to analyze trends, patterns, events, or changes over time in various domains, such as weather, traffic, demographics, etc.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon by an agent.
- Temporal data can be stored in different ways, such as using separate attributes, using temporal data types, or using temporal tables.
- Temporal data can be queried and manipulated using different methods, such as using temporal predicates, temporal functions, or temporal operators.
- Temporal data can be visualized using different techniques, such as using temporal charts, maps, or animations.



### Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of non-real-time systems that ensures that the data stored in the database satisfies the integrity constraints and the consistency rules.
- Temporal consistency is important for real-time systems because they need to make decisions and take actions based on the most up-to-date information about the physical environment.
- Temporal consistency can be violated by two factors: data staleness and data inconsistency.
  - Data staleness occurs when the data stored in the database is outdated and does not reflect the current state of the physical environment. This can happen due to the delay in sensing, processing, and updating the data.
  - Data inconsistency occurs when the data stored in the database is contradictory and does not agree with each other. This can happen due to the concurrency and interference of multiple transactions that access and update the data.
- Temporal consistency can be maintained by using various techniques, such as triggered updates, temporal validity, and temporal constraints .
  - Triggered updates are a technique that updates the data in the database whenever there is a significant change in the physical environment. This reduces the data staleness and ensures that the data is always fresh.
  - Temporal validity is a technique that assigns a validity interval to each data item in the database, which specifies the time period during which the data item is valid and can be used by transactions. This reduces the data staleness and ensures that the transactions only read valid data.
  - Temporal constraints are a technique that imposes deadlines and priorities on the transactions that access and update the data in the database. This reduces the data inconsistency and ensures that the transactions are executed in a timely and orderly manner.



### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, where many events and actions occur simultaneously.
- Real-time systems (RTS) are systems that respond to their environment within specified time constraints .
- RTS are inherently concurrent and typically manage shared data resources, such as sensors, actuators, files, databases, etc .
- Concurrency control is the process of ensuring both logical and timing correctness of concurrent accesses to shared data resources in RTS.
- Logical correctness means that the concurrent accesses do not violate the data integrity and consistency rules, such as mutual exclusion, serializability, etc.
- Timing correctness means that the concurrent accesses do not cause deadline misses or timing anomalies, such as priority inversion, blocking, etc.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by using locks, timestamps, or other mechanisms to coordinate concurrent accesses.
- Optimistic concurrency control techniques allow conflicts to occur and then resolve them by using validation, compensation, or restart mechanisms.
- Concurrency control techniques can also be classified into centralized and distributed, depending on whether there is a single or multiple coordinators for managing concurrent accesses.
- Concurrency control techniques should be designed and evaluated based on the following criteria: correctness, performance, scalability, and adaptability.
- Correctness criteria include logical and timing correctness, as well as deadlock-freedom, liveliness, and fairness.
- Performance criteria include throughput, response time, utilization, and overhead.
- Scalability criteria include the ability to handle increasing number of concurrent accesses, data resources, and system nodes.
- Adaptability criteria include the ability to cope with dynamic changes in the system workload, environment, and requirements.
- Concurrency control for real-time systems is a challenging and active research area, as it involves trade-offs and conflicts among different criteria and techniques.



### Overview of Commercial Real Time databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service.
- Some of the attributes of live real-time databases are:
  - Concurrency control: the ability to handle multiple transactions accessing the same data without compromising the consistency and integrity of the data.
  - Data freshness: the degree to which the data reflects the current state of the real world.
  - Data distribution: the ability to store and access data across multiple nodes or locations for scalability and availability.
  - Data replication: the ability to create and maintain copies of data for backup, load balancing, or fault tolerance.
  - Data security: the ability to protect data from unauthorized access, modification, or deletion.
  - Data recovery: the ability to restore data to a consistent state after a failure or error.
  - Data analysis: the ability to perform queries, reports, or analytics on the data to derive insights or support decision making.
  - Data integration: the ability to combine data from different sources or formats into a unified view or schema.
- Some of the examples of commercial real-time databases are :
  - Dealpath: a cloud-based platform that provides data and workflow management for commercial real estate transactions.
  - Altus Group: a data provider that offers historical and current market information, valuation, and advisory services for commercial real estate.
  - CoStar: a leading provider of commercial real estate data, analytics, and online marketplaces.
  - Google Cloud Firestore: a highly scalable, fully managed NoSQL database service that supports real-time data synchronization and offline access for web and mobile applications.

