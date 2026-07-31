

## Unit 1 - Introduction of Real Time System

- A real-time system is a system that can process data and events within predictable and specific time constraints .
- A real-time system is characterized by its ability to produce the expected result within a defined deadline (timeliness) and to coordinate independent clocks and operate together in unison (time synchronization) .
- A real-time system can be classified into two types based on the timing constraints: hard real-time system and soft real-time system .
  - A hard real-time system has absolute deadlines, and if those allotted time spans are missed, a system failure will occur . For example, flight control systems, nuclear power plant control systems, etc.
  - A soft real-time system has relative deadlines, and if those allotted time spans are missed, the system performance will degrade but not fail . For example, video streaming, online gaming, etc.
- A real-time system requires a real-time operating system (RTOS) that can manage the system resources and tasks with a scheduler, data buffers, or fixed task priorities .
  - An RTOS is different from a time-sharing operating system, such as Unix, which does not guarantee the timeliness or synchronization of the system .
  - An RTOS can be preemptive or cooperative, depending on whether the tasks can be interrupted by higher priority tasks or not .
- A real-time system can be designed and analyzed using various methods and tools, such as real-time modeling, real-time scheduling, real-time communication, real-time testing, etc. .



# Definition for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events or inputs within a specified time interval, called a deadline.
- A real time system can be classified into two types: hard real time system and soft real time system.
- A hard real time system is a system that must meet all its deadlines, otherwise it may cause catastrophic consequences or failure. For example, a flight control system, a nuclear reactor control system, or a pacemaker.
- A soft real time system is a system that can tolerate some missed deadlines, but the quality of service or performance may degrade. For example, a video streaming system, a voice recognition system, or a web server.
- A real time system can also be classified into two types based on the predictability of the events or inputs: periodic and aperiodic.
- A periodic system is a system that has events or inputs that occur at regular intervals, such as a sensor reading, a clock tick, or a task execution. The interval between two consecutive events or inputs is called the period.
- An aperiodic system is a system that has events or inputs that occur at irregular or unpredictable intervals, such as a user request, a network packet, or a fault. The interval between two consecutive events or inputs is called the interarrival time.
- A real time system can also be classified into two types based on the complexity of the system: simple and complex.
- A simple system is a system that has a single processor, a single task, and a single resource. The system can be easily analyzed and verified using mathematical models and techniques.
- A complex system is a system that has multiple processors, multiple tasks, and multiple resources. The system may have dependencies, conflicts, or uncertainties among the components. The system may require advanced methods and tools for analysis and verification.



# Typical Real Time Applications

- A real-time application (RTA) is an application that requires a program to respond to stimuli within a specific time frame. A real-time application can be classified as either hard or soft, depending on the severity of the consequences of missing a deadline.
- Some examples of typical real-time applications are:

  - **Video conferencing**: This application allows users to communicate with each other through video and audio streams over the internet. It requires low latency and high bandwidth to ensure smooth and synchronized transmission of data.
  - **Voice over Internet Protocol (VoIP)**: This application enables users to make phone calls over the internet using digital signals. It requires low jitter and packet loss to ensure clear and uninterrupted voice quality.
  - **Online gaming**: This application allows users to play games with other players over the internet. It requires fast and consistent response time to ensure fair and enjoyable gameplay.
  - **Community storage applications**: These applications allow users to store and access data on a distributed network of servers. They require high availability and reliability to ensure data integrity and security.
  - **Some e-commerce applications**: These applications allow users to buy and sell goods and services online. They require timely and accurate processing of transactions and orders to ensure customer satisfaction and trust.
  - **Real-time operating system (RTOS)**: This is a type of operating system that is designed to handle real-time tasks with predictable and deterministic behavior. It requires low overhead and minimal interference to ensure efficient and timely execution of tasks.
  - **Instant messaging (IM) applications**: These applications allow users to send and receive text, voice, and video messages over the internet. They require low latency and high throughput to ensure fast and smooth communication.
  - **Team collaboration applications**: These applications allow users to work together on projects and tasks over the internet. They require real-time synchronization and coordination of data and actions to ensure effective and productive collaboration.
  - **Digital control**: This is a type of real-time application that is embedded in sensors and actuators and functions as a digital controller. It requires precise and timely feedback and control of physical systems and processes .
  - **Optimal control**: This is a type of real-time application that is used to optimize the performance of a system or process by minimizing or maximizing a certain objective function. It requires complex and dynamic computation and decision making.
  - **Command and control**: This is a type of real-time application that is used to monitor and control the activities and operations of a system or organization. It requires high reliability and security to ensure safety and effectiveness.
  - **Signal processing**: This is a type of real-time application that is used to analyze, modify, and synthesize signals such as sound, image, and video. It requires high speed and accuracy to ensure quality and functionality.
  - **Tracking**: This is a type of real-time application that is used to locate and follow the movement and position of an object or entity. It requires high resolution and precision to ensure accuracy and usefulness.
  - **Real-time databases**: These are databases that are designed to handle real-time data and queries. They require high concurrency and consistency to ensure data validity and timeliness.
  - **Multimedia**: These are applications that involve the creation, processing, and presentation of multimedia content such as audio, video, and graphics. They require high performance and quality to ensure user satisfaction and engagement.

- These are some of the typical real-time applications that are used in various domains and scenarios. They have different requirements and challenges that need to be addressed by real-time systems and technologies.



# Release Times for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- A real time system is a system that must respond to events within a specified time interval, otherwise it may cause undesirable consequences or failure.
- A real time system consists of a set of tasks that have deadlines and priorities, and a scheduler that assigns the processor to the tasks according to some algorithm.
- A task is a unit of work that can be executed by the processor. A task can be periodic, aperiodic, or sporadic, depending on its arrival pattern.
- A periodic task is a task that arrives at regular intervals, and has a fixed execution time and deadline. For example, a task that samples a sensor every 10 milliseconds is a periodic task.
- An aperiodic task is a task that arrives at irregular intervals, and has a variable execution time and deadline. For example, a task that handles user input is an aperiodic task.
- A sporadic task is a task that arrives at unpredictable intervals, and has a minimum inter-arrival time, a variable execution time and deadline. For example, a task that responds to an alarm is a sporadic task.
- The release time of a task is the time when the task becomes available for execution. For a periodic task, the release time is equal to the arrival time. For an aperiodic or sporadic task, the release time is the time when the task is accepted by the system, which may be different from the arrival time.
- The release time of a task is an important parameter for the scheduler, as it determines the eligibility of the task for execution. The scheduler must ensure that all the tasks meet their deadlines, while maximizing the system performance and minimizing the overhead.
- The release time of a task can be affected by several factors, such as the system load, the task priority, the scheduling algorithm, the preemption policy, the resource contention, and the external events.
- The release time of a task can be determined by different methods, such as the earliest deadline first (EDF) method, the rate monotonic (RM) method, the least laxity first (LLF) method, the earliest release time (ERT) method, and the slack stealing (SS) method. Each method has its own advantages and disadvantages, and may be suitable for different types of tasks and systems.



### Deadlines for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Unit 1 covers the following topics:
  - Definition and characteristics of real time systems
  - Classification and examples of real time systems
  - Typical components and architecture of real time systems
  - Design challenges and methods for real time systems
  - Real time operating systems and scheduling algorithms
- The notes for Unit 1 are expected to be completed by the end of the second week of the semester.
- The notes should be written in a clear, concise, and accurate manner, following the guidelines and format provided by the instructor.
- The notes should include the following elements:
  - A summary of the main concepts and definitions of each topic
  - A list of the key terms and acronyms used in each topic
  - A diagram or table to illustrate the classification or architecture of real time systems
  - A comparison or contrast of the different types or examples of real time systems
  - A description of the design challenges and methods for real time systems
  - A brief explanation of the real time operating systems and scheduling algorithms
- The notes should be submitted electronically via the course website or email, depending on the instructor's preference.
- The notes will be graded based on the following criteria:
  - Completeness and coverage of the topics
  - Clarity and correctness of the language and notation
  - Relevance and accuracy of the examples and diagrams
  - Organization and presentation of the notes
- The notes will count for 10% of the final grade for the course.
- Late submissions will be penalized by 10% of the total marks for each day of delay.
- If you have any questions or difficulties regarding the notes, please contact the instructor as soon as possible.



# Timing Constraints for the notes of the Unit 1 - Introduction of Real Time System in the subject of Real Time System

- Timing constraints are a vital attribute in real-time systems. They decide the total correctness of the result in real-time systems.
- The correctness of results in real-time systems does not depend only on logical correctness but also on the result being obtained within the time constraint.
- Every real-time system has a set of timing constraints that it has been designed to meet. If a system does not have timing constraints, it is not real-time.
- Timing constraints can be broken down into two categories :
  - Performance constraints: The constraints enforced on the response of the system are known as performance constraints. They specify the maximum or minimum time required for the system to react to an event or complete a task.
  - Reliability constraints: The constraints enforced on the behavior of the system are known as reliability constraints. They specify the probability or frequency of the system meeting the performance constraints.
- Timing constraints can be expressed using various constructs in requirements languages, such as deadlines, periodicity, jitter, latency, etc.
- Timing constraints can be validated using automatic test systems that can measure the actual response time and behavior of the system under different scenarios and compare them with the expected values.
- Timing constraints can be affected by various factors, such as hardware, software, communication, environment, etc. Therefore, real-time systems need to have time synchronization and timeliness capabilities to coordinate independent clocks and operate together in unison.



# Hard Real Time Systems

- A hard real time system is a system that must produce the expected result within a defined deadline (timeliness) and coordinate independent clocks and operate together in unison (time synchronization) .
- A hard real time system has absolute deadlines, and if those deadlines are missed, a system failure will occur  .
- A hard real time system is also known as an immediate real time system .
- A hard real time system is typically found interacting at a low level with physical hardware, in embedded systems .
- Examples of hard real time systems are nuclear power plant control systems, air traffic control systems, missile guidance systems, medical devices, etc. .
- Some characteristics of hard real time systems are:
  - The size of data and code is small and fixed .
  - The response time is in milliseconds or microseconds .
  - The peak load performance should be predictable and consistent .
  - The safety is critical and the system cannot tolerate any errors .
  - The system is usually preemptive and uses priority-based scheduling algorithms .



# Soft Real Time Systems

- A soft real-time system is a system that can tolerate some degree of latency or jitter in the execution of its tasks, without causing a catastrophic failure or a significant degradation of performance  .
- A soft real-time system has a **small window of time** for program completion rather than a precise moment due to a bit of jitter from the operating system.
- A soft real-time system can be run on **multiple cores** and impose fewer restrictions on applications.
- A soft real-time system can **miss some deadlines** occasionally acceptably with low probability.
- A soft real-time system can continue to function, though with **undesirable lower quality of output**.
- A soft real-time system is typically used to solve issues of **concurrent access** and the need to keep a number of **connected systems up-to-date** through changing situations.
- Some examples of soft real-time systems are:
  - Software that maintains and updates the flight plans for commercial airliners.
  - Streaming audio-video.
  - Online gaming.
  - Multimedia applications.



# Reference Models for Real Time Systems

- A reference model is a canonical form that defines the types and relations of the functions needed in a real time system .
- A reference model helps us to reason about the timing behavior and performance of a real time system, using consistent terminology and abstraction .
- A reference model consists of three elements: a workload model, a resource model, and a system model  .

## Workload Model

- The workload model specifies the applications supported by the system, such as tasks, jobs, processes, etc  .
- The workload model describes the parameters of each application, such as execution time, deadline, period, priority, resource dependencies, etc  .
- The workload model can also represent the precedence and communication relations among the applications, such as task graphs, data flow graphs, etc .

## Resource Model

- The resource model describes the resources available in the system, such as processors, memory, network, sensors, actuators, etc  .
- The resource model specifies the types and properties of each resource, such as speed, capacity, bandwidth, latency, etc  .
- The resource model can also represent the relations and constraints among the resources, such as shared access, mutual exclusion, contention, etc .

## System Model

- The system model defines the policies and mechanisms that govern the allocation and execution of the applications on the resources .
- The system model includes the scheduling algorithms, the synchronization protocols, the communication protocols, the fault tolerance techniques, etc .
- The system model determines the quality of service and the performance guarantees of the system, such as timeliness, reliability, availability, etc .



# Processors and Resources

- Processors and resources are two major types of system components in real-time systems.
- Processors are also called servers or active resources. They are essential for the execution of a job. A job must have one or more processors in order to execute and proceed towards completion. Examples of processors are computers, transmission links, disks, and database servers.
- Resources are also called passive resources. A job may or may not require a resource during its execution. A resource can be shared by multiple jobs, but only one job can access it at a time. Examples of resources are memory, files, printers, and sensors.
- Processors and resources can be classified into two categories: dedicated and shared.
- Dedicated processors or resources are allocated to a single job or task and cannot be used by any other job or task. Dedicated processors or resources can guarantee predictable and deterministic performance for the assigned job or task.
- Shared processors or resources are accessible by multiple jobs or tasks and can be used by any job or task that needs them. Shared processors or resources can improve the utilization and efficiency of the system, but they can also introduce contention and interference among the competing jobs or tasks.
- Real-time systems need to manage the allocation and scheduling of processors and resources to meet the timing constraints and quality of service requirements of the real-time applications .
- Real-time systems can use different techniques and algorithms to allocate and schedule processors and resources, such as priority-based, deadline-based, rate-monotonic, earliest deadline first, etc.
- Real-time systems can also use different technologies and solutions to optimize the performance and reliability of processors and resources, such as workload-aware processor tuning, time synchronization, and time-sensitive networking .



# Temporal Parameters of Real Time Workload

- A real time workload is a set of tasks or jobs that need to be executed by a real time system within certain time constraints.
- The temporal parameters of a job are the attributes that define its timing requirements and characteristics .
- The temporal parameters of a job are:
  - **Release time (r<sub>i</sub>)**: The time instant when the job becomes available for execution.
  - **Absolute deadline (d<sub>i</sub>)**: The time instant by which the job must finish its execution.
  - **Relative deadline (D<sub>i</sub>)**: The time interval between the release time and the absolute deadline of the job.
  - **Feasible interval ([r<sub>i</sub>, d<sub>i</sub>])**: The time interval during which the job can be executed by the system.
- The temporal parameters of a job can be specified by the application or the system designer, or they can be derived from other parameters such as periodicity, frequency, or latency .
- The temporal parameters of a job can be used to determine the schedulability and feasibility of the real time workload, as well as to evaluate the performance and quality of service of the real time system .



# Periodic Task Model

The periodic task model is a well-known deterministic workload model for real-time systems. It is best suited for hard real-time applications, such as digital control, real-time monitoring, and constant bit-rate voice/video transmission .

A periodic task is one that repeats itself after a fixed time interval. A periodic task is denoted by four tuples: Ti = < Φi, Pi, ei, Di >

Where,

- Φi – is the phase of the task. It is the time at which the first job of the task is released.
- Pi – is the period of the task. It is the time interval between two consecutive job releases of the task.
- ei – is the worst-case execution time of the task. It is the maximum time required by any job of the task to complete its execution on the processor.
- Di – is the relative deadline of the task. It is the maximum time allowed for any job of the task to finish its execution after its release.

The periodic task model assumes that:

- All tasks are independent and do not share any resources.
- All tasks have fixed and known parameters.
- All tasks have implicit deadlines, i.e., Di = Pi for all tasks.
- All tasks have constrained deadlines, i.e., Di ≤ Pi for all tasks.
- All tasks have zero jitter, i.e., Ji = 0 for all tasks.

The periodic task model can be extended by adding more parameters, such as jitter, offset, precedence constraints, resource requirements, etc. to capture more realistic scenarios.




# Precedence Constraints and Data Dependency

- Precedence constraints and data dependency are two types of constraints that may affect the scheduling of jobs in real-time systems.
- Precedence constraints specify the order in which jobs must execute, while data dependency specifies the data flow between jobs that communicate via shared data.
- Precedence constraints can be represented by a directed graph, called a precedence graph, where vertices are jobs and edges are precedence relations. A job J_i is a predecessor of another job J_k (and J_k a successor of J_i) if J_k cannot begin execution until the execution of J_i completes.
- Data dependency cannot be captured by a precedence graph. Data dependency occurs when jobs communicate via shared data, and the data of one job is dependent on the data of another job. For example, a job J_i may produce some data that is consumed by another job J_k, and J_k cannot execute until J_i has finished writing the data.
- Precedence constraints and data dependency may introduce additional delays and overheads in the execution of jobs, and may affect the feasibility and optimality of scheduling algorithms. Therefore, they must be taken into account when designing and analyzing real-time systems.



# Unit 2 - Real Time Scheduling

- Real time scheduling is the process of assigning and executing tasks in a system that has strict timing constraints and deadlines .
- Real time scheduling aims to achieve predictable and deterministic behavior of the system, by minimizing the response time and meeting the deadlines of the tasks .
- Real time scheduling can be classified into two categories: static and dynamic .
  - Static scheduling is done at compile time or before the system starts running. It is based on the known characteristics of the tasks, such as their arrival time, execution time, deadline, and priority. Static scheduling is suitable for systems that have fixed and periodic tasks, and do not require much flexibility or adaptability .
  - Dynamic scheduling is done at run time or during the system execution. It is based on the current state of the system, such as the availability of resources, the arrival of new tasks, the completion of existing tasks, and the occurrence of events. Dynamic scheduling is suitable for systems that have variable and aperiodic tasks, and require more flexibility and adaptability .
- Real time scheduling can also be classified into two types: preemptive and non-preemptive .
  - Preemptive scheduling allows a higher priority task to interrupt and suspend a lower priority task that is currently running. The lower priority task resumes its execution when the higher priority task finishes or is blocked. Preemptive scheduling can reduce the response time and improve the schedulability of the tasks, but it can also introduce overhead and complexity due to context switching and synchronization .
  - Non-preemptive scheduling does not allow a higher priority task to interrupt a lower priority task that is currently running. The higher priority task has to wait until the lower priority task finishes or is blocked. Non-preemptive scheduling can avoid the overhead and complexity of context switching and synchronization, but it can also increase the response time and reduce the schedulability of the tasks .
- Real time scheduling algorithms are the rules or methods that determine how to select and execute the tasks in a real time system. There are many real time scheduling algorithms, such as rate monotonic, earliest deadline first, least laxity first, etc. Each algorithm has its own advantages and disadvantages, and may be suitable for different types of systems and tasks .
- Real time scheduling analysis is the process of evaluating and verifying the performance and correctness of a real time system and its scheduling algorithm. It can be done by using mathematical models, simulation tools, or empirical methods. The main metrics or criteria for real time scheduling analysis are feasibility, schedulability, utilization, response time, deadline miss ratio, etc .
- Real time scheduling applications are the domains or scenarios that require real time systems and scheduling, such as industrial control, robotics, multimedia, avionics, automotive, etc. Each application may have different requirements and challenges for real time scheduling, such as hard or soft deadlines, periodic or aperiodic tasks, resource constraints, fault tolerance, etc .



# Common Approaches to Real Time Scheduling

Real time scheduling is the process of assigning execution time to tasks that have timing constraints, such as deadlines or periodicity. Real time scheduling aims to ensure that the system meets its timing requirements and performs its functionality correctly. There are different approaches to real time scheduling, depending on the characteristics of the tasks, the system, and the environment. Some of the common approaches are:

- **Clock-driven approach**: This approach is also known as time-driven or table-driven approach. It is mainly used for hard real time systems, where all the properties of the tasks, such as arrival time, execution time, deadline, and period, are known at design time. In this approach, a schedule is computed offline and stored in a table. The table specifies which task to execute at each time instant. A timer interrupts the system periodically and triggers the execution of the next task in the table. This approach is simple, predictable, and efficient, but it is not flexible or adaptable to dynamic changes in the system or the environment.   

- **Round-robin approach**: This approach is a commonly used technique in time-shared systems, where tasks are scheduled in a repetitive manner based on a time slice allocated to each task. The scheduler maintains a queue of ready tasks and assigns the processor to the first task in the queue for a fixed amount of time. When the time slice expires, the task is preempted and moved to the end of the queue, and the next task is selected. This approach is fair and simple, but it does not consider the timing constraints or the priorities of the tasks. It may cause deadline misses or underutilization of the processor.  

- **Weighted round-robin approach**: This approach is a variation of the round-robin approach, where tasks are assigned different weights based on their importance or urgency. The weight of a task determines the length of its time slice. Tasks with higher weights get longer time slices than tasks with lower weights. This approach is more responsive and flexible than the round-robin approach, but it still does not guarantee the satisfaction of the timing constraints or the optimality of the schedule.  

- **Priority-driven approach**: This approach is widely used for real time systems, where tasks are assigned different priorities based on their timing constraints or other criteria. The scheduler maintains a queue of ready tasks and selects the task with the highest priority to execute. If a higher priority task arrives or becomes ready, the current task is preempted and the higher priority task is executed. This approach can be static or dynamic, depending on whether the priorities are fixed or can change during the execution. Static priority-driven scheduling algorithms include rate-monotonic scheduling (RMS), where tasks are assigned priorities inversely proportional to their periods, and deadline-monotonic scheduling (DMS), where tasks are assigned priorities inversely proportional to their deadlines. Dynamic priority-driven scheduling algorithms include earliest-deadline-first scheduling (EDF), where tasks are assigned priorities based on their absolute deadlines, and least-slack-time scheduling (LST), where tasks are assigned priorities based on their remaining slack time. Priority-driven scheduling algorithms can achieve optimal schedules, meaning that they can schedule any set of tasks that is feasible, i.e., that can be scheduled by any algorithm. However, they are also more complex and require more overhead than clock-driven or round-robin approaches.



# Clock Driven Approach

- Clock-driven scheduling is also known as time-driven scheduling.
- In clock-driven scheduling, the system executes tasks according to a predetermined schedule.
- The schedule is computed offline based on the known parameters of the tasks, such as period, deadline, execution time, and precedence constraints.
- The schedule is typically cyclic, meaning that it repeats after a fixed interval called the major cycle.
- The schedule specifies which task should execute at each time instant, independent of events such as job releases and completions.
- Clock-driven scheduling is suitable for hard real-time systems that require predictable and deterministic behavior.
- Clock-driven scheduling has some advantages, such as:
  - It avoids the overhead of online scheduling decisions and context switches.
  - It can handle tasks with arbitrary deadlines and precedence constraints.
  - It can guarantee the schedulability of all tasks if the schedule is feasible.
- Clock-driven scheduling also has some disadvantages, such as:
  - It requires a priori knowledge of all task parameters and system workload.
  - It is not flexible to handle dynamic changes in task parameters or system workload.
  - It may waste processor utilization if the schedule is not fully packed.
  - It may not be scalable to handle a large number of tasks or complex task interactions.



# Weighted Round Robin Approach

- Weighted round robin is a generalisation of round-robin scheduling.
- It is used for scheduling real-time traffic in high-speed switched networks  .
- It builds on the basic round-robin scheme, which gives equal shares of the processor time to all the ready jobs.
- Rather than giving equal shares, weighted round robin gives different weights to different jobs, which serve to influence the portion of service time they receive  .
- The weight of a job can be determined by various factors, such as its priority, deadline, resource requirements, etc.
- The algorithm works as follows :
  - Assign a weight to each job in the ready queue.
  - Calculate the total weight of all the jobs in the ready queue.
  - Divide the time quantum by the total weight to get the unit time quantum.
  - For each job in the ready queue, multiply its weight by the unit time quantum to get its allocated time quantum.
  - Serve each job in the ready queue for its allocated time quantum, or until it finishes or blocks, whichever comes first.
  - Repeat the above steps until all the jobs are completed or the ready queue is empty.
- The advantages of weighted round robin are :
  - It is simple and easy to implement.
  - It can handle different types of jobs with different service requirements.
  - It can achieve a fair and proportional allocation of the processor time among the jobs.
  - It can reduce the response time and increase the throughput of the system.
- The disadvantages of weighted round robin are :
  - It may not be optimal for some jobs, especially those with strict deadlines or precedence constraints.
  - It may cause a high context-switching overhead if the time quantum is too small or the number of jobs is too large.
  - It may not be suitable for heterogeneous systems with different processor speeds or capacities.



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
- This approach can cause deadline misses and resource underutilization for real-time tasks.
- Priority-driven scheduling can overcome these limitations by giving higher priority to real-time tasks and preempting lower priority tasks when necessary.



# Dynamic Versus Static Systems

- A **dynamic system** is one that changes its behavior or configuration based on the current state, input, or environment. A **static system** is one that has a fixed or predetermined behavior or configuration regardless of the state, input, or environment.
- In the context of real-time scheduling, a **dynamic scheduler** is one that assigns priorities or resources to tasks at run-time, based on factors such as deadlines, arrival times, resource availability, etc. A **static scheduler** is one that assigns priorities or resources to tasks before run-time, based on factors such as worst-case execution times, periods, criticality, etc.
- Dynamic scheduling has the advantage of being more flexible and adaptive to changing workloads and unpredictable events, but it also has the disadvantage of being more complex, overhead-intensive, and difficult to verify or guarantee. Static scheduling has the advantage of being simpler, faster, and easier to verify or guarantee, but it also has the disadvantage of being less flexible and adaptive to changing workloads and unpredictable events.
- The choice of dynamic or static scheduling depends on the characteristics and requirements of the real-time system. For example, for hard real-time systems that have strict timing constraints and high predictability, static scheduling may be more suitable. For soft real-time systems that have relaxed timing constraints and low predictability, dynamic scheduling may be more suitable. For mixed-criticality systems that have both hard and soft real-time tasks, a combination of dynamic and static scheduling may be more suitable.
- Some examples of dynamic scheduling algorithms are earliest deadline first (EDF), least laxity first (LLF), rate-monotonic (RM), and earliest deadline until zero laxity (EDZL). Some examples of static scheduling algorithms are cyclic executive, time-triggered, and table-driven.



# Optimality of Effective-Deadline-First (EDF) and Least-Slack-Time-First (LST) Algorithms

- EDF and LST are two dynamic priority scheduling algorithms for real-time systems that assign priorities to tasks based on their deadlines and slacks, respectively.
- A deadline is the time by which a task must finish its execution, and a slack is the difference between the deadline and the remaining execution time of a task.
- EDF assigns the highest priority to the task with the earliest deadline, and LST assigns the highest priority to the task with the least slack.
- EDF and LST are optimal only when they always produce a feasible schedule if one exists, meaning that they can meet all the deadlines of the tasks in the system.
- EDF is optimal for preemptive scheduling of periodic and sporadic tasks with arbitrary deadlines, as long as the total utilization of the system is less than or equal to one.
- LST is optimal for preemptive scheduling of periodic and sporadic tasks with constrained deadlines, meaning that the deadline of each task is less than or equal to its period.
- EDF and LST may not be optimal for non-preemptive scheduling, aperiodic tasks, tasks with shared resources, or tasks with precedence constraints.
- EDF and LST may also under-utilize the CPU, meaning that they may leave some idle time when some tasks are not ready or have finished their execution.
- EDF and LST can be combined to enhance the performance of real-time task scheduling by switching between them according to the system load or the slack distribution of the tasks  .



# Rate Monotonic Algorithm

- Rate monotonic algorithm (RMA) is a priority assignment algorithm used in real-time operating systems with a static-priority scheduling class .
- The static priorities are assigned according to the cycle duration of the job, so that a shorter cycle duration results in a higher job priority .
- RMA is preemptive, meaning that a higher priority job can interrupt a lower priority job at any time.
- RMA is optimal for periodic tasks, meaning that it can schedule any set of periodic tasks that is feasible, i.e., that can be scheduled by any algorithm .
- RMA has a simple schedulability test, which is based on the utilization factor of the task set, defined as the sum of the ratios of execution time to period for each task .
- The schedulability test states that a set of periodic tasks is schedulable by RMA if the utilization factor is less than or equal to n(2^(1/n) - 1), where n is the number of tasks .
- RMA has some limitations, such as not being suitable for aperiodic or sporadic tasks, not considering deadlines or resource constraints, and not being optimal for multiprocessor systems .



# Offline Versus Online Scheduling

- Offline scheduling is a technique that makes use of pre-computed schedule of all hard real-time tasks, i.e., the schedule is computed at offline before the system begins to execute and the computation is based on the knowledge of release time, execution time, deadline, and resource requirement of all tasks for all time.
- Online scheduling is a technique that makes scheduling decisions during the run-time of the system, i.e., the scheduler does not have prior information about the tasks that will be released in the future and the parameters of each task are known to the scheduler only after the release of the task. Online scheduling can be either static or dynamic, depending on whether the scheduling decisions are fixed or can be changed during the execution of the tasks.
- The advantages of offline scheduling are that it can guarantee the schedulability of all tasks, it can optimize the resource utilization, and it can reduce the run-time overhead of the scheduler. The disadvantages of offline scheduling are that it requires complete and accurate knowledge of all task parameters, it cannot handle unpredictable events or changes in the system, and it may not be feasible for large or complex systems.
- The advantages of online scheduling are that it can handle dynamic and unpredictable situations, it can adapt to changes in the system or the environment, and it can be applied to a wide range of systems. The disadvantages of online scheduling are that it may not be able to guarantee the schedulability of all tasks, it may have higher run-time overhead and complexity, and it may not be able to optimize the resource utilization.
- The choice of offline or online scheduling depends on the characteristics and requirements of the system, such as the degree of predictability, the size and complexity, the performance and reliability, and the cost and feasibility. Some examples of systems that use offline scheduling are avionics systems, automotive systems, and robotic systems. Some examples of systems that use online scheduling are web servers, multimedia systems, and cloud computing systems.



# Scheduling Aperiodic and Sporadic jobs in Priority Driven and Clock Driven Systems

- Aperiodic jobs are jobs that have no fixed arrival pattern or inter-arrival time. They can arrive at any time and have soft deadlines or no deadlines at all. Examples are user requests, interrupts, etc.
- Sporadic jobs are jobs that have a minimum inter-arrival time between consecutive jobs, but no fixed arrival pattern. They have hard deadlines and must be completed before their deadlines. Examples are sensor readings, alarms, etc.
- Priority driven systems are systems that assign priorities to jobs based on some criteria, such as deadline, period, utilization, etc. The scheduler always selects the highest priority job to execute at any time. Examples are rate monotonic, earliest deadline first, etc.
- Clock driven systems are systems that assign fixed time slots to jobs based on their periods and deadlines. The scheduler follows a pre-computed schedule that is determined offline. Examples are cyclic executive, time triggered architecture, etc.

## Scheduling Aperiodic and Sporadic jobs in Priority Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in priority driven systems is to balance the responsiveness of aperiodic jobs and the schedulability of periodic and sporadic jobs. If aperiodic jobs are given high priority, they may interfere with the deadlines of periodic and sporadic jobs. If aperiodic jobs are given low priority, they may suffer from long response times.
- There are two main approaches to scheduling aperiodic and sporadic jobs in priority driven systems: background scheduling and server-based scheduling.
- Background scheduling is the simplest approach, where aperiodic jobs are given the lowest priority and execute only when no periodic or sporadic jobs are ready. This ensures that periodic and sporadic jobs meet their deadlines, but aperiodic jobs may have poor response times. This approach is suitable for soft aperiodic jobs that do not have strict timing requirements.
- Server-based scheduling is a more sophisticated approach, where aperiodic jobs are assigned to a special periodic task called a server. The server has a fixed priority, a period, and a budget. The server can execute aperiodic jobs up to its budget in each period. The server can also replenish its budget when it is idle or when it completes an aperiodic job. This allows aperiodic jobs to have higher priority than some periodic or sporadic jobs, and to have better response times. There are different types of servers, such as polling server, deferrable server, sporadic server, etc., that differ in how they manage their budgets and handle aperiodic arrivals.
- Sporadic jobs can be scheduled in priority driven systems by assigning them fixed priorities based on their periods or deadlines, and treating them as periodic jobs with jitter. Jitter is the maximum deviation of the actual arrival time from the expected arrival time of a job. Sporadic jobs can also be assigned to servers, but this may introduce additional overhead and complexity.

## Scheduling Aperiodic and Sporadic jobs in Clock Driven Systems

- The main challenge of scheduling aperiodic and sporadic jobs in clock driven systems is to handle the unpredictability of their arrival times and execution times. Clock driven systems assume that all jobs have fixed periods and deadlines, and that their execution times are known in advance. Aperiodic and sporadic jobs violate these assumptions, and may cause conflicts with the pre-computed schedule.
- There are two main approaches to scheduling aperiodic and sporadic jobs in clock driven systems: slack stealing and dynamic scheduling.
- Slack stealing is an approach where aperiodic and sporadic jobs are executed in the unused time slots of the pre-computed schedule. These time slots are called slack, and they are the difference between the worst-case execution time and the actual execution time of a job. Slack stealing algorithms try to find and use the available slack in the schedule to complete aperiodic and sporadic jobs as soon as possible. This approach requires online monitoring of the slack and offline analysis of the schedule feasibility.
- Dynamic scheduling is an approach where aperiodic and sporadic jobs are executed in the time slots of the pre-computed schedule that are allocated to periodic jobs. This requires modifying the schedule at runtime to accommodate the arrival and execution of aperiodic and sporadic jobs. Dynamic scheduling algorithms try to minimize the impact of the schedule modification on the periodic jobs, and to ensure that all jobs meet their deadlines. This approach requires online decision making and offline verification of the schedule correctness.



## Unit 3 - Resource Sharing

- Resource sharing is the process of making the resources of one computer system available to other computer systems on a network.
- Resource sharing can improve the efficiency, performance, reliability, and scalability of a distributed system by allowing multiple users and applications to access and utilize the same resources.
- Resource sharing can also enable collaboration, communication, and coordination among users and applications by allowing them to exchange data and information.
- Some examples of resources that can be shared on a network are:

  - Hardware resources, such as printers, scanners, disks, memory, CPU, etc.
  - Software resources, such as applications, databases, files, etc.
  - Data resources, such as documents, images, videos, etc.
  - Information resources, such as web pages, news, weather, etc.

- Resource sharing can be classified into two types:

  - Centralized resource sharing, where the resources are managed and controlled by a single server or a cluster of servers, and the clients access the resources through the server(s).
  - Distributed resource sharing, where the resources are distributed among multiple nodes or peers on the network, and the clients access the resources directly from the nodes or peers that have them.

- Resource sharing can be implemented using different techniques, such as:

  - File transfer, where the resource is copied from one node to another node on the network.
  - Remote access, where the resource is accessed from one node by another node on the network without copying it.
  - Remote execution, where the resource is executed on one node by another node on the network without transferring it.
  - Remote procedure call, where the resource is invoked as a procedure or a function on one node by another node on the network without transferring it.
  - Message passing, where the resource is exchanged as a message or a packet on the network between two or more nodes.
  - Publish/subscribe, where the resource is published by one or more nodes on the network and subscribed by one or more nodes on the network.
  - Peer-to-peer, where the resource is shared among equal nodes or peers on the network without any central server or authority.



# Effect of Resource Contention and Resource Access Control (RAC) for the notes of the Unit 3 - Resources Sharing in the subject of Real Time System

- Resource contention occurs when two or more tasks compete for the same resource, such as a processor, a memory, a device, or a communication channel.
- Resource contention affects the execution behavior and schedulability of tasks, as it may cause delays, blocking, priority inversion, timing anomalies, or deadlock  .
- Resource access control (RAC) is a set of rules that govern when and under what conditions each request for a resource is granted and how tasks requiring resources are scheduled .
- The main objective of RAC is to minimize the undesirable effects of resource contention and to ensure the correctness and timeliness of tasks .
- RAC can be classified into two categories: non-preemptive and preemptive .
  - Non-preemptive RAC means that a task that has acquired a resource cannot be preempted by another task until it releases the resource .
  - Preemptive RAC means that a task that has acquired a resource can be preempted by another task, but the resource is not released until the preempted task resumes and finishes its critical section .
- Some examples of RAC protocols are:
  - Non-preemptive protocols: Priority Ceiling Protocol (PCP), Stack Resource Policy (SRP), Priority Inheritance Protocol (PIP), etc .
  - Preemptive protocols: Multiprocessor Priority Ceiling Protocol (MPCP), Multiprocessor Stack Resource Policy (MSRP), Preemptive Priority Inheritance Protocol (PPIP), etc .
- The choice of RAC protocol depends on the characteristics of the system, such as the number of processors, the type of resources, the priority assignment, the task model, the schedulability analysis, etc .
- The performance of RAC protocols can be evaluated by metrics such as blocking time, response time, schedulability, utilization, overhead, etc .



Hello, I am Sydney, your AI assistant. I can help you with your query.

# Non-preemptive Critical Sections

- Non-preemptive critical sections are a way of controlling access to shared resources in real-time systems by scheduling all critical sections on the processor non-preemptively .
- A critical section is a code segment that accesses or modifies shared variables or resources that need to be synchronized to maintain the consistency of data variables .
- Non-preemptive means that once a job requests a resource, it is always allocated the resource, and no other job can interrupt or preempt it until it releases the resource  .
- When a job holds any resource, it executes at a priority higher than the priorities of all other jobs, regardless of their original priorities  .
- This protocol ensures mutual exclusion, deadlock-freedom, and bounded blocking time for all jobs .
- However, it also has some disadvantages, such as:
  - It may cause priority inversion, where a high-priority job is blocked by a low-priority job that holds a resource .
  - It may cause unnecessary blocking, where a job is blocked by another job that does not access the same resource .
  - It may cause long blocking time, where a job is blocked by another job that executes a long critical section .
  - It may cause low processor utilization, where a job that holds a resource does not use the processor effectively .
- Therefore, non-preemptive critical sections are only suitable for systems that have short and infrequent critical sections, and where the priority of jobs is not very important .



# Basic Priority-Inheritance and Priority-Ceiling Protocols

- Priority-Inheritance Protocol (PIP) and Priority-Ceiling Protocol (PCP) are two critical resource sharing protocols for real-time systems that aim to reduce the blocking time of high-priority tasks due to low-priority tasks holding shared resources .
- PIP works by temporarily elevating the priority of a low-priority task that holds a shared resource to the priority of the highest-priority task that is blocked by it . This way, the low-priority task can finish using the resource and release it to the high-priority task, avoiding priority inversion .
- PCP works by assigning a ceiling priority to each shared resource, which is the highest priority of any task that can access that resource  . A task can only lock a resource if its priority is higher than the ceiling priority of all the resources currently locked by other tasks  . This way, the protocol prevents deadlocks and ensures that a task can be blocked by at most one lower-priority task  .
- The main differences between PIP and PCP are  :
  - PIP is greedy while PCP is not. PIP allows a task to lock a resource whenever it is free, while PCP may deny a task from locking a resource even if it is free, depending on the ceiling priorities of other locked resources .
  - PIP requires minimum support from the operating system, while PCP requires maximum support from the operating system. PIP only needs to change the priority of a task when it locks or releases a resource, while PCP needs to keep track of the ceiling priorities of all the resources and compare them with the priorities of the tasks .
  - PIP cannot prevent deadlocks, while PCP can prevent deadlocks. PIP may cause a circular wait among tasks that request multiple resources, while PCP avoids such situations by enforcing a strict order of resource allocation based on the ceiling priorities .
  - PIP may cause unbounded priority inversion, while PCP can bound the priority inversion. PIP may allow a high-priority task to be blocked by a chain of lower-priority tasks that inherit the priority of each other, while PCP limits the blocking time of a high-priority task to the execution time of the lowest-priority task that can lock the highest-priority resource .



# Stack Based Priority-Ceiling Protocol

- Stack Based Priority-Ceiling Protocol (SBPCP) is a resource access control protocol for real-time systems that allows tasks to share a run-time stack and other resources .
- SBPCP is based on the Original Ceiling Priority Protocol (OCPP), which assigns a priority ceiling to each resource equal to the highest priority of any task that may lock the resource .
- SBPCP works by temporarily raising the priorities of tasks in certain situations, thus it requires a scheduler that supports dynamic priority scheduling .
- The rules of SBPCP are:
  - A task can lock a resource only if its current priority is higher than the current ceiling of the system, which is the highest priority ceiling of all the resources that are in use.
  - When a task locks a resource, its priority is raised to the priority ceiling of that resource, and the current ceiling of the system is also raised accordingly.
  - When a task unlocks a resource, its priority is restored to its original value, and the current ceiling of the system is lowered accordingly.
  - A task can preempt another task only if its current priority is higher than the current ceiling of the system.
- The advantages of SBPCP are :
  - It prevents priority inversion, deadlock, and chain blocking.
  - It has a bounded blocking time for each task, which is equal to the worst-case execution time of the critical sections of the lower priority tasks that share the same resources.
  - It reduces the number of context switches and stack operations compared to OCPP, since a task does not need to switch to a new stack when it locks a resource.
  - It allows tasks to share a run-time stack, which reduces the memory requirement and simplifies the stack management.



# Use of Priority-Ceiling Protocol in Dynamic Priority Systems

- Priority-ceiling protocol is a synchronization technique for preventing deadlock and unbounded priority inversion in real-time systems that share resources among tasks with different priorities.
- In a dynamic priority system, the priorities of the periodic tasks change with time while the resources required by each task remain constant .
- Hence, the priority ceilings of the resources may change with time as well .
- The priority ceiling of a resource is the highest priority of any task that can access that resource .
- The system ceiling is the highest priority ceiling of any resource currently locked by any task .
- A task can lock a resource only if its priority is higher than the system ceiling .
- This ensures that a higher priority task will not be blocked by a lower priority task that holds a resource .
- For dynamic systems, we can use the priority ceiling protocol to control resource accesses provided we update the priority ceiling of each resource and the system ceiling each time task priorities change .
- This can be done by using a table that stores the priority ceilings of each resource for each possible priority level of the tasks .
- For example, consider a system with two tasks T1 (2, 0.9) and T2 (5, 2.3) executed in a deadline driven system as below :

| Time | T1 | T2 | Priority |
|------|----|----|----------|
| 0    | R  |    | 1        |
| 1    | R  |    | 1        |
| 2    |    | R  | 2        |
| 3    |    | R  | 2        |
| 4    | R  |    | 2        |
| 5    | R  |    | 2        |
| 6    |    | R  | 1        |
| 7    |    | R  | 1        |
| 8    | R  |    | 1        |
| 9    | R  |    | 1        |

- Assume that both tasks share a resource X that is initially unlocked. The priority ceiling of X is 1 from time 0 to 4 and becomes 2 from time 4 to 5 and so on .
- The table below shows the priority ceilings of X for each priority level of the tasks :

| Priority | Priority Ceiling of X |
|----------|-----------------------|
| 1        | 1                     |
| 2        | 2                     |

- The priority ceiling protocol works as follows :
  - At time 0, T1 locks X and executes. The system ceiling becomes 1.
  - At time 2, T2 preempts T1 and executes. The system ceiling remains 1.
  - At time 4, T1 preempts T2 and executes. The system ceiling becomes 2.
  - At time 6, T2 preempts T1 and executes. The system ceiling becomes 1.
  - At time 8, T1 preempts T2 and executes. The system ceiling remains 1.
  - At time 10, T1 unlocks X and finishes. The system ceiling becomes 0.
  - At time 11, T2 resumes and finishes.

- The priority ceiling protocol ensures that no deadlock or unbounded priority inversion occurs in the system .



# Preemption Ceiling Protocol

- Preemption ceiling protocol is a synchronization protocol for shared resources to avoid unbounded priority inversion and mutual deadlock due to wrong nesting of critical sections.
- Priority inversion occurs when a high-priority task is blocked by a low-priority task that holds a shared resource, and the low-priority task is preempted by a medium-priority task.
- Mutual deadlock occurs when two or more tasks hold some resources and request for other resources held by each other, forming a circular wait.
- Preemption ceiling protocol assigns a ceiling priority to each resource, which is the highest priority of any task that can access that resource.
- A task can lock a resource only if its priority is higher than the ceiling priority of all the resources currently locked by other tasks.
- When a task locks a resource, its priority is raised to the ceiling priority of that resource, and it cannot be preempted by any other task until it releases the resource.
- There are two variants of preemption ceiling protocol: static and dynamic.
- Static preemption ceiling protocol assigns the ceiling priority of each resource at design time, based on the worst-case scenario.
- Dynamic preemption ceiling protocol assigns the ceiling priority of each resource at run time, based on the current priority of the task that requests the resource.
- Preemption ceiling protocol can be integrated with preemption threshold scheduling (PTS), which is a fixed-priority scheduling scheme that allows a task to specify a preemption threshold, below which it cannot be preempted by higher-priority tasks.
- PTS can reduce the number of context switches, increase the schedulability, and decrease the memory requirements of real-time systems.
- However, PTS may lead to long priority inversion if not combined with a synchronization protocol, such as preemption ceiling protocol.
- Preemption ceiling protocol can also be extended to support object-oriented real-time systems, which require synchronization considerations to maintain consistent object states.
- Dual ceiling protocol is an example of such an extension, which assigns two ceiling priorities to each object: one for read operations and one for write operations.




# Access Control in Multiple-Unit Resources

- Multiple-unit resources are resources that can be used by more than one job at a time, such as memory, disk, or network bandwidth.
- Each unit of a multiple-unit resource is used in a non-preemptive and mutually exclusive manner; resources are serially reusable  .
- Access to multiple-unit resources is controlled using locks. Jobs attempt to lock a resource before starting to use it, and unlock the resource afterwards; the time the resource is locked is the critical section  .
- The challenge of access control in multiple-unit resources is to avoid deadlock and priority inversion, while ensuring schedulability and resource utilization.
- Some of the protocols for access control in multiple-unit resources are:
  - Highest Locker Protocol (HLP): A job can lock a resource only if its priority is higher than or equal to the highest priority of any job holding any unit of the resource.
  - Maximum Urgency First (MUF): A job can lock a resource only if its urgency (a function of its deadline and priority) is higher than or equal to the maximum urgency of any job holding any unit of the resource.
  - Priority Inheritance Protocol (PIP): A job that holds a resource inherits the priority of the highest-priority job that is blocked on that resource; when the resource is released, the original priority is restored .
  - Priority Ceiling Protocol (PCP): A job can lock a resource only if its priority is higher than the priority ceiling of the resource, which is the highest priority of any job that may request the resource; a job that holds a resource inherits the priority ceiling of the resource .
  - Preemption Ceiling Protocol (PrCP): A job can lock a resource only if its priority is higher than the preemption ceiling of the resource, which is the highest priority of any job that may request the resource; a job that holds a resource is scheduled with the preemption ceiling of the resource in a non-preemptable manner .



# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts from occurring by locking data objects before accessing them. They require a priori knowledge of the data access patterns of the jobs and may cause blocking or priority inversion.
  - Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting some jobs. They do not require a priori knowledge of the data access patterns of the jobs and may cause wasted computation or deadline misses.
- Some examples of pessimistic algorithms are:
  - Priority inheritance protocol: When a job is blocked by a lower priority job that holds a lock on a data object, the lower priority job inherits the priority of the blocked job until it releases the lock. This reduces the blocking time and the priority inversion problem.
  - Priority ceiling protocol: Each data object is assigned a priority ceiling, which is the highest priority of any job that may access it. A job can lock a data object only if its priority is higher than the current priority ceiling of the system, which is the maximum of the priority ceilings of all the locked data objects. This prevents deadlock and reduces the blocking time and the priority inversion problem.
  - Convex ceiling protocol: Each data object is assigned a convex ceiling, which is a function of the priority of the job that locks it. A job can lock a data object only if its priority is higher than the current convex ceiling of the system, which is the maximum of the convex ceilings of all the locked data objects. This allows more concurrency and flexibility than the priority ceiling protocol.
- Some examples of optimistic algorithms are:
  - Wait-free algorithm: Each job has a private copy of the data objects it accesses and updates them locally. When a job commits, it compares its local copies with the global copies and aborts if there is a conflict. This ensures that each job can complete without waiting for other jobs, but may cause a high abort rate and wasted computation.
  - Timestamp ordering algorithm: Each job is assigned a timestamp based on its deadline or arrival time. A job can access a data object only if its timestamp is smaller than the timestamp of the last job that accessed the same data object. This ensures that the jobs are executed in a serializable order, but may cause a high abort rate and deadline misses.



## Unit 4 - Real Time Communication

- Real time communication (RTC) is the exchange of information between two or more parties without significant delay.
- RTC can be synchronous or asynchronous, depending on the degree of coordination and synchronization required by the communication scenario.
- Synchronous RTC is when the parties communicate at the same time, such as in a phone call, a video conference, or a chat session.
- Asynchronous RTC is when the parties communicate at different times, such as in an email, a voice message, or a forum post.
- RTC can be one-to-one, one-to-many, or many-to-many, depending on the number and role of the participants.
- One-to-one RTC is when two parties communicate directly with each other, such as in a private chat or a phone call.
- One-to-many RTC is when one party communicates with multiple parties, such as in a broadcast, a webinar, or a lecture.
- Many-to-many RTC is when multiple parties communicate with each other, such as in a group chat, a video conference, or a multiplayer game.
- RTC can be text-based, voice-based, video-based, or a combination of these, depending on the type and quality of the information exchanged.
- Text-based RTC is when the parties communicate using written words, such as in a chat, an email, or a forum.
- Voice-based RTC is when the parties communicate using spoken words, such as in a phone call, a voice message, or a podcast.
- Video-based RTC is when the parties communicate using visual images, such as in a video call, a video message, or a live stream.
- RTC can be facilitated by various technologies, platforms, and protocols, depending on the requirements and preferences of the parties involved.
- Some examples of RTC technologies are: telephones, radios, televisions, computers, smartphones, tablets, smartwatches, webcams, microphones, speakers, headphones, etc.
- Some examples of RTC platforms are: Skype, Zoom, WhatsApp, Telegram, Discord, Slack, Facebook, Twitter, Instagram, YouTube, Twitch, etc.
- Some examples of RTC protocols are: Session Initiation Protocol (SIP), Real-time Transport Protocol (RTP), Web Real-Time Communication (WebRTC), etc.
- RTC can have various benefits and challenges, depending on the context and purpose of the communication.
- Some benefits of RTC are: immediacy, interactivity, engagement, feedback, collaboration, social presence, etc.
- Some challenges of RTC are: latency, bandwidth, reliability, security, privacy, etiquette, etc.



# Basic Concepts in Real Time Communication

Real time communication (RTC) is any mode of telecommunications in which all users can exchange information instantly or with negligible latency or transmission delays . In this context, the term real time is synonymous with live. In RTC, there is always a direct path between the source and the destination.

Some examples of real time communication are:

- Voice over landlines and mobile phones
- Video conferencing and webinars
- Online chat and instant messaging
- Online gaming and virtual reality
- Streaming media and live broadcasting

Some basic concepts in real time communication are:

- Bandwidth: The amount of data that can be transmitted or received per unit of time. Bandwidth affects the quality and speed of RTC.
- Latency: The time it takes for a signal to travel from the source to the destination. Latency affects the responsiveness and synchronicity of RTC.
- Jitter: The variation in latency caused by network congestion, interference, or other factors. Jitter affects the smoothness and stability of RTC.
- Packet loss: The loss of data packets during transmission due to network errors, congestion, or other factors. Packet loss affects the reliability and completeness of RTC.
- Encoding and decoding: The process of converting analog signals (such as sound or video) into digital data (such as bits or bytes) and vice versa. Encoding and decoding affect the compatibility and efficiency of RTC.
- Compression and decompression: The process of reducing the size of data by removing redundant or irrelevant information and restoring it to its original form. Compression and decompression affect the bandwidth and quality of RTC.
- Encryption and decryption: The process of securing data by transforming it into an unreadable form and restoring it to its original form. Encryption and decryption affect the privacy and security of RTC.
- Synchronization: The process of aligning the timing and order of data streams from different sources. Synchronization affects the coherence and consistency of RTC.
- Feedback: The process of sending and receiving signals that indicate the status or quality of RTC. Feedback affects the adjustment and improvement of RTC.
- Protocols: The rules and standards that govern the format, exchange, and behavior of data in RTC. Protocols affect the interoperability and functionality of RTC.

Some examples of protocols used in RTC are:

- Real-time Transport Protocol (RTP): A protocol that provides end-to-end delivery of audio and video data over IP networks.
- Real-time Transport Control Protocol (RTCP): A protocol that provides feedback and control information for RTP streams.
- Session Initiation Protocol (SIP): A protocol that establishes, modifies, and terminates multimedia sessions over IP networks.
- Web Real-Time Communication (WebRTC): A set of technologies that enable browser-based RTC applications without plugins or downloads.



# Soft and Hard Real-Time Communication Systems

- Real-time communication systems are systems that exchange information between two or more entities within a specified time bound.
- Real-time communication systems are generally understood as one of two types: Hard Real-Time (HRT) and Soft Real-Time (SRT) .
- The difference between a hard and soft real-time communication system is the consequences of incorrect operation .
- Hard real-time systems are deterministic in nature while soft real-time systems are probabilistic .
- Hard real-time systems have strict deadlines that must be met, otherwise the system may fail or cause severe damage  .
- Examples of hard real-time systems are nuclear power plants, air traffic control systems, and pacemakers  .
- Soft real-time systems have deadlines that can be missed occasionally with low probability, without compromising the system functionality or performance  .
- Examples of soft real-time systems are multimedia applications, online gaming, and video conferencing  .
- Hard real-time systems require specialized hardware and software that can guarantee the timing constraints and handle the worst-case scenarios  .
- Soft real-time systems can use general-purpose hardware and software that can optimize the average-case performance and tolerate some delays or errors  .
- Hard real-time systems are more complex and costly to design, implement, and maintain than soft real-time systems  .
- Soft real-time systems are more flexible and scalable than hard real-time systems  .
- Hard real-time systems have higher reliability and safety requirements than soft real-time systems  .
- Soft real-time systems have higher user satisfaction and quality of service requirements than hard real-time systems  .
- Hard and soft real-time systems have different trade-offs and challenges that need to be considered when developing real-time communication systems  .



# Model of Real Time Communication

- Real time communication (RTC) is any live telecommunications method in which all users can interact in a live capacity, with negligible latency  .
- RTC can involve different types of media, such as voice, video, text, images, etc.
- RTC can be implemented using different technologies, such as landlines, mobile phones, VoIP, WebRTC, etc.
- RTC can be used for various applications, such as online gaming, video conferencing, telemedicine, social media, etc.
- RTC can be modeled using different parameters, such as traffic, throughput, delay, jitter, etc.

## Real Time Traffic Model

- The real time traffic means isochronous or synchronous traffic, consisting stream of message that are generated by their sources and delivered to their respective destination on continuous basis.
- The traffic includes the periodic, aperiodic and sporadic messages.
- Periodic messages are generated at regular intervals, such as sensor data, audio samples, etc.
- Aperiodic messages are generated at irregular intervals, such as alarms, events, etc.
- Sporadic messages are generated at random intervals, such as user inputs, commands, etc.
- In real time traffic model, each message (Mi) can be characterized by tuples of inter-packet spacing (Pi), message length (ei), reception deadline (Di) as below.
- Mi = (pi, ei, Di)
- This traffic model is called peak rate model in real time communication.

## Throughput, Delay and Jitter

- Throughput is the amount of data that can be transmitted or received per unit time in a communication channel.
- Throughput can be affected by factors such as bandwidth, congestion, errors, etc.
- Delay is the time taken for a message to travel from the source to the destination in a communication channel.
- Delay can be affected by factors such as propagation, transmission, processing, queuing, etc.
- Jitter is the variation in delay for a sequence of messages in a communication channel.
- Jitter can be affected by factors such as network load, routing, buffering, etc.
- Throughput, delay and jitter are important metrics for evaluating the performance and quality of service (QoS) of real time communication.



# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) is a simple and fair priority-based service discipline that assigns a weight to each queue and serves them in a circular order, proportional to their weights.
- WRR does not require a sorted priority queue, only a round-robin queue. It can guarantee the minimum bandwidth for each queue and avoid starvation of low-priority queues.
- However, WRR does not provide delay and jitter guarantees for real-time packets, as it does not consider the packet arrival times or deadlines.
- To overcome this limitation, some variations of WRR have been proposed, such as:
  - Rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server. The rate controller adjusts the weights of the queues according to their delay requirements, and the frame-based WRR server serves the packets within a fixed frame size. This way, RFWRR can provide delay jitter bounds and satisfy diverse delay requirements for different queues.
  - Probabilistic priority (PP), which is based on the strict priority (SP) discipline with the difference that each priority queue is assigned a parameter as in weighted fair queueing (WFQ). The parameter determines the probability with which its corresponding queue is served when it is polled by the server. This way, PP can balance the trade-off between priority and fairness, and avoid the head-of-line blocking problem of SP.
  - Class-based weighted fair queueing (CBWFQ) and weighted fair priority queueing (WFPQ), which are extensions of WFQ that support multiple classes of service. CBWFQ assigns a weight to each class and allocates the bandwidth proportionally among the classes. WFPQ assigns a priority level to each class and serves the highest-priority class first, while applying WFQ within each class. These techniques can provide both bandwidth and delay guarantees for different classes of packets.



# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast network.
- Broadcast networks are networks where a single transmission can reach all the nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks need to deal with the challenges of interference, collisions, hidden terminals, and fairness.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to decide which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but suffer from low efficiency and high collision probability.
- Deterministic contention protocols use a predefined order or priority to decide which node will transmit next, such as TDMA or token passing. These protocols are efficient and fair, but require synchronization and coordination among nodes, and are not adaptive to traffic changes or node failures.
- Reservation-based protocols use a combination of contention and reservation to allocate slots for transmission, such as ABROAD or PRMA. These protocols can provide performance guarantees and adaptivity, but require more overhead and complexity than pure contention protocols.



# Internet and Resource Reservation Protocols

- Internet is a global network of interconnected devices that communicate using standard protocols such as TCP/IP and HTTP.
- Internet applications have different network performance requirements, such as reliability, timeliness, bandwidth, and jitter.
- Resource Reservation Protocol (RSVP) is a network control protocol that enables Internet applications to obtain specific qualities of service (QoS) for their data flows or streams.
- RSVP operates over IPv4 or IPv6 and supports both multicast and unicast data flows.
- RSVP is receiver-initiated, meaning that the receiver of a data flow requests a certain QoS from the network by sending RSVP messages along the reverse path of the data flow.
- RSVP messages include PATH and RESV messages, which are used to establish and maintain resource reservations along the data path.
- PATH messages are sent by the sender of a data flow and carry information about the sender, the data flow characteristics, and the QoS requirements.
- RESV messages are sent by the receiver of a data flow and carry information about the desired QoS and the reservation style.
- Reservation styles specify how the resources are shared among the receivers of a multicast data flow. There are three main reservation styles: Fixed-Filter (FF), Shared-Explicit (SE), and Wildcard-Filter (WF).
- FF style reserves resources for each sender-receiver pair separately, and requires the receiver to specify the sender's address in the RESV message.
- SE style reserves resources for a group of senders that are explicitly listed by the receiver in the RESV message, and allows the receiver to share the resources among the senders.
- WF style reserves resources for any sender of the data flow, and does not require the receiver to specify the sender's address in the RESV message.
- RSVP also uses other messages, such as CONFIRM, TEAR, and ERROR, to confirm, tear down, or report errors in the resource reservations.
- RSVP is not a routing protocol, but it works with routing protocols to determine the data path and the reverse path. RSVP can also work with traffic control mechanisms, such as admission control, packet classification, packet scheduling, and policing, to enforce the QoS guarantees.
- RSVP is designed to be scalable, robust, and flexible. It can handle dynamic changes in the network topology, the data flows, and the QoS requirements. It can also support different QoS models, such as IntServ and DiffServ.



# Unit 5 - Real Time Operating Systems and Databases

- A **real-time operating system (RTOS)** is an operating system that can handle data and events that have strict time constraints, such as industrial control, flight control, and real-time simulations .
- An RTOS provides features such as real-time multithreading, inter-thread communication and synchronization, and memory management.
- An RTOS is different from a time-sharing operating system, such as Unix, which manages the sharing of system resources with a scheduler, data buffers, or fixed task priorities.
- An RTOS typically has a deterministic response time, meaning that it can guarantee that a task will be completed within a specified time limit.
- A **real-time database** is a database system that can handle data workloads that are in constant flux and are extremely time-sensitive, such as sensor data, stock market data, and online gaming data.
- A real-time database provides features such as concurrency control, data consistency, data freshness, and data recovery.
- A real-time database is different from a time-series database, which is a database system that can store and analyze data that has a temporal dimension, such as weather data, web analytics data, and IoT data.
- A real-time database is also different from a real-time analytics system, which is a system that can process and visualize data in real-time, such as dashboards, alerts, and recommendations.
- A real-time database can be based on SQL or NoSQL, depending on the data model, query language, and scalability requirements of the application.
- A real-time database can be integrated with an RTOS to enable real-time data processing and decision making for embedded applications.



# Features of RTOS

A real-time operating system (RTOS) is an operating system that can guarantee a certain level of performance and reliability for time-critical applications. An RTOS has two key features: predictability and determinism. Predictability means that the RTOS can respond to events within a known and bounded time frame, regardless of the system load. Determinism means that the RTOS can execute tasks in a consistent and predefined order, without any unexpected delays or interruptions.

Some of the features and advantages of an RTOS are  :

- **Small and fast**: An RTOS is designed to occupy very less memory and consume fewer resources, as it has to run on embedded devices with limited hardware capabilities. An RTOS is also optimized for speed and efficiency, as it has to meet strict deadlines and handle high-priority tasks.
- **Responsive**: An RTOS can react to external events or interrupts quickly and reliably, as it has to deal with real-time situations and avoid missing deadlines. An RTOS can also preempt lower-priority tasks to give way to higher-priority ones, ensuring that the most urgent tasks are completed first.
- **Scalable and modular**: An RTOS can be customized and configured to suit different applications and requirements, as it has to support a variety of devices and platforms. An RTOS can also be modular, meaning that it can be composed of different components or services that can be added or removed as needed, without affecting the core functionality of the system.
- **Secure and reliable**: An RTOS can provide security and reliability features, such as memory protection, fault tolerance, error detection and correction, and data encryption, to ensure the integrity and safety of the system and the data. An RTOS can also handle failures and exceptions gracefully, without compromising the performance or functionality of the system.

Some of the challenges and limitations of an RTOS are :

- **Complexity and cost**: An RTOS can be complex and costly to develop, test, and maintain, as it has to meet high standards of quality and performance. An RTOS can also require specialized skills and tools to implement and debug, as it has to deal with low-level hardware and software issues.
- **Compatibility and interoperability**: An RTOS can face compatibility and interoperability issues, as it has to work with different devices, protocols, and standards. An RTOS can also have limited support and compatibility for third-party software and libraries, as it has to ensure that they do not interfere with the real-time behavior of the system.
- **Flexibility and adaptability**: An RTOS can be less flexible and adaptable than a general-purpose operating system, as it has to follow strict rules and constraints to ensure real-time performance. An RTOS can also have difficulty in adding new features or functionalities to the system, as it has to ensure that they do not affect the existing performance or functionality of the system.



# Time Services for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Time services are the functions and mechanisms that provide the ability to measure, represent, and manipulate time in real-time systems.
- Time services are essential for real-time systems because they enable the following features :
  - Timeliness: the ability to produce the expected result within a defined deadline.
  - Time synchronization: the ability to coordinate independent clocks and operate together in unison.
  - Time representation: the ability to store and manipulate time values in a consistent and accurate way.
  - Time measurement: the ability to obtain and compare time values from different sources and devices.
  - Time management: the ability to schedule and execute tasks and events based on time constraints and priorities.
- Time services can be implemented in hardware and software, or a combination of both. Some examples of hardware and software components that provide time services are:
  - Clocks: devices that generate periodic signals and count the number of cycles to measure time intervals.
  - Timers: devices that generate interrupts or signals after a specified time interval or at a specified time point.
  - Synchronization protocols: algorithms that adjust the clocks of different devices to achieve a common notion of time.
  - Time libraries: software modules that provide functions and data structures to represent and manipulate time values.
  - Real-time operating systems (RTOS): software platforms that provide mechanisms to schedule and execute tasks and events based on time constraints and priorities.
  - Real-time databases: software systems that store and retrieve data with time-related properties and guarantees.
- Time services can be classified into two categories based on the type of deadlines they support:
  - Hard real-time: time services that have absolute deadlines, and if those allotted time spans are missed, a system failure will occur.
  - Soft real-time: time services that have relative deadlines, and if those allotted time spans are missed, a system degradation will occur.



# UNIX as RTOS

- A real-time operating system (RTOS) is an operating system (OS) for real-time computing applications that processes data and events that have critically defined time constraints.
- An RTOS is distinct from a time-sharing operating system, such as UNIX, which manages the sharing of system resources with a scheduler, data buffers, or fixed task prioritization in a multitasking or multiprogramming environment.
- While a time-sharing OS like UNIX strives to provide good average performance, for a RTOS, correct timing is the key feature.
- UNIX is not a RTOS by default, but it can be modified or extended to support some real-time features, such as:
  - Preemptive scheduling: the ability to interrupt a running task and switch to a higher priority one.
  - Priority inheritance: the mechanism to avoid priority inversion, where a low priority task blocks a high priority one.
  - Real-time signals: the signals that are delivered to a process immediately, without being queued.
  - POSIX real-time extensions: the set of standards that define interfaces and behavior for real-time applications on UNIX-like systems.
- Some examples of UNIX-like systems that have been used or adapted as RTOSs are:
  - Linux: an open source OS that can be configured with real-time patches or kernels, such as PREEMPT_RT or Xenomai, to improve its real-time performance .
  - QNX: a commercial OS that is based on a microkernel architecture and supports POSIX real-time extensions, message passing, and fault tolerance.
  - Solaris: an OS developed by Sun Microsystems (now Oracle) that supports real-time scheduling, priority inheritance, and real-time signals.
- The advantages of using UNIX as a RTOS are:
  - Familiarity: many developers are familiar with UNIX and its tools, libraries, and applications, which can reduce the learning curve and development time.
  - Portability: UNIX can run on various hardware platforms and architectures, which can increase the compatibility and interoperability of real-time applications.
  - Flexibility: UNIX can be customized and modified to suit different real-time requirements and scenarios, such as hard or soft real-time, embedded or distributed systems, etc.
- The disadvantages of using UNIX as a RTOS are:
  - Overhead: UNIX has many features and services that are not necessary or desirable for real-time applications, such as memory management, file systems, networking, etc., which can introduce overhead and latency.
  - Complexity: UNIX is a complex OS that can have many sources of unpredictability and variability, such as interrupts, exceptions, system calls, etc., which can affect the real-time performance and reliability.
  - Compatibility: UNIX may not comply with some real-time standards or specifications, such as ARINC 653 or IEC 61508, which can limit its applicability and acceptance in some domains or industries.



# POSIX Issues for Real Time Operating Systems

- POSIX stands for Portable Operating System Interface, and it is a set of standards that define how an application can interact with an operating system.
- POSIX was originally designed for UNIX systems, but it has been extended to cover other operating systems, including real-time operating systems (RTOS).
- RTOS are operating systems that provide predictable and timely responses to events, such as sensor inputs, user commands, or network messages.
- RTOS are often used in embedded systems, such as industrial control, robotics, or aerospace applications, where reliability, performance, and safety are critical.
- POSIX issues for RTOS include the following:

  - POSIX.1 defines the basic operating system services, such as file operations, process management, signals, and devices. However, POSIX.1 does not address the specific needs of real-time applications, such as priority scheduling, timers, synchronization, or memory management.
  - POSIX.4 defines the real-time extensions to POSIX.1, such as priority inheritance, high-resolution timers, asynchronous I/O, message queues, and semaphores. However, POSIX.4 does not cover all the aspects of real-time systems, such as deadline scheduling, resource reservation, or fault tolerance.
  - POSIX.13 defines the application environment profile for real-time systems, such as the minimum set of features and functions that a POSIX-compliant RTOS must provide. However, POSIX.13 does not specify the performance or quality of service guarantees that a RTOS must offer, such as the maximum latency, jitter, or throughput.
  - POSIX.26 defines the real-time trace and debug extensions to POSIX.1, such as the mechanisms for recording, analyzing, and controlling the execution of real-time applications. However, POSIX.26 does not address the challenges of debugging concurrent, distributed, or adaptive real-time systems, such as the consistency, scalability, or security issues.

- POSIX issues for RTOS are important because they affect the portability, interoperability, and compatibility of real-time applications across different platforms and environments.
- POSIX issues for RTOS are also challenging because they require balancing the trade-offs between standardization, flexibility, and performance, as well as addressing the diversity and complexity of real-time systems and applications.



# Characteristic of Temporal Data

- Temporal data is the data that is valid only for a prescribed time and becomes invalid or obsolete after a certain period of time.
- Temporal data can represent time in different forms, such as dates, intervals, durations, or events, and allow other data to be placed in a chronological sequence or to be analyzed chronologically.
- Temporal data can be collected from various sources, such as manual data entry, observational sensors, simulation models, or historical records.
- Temporal data can have different aspects, such as valid time, transaction time, or decision time.
  - Valid time is the time period during or event time at which a fact is true in the real world.
  - Transaction time is the time at which a fact was recorded in the database.
  - Decision time is the time at which a fact was decided or acted upon by an agent.
- Temporal data can be used for various purposes, such as analyzing weather patterns, monitoring traffic conditions, studying demographic trends, tracking changes in data, or supporting temporal queries and reasoning .



# Temporal Consistency

- Temporal consistency is a property of real-time systems that ensures that the data stored in the database reflects the current state of the physical environment.
- Temporal consistency is different from logical consistency, which is a property of conventional database systems that ensures that the data stored in the database satisfies the integrity constraints and the transaction isolation levels.
- Temporal consistency is important for real-time systems because they need to use accurate and up-to-date data to perform time-critical tasks and to control the physical environment.
- Temporal consistency can be violated if the data stored in the database becomes stale or outdated due to the changes in the physical environment or the delays in the data acquisition and update processes.
- Temporal consistency can be measured by the temporal error, which is the difference between the actual value of the data in the physical environment and the value of the data stored in the database.
- Temporal consistency can be maintained by using various techniques, such as:
  - Triggered updates, which are updates that are initiated by the data sources whenever the data changes in the physical environment.
  - Periodic updates, which are updates that are performed at regular intervals by the data sources or the database system.
  - Temporal validity, which is a property of the data that specifies the maximum duration for which the data can be used without violating the temporal consistency.
  - Temporal freshness, which is a property of the data that specifies the maximum age of the data that can be used without violating the temporal consistency.
  - Temporal constraints, which are constraints that specify the deadlines or the maximum response times for the transactions that access or update the data.
  - Temporal isolation, which is a property of the concurrency control algorithms that ensures that the transactions do not interfere with each other's temporal consistency.
  - Temporal caching, which is a technique that uses local copies of the data to reduce the access time and the network traffic.



# Concurrency Control

Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other. It ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the database.

## Concurrency Control in Real-Time Database

A real-time database is a database that supports applications that have timing constraints on their data and transactions. For example, a real-time database may be used for air traffic control, industrial automation, or online gaming. A real-time database must provide timely and consistent data access to meet the deadlines and quality of service requirements of the real-time applications.

Concurrency control in real-time database is about ensuring non-interference among transactions by restricting concurrent transactions to be serializable. A concurrent execution of a set of transactions is said to be serializable if and only if the database operations carried out by them is equivalent to some serial execution of these transactions.

However, serializability alone is not sufficient for real-time database, as it does not consider the timing constraints of the transactions. A real-time database must also ensure that transactions meet their deadlines, which may be hard or soft. A hard deadline is a deadline that must be met by the transaction, otherwise the system may fail or cause serious consequences. A soft deadline is a deadline that can be missed by the transaction, but the system performance or quality may degrade.

Therefore, concurrency control in real-time database must balance between data consistency and timing constraints, and adapt to the changes in the operating environment and the workload. Some of the challenges and issues in concurrency control in real-time database are:

- How to assign priorities to transactions based on their deadlines, importance, and resource requirements?
- How to resolve conflicts among transactions that access the same data items in read or write mode?
- How to handle transactions that miss their deadlines or abort due to concurrency control or other reasons?
- How to cope with data freshness and temporal consistency, which means that the data accessed by the transactions should reflect the current state of the real world?
- How to deal with distributed and decomposable transactions that span across multiple nodes or subtransactions ?

## Concurrency Control Protocols for Real-Time Database

There are various concurrency control protocols that have been proposed for real-time database, which can be classified into two main categories: lock-based protocols and timestamp-based protocols.

### Lock-Based Protocols

Lock-based protocols use locks to control the access to data items by transactions. A lock is a mechanism that grants exclusive or shared access to a data item to a transaction. A transaction must acquire a lock on a data item before reading or writing it, and release the lock after finishing the operation. A lock can be either exclusive or shared. An exclusive lock allows only one transaction to access the data item in write mode, while a shared lock allows multiple transactions to access the data item in read mode. A conflict occurs when two transactions try to acquire incompatible locks on the same data item, such as an exclusive lock and a shared lock, or two exclusive locks. A conflict resolution policy is used to decide which transaction should get the lock and which transaction should wait or abort.

Some of the lock-based protocols for real-time database are:

- Two-Phase Locking (2PL): This is a basic lock-based protocol that requires a transaction to acquire all the locks it needs before releasing any lock. This ensures serializability, but may cause deadlock, which is a situation where two or more transactions are waiting for each other to release locks. Deadlock can be prevented or detected and resolved by using timeouts, deadlock prevention algorithms, or deadlock detection algorithms.
- Priority Ceiling Protocol (PCP): This is a lock-based protocol that assigns a priority ceiling to each data item, which is the highest priority of any transaction that may lock the data item. A transaction can lock a data item only if its priority is higher than the priority ceiling of all the data items currently locked by other transactions. This prevents deadlock and ensures that higher priority transactions are not blocked by lower priority transactions. However, it may cause priority inversion, which is a situation where a higher priority transaction is blocked by a lower priority transaction that holds a lock on a data item needed by the higher priority transaction.
- Wait-Free Priority Ceiling Protocol (WFPCP): This is a lock-based protocol that extends PCP by allowing a transaction to abort and restart another transaction that holds a lock on a data item needed by the former transaction, if the latter transaction has a lower priority and a later deadline than the former transaction. This avoids priority inversion and ensures that transactions meet their



# Overview of Commercial Real Time Databases

- A real-time database is a database system that uses real-time processing to handle workloads whose state is constantly changing.
- Real-time databases are useful for accounting, banking, law, medical records, multi-media, process control, reservation systems, and scientific data analysis.
- Real-time databases can be classified into two types: hard real-time and soft real-time.
  - Hard real-time databases have strict timing constraints and must guarantee that transactions are completed within their deadlines, otherwise the system may fail or cause severe consequences.
  - Soft real-time databases have more relaxed timing constraints and can tolerate some degree of deadline misses, but still aim to optimize the performance and quality of service of the system.
- Some of the attributes of live real-time databases are:
  - Concurrency control: the ability to handle multiple transactions accessing the same data without compromising data integrity or consistency.
  - Data freshness: the degree to which the data reflects the current state of the real world.
  - Data distribution: the ability to store and access data across multiple nodes or locations for scalability, availability, and fault tolerance.
  - Data replication: the ability to create and maintain copies of data on different nodes or locations for backup, load balancing, or performance enhancement.
  - Data security: the ability to protect data from unauthorized access, modification, or deletion.
  - Data recovery: the ability to restore data to a consistent state after a failure or error.
  - Data analysis: the ability to process and extract useful information from data for decision making or reporting.
  - Data visualization: the ability to present data in a graphical or interactive way for better understanding or communication.
- Some of the examples of commercial real-time databases are :
  - Altus Group: a commercial real estate database that provides historical and current data on properties, transactions, markets, and trends.
  - CoStar: a commercial real estate database that offers comprehensive data on properties, tenants, leases, sales, and analytics.
  - Google Cloud Firestore: a fully managed NoSQL database service that supports real-time data synchronization, offline access, and scalability.
  - Google Cloud Bigtable: a highly performant, fully managed NoSQL database service that supports large analytical and operational workloads.

